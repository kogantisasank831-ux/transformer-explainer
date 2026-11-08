# Validation results

Completed for the repository package on 8 November 2026.

## Executed successfully

- Python compilation checks.
- 27 pytest checks passed: pure logic, YAML validation, and simulated UI workflows.
- Valid-configuration CLI smoke check returned zero.
- Default unconfigured YAML was correctly rejected before browser launch or editing.
- Windows Task Scheduler XML parsed successfully; trigger ordering was checked
  against Microsoft's published schema.
- Guide rendered into three pages and each page was visually inspected.
- The current public Naukri login page loaded and exposed email/username,
  password, Login and OTP-login controls.
- The current public Hirist page loaded and its Login action opened an OTP-first
  dialog with password, Google and Apple alternatives.

The executed tests include resume file selection, local file path and size
validation, alternate headline selection, protection of manual headline edits,
whitespace normalization, dry runs without mutation, unchanged timestamps,
duplicate selectors, daily skipping, failed submission journaling, and blocking
retries after uncertain saves. Simulated UI workflows do not execute Chromium.

## Live-test boundary

The two public login checks used the actual websites and required no account
data. No dummy credential was submitted because a rejected login cannot reach a
profile page or exercise this updater: the application deliberately accepts no
login credentials and instead reuses a browser session created by the operator.
The live checks therefore establish current page reachability only.

Authenticated Naukri/Hirist selectors, resume selection, upload confirmation,
last-updated values and recruiter visibility were not tested. These require a
real test account, current per-account selectors and a harmless resume that the
account owner authorizes for upload. No authenticated profile session or
profile mutation was used.

## Other checks not executed

Eight optional Chromium tests were skipped because the browser binary was not
available. Browser-download attempts failed with invalid/truncated ZIP payloads
in this environment. The optional tests are included and use intercepted mock
HTTPS routes; they do not access real job portals.

Windows task registration and sign-in/unlock/wake triggers were not executed on
a Windows machine. Indeed remains a manual reminder.

## Checks on your laptop

1. Install Chromium with `python -m playwright install chromium`.
2. Run `python -m pytest -q -ra`; all 35 cases should execute when Chromium and
   its required system dependencies are installed.
3. Configure your resume path and all live selectors. Disable unused sites.
4. Run `validate`, then `run --dry-run`.
5. Run one update and compare the visible profile update date yourself.
6. If the script reports `needs_review`, inspect the live profile before reset.
7. Install the Windows scheduler, start its task manually and inspect its log.
8. Unlock or wake the laptop to check trigger delivery.

Follow [`SETUP.md`](SETUP.md) for the command-by-command Windows procedure.

A zero test exit code with skipped cases is not evidence that browser tests
passed. `verified` in the application means its selected content/date evidence
passed, not that recruiter ranking improved.
