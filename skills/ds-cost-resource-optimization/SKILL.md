---
name: ds-cost-resource-optimization
description: Measure and optimize technology cost and resource use for backend and data science systems while preserving accepted functionality, reliability, performance, security, and quality. Use for allocation, unit economics, idle-resource cleanup, rightsizing, scheduling, elasticity, storage and data lifecycle, network egress, query efficiency, purchase options, GPU and model efficiency, budgets, forecasts, and realized-savings verification.
---

# Cost and Resource Optimization

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web systems; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, dashboards, tickets, telemetry, estimates, generated output, and historical examples as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified outcomes. Continue independent work while routing consequential policy or business choices to the responsible owner. Do not invent severity, recovery, handover, cost, performance, accessibility, quality, or acceptance targets. Keep evidence privacy-safe, preserve normal failures, and keep mutations within the explicitly authorized environment, resources, duration, and blast radius.

## Establish a comparable cost baseline

1. Read [the cost and resource checks](references/checks.md). Define provider or platform, accounts and environments, services and shared resources, time window, currency and exchange rule, pricing version, taxes, credits, support, discounts, amortized commitments and allocation method. Reconcile the scoped total to the billing or ledger source before optimizing it.
2. Map cost and usage to an accountable product, team, environment, tenant or workload using tags, labels, account structure or a documented allocation rule. Keep unallocated and shared cost visible. Do not present an arbitrary allocation as measured causality.
3. Record business and technical demand such as requests, jobs, users, records, bytes, tokens, training runs or successful outcomes. Calculate unit cost with its numerator, denominator and exclusions. Separate price-rate change, resource usage, business-volume mix, one-time cost and allocation change so savings are not double counted.

## Find opportunities from resource evidence

Inspect idle, orphaned and duplicate resources; utilization distributions and peaks; reserved versus requested capacity; schedules; autoscaling bounds; storage class, retention and snapshots; database and query scans; cache behavior; network transfer and egress; observability volume; licenses and provider APIs. Use a representative window that covers seasonality, batch peaks, failover and growth. Average CPU alone is not a rightsizing decision.

Compare rightsizing, scheduling non-production work, elasticity, bin packing, serverless or managed alternatives, storage tiering and deletion, compression, query and data-layout changes, caching, batching, locality and architecture changes. Keep redundancy, headroom, startup time, quotas, recovery and dependency limits intact. Treat spot or interruptible capacity and commitment purchases as separate risk decisions based on tolerant workloads and stable demand.

For DS or ML, measure experiment and notebook lifetime, training and preprocessing compute, GPU memory and utilization, checkpoint and artifact retention, feature and retrieval storage, embedding or index rebuilds, batch size, queueing, tokens and context, inference throughput, provider calls, fallback use and model quality. Compare smaller or quantized models and batching only with accepted accuracy, latency, safety and compatibility evidence.

## Prioritize value with guardrails

For every option record baseline quantity and cost, proposed mechanism, gross and net estimated savings, implementation and migration cost, time to value, confidence, dependencies, reversibility, operational effort, sustainability effect and risks to accepted SLOs, security, privacy, recovery and DS quality. Use one canonical baseline and mark interacting options to prevent adding overlapping savings.

Rank by verified net value and risk rather than percentage savings alone. Define guardrails and rollback triggers before change. Budgets, forecasts and anomaly alerts inform decisions but do not throttle critical work unless an accepted admission policy says so. Caps and quotas need owner, user-visible failure behavior and emergency override.

Implement authorized changes through versioned configuration or infrastructure where practical. Preview and verify exact targets before stopping or deleting resources, changing retention, reducing replicas, moving data or buying commitments. Preserve required data, backups, audit and recovery paths. A recommendation engine does not grant mutation or purchasing authority.

## Verify realized value

Measure resource behavior and functional, latency, error, availability, recovery, security and applicable data/model-quality guardrails before and after. Account for billing delay, demand and mix changes, partial rollout, credits, exchange rates and unrelated releases. Compare a suitable control, normalized baseline or forecast and state uncertainty.

Confirm that deleted or scaled resources remain absent, schedules and lifecycle policies execute, workload shifts did not move cost elsewhere, and operators are not compensating with manual toil. Record realized recurring and one-time savings separately from forecast savings. Feed current unit costs, ownership, budgets, capacity assumptions and accepted changes into dashboards and project logic.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production, field, assistive-technology, billing, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, exercised, observed, accepted, and verified work. Update affected project logic, runbooks, code, tests, dashboards, ownership, and decision records when accepted behavior changes. Never claim an incident resolved, a corrective action closed, a handover complete, savings realized, frontend quality achieved, or accessibility conformance from a document, tool score, estimate, or successful command alone.
