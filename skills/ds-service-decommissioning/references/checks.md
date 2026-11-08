# Service decommissioning checks

- Bind exact service/version/environments, capability, owners, authority, target dates, replacement or cessation, scope and rollback window.
- Inventory consumers, APIs/events/jobs, data/queues/caches, DNS/certs/IAM/secrets, code/artifacts/CI/IaC, telemetry, backups, vendors/cost and applicable ML pipelines/features/models/indexes.
- Combine telemetry, billing, search and owner confirmation over an accepted window; missing observability is unknown usage.
- Migrate and verify contract, identity, errors, performance and applicable model quality before staged deprecation, drainage, reversible disablement and deletion.
- Reconcile in-flight work and prevent stale retries from recreating state. Audit any temporary break-glass path.
- Map retention, legal hold, export, archive, restore, deletion and sanitization across replicas, logs, caches, backups, feature/model/index artifacts and providers.
- Revoke access and remove routing, infrastructure, delivery, monitoring, ownership, quotas, licenses and contracts in dependency order with reviewed exact targets.
- Verify replacement journeys and absence of traffic, jobs, orphan state, credentials, resources and charges through an observation window; quiet telemetry is insufficient.

Use current [NIST SP 800-88 Rev. 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final) for media-sanitization program guidance while applying the target organization's retention, cloud, legal and disposal requirements.
