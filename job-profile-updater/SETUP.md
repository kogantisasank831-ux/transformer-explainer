# Setup and first-run checklist

This updater uses a persistent local Chromium profile. You sign in yourself;
the script does not accept, store, or submit a username, password, OTP, or
CAPTCHA response. Complete the first run manually before installing the daily
Windows task.

## 1. Install

Requirements: Windows 10/11, Python 3.11 or newer, and PowerShell.

```powershell
git clone https://github.com/kogantisasank831-ux/transformer-explainer.git
cd transformer-explainer\job-profile-updater
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

Run the tests after Chromium is installed:

```powershell
.\.venv\Scripts\python.exe -m pytest -q -ra
```

The full local suite has 35 cases. A skipped Chromium case means the browser or
one of its system dependencies is unavailable; it is not a passing browser
test.

## 2. Add the resume without committing it

Copy the resume you want to upload into this folder as `resume.pdf`,
`resume.doc`, or `resume.docx`. These conventional filenames are ignored by
Git. You can instead keep it elsewhere and put its absolute path in
`resume_path`.

Keep every resume revision accurate. Re-uploading identical bytes may leave a
portal's profile date unchanged.

## 3. Sign in and collect current selectors

Start with one portal at a time. Disable the other automatic profile in
`config.yaml` while configuring it.

```powershell
.\.venv\Scripts\python.exe profile_updater.py login --site naukri --inspect
```

Sign in in the opened Chromium window, including any OTP or CAPTCHA. Return to
the terminal and press Enter. Playwright Inspector then lets you use **Pick
locator** on the profile controls. Repeat for Hirist:

```powershell
.\.venv\Scripts\python.exe profile_updater.py login --site hirist --inspect
```

For each automatic profile, set these values in `config.yaml`:

| Setting | Required evidence |
| --- | --- |
| `url` | Exact logged-in profile page URL |
| `edit_steps` | Clicks needed to expose the resume upload control |
| `file_input_selector` | Unique `input[type=file]` selector |
| `save_selector` | Unique upload/save button, or empty only for auto-upload |
| `success_selector` | Element that appears only after a successful save |
| `verification_steps` | Clicks needed to display the saved resume/date |
| `resume_name_selector` | Element showing the current resume filename |
| `last_updated_selector` | The profile's update date/time element |
| `last_updated_attribute` | Optional precise attribute such as `datetime` |

Every configured selector must match exactly one element. Portal layouts vary
by account and can change, so the repository intentionally contains no guessed
Naukri or Hirist selectors. Use the profile update time, not login time or an
upload toast.

Indeed stays in `manual` mode. The scheduled run can open its profile page as a
reminder, but this project does not automate Indeed.

## 4. Validate without changing a profile

```powershell
.\.venv\Scripts\python.exe profile_updater.py validate
.\.venv\Scripts\python.exe profile_updater.py run --site naukri --dry-run
.\.venv\Scripts\python.exe profile_updater.py run --site hirist --dry-run
```

Dry run opens the configured live profile, resolves controls, and reads the
existing filename and update indicator. It does not choose a file or click
Save. Fix any selector error before continuing.

## 5. Perform one supervised update

Run one site while watching its Chromium window. Temporarily set
`headless: false` in `config.yaml` if you want it visible.

```powershell
.\.venv\Scripts\python.exe profile_updater.py run --site naukri
.\.venv\Scripts\python.exe profile_updater.py status
```

Repeat for Hirist only after Naukri works. A `verified` result requires both the
expected filename and a changed configured profile timestamp. A
`needs_review` result means an upload may have happened; inspect the live
profile before running anything again.

After resolving an uncertain result, clear only that site's local block:

```powershell
.\.venv\Scripts\python.exe profile_updater.py reset --site naukri
```

Resetting does not undo a portal change.

## 6. Install the daily Windows task

Install the task only after both configured automatic sites pass a supervised
run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install_scheduler.ps1
Start-ScheduledTask -TaskName 'Daily Job Profile Updater'
Get-ScheduledTaskInfo -TaskName 'Daily Job Profile Updater'
```

Check `runtime\scheduler-YYYY-MM-DD.log`. The task runs one minute after sign
in, unlock, or a supported resume-from-sleep event, with an 08:00 local-time
fallback. It performs at most one verified update per configured timezone day.
The laptop must be awake and the Windows user must have an interactive session.

Remove the task before moving the folder or reinstalling it:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\remove_scheduler.ps1
```

Keep `runtime\browser` private because it contains the saved browser session.
Do not commit a resume, runtime files, or personal selector configuration.

## What was verified in this repository

On 8 November 2026, 27 non-browser tests passed and eight optional Chromium
tests were skipped because Chromium was unavailable in the build environment.
The current public Naukri login page and Hirist login dialog were also opened:
Naukri displayed email/username and password controls; Hirist displayed an
OTP-first login with password, Google, and Apple alternatives.

That public check confirms reachability only. Dummy credentials cannot reach a
profile, upload a resume, or prove that a portal changes its profile timestamp.
Authenticated selector, upload, timestamp, and Windows-trigger checks must be
completed with the checklist above on a test account you control. See
[`VALIDATION.md`](VALIDATION.md) for the exact evidence boundary.
