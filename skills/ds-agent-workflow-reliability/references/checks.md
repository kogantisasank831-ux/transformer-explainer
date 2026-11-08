# Agent workflow reliability checks

- Define goal, allowed/forbidden actions, trusted identity/policy, terminal states, side effects, budgets, cancellation/escalation and owners; justify model-driven choice.
- Version an explicit typed state graph with transition guards, persisted/ephemeral state, retry/compensation and exact prompt/model/tool/policy/memory/checkpoint identities.
- Keep authentication, authorization, semantic validation and effect commit in trusted code. A model decision cannot create authority.
- Use narrow typed tools with least privilege and explicit errors; bind approval to exact consequential arguments and expiry.
- Allocate operation keys before effects, persist intent/attempt/result and reconcile on retry/resume. There is no generic exactly-once guarantee.
- Validate and bound untrusted tool results; distinguish error from empty success and redact sensitive context and telemetry.
- Checkpoint compatible authoritative state; reconcile in-flight work before resume and expose partial effects and compensation.
- Enforce step/call/retry/token/cost/time budgets, repeated-action detection and propagated cancellation with typed terminal outcomes.
- Scope memory and handoffs by identity, purpose and lifetime; preserve provenance, correction/deletion and explicit multi-agent ownership/conflict rules.
- Evaluate terminal state and side effects plus safe trajectory, crashes, duplicates, stale checkpoints, denial, cancellation, loops and concurrency; never blindly replay writes.
- Trace workflow/model/tool/backend operations and operate pause, reconcile, disable, rollback and incident paths for the exact candidate.

OpenTelemetry's [semantic conventions](https://opentelemetry.io/docs/specs/semconv/) provide a common vocabulary for traces and metrics, including evolving GenAI conventions. Pin the convention version and add workflow/operation identity without recording sensitive prompt or tool content by default.
