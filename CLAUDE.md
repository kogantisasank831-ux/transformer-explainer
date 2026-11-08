# Shared engineering guidance

Read [AGENTS.md](AGENTS.md), the nearest component [PROJECT_LOGIC.md](PROJECT_LOGIC.md), sibling [WORK_PROGRESS.md](WORK_PROGRESS.md), and more specific component instructions before work. Component-local files supersede these root toolkit examples for that component.

## Project memory files

- `PROJECT_LOGIC.md` is the durable current baseline: accepted business rules, complete processes and states, input/output contracts, implementation status (`not_started`, `active`, `implemented`, `parked`, `superseded`), separate verification/release status, code/test traceability and future change-impact notes.
- `WORK_PROGRESS.md` is the transient resume point: only the current active or blocked work item, applicable logic revision/IDs, branch/commit/dirty state, files and environment in flight, actual checks, blockers and the first exact next action.
- `docs/decisions/` preserves why significant choices were made. SRS, API/event schemas and plans remain authoritative sources linked from project logic rather than copied wholesale.

At session start, verify the progress file's branch, commit, working tree and environment, then load the referenced logic IDs. Treat stale progress as evidence to reconcile. Do not infer accepted behavior from code, a database, chat, or an old checkpoint.

During work, checkpoint `WORK_PROGRESS.md` after material discoveries or failures and before a context limit or workday ends. Move stable accepted process, input/output and dependency facts into `PROJECT_LOGIC.md` promptly. On completion or parking, update durable status, verification, code/test links, parked reason/restart condition and change-impact notes, then clear old active detail or replace it with the next item.

Different workflows maintain different evidence: requirements and SRS validation establish accepted processes and known contracts; repository assessment records observed behavior and discrepancies; planning creates the active handoff; coding maintains and closes it; tests update actual verification evidence. An answer is not acceptance, `implemented` is not `verified`, and `released` is not `production_verified`.

Select an available workflow from [skills/README.md](skills/README.md); read its `SKILL.md` and only relevant references. Scope workflows to the requested backend, native or data science component and apply ML concerns only where relevant. Follow the shared local/CI/server test policy in AGENTS.md; diagnostic or smoke success does not waive candidate gates or authorize deployment.

For a new product, consequential feature or productionization task, follow [the end-to-end lifecycle](docs/END_TO_END_PROJECT_LIFECYCLE.md). Record the current G0–G7 gate in project logic and progress. Do not implement domain behavior for an affected slice until `G1_SRS_LOGIC`, `G2_ARCHITECTURE_CONTRACTS` and `G3_PLAN_TEST_STRATEGY` pass or explicitly permit that named independent slice. At release, require `G5_EXACT_CANDIDATE`; unit tests alone, stale evidence or smoke alone cannot permit deployment.

The complete registry contains 91 workflows. Load only what the task needs rather than copying skill instructions into this file.
