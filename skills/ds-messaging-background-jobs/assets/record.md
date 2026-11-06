# Messaging and background-job record

- Workflow, rule IDs, broker/worker versions, topology, and authority:
- Message/job grain, schema, ordering scope, durability, and completion semantics:

| Boundary | Identity / state | Guarantee | Failure / retry | Evidence / owner |
|---|---|---|---|---|

## Recovery and pressure

Record outbox/inbox, idempotency, ack point, retries/backoff/deadline, DLQ/replay, lease/fencing, cancellation, partitioning, concurrency/prefetch, and backpressure.

## Verification

List duplicate/order/crash/reconnect/poison/schema/shutdown cases, real/fake broker boundaries, commands/results, final-state and side-effect assertions, CI/server gates, residual risks, owners, and next actions.
