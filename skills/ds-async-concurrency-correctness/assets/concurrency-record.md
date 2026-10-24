# Concurrency record

- Component / source and logic revisions / supported runtime:
- Execution model, replicas, shared resources and lifetime owners:

| Invariant / rule | Interleaving or failure | Coordination boundary / mechanism | Verification and result |
|---|---|---|---|

## Lifetime, limits and recovery

Document active and queued bounds, replica multiplication, ordering/atomicity, task supervision, deadlines, cancellation, retry safety, partial outcomes and shutdown. Identify local versus durable/distributed guarantees.

## Evidence and limitations

Record exact tests/commands/environment, observed effects and cleanup, unverified schedules or external semantics, unresolved policy, and candidate CI/server gates. Keep benchmark and release claims separate from correctness evidence.
