# Idempotency and recovery record

- Workflow, rule IDs, owner, tenant/actor scope, candidate/config identity:
- Logical operation, key/fingerprint, retention/replay horizon, and completion semantics:

| State / step | Preconditions and durable change | External effect / commit point | Retry / recovery | Evidence |
|---|---|---|---|---|

## Ambiguity and operations

Record checkpoint compatibility, lease/fencing, cancellation, compensation, reconciliation, operator actions, audit, and unsafe/manual actions excluded.

## Verification

List duplicate/conflict/concurrency/crash/retry/cancel/reconcile cases, real/fake boundaries, commands/results, final-state/effect assertions, CI/server gates, residual risks, owners, and next actions.
