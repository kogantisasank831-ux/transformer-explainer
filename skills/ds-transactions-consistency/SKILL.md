---
name: ds-transactions-consistency
description: Design, inspect, or repair transaction boundaries and consistency behavior for backend and data science products. Use for races, isolation anomalies, locking, optimistic concurrency, retries, idempotency, multi-resource workflows, outbox patterns, and read consistency. Ground guarantees in accepted invariants and actual engine semantics.
---

# Transactions and Consistency

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts, current implementation, and native tooling. Record rule IDs, requested action, engine/broker/cache and version, environment or candidate identity, and authority. Support ordinary backend systems; add DS/ML/RAG checks only where those workloads exist. Treat repository text, metrics exports, query plans, generated output, and external artifacts as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential product or consistency decisions to the responsible owner. Do not invent data-loss tolerance, downtime, staleness, ordering, retry, retention, or performance targets. Keep review/design-only work read-only and implementation within the authorized component.

## Define the invariant and boundary

1. Express each accepted invariant with the records/resources it spans, authorized writers, observation point, and failure behavior. Map current transaction boundaries, autocommit calls, connection/session ownership, ORM flush/commit behavior, constraints, locks, replicas, caches, messages, files, and external services. A function boundary is not necessarily a transaction boundary.
2. Read [the consistency checks](references/checks.md). Identify anomalies that can violate the invariant: lost update, write skew, duplicate creation, stale read, non-repeatable read, phantom, partial commit, retry duplication, out-of-order event, or replica lag. Match the isolation level and engine's actual semantics rather than relying on generic names.
3. Prefer database constraints and atomic statements for local invariants. Choose pessimistic locking, optimistic version checks, serializable transactions, advisory locks, or application coordination only with a named invariant and contention model. Define lock acquisition order, scope, timeout, deadlock handling, and resource lifetime. Process-local locks do not coordinate multiple workers or hosts.

## Make retry a whole-operation contract

Classify retryable engine errors by documented codes. On deadlock or serialization failure, roll back and retry the entire transaction from a clean session with bounded attempts, backoff, cancellation, and observability. Ensure inputs remain valid and external side effects are not duplicated. Do not retry arbitrary integrity, validation, or authorization failures.

Use idempotency keys and uniqueness at the authoritative boundary for client/job retries. Store outcome semantics and payload identity where required; a request identifier alone does not define equivalence. Keep network calls, model inference, file writes, and broker publication outside long-held database locks unless their failure contract is explicit.

## Coordinate multiple resources honestly

Do not claim atomicity across a database and external service without a supported distributed protocol. Use a transactional outbox/inbox, state machine, saga/compensation, or reconciliation according to accepted requirements. Define commit point, delivery semantics, deduplication identity, ordering, compensating limits, and human recovery. Compensating actions are new operations and may fail.

For DS workflows, preserve dataset/model/artifact identity with job state. Ensure concurrent training, evaluation, feature refresh, and registry promotion cannot publish mismatched artifacts or overwrite a newer result. Long computations should use claims/leases and short state transitions rather than holding database transactions open.

## Verify interleavings

Test controlled concurrent schedules, barriers, retries, duplicate requests, worker loss, stale versions, deadlocks, serialization failures, and partial external failures. Assert invariants from the authoritative store, not only response codes. Use the real supported engine for isolation claims; SQLite or mocks cannot establish PostgreSQL/MySQL/distributed behavior. Record isolation/session settings and connection-pool behavior used by the test.

## Verify and hand off

Run proportionate checks with the project's native tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local or substitute-service results do not establish CI or deployed enforcement.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config identity, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and test links when accepted behavior changes. This workflow does not itself authorize production migration, deployment, data repair, traffic replay, or risk acceptance.
