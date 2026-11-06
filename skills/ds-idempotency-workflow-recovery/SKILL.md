---
name: ds-idempotency-workflow-recovery
description: Design, implement, or review idempotency and recovery for backend and data science workflows. Use for retryable API operations, multi-step state machines, job restarts, checkpoints, duplicate events, ambiguous outcomes, compensations, reconciliation, and operator recovery. Define operation identity and durable progress from accepted business semantics.
---

# Idempotency and Workflow Recovery

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent retry, data-loss, lateness, throughput, latency, concurrency, duration, recovery, or resource targets. Keep review/design work read-only and execution within the explicitly authorized environment and component.

## Define one logical operation

1. Identify the operation's business meaning, authoritative owner, caller/tenant, inputs, accepted equivalence, completion result, side effects, and retention/replay horizon. Define an idempotency identity from those semantics. A random request ID distinguishes attempts but does not prove two payloads represent the same operation.
2. Read [the recovery checks](references/checks.md). Specify key namespace, tenant/actor binding, canonical input fingerprint, result/status stored, expiry policy, concurrency behavior, and response for key reuse with different inputs. Avoid personal or secret data in keys. Enforce uniqueness and progress durably at the authoritative boundary rather than only in process memory.
3. Map each workflow state and transition with preconditions, authorized actor, atomic writes, side effects, terminal states, retryable failures, timeout, cancellation, and recovery. Prefer compare-and-set/versioned transitions and database constraints. Prevent stale workers from advancing newer work through lease owner tokens or fencing versions.

## Order durable progress and side effects

Choose and document the commit point. For local database effects, atomically store the effect, operation status, and outbox record where appropriate. For external effects, use provider-supported idempotency, stable correlation, transactional outbox/inbox, a resumable step record, or reconciliation. Do not mark completion before the required effect is durably acknowledged.

On retries, reload authoritative state and continue from the last verified step. A checkpoint must bind code/config version, input/artifact identity, completed partition/range, and output validation. Checkpoints for long data or ML jobs must reject incompatible resume attempts. Never assume a partially written file, model, or index is complete because its name exists; publish immutable output through an atomic manifest/pointer after validation.

## Recover ambiguous and failed workflows

Classify outcomes as not started, in progress, completed, failed-retryable, failed-terminal, cancellation requested, canceled, and unknown/ambiguous as applicable. Resolve ambiguous outcomes by querying the authoritative provider/store before retrying. Bound retries with deadline, backoff/jitter, attempt budget, and cancellation. Preserve the primary failure and attempt history.

Use compensations only for accepted reversible business actions; compensation is a new fallible workflow, not rollback. Define ordering, idempotency, authorization, and reconciliation. Provide an operator path for inspect, retry/resume, cancel/fence, compensate, and reconcile with audit evidence. Do not let operators arbitrarily rewrite state without invariant checks.

## Exercise crash points

Test concurrent first attempts, same key/same input, same key/different input, duplicate delivery, timeout before and after commit, crash at every transition/effect boundary, stale lease, checkpoint incompatibility, retry exhaustion, cancellation, compensation failure, and reconciliation. Assert final authoritative state and effect count, not only returned status. Use the real database/broker/provider sandbox where its guarantees are part of the claim.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, data replay, destructive recovery, deployment, or risk acceptance.
