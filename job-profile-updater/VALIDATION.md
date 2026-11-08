# Validation results

Completed for the updated package on 3 October 2026.

## Executed successfully

- Python compilation checks.
- 27 pytest checks passed: pure logic, YAML validation, and simulated UI workflows.
- Valid-configuration CLI smoke check returned zero.
- Default unconfigured YAML was correctly rejected before browser launch or editing.
- Windows Task Scheduler XML parsed successfully; trigger ordering was checked
  against Microsoft's published schema.
- Guide rendered into three pages and each page was visually inspected.

The executed tests include resume file selection, local file path and size
validation, alternate headline selection, protection of manual headline edits,
whitespace normalization, dry runs without mutation, unchanged timestamps,
duplicate selectors, daily skipping, failed submission journaling, and blocking
retries after uncertain saves. Simulated UI workflows do not execute Chromium.

## Not executed

Eight optional Chromium tests were skipped because the browser binary was not
available. Browser-download attempts failed with invalid/truncated ZIP payloads
in this environment. The optional tests are included and use intercepted mock
HTTPS routes; they do not access real job portals.

Live Naukri/Hirist selectors, actual upload behavior, last-updated values and
recruiter visibility were not tested. No authenticated profile session was used.
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

A zero test exit code with skipped cases is not evidence that browser tests
passed. `verified` in the application means its selected content/date evidence
passed, not that recruiter ranking improved.
