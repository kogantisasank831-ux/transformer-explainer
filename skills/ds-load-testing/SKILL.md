---
name: ds-load-testing
description: Design and execute authorized load tests for backend and data science systems under expected traffic. Use for workload modeling, concurrency or arrival rates, scenario mixes, latency and error thresholds, dependency capacity, autoscaling observations, and performance regression evidence. Start with smoke validation and distinguish generator limits from system behavior.
---

# Load Testing

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent retry, data-loss, lateness, throughput, latency, concurrency, duration, recovery, or resource targets. Keep review/design work read-only and execution within the explicitly authorized environment and component.

## Build an accepted workload model

1. Define the decision the test supports, system boundary, authorized environment, candidate/config/data identity, topology, dependencies, and safety owner. Derive scenario mix, arrival rate or concurrency, think time, session behavior, request/response sizes, tenant/key distribution, cache hit state, background work, duration, and ramp from production evidence or accepted projections. Label assumptions.
2. Read [the load-test checks](references/checks.md). Choose an open model for externally imposed arrival rates or a closed model for a bounded user/worker population, and explain the choice. Avoid coordinated omission and client-side pacing that hides server delay. Model retries only as real clients would; an uncontrolled retry storm changes the workload.
3. Define measurable gates before execution: per-scenario latency percentiles, throughput, error/timeout rate, correctness or invariant checks, queue depth/age, resource saturation, dependency limits, and recovery. Specify populations, windows, exclusions, and failure treatment. Averages and aggregate throughput can hide a failed critical journey.

## Create production-representative scenarios

Use real supported entry points and weighted journeys, authentication/authorization, varied parameters, realistic payloads, stable test identities, and bounded test data setup/cleanup. Include reads and writes in accepted proportions. Avoid one hot synthetic key unless it reflects reality. For DS/ML, model input/token/sequence distributions, batching, model mix, cold/warm state, GPU memory, queueing, quality/error/fallback results, and rate/provider limits.

Start with a minimal smoke run to validate script assertions, correlation, data isolation, and observability. Calibrate the load generator separately: CPU, network, sockets, event loop, connection reuse, DNS/TLS, and clock synchronization. Use multiple generators only when required and verify aggregate offered versus achieved load.

## Execute safely and observe end to end

Obtain explicit authorization for the target and traffic level. Use test tenants/data and rate/abort controls; do not aim load at shared production or third-party services without permission. Monitor client, gateways, services, pools, queues, databases/caches, external dependencies, host/container, and accelerators. Record deployment/autoscaling events and candidate identity.

Ramp, hold long enough for representative steady state, then ramp down and observe recovery. Save raw results and time-aligned telemetry. Separate offered load, achieved throughput, completed work, and rejected work. If the generator saturates or observability is missing, the affected claim is inconclusive.

Repeat comparable runs to assess variance, then compare with an independently governed baseline. Diagnose saturation rather than immediately tuning. Load testing validates expected conditions; use the separate stress/spike/soak workflow for breaking point, sudden surge, or endurance objectives.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, data replay, destructive recovery, deployment, or risk acceptance.
