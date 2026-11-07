# Backup and disaster recovery record

- System, rule/NFR IDs, owners, business priorities and test or event authority:
- Accepted RPO/RTO and boundaries, source/config/schema/data/model identities, backup and DR topology:

| Asset / process | Backup or rebuild method and consistency | Location / retention / protection | Restore validation | Measured RPO / RTO / owner |
|---|---|---|---|---|

## DR dependencies and sequence

Record infrastructure, capacity/quotas, identity/keys/secrets, DNS/routing, data replication/lag, split-brain fencing, artifact/config drift, failover, backlog and external-effect reconciliation, and failback.

## Verification and handoff

List restore/drill commands and results, checksum and domain/application/model tests, failed copies or steps, manual dependencies, test-data cleanup, runbook updates, residual risks, owners and next actions. State whether any live failover or production restore occurred.
