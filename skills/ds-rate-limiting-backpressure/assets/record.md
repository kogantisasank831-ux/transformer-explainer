# Rate limiting and backpressure record

- Resource, rule/policy IDs, owner, environment, candidate/config and enforcement boundary:
- Trusted identity/tenant, operation/cost unit, quota/rate/burst/concurrency, window and override authority:

| Layer / path | Algorithm and atomic store | Key / cost / limit | Reject, defer or pressure behavior | Failure and evidence |
|---|---|---|---|---|

## Queue, retry and fairness contract

Record queue item/byte/age and pool bounds, priorities, shedding, deadlines/cancellation, retry and idempotency budgets, HTTP fields/errors, tenant isolation, limiter failure mode, audit and recovery.

## Verification

List boundary/burst/sustained/race/distributed/skew/hot-key/fairness/full-queue/retry/outage cases, protected-resource assertions, commands/results, simulated-versus-deployed boundary, residual risks, owners and next actions.
