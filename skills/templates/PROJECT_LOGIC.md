# Project logic: [project/component]

Status: draft template, not accepted requirements. Replace placeholders with evidence. Keep this as a concise index and split large domains into linked documents.

## Scope, users, and sources

- Purpose, user decisions, and business outcomes: [values]
- Component boundary, exclusions, delivery stage: [values]
- Owner and last verified date/revision: [values or unknown]
- Sources: [S-ID, document/section or statement, version/date, authority, limitations]
- Glossary: [domain terms, units, timezones, rounding, null/absent meanings]

## Business rules and invariants

| Rule ID | Condition and required behavior | Exceptions / invariant | Source | Confirmed/proposed/unresolved; acceptance | Code and verification links |
|---|---|---|---|---|---|
| [RULE-ID] | [One explicit rule] | [Value] | [S-ID] | [Status and evidence] | [Paths/test IDs or pending] |

## Workflows and state transitions

| Flow/state | Actor and trigger | Preconditions and authorization | Action / next state | Failure, cancellation, duplicate, and concurrent behavior |
|---|---|---|---|---|
| [ID] | [Value] | [Rules] | [Outcome] | [Behavior or Q-ID] |

Define normal, alternative, and terminal outcomes. Record which external or financial side effects require explicit authority and which operations must remain atomic or idempotent.

## Data and interface contracts

- Entities, ownership, identifiers, schema links, constraints, and retention/deletion: [values]
- API/event/job/file input/output schemas and error behavior: [links or open decisions]
- Transactions, consistency, migrations, concurrency, retries, and unknown outcomes: [rules]
- Integrations, permissions, tenant boundaries, audit, and provider constraints: [rules]
- ML/GenAI only: targets, label timing, data/model/prompt versions, evaluation population/splits/metrics, quality gates, tool limits, grounding, and fallback: [values or not applicable with reason]

## Acceptance and operating constraints

| Requirement/rule IDs | Observable criterion and environment/workload | Verification method | Planned or executed; evidence |
|---|---|---|---|
| [IDs] | [Threshold or explicitly unresolved decision] | [Test/analysis/inspection/demonstration] | [Actual state] |

Capture latency boundary, throughput, cost, availability, recovery, monitoring, and release compatibility when relevant. Do not substitute model quality for service correctness or invent missing numeric targets.

## Open decisions and assumptions

| Q/A-ID | Question or assumption | Options and impact | Affected rules / blocked work | Owner | Open/answered/deferred; assumption acceptance |
|---|---|---|---|---|---|
| [ID] | [Value] | [Alternatives] | [Exact scope] | [Owner or unassigned] | [Evidence] |

## Decisions and change control

Link significant choices in the project's `docs/decisions/` using the [ADR template](ADR.md) from the shared toolkit. When copying this template into a project, replace that relative link with the actual template location or remove it after use.

Update rules, contracts, and verification references together. Preserve stable IDs and explicitly supersede old decisions. Record contradictions between intended and implemented behavior for resolution. Keep credentials, sensitive records, and client-confidential details out of this file.
