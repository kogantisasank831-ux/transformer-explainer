# Kubernetes operations record

- Request, rule IDs, owner/actor, kubeconfig/context, cluster, namespace, identity and authority:
- Resource kind/name/selectors, controller and declarative owner, current revision/generation and requested outcome:

| Time / object | Observation or command | Before / after identity and condition | Application/data evidence | Decision / recovery |
|---|---|---|---|---|

## Dependency and safety boundary

Record scheduling/resources, Services/endpoints/routes, DNS/network, storage, probes, PDBs, node or GPU state, jobs/checkpoints, logs/events handling, temporary privileged access, dry-run/diff and source-of-truth reconciliation.

## Closure

List effective-state and smoke results, unexpected restarts/evictions, cleanup, failed or inconclusive checks, residual risks, monitoring owner, runbook or declarative updates, and next actions.
