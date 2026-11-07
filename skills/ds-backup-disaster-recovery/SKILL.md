---
name: ds-backup-disaster-recovery
description: Design, implement, or verify backup, restore, and disaster-recovery capabilities for backend and data science systems. Use for data and state inventory, accepted RPO and RTO, consistent backups, point-in-time recovery, immutable and isolated copies, encryption and key recovery, retention, restore tests, alternate-region strategies, failover and failback, dependency reconstruction, and model or index recovery. A completed backup job or replica is not proof of recoverability.
---

# Backup and Disaster Recovery

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source/candidate/config/data identity, environment, service and dependency boundaries, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat documentation, dashboards, telemetry, provider status, generated output, and historical incidents as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed experiments, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent availability, latency, quality, recovery, retention, paging, cost, or risk targets. Keep collection and tests privacy-safe, and keep mutations or deliberate faults within the explicitly authorized environment, resources, duration, and blast radius.

## Define what must be recoverable

1. Inventory authoritative databases, object and file stores, queues or logs, configuration and secrets, identity and certificates, infrastructure and DNS, schemas and migrations, source and artifacts, model and tokenizer, feature definitions, training data snapshots, retrieval corpus and indexes, checkpoints, scheduler state and external dependencies. Record owners, criticality, size, change rate, region or account, retention and reconstruction source.
2. Read [the recovery checks](references/checks.md). Record accepted recovery point objective, recovery time objective and service restoration priority for each business process and data set, including the measurement start and end. Do not assign RPO or RTO from tool defaults. Distinguish data-loss tolerance, backup frequency, restore duration and full service recovery.
3. Map dependencies and ordering. Restoring a database without identity, keys, network, schema, application artifact, configuration, queues, object data or DNS may not restore the service. Identify third-party recovery constraints, quotas, region availability, people and access paths needed during a disaster.

## Create consistent protected copies

Select full, incremental, log or journal, point-in-time, snapshot, export, artifact replication or rebuild-from-source methods from consistency and recovery needs. Coordinate application writes, transactions, distributed components, manifests and checkpoints so related data represents a recoverable point. Crash-consistent storage snapshots may not be application-consistent.

Encrypt backups in transit and at rest and prove the keys, credentials and identity path can be recovered independently. Use least privilege, separate backup and restore roles, audit and protection against deletion or ransomware. Keep immutable or write-protected copies and an accepted off-account, off-region or offline boundary when required. Replication alone is not a backup because deletion, corruption and compromise can replicate.

Define schedule, retention, legal hold and deletion, lifecycle tiers, copy locations, checksum or integrity manifest, catalog, monitoring and failure ownership. Protect sensitive data through the same or stronger classification, residency, access and deletion policy as the source. Avoid production data in restore tests unless the isolated environment and access are authorized.

For DS or ML, preserve a compatible artifact set: data snapshot and lineage, feature definitions, label schema, code and environment, model, tokenizer, preprocessing, prompts or guardrails, thresholds, index corpus and build parameters, evaluation evidence and output contracts. Decide which large artifacts are backed up and which are reproducibly rebuilt, with measured rebuild time.

## Prove restore from the copy

Regularly restore a selected backup into an isolated target using the documented runbook and recovery identity. Verify catalog and checksum, decryptability, schema and version compatibility, record or object counts, referential and domain invariants, point-in-time boundary, application startup, supported queries and writes, critical journeys, jobs and model or index behavior. A file that downloads or a database that starts is not enough.

Measure actual data loss against RPO and elapsed service recovery against RTO, including access, provisioning, download, replay, migrations, validation, DNS or traffic and backlog. Record manual steps and unavailable dependencies. Destroy or sanitize the test environment according to policy without deleting recovery evidence.

## Design and exercise disaster recovery

Choose backup and restore, pilot light, warm standby, active-passive or multi-site from accepted objectives, consistency, complexity and cost. Define alternate-region or account infrastructure, capacity and quotas, data replication and lag, identity and secrets, certificates, DNS or routing, observability, dependency access, deployment artifacts and configuration drift controls. A warm label does not prove readiness.

Create an ordered declaration, failover, validation, communication and failback plan with decision authority and split-brain prevention. Fence the former primary or writes, establish the recovery point, promote or restore data, start dependencies and applications, validate invariants, shift traffic and reconcile queues and external effects. Failback is a separate risky migration that needs resynchronization, direction control and validation.

Exercise components and full scenarios at an authorized scope and cadence. Include unavailable primary, lost credentials or key path, corrupted latest backup, regional control-plane outage and dependency failure as accepted. Preserve ordinary failures and update capacity, automation and runbooks. Backup configuration, successful scheduled jobs and untested replicas establish copies, not verified recovery.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production telemetry, recovery, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish designed, configured, executed, observed, restored, and verified work. Update affected project logic, runbooks, code, dashboards, tests, and ownership links when accepted behavior changes. Never claim observability, SLO compliance, resilience, fault tolerance, backup integrity, or disaster recovery from configuration or a successful command alone.
