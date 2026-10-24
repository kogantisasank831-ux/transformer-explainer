# Nonfunctional requirements: [project/component]

Replace placeholders with evidence or explicit unknowns. Compress for small requests. Do not present this template as an approved or verified quality baseline.

## Scope, sources and intent

- Objective, delivery stage and named next activity: [values]
- SRS/logic/architecture/assessment revisions and related rules: [sources and IDs]
- Critical journeys and business consequences: [values]
- Hard constraints and accepted objectives: [source and authority]
- Qualitative expectations, source-supplied targets, proposals and open decisions: [separate states]
- Decision/operating/verification owners: [roles or unassigned]

## Workload and environment

| Journey/workload ID | Population, arrival/burst/batch model and duration | Input/output/data/token distributions and growth | Runtime/hardware/dependency/cache/warm-cold conditions | Evidence or unresolved fields |
|---|---|---|---|---|
| [ID] | [Values; do not infer request rate from registered users] | [Values or unknowns] | [Versions and boundaries] | [Sources/Q-IDs] |

## NFR measurement register

| Stable ID / linked rules | Stimulus, environment and required response | Metric, units, boundary and eligible population | Target / aggregation / observation window | Source, decision/acceptance state and open fields | Verification method, owner and actual evidence state |
|---|---|---|---|---|---|
| [NFR-ID] | [Scenario] | [Start/end, numerator/denominator, errors/retries/timeouts/rejections] | [Supplied/proposed/pending; percentile/support] | [Source/revision, authority, Q-IDs] | [Planned check; executed results separately] |

Preserve source-supplied target values even when feasibility is unknown. Mark missing policies and proposed thresholds locally. Define how missing telemetry and insufficient sample support affect the decision.

## Coverage and applicable quality guardrails

| Area | Covered / open / not applicable | NFR/ER/FR IDs, boundaries and reason |
|---|---|---|
| Performance and useful throughput | [Status] | [Acknowledgment versus completion; failures/quality] |
| Scalability and resource/cost limits | [Status] | [Workload and evidence] |
| Availability and dependency degradation | [Status] | [Useful outcome, denominator/window/exclusions] |
| Recovery, durability and data integrity | [Status] | [RTO/RPO and restore verification] |
| Security, privacy and access | [Status] | [Applicable policy and verification] |
| Operability, maintainability, testability and compatibility | [Status] | [Change/recovery scenarios] |
| Data freshness, quality and reproducibility | [Status] | [Event/data/artifact boundaries or reason] |
| Model/GenAI quality, task success and bounded execution | [Status] | [Linked evaluation/functional rules or no-ML reason] |
| Usability/accessibility and relevant obligations | [Status] | [Applicable scope; do not invent legal duties] |

## Decisions, feasibility and tradeoffs

| Q/decision ID | Missing target/policy or conflicting expectations | Options/rationale and affected work | Owner and acceptance evidence | Current feasibility/evidence gap |
|---|---|---|---|---|
| [ID] | [Question] | [Scope] | [Source or pending] | [What must be measured; not assumed] |

## Verification and coding handoff

| NFR / linked rule IDs | Instrumentation/source and representative conditions | Method and pass/fail/insufficient-evidence rule | Planned / executed; actual result and limitations |
|---|---|---|---|
| [IDs] | [Environment, workload/window/sample/version] | [Test/analysis/inspection/demonstration] | [Evidence or not run reason] |

- Readiness for the named next activity: [ready / conditionally ready / blocked with dependencies]
- Independent work and exact blocked commitments: [scope]
- Highest-impact questions for the next clarification round: [up to three]
- Logic/NFR/architecture revisions and IDs required by coding/testing: [values]
- Quality document path and accepted-target synchronization into PROJECT_LOGIC.md: [actual or pending persistence]
- Relevant specialist follow-up: [task; verify skill availability]
- Checks actually performed: [evidence; keep benchmark/quality/recovery plans separate]
