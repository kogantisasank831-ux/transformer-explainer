[CmdletBinding()]
param([string]$TaskName = 'Daily Job Profile Updater')
$ErrorActionPreference = 'Stop'
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
Write-Host "Removed '$TaskName'. Files and saved browser login were retained."
