# Backend and data science requirements baseline

Replace bracketed instructions with project evidence. Label unknowns explicitly. Omit irrelevant detail with a reason; do not present this unfilled template as completed analysis.

## Context and evidence

- Project and baseline version/date: [value]
- Intended next activity: [feasibility experiment / architecture / implementation planning / another activity]
- Stage and workload: [analysis / prototype / production; applicable workload]
- Source register: [source ID, location/section, version/date, authority, limitation]
- Business outcome and current baseline: [evidence or pending decision]
- Actors and owners: [roles; use unassigned where unknown]
- Scope, exclusions, constraints, and glossary: [values]

## Required process

[Actor → trigger → inputs → decisions/states → output/action → terminal outcome. Include relevant alternative and failure flows.]

## Requirements register

| ID | Statement | Source/rationale | Evidence status / acceptance | Priority/owner | Acceptance criterion and verification method | Dependencies |
|---|---|---|---|---|---|---|
| [BR/FR/DR/ER/NFR/ENG-ID] | [One behavior or constraint] | [Source ID/section] | [confirmed/proposed/unresolved; accepted/pending/rejected] | [Value or unknown] | [Observable criterion; test/analysis/inspection/demonstration; mark pending thresholds] | [Requirement/decision/assumption IDs] |

## Data and evaluation contract

For backend-only work, complete the backend contract below and mark ML-specific fields not applicable with a reason. Do not invent a model or dataset requirement.

- Unit, target, horizon, feature availability, and label timing: [value or open decision]
- Sources, access rights, schemas, provenance, quality, and permitted use: [value or open decision]
- Baseline, evaluation population, splits, leakage prevention, and important slices: [value or open decision]
- Metrics, aggregation, uncertainty, acceptance thresholds, and decision owner: [confirmed/proposed/unresolved]
- Reproduction inputs and model/data/config/prompt lineage: [applicable artifacts]
- Relevant GenAI/agent requirements: [grounding, permissions, evaluation, budgets, recovery; or not applicable with reason]

## Backend contract

- Entities, ownership, business invariants, states, and transitions: [confirmed rules or decisions]
- API/worker/integration input/output and error contracts: [schemas or unresolved fields]
- Authentication, authorization, tenant scope, and sensitive operations: [rules or decisions]
- Persistence, transaction boundaries, migrations, and consistency: [constraints or decisions]
- Duplicate requests, concurrency, retries, cancellation, and unknown outcomes: [behavior or decisions]
- Webhooks, external systems, versioning, and compatibility: [applicable contracts]
- Load, latency boundary, failure/recovery policy, and operational owner: [measurable targets or unresolved decisions]

## Coverage and engineering constraints

| Area | Covered / open / not applicable | Requirement or decision IDs; rationale |
|---|---|---|
| Business scope and process | [status] | [IDs/reason] |
| Functional behavior and contracts | [status] | [IDs/reason] |
| Data, rights, labels, and lineage | [status] | [IDs/reason] |
| Evaluation and scientific validity | [status] | [IDs/reason] |
| Reproducibility and coding quality | [status] | [IDs/reason] |
| Security, privacy, and access | [status] | [IDs/reason] |
| Performance, scale, and cost | [status] | [IDs/reason] |
| Failure behavior and operations | [status] | [IDs/reason] |

## Decision and assumption register

| ID | Question or assumption; source/gap | Options and consequences | Affected IDs and blocked activity | Owner | Status / answer / acceptance evidence |
|---|---|---|---|---|---|
| [Q/A-ID] | [Specific issue] | [Alternatives] | [Exact scope] | [Owner or unassigned] | [open/answered/deferred; assumptions proposed/accepted/rejected] |

## Verification and traceability

| Requirement IDs | Proposed scenario or evidence | Expected outcome or pending decision | Verification owner | Planned / executed; actual evidence |
|---|---|---|---|---|
| [IDs] | [Positive/negative/scientific/operational scenario] | [Observable result] | [Owner or unknown] | [Do not invent execution] |

## Readiness and handoff

- Readiness for the named next activity: [ready / conditionally ready / blocked, with evidence]
- Highest-impact unanswered questions: [up to three for the next clarification round]
- Independent work that can proceed: [bounded activities]
- Blocked work and dependencies: [specific activities and Q/A IDs]
- Recommended next activity: [justified handoff or feasibility experiment with exit criterion]
- Stakeholder acceptance: [actual evidence or pending; never infer approval]
