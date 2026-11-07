# Backup and disaster recovery checks

- Inventory all authoritative data/state, config/secrets/identity, infra/DNS, schemas, queues, artifacts, DS models/features/indexes/checkpoints and dependencies with owners, criticality and reconstruction source.
- Record accepted RPO, RTO, priority and measurement boundaries per process or dataset; distinguish backup frequency, data loss, restore duration and full service recovery.
- Choose application-consistent backup/PITR/snapshot/export/rebuild methods and ordering. Protect encryption keys and restore identity independently.
- Use least privilege, audit, immutable or isolated copies and required off-region/account/offline boundaries; enforce retention, legal hold, deletion, residency and monitoring. Replication alone is not backup.
- Restore regularly into an isolated target and verify checksum, decryptability, version, counts, domain invariants, point in time, application reads/writes, journeys/jobs and applicable model/index behavior.
- Measure actual RPO/RTO including provisioning, replay, migrations, validation, traffic and backlog. Record manual dependencies and sanitize test data safely.
- Define DR topology, capacity/quotas, drift, identity, routing, split-brain fencing, failover, validation, reconciliation and failback; exercise authorized scenarios and update runbooks.

NIST's [contingency planning guidance](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) covers coordinated recovery planning. Provider guidance such as [periodic recovery testing](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_backing_up_data_periodic_recovery_testing_data.html) reinforces verifying restored data against RPO and RTO.
