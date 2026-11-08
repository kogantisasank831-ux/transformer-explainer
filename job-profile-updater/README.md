# Daily profile updater

For an end-to-end Windows installation checklist, start with
[`SETUP.md`](SETUP.md). This README explains the behavior and configuration
contract in more detail.

Re-upload your chosen resume or alternate between two accurate headline/summary
variants. The updater checks the saved content and the profile's visible
last-updated indicator. Windows scheduling runs when you sign in, unlock or
wake the laptop, with an 08:00 fallback. Each verified site runs once per IST day.

## Update methods

| Method | Actual change | Verification |
| --- | --- | --- |
| `resume_upload` | Select and upload your configured PDF/DOC/DOCX | New upload success indicator, visible exact filename, changed last-updated value |
| `text_variants` | Save the alternative of two approved text versions | Reopened field equals proposed text, changed last-updated value |
| `whitespace` | Legacy one/two internal space toggle | Exact persisted spacing, changed last-updated value |

Resume upload is the default. An identical file may not refresh a site's date.
A revised resume is preferable. The code never changes your resume bytes to
manufacture a difference. The filename check does not compare downloaded server
bytes; the SHA256 in state records which local file was submitted.

Text variants must both be truthful. The current field must exactly match one
of them, or the script stops before saving so it cannot overwrite a later manual
edit. It never deletes your name or removes and restores your skills.

There is no guarantee of ranking improvement or timestamp behavior on any site.
A changed indicator only proves that the selected indicator changed. Configure
it from the site's PROFILE last-updated value, not an upload timer, a toast or
your current login time. If the site only shows "Today", an edit made later the
same day may produce an unchanged indicator and need manual review.

## Install

Python 3.11+. Extract to a permanent folder and open a terminal there:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

Linux/macOS: use `.venv/bin/python` in place of `.venv\Scripts\python.exe`.
Linux may require `python -m playwright install --with-deps chromium`.

## Configure once

1. Put your resume beside `config.yaml`, or set `resume_path` to its absolute
   path. Relative paths are resolved beside the YAML, not the working directory.
   Default maximum is 2 MiB; set `max_resume_bytes` to the site's actual limit.
2. Log in manually, including OTP/CAPTCHA:

```powershell
.\.venv\Scripts\python.exe profile_updater.py login --inspect
```

3. Open your profile page in each tab and copy its exact URL into `url`.
   In Playwright Inspector, use Pick locator to identify the controls below.
   Press Resume to move through the tabs. Copy selector strings such as `#id`
   or `text="Upload"`; do not paste Python `page.get_by_role(...)` expressions.
4. Fill the selectors in `config.yaml`. Every configured locator must match
   exactly one element. The supplied selectors are intentionally blank because
   your account's logged-in UI has not been inspected here.
5. Set any unconfigured site to `mode: disabled` (or `manual`). All enabled
   auto profiles must validate before running. Indeed defaults to `manual`.

| YAML field | What you supply |
| --- | --- |
| `url` | Profile page URL from your logged-in browser |
| `edit_steps` | Ordered selectors to click before the editable field/file input is accessible |
| `file_input_selector` | The actual `input[type=file]`; it may be hidden |
| `save_selector` | Save/upload button; leave empty only when file selection uploads automatically |
| `success_selector` | A post-save success element, absent or hidden before submission |
| `verification_steps` | Ordered clicks from the profile URL to show verification indicators |
| `resume_name_selector` | Element containing exactly the uploaded filename |
| `expected_resume_name` | Optional exact displayed filename if the site renames it |
| `last_updated_selector` | Profile last-updated element |
| `last_updated_attribute` | Optional precise attribute, such as `datetime`; empty means visible text |
| `verification_attempts` | Reload checks from 1 to 10; default 3 |

The implementation supports direct input/textarea and file-input controls in
the main page. Sites using rich-text editors, inaccessible iframe controls,
OS-only file dialogs, multiple upload confirmation stages or resume workflows
with additional compulsory fields require a custom adapter. Selectors can
change and must be maintained.

For headline edits use `config.text-example.yaml` as a starting point. Its
selectors are illustrative, not actual Naukri selectors. Configure your own,
ensure the current headline equals one approved variant, and pass that file
with `--config config.text-example.yaml` for every command. The scheduler uses
`config.yaml`, so copy your preferred final configuration there before installing.

## Validate and first run

```powershell
.\.venv\Scripts\python.exe profile_updater.py validate
.\.venv\Scripts\python.exe profile_updater.py run --dry-run
.\.venv\Scripts\python.exe profile_updater.py run
.\.venv\Scripts\python.exe profile_updater.py status
```

`validate` checks YAML, methods, required selectors, variant structure and local
resume file/size. It does not inspect websites. Dry run opens the live pages,
reads the field and update indicator, and resolves controls without selecting
files, filling fields, clicking Save, or writing the submission journal.

`verified` means content evidence was found and the configured update indicator
changed after reload. `needs_review` means a save may have occurred but evidence
is incomplete. Inspect your live profile and `runtime/state.json`. The file
contains timestamps, status and (for uploads) local resume SHA256, not headline
text or resume contents. It is not a recruiter-ranking measurement.

## Review and resume after an uncertain save

The script journals `submitted` BEFORE selecting a file or filling a field,
because some sites save automatically. A crash cannot cause repeated daily
submissions. `submitted` and `needs_review` remain blocked even on following
days until you check the site and explicitly reset that site:

```powershell
.\.venv\Scripts\python.exe profile_updater.py reset --site naukri
```

Reset only clears local tracking; it does not undo the site's edit. Then fix the
selector/configuration if needed and run again. Do not reset automatically.
Failures before submission remain eligible for later scheduler retries.
A nonzero exit code indicates a failure or review requirement. Expired login
requires another manual `login` command. No CAPTCHA bypass is implemented.

## Schedule on Windows

After a successful configured first run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install_scheduler.ps1
```

This installs a task for your current Windows user. It validates configuration
before registration. It runs one minute after sign-in, unlock, or a Windows
Power-Troubleshooter resume event, and at 08:00 laptop local time. The laptop
must be awake and your user signed in; it never wakes the machine. Opening the
lid usually causes resume/unlock, but the lid itself is not a guaranteed event.
Some hardware omits the resume event; unlock and daily triggers remain fallbacks.
It works on battery and retries a failed run up to three times, one minute apart,
allowing Wi-Fi to reconnect. Reviews stay blocked, so retries don't duplicate
possibly successful edits. There is a 15-minute task execution limit.

Inspect `runtime/scheduler-YYYY-MM-DD.log` and Task Scheduler's Last Run Result.
The installer does not run an update immediately. Test the registered task:

```powershell
Start-ScheduledTask -TaskName 'Daily Job Profile Updater'
Get-ScheduledTaskInfo -TaskName 'Daily Job Profile Updater'
```

Remove it before reinstalling or moving the folder:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\remove_scheduler.ps1
```

No task has been installed on your laptop from this conversation. The XML has
been checked against Microsoft's documented trigger ordering. Windows task
registration and wake/unlock delivery were not executed in this environment.

## Linux and macOS scheduling

Use cron on an awake computer, with its timezone set as desired. YAML timezone
controls once-per-day deduplication; it does not set the OS scheduler's timezone.
Example (replace paths):

```cron
0 8 * * * /home/you/Profile_Updater/.venv/bin/python /home/you/Profile_Updater/profile_updater.py run >> /home/you/Profile_Updater/daily.log 2>&1
```

Cron is not a lid-open trigger and usually cannot open browser reminder tabs.
Set `open_manual_pages: false` and check logs for reminders.

## Privacy and platform behavior

`runtime/browser` contains login cookies. Do not share or commit it. Daily
scheduler logs are not automatically deleted; remove old ones periodically.
Indeed remains a manual reminder because its terms prohibit automated access
and content submission without express written permission. Check Naukri/Hirist
terms before using automated access. No passwords are saved by this application.

Official references:
- https://in.indeed.com/legal
- https://www.naukri.com/termsconditions
- https://www.hirist.tech/terms
- https://naukricom.freshdesk.com/support/solutions/articles/228162--how-can-i-update-edit-my-profile-
- https://www.indeed.com/help/job-seekers/articles/360051197532-profile-and-preferences-what-do-i-share-with-employers
- https://playwright.dev/python/docs/input
- https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-schema

## Tests

```powershell
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -q
```

Tests include local logic, simulated UI fixtures, and optional Chromium tests
with intercepted mock-site routes. They send no traffic to Naukri, Hirist or
Indeed. The separate public login-page smoke check did not perform a profile
edit. See `VALIDATION.md` for the actual execution results and remaining live
checks.
