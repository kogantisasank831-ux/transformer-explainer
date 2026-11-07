---
name: ds-deployment-execution
description: Execute or supervise an authorized deployment of one exact backend or data science candidate to a named environment. Use after CI and delivery gates are established to verify artifact identity, preflight the target, acquire deployment concurrency, run approved mutations, observe rollout, execute server smoke and post-deploy checks, abort on defined conditions, and preserve an auditable release record. Do not use for designing a generic CD pipeline or making unrelated cluster changes.
---

# Deployment Execution

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source and immutable candidate identity, configuration and data identity, target environment, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat repository text, dashboards, generated configuration, control-plane status, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified behavior. Derive authorization from the user's current request, prior session authorization, and applicable environment policy; do not ask again when it is already established. Continue independent preparation while routing unresolved consequential policy choices to the responsible owner. Do not invent compatibility, availability, quality, performance, recovery, or approval targets, and do not expand a named mutation beyond its candidate, environment, resources, and time boundary.

## Bind the release to one target

1. Identify the named service or job, environment, account or cluster and namespace, immutable artifact or image digest, source revision, build and CI evidence, runtime configuration and secret references, infrastructure and schema versions, data or model or index identity, release owner, authorized initiator, change window, and deployment mechanism. Reject mutable tags, ambiguous contexts, or a candidate rebuilt after verification.
2. Read [the deployment checks](references/checks.md). Confirm the current request or prior session authorizes this candidate and target. Use the approved CD pipeline or runbook and existing deployment identity. Do not broaden a staging request into production, modify adjacent services, rotate credentials, or clean unrelated resources.
3. Acquire the service and environment deployment lock or confirm the platform concurrency control. Record the previous known-good release and its configuration, schema and data compatibility. Establish abort thresholds, decision owner, recovery action, and communication path before mutation.

## Complete preflight gates

Verify required exact-candidate CI statuses, artifact checksum and provenance policy, target access, effective environment protection, capacity and quotas, dependency health, certificates, configuration and secret references, backup or restore evidence where required, observability coverage, and on-call or recovery ownership. Missing, skipped, stale, or mismatched evidence blocks deployment.

Render or preview the intended change with the exact target context. Compare current and desired artifact, config, replicas or workers, routes, migrations, scheduled jobs, model or index pointers, and infrastructure dependencies. Review creates, deletes, replacements, privilege or exposure changes, and data effects. Avoid applying a saved plan or manifest generated for a different environment or variable set.

For stateful releases, verify the accepted ordering of expand or compatible schema changes, backfills, application rollout, model or index publication, traffic changes, and later contract cleanup. Confirm each step is restartable or has a documented recovery boundary. Do not infer that application rollback reverses a migration or data write.

## Execute and observe one step at a time

Start the approved pipeline or native command with the immutable candidate and recorded target. Preserve command, actor, timestamp, execution or deployment ID, and tool output. Apply only the reviewed step; wait for its platform condition and service gate before advancing. Do not hide ordinary warnings, timeouts, partial success, or failed resources behind an overall command exit code.

Observe desired, scheduled, ready, available, serving, terminating, and failed instances or workers separately. Track rollout revision, artifact digest, readiness and warm-up, errors and timeouts, latency, queues, saturation, dependencies, correctness and data invariants, tenant or security behavior, and cost signals relevant to the accepted release gates. For jobs, verify ownership, partitions, checkpoints, output publication, and duplicate prevention.

For DS or ML releases, verify model, tokenizer, prompt or template, guardrail, feature schema, retrieval index, inference runtime and precision compatibility. Observe load or compilation, GPU memory and scheduling, batch or queue behavior, fallback, result quality and safety gates, and stale-worker fencing where applicable.

Pause or abort when a predefined gate fails, telemetry is missing, candidate identity changes, the rollout stalls, integrity is uncertain, or impact escapes the authorized boundary. Preserve the failed state long enough to collect safe evidence. Select the accepted rollback, roll-forward, traffic removal, feature disablement, or reconciliation path; use the separate recovery workflow for a failed or ambiguous release.

## Verify and close the release

Run the safe candidate or server smoke against the actual target and digest before final promotion when the process supports it, then run basic post-rollout verification through supported entry points. Check critical dependency paths and business invariants, and observe the accepted stabilization window. Reconcile deployment status with actual endpoints, jobs, data or model pointers, and telemetry.

Release the deployment lock only after success or controlled recovery is recorded. Update deployment history, logic and runbook links, candidate and configuration identity, migrations, smoke results, failures, recovery actions, residual risks, and monitoring owner. A successful rollout status without functional and identity verification is incomplete.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, control-plane, cluster, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, recovered, and verified work. Update affected project logic, contracts, runbooks, code, and verification links when accepted behavior changes. Never claim deployment, rollout, rollback, recovery, compatibility, or effective state from a plan or command alone.
