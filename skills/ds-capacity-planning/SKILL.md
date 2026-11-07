---
name: ds-capacity-planning
description: Create or review evidence-based capacity plans for backend and data science systems. Use for demand forecasts, service-demand units, measured resource curves, failure reserve, provisioning lead time, quota constraints, growth scenarios, headroom, and cost-aware capacity decisions. Keep forecasts, measured capacity, configured capacity, and observed production behavior distinct.
---

# Capacity Planning

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, growth, headroom, latency, throughput, concurrency, fairness, cost, recovery, or resource targets. Keep review and design work read-only, and keep execution within the explicitly authorized environment and component.

## Define the planning decision

1. Name the service or workflow boundary, owner, regions and failure domains, planning horizon, procurement or quota lead time, accepted availability and recovery requirements, budget boundary, and the decision this plan supports. Record current deployed and usable capacity separately. A resource inventory is not a capacity plan.
2. Read [the capacity checks](references/checks.md). Express demand in service units that drive work: requests or transactions by journey, events or bytes, jobs, records, tokens, model invocations, GPU-seconds, concurrent sessions, storage growth, or another measured unit. User count alone is usually insufficient. Define peak window, geographic and tenant distribution, payload or sequence distribution, cache state, background work, and dependency demand.
3. Build an evidence-linked demand forecast beyond the longest acquisition or provisioning lead time. Separate organic trend, seasonality, launches, migrations, campaigns, contractual commitments, and one-time events. Produce base, high, and accepted worst-case scenarios with assumptions, uncertainty, and sensitivity. Reconcile prior forecasts with actual demand before reusing the method.

## Convert demand to service capacity

Derive resource-to-service curves from representative load tests, production telemetry, profiles, and engine or vendor limits. For each tier, identify the first limiting resource and the range where latency, errors, queues, quality, and correctness remain acceptable. Account for CPU, memory, allocation, disk and network I/O, connections, file descriptors, database/cache/broker limits, storage and retention, external quotas, accelerators, model memory, token throughput, and data-transfer limits as applicable.

State scale-unit granularity and efficiency. Capacity does not necessarily grow linearly: coordination, sharding, cache behavior, batching, compaction, synchronization, hot keys, and dependency ceilings can change the curve. Use Little's Law only for a stable boundary with consistent arrival, completion, and time definitions; record when its assumptions do not hold.

Calculate required capacity per scenario from measured sustainable service capacity, then apply accepted operating headroom, redundancy, maintenance reserve, and failure-domain survival. Do not double-count reserve already embedded in a benchmark or provider limit. End-to-end capacity is constrained by the narrowest tier, shared dependency, quota, or operational bottleneck, not the sum of nominal instances.

## Produce an actionable plan

For each horizon, record required, available, committed, and shortfall capacity with acquisition lead time, cost range, owner, and trigger date. Include reservations or quotas, licenses, IPs, storage growth and cleanup, database connection budgets, warm pools, model or index footprints, and human operations constraints where material. Evaluate rightsizing, demand shaping, efficiency work, architectural changes, and additional capacity without assuming autoscaling creates unavailable underlying capacity.

Define leading indicators, forecast review cadence, reorder or scale triggers, and contingency actions for forecast error or delayed supply. Validate the plan with representative benchmarks and failure-reserve exercises appropriate to the claim. Report forecast uncertainty and maximum measured safe conditions; never turn an unvalidated spreadsheet estimate into a production-capacity claim.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, scaling changes, quota changes, infrastructure purchase, deployment, or risk acceptance.
