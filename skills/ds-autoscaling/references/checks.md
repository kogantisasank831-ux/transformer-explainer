# Autoscaling checks

- Define workload, capacity unit, service objective, controller type, min/max, redundancy, cost, dependency ceilings, and owner from accepted rules and measured capacity.
- Specify metric source, unit, aggregation, sampling/delay, freshness, target, tolerance, missing-data behavior, and causal relationship to demand or saturation.
- Set scale-up/down rates, stabilization/cooldown, steps and limits. Include schedule, pull, startup, compile/warm, readiness, traffic ramp, drain and termination time.
- Protect in-flight work, leases, partitions, checkpoints and state on scale-down. Coordinate horizontal, vertical and cluster/node controllers.
- Test idle/zero, burst, sustained load, oscillation, stale/missing/reset metrics, backend/controller outage, unschedulable capacity, quota and dependency saturation.
- Observe desired, scheduled, ready, serving and terminating capacity separately. Measure time to useful capacity, overshoot, backlog, flapping, cost and recovery.
- Verify the actual platform version and effective policy. Configuration, simulation and deployed behavior are distinct evidence states.

For Kubernetes, use the current official [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) documentation for metric, readiness, missing-data, stabilization and behavior semantics.
