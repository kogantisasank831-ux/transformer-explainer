# Query optimization record

- Query fingerprint/caller, rule IDs, engine/version, schema/statistics revision:
- Workload, bindings/data distribution, concurrency, cache state, and target source:

| Case | Correctness oracle | Before plan/metrics | Change | After plan/metrics | Limit |
|---|---|---|---|---|---|

## Tradeoffs

Record index/storage/write effects, lock/migration needs, quality impact for approximate retrieval, rollback, and monitoring.

## Verification

List commands, repetitions, percentiles, data scale, concurrent tests, failures, untested boundaries, candidate/config identity, CI/server gate status, residual risks, owners, and next actions.
