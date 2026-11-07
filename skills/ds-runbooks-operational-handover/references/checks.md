# Runbook and operational handover checks

- Name the concrete trigger, operator, target/environment, owner, versions, prerequisites, access, dependencies, risk, expected duration and prohibited conditions.
- Start with identity/context and read-only evidence. Use copy-safe commands, explicit placeholders, expected output, interpretation and visible errors; never embed secrets.
- Give each branch an observable decision rule. Bound retries, duration, concurrency and scope; state abort, escalation and authorization points.
- Pair each mutation with preconditions, exact target, checkpoint, verification, failure path, rollback or roll-forward and cleanup. State idempotency and partial-run detection.
- Cover ordinary services and jobs; add pipeline, feature, model, index, accelerator, provider, quality and safety steps only when applicable.
- Validate with a cold reader and risk-based exercise. Track owner, compatible versions, last review/exercise and change or incident triggers for refresh.
- Handover inventory includes purpose, dependencies, access, SLOs/alerts, release/recovery, backup, recurring work, capacity/cost, risks, vendors and data/model lineage where relevant.
- Prove receiving-team competence through pairing, shadow/reverse-shadow and representative scenarios; require accountable acceptance and preserve blocking gaps.

Google SRE's [Being On-Call](https://sre.google/sre-book/being-on-call/) and [Managing Incidents](https://sre.google/sre-book/managing-incidents/) chapters provide useful primary operational context. Apply the target organization's ownership, access and change policies.
