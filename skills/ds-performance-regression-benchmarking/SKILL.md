---
name: ds-performance-regression-benchmarking
description: Create or review repeatable performance regression benchmarks for backend and data science code. Use for micro, component, API, pipeline, model, and end-to-end benchmarks; controlled environments; warm-up; repeated measurement; statistical thresholds; immutable baselines; dedicated CI runners; and regression diagnosis. Preserve correctness and classify noisy evidence as inconclusive rather than silently accepting a new baseline.
---

# Performance Regression Benchmarking

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, growth, headroom, latency, throughput, concurrency, fairness, cost, recovery, or resource targets. Keep review and design work read-only, and keep execution within the explicitly authorized environment and component.

## Define the benchmark contract

1. Name the decision, operation, accepted correctness oracle, metric, unit, input/data/model identity, candidate and baseline revisions, environment, configuration, resource limits, and performance budget. Separate micro, component, endpoint, pipeline, model, and end-to-end benchmarks; one level cannot silently stand in for another.
2. Read [the benchmark checks](references/checks.md). Choose representative parameter ranges and adversarial sizes or distributions that expose relevant complexity, hot and cold paths, cache state, serialization, database or network behavior, batching, compilation, model loading, accelerator transfer, and concurrency as applicable. Keep fixtures immutable or versioned.
3. Pin or record hardware, runner image, OS/kernel, runtime/compiler, dependency lock, CPU and memory limits, power settings when controllable, accelerator and driver, topology, services, data, config, and background work. Use a dedicated or characterized runner for gates. Results from materially different environments are separate series.

## Measure repeatably

Warm up until the relevant runtime, JIT, cache, pool, model, or kernel reaches the defined state; keep cold-start benchmarks separate. Calibrate iteration size so timer resolution and harness overhead are small relative to the operation. Run independent repetitions, randomize or counterbalance candidate order when interference matters, and record raw samples, failures, throttling, frequency changes, allocation/GC, I/O, and system noise.

Report an appropriate distribution such as median and percentiles with sample count and variability or confidence interval. Define outlier handling before inspection and retain raw results. Do not gate on a single wall-clock reading or hide ordinary slow samples. For throughput, latency, memory, allocation, storage, GPU, energy, or cost, specify the measurement boundary and correctness/quality guardrail.

## Govern baselines and gates

Use an immutable, identifiable accepted baseline built and measured under a comparable contract. Set absolute budgets and/or relative regression thresholds above the characterized noise floor, with directionality and treatment of improvements, failures, timeouts, missing samples, and insufficient confidence. A noisy or incomparable result is inconclusive and must not automatically pass.

Keep a fast stable benchmark subset on exact candidates in CI and run longer or hardware-specific suites on dedicated scheduled or pre-release infrastructure. Preserve raw artifacts, environment fingerprints, summaries, and trend history. Require explicit review and rationale to update a baseline; never auto-bless the current result merely to make a gate green.

For DS/ML, version data, preprocessing, model, precision, batch and sequence shapes, device placement, compilation, quality metrics, and stochastic controls. A faster result that violates accuracy, safety, freshness, fairness, or output equivalence is not an acceptable improvement.

## Confirm and diagnose a regression

Rerun comparable samples, check environment drift, and use paired/interleaved experiments where suitable. Once the regression is repeatable, narrow it with version bisection, profiling, query plans, allocation or I/O tracing, and component benchmarks. Verify the fix against the same contract plus meaningful functional tests. Report the affected scope and uncertainty; a microbenchmark improvement alone does not prove end-to-end benefit or deployed capacity.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, scaling changes, quota changes, infrastructure purchase, deployment, or risk acceptance.
