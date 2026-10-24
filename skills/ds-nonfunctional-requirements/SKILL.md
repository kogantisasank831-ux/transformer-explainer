---
name: ds-nonfunctional-requirements
description: Define measurable nonfunctional and quality requirements for backend services and data science products from reviewed intent, project logic, workloads, and constraints. Use to clarify performance, scalability, availability, recovery, security/privacy, data freshness, reproducibility, maintainability, operability, cost, and applicable ML/GenAI quality boundaries before design, coding, or release evaluation. Produce traceable measurement contracts and verification plans; keep supplied targets, proposed targets, acceptance, feasibility, and actual results distinct. Do not substitute this workflow for load testing, capacity sizing, a security audit, model evaluation execution, or deployment.
---

# Backend and Data Science Nonfunctional Requirements

Convert quality expectations into testable scenarios and measurement contracts. Preserve source targets without inventing missing policies or claiming the system already meets them.

## 1. Establish scope and source intent

- Read applicable agent guidance, reviewed SRS/requirements, the target PROJECT_LOGIC.md or equivalent, architecture, and relevant assessment or measurement evidence. Record revisions and rule IDs; distinguish current evidence from proposed future behavior.
- Identify critical journeys, users, delivery stage, business loss/error costs, component boundaries, workload, operating constraints, and the named next activity. Do not carry another project's hardware, clients, budgets, or traffic into this baseline.
- Classify each source statement: qualitative expectation, supplied numeric target, accepted objective, hard constraint, proposed assumption, or open decision. A supplied target may still have incomplete measurement semantics or unproven feasibility.
- Preserve established requirement IDs and ownership. Identify which controls/targets are already mandated and which need a decision; do not silently turn a design preference into a requirement.
- Ask at most three high-impact questions per round, using existing answers first. Continue independent specification while missing decisions block only affected commitments.

## 2. Select relevant quality scenarios

Read [quality-scenarios.md](references/quality-scenarios.md). Apply backend concerns to services/workers and DS/ML/GenAI concerns only when relevant. Mark each coverage area covered, open, or not applicable with a reason; do not create speculative compliance obligations or an AI requirement for ordinary backends.

- Describe stimulus, source/actor, environment/workload, affected artifact/journey, required response, and response measure.
- Separate request acknowledgment, durable acceptance, processing completion, external delivery, and user-visible usable outcome; they may need different objectives.
- Define important overload, degraded-dependency, startup, burst, stale-data, invalid-input, unauthorized, retry/concurrent, recovery, and partial-failure conditions as applicable.
- Keep deterministic functional invariants and policies linked to their FR/business-rule IDs rather than relabeling everything as an NFR. Link model/data quality to its evaluation requirements; a successful HTTP request is not proof of a useful or correct model answer.

## 3. Write explicit measurement contracts

Read [measurement-and-verification.md](references/measurement-and-verification.md) before defining a metric, denominator, or pass/fail result.

For each NFR record:

| Field | Record |
|---|---|
| ID, scenario, source | Stable project ID, required response, rationale, source/revision and related rules/journeys. |
| Scope and workload | System boundary, environment, traffic/batch/input distributions, dependency state, warm/cold/cache state, data/model/config versions when relevant. |
| Measure | Metric/formula, units, start/end events, eligible population/denominator, success/failure classification, percentile/aggregation, observation window and sample support. |
| Target and decisions | Supplied value if any; proposed alternatives/rationale; threshold, exceptions and policy acceptance status; unresolved fields with decision IDs. |
| Verification | Instrumentation/data source, test/analysis/inspection/demonstration method, reproducible conditions, evidence required, and failure/insufficient-evidence behavior. |
| Ownership and state | Decision/operating/verification owner or unassigned; evidence/feasibility state; accepted/proposed/unresolved/superseded decision state; planned/executed actual verification separately. |

- Do not replace unspecified values with arbitrary latency, availability, coverage, memory, quality, retention, or cost targets. Offer numeric proposals only with explicit rationale and pending status; preserve source-supplied values even if feasibility is unknown.
- Distinguish registered users, active users, in-flight requests, arrival rate, batch volume, and completed useful work. A user count alone cannot establish requests per second, concurrency, hardware, or a percentile guarantee.
- Define how errors, timeouts, rejected/abandoned requests, retries and cached/fallback responses affect both latency and success/quality measures. Do not meet a latency objective merely by dropping slow work or returning unusable outputs.
- Specify latency percentiles per relevant journey and the end-to-end boundary. Streaming first-token time, queue wait, service time, and completed-answer latency are different measures. Do not sum component percentiles to assert an end-to-end percentile.
- Define availability as request-based, time-based, or another explicitly scoped useful-outcome measure, with its window, denominator, dependency treatment and exclusions. Do not invent maintenance exclusions or translate request success into allowed downtime.
- Distinguish RTO from RPO and both from backup frequency; define failure event, restore boundary, data cutoff and integrity checks. Require restore/recovery evidence rather than inferring recoverability from a scheduled backup.

## 4. Separate quality, cost, and resource tradeoffs

- For ML, specify evaluation population/version, baseline, split, leakage safeguards, metric aggregation, important slices/support, uncertainty and acceptance rule. Preserve unknown thresholds; do not promise accuracy or quality from architecture, hardware, a random seed, or a judge score alone.
- For GenAI, distinguish retrieval/grounding/citation quality, task/tool success, abstention/coverage, time-to-first-token, full completion, token/cost budgets, and data/tool permissions. Couple performance/cost objectives with applicable quality and policy guardrails.
- Specify resource/cost budgets with measurement boundaries, utilization/workload assumptions, billing/accounting scope and currencies/time periods when applicable. Verify current primary prices/specifications if using real numbers; label estimates and unproven feasibility.
- Surface tradeoffs among latency, throughput, memory, quality, cost, privacy and recovery. Do not silently satisfy one target by changing accepted retention, fallback, authorization, model quality or error policies.
- Use project authority for consequential policy/target decisions. Make routine reversible measurement/tooling choices within authorized scope; do not impose approval for every technical detail or force unattainable goals into a fake complete baseline.

## 5. Define verification and scoped readiness

- Plan representative workload, duration/window, environment/versions, dependency conditions, success/negative/degraded cases, observation method, evidence and completion criteria. Identify what must be instrumented or clarified before the requirement is testable.
- Distinguish specification completeness, empirical feasibility and demonstrated compliance with the target. A measurable accepted requirement can remain untested; a benchmark pass in one environment does not establish a general guarantee.
- If measurement is unavailable, propose a focused experiment with the question and exit criterion. Use insufficient evidence, not pass, when workload/window/sample support is missing or unsuitable.
- Do not implement instrumentation, install tools, run load/fault/security tests, train/evaluate models, spend money, access production, or deploy as part of this specification unless separately requested. Inspect authorized existing evidence without exposing sensitive records.
- Resolve contradictions and overlapping metrics; state which exact commitments remain blocked and which design/coding tasks can proceed. Do not infer acceptance from silence, urgency, or a completed template.

## 6. Persist and hand off the baseline

Use [nonfunctional-baseline.md](assets/nonfunctional-baseline.md) as a scalable output; compress for small requests and mark irrelevant sections with reasons. Present in conversation unless artifact/project-document maintenance is requested; follow host storage rules for requested files.

- When project-document maintenance is in scope, update its established quality/SRS document or create docs/NONFUNCTIONAL_REQUIREMENTS.md and link it from PROJECT_LOGIC.md. Incorporate accepted answers and effective constraints into the logic index/domain rules using the existing handoff procedure when available; keep proposals/open targets labeled and preserve IDs/history.
- Hand architecture/coding/testing workflows the logic/NFR revisions, relevant IDs, measurement contracts, accepted constraints, open policy/feasibility questions, expected verification, and affected dependency boundaries.
- State readiness for the named next activity only: ready, conditionally ready, or blocked with specific dependencies. Report actual persistence and actual checks separately from planned tests; never claim production readiness or stakeholder acceptance without evidence.
- Verify specialist skill availability before invoking another workflow. Keep detailed SLO/alert operations, load/capacity measurement, security verification, model evaluation, and implementation as distinct downstream tasks.
