# Current work: [project/component]

Status: `active`, `blocked`, or `no_active_work`  
Last updated: [ISO timestamp and author/session when known]

This is a transient resume file. Keep only current active or blocked work. Durable rules, accepted decisions, completed/parked status, process definitions, contracts and future impact notes belong in `PROJECT_LOGIC.md`. Never store credentials, secret values, personal records or large logs here.

## Resume first

- Work item ID and objective: [ID; one bounded outcome]
- Current phase/status: [discovery / requirements / design / implementation / testing / release / blocked]
- Current delivery gate: [G0–G7; outcome; exact permitted slice; evidence link; next gate]
- Logic path, revision and applicable IDs: [PROJECT_LOGIC.md; revision; rule/process/input/output IDs]
- Branch/worktree and last known commit: [values]
- Dirty or uncommitted state: [exact files and whether changes are saved]
- Last verified checkpoint: [what is known to work, with command/evidence]
- Exact next action: [first concrete action or command for the next session]
- Current blocker and owner: [decision/dependency/access; or none]

## Active scope and boundaries

- In scope / out of scope: [values]
- Accepted behavior and definition of done: [IDs and concise outcome]
- Inputs currently being traced or changed: [IN IDs, sources, schemas, DB tables/queries, examples]
- Outputs and effects currently being traced or changed: [OUT IDs, destinations, schemas, state/events/errors]
- Dependencies and impact triggers: [services, events, fields, processes, migrations, model/index/prompt identities]

## Current implementation state

| Area/file/symbol | Current change or observation | Status | Risk/decision needed | Next action |
|---|---|---|---|---|
| [Path] | [Concise state] | [active/blocked/verified for this work item] | [Value] | [Action] |

Record database/schema/config/environment state when relevant, including migrations applied only in disposable environments. Do not copy full source files or command logs.

## Decisions and discoveries during active work

| ID | Discovery, proposal or answer | Evidence/source | Acceptance state | Required durable update |
|---|---|---|---|---|
| [ID] | [Value] | [Path/output/owner] | [observed/proposed/answered/accepted] | [PROJECT_LOGIC section/ID or pending] |

Observed code or DB behavior does not automatically become accepted business logic. Transfer stable accepted facts promptly; do not wait for session close if losing them would make resumption unsafe.

## Verification ledger

| Command/check | Candidate/environment | Result | Failure/skip/limit | Next verification |
|---|---|---|---|---|
| [Command] | [Identity] | [Pass/fail/not run] | [Evidence] | [Action] |

## Ordered next steps

1. [Exact next action]
2. [Following action]
3. [Verification or handoff]

## Closeout checklist

When the work becomes implemented, parked, superseded or otherwise inactive:

1. Update `PROJECT_LOGIC.md` with the final implementation status, accepted process, input/output contracts, code/test references, verification/release state and future change-impact notes.
2. Record a parked reason, blocker owner and restart condition in `PROJECT_LOGIC.md` when applicable.
3. Move important rationale to a decision record; keep large test/build artifacts in their normal systems.
4. Remove completed history from this file and set it to `no_active_work`, or replace it with the next active work item.

A future session must verify branch, commit, working-tree state and external environment before trusting this handoff.
