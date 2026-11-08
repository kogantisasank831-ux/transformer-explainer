# Job profile updater logic

Baseline revision: import-2, 2026-11-08. Owner: repository owner.
Scope: import the previously delivered updater, add setup instructions, and
record public login-flow evidence without changing runtime behavior. The user's
current request authorizes source publication and a dummy-account website test,
but no authenticated test account was available. No live profile update or
laptop task installation was performed.

## Sources and status

- S1: User requested daily Naukri, Hirist and Indeed profile freshness updates, then resume re-upload, profile edits, scheduling, validation and a simple guide in the preceding conversation.
- S2: `Daily_Profile_Updater.zip`, version 2, delivered 2026-10-03. SHA256: `8593dd644a26e35312f3187003af2088e10897f0c684f298c82bd293a16d6dfb`.
- S3: User requested publication to the transformer repository on 2026-11-08.
- S4: User requested setup documentation and an actual-website test using dummy
  credentials on 2026-11-08.
- Existing source files are imported byte for byte from S2. This document and `WORK_PROGRESS.md` record the component boundary required by the repository's agent instructions.
- Implementation exists. Local evidence is distinct from CI, Windows scheduling, authenticated site behavior and recruiter visibility.

## Capabilities and change impact

| ID | Observed behavior and acceptance | Implementation | Verification | References and change impact |
|---|---|---|---|---|
| JPU-001 | Upload the configured resume or alternate approved text versions; retain the optional whitespace strategy. Accepted feature direction in S1; exact selectors are operator inputs. | Implemented | Local mocked flows; browser/live checks incomplete | `profile_updater.py`: `update`, `next_variant`, `resume_file`; `test_profile_updater.py`. Changes to file controls, headline text or upload stages require rechecking this flow. |
| JPU-002 | Require persisted content evidence and a changed selected last-updated value before reporting verified. Observed implementation; no claim of ranking benefit. | Implemented | Mocked cases pass; platform date semantics unresolved | `read_timestamp`, `update`. Changing the selector/attribute or display precision requires re-review with the owner. |
| JPU-003 | Journal before potentially saving, block uncertain outcomes until manual reset, and skip verified sites within the same configured day. Accepted reliability direction from S1. | Implemented | Local state/recovery tests pass | `should_skip`, `run_profiles`, `save_state`. Re-review state compatibility, timezone and retry behavior when changing these fields. |
| JPU-004 | Provide Windows sign-in, unlock, wake-event and daily triggers; Indeed remains a manual reminder. Observed implementation. | Implemented | XML checked previously; task registration and live delivery unverified | `install_scheduler.ps1`, `run_scheduled.ps1`, `remove_scheduler.ps1`. Any trigger/policy change requires Windows verification. |

## Process and input output contracts

- PROC-01: Read YAML, validate configured profiles, acquire the local run lock and read daily state. A manual site generates a reminder. An auto site reads the update indicator, resolves controls and chooses its proposed edit. Dry run ends without saving. A real run journals `submitted`, performs the action, reopens the page and checks evidence. The terminal state is `verified` or `needs_review`; errors after submission remain blocked for review.
- IN-01: CLI commands are `validate`, `login`, `run`, `status` and `reset`; options include `--config`, `--site`, `--dry-run` and `--inspect`.
- IN-02: YAML profile settings, user-maintained selectors, manual browser login and a local PDF/DOC/DOCX resume. See `README.md` and the example configurations for defaults, size limits and supported controls.
- OUT-01: Site upload/profile-edit side effects occur only when the operator runs configured automation. This import performs none.
- OUT-02: Local runtime state, browser cookies and scheduler logs. Keep runtime data private and excluded from Git. `verified` describes the configured checks; `reminded` does not mean a profile edit occurred.
- Recovery: `submitted` and `needs_review` block resubmission across days. The operator must inspect the live result before `reset --site NAME`. Reset clears local tracking and does not undo site edits.

## Verification and delivery evidence

On 2026-11-08, the recovered source suite returned **27 passed and 8 skipped**
on Python 3.12/Linux. The eight Chromium cases were skipped because the browser
executable was unavailable. Compilation passed. Source-file parity with S2 was
checked before adding these component records. The current public Naukri login
form and Hirist login dialog were inspected successfully. Dummy credentials
cannot exercise profile updates, and no authenticated account was used.
Historical checks and laptop instructions remain in `VALIDATION.md`; the Word
guide is included unchanged and `SETUP.md` provides a concise current procedure.

| Gate | Scope and outcome | Next boundary |
|---|---|---|
| G0_CONTEXT_BOUNDARY | PASS for isolated source import into `job-profile-updater/`. Root web/native projects are outside scope. | Existing source baseline |
| G1_SRS_LOGIC | CONDITIONAL for byte-preserving source import only; S1/S2 establish the historical implementation. | New domain behavior requires reviewed rules |
| G2_ARCHITECTURE_CONTRACTS | CONDITIONAL for source import only; observed interfaces are recorded above. | New architecture requires review |
| G3_PLAN_TEST_STRATEGY | PASS for import checks: archive recovery, parity, manifest inspection, compilation and existing suite. | Local checks |
| G4_IMPLEMENT_LOCAL | CONDITIONAL: source and mocked checks pass; eight browser cases remain skipped. Public login flows are reachable. | Authenticated browser/Windows verification |
| G5_EXACT_CANDIDATE | BLOCKED for deployment: no candidate-specific CI or real-site evidence is claimed. | Required CI and applicable suites |
| G6_RELEASE_VERIFY | BLOCKED for runtime release: no laptop task or authenticated profile action is installed/executed. | Operator setup and supervised smoke checks |
| G7_OPERATE_LEARN | BLOCKED for production verification: no live outcomes observed. | Evidence from the actual target environment |

## Open operational decisions

The owner must supply the resume, logged-in profile URLs, current selectors and a meaningful last-updated indicator. Coarse values such as Today can produce an inconclusive result. Windows wake-event availability varies by hardware. Changes to platform UI or automation permissions require rechecking the affected integration. No application CI, live portal session or scheduler installation is inferred from this source import.
