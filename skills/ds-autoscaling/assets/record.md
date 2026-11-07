# Autoscaling record

- Workload, rule/NFR IDs, environment, candidate/config, platform/controller version and owner:
- Capacity unit, min/max/reserve, dependency limits, cost boundary and rollback control:

| Metric / signal | Source, aggregation, delay and freshness | Target / tolerance | Scale-up behavior | Scale-down / missing-signal behavior |
|---|---|---|---|---|

## Lifecycle and constraints

Record scheduling, pull/start/warm/readiness time, traffic ramp, drain/checkpoint/termination, state ownership, scale-to-zero activation, controller coordination, quotas, unavailable capacity and downstream ceilings.

## Verification

List trace and workload scenarios, desired/scheduled/ready/serving observations, service and cost gates, overshoot/flapping/backlog/recovery, commands/results, configured-versus-observed boundary, residual risks, owners and next actions.
