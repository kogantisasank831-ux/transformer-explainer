# Preservation checks

| Surface | Preserve or explicitly authorize a change |
|---|---|
| API/library | Names/signatures, import paths, defaults, coercion and exception/status behavior, sync/async interface, ordering, null/missing meaning, mutability and serialization. |
| Persistence/effects | Transaction and commit timing, write/notification counts, retry safety, tenancy keys, external calls, resource cleanup and publication/overwrite behavior. |
| Dataframes/pipelines | Join cardinality, index/dtypes, feature order, null/NaN/infinity, time zone/units, aggregation denominator, deterministic sorting, copy/view behavior and chunk boundaries. |
| ML/GenAI | Preprocessing/model/prompt/config versions, seed scope, feature leakage boundaries, output alignment, evaluation population and approved quality/fallback policies. |
| Runtime | Supported Python/native version, packaging/import behavior, dependency initialization, worker/process safety, memory and contractual latency constraints. |

Characterization is evidence of what code does, not proof that it matches the SRS. Exclude secrets and production records from fixtures. Prefer sanitized deterministic fixtures and injected clocks/randomness/I/O. For nondeterministic outputs, compare agreed invariant/distribution/quality checks and record evidence limits; do not assert byte equivalence.

A regression test should exercise the public or stable behavioral boundary. Avoid snapshotting unstable incidental representation, asserting private call order without a contractual reason, or fixing every test by copying the new implementation's answer. Differential checks also compare against an old implementation that may have defects; retain independent rule-based assertions.

Stop at the scoped structural outcome. Do not mix formatting of unrelated modules, schema redesign, new infrastructure and model retraining into a refactor.
