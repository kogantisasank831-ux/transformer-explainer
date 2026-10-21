# Evidence, triage, and scope

## Evidence levels

| Level | Meaning and reporting rule |
|---|---|
| Observed | Directly read code, configuration, test, or documentation at a recorded revision. State the exact path/symbol and what it establishes. |
| Verified | Executed a bounded check or observed an authoritative result for the stated revision/environment. Record command/result and practical limits. |
| Hypothesis | Inferred a plausible issue from incomplete evidence. Explain missing assumptions and the check needed to confirm it. |
| Unknown / not assessed | Access, data, scope, tooling, or safe execution did not support a conclusion. This is not a demonstrated defect. |

An absent-control claim is an observed, scope-qualified conclusion only after inspecting relevant entry points, shared enforcement layers, configuration, and relevant tests. Otherwise say not observed in inspected scope. A README claim is observed documentation, not verified implementation. A current behavior can be observed while business acceptability remains unresolved.

## Finding schema and severity

Record: F-ID; affected component/requirement/rule; category; evidence and level; confidence and assumptions; impact/exposure; severity; recommended action; validation; dependencies/owner if known.

| Severity | Use when supported by evidence and context |
|---|---|
| Critical | An established path can cause severe unauthorized exposure, destructive side effects, or fundamental invalidity with major consequences. Explain scope and preconditions; use a hypothesis instead when these are unknown. |
| High | A demonstrated correctness, confidentiality, integrity, availability, or scientific-validity gap materially threatens an agreed outcome. |
| Medium | A bounded reliability, maintainability, reproducibility, or verification gap has a credible practical impact. |
| Low | A limited-impact improvement is useful but does not materially block the named next activity. |

Keep confidence separate from severity. Mark speculative severity provisional and state the condition that would change it. Do not classify unknown production authentication as a verified critical vulnerability or an unrun test as a failed test.

Use blocker status separately: identify the named activity and exact requirement/dependency blocked. A high-risk path may block a release while allowing isolated refactoring or investigation. Do not inflate all findings to launch blockers.

## Prioritization and handoff

- Prefer concrete impact, reachable paths, accepted-rule violations, and evidence strength over framework fashion or arbitrary line/coverage counts.
- Group duplicate symptoms under their underlying cause. Keep a concise ordered backlog with prerequisites, bounded actions, owner or unassigned, and proof of completion.
- Record healthy existing controls and their limits so later work preserves them. Do not manufacture findings to fill every category.
- Describe uncertainty from samples, missing submodules/files, ignored data, unrun checks, and stale documents. Do not generalize a sample inspection to every repository component.
- Link confirmed code-to-logic discrepancies to the current rule revision. Propose business questions for requirements analysis; preserve unaccepted answers and planned checks explicitly.

## Example distinctions

- A test function exists: observed test code. Its assertion is relevant: inspected test quality. A matching test command passed locally: verified only for that execution. A pipeline file invokes it: observed CI configuration, not current CI success.
- A route lacks an inline permission check: inspect middleware/service/storage enforcement before judging. If those paths are unavailable, report authorization unknown rather than absent.
- A transformation fits on all rows before splitting: observed leakage path if the full code flow supports that conclusion. Report model-quality inflation as unmeasured unless demonstrated with a valid comparison.
- A synchronous client is invoked from an async path: observe potential blocking and relevant wrapper/executor context. Do not claim a particular latency loss or user limit without measurement.
