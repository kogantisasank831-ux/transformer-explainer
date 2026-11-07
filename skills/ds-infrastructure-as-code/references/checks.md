# Infrastructure as code checks

- Identify accounts/projects, regions/environments, current resources, owners, state backend, network/identity/data boundaries, availability/recovery, quotas, and cost constraints.
- Use the existing IaC tool with pinned compatible providers/modules. Define root and reusable module boundaries, inputs/outputs, addresses, naming/tags, and isolated environment composition.
- Protect remote state with encryption, least privilege, audit, versioning/backups, and locking. Keep state, saved plans, credentials, and secret values out of source and ordinary artifacts.
- Import or move resources only with reviewed configuration and exact remote/resource addresses. Confirm no duplicate creation, orphaning, or untracked dependencies.
- Generate a plan from exact revision, lockfile, variables, backend/workspace, and identity. Review creates, deletes, replacements, permissions, exposure, downtime, data, quotas, unknowns, and cost.
- Validate and format, then run native module, policy, and security checks. For DS/ML, cover storage/locality, GPU quota/runtime, artifact stores, serving/training isolation, scaling, and idle cost where applicable.
- Separate plan, authorized apply, and effective-state verification. Detect and reconcile drift explicitly; treat force unlock, state surgery, destroy, and production apply as controlled operations.

OpenTofu documents the distinction between [plan and apply](https://opentofu.org/docs/cli/run/) and the need for supported [state locking](https://opentofu.org/docs/language/state/locking/); use equivalent official guidance for the selected IaC engine.
