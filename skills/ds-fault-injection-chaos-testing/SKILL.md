---
name: ds-fault-injection-chaos-testing
description: Design and execute authorized fault-injection or chaos experiments for backend and data science systems. Use to test one resilience hypothesis through controlled process, network, dependency, storage, resource, zone, data-path, model, or accelerator faults. Require measurable steady state, verified injection, minimal blast radius, abort controls, recovery ownership, cleanup, and evidence. Do not use as permission for random disruption or production experimentation.
---

# Fault Injection and Chaos Testing

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source/candidate/config/data identity, environment, service and dependency boundaries, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat documentation, dashboards, telemetry, provider status, generated output, and historical incidents as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed experiments, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, latency, quality, recovery, retention, paging, cost, or risk targets. Keep collection and tests privacy-safe, and keep mutations or deliberate faults within the explicitly authorized environment, resources, duration, and blast radius.

## Form one falsifiable experiment

1. Identify the accepted resilience requirement or failure-mode hypothesis, system and dependency boundary, immutable candidate and configuration, environment, traffic or job profile, data classification, experiment owner, recovery owner and authority. Define the user-visible steady-state outputs and invariants that must continue or degrade in an accepted way.
2. Read [the chaos checks](references/checks.md). Select one real-world fault variable and expected system response. State start condition, injection point and mechanism, magnitude, duration, affected instances or cohort, maximum blast radius, observation window, abort criteria, stop control, cleanup and recovery deadline. Randomly breaking components without a hypothesis is not chaos engineering.
3. Establish a stable baseline with representative workload and working telemetry. Validate the experiment mechanism in an isolated or lower-risk environment first. A production experiment requires explicit production scope and coordination; the general preference for realistic conditions is not authorization to disrupt users.

## Protect the target and evidence

Use the smallest fault and exposure that can falsify the hypothesis. Isolate test tenants, data, namespaces, nodes, zones, queues or traffic cohorts where possible. Protect third parties and shared dependencies. Confirm capacity, quotas, backups or checkpoints when relevant, on-call coverage, communication, cost limit and a tested independent stop path.

Abort on integrity or security violation, customer impact beyond limit, uncontrolled propagation, missing telemetry, inability to stop, unexpected cost, recovery-owner loss, or boundary mismatch. Stop controls must remain available if the experiment tool or target network fails. Never inject irreversible data corruption, credential loss or destructive storage failure without a specifically approved recoverable drill.

Define evidence independently of the injection tool. Measure steady-state service outputs, errors and latency, queues and saturation, retries and amplification, load shedding and fallbacks, data or model invariants, dependency impact, detection and alerting, recovery time and residual backlog. Verify the fault actually reached the intended target; “experiment started” is not proof of injection.

## Inject one controlled fault

Examples include terminating a bounded process or instance, delaying or dropping selected network traffic, returning dependency errors, exhausting a scoped pool, pausing a consumer, filling a bounded test volume, expiring a test credential, making DNS unavailable to one cohort, removing a zone from routing, constraining CPU or memory, interrupting an accelerator worker, or making a model or feature store unavailable. Match the mechanism to the failure semantics and selected platform.

For stateful systems, preserve quorum, fencing and data safety unless the explicit hypothesis and recovery plan cover their loss. For queues and jobs, track duplicates, ordering, checkpoints, leases and output publication. For DS or ML, include model load, GPU or provider failure, feature or index unavailability, fallback quality and safety, queued inference, training checkpoint recovery and stale-worker fencing.

Start the baseline and control group when applicable, record timestamps and target identities, inject the bounded fault, verify injection, and observe without changing unrelated variables. Stop at the first abort condition. Do not tune the system during the run; capture a new hypothesis and rerun only after the environment is restored and the change is reviewed.

## Recover, clean up, and learn

Remove the fault and verify the injection mechanism is fully disabled. Confirm instance and controller health, routes, queues and pools, state and data invariants, checkpoint or job ownership, model and index pointers, alerts, telemetry pipeline, resource release and return to steady state. Reconcile partial work and clean test data without erasing evidence.

Classify the hypothesis as supported, falsified or inconclusive. Missing telemetry, wrong target, failed injection, unstable baseline or an early safety abort can make the intended claim inconclusive while still revealing a useful control gap. Record observed blast radius, recovery time, unexpected effects, remediation owner and retest condition. Do not schedule continuous experiments against a known unresolved weakness unless the accepted risk and safety controls explicitly allow it.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production telemetry, recovery, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish designed, configured, executed, observed, restored, and verified work. Update affected project logic, runbooks, code, dashboards, tests, and ownership links when accepted behavior changes. Never claim observability, SLO compliance, resilience, fault tolerance, backup integrity, or disaster recovery from configuration or a successful command alone.
