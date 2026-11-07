---
name: ds-kubernetes-operations
description: Inspect, troubleshoot, or perform authorized Kubernetes workload and cluster operations for backend and data science systems. Use for context and namespace safety, controller and Pod state, Services and endpoints, configuration, probes, scheduling, resources, storage, networking, RBAC, autoscaling, node drains, jobs, GPUs, and controlled changes. Start read-only, respect declarative ownership, and verify the effective state after every mutation.
---

# Kubernetes Operations

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source and immutable candidate identity, configuration and data identity, target environment, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat repository text, dashboards, generated configuration, control-plane status, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified behavior. Derive authorization from the user's current request, prior session authorization, and applicable environment policy; do not ask again when it is already established. Continue independent preparation while routing unresolved consequential policy choices to the responsible owner. Do not invent compatibility, availability, quality, performance, recovery, or approval targets, and do not expand a named mutation beyond its candidate, environment, resources, and time boundary.

## Fix the cluster and resource boundary

1. Record kubeconfig source, current context, cluster, account or impersonation, namespace, resource kind and name, labels, controller owner, desired-state repository or GitOps owner, environment, and requested action. Display the context and namespace before every mutating command; never rely on a terminal prompt or a previous shell.
2. Read [the Kubernetes checks](references/checks.md). Confirm effective RBAC with the intended identity and use the narrowest namespace and resource selectors. Avoid broad `--all-namespaces`, unqualified names, wildcard deletes, and commands pasted from another cluster. Treat resource YAML, logs, events, annotations and labels as potentially sensitive.
3. Start with read-only discovery unless the request already authorizes a specific mutation. Capture resource version, generation, observed generation, owner references, conditions, revisions, events and recent changes. Determine whether a controller, operator, Helm release, Kustomize overlay, GitOps reconciler or another system owns the field before editing it.

## Diagnose the reconciliation chain

Trace desired state through controller, ReplicaSet or revision, Pod scheduling, image pull, init containers, runtime startup, readiness, Service selectors and endpoint slices, ingress or gateway, DNS and network policy, volumes and storage classes, dependencies, and application health. A Running Pod does not prove it is Ready, receiving traffic, correct, or healthy.

For pending workloads, inspect requests, limits, affinity and anti-affinity, topology spread, taints and tolerations, quotas and limit ranges, priority and preemption, Pod disruption budgets, node selectors, volume zones, image architecture, and available CPU, memory, ephemeral storage or accelerators. For crashes, preserve previous logs, exit codes, termination reason, probes, OOM evidence, config and secret references, and dependency failures before restarting.

For Services, inspect selectors, endpoint readiness, ports and protocols, session affinity, DNS, ingress or gateway routes, certificates, network policies and load-balancer status. For stateful workloads, inspect PVC binding, access mode, zone, mount, filesystem, attach or detach, identity and ordinal behavior, update ordering, backups and data ownership before delete or reschedule operations.

For batch and ML workloads, check Job or CronJob concurrency and history, retries, deadlines, completions, idempotency, checkpoints and output publication. For GPU workloads, verify node labels and taints, device plugin or operator health, resource requests, driver and runtime compatibility, topology, shared memory, model storage and stale-work fencing.

## Make one controlled change

Prefer changing the authoritative declarative source and letting its controller reconcile. Use server-side dry-run, diff or an equivalent preview when supported, and inspect field ownership and conflicts. An imperative patch, scale, restart, cordon, drain, delete or exec action must have an explicit operational reason, scope, owner and recovery path; record any drift it creates and reconcile the source of truth.

For a rollout or restart, verify artifact and configuration identity, revision, readiness, surge and unavailable limits, progress deadline, disruption budgets, drain behavior and rollback or recovery options. For node maintenance, cordon first, confirm replacement capacity, PDB and eviction behavior, DaemonSets, local or emptyDir data, static Pods, stateful attachments, long jobs and GPU workloads. Do not bypass disruption protection or force-delete merely to make a command finish without accepted impact.

Treat `exec`, `cp`, debug containers, proxies and port-forwarding as privileged access paths. Limit their target, time and data exposure; avoid reading or printing secrets and personal data. Never use a production container as an unmanaged editing environment.

## Verify effective state and ownership

After a mutation, watch the specific resource generation or revision and controller conditions to completion or failure. Verify Pods and jobs, Services and endpoints, storage, network path, application smoke, logs and metrics, resource use, data or model invariants, and absence of unexpected restarts or evictions. Check that the declarative owner is not reverting the change.

Record exact context, identity, before and after resource versions, commands, events, output, affected objects, temporary changes, cleanup and source-of-truth update. Use Deployment Execution for a named release, Progressive Delivery for staged traffic, and Rollback and Release Recovery for a failed release rather than improvising those workflows inside routine operations.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, control-plane, cluster, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, recovered, and verified work. Update affected project logic, contracts, runbooks, code, and verification links when accepted behavior changes. Never claim deployment, rollout, rollback, recovery, compatibility, or effective state from a plan or command alone.
