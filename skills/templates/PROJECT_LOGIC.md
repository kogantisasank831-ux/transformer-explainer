# Project logic: [project/component]

Status: draft template, not accepted requirements. Replace placeholders with evidence. Keep this as the durable current baseline; put active-session details in `WORK_PROGRESS.md`. Split large domains into linked documents while retaining this index.

## Document contract and status vocabulary

- Logic owner and last verified date/revision: [values or unknown]
- Logic baseline revision and source SRS revisions: [stable revision; sources; actual review state]
- Active-work file: [WORK_PROGRESS.md or established equivalent]
- Acceptance status: `proposed`, `accepted`, `rejected`, `unresolved`, or `superseded`.
- Implementation status: `not_started`, `active`, `implemented`, `parked`, or `superseded`.
- Verification/release status: `unverified`, `tests_planned`, `locally_verified`, `ci_verified`, `released`, or `production_verified`.

Keep these dimensions separate. `implemented` means code exists; it does not mean tests, CI, deployment, or production verification passed. An `active` row points to the active-work file for transient details.

## Delivery stage gates

Follow the repository end-to-end lifecycle. A gate is `PASS`, `CONDITIONAL`, or `BLOCKED`; `NOT_APPLICABLE` is allowed only for a reasoned optional specialist check, not for G0–G7 themselves. A conditional gate must name every independent slice it permits. Missing gates block the affected next stage.

| Gate ID | Scope / permitted slices | Outcome | Required evidence and revision | Blockers / affected IDs | Owner and next gate |
|---|---|---|---|---|---|
| `G0_CONTEXT_BOUNDARY` | [Component] | [Status] | [Repository/current-state evidence] | [IDs or none] | [Owner/G1] |
| `G1_SRS_LOGIC` | [Process slices] | [Status] | [SRS coverage, accepted decisions, logic revision] | [Q/rule/process IDs] | [Owner/G2] |
| `G2_ARCHITECTURE_CONTRACTS` | [Slices] | [Status] | [Architecture, contract, NFR and risk revisions] | [IDs] | [Owner/G3] |
| `G3_PLAN_TEST_STRATEGY` | [Slices] | [Status] | [Plan and test-strategy revisions] | [IDs] | [Owner/G4] |
| `G4_IMPLEMENT_LOCAL` | [Candidate scope] | [Status] | [Code revision and local checks] | [Defects/limits] | [Owner/G5] |
| `G5_EXACT_CANDIDATE` | [Source/artifact identity] | [Status] | [CI unit plus applicable suite reports] | [Missing/failed/stale gates] | [Owner/G6] |
| `G6_RELEASE_VERIFY` | [Environment/candidate] | [Status] | [Readiness, smoke, deployment and rollback evidence] | [Release blockers] | [Owner/G7] |
| `G7_OPERATE_LEARN` | [Deployed identity/population] | [Status] | [Telemetry integrity and outcome evidence] | [Unknowns/incidents] | [Owner/re-entry gate] |

Before domain coding, require G1, G2 and G3 to pass or explicitly permit the exact slice. Unit tests alone do not pass G5. Update this table when a dependency-impact change reopens an earlier gate.

## Scope, users, and sources

- Purpose, user decisions, and business outcomes: [values]
- Component boundary, exclusions, delivery stage: [values]
- Sources: [S-ID, document/section or statement, version/date, authority, limitations]
- Glossary: [domain terms, units, time zones, rounding, null/absent meanings]

## Capability and implementation register

| Logic ID | Capability / required behavior | Acceptance status | Implementation status | Verification/release status | Process, input and output IDs | Code/test references | Future change-impact note |
|---|---|---|---|---|---|---|---|
| [LOGIC-ID] | [Stable effective behavior] | [Status/evidence] | [Status] | [Status/evidence] | [PROC/IN/OUT IDs] | [Paths/test IDs or pending] | [Dependency or field whose change requires re-review, affected IDs, coder/owner to consult] |

Impact-note pattern: “Uses `[dependency/field/value]`. Any change to `[trigger]` must re-review `[logic/process/contract IDs]` with the coder and named logic owner before implementation.” Example only: an LR flow that consumes `event_type=delivery` must be re-reviewed when delivery-event semantics or schema change.

## Business rules and invariants

| Rule ID | Condition and required behavior | Exceptions / invariant | Source | Acceptance status and evidence | Code and verification links |
|---|---|---|---|---|---|
| [RULE-ID] | [One explicit rule] | [Value] | [S-ID] | [Status/evidence] | [Paths/test IDs or pending] |

## Processes and state transitions

| Process/state ID | Purpose, actor and trigger | Preconditions and authorization | Steps, decisions and next state | Failure, cancellation, duplicate, concurrent and recovery behavior | Status/source |
|---|---|---|---|---|---|
| [PROC-ID] | [Value] | [Rules] | [Ordered behavior/output] | [Behavior or Q-ID] | [Status/evidence] |

Define normal, alternate, exception and terminal outcomes. Record human/system handoffs, timeouts, retries, compensation, rollback, idempotency, atomicity and externally visible effects where relevant.

## Input contracts

| Input ID | Source and authority | Schema/type, units and required fields | Validation, authorization and edge cases | Version/freshness | Consumers and status |
|---|---|---|---|---|---|
| [IN-ID] | [API/event/DB/file/user/provider] | [Contract/link] | [Rules/errors] | [Identity] | [PROC/LOGIC IDs; status] |

Inputs discovered from code or a database are observed evidence until reconciled with intended behavior. Record null/absent/default semantics, identifiers, time zones, ordering, duplicates, sensitive-data class and ownership where applicable.

## Output and side-effect contracts

| Output ID | Producer and destination | Schema/type and meaning | Side effects, idempotency and errors | Version/compatibility | Consumers and status |
|---|---|---|---|---|---|
| [OUT-ID] | [PROC/service] | [Contract/link] | [Rules] | [Identity] | [Consumers; status] |

Include persisted state, events, notifications, API responses, files, predictions, model/tool actions and audit records. A notification or successful call does not by itself prove the downstream business outcome.

## Data, interfaces, and operating constraints

- Entities, ownership, identifiers, schema links, constraints, history and retention/deletion: [values]
- Transactions, consistency, migrations, concurrency, retries and unknown outcomes: [rules]
- Integrations, permissions, tenant boundaries, audit and provider constraints: [rules]
- Latency boundary, throughput, cost, availability, recovery, monitoring and release compatibility: [values or unresolved IDs]
- ML/GenAI only: targets, label timing, data/model/prompt/index versions, evaluation population/splits/metrics, quality gates, tool limits, grounding, human oversight and fallback: [values or not applicable]

## Acceptance and verification

| Requirement/rule IDs | Observable criterion and environment/workload | Verification method | Planned or executed evidence |
|---|---|---|---|
| [IDs] | [Threshold or unresolved decision] | [Test/analysis/inspection/demonstration] | [Actual status and links] |

Do not substitute model quality for service correctness or invent missing targets. Update verification status only from actual evidence tied to the relevant candidate.

## Open decisions and assumptions

| Q/A-ID | Neutral question/source or assumption | Answer/options and impact | Affected IDs / blocked work | Source/decision maker | Decision and acceptance status |
|---|---|---|---|---|---|
| [ID] | [SRS section/gap] | [Actual answer or pending] | [Exact scope] | [Owner/source] | [Open/answered/deferred and accepted/pending/rejected] |

An answer is not acceptance. Incorporate accepted decisions into the effective capability, rule, process, input/output and acceptance sections; do not leave usable logic only in this ledger, chat, or `WORK_PROGRESS.md`.

## SRS review and logic synchronization

| Logic revision | Source SRS/review and answered Q-IDs | Effective changes and superseded IDs | Acceptance evidence / unresolved conflicts | Implementation and verification synchronization |
|---|---|---|---|---|
| [Revision] | [Sources/IDs] | [Current IDs] | [Evidence/pending] | [Status and links] |

## Decisions and change control

Link significant rationale in the project's `docs/decisions/` using the shared ADR template. Preserve stable IDs, explicitly supersede old behavior and record intended-versus-observed conflicts for resolution. Keep credentials, personal records and client-confidential details out of this file.

Before coding, read this revision and the active-work file, then load the applicable rule/process/input/output IDs and blockers. During closeout, update stable logic, status, code/test links and impact notes before clearing completed or parked details from `WORK_PROGRESS.md`.
