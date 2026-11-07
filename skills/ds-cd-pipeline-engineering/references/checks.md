# CD pipeline engineering checks

- Bind exact CI-tested artifact digest and source revision to target environments, config/secrets, infrastructure, schema/data/model identities, owners, promotion order, and authority.
- Protect environments with allowed initiators, approvals or automated policy, narrow deployment identity, audit, and per-environment concurrency. Never expose production credentials to general CI.
- Verify artifact and provenance, capacity, quotas, dependencies, certificates, backups and recovery, observability, and previous known-good compatibility before mutation.
- Order infrastructure, expand/migrate/contract schema, backfills, model/index publication, application rollout, and cleanup as restartable gated steps. Do not equate app rollback with data rollback.
- Choose rollout strategy and define surge or unavailable capacity, traffic/cohort steps, dwell, readiness/warm-up, drain/handoff, progress deadline, abort, and recovery behavior.
- Gate on service health, latency/errors, queues/resources, dependencies, correctness/data/security/tenant invariants, cost, and applicable model quality/fallback. Missing telemetry blocks automatic claims.
- Require candidate/server smoke before promotion and exact-digest post-rollout verification. Test gate failure, mismatch, stall, and recovery; inspect effective environment protections. Pipeline design does not authorize deployment.

For one orchestrator example, Kubernetes documents controlled [Deployment rollouts and status](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). GitHub describes [protected deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments/); use official semantics for the selected platforms.
