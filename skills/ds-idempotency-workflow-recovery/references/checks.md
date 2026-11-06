# Idempotency and recovery checks

- Define business operation identity, tenant/actor scope, canonical input equivalence, result semantics, retention/replay window, and key-conflict behavior.
- Store durable claim/status and input fingerprint under a uniqueness constraint. Handle concurrent first attempts and ambiguous commits.
- Model explicit states/transitions, preconditions, versions, terminal states, timeouts, cancellation, and stale-worker fencing. Never infer completion from a process heartbeat.
- Bind checkpoints to input, code/config, partition/range, output manifest, and validation. Reject incompatible resume.
- Coordinate external effects through supported idempotency, outbox/inbox, stable provider references, or reconciliation. Query authoritative status before repeating an ambiguous effect.
- Bound retries and preserve attempt/error history. Compensation needs its own idempotency, failure handling, and authorization.
- Test each crash boundary, duplicates, conflicts, cancellation, retry exhaustion, and operator actions using final-state/effect-count assertions.

For an example of an API-specific policy, see [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests); copy its semantics only when they match the target system's accepted contract.
