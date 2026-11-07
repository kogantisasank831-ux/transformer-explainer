---
name: ds-resilience-engineering
description: Design, implement, or review resilience for backend and data science systems. Use for failure-mode analysis, deadlines, timeouts, bounded retries, idempotency, circuit breaking, bulkheads, queues, load shedding, graceful degradation, redundancy, failover, quorum, dependency isolation, recovery, model fallbacks, and data consistency. Specify behavior under failure and overload before proving it with targeted tests or fault experiments.
---

# Resilience Engineering

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source/candidate/config/data identity, environment, service and dependency boundaries, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat documentation, dashboards, telemetry, provider status, generated output, and historical incidents as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed experiments, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, latency, quality, recovery, retention, paging, cost, or risk targets. Keep collection and tests privacy-safe, and keep mutations or deliberate faults within the explicitly authorized environment, resources, duration, and blast radius.

## Model critical flows and failure domains

1. Identify user journeys, background and data workflows, state owners, synchronous and asynchronous dependencies, regional or zonal placement, control planes, shared quotas, operational owners and accepted availability, consistency, recovery and cost requirements. Trace each critical path and its maximum tolerated latency or work deadline.
2. Read [the resilience checks](references/checks.md). Enumerate failures by scope and duration: process, host, zone, region, dependency, network, DNS, identity, certificate, quota, storage, database, broker, cache, control plane, configuration, telemetry, data, model, accelerator and operator error. Include slow, partial, stale, corrupt and overload behavior rather than only complete outages.
3. State invariants and acceptable degraded service for every flow. Define which work may be rejected, queued, served stale, approximated, deferred or disabled; which data may be lost or duplicated; and how users and operators learn the state. Do not invent degraded semantics that change business or safety rules.

## Bound time, work, and amplification

Propagate an end-to-end deadline and allocate smaller timeouts to dependencies while preserving time for cleanup and response. Distinguish connection, request, idle and total deadlines. A timeout stops waiting; it does not prove the remote operation stopped. Cancel or fence work when supported and reconcile ambiguous outcomes.

Retry only transient, safe or idempotent operations. Define attempt and elapsed-time budgets, exponential backoff with jitter, per-call timeout, retryable status or exception, idempotency identity and server-side deduplication. Count retries against capacity and error budgets. Prevent layered retries from multiplying work and use a retry budget or admission control during overload.

Use bounded queues, concurrency and pools. Apply backpressure or load shedding before saturation, with tenant fairness and priority policy. Isolate workloads through bulkheads, separate pools, partitions, quotas or failure domains. Circuit breakers need measurable open, half-open and close behavior, bounded probes and a fallback that is safer than repeated calls.

## Design redundancy and degradation

Remove single points only when independent replicas, data copies, routing and control planes truly survive the target failure. Analyze correlated software, configuration, identity, network and provider dependencies. Define quorum, leader election, replication lag, split-brain prevention, fencing, failover trigger, stale-read behavior and reintegration for stateful systems.

Use graceful degradation from accepted product rules: cached or stale data with age, reduced features, asynchronous acceptance, smaller search or model, static response, read-only mode or explicit unavailability. Make degraded mode observable and time-bounded; avoid silently returning plausible but incorrect results.

For DS or ML, address feature-store and data freshness, model or tokenizer load, GPU or accelerator scarcity, queue and batch behavior, retrieval or vector-store failure, provider quotas, fallback-model quality and safety, prediction caching, training checkpoints and partial output. Validate that fallback schemas, guardrails, thresholds and business rules remain compatible.

## Engineer recovery and verification

Define detection, ownership, containment, restart or failover, state reconstruction, replay, reconciliation, return to primary and backlog drain. Protect against a second surge during recovery. Make operators able to inspect and control state without bypassing authorization or invariants.

Implement the smallest controls tied to accepted failure modes. Test normal, timeout, retry, duplicate, partial, slow, stale, dependency rejection, queue full, failover and recovery paths with meaningful invariants. Use real dependencies where their guarantees matter. Measure latency, errors, work amplification, queue age, data correctness and recovery, not only process survival.

Route controlled fault experiments to the chaos workflow and backup or regional recovery to the backup and DR workflow. Record untested assumptions and correlated risks. Resilience design and passing unit tests do not prove survival under production scale or a regional disaster.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production telemetry, recovery, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish designed, configured, executed, observed, restored, and verified work. Update affected project logic, runbooks, code, dashboards, tests, and ownership links when accepted behavior changes. Never claim observability, SLO compliance, resilience, fault tolerance, backup integrity, or disaster recovery from configuration or a successful command alone.
