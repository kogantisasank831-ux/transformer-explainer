# CD pipeline record

- Service, rule/NFR IDs, owners, source revision, and immutable artifact or image digest:
- Environments/accounts/clusters, config/schema/data/model/infra identities, promotion policy, and deployment authority:

| Stage / environment | Preconditions and protection | Mutation / rollout step | Health and business gates | Abort / recovery / evidence |
|---|---|---|---|---|

## Compatibility and progression

Record database/event/data/model compatibility, migrations/backfills, rollout strategy, traffic/cohorts, capacity, warm-up/readiness/drain, telemetry populations/windows, missing-signal behavior, concurrency, and previous-release viability.

## Validation and handoff

List syntax or dry-run and deliberate failure/mismatch/stall/recovery results, effective permissions/protections, server smoke and post-rollout definitions, audit/retention, execution status, residual risks, owners, and next actions. State explicitly whether any environment was changed.
