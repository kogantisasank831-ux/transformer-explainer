# Deployment execution checks

- Bind service, target environment/context, immutable artifact digest, source revision, config/secrets, infrastructure, schema/data/model identities, owner, authority, window, and deployment lock.
- Confirm exact-candidate CI gates, artifact policy, access, capacity/quotas, dependencies, certificates, backups/recovery, observability, and previous known-good compatibility.
- Preview current versus desired state in the exact target. Review deletes, replacements, permissions/exposure, migrations, jobs, traffic, model/index pointers, and data effects.
- Use the approved pipeline or command. Record actor, timestamp, execution ID, commands, outputs, and each gated step; never rebuild or substitute the candidate.
- Observe rollout identity and desired/scheduled/ready/available/serving/failed state plus errors, latency, queues, resources, dependencies, invariants, security, and applicable model quality.
- Pause or abort on failed gates, missing telemetry, identity mismatch, stall, integrity uncertainty, or boundary escape. Preserve evidence and execute the accepted recovery path.
- Run server smoke and exact-target post-rollout checks, observe stabilization, reconcile endpoints/jobs/data/model pointers, update history, and release the lock only after closure.

For Kubernetes targets, the official [`kubectl rollout status`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/) documentation describes revision-aware rollout observation; use the selected platform's authoritative equivalent.
