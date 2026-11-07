# Kubernetes operations checks

- Record kubeconfig/context, cluster, identity, namespace, resource kind/name/selectors, controller owner, desired-state source, environment and authorized action before mutation.
- Start read-only. Capture generation/observed generation, resource version, owner references, conditions, revisions, events and changes; verify effective RBAC and field ownership.
- Trace controller to Pod, image/init/startup/readiness, Service/endpoints, route/DNS/network, dependencies and application health. Running is not Ready or correct.
- Check requests/limits, quotas, scheduling, topology, taints, PDBs, storage and architecture; preserve previous logs, exit/OOM/probe evidence before restart or deletion.
- For Jobs/ML/GPU, verify retry/deadline/idempotency/checkpoint/output, device plugin, driver/runtime, resources, topology, model storage and stale-worker fencing.
- Prefer declarative changes with diff or server dry-run. Bound patches, restarts, drains, deletes, exec/debug access and force options; record recovery and reconcile drift.
- Watch the exact revision to completion and verify endpoints, storage/network, smoke, metrics, invariants and source-of-truth ownership; record before/after evidence and temporary cleanup.

Use current official [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and [`kubectl` reference](https://kubernetes.io/docs/reference/kubectl/) semantics for the deployed cluster version.
