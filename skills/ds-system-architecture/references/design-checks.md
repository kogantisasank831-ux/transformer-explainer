# Architecture design checks

Use these as design prompts, not a compulsory list of technologies. Apply a concern only where the product needs it and trace decisions to rules or constraints.

## Backend responsibilities and contracts

| Concern | Establish in the design |
|---|---|
| Domain boundaries | Entities, invariants, state machines, ownership, transaction scope, and modules; distinguish a logical module from a network service. |
| API boundary | Identity/tenant propagation, validated schemas, error outcomes, pagination/versioning, upload/download limits, and compatibility ownership. |
| Persistence | Source of truth, constraints, concurrency control, consistency requirements, query/access shape, migrations/backfills, retention/deletion, and recovery. |
| Async work | Submission acknowledgment versus completion, durable state/dispatch, idempotency scope, worker acknowledgment/retry, order/replay, and cancellation races. |
| Side effects | Authorization, invariant/transaction boundary, external-call outcome reconciliation, deduplication limits, compensation, and audit needs. |
| Caching | Justification, isolation and authorization, invalidation/freshness, stale serving policy, stampede handling, and bypass/dependency failure. |
| Integrations | Contract/version ownership, quotas/timeouts, webhook authentication/replay, unknown outcomes, sandbox evidence, and provider outage. |

For example, a database transaction cannot by itself guarantee an external notification or payment effect exactly once. Choose a mechanism matching the required invariant and the external system's capabilities; state residual failure modes. Avoid a distributed transaction or broker merely to decorate a simple design.

## Data science lifecycle

- Define ingestion contracts, schema/version and units/timezones, provenance, event/availability time, labels, rights, quality/freshness controls, and the destination of bad or stale records.
- Keep preprocessing fit, feature selection, and tuning within appropriate training partitions. Package fitted transformations with the estimator or specify a versioned equivalent contract; define inference parity and compatibility checks.
- Separate data/model/prompt/config lineage from source versioning. Define immutable release references and promotion/rollback semantics; do not claim reproducibility from a random seed alone.
- Design evaluation against the deployment population, baseline, time/entity dependence, important slices, uncertainty, and agreed business loss. Keep numeric release gates and policy authority explicit or unresolved.
- Distinguish offline research/training/evaluation jobs, batch scoring, online inference, and downstream business actions. Select deployment/resource separation for actual lifecycle, memory, latency, or isolation needs.
- For forecasting, carry issue time, horizon/grain, future-feature availability and temporal backtesting. For optimization, carry hard/soft constraints, feasibility tolerances, solver budgets and infeasible-result behavior.
- Define model/data drift and delayed-label feedback ownership, monitoring/review, safe rollback, and how retraining is triggered and validated. Do not mandate autonomous retraining without an accepted policy.
- For a one-off analysis, use a reproducible analytical pipeline and output contract when sufficient; do not invent a continuously operated service.

## RAG and agents

- Track corpus/source versions, effective dates, permission propagation, ingestion/deletion updates, and provenance needed for grounding/citations.
- Enforce tenant/role filters in actual retrieval and storage paths and isolate cache/session/checkpoint state; do not use prompt text as access control.
- Define tool contracts and authority outside the model, validated arguments/outputs, approval/human paths required by policy, and recovery after partial external effects.
- Bound steps/time/tokens/cost/parallelism; define checkpoint ownership, replay/idempotency, cancellation, expired state, and outcome reconciliation.
- Separate retrieval quality, answer quality, tool/task success, latency and cost. Define representative evaluation cases and release comparisons; an LLM judge alone is not proof of correctness.
- Specify provider/model changes, data processing/egress restrictions, fallback, unsupported answers, unavailable retrieval/inference, and user-visible degraded behavior.

## Operations and resource boundaries

- Define logical and deployment views, stateful/stateless parts, process lifecycles, resource pools, backpressure, admission limits, dependency budgets, and safe shutdown.
- Identify tenant isolation, audit/redaction, configuration/secrets, health/readiness, logs/metrics/traces, service/quality objectives, incident ownership, and restore/recovery tests.
- For CPU/GPU serving, account for model weights, runtime overhead, activations/KV/cache where applicable, input/output/context distributions and queueing. Use actual benchmark/version evidence before asserting feasible concurrency or latency; label estimates and headroom assumptions.
- Preserve measured requirements separately from recommended budgets. Distinguish request rate, in-flight concurrency, registered users, and batch volume; user population alone does not specify arrival rate.
- Compare total operating cost and unit cost using workload, utilization and pricing assumptions. Verify current prices/specifications if using real provider/hardware numbers.
- Keep deployment/rollback and schema/data/model compatibility in the design. For multi-version coexistence, describe which components can read/write old and new contracts and how partial cutovers recover.
