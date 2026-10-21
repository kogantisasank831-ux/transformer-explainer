# Architecture tradeoffs, evidence, and readiness

## Compare meaningful alternatives

For consequential choices, compare the simplest viable option with another plausible approach. Base the comparison on constraints, not a preference for a pattern or vendor.

| Choice | Questions that change the answer |
|---|---|
| Monolith/modules versus services | Is independent release/scaling/security ownership needed? Can the team operate the added network and failure boundaries? |
| Synchronous versus jobs | What is the completion deadline, duration distribution, client expectation, retry/cancellation behavior, and resource occupancy? |
| Single store versus specialized stores | Which access/consistency/search requirements justify extra state, synchronization, migration, and recovery obligations? |
| Embedded model versus inference service | Do resource lifecycles, artifact size/load time, request contention, deployment cadence, or isolation justify separation? |
| Hosted versus self-hosted inference | What are the data-egress constraints, quality targets, workload distribution, availability needs, hardware evidence, and operating skills? |
| Cache versus recompute | Is reuse material, are cache entries correctly authorized/versioned, and what stale behavior is acceptable? |

Record the option, constraint/rule evidence, benefit, operational and failure cost, residual uncertainty, selected/proposed state, and conditions that should trigger reconsideration. Do not invent numerical weights or force multiple options for a routine local implementation choice.

## Reason about failure and validity

For each critical journey inspect identity/permission, validation, state changes, dependencies, acknowledgment, and observable outcome. Ask where a process can stop, retry, race, or return an unknown result. Map each failure to its owner, retry/reconciliation path, user-visible state, and verification case.

For example, persisting a job and dispatching work independently introduces a gap; transactionally stored dispatch intent plus a retrying dispatcher is one candidate mechanism. It still needs consumer deduplication, bounded retries, failure visibility, and external-side-effect reconciliation. Select such patterns only when they address an actual invariant.

For ML, distinguish software validity (schema, loading, output handling), scientific validity (data, split, metric evidence), and product utility (business action/outcome). A design that satisfies one dimension cannot establish the others.

## Evidence discipline

- Mark confirmed requirements, authorized technical decisions, proposed assumptions, estimates, and unresolved business policy separately.
- Cite supplied logic/SRS/repository revisions and direct evidence. Check current primary documentation when a version-specific capability, security control, formal obligation, provider price or hardware limit affects the design.
- Treat existing tests, diagrams and configuration as inspected artifacts unless actual execution/results are available. Document verification scope and failures honestly.
- Do not derive hardware requirements, requests per second, or a latency guarantee from a user count. If using a workload/resource model, state units, assumptions, stability bounds, and the measurement needed to validate it.
- Do not claim blanket ISO, OWASP, NIST, or other compliance because a checklist or diagram exists. Apply project-required controls and collect evidence for the actual obligation.

## Keep the design usable by coding agents

- Preserve business rule IDs; assign stable component/contract/decision IDs only when helpful. Trace requirements to design mechanisms and planned validation.
- Keep current architecture in its authoritative document and summarize/link it in PROJECT_LOGIC.md. Keep significant rationale in ADRs; do not duplicate entire contracts across files.
- Do not demand user approval for every reversible technical detail. Respect the project's governance for consequential decisions and keep unsupplied business rules unresolved.
- Separate implementation mechanisms from observable policy. A lock/index/outbox can be an authorized technical choice; cancellation authority, fixed versus sliding expiry, payload equivalence, post-expiry behavior, retention, and user-visible fallback require source-backed rules or explicitly pending alternatives. Do not hide those choices beneath a generic proposed-design label.
- Hand off the applicable logic/design revisions, selected boundaries, interfaces, dependency direction, failure semantics, constraints and test cases. Identify exact blocked work and independent tasks.
- If key evidence is unavailable, propose a focused feasibility experiment with a question and exit criterion; do not fabricate its outcome or execute it outside task scope.

## Reference anchors

Use these primary sources as guidance when needed, without treating them as mandatory architecture templates:

- [C4 model](https://c4model.com/): system context and component/deployment views at appropriate levels.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/): load, configuration, monitoring, reliability and releases.
- [OWASP ASVS](https://owasp.org/projects/asvs): security requirements and verification.
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html): leakage and preprocessing considerations.
