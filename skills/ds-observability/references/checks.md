# Observability checks

- Map operational questions and critical journeys to logs, metrics, traces, profiles or events with source, owner, dimensions, freshness, retention and access.
- Define stable service/environment/version/operation/outcome/dependency identities, units and semantic conventions; propagate safe context across async and message boundaries.
- Exclude secrets and sensitive payloads at capture. Keep metric labels bounded; protect logs, baggage, traces, profiles and heap data with purpose-aware access and retention.
- Use structured logs, correct metric types and distributions, explicit sampling and profiles with known overhead. Record sampling bias, resets, buckets and aggregation.
- Cover ingress, dependencies, queues/workers, retries/cancellation and scheduled pipelines; for DS/ML add safe model/feature/index identity, quality/freshness and accelerator evidence where applicable.
- Bound and monitor collectors, buffers, backpressure, retries, drops, storage, cardinality, query cost and deletion. Define service behavior when telemetry fails.
- Validate end-to-end correlation, units, identities, redaction, cardinality and failure paths against independent counts; a dashboard alone does not prove correctness.

Use current [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) and signal-specific specifications when OpenTelemetry is selected, while verifying the implementation status of the deployed language SDK and collector.
