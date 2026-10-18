#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use orbit_core::{catalog, Cancellation, Engines, Receipt, Request};
use serde::{Deserialize, Serialize};
use std::{
    collections::{HashMap, VecDeque},
    fs,
    path::{Path, PathBuf},
    process::Command,
    sync::{mpsc, Arc, Mutex, RwLock},
};
use tauri::{Emitter, Manager};

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(default)]
struct Settings {
    office_path: Option<PathBuf>,
    python_path: Option<PathBuf>,
    tesseract_path: Option<PathBuf>,
}

#[derive(Debug, Clone, Serialize)]
struct EngineStatus {
    office: bool,
    pdf: bool,
    ocr: bool,
    worker_error: Option<String>,
}

#[derive(Debug, Clone, Serialize)]
struct InputFile {
    path: PathBuf,
    name: String,
    size: u64,
    extension: String,
    formats: Vec<catalog::Format>,
}

#[derive(Debug, Clone, Serialize)]
struct Job {
    id: String,
    name: String,
    format: String,
    status: String,
    message: String,
    receipt: Option<Receipt>,
}
struct Registry {
    jobs: HashMap<String, Job>,
    order: VecDeque<String>,
    cancellations: HashMap<String, Cancellation>,
}
struct Work {
    request: Request,
    id: String,
    engines: Engines,
    cancellation: Cancellation,
}
struct AppState {
    engines: RwLock<Engines>,
    registry: Arc<Mutex<Registry>>,
    sender: mpsc::SyncSender<Work>,
    exiting: std::sync::atomic::AtomicBool,
}

fn read_settings(app: &tauri::AppHandle) -> Settings {
    app.path()
        .app_config_dir()
        .ok()
        .and_then(|d| fs::read(d.join("settings.json")).ok())
        .and_then(|data| serde_json::from_slice(&data).ok())
        .unwrap_or_default()
}

fn detect(app: &tauri::AppHandle, settings: &Settings) -> Engines {
    let mut offices = Vec::new();
    if let Some(p) = &settings.office_path {
        offices.push(p.clone());
    }
    if let Some(p) = std::env::var_os("ORBIT_OFFICE") {
        offices.push(p.into());
    }
    offices.extend([
        PathBuf::from("/Applications/LibreOffice.app/Contents/MacOS/soffice"),
        PathBuf::from("C:\\Program Files\\LibreOffice\\program\\soffice.com"),
        PathBuf::from("C:\\Program Files\\LibreOffice\\program\\soffice.exe"),
    ]);
    let mut tess = Vec::new();
    if let Some(p) = &settings.tesseract_path {
        tess.push(p.clone());
    }
    if let Some(p) = std::env::var_os("ORBIT_TESSERACT") {
        tess.push(p.into());
    }
    tess.extend([
        PathBuf::from("/opt/homebrew/bin/tesseract"),
        PathBuf::from("/usr/local/bin/tesseract"),
        PathBuf::from("C:\\Program Files\\Tesseract-OCR\\tesseract.exe"),
    ]);
    let dev = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap_or(Path::new("."))
        .to_path_buf();
    let mut pythons = Vec::new();
    if let Some(p) = &settings.python_path {
        pythons.push(p.clone());
    }
    if let Some(p) = std::env::var_os("ORBIT_ENGINE_PYTHON") {
        pythons.push(p.into());
    }
    pythons.extend([
        dev.join(".venv/Scripts/python.exe"),
        dev.join(".venv/bin/python"),
    ]);
    let python = catalog::find_program(if cfg!(windows) { "python" } else { "python3" }, &pythons);
    let mut workers = Vec::new();
    let name = if cfg!(windows) {
        "orbit-engine.exe"
    } else {
        "orbit-engine"
    };
    if let Some(p) = std::env::var_os("ORBIT_ENGINE") {
        workers.push(p.into());
    }
    if let Ok(resource) = app.path().resource_dir() {
        workers.push(resource.join(name));
    }
    if let Ok(exe) = std::env::current_exe() {
        if let Some(parent) = exe.parent() {
            workers.push(parent.join(name));
        }
    }
    let script = dev.join("engine/worker.py");
    Engines {
        office: catalog::find_program("soffice", &offices),
        worker: workers.into_iter().find(|p| p.is_file()),
        python,
        script: script.is_file().then_some(script),
        tesseract: catalog::find_program("tesseract", &tess),
    }
}

fn doctor(engines: &mut Engines) -> EngineStatus {
    let mut status = EngineStatus {
        office: engines.office.is_some(),
        pdf: false,
        ocr: engines.tesseract.is_some(),
        worker_error: None,
    };
    let mut command = if let Some(worker) = &engines.worker {
        Command::new(worker)
    } else if let (Some(python), Some(script)) = (&engines.python, &engines.script) {
        let mut c = Command::new(python);
        c.arg(script);
        c
    } else {
        status.worker_error =
            Some("PDF worker not found. Run the setup script or use a packaged build.".into());
        return status;
    };
    let result = (|| -> Result<(), orbit_core::Error> {
        let temp = tempfile_dir()?;
        let response = temp.path().join("doctor.json");
        command.arg("--doctor").arg("--response").arg(&response);
        orbit_core::process::run(&mut command, &Cancellation::default())?;
        let data: serde_json::Value = serde_json::from_slice(&fs::read(response)?)?;
        status.pdf = data["ready"].as_bool().unwrap_or(false);
        if !status.pdf {
            status.worker_error = Some(format!("Worker dependencies missing: {}", data["missing"]));
        }
        Ok(())
    })();
    if let Err(error) = result {
        status.worker_error = Some(error.to_string());
    }
    if !status.pdf {
        engines.worker = None;
        engines.python = None;
    }
    status
}

// Keep temporary directory implementation inside the core's dependency graph unnecessary:
fn tempfile_dir() -> Result<TempFolder, std::io::Error> {
    let path = std::env::temp_dir().join(format!("orbit-doctor-{}", uuid::Uuid::new_v4()));
    fs::create_dir(&path)?;
    Ok(TempFolder(path))
}
struct TempFolder(PathBuf);
impl TempFolder {
    fn path(&self) -> &Path {
        &self.0
    }
}
impl Drop for TempFolder {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.0);
    }
}

#[tauri::command]
async fn refresh_engines(
    app: tauri::AppHandle,
    state: tauri::State<'_, AppState>,
) -> Result<EngineStatus, String> {
    let handle = app.clone();
    let (engines, status) = tauri::async_runtime::spawn_blocking(move || {
        let mut engines = detect(&handle, &read_settings(&handle));
        let status = doctor(&mut engines);
        (engines, status)
    })
    .await
    .map_err(|e| e.to_string())?;
    *state.engines.write().map_err(|e| e.to_string())? = engines;
    Ok(status)
}

#[tauri::command]
fn get_settings(app: tauri::AppHandle) -> Settings {
    read_settings(&app)
}

#[tauri::command]
fn save_settings(app: tauri::AppHandle, settings: Settings) -> Result<(), String> {
    for path in [
        &settings.office_path,
        &settings.python_path,
        &settings.tesseract_path,
    ]
    .into_iter()
    .flatten()
    {
        if !path.is_absolute() || !path.is_file() {
            return Err("Choose an existing executable using its absolute path".into());
        }
    }
    let dir = app.path().app_config_dir().map_err(|e| e.to_string())?;
    fs::create_dir_all(&dir).map_err(|e| e.to_string())?;
    let data = serde_json::to_vec_pretty(&settings).map_err(|e| e.to_string())?;
    fs::write(dir.join("settings.json"), data).map_err(|e| e.to_string())
}

#[tauri::command]
fn inspect_files(
    paths: Vec<PathBuf>,
    state: tauri::State<'_, AppState>,
) -> Result<Vec<InputFile>, String> {
    if paths.is_empty() || paths.len() > 100 {
        return Err("Choose between 1 and 100 files".into());
    }
    let engines = state.engines.read().map_err(|e| e.to_string())?;
    paths
        .into_iter()
        .map(|path| {
            let path = orbit_core::canonical_path(&path).map_err(|e| e.to_string())?;
            let meta = fs::metadata(&path).map_err(|e| e.to_string())?;
            if !meta.is_file() || meta.len() > orbit_core::MAX_INPUT_BYTES {
                return Err("Choose regular files up to 250 MiB each".into());
            }
            Ok(InputFile {
                name: path
                    .file_name()
                    .unwrap_or_default()
                    .to_string_lossy()
                    .into(),
                size: meta.len(),
                extension: orbit_core::extension(&path),
                formats: catalog::formats(&path, &engines),
                path,
            })
        })
        .collect()
}

#[tauri::command]
fn enqueue(request: Request, state: tauri::State<'_, AppState>) -> Result<Job, String> {
    if state.exiting.load(std::sync::atomic::Ordering::SeqCst) {
        return Err("Orbit is closing".into());
    }
    request.options.validate().map_err(|e| e.to_string())?;
    let engines = state.engines.read().map_err(|e| e.to_string())?.clone();
    if !catalog::formats(&request.input, &engines)
        .iter()
        .any(|f| f.id == request.format && f.available)
    {
        return Err("This conversion engine is unavailable".into());
    }
    let mut registry = state.registry.lock().map_err(|e| e.to_string())?;
    if registry.cancellations.len() >= 100 {
        return Err("The queue is full (100 files). Wait for jobs to finish.".into());
    }
    let id = uuid::Uuid::new_v4().to_string();
    let cancellation = Cancellation::default();
    let job = Job {
        id: id.clone(),
        name: request
            .input
            .file_name()
            .unwrap_or_default()
            .to_string_lossy()
            .into(),
        format: request.format.clone(),
        status: "queued".into(),
        message: "Waiting to convert".into(),
        receipt: None,
    };
    registry.jobs.insert(id.clone(), job.clone());
    registry.order.push_back(id.clone());
    registry
        .cancellations
        .insert(id.clone(), cancellation.clone());
    if let Err(error) = state.sender.try_send(Work {
        request,
        id: id.clone(),
        engines,
        cancellation,
    }) {
        registry.jobs.remove(&id);
        registry.cancellations.remove(&id);
        registry.order.retain(|v| v != &id);
        return Err(format!("Could not queue the job: {error}"));
    }
    Ok(job)
}

#[tauri::command]
fn list_jobs(state: tauri::State<'_, AppState>) -> Result<Vec<Job>, String> {
    let registry = state.registry.lock().map_err(|e| e.to_string())?;
    Ok(registry
        .order
        .iter()
        .filter_map(|id| registry.jobs.get(id).cloned())
        .collect())
}

#[tauri::command]
fn cancel_job(id: String, state: tauri::State<'_, AppState>) -> Result<(), String> {
    let registry = state.registry.lock().map_err(|e| e.to_string())?;
    if let Some(token) = registry.cancellations.get(&id) {
        token.cancel();
    }
    Ok(())
}

#[tauri::command]
fn show_output(id: String, state: tauri::State<'_, AppState>) -> Result<(), String> {
    let registry = state.registry.lock().map_err(|e| e.to_string())?;
    let dir = registry
        .jobs
        .get(&id)
        .and_then(|j| j.receipt.as_ref())
        .map(|r| r.directory.clone())
        .ok_or("No completed output for this job")?;
    let mut command = if cfg!(windows) {
        Command::new("explorer.exe")
    } else if cfg!(target_os = "macos") {
        Command::new("/usr/bin/open")
    } else {
        Command::new("xdg-open")
    };
    command.arg(dir).spawn().map_err(|e| e.to_string())?;
    Ok(())
}

#[tauri::command]
fn toggle_drop(app: tauri::AppHandle) -> Result<(), String> {
    if let Some(window) = app.get_webview_window("drop") {
        window.close().map_err(|e| e.to_string())?;
        return Ok(());
    }
    tauri::WebviewWindowBuilder::new(
        &app,
        "drop",
        tauri::WebviewUrl::App("index.html?drop=1".into()),
    )
    .title("Orbit Drop")
    .inner_size(250.0, 230.0)
    .resizable(false)
    .always_on_top(true)
    .build()
    .map_err(|e| e.to_string())?;
    Ok(())
}

#[tauri::command]
fn forward_drop(app: tauri::AppHandle, paths: Vec<PathBuf>) -> Result<(), String> {
    if paths.len() > 100 {
        return Err("Drop at most 100 files".into());
    }
    app.emit_to("main", "orbit:drop", paths)
        .map_err(|e| e.to_string())?;
    if let Some(main) = app.get_webview_window("main") {
        let _ = main.show();
        let _ = main.set_focus();
    }
    Ok(())
}

fn update(
    app: &tauri::AppHandle,
    registry: &Arc<Mutex<Registry>>,
    id: &str,
    status: &str,
    message: String,
    receipt: Option<Receipt>,
) {
    if let Ok(mut reg) = registry.lock() {
        if let Some(job) = reg.jobs.get_mut(id) {
            job.status = status.into();
            job.message = message;
            job.receipt = receipt;
            let _ = app.emit("orbit:job", job.clone());
        }
        if ["done", "failed", "cancelled"].contains(&status) {
            reg.cancellations.remove(id);
        }
        while reg.order.len() > 200 {
            let Some(first) = reg.order.front().cloned() else {
                break;
            };
            if reg.cancellations.contains_key(&first) {
                break;
            }
            reg.order.pop_front();
            reg.jobs.remove(&first);
        }
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "orbit=info,orbit_core=info".into()),
        )
        .init();
    tauri::Builder::default().plugin(tauri_plugin_dialog::init()).setup(|app| {
        let registry=Arc::new(Mutex::new(Registry{jobs:HashMap::new(),order:VecDeque::new(),cancellations:HashMap::new()}));
        let (sender,receiver)=mpsc::sync_channel::<Work>(100);
        app.manage(AppState{engines:RwLock::new(detect(app.handle(),&read_settings(app.handle()))),registry:registry.clone(),sender,exiting:std::sync::atomic::AtomicBool::new(false)});
        let handle=app.handle().clone();
        std::thread::spawn(move || {
            for work in receiver {
                if work.cancellation.check().is_err() { update(&handle,&registry,&work.id,"cancelled","Cancelled before starting".into(),None); continue; }
                update(&handle,&registry,&work.id,"running","Converting locally…".into(),None);
                tracing::info!(job_id=%work.id,format=%work.request.format,"conversion started");
                match orbit_core::convert::convert(&work.request,&work.engines,&work.cancellation) {
                    Ok(receipt) => { let message=format!("{} output file(s)",receipt.files.len()); update(&handle,&registry,&work.id,"done",message,Some(receipt)); }
                    Err(orbit_core::Error::Cancelled) => update(&handle,&registry,&work.id,"cancelled","Cancelled; partial output removed".into(),None),
                    Err(error) => { tracing::warn!(job_id=%work.id,error=%error,"conversion failed"); update(&handle,&registry,&work.id,"failed",error.to_string(),None); }
                }
            }
        });
        Ok(())
    }).invoke_handler(tauri::generate_handler![refresh_engines,get_settings,save_settings,inspect_files,enqueue,list_jobs,cancel_job,show_output,toggle_drop,forward_drop])
        .build(tauri::generate_context!()).expect("Orbit could not start")
        .run(|app,event| {
            if let tauri::RunEvent::WindowEvent {label,event:tauri::WindowEvent::CloseRequested {..},..}=&event {
                if label=="main" { if let Some(drop)=app.get_webview_window("drop") { let _=drop.close(); } }
            }
            if let tauri::RunEvent::ExitRequested {api,..}=event {
                let state=app.state::<AppState>();
                let registry=state.registry.clone();
                let active=registry.lock().map(|reg| { for token in reg.cancellations.values() { token.cancel(); } !reg.cancellations.is_empty() }).unwrap_or(false);
                if active {
                    api.prevent_exit();
                    if !state.exiting.swap(true,std::sync::atomic::Ordering::SeqCst) {
                        let handle=app.clone();
                        std::thread::spawn(move || {
                            // Wait for native codecs or process-tree cancellation and staged-file cleanup.
                            while registry.lock().map(|reg| !reg.cancellations.is_empty()).unwrap_or(false) {
                                std::thread::sleep(std::time::Duration::from_millis(100));
                            }
                            handle.exit(0);
                        });
                    }
                }
            }
        });
}
