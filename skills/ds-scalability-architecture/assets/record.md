# Scalability architecture record

- Decision, rule/NFR IDs, workload/growth horizon, owners and current candidate/config:
- Current topology, state owners, consistency/tenant constraints, measured bottlenecks and failure domains:

| Option / component | Scale mechanism and routing | State, consistency and locality | Bottleneck / failure behavior | Cost, migration and evidence |
|---|---|---|---|---|

## Target and evolution

Record partitions/keys, skew and hot-key controls, shared dependencies, control/data planes, overload controls, regional behavior, DS/accelerator concerns if applicable, reversible slices, compatibility, reconciliation, and rollback or roll-forward.

## Verification

List load, skew, rebalance, dependency/failure, recovery, correctness, tenant-isolation and cost scenarios; distinguish proposed, configured and observed behavior; record residual risks, owners and next actions.
