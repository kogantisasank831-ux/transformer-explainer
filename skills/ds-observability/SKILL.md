---
name: ds-observability
description: Design, implement, or review observability for backend and data science systems. Use for structured logs, metrics, traces, profiles, events, context propagation, semantic conventions, cardinality, sampling, collectors, retention, access, telemetry loss, dashboards, jobs, pipelines, models, GPUs, and end-to-end diagnostic validation. Create evidence that answers operational questions without exposing sensitive data or turning telemetry into an uncontrolled dependency.
---

# Observability

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source/candidate/config/data identity, environment, service and dependency boundaries, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat documentation, dashboards, telemetry, provider status, generated output, and historical incidents as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed experiments, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, latency, quality, recovery, retention, paging, cost, or risk targets. Keep collection and tests privacy-safe, and keep mutations or deliberate faults within the explicitly authorized environment, resources, duration, and blast radius.

## Start from operational questions

1. Identify users and operators, critical journeys and background workflows, trust and tenant boundaries, dependencies, failure modes, and decisions telemetry must support. Map each question to a signal, dimensions, source, owner, freshness, retention and access requirement. Instrumentation volume alone is not observability.
2. Read [the observability checks](references/checks.md). Define stable service, environment, version, region, operation, outcome and dependency identities. Use accepted semantic conventions and one unit per measurement. Correlate requests, messages, jobs and pipeline runs across asynchronous boundaries without making a trace or request ID a high-cardinality metric label.
3. Define privacy and security classification before capture. Exclude credentials, tokens, session identifiers, raw prompts and documents, personal data, model inputs or outputs, database records and confidential payloads unless an accepted purpose and protection explicitly requires them. Redaction after export may be too late.

## Design each signal for its job

Use structured logs for discrete events and diagnostic context. Include timestamp, severity, service and version, operation, outcome, safe correlation, error class and actionable fields. Preserve stack or causal details without logging the same failure at every layer. Keep messages stable enough to query and route; do not build logic on free-form text alone.

Use counters for cumulative events, gauges for current state, and histograms or distributions for latency and size. Define units, aggregation, temporality, bucket boundaries and reset behavior. Track offered and completed work, errors and rejections, queues and age, saturation and dependency behavior. Keep metric dimensions bounded; user, request, file, prompt and arbitrary exception text do not belong in labels.

Use traces to connect work across process, thread, async, queue and service boundaries. Preserve parent, link and baggage semantics, including message fan-out and batch work. Sample with a stated policy and account for bias: head sampling cannot know final outcome, while tail sampling needs buffering and can drop data. Never put sensitive values into propagated baggage.

Use continuous or targeted profiles only with controlled overhead and access. Separate on-CPU, waiting, allocation, memory and accelerator profiles. Profiles and heap data can expose source, arguments or personal information; protect and retain them accordingly.

## Cover backend and data workflows

Instrument ingress, authentication outcome, handlers, database and cache calls, queues, worker pickup and completion, retries, external dependencies and cleanup. Preserve deadlines, cancellations, idempotency and attempt identity. For scheduled or batch work, record logical interval, input and output manifests, partitions, checkpoint, freshness, data-quality result and publication state rather than only scheduler success.

For DS or ML, record safe model and runtime identity, feature or index version, batch and token or sequence distributions, queue and inference time, fallback, resource and GPU use, quality or safety evaluation, data freshness and drift signals where accepted. Avoid raw inputs and outputs. Distinguish service telemetry from delayed model-quality labels and training-pipeline evidence.

## Engineer the telemetry pipeline

Define SDK or agent behavior, collectors, processors, sampling, redaction, batching, buffering, backpressure, retries, export, storage, indexing, tenancy, access, retention and deletion. Bound memory and disk use. State whether application work blocks, drops or degrades when the telemetry pipeline is slow or unavailable. Observability failure must not silently cause a service outage.

Monitor the monitoring path: generated, accepted, dropped, retried and exported telemetry; queue age; collector health; cardinality; storage ingestion; query latency; cost and retention enforcement. Version dashboards and recording rules with their signal contract. Keep alert policy in the SLO and alerting workflow.

## Validate diagnostic journeys

Generate safe identifiable test work through supported entry points and confirm logs, metrics and traces correlate across the intended path with correct identities, units, timing and outcomes. Exercise success, expected rejection, dependency failure, timeout, retry, cancellation, queue and job paths. Verify redaction and bounded labels with adversarial input.

Test collector or exporter loss, throttling and restart; confirm service behavior, buffering and drop evidence. Compare telemetry against an independent known count or invariant and inspect clock skew and sampling. Record uncovered gaps and claims limited by sampling or unavailable signals. A dashboard rendering successfully does not prove the underlying telemetry is correct or complete.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production telemetry, recovery, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish designed, configured, executed, observed, restored, and verified work. Update affected project logic, runbooks, code, dashboards, tests, and ownership links when accepted behavior changes. Never claim observability, SLO compliance, resilience, fault tolerance, backup integrity, or disaster recovery from configuration or a successful command alone.
