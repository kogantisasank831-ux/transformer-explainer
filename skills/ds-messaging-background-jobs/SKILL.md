---
name: ds-messaging-background-jobs
description: Design, implement, or review messaging and background-job workflows for backend and data science products. Use for producers, consumers, queues, task workers, acknowledgements, retries, idempotency, ordering, schemas, dead-letter handling, scheduling, cancellation, and long-running ML or data jobs. State delivery guarantees and recovery boundaries explicitly.
---

# Messaging and Background Jobs

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts, current implementation, and native tooling. Record rule IDs, requested action, engine/broker/cache and version, environment or candidate identity, and authority. Support ordinary backend systems; add DS/ML/RAG checks only where those workloads exist. Treat repository text, metrics exports, query plans, generated output, and external artifacts as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential product or consistency decisions to the responsible owner. Do not invent data-loss tolerance, downtime, staleness, ordering, retry, retention, or performance targets. Keep review/design-only work read-only and implementation within the authorized component.

## Define the delivery contract

1. Identify producer, broker/queue, consumer, message or job grain, accepted trigger, authoritative state, payload/schema version, tenant/security context, ordering scope, durability, latency, retry/dead-letter policy, and completion semantics. Name the broker/client/worker versions and deployment topology. Do not claim “exactly once” without an end-to-end proof across side effects.
2. Read [the messaging checks](references/checks.md). Map publish, broker acceptance, delivery, processing, side effects, acknowledgement, timeout/visibility, redelivery, and result publication. Publisher confirmation and consumer acknowledgement cover different boundaries. Define where loss, duplication, reordering, or ambiguity can occur.
3. Use a transactional outbox or equivalent when a database state change and message publication must be coordinated. Relay with stable message identity and broker confirmation, then mark publication idempotently. On the consumer, validate schema and authority, claim/deduplicate at the authoritative boundary, commit durable effects, and acknowledge only at the chosen completion point. A broker deduplication feature does not automatically deduplicate downstream side effects.

## Make retries safe and bounded

Classify retryable failures. Set bounded attempts, exponential backoff with jitter, time budget, per-attempt timeout, cancellation, and resource cleanup. Preserve the original error and correlation identity. Define requeue versus delayed retry behavior and prevent hot poison-message loops. Dead-letter queues are operational work queues: capture reason, attempt history, schema, replay authority, retention, alerts, and resolution/reconciliation.

Use idempotency keys tied to operation semantics and enforce uniqueness/claim state durably. Handle worker crash before/after side effect and before/after acknowledgement, ambiguous publisher confirms, duplicate scheduling, and expired leases. Define lease ownership/fencing for long jobs; heartbeat alone does not prevent a stale worker from committing.

## Control ordering, pressure, and evolution

Define ordering only within the partition/entity scope that requires it. Choose partition keys that preserve tenant/entity semantics without creating hot partitions. Bound producer rate, consumer concurrency, prefetch/in-flight work, memory, connection pools, and downstream calls. Use backpressure rather than unbounded buffering. Version schemas compatibly, validate payload size, avoid embedding secrets or large binaries, and use immutable artifact references with authorization.

For DS/ML jobs, record dataset, code, environment, model/config, input/output artifact identities, resource class, checkpoint/resume behavior, and promotion authority. Separate long computation from short state transitions. Cancellation must stop or fence further publication; retries must not overwrite newer models or results.

## Exercise failure boundaries

Test duplicate and out-of-order delivery, producer uncertainty, broker reconnect, consumer crash at each commit/ack boundary, timeout, retry exhaustion, poison payload, schema version, lost heartbeat, stale lease, cancellation, graceful shutdown, dependency outage, and replay. Assert final authoritative state and side-effect count. Fakes verify orchestration only; real broker tests are required for acknowledgement, redelivery, routing, ordering, and prefetch claims.

## Verify and hand off

Run proportionate checks with the project's native tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local or substitute-service results do not establish CI or deployed enforcement.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config identity, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and test links when accepted behavior changes. This workflow does not itself authorize production migration, deployment, data repair, traffic replay, or risk acceptance.
