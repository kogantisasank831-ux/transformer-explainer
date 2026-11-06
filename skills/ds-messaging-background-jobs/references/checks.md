# Messaging and background-job checks

- State delivery semantics per boundary: producer-to-broker confirmation, broker durability, consumer delivery, effect commit, acknowledgement, and result publication.
- Coordinate database writes and publication through an outbox or documented equivalent when required. Use stable IDs and reconciliation.
- Acknowledge after the chosen durable completion point. Test crashes before/after effect and ack; enforce idempotency at the authoritative side effect.
- Bound retries, backoff/jitter, deadlines, attempt timeout, cancellation, resource cleanup, and poison handling. Preserve failure history.
- Define DLQ retention, access, alerts, replay validation, authorization, and closure. A growing DLQ is not successful recovery.
- Specify ordering/partition scope, hot-key behavior, concurrency, prefetch/in-flight bounds, backpressure, payload size, schema compatibility, and graceful shutdown.
- For long DS/ML jobs, use leases/fencing, checkpoints, immutable artifact identities, resource limits, and stale-result rejection.

Consult official broker/worker documentation. RabbitMQ users should review [consumer acknowledgements and publisher confirms](https://www.rabbitmq.com/docs/confirms) for the deployed version; these mechanisms solve distinct delivery boundaries.
