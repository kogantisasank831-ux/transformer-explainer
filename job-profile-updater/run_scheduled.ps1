# Invoked by Task Scheduler. Retries allow Wi-Fi to connect after waking.
$ErrorActionPreference = 'Continue'
$Root = $PSScriptRoot
$Python = Join-Path $Root '.venv\Scripts\python.exe'
$Script = Join-Path $Root 'profile_updater.py'
$Config = Join-Path $Root 'config.yaml'
$Runtime = Join-Path $Root 'runtime'
New-Item -ItemType Directory -Force -Path $Runtime | Out-Null
$Log = Join-Path $Runtime ('scheduler-' + (Get-Date -Format 'yyyy-MM-dd') + '.log')
if (-not (Test-Path -LiteralPath $Python)) { 'Python environment missing.' | Out-File -Append $Log; exit 1 }
for ($Attempt = 1; $Attempt -le 3; $Attempt++) {
    "$(Get-Date -Format o) attempt=$Attempt" | Out-File -Append -Encoding utf8 $Log
    & $Python $Script run --config $Config 2>&1 | Out-File -Append -Encoding utf8 $Log
    $Code = $LASTEXITCODE
    if ($Code -eq 0) { exit 0 }
    if ($Attempt -lt 3) { Start-Sleep -Seconds 60 }
}
exit $Code
