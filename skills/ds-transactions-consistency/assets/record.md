# Transaction and consistency record

- Component, rule IDs, engine/version, isolation/session settings:

| Invariant | Writers/resources | Current boundary / anomaly | Chosen control | Commit point / recovery | Evidence |
|---|---|---|---|---|---|

## Retry and external effects

Record retryable codes, whole-operation boundary, attempts/backoff/cancellation, idempotency identity, ambiguous outcomes, outbox/saga/reconciliation, and compensation limits.

## Verification

List controlled interleavings, real/fake boundaries, commands/results, final invariant checks, pool/replica settings, CI/server gates, residual risks, owners, and next actions.
