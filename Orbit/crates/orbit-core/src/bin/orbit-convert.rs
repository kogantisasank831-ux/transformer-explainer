//! Headless entry point for repeatable integration checks and automation.
use orbit_core::{catalog::find_program, Cancellation, Engines, Request};
use std::{fs, path::PathBuf};
fn main() {
    if let Err(error) = run() {
        eprintln!("{error}");
        std::process::exit(1);
    }
}
fn run() -> Result<(), Box<dyn std::error::Error>> {
    let file = std::env::args_os()
        .nth(1)
        .ok_or("Usage: orbit-convert REQUEST.json")?;
    let request: Request = serde_json::from_slice(&fs::read(file)?)?;
    let env_path = |key: &str| std::env::var_os(key).map(PathBuf::from);
    let engines = Engines {
        office: env_path("ORBIT_OFFICE").or_else(|| find_program("soffice", &[])),
        worker: env_path("ORBIT_ENGINE"),
        python: env_path("ORBIT_ENGINE_PYTHON")
            .or_else(|| find_program(if cfg!(windows) { "python" } else { "python3" }, &[])),
        script: env_path("ORBIT_ENGINE_SCRIPT"),
        tesseract: env_path("ORBIT_TESSERACT").or_else(|| find_program("tesseract", &[])),
    };
    let receipt = orbit_core::convert::convert(&request, &engines, &Cancellation::default())?;
    println!("{}", serde_json::to_string_pretty(&receipt)?);
    Ok(())
}
