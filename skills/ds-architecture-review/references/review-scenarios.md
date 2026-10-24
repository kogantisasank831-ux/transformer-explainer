# Scenario-driven review

| Scenario | Inspect |
|---|---|
| Request to side effect | Caller/tenant identity, per-resource authority, validation, state invariant, commit boundary, external effect, acknowledgment and ambiguous outcome. |
| Duplicate/race/replay | Key scope and expiry, payload comparison, unique/locking mechanism, stale attempt fencing, cancellation/start races and replayable external actions. |
| Dependency outage | Time budgets, bounded retries, idempotency, isolation, backpressure, queue growth, degraded response and reconciliation. |
| Release/recovery | Compatible schemas/payloads/model versions, immutable artifact identity, restore checks, state integrity, migration/cutover and rollback limits. |
| ML validity | Deployment-time feature availability, leakage-safe preprocessing/evaluation, independent test evidence, inference parity, lineage and quality guardrails. |
| RAG/agents | Permission propagation across source/retrieval/cache/history/tools, withdrawal at response release, checkpoint isolation and bounded effects. |

A finding needs a reachable or well-defined scenario, relevant accepted rule/constraint, evidence, impact, assumptions and a remedy/validation. If a diagram suggests a missing transaction but implementation is unavailable, report the design gap or hypothesis rather than a verified data-loss incident.

Use critical/high/medium/low only with practical impact and explicit confidence. Identify blockers for the named activity separately. Unknown traffic may block capacity promises while permitting isolated module development. Mandatory failed/missing CI gates cannot be treated as successful because other evidence is reassuring.

Review the design selected for this task; do not impose microservices, Kubernetes, a vector database or continuous training without a requirement. Separate remedies that preserve behavior from decisions that change user-visible policy and need source-backed acceptance.
