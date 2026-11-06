---
name: ds-stress-spike-soak-testing
description: Design and execute authorized stress, spike, and soak tests for backend and data science systems. Use to discover limits, validate sudden-traffic behavior, expose leaks or cumulative degradation, and verify controlled recovery. Require a stable average-load baseline, explicit safety controls, and separate evidence for each workload shape.
---

# Stress Spike and Soak Testing

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent retry, data-loss, lateness, throughput, latency, concurrency, duration, recovery, or resource targets. Keep review/design work read-only and execution within the explicitly authorized environment and component.

## Choose the abnormal-load question

Start from a validated functional script and stable average-load baseline. Select one test type from the decision needed:

- **Stress:** increase beyond normal/peak expectations to identify saturation, degradation shape, maximum sustainable throughput, rejection behavior, and recovery.
- **Spike:** apply an evidence-based rapid rise and fall to verify admission control, queues, autoscaling/warm-up, retry behavior, and recovery from a surge.
- **Soak:** hold a representative or elevated accepted load long enough to expose leaks, fragmentation, queue accumulation, connection/resource exhaustion, rollover, compaction, or performance drift.

Do not combine all three into one ambiguous run. Read [the stress-test checks](references/checks.md) and define offered-load shape, duration, decision criteria, abort/damage limits, recovery observation, and environment authority before execution. A breaking point is specific to candidate, configuration, topology, data, dependencies, and generator.

## Protect the environment

Use an isolated or purpose-built environment with production-representative limits whenever possible. Obtain explicit authorization for target, maximum load, duration, data and cost envelope, external dependencies, and recovery owner. Protect shared databases, brokers, caches, model endpoints, quotas, and third parties. Prepare stop controls, dashboards, backups/restore evidence where required, and on-call coordination. Never interpret this skill as permission to stress production.

Define abort conditions for integrity violations, data loss/corruption, cascading impact, uncontrolled cost, dependency harm, excessive error/latency/queue, generator loss of control, and missing observability. An abort is a valid result; preserve the evidence and verify recovery.

## Execute one controlled profile

For stress, use incremental stages with holds sufficient to observe steady behavior. Record saturation knee, throughput plateau, latency/error/queue shape, admission/rejection, scaling, and resource constraint. Avoid jumping directly to destructive load.

For spike, model the expected rise rate, magnitude, duration, and fall. Track accepted/rejected work, queue age, time to scale, retry amplification, fairness, and time to return to normal. Verify queued work does not create a second spike.

For soak, define duration from suspected cycles and resource lifetimes. Track slopes and periodic behavior for live/retained memory, descriptors, connections, threads/tasks, GPU allocation, disk/log growth, queue/backlog, database bloat/lag, cache churn, latency/errors, and data-quality drift. Preserve comparable snapshots and account for scheduled maintenance or rotation.

For DS/ML, include accelerator thermal/memory stability, batch/sequence mix, model reload/compilation, checkpoint/artifact growth, provider limits, quality/fallback drift, and stale-result fencing.

## Verify graceful degradation and recovery

Assert correctness and tenant/security invariants throughout. Measure load shedding, backpressure, timeouts, circuit behavior, fairness, and bounded queues. After ramp-down or abort, observe backlog drain, resource release, autoscaling down, replica/consumer health, data reconciliation, and return to baseline. A process still responding does not prove recovery.

Repeat only when the environment is restored and comparable. Report maximum observed safe load rather than an unsupported universal capacity. Route capacity planning, scaling design, resilience faults, and remediation to their respective workflows.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, data replay, destructive recovery, deployment, or risk acceptance.
