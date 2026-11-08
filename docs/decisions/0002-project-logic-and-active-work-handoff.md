# 0002: Separate durable project logic from active work handoff

- Status: implemented.
- Date: 2026-11-08.
- Source: user requirement for business logic, implementation status, process and input/output contracts to persist across sessions while current unfinished work remains easy to resume.
- Scope: shared engineering toolkit and component-local documentation protocol.

## Context

`PROJECT_LOGIC.md` already holds accepted product behavior, but session checkpoints, partial edits, failed commands and exact next actions have a different lifecycle. Mixing them makes the durable baseline noisy and makes a new programmer search old history to find the current resume point. Keeping only chat history is fragile when a context limit or workday ends.

## Decision

- Keep a component-local `PROJECT_LOGIC.md` as the durable current business and engineering baseline.
- Keep a sibling `WORK_PROGRESS.md` as the transient resume point for current active or blocked work.
- `PROJECT_LOGIC.md` records accepted processes, business rules, input/output contracts, implementation status, verification/release status, code/test traceability, parked reasons and future change-impact notes.
- `WORK_PROGRESS.md` records the active work item, logic revision and IDs, branch/commit/dirty state, current files and environment, discoveries, actual checks, blockers and the exact next action.
- On completion or parking, consolidate durable facts into `PROJECT_LOGIC.md`, then remove the old active detail and set `WORK_PROGRESS.md` to `no_active_work` or replace it with the next active item.
- Requirements and SRS workflows define accepted process and known contracts. Repository assessment records observed behavior without promoting it to accepted intent. Planning opens the active handoff. Coding and testing maintain it and close it by updating durable status and traceability.

## Status model

Acceptance, implementation and verification are independent:

- Acceptance: proposed, accepted, rejected, unresolved or superseded.
- Implementation: not started, active, implemented, parked or superseded.
- Verification/release: unverified, tests planned, locally verified, CI verified, released or production verified.

This prevents “implemented” from being interpreted as tested or deployed.

## Consequences

Agents and programmers must read the nearest component logic and progress files before work. They must verify the recorded branch, commit, working tree and environment rather than trusting a stale checkpoint. Stable facts must not remain only in the transient file. Completed history must not accumulate there.

An impact note should name the dependency and review trigger. For example, if an LR capability consumes `event_type=delivery`, a change to delivery-event semantics or schema must trigger review of the linked logic, process and contract IDs with the coder and named logic owner before implementation.

## Verification

Validate both templates, document links, status vocabulary, closeout rules and the skill responsibility handoffs. This organization preserves knowledge; it does not itself verify application logic or automatically load documents into an external runtime harness.
