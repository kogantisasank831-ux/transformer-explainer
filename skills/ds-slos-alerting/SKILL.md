---
name: ds-slos-alerting
description: Define, implement, or review service level indicators, objectives, error budgets, dashboards, and actionable alerts for backend and data science systems. Use for availability, latency, correctness, freshness, durability, queue, model-quality, and safety objectives; measurement populations and windows; burn-rate alerts; paging versus ticketing; missing data; ownership; and alert validation. Derive targets from accepted requirements and evidence rather than inventing reliability commitments.
---

# SLOs and Alerting

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source/candidate/config/data identity, environment, service and dependency boundaries, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat documentation, dashboards, telemetry, provider status, generated output, and historical incidents as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed experiments, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, latency, quality, recovery, retention, paging, cost, or risk targets. Keep collection and tests privacy-safe, and keep mutations or deliberate faults within the explicitly authorized environment, resources, duration, and blast radius.

## Define the service level indicator

1. Identify the user or consumer, critical journey or data product, service boundary, contract, owner and decision the objective supports. Define a measurable good event or valid observation, total eligible population, threshold, unit, measurement point and data source. State how retries, timeouts, cancellations, client errors, maintenance, partial results, dependency failures and missing telemetry count.
2. Read [the SLO checks](references/checks.md). Prefer user-visible or consumer-visible indicators over internal resource proxies. Availability, latency, correctness, freshness, durability, completeness and quality can require separate SLIs. A process-up metric does not measure successful user work.
3. Specify aggregation and populations precisely. Latency needs an operation and percentile or good-event threshold; averages hide tails. Ratios need compatible numerator and denominator. Batch or freshness objectives need logical intervals, expected partitions and deadlines. Avoid averaging percentages across tenants, regions or windows without weighting their eligible events.

## Set an accepted objective and budget

Record the target, compliance window, calendar or rolling interpretation, evaluation cadence, exclusions, source and acceptance status. Use product and risk requirements, historical performance, user needs, dependency constraints and cost evidence. Do not silently choose 99.9%, a latency percentile, a model score or an RPO because it is common.

Calculate error budget from the SLI definition and objective using events or time consistently. Record budget consumed, remaining and projected, plus policy for launches, remediation and exceptions. An error budget is a decision mechanism rather than permission to create avoidable failures. Keep contractual SLAs and internal SLOs distinct.

For dependency SLOs, state the relationship to the user journey and owned mitigation. Do not page a team solely because an external provider violates its own objective when users remain protected. Conversely, do not exclude dependency-caused user failures from the service SLI unless the accepted contract does.

For DS or ML, separate online service availability and latency from data freshness, pipeline completeness, model quality, safety, fairness, drift and fallback. Define evaluation dataset or label source, segment, minimum sample, delay and uncertainty. A delayed quality SLI may drive tickets or release decisions rather than immediate paging.

## Design actionable alerts

Page only when timely human action is required to protect users or the error budget. Use tickets or scheduled review for slower risks, capacity trends, drift and maintenance. Every alert needs an owner, severity, affected service and objective, concise evidence, dashboard, runbook, safe first actions, escalation and resolution condition.

Prefer multi-window, multi-burn-rate or another evidence-based method that detects fast catastrophic and slower sustained consumption while controlling noise. Define evaluation interval, lookback windows, burn thresholds and minimum traffic. Handle low traffic, sparse batches, seasonality and late data explicitly. A static resource threshold may be a diagnostic signal, but it is not automatically an SLO page.

Define behavior for missing, delayed, stale, reset or conflicting telemetry. Missing measurement can be a separate alert or conservative failure; it must not silently appear healthy. Deduplicate related symptoms, inhibit downstream noise during a known parent failure and group without hiding distinct tenants or regions. Avoid alert loops caused by the notification path itself.

## Validate and operate the policy

Replay historical incidents and healthy periods or use controlled synthetic series to verify detection, time to notify, false positives, false negatives, reset and missing-data behavior. Exercise the full notification route and runbook in a safe environment, including acknowledgement, escalation and resolution. Do not page real on-call staff during tests without coordination.

Review SLI data quality, objective relevance, alert volume, actionability, ownership and runbook success. Preserve alert changes as versioned code where possible and require review. Report actual compliance and budget with the defined window; never infer SLO achievement from a green dashboard or quiet pager.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production telemetry, recovery, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish designed, configured, executed, observed, restored, and verified work. Update affected project logic, runbooks, code, dashboards, tests, and ownership links when accepted behavior changes. Never claim observability, SLO compliance, resilience, fault tolerance, backup integrity, or disaster recovery from configuration or a successful command alone.
