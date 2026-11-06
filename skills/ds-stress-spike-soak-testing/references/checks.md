# Stress, spike, and soak checks

- Require a validated average-load baseline, correct script, representative data, generator headroom, and full-tier telemetry.
- Define one workload shape, decision, maximum load/duration, step/rise/fall, gates, abort/damage criteria, recovery window, cost, and authorized environment.
- Protect dependencies and third parties; use isolation, quotas, test tenants/data, stop controls, dashboards, and recovery ownership.
- Stress: measure saturation knee, sustainable throughput, degradation/rejection, fairness, bottleneck, and recovery at controlled stages.
- Spike: measure rise handling, queue/admission, scale/warm-up, retry amplification, fall/backlog drain, and return to baseline.
- Soak: measure time-series slopes, cycles, leaks/retention, descriptors/connections, disk/log/bloat, queues, latency/errors, and data or model quality drift.
- Verify correctness, security, idempotency, and data reconciliation during and after overload. Preserve aborted and inconclusive results.

Consult the current official test-tool guidance. Grafana k6 users can review [automated performance test types](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/) and version-matched scenario controls.
