# Backend requirements checklist

Apply this to ordinary backend services and to the backend portions of data science products. Use applicable items to produce requirements or open decisions, not a mandatory architecture or a questionnaire to send verbatim.

## Domain and lifecycle

- Identify users, entities, ownership, invariants, business rules, states, and allowed transitions.
- Specify create/read/update/delete behavior, validation, uniqueness, soft versus permanent deletion, restoration, retention, and audit needs.
- Establish atomic operations and failure boundaries. Define behavior for simultaneous updates, duplicate submissions, stale versions, and partial completion.
- Define timezones, units, rounding, null versus absent fields, defaults, and effective dates where relevant. Do not invent business policies.

## API and access contracts

- Identify clients and integration styles; avoid selecting REST, GraphQL, RPC, or framework versions before constraints justify them.
- Specify input/output schemas, identifiers, validation errors, status/error contracts, limits, pagination, sorting, filtering, and supported versions.
- Establish authentication, session/token lifecycle, account recovery, authorization, ownership checks, administrative actions, and tenant isolation as applicable.
- Specify upload content validation and size limits, streaming/download behavior, and file access boundaries where files are accepted.
- Define caller-visible idempotency, deduplication scope/lifetime, concurrent request semantics, and response behavior after unknown outcomes.
- Define API compatibility and deprecation expectations; capture machine-readable schema and consumer-contract verification needs.

## Persistence and consistency

- Establish data ownership, relational/document constraints, required consistency, and transaction boundaries; keep database selection proposed unless mandated.
- Define how schema changes and backfills remain compatible with running versions, and how failed changes are recovered.
- Define cache freshness, invalidation, sensitive-content handling, and behavior on unavailable/stale cache where caching is justified.
- Describe query/record volumes and growth; do not invent indexes or latency guarantees before evidence.

## Workers, integrations, and side effects

- Specify synchronous versus asynchronous outcomes, job states, progress visibility, timeouts, cancellation, expiry, and completion notifications.
- Define message validation, ordering needs, delivery assumptions, acknowledgment, retries, deduplication, dead-letter handling, and replay.
- For webhooks, specify sender authentication/signature verification, timestamp/replay policy, versioning, duplicates, and out-of-order events.
- Define reconciliation when an external write may have succeeded but its response was lost. Never promise exactly-once execution without an end-to-end mechanism and stated scope.
- Specify retryable failures and retry/time budgets; avoid blind retries of non-idempotent effects.
- Establish external provider rate limits, contract assumptions, sandbox availability, and outage/degradation behavior.

## Security, workload, and operations

- Define permission-denial, malformed-input, injection, secret handling, log redaction, audit, retention/deletion, and dependency-security requirements according to project risk.
- Establish traffic, in-flight concurrency, payload sizes, burst patterns, processing duration, queue limits, and expected growth before sizing.
- Define latency measurement boundaries, error rates, availability, admission/rate limits, backpressure, and overload behavior as measurable criteria or unresolved decisions.
- Define startup/readiness, graceful shutdown, configuration validation, observability, on-call ownership, backup/restore, deployment compatibility, and rollback needs.
- Verify deterministic business behavior with meaningful unit, integration, contract, negative-path, permission, concurrency, and recovery cases as appropriate.
- Use the engineering reference for coding constraints. Keep ML metrics and experiments not applicable unless the service actually uses them.
