# Quality scenario selection

Apply only relevant concerns and preserve explicit open fields. These are prompts for testable contracts, not universal numeric targets or mandatory technologies.

## Backend and shared software concerns

| Area | Establish in the requirement |
|---|---|
| Performance | Journey and latency boundary; acknowledgment versus complete outcome; percentile; input/response mix; arrival pattern, burst/duration, warm/cold/cache/dependency state; errors and saturation. |
| Scalability | Workload/data growth dimensions, useful throughput, contention and saturation signals, accepted degradation/overload behavior, target horizon, and representative scale points. Do not equate registered users with concurrency. |
| Availability | Useful outcome, eligible request or time denominator, window, exclusions and dependency policy, partial availability, low-traffic/no-traffic handling, and ownership. |
| Recovery and durability | Failure scenario, detection/start event, restored capability, RTO, permitted lost data/RPO, acknowledged-write integrity, reconciliation and restore proof. |
| Security/privacy | Applicable authorization/tenant boundaries, sensitive-data handling/egress, retention/deletion, audit, secrets and verification conditions. Link deterministic policies; do not claim zero risk or legal compliance from sample tests. |
| Operability | Detection/diagnostic signals, actionable ownership, redacted observability, configuration validation, shutdown/startup, release/migration compatibility, and recovery/runbook evidence. |
| Maintainability/testability | Relevant change scenario, bounded interfaces, validated/typed contracts where appropriate, reproducible build/checks, meaningful regression evidence and compatibility; avoid arbitrary lines-of-code or coverage percentages. |
| Portability/interoperability | Supported runtime/platform/client/version combinations, interchange/schema contract, dependency constraints, backward compatibility and verification scope. |
| Usability/accessibility | Relevant API/client/operator workflow, actionable errors/docs and supported access needs; defer UI-specific criteria when there is no UI in scope. |
| Cost/resources | Workload-normalized and total cost, accounting period, included resources, peak/headroom/memory/storage/bandwidth assumptions, hard limits, and quality/failure tradeoffs. |

For asynchronous jobs, distinguish admission, durable persistence, queue delay, execution, usable completion and external notification. Define whether retries are new attempts or the same logical job, and how each population is measured.

For consequential side effects, preserve accepted business invariants such as idempotency and authorization. A fast acknowledgment cannot substitute for durable acceptance or exactly-once external effects.

## Data science and analytical products

- Define data freshness/completeness/validity at the correct event-time/ingestion-time boundary, units, source version, late-arrival policy, and useful-output deadline.
- For batch analysis/forecasting, specify input cutoff, output grain/horizon, release deadline/timezone, eligible population, rerun/backfill and incomplete-output behavior. Avoid turning one-off research into an always-on service requirement.
- For model quality, link task-appropriate evaluation requirements: population, frozen dataset/version and split, baselines, error costs, slices/support, uncertainty, acceptance threshold/pending decision and authority. Do not substitute accuracy for the actual business loss.
- Keep preprocessing/feature selection/tuning leakage-safe and deployment-time data availability explicit. Reproducibility needs data/code/environment/config/model lineage and a tolerance where exact reproducibility is infeasible.
- For optimization, include feasibility, constraint violations and objective units in addition to solver runtime; a quick infeasible answer is not useful success.
- Separate offline training/evaluation resources and completion from online inference, and distinguish software contract validity from scientific validity and product utility.

## RAG, LLMs and agents

- Measure usable answers/task completion separately from transport success and token emission. Define grounding/citation support, abstention/coverage, important slices and adjudication; report judge limitations.
- Separate first-token, full-response, tool/task completion, queue time and input/output token distribution. Cache-hit speed and a short answer do not establish performance for the complete workload.
- Define budgets for tokens, context, steps, execution time, spend and parallelism only with source values or explicitly proposed rationale. Specify limit/timeout behavior, including partial side effects and recovery.
- Preserve data processing/egress and retrieval/cache/session/checkpoint isolation. Never meet a cost/latency target using an unapproved external provider or weaker authorization.
- Define source/prompt/model/config/retrieval versioning and withdrawal/deletion freshness at retrieval, caches, conversation reuse and response release where policy requires it.
- Specify fallback/abstention/outage outcomes and their classification in quality and availability metrics. A fast refusal or dependency error must not count as a correct grounded answer by default.
- Account for model-quality drift and delayed feedback with an owner and decision policy; do not invent autonomous retraining or feedback retention obligations.

## Scope and decisions

Mark ML concerns not applicable for ordinary backend work. Treat policy choices such as maintenance exclusions, allowed data loss, fallback actions, retention, fairness slices, and acceptance thresholds as source-backed or explicitly pending, rather than hiding them inside metric definitions.
