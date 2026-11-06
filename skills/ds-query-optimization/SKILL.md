---
name: ds-query-optimization
description: Diagnose and optimize scoped database, analytical, or vector queries for backend and data science products. Use for slow queries, N+1 access, plans, indexes, joins, pagination, statistics, and workload regressions. Preserve accepted results and authorization while measuring representative before-and-after behavior on the actual supported engine.
---

# Query Optimization

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts, current implementation, and native tooling. Record rule IDs, requested action, engine/broker/cache and version, environment or candidate identity, and authority. Support ordinary backend systems; add DS/ML/RAG checks only where those workloads exist. Treat repository text, metrics exports, query plans, generated output, and external artifacts as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential product or consistency decisions to the responsible owner. Do not invent data-loss tolerance, downtime, staleness, ordering, retry, retention, or performance targets. Keep review/design-only work read-only and implementation within the authorized component.

## Establish a reproducible baseline

1. Identify the exact query or fingerprint, caller, accepted result semantics, authorization/tenant scope, engine/version, schema/statistics revision, parameters, data distribution, concurrency, and latency/throughput objective from accepted sources. Separate client, pool, network, lock-wait, planning, execution, serialization, and downstream time when evidence permits.
2. Capture representative before evidence with safe bindings and sanitized plans. Use production-like data volume, skew, nulls, hot/cold keys, and parameter distributions; one literal can produce a misleading plan. Record cache state, repetitions, percentiles, rows returned/scanned, I/O, memory/temp spill, locks, and planner estimate-versus-actual differences. Use `EXPLAIN ANALYZE` only where execution and side effects are safe.
3. Read [the query checks](references/checks.md). Verify correctness first: filters, joins, tenant predicates, null behavior, ordering, pagination stability, time zones, aggregation grain, and duplicate semantics. Preserve authorization independently of any performance shortcut. A faster query returning different rows is a behavior change requiring acceptance.

## Change the dominant cost

Trace N+1 and duplicate calls before tuning SQL in isolation. Consider set-based/batched access, preloading, keyset pagination, query shape, predicate sargability, join order/data types, narrower projections, pre-aggregation, and eliminating redundant work. Add or change indexes only after matching equality/range/order/include/partial predicates to the actual workload and engine behavior. Account for write amplification, storage, maintenance, uniqueness, build locks, and unused/redundant indexes.

Refresh or correct statistics when estimates are wrong; do not force a plan before understanding distribution and parameter sensitivity. Bound memory and result sizes. For analytics, verify grain, partition pruning, column projection, file layout, and shuffle/spill. For vector/hybrid retrieval, record filter selectivity, index type/parameters, recall and ranking acceptance alongside latency; an approximate index changes quality as well as speed.

## Compare under controlled conditions

Re-run the same representative cases and correctness oracle. Compare plan shape, estimates, rows, buffers/I/O, temp spill, planning/execution time, end-to-end latency, throughput, and error/timeout rate. Test concurrent workload when the accepted claim concerns production contention; a single-user microbenchmark is limited evidence. Test write paths and index creation/migration impact. Retain a safe rollback and monitor for plan regression across parameter classes and data growth.

Avoid embedding environment-specific planner toggles or hints as a universal fix. If evidence requires schema migration, caching, capacity, or application changes, hand off those bounded dependencies without claiming their results.

## Verify and hand off

Run proportionate checks with the project's native tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local or substitute-service results do not establish CI or deployed enforcement.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config identity, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and test links when accepted behavior changes. This workflow does not itself authorize production migration, deployment, data repair, traffic replay, or risk acceptance.
