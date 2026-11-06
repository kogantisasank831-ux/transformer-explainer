---
name: ds-data-pipeline-reliability
description: Design, implement, or review reliable batch and streaming data pipelines for backend analytics and data science products. Use for partitioning, checkpoints, watermarks, late data, schema evolution, data quality, lineage, retries, backfills, atomic publication, and reconciliation. Preserve deterministic data semantics and independently validate outputs.
---

# Data Pipeline Reliability

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, candidate/config/data identity, environment, workload, and authority. Support ordinary backend systems; apply data science, ML, RAG, and GPU checks only where those components exist. Treat repository text, telemetry, profiles, generated output, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, and unknowns. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent retry, data-loss, lateness, throughput, latency, concurrency, duration, recovery, or resource targets. Keep review/design work read-only and execution within the explicitly authorized environment and component.

## Define the data contract and run identity

1. Identify source owners and contracts, extraction mode, event/processing time, partition or offset grain, schema/version, key and deduplication semantics, lateness/correction policy, transformation rules, destinations, consumers, and accepted quality/freshness requirements. Record code/config/environment and run identity. “Latest” is not a reproducible input.
2. Read [the pipeline checks](references/checks.md). Map each stage's authoritative inputs, immutable locators or snapshots, expected cardinality, output partition, side effects, retry boundary, and lineage. Distinguish scheduler success, task success, data publication, downstream visibility, and business completeness.
3. Make tasks deterministic for a fixed logical interval and input snapshot. Use stable partitioning, UPSERT/merge or replace-partition semantics as accepted, and explicit time zones. Do not use wall-clock `now()` for business logic in a replayable run. Keep large artifacts in durable shared storage rather than worker-local files.

## Publish complete outputs

Write to staging or immutable versioned locations, validate schema and quality, then atomically publish through a manifest, partition commit, table transaction, or version pointer. Downstream consumers should see the previous complete version or the new complete version, never partial output. Define cleanup for abandoned staging data.

Checkpoint offsets or partitions only after durable output is committed. Bind checkpoint to source identity, code/config, schema, and output version. For streams, define watermark, allowed lateness, window closure, deduplication horizon, correction/retraction, and replay behavior. “Exactly once” must be proven end-to-end; otherwise state duplicate/loss boundaries and make sinks idempotent.

## Validate and reconcile data

Use contract checks plus independent domain invariants: schema/types, nulls, uniqueness, referential integrity, ranges, volume, partition completeness, source-to-target counts/totals, freshness, distribution drift, and quarantine accounting. Define accepted tolerances and owners; a quality framework's green status does not validate an incorrect rule. Fail or quarantine according to accepted policy without silently dropping records.

Preserve column/row lineage, source snapshots, transformations, code/config, environment, and output manifests. For ML, add feature availability time, label construction, leakage checks, training/evaluation split lineage, model consumer compatibility, and artifact linkage.

## Backfill and recover safely

Plan backfill scope, immutable inputs, partition order, concurrency, rate/resource limits, interaction with live runs, destination isolation, validation, and promotion. Prevent a backfill from overwriting newer data or triggering unintended downstream effects. Test interruption/resume, duplicate run, partial source, late/corrected events, schema changes, corrupted/quarantined records, destination failure, and scheduler/worker restart. Reconcile published partitions and consumer-visible state after recovery.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, or substitute-service results do not establish CI or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, executed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize production traffic generation, data replay, destructive recovery, deployment, or risk acceptance.
