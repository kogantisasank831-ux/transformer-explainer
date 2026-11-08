# Run from Windows PowerShell as your normal signed-in user.
[CmdletBinding()]
param([string]$TaskName = 'Daily Job Profile Updater')
$ErrorActionPreference = 'Stop'
$Root = $PSScriptRoot
$Python = Join-Path $Root '.venv\Scripts\python.exe'
$Runner = Join-Path $Root 'run_scheduled.ps1'
if (-not (Test-Path -LiteralPath $Python)) {
    throw 'Install the virtual environment and requirements first (see README).'
}
if (-not (Test-Path -LiteralPath $Runner)) { throw 'run_scheduled.ps1 is missing.' }
& $Python (Join-Path $Root 'profile_updater.py') validate
if ($LASTEXITCODE -ne 0) { throw 'Configuration validation failed. Complete config.yaml before scheduling.' }
function Escape-Xml([string]$Value) { [System.Security.SecurityElement]::Escape($Value) }
$Sid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$Boundary = (Get-Date).Date.AddHours(8).ToString('yyyy-MM-ddTHH:mm:ss')
$PowerShell = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$Arguments = '-NoProfile -NonInteractive -ExecutionPolicy Bypass -File "' + $Runner + '"'
$WakeQuery = '<QueryList><Query Id="0" Path="System"><Select Path="System">*[System[Provider[@Name=''Microsoft-Windows-Power-Troubleshooter''] and EventID=1]]</Select></Query></QueryList>'
$Xml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo><Description>Update configured profiles once per day when this user uses the laptop.</Description></RegistrationInfo>
  <Triggers>
    <LogonTrigger><Enabled>true</Enabled><UserId>$(Escape-Xml $Sid)</UserId><Delay>PT1M</Delay></LogonTrigger>
    <SessionStateChangeTrigger><Enabled>true</Enabled><UserId>$(Escape-Xml $Sid)</UserId><Delay>PT1M</Delay><StateChange>SessionUnlock</StateChange></SessionStateChangeTrigger>
    <EventTrigger><Enabled>true</Enabled><Subscription>$(Escape-Xml $WakeQuery)</Subscription><Delay>PT1M</Delay></EventTrigger>
    <CalendarTrigger><Enabled>true</Enabled><StartBoundary>$Boundary</StartBoundary><ScheduleByDay><DaysInterval>1</DaysInterval></ScheduleByDay></CalendarTrigger>
  </Triggers>
  <Principals><Principal id="User"><UserId>$(Escape-Xml $Sid)</UserId><LogonType>InteractiveToken</LogonType><RunLevel>LeastPrivilege</RunLevel></Principal></Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <AllowHardTerminate>true</AllowHardTerminate>
    <Enabled>true</Enabled><Hidden>false</Hidden>
    <WakeToRun>false</WakeToRun><ExecutionTimeLimit>PT15M</ExecutionTimeLimit>
  </Settings>
  <Actions Context="User"><Exec><Command>$(Escape-Xml $PowerShell)</Command><Arguments>$(Escape-Xml $Arguments)</Arguments><WorkingDirectory>$(Escape-Xml $Root)</WorkingDirectory></Exec></Actions>
</Task>
"@
# Refuse to overwrite an unrelated task with the same name.
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    throw "Task '$TaskName' already exists. Run remove_scheduler.ps1 first to reinstall."
}
Register-ScheduledTask -TaskName $TaskName -Xml $Xml | Out-Null
Write-Host "Installed '$TaskName' for your current Windows user."
Write-Host 'Runs after sign-in, unlock, resume from sleep, and daily at 08:00 local time.'
Write-Host 'The laptop stays asleep until you wake it. Successful site edits are skipped for the rest of that IST day.'
Write-Host 'The task was installed; no profile update was started by this installer.'
