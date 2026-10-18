$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
foreach ($program in @("node", "npm", "cargo")) {
    if (-not (Get-Command $program -ErrorAction SilentlyContinue)) { throw "Install $program first; see README.md." }
}
if (Get-Command py -ErrorAction SilentlyContinue) { py -3 -m venv .venv }
elseif (Get-Command python -ErrorAction SilentlyContinue) { python -m venv .venv }
else { throw "Install Python 3.11 or 3.12 first." }
if ($LASTEXITCODE -ne 0) { throw "Could not create Python environment." }
$python = Join-Path $PWD ".venv\Scripts\python.exe"
& $python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw "pip update failed." }
& $python -m pip install -r engine/requirements-dev.txt
if ($LASTEXITCODE -ne 0) { throw "Worker dependency installation failed." }
npm ci
if ($LASTEXITCODE -ne 0) { throw "Frontend dependency installation failed." }
Write-Host "Setup complete. Run npm run desktop. Install LibreOffice for Office conversion; Tesseract is optional for OCR."

