import { invoke } from '@tauri-apps/api/core';
import { listen } from '@tauri-apps/api/event';
import { getCurrentWebview } from '@tauri-apps/api/webview';
import { getCurrentWindow } from '@tauri-apps/api/window';
import { open } from '@tauri-apps/plugin-dialog';
import { parentPath, matchingFiles, mergeJob, sizeLabel, terminal } from './model.js';

const desktop = Boolean(window.__TAURI_INTERNALS__);
const dropMode = new URLSearchParams(location.search).has('drop');
const app = document.getElementById('app');
const state = { files: [], active: 0, format: '', batch: true, output: null, jobs: [], busy: false,
  engines: {office:false,pdf:false,ocr:false}, settings: {}, error:'', notice:'', checking:true };
const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $ = selector => app.querySelector(selector);
const options = { quality:90,dpi:150,pages:'',ocr:false,language:'eng',docx_mode:'editable',single_page_sheets:false };
const demoRoutes = {
  image: [['png','Lossless image with transparency'],['webp','Lossless WebP image'],['tiff','TIFF image'],['bmp','Uncompressed bitmap'],['pdf','Image on a PDF page'],['txt','Recognise printed text with OCR']],
  word: [['pdf','Export document pages'],['odt','OpenDocument text'],['rtf','Basic rich text'],['txt','Text only; formatting is removed'],['html','HTML document']],
  excel: [['pdf','Export sheets using workbook print settings'],['ods','OpenDocument spreadsheet'],['csv','First sheet only; values without formatting'],['tsv','First sheet only; tab-separated values']],
  pdf: [['docx','Reconstruct editable content, or preserve page appearance as images'],['xlsx','Extract detected tables; original formulas cannot be recovered'],['csv','One CSV file per detected table'],['jpg','One image per page'],['png','One image per page'],['txt','Extract text; enable OCR for scans']]
};
function sample(kind) {
  const names={image:'coastline.jpg',word:'proposal.docx',excel:'forecast.xlsx',pdf:'statement.pdf'};
  state.files=[{path:'/Example/'+names[kind],name:names[kind],size:kind==='image'?2412000:184000,extension:names[kind].split('.').pop(),
    formats:demoRoutes[kind].map(([id,detail])=>({id,label:id.toUpperCase(),detail,available:true,requires:'Preview'}))}];
  state.active=0;state.format=state.files[0].formats[0].id;render();
}
function alertError(error) { state.error=String(error);state.notice='';render(); }
function render() {
  if(dropMode) return renderDrop();
  const file=state.files[state.active];
  const formats=file?.formats || [];
  const selected=formats.find(f=>f.id===state.format);
  const eligible=matchingFiles(state.files,state.format,state.batch?null:file?.path);
  const total=state.batch?state.files.length:1;
  app.innerHTML=`${desktop?'':'<div class="banner">Browser preview · Open the desktop app to convert files. Sample choices below only demonstrate the interface.</div>'}
    <header class="app-header"><div class="brand"><span class="brand-mark" aria-hidden="true"></span><strong>Orbit</strong></div><span class="header-sub">A new format, one turn away.</span><button class="text-button header-drop" id="drop-toggle" ${desktop?'':'disabled'}>Floating drop target</button><button class="outline-button" id="settings">Settings</button></header>
    <div class="layout"><main class="main"><div class="eyebrow">Drop. Choose. Convert.</div><h1>Your files. A different format.</h1><p class="subtitle">Choose a format around the circle. Everything stays on your computer.</p>
      <div class="workspace"><section class="drop-area" aria-label="Drop files here">${file?`
        <div class="wheel open"><div class="orbit-line" aria-hidden="true"></div><button class="wheel-center" id="browse-center" aria-label="Add files"><strong>${escape(file.extension.toUpperCase())}</strong><small>Drop or browse</small></button><div role="group" aria-label="Choose output format">${formats.map((f,i)=>{const angle=(-90+i*360/formats.length)*Math.PI/180;return `<button class="format" data-format="${escape(f.id)}" style="left:${50+35*Math.cos(angle)}%;top:${50+35*Math.sin(angle)}%" aria-pressed="${state.format===f.id}" ${f.available?'':'disabled'} title="${escape(f.available?f.detail:'Requires '+f.requires)}"><strong>${escape(f.label)}</strong><small>${f.available?(f.id==='xlsx'&&file.extension==='pdf'?'Tables':f.id==='txt'&&file.extension!=='pdf'?'OCR':'Select'):'Setup needed'}</small></button>`;}).join('')}</div></div>`:
        '<div class="empty-center"><div class="empty-icon" aria-hidden="true">↧</div><strong>Drop your files here</strong><p>Images, documents, spreadsheets and PDFs</p><button class="outline-button" id="browse-center">Browse files</button><p>Up to 100 files · 250 MB each</p></div>'}</section>
      <section class="detail">${file?`
        <div class="source"><div class="source-icon">${escape(file.extension.toUpperCase())}</div><div><div class="source-name">${escape(file.name)}</div><div class="meta">${escape(sizeLabel(file.size))} · Original file kept</div></div></div>
        <h2 class="output-title">${selected?'Convert to '+escape(selected.label):'Choose a format'}</h2><p class="format-description">${escape(selected?.detail || (formats.length?'Set up the required engine in Settings.':'This file type is not supported.'))}</p>
        ${file.extension==='pdf'?`<label class="field">Pages<input id="pages" type="text" placeholder="All, or 1-3,5" value="${escape(options.pages)}" maxlength="256"></label>`:''}
        ${['jpg','png'].includes(state.format)&&file.extension==='pdf'?`<label class="field">Resolution<select id="dpi">${[72,150,200,300].map(d=>`<option ${d===options.dpi?'selected':''} value="${d}">${d} DPI</option>`).join('')}</select></label>`:''}
        ${state.format==='jpg'?`<label class="field">JPEG quality<input id="quality" type="number" value="${options.quality}" min="1" max="100"></label>`:''}
        ${file.extension==='pdf'&&state.format==='docx'?`<label class="field">Word mode<select id="docx-mode"><option value="editable" ${options.docx_mode==='editable'?'selected':''}>Editable text & tables</option><option value="page_images" ${options.docx_mode==='page_images'?'selected':''}>Page images</option></select></label><p class="note">${options.docx_mode==='editable'?'Rebuilds text and tables. Pictures, exact styling and complex layouts are not retained.':'Keeps the page appearance as pictures. Text is not editable.'}</p>`:''}
        ${file.extension==='pdf'&&['docx','xlsx','csv','txt'].includes(state.format)?`<label class="field">OCR for scanned pages<input id="ocr" type="checkbox" ${options.ocr?'checked':''}></label>${options.ocr?`<label class="field">OCR language<input id="language" type="text" value="${escape(options.language)}" placeholder="eng"></label><p class="note">${state.engines.ocr?'OCR results need review. Language data must be installed.':'Tesseract is not detected. Configure it in Settings before using OCR.'}</p>`:''}`:''}
        ${['xlsx','xls','ods','csv','tsv'].includes(file.extension)&&state.format==='pdf'?`<label class="field">One page per sheet<input id="single-page" type="checkbox" ${options.single_page_sheets?'checked':''}></label><p class="note">Uses workbook print settings by default. One-page mode can make large sheets hard to read.</p>`:''}
        <label class="field">Save to<button id="output-folder" class="text-button folder-label" title="${escape(state.output||'Each source file’s folder')}">${state.output?'Custom folder…':'Same folder…'}</button></label>
        ${state.files.length>1?`<label class="field">Apply to compatible files<input id="batch" type="checkbox" ${state.batch?'checked':''}></label>`:''}
        ${eligible.length<total?`<p class="note">${total-eligible.length} file(s) do not support this format or need an engine. They will not be queued.</p>`:''}
        <div class="file-result">${state.format?`${escape(state.format.toUpperCase())} output → a new folder for each file`:'Select a supported output format'}</div>
        <button class="primary full" id="convert" ${!desktop||!selected?.available||!eligible.length||state.busy||state.checking?'disabled':''}>${desktop?(state.busy?'Adding to queue…':`Convert ${eligible.length>1?eligible.length+' files':'to '+escape(selected?.label||'…')}`):'Desktop app required'} <span aria-hidden="true">↗</span></button>`:
        '<div class="welcome-detail"><h2>Make the next format easy.</h2><p>Drop a file to reveal its compatible formats.</p><ul class="welcome-list"><li>Word & Excel → PDF</li><li>PDF → Word & Excel tables</li><li>Images → images, PDF & text</li></ul><p>Available formats depend on the local engines installed.</p></div>'}</section></div>
        ${state.files.length?`<div class="file-strip"><span class="meta">${state.files.length} file(s) selected</span><div><button class="text-button" id="add-files">+ Add files</button><button class="text-button" id="clear-files">Clear</button></div></div><div class="selected-files">${state.files.map((f,i)=>`<button class="file-chip" data-file="${i}" aria-pressed="${i===state.active}" title="${escape(f.name)}">${escape(f.name)}</button>`).join('')}</div>`:''}
        ${!desktop?'<div class="demo-samples"><span>Try a sample</span><button class="outline-button" data-sample="image">Image</button><button class="outline-button" data-sample="word">Word</button><button class="outline-button" data-sample="excel">Excel</button><button class="outline-button" data-sample="pdf">PDF</button></div>':''}
        <div class="alert" role="alert">${escape(state.error)}</div><div class="toast" role="status" aria-live="polite">${escape(state.notice)}</div>
      </main><aside class="aside"><div class="aside-head"><h2>Conversion queue</h2><span class="count">${state.jobs.filter(j=>!terminal(j.status)).length} active</span></div><div id="jobs"></div><p class="meta" style="margin-top:20px">Jobs run one at a time to keep memory use predictable. Queue history lasts for this session.</p></aside></div>
      <footer class="footer"><div class="status-group">${[['office','Office'],['pdf','PDF'],['ocr','OCR']].map(([key,label])=>`<button class="status ${state.engines[key]?'ready':''}" data-engine="${key}"><span class="status-dot"></span>${label} · ${state.checking?'checking':state.engines[key]?'ready':'setup needed'}</button>`).join('')}</div><span class="footer-note">Local processing · Originals kept</span></footer>
      <dialog id="settings-dialog"><h2>Conversion engines</h2><p>Image conversion is built in. Office conversions need LibreOffice; scanned text needs Tesseract. Packaged builds include the PDF worker. Setup and build steps are in the included README.</p>
      ${[['office_path','LibreOffice executable','Leave blank for automatic detection.'],['python_path','Development Python executable','For source builds only: use the Python inside the project’s .venv.'],['tesseract_path','Tesseract executable','Install the language data you want to recognise.']].map(([key,label,hint])=>`<div class="settings-field"><label for="${key}">${label}</label><div class="settings-path"><input id="${key}" value="${escape(state.settings[key]||'')}" placeholder="Auto-detect"><button class="outline-button" data-executable="${key}" ${desktop?'':'disabled'}>Browse</button></div><small>${hint}</small></div>`).join('')}
      <p id="engine-error" class="alert">${escape(state.engines.worker_error||'')}</p><div class="dialog-actions"><button class="text-button" id="settings-close">Close</button><button class="primary" id="settings-save" ${desktop?'':'disabled'}>Save & check</button></div></dialog>`;
  bind();renderJobs();
}

function bind() {
  $('#settings').onclick=()=>$('#settings-dialog').showModal();
  app.querySelectorAll('[data-engine]').forEach(b=>b.onclick=()=>$('#settings-dialog').showModal());
  $('#settings-close').onclick=()=>$('#settings-dialog').close();
  $('#settings-save').onclick=saveSettings;
  app.querySelectorAll('[data-executable]').forEach(b=>b.onclick=async()=>{try {const path=await open({multiple:false,directory:false});if(path)$('#'+b.dataset.executable).value=path;}catch(e){$('#engine-error').textContent=String(e);}});
  $('#drop-toggle').onclick=()=>invoke('toggle_drop').catch(alertError);
  $('#browse-center').onclick=browse;
  if($('#add-files')) $('#add-files').onclick=browse;
  if($('#clear-files')) $('#clear-files').onclick=()=>{state.files=[];state.active=0;state.error='';state.notice='';render();};
  app.querySelectorAll('[data-format]').forEach(b=>b.onclick=()=>{state.format=b.dataset.format;state.error='';render();});
  app.querySelectorAll('[data-file]').forEach(b=>b.onclick=()=>{state.active=Number(b.dataset.file);const file=state.files[state.active];if(!file.formats.some(f=>f.id===state.format&&f.available))state.format=file.formats.find(f=>f.available)?.id||'';render();});
  app.querySelectorAll('[data-sample]').forEach(b=>b.onclick=()=>sample(b.dataset.sample));
  const handlers={pages:e=>options.pages=e.target.value,quality:e=>options.quality=Number(e.target.value),dpi:e=>options.dpi=Number(e.target.value),language:e=>options.language=e.target.value};
  for(const [id,fn] of Object.entries(handlers)) if($('#'+id)) $('#'+id).onchange=fn;
  if($('#docx-mode')) $('#docx-mode').onchange=e=>{options.docx_mode=e.target.value;render();};
  if($('#ocr')) $('#ocr').onchange=e=>{options.ocr=e.target.checked;render();};
  if($('#single-page')) $('#single-page').onchange=e=>options.single_page_sheets=e.target.checked;
  if($('#batch')) $('#batch').onchange=e=>{state.batch=e.target.checked;render();};
  if($('#output-folder')) $('#output-folder').onclick=async()=>{if(!desktop)return;try{const selected=await open({directory:true,multiple:false});if(selected){state.output=selected;render();}}catch(e){alertError(e);}};
  if($('#convert')) $('#convert').onclick=convert;
  const area=$('.drop-area');
  area.ondragover=e=>{e.preventDefault();area.classList.add('dragging');};
  area.ondragleave=()=>area.classList.remove('dragging');
  area.ondrop=e=>{e.preventDefault();area.classList.remove('dragging');if(!desktop)alertError('This is the browser preview. Open the desktop app to use your files.');};
}

function renderJobs() {
  const holder=$('#jobs');if(!holder)return;
  holder.innerHTML=state.jobs.length?state.jobs.slice().reverse().map(job=>`<article class="job ${escape(job.status)}"><div class="job-top"><span class="job-name">${escape(job.name)}</span><span class="job-format">${escape(job.format.toUpperCase())}</span></div><div class="job-state">${job.status==='running'?'<span class="spinner" aria-hidden="true"></span>':''}${escape({queued:'Queued',running:'Converting',done:'Complete',failed:'Failed',cancelled:'Cancelled'}[job.status]||job.status)}</div><p class="job-message">${escape(job.message)}</p>${job.receipt?.warnings.map(w=>`<p class="job-message">${escape(w)}</p>`).join('')||''}<div class="job-actions">${!terminal(job.status)?`<button class="text-button" data-cancel="${escape(job.id)}">Cancel</button>`:''}${job.status==='done'?`<button class="outline-button" data-show="${escape(job.id)}">Show in folder ↗</button>`:''}</div></article>`).join(''):'<div class="queue-empty">Your next conversion<br>will appear here.</div>';
  holder.querySelectorAll('[data-cancel]').forEach(b=>b.onclick=async()=>{try{await invoke('cancel_job',{id:b.dataset.cancel});b.textContent='Cancelling…';b.disabled=true;}catch(e){alertError(e);}});
  holder.querySelectorAll('[data-show]').forEach(b=>b.onclick=()=>invoke('show_output',{id:b.dataset.show}).catch(alertError));
  const count=$('.aside .count');if(count)count.textContent=state.jobs.filter(j=>!terminal(j.status)).length+' active';
}

async function browse() {
  if(!desktop){state.error='Open the desktop app to choose files, or use a sample below.';render();return;}
  try{const paths=await open({multiple:true,directory:false});if(paths)await ingest(Array.isArray(paths)?paths:[paths]);}catch(e){alertError(e);}
}
async function ingest(paths) {
  try{
    const newFiles=await invoke('inspect_files',{paths});
    const combined=new Map(state.files.map(file=>[file.path,file]));newFiles.forEach(file=>combined.set(file.path,file));
    if(combined.size>100)throw new Error('Choose at most 100 files at a time.');
    state.files=[...combined.values()];state.active=Math.max(0,state.files.findIndex(f=>f.path===newFiles[0]?.path));
    const file=state.files[state.active];state.format=file?.formats.find(f=>f.available)?.id||'';state.error='';state.notice='';render();
  }catch(e){alertError(e);}
}
async function convert() {
  if(state.busy||!desktop)return;
  if(!(options.quality>=1&&options.quality<=100)){alertError('JPEG quality must be between 1 and 100.');return;}
  const file=state.files[state.active];const eligible=matchingFiles(state.files,state.format,state.batch?null:file.path);
  if(!eligible.length)return;
  const format=state.format, jobOptions={...options}, output=state.output;
  state.busy=true;state.error='';render();let count=0;
  try{
    for(const file of eligible){const job=await invoke('enqueue',{request:{input:file.path,output_dir:output||parentPath(file.path),format,options:jobOptions}});state.jobs=mergeJob(state.jobs,job);count++;renderJobs();}
    state.notice=`${count} file(s) added to the conversion queue.`;
  }catch(e){state.error=`${count} queued. ${String(e)}`;}finally{state.busy=false;render();}
}
async function saveSettings() {
  const values={};for(const key of ['office_path','python_path','tesseract_path'])values[key]=$('#'+key).value.trim()||null;
  const button=$('#settings-save');button.disabled=true;button.textContent='Checking…';
  try{await invoke('save_settings',{settings:values});state.settings=values;state.engines=await invoke('refresh_engines');state.checking=false;
    if(state.files.length)state.files=await invoke('inspect_files',{paths:state.files.map(f=>f.path)});
    state.notice='Engine settings updated.';render();
  }catch(e){$('#engine-error').textContent=String(e);button.disabled=false;button.textContent='Save & check';}
}
function renderDrop() {
  app.innerHTML='<main class="drop-window"><button class="compact-drag" id="drag-handle">⋮⋮ Move</button><div class="empty-icon" aria-hidden="true">↧</div><strong>Drop into Orbit</strong><p>The format wheel opens<br>in the main window.</p><button class="text-button" id="drop-browse">Choose files</button><div class="alert" role="alert"></div></main>';
  $('#drag-handle').onmousedown=()=>getCurrentWindow().startDragging();
  $('#drop-browse').onclick=async()=>{try{const paths=await open({multiple:true,directory:false});if(paths)await invoke('forward_drop',{paths:Array.isArray(paths)?paths:[paths]});}catch(e){$('.alert').textContent=String(e);}};
}

const cleanups=[];
window.addEventListener('beforeunload',()=>cleanups.forEach(fn=>fn()));
async function start() {
  render();
  if(!desktop){state.checking=false;if(new URLSearchParams(location.search).has('demo'))sample('pdf');else render();return;}
  try{
    cleanups.push(await getCurrentWebview().onDragDropEvent(async event=>{
      const data=event.payload;
      if(data.type==='over'||data.type==='enter')$('.drop-area')?.classList.add('dragging');
      if(data.type==='leave')$('.drop-area')?.classList.remove('dragging');
      if(data.type==='drop'){
        if(dropMode)await invoke('forward_drop',{paths:data.paths});else await ingest(data.paths);
      }
    }));
    if(dropMode)return;
    cleanups.push(await listen('orbit:drop',event=>ingest(event.payload)));
    cleanups.push(await listen('orbit:job',event=>{state.jobs=mergeJob(state.jobs,event.payload);renderJobs();}));
    state.settings=await invoke('get_settings');state.jobs=await invoke('list_jobs');
    state.engines=await invoke('refresh_engines');
    if(state.files.length)state.files=await invoke('inspect_files',{paths:state.files.map(f=>f.path)});
    state.checking=false;render();
  }catch(e){state.checking=false;alertError(e);}
}
start();
