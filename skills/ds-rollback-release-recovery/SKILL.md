---
name: ds-rollback-release-recovery
description: Assess and execute authorized rollback or roll-forward recovery for failed backend and data science releases. Use for release containment, artifact and configuration restoration, feature disablement, traffic removal, database or data compatibility, model and index recovery, in-flight work reconciliation, rollback validation, and release-history closure. Decide from current effective state rather than assuming the previous application version can safely reverse every change.
---

# Rollback and Release Recovery

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source and immutable candidate identity, configuration and data identity, target environment, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat repository text, dashboards, generated configuration, control-plane status, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified behavior. Derive authorization from the user's current request, prior session authorization, and applicable environment policy; do not ask again when it is already established. Continue independent preparation while routing unresolved consequential policy choices to the responsible owner. Do not invent compatibility, availability, quality, performance, recovery, or approval targets, and do not expand a named mutation beyond its candidate, environment, resources, and time boundary.

## Stabilize and identify the release state

1. Confirm the affected service, environment, incident or release owner, current and previous artifact and configuration digests, deployment revision, infrastructure and schema state, data migrations and backfills, model or index pointers, traffic exposure, active jobs and messages, and observed impact. Freeze further automated promotion and competing deployments without blocking unrelated emergency safety work.
2. Read [the recovery checks](references/checks.md). Establish authority from the active incident or release process and use the approved recovery identity and runbook. Preserve timestamps, events, logs, metrics, change records and command output with redaction. Avoid speculative cleanup, broad restarts and state deletion that destroy evidence or increase impact.
3. Contain impact through the narrowest accepted mechanism: pause rollout, stop promotion, remove candidate traffic, disable a feature, reject new work, stop a scheduled trigger, drain or fence workers, or isolate a dependency. Maintain security and tenant boundaries and verify containment took effect.

## Decide rollback, roll forward, or compensate

Compare the current effective state with the previous known-good release and target recovery state. Evaluate application and API compatibility, configuration and secret references, database schema and data mutations, event and message formats, caches and sessions, infrastructure, feature flags, model or tokenizer or feature schema, retrieval index, checkpoints, external side effects and irreversible operations.

Choose rollback only when the previous artifact can run safely against the current schema, data, configuration and dependencies, capacity still exists, and the rollback mechanism is tested. Application rollback does not undo database changes, sent messages, billing, external calls, model-produced decisions or partial backfills. Define reconciliation or compensation for effects that remain.

Choose roll forward when backward compatibility is absent, the repair is smaller and safer, migrations cannot reverse, or returning traffic to the previous version would corrupt data. A roll-forward candidate still requires scoped tests, exact artifact identity and release gates proportional to the incident; urgency does not turn an untested build into a known-good release.

Feature or configuration restoration can be faster than binary rollback, but verify version compatibility, propagation delay, cache invalidation and audit. Database down migrations require explicit data-loss and lock analysis plus backup or restore evidence. Prefer accepted forward-compatible expand or contract recovery over destructive reversal when possible.

For DS or ML releases, restore a compatible set of model, tokenizer, prompt or template, guardrails, feature transformations, retrieval index, inference runtime, thresholds and routing policy. Reconcile predictions, cached results, queued requests, online learning or feedback, and downstream decisions. A model pointer change alone is incomplete if features or indexes changed.

## Execute one recovery plan

Record the recovery target, ordered steps, owner, command or pipeline, abort criteria, concurrency lock and verification at each step. Use immutable artifact or configuration identities and the platform's approved rollback, promotion or traffic control. Prevent stale deployment controllers, workers or jobs from reapplying the failed state.

Observe controller and instance state, traffic, errors, latency, saturation, dependencies, correctness and data invariants, security and tenant behavior, queues and retries, background jobs, schema and replication, and applicable model quality. If recovery makes impact worse or state becomes ambiguous, stop and escalate to the next accepted containment or restore plan rather than repeatedly toggling versions.

## Reconcile and close

Run server smoke and critical business or data checks against the recovered environment and exact identities. Reconcile in-flight requests, messages, leases, jobs, checkpoints, partial outputs, caches, sessions, schema/data/model/index versions and external side effects. Verify alert recovery and observe the accepted stabilization window; a lower error rate alone is not proof of data correctness.

Record what was reverted, retained, compensated, rebuilt or left for follow-up; final artifact, config, schema and data or model state; commands and actors; failed recovery attempts; residual customer or data impact; monitoring and communication owners. Create durable regression coverage and update runbooks and compatibility rules after stabilization. Keep incident analysis factual and do not erase the failed revision or evidence from release history.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, control-plane, cluster, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, recovered, and verified work. Update affected project logic, contracts, runbooks, code, and verification links when accepted behavior changes. Never claim deployment, rollout, rollback, recovery, compatibility, or effective state from a plan or command alone.
