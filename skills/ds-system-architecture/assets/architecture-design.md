# System architecture: [project/component]

Replace placeholders with evidence or explicit unknowns. Scale depth to the request. Treat a completed document as a design, not proof of runtime behavior or stakeholder acceptance.

## Baseline and design scope

- Objective and named next activity: [values]
- Source SRS/PROJECT_LOGIC/repository revisions and accepted rules: [sources and IDs]
- Current state versus target changes: [evidence and proposed scope]
- Delivery stage, users, team/operations constraints, exclusions: [values]
- Confirmed functional and quality constraints: [IDs; units and measurement boundary]
- Proposed assumptions, unresolved business decisions, and blocking scope: [IDs and status]

## Options and selected approach

| Decision ID / relevant rules | Plausible options | Benefits and costs/failure burden | Selected or proposed choice and rationale | Evidence, authority, and revisit condition |
|---|---|---|---|---|
| [ID] | [Meaningful alternatives] | [Tradeoffs] | [Status and reason] | [Sources, not inferred approval] |

## Components and boundaries

[Add compact context/component/deployment views only when they clarify topology, trust, resource isolation, or branching. Separate logical modules from network services.]

| Component ID | Responsibility / rule IDs | Owned state and source of truth | Interfaces/dependencies and trust context | Logical and deployment/resource boundary |
|---|---|---|---|---|
| [ID] | [Scope] | [State] | [Contract IDs and identity/tenant context] | [Process/service/job; rationale] |

## Contracts and critical journeys

| Contract / flow ID | Input, actor and authorization | Success/state/side effect | Error, timeout, duplicate/concurrency, partial-failure and cancellation behavior | Version/consistency and recovery owner |
|---|---|---|---|---|
| [ID] | [Validated boundary] | [Outcome] | [Explicit behavior or decision IDs] | [Rules and owner/unknown] |

Define atomic boundaries, acknowledgment versus completion, retries/reconciliation, queue admission/backpressure, cache freshness/isolation, and external dependencies as applicable. Mark remaining detailed API/schema work explicitly.

## Data and model lifecycle

[For ordinary backend work, mark ML/GenAI areas not applicable with a reason.]

- Data contracts, rights, provenance, label/time availability and quality controls: [values]
- Preprocessing/splits/training/evaluation and inference parity: [boundaries and evidence]
- Data/model/prompt/config versions, artifact promotion and rollback: [compatibility and ownership]
- RAG/agent grounding, retrieval/tool authority, checkpoint/state isolation and limits: [applicable mechanisms]
- Evaluation/quality feedback and release gates: [confirmed versus proposed thresholds/ownership]

## Operating and security design

- Workload shape, resource topology and bottlenecks: [evidence or assumptions; no inferred RPS from users]
- Latency/availability/recovery/cost constraints and estimates: [units, boundary, assumptions, validation required]
- Authentication, authorization/tenants, secrets/configuration, egress, redaction and audit: [mechanisms tied to rules]
- Dependency degradation, admission control, startup/shutdown, observability and operational ownership: [behavior]
- Backup/restore, release/data/schema/model compatibility and rollback limits: [design]

## Evolution and verification

| Rule/requirement ID | Design component/contract or mechanism | Planned proof or actual evidence | Open dependency / owner |
|---|---|---|---|
| [ID] | [Link] | [Test/analysis/inspection/experiment; actual state] | [Scope] |

- Current-to-target sequence, coexistence/backfill/cutover and recovery: [steps or not applicable]
- Highest-impact risks, missing decisions and feasibility questions: [scoped priorities]
- Checks actually performed versus planned: [evidence; no invented measurements]
- Named-next-activity readiness: [ready / conditionally ready / blocked and why]

## Coding handoff and knowledge synchronization

- Logic and architecture revisions, accepted rules, selected component/contract IDs: [values]
- Boundaries, allowed technical choices, failure cases and verification expected by implementation: [values]
- Blocked work and independent work that can proceed: [scope and dependencies]
- Authoritative architecture path and PROJECT_LOGIC.md link/update: [actual persisted or proposed status]
- Significant decision-record links and business decisions still pending: [sources]
- Specialist follow-up: [task; verify a skill exists before claiming installation]
