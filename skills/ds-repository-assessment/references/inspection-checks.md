# Backend and DS inspection checks

Apply relevant rows and mark others not applicable with reasons. Use these prompts to inspect actual implementation; do not label every unchosen technology a gap.

## Shared software baseline

| Area | Inspect and trace |
|---|---|
| Boundaries | Package layout, API/CLI/jobs, domain logic versus transport/persistence, shared dependencies, and dynamic/plugin entry points. |
| Contracts | Typed interfaces where established, schema validation at trust boundaries, null/default semantics, units/timezones, compatibility, and documented error behavior. |
| Failure and resources | Explicit exception boundaries, error translation, cleanup, cancellation, bounded timeouts/retries, and useful redacted logs. |
| Dependencies | Manifests, lockfiles, supported interpreter/runtime constraints, reproducible builds, model/data licenses and obligations needing further review. Do not assert CVEs without current advisory evidence and applicable resolved versions. |
| Configuration | Validation/defaults, environment separation, secret references, hidden runtime assumptions, and configuration precedence. Do not read or emit secrets unnecessarily. |
| Verification | Existing unit/integration/contract/e2e tests, assertions and negative paths, deterministic fixtures, external-service coupling, CI invocation, and reported versus actually verified results. |
| Operations | Build/package/deployment definitions, startup/readiness/shutdown, resource constraints, logging/metrics/traces, ownership, restore/recovery evidence, migration compatibility, and known workload targets. |

## Backend services and workers

- Trace caller identity through permission enforcement and ownership/tenant scoping on both read and write paths; inspect common middleware and storage filters before claiming a check is absent.
- Trace input parsing, upload restrictions, validation, domain transitions, response/error contracts, pagination/filtering, and exposed configuration.
- Inspect persistence constraints, transaction boundaries, session/connection cleanup, migration history, simultaneous update behavior, and cache invalidation where relevant.
- Trace enqueue/acknowledgment, retries, duplicate delivery, deduplication/idempotency, ordering, cancellation, dead-letter/replay handling, and reconciliation after ambiguous external outcomes.
- Trace webhook authentication/replay protection and external side effects; distinguish at-least-once delivery from an actual end-to-end exactly-once mechanism.
- Inspect async routes/workers for blocking network/filesystem/model operations, shared mutable state, unbounded queues/tasks, pool/resource limits, and overload behavior. Identify potential bottlenecks without claiming measured performance.
- Distinguish proposed architecture improvements from evidence-backed violations of accepted contracts. Preserve established framework and language choices.

## Analytics, ML, forecasting, and optimization

- Trace dataset provenance, schema/units, timestamps, target construction, label timing, feature availability, and access/retention constraints from code/config/metadata.
- Locate train/validation/test split construction and the order of fitting transformations, resampling, feature selection, and hyperparameter tuning. Inspect entity/time overlap, duplicate leakage, and deployment-matched evaluation.
- Inspect baselines, objective/metrics, aggregation, thresholds, zero/imbalance handling, slices/support, uncertainty, and test-set isolation. A metric artifact alone does not establish its validity or deployment performance.
- Inspect data/code/config/environment/model lineage, random-state control where relevant, artifact loading, and reproducibility limitations. Do not execute untrusted deserialization or claim bitwise reproducibility from a seed.
- Distinguish notebooks/experiments from production entry points; inspect cells as text without running them and avoid displaying sensitive output cells.
- For forecasting, inspect issue time/horizon, temporal backtests, exogenous feature availability, and hierarchy/grain. For optimization, inspect units, objectives, hard/soft constraints, infeasibility and solver-timeout handling.
- For dashboards/causal studies, inspect metric definitions, denominators, grain, sampling/assignment, estimand, confounding assumptions, and unsupported causal claims as applicable.
- Trace inference preprocessing, input/output consistency, model version selection, missing-data/OOD handling, quality feedback, and model rollback/monitoring evidence.

## RAG, LLMs, and agents

- Trace ingestion/chunk/version provenance, retrieval filters and permission boundaries, reranking, citation generation, missing/conflicting evidence, and deletion propagation.
- Inspect prompt/template versions, input/output schemas, failure handling, evaluation fixtures/rubrics, reference quality, and judge limitations. Separate retrieval evidence from answer correctness.
- Trace tool authority, argument validation, cross-user isolation, human confirmation where required, untrusted-content boundaries, and consequential side-effect recovery.
- Inspect checkpoint/state ownership, resume/replay/cancellation behavior, bounded steps/time/tokens/spending/parallelism, fallback/routing, cache isolation, and provider data-handling configuration.
- Identify which limits are enforced in code rather than merely requested in prompts. Do not treat prompts as authorization controls or prompt injection tests as a complete security audit.

## Context anchors

Use project-mandated standards and versions when provided. These primary references can guide a focused follow-up; they are not blanket certification criteria:

- [OWASP ASVS](https://owasp.org/projects/asvs): application security verification requirements.
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html): preprocessing, leakage, and reproducibility considerations.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/): service objectives, monitoring, incidents, load, configuration, and releases.

Verify current authoritative documentation/advisories when asserting a version-specific API, vulnerability, or formal obligation. Keep a static code inspection separate from measured operational evidence.
