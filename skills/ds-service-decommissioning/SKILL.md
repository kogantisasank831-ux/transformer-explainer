---
name: ds-service-decommissioning
description: Plan and execute authorized retirement of backend and data science services without orphaning consumers, data, access, infrastructure, or obligations. Use for dependency and usage discovery, replacement and migration, deprecation, traffic and job drainage, archival and retention, deletion and sanitization, identity and secret revocation, infrastructure removal, model and feature retirement, rollback windows, billing closure, and evidence-based completion.
---

# Service Decommissioning

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data/model identity, environment, affected users and consumers, owners, and authority. Support ordinary backend retirement where applicable; use ML-specific validation, training, evaluation, and serving controls only for systems that contain those components. Treat documentation, registries, dashboards, experiment trackers, generated reports, and provider metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, data, model-risk, retention, quality, or release choices to the responsible owner. Do not invent usage, retention, quality, reproducibility, fairness, safety, latency, throughput, cost, or acceptance targets. Protect personal, confidential, licensed, and model-sensitive data and keep mutations within the explicitly authorized environment and scope.

## Prove the retirement boundary

1. Read [the decommissioning checks](references/checks.md). Identify the exact service, endpoints, domains, versions, environments, accounts, owners, business capability, replacement or termination decision, authority, target dates and rollback window. State whether the work covers deprecation, traffic disablement, data retirement, infrastructure deletion, contract termination or full closure.
2. Inventory callers and consumers, APIs and events, scheduled and background jobs, databases and object stores, caches and queues, DNS and certificates, identity and network grants, secrets and keys, repositories and artifacts, CI/CD and IaC, observability and alerts, backups and archives, vendors and licenses, budgets and support obligations. For DS/ML add pipelines, datasets, feature definitions and stores, model registry entries, checkpoints, tokenizers, indexes, prompt assets, accelerators and downstream predictions.
3. Use access logs, traces, billing, ownership catalogs, code/config search, event subscriptions and stakeholder confirmation across an accepted observation window. Missing telemetry is an unknown, not zero usage. Record dormant, emergency, seasonal, manual and external consumers separately.

## Migrate and deprecate before removal

Define the future capability and contract, including the replacement, manual process or explicit cessation. Map each consumer and dataset to migrate, retire or accept as an exception. Verify identity, authorization, semantics, ordering, error behavior, performance, data/model quality and support for the replacement. For model changes, compare output schema, feature and label semantics, quality and safety gates, thresholds, explanations and fallback behavior.

Publish deprecation with affected versions, migration steps, support dates and escalation. Stop new onboarding and update SDKs, examples, documentation and ownership catalogs. Use progressive stages where risk warrants: shadow or dual-read, migrate, read-only, reject new work, drain, disable with rapid re-enable, observe, then delete. Do not maintain unsafe dual writes without reconciliation and a named authority.

Drain requests, connections, queues, retries, workflows and scheduled runs using explicit completion and timeout rules. Reconcile partial, duplicate and external effects. Prevent retries or stale clients from recreating state after disablement. Preserve an authorized break-glass path only for the accepted period and audit it.

## Retain, transfer, delete and sanitize data

Classify each record, object, log, backup, replica, cache, queue, feature value, training snapshot, model artifact and index by owner, purpose, legal hold, retention, export, deletion and reconstruction needs. Verify required archives can be restored and interpreted with schemas, keys, code and documentation before deleting the source. An archive job success does not prove usable preservation.

Delete data through all applicable lifecycle paths and record limitations for immutable backups or third parties. Revoke encryption material only when the accepted sanitization design and recovery obligations allow it. Validate deletion or sanitization at the logical and media boundary appropriate to the environment and sensitivity. Do not use a database row delete as proof that replicas, indexes, logs, caches, snapshots or provider copies are gone.

For data/model artifacts retained for audit or reproducibility, restrict access, record provenance and retention, and prevent accidental serving or retraining. Remove retired features and models from selection, routing and fallback paths before deleting artifacts.

## Remove capability and verify closure

Revoke service accounts, IAM roles, tokens, secrets, keys, certificates, firewall rules, webhooks, vendor access and support contacts. Remove or update DNS, routes, load balancers, registries, deployment pipelines, IaC resources and state, monitors, alerts, dashboards, runbooks, status pages, quotas, reservations and licenses in dependency order. Preserve audit evidence without leaving an active credential.

Use reviewed plans and exact contexts for destructive actions. Keep backups, rollback artifacts and replacement capacity through the accepted window. Confirm restoration or re-enable steps before crossing irreversible points; a rollback plan based on deleted keys or incompatible schemas is not viable.

After disablement and deletion, verify no accepted traffic, jobs, subscriptions, errors, retries, orphan data, identities, infrastructure or charges remain. Test replacement journeys and downstream state, close contracts and ownership records, and monitor for the defined observation period. Record unresolved third-party retention, archives and exceptions. A quiet dashboard alone does not prove full decommissioning.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, restoration, model quality, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, accepted, released, retired, and verified work. Update affected project logic, code, tests, contracts, data/model records, documentation, ownership, and decisions when accepted behavior changes. Never claim decommissioning, data fitness, reproducibility, model approval, or inference optimization from a plan, successful command, tracked run, aggregate score, or theoretical calculation alone.
