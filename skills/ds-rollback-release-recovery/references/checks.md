# Rollback and release recovery checks

- Identify current, failed, previous and target artifact/config revisions plus infra, schema/data/model/index state, traffic, jobs/messages, owner, authority and impact; freeze competing promotion.
- Preserve evidence and contain narrowly through pause, traffic removal, feature disablement, admission control or worker fencing; verify containment and tenant/security boundaries.
- Decide rollback, roll forward, config restore or compensation from current compatibility and irreversibility. App rollback does not undo data, messages, external effects or backfills.
- Verify previous-version capacity and compatibility, or test an exact roll-forward candidate. Analyze down migrations for data loss and locks; preserve backup/restore evidence.
- For DS/ML, restore a compatible model, tokenizer, prompts/guardrails, features, index, runtime, thresholds and routing set; reconcile cached, queued and downstream decisions.
- Execute one ordered plan with immutable identities, concurrency lock, abort criteria and per-step evidence; prevent stale controllers or workers from restoring failed state.
- Run smoke and business/data checks, reconcile in-flight work and side effects, observe stabilization, record final state and impact, and add regression/runbook follow-up without deleting history.

Kubernetes documents revision-aware [rolling updates and rollback](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/); verify data and dependency compatibility beyond the workload-controller revision.
