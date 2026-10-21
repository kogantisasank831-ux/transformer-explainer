# Repository assessment: [component]

Replace placeholders with evidence. Compress for small tasks; mark irrelevant sections with reasons. Keep secrets and personal records out of excerpts.

## Scope and revision

- Objective and named next activity: [values]
- Repository/component, commit/ref/snapshot, working-tree state, date if known: [values]
- Logic/SRS/contract revisions and acceptance state: [sources or unavailable]
- Inspected paths and sample selection: [scope]
- Exclusions/inaccessible paths and constraints: [limitations]
- Execution mode and authorized mutations: [static / bounded checks; changes or none]

## Component map and behavior

| Component / entry point | Responsibility and dependencies | Contract/data/model/side-effect flow | Evidence path/symbol and level |
|---|---|---|---|
| [Component] | [Observed behavior] | [Flow, including relevant failure path] | [Evidence] |

Describe one representative critical journey and a relevant failure/duplicate/concurrency journey. Mark where unavailable code prevents tracing. Distinguish production paths from experiments and examples.

## Accepted logic versus implementation

| Rule/requirement ID and revision | Intended accepted behavior | Observed behavior and evidence | Consistent / conflict / unknown | Decision or follow-up |
|---|---|---|---|---|
| [ID or missing logic] | [Source] | [Path/symbol] | [Status] | [Bounded action] |

## Evidence and coverage

| Area | Observed / verified / hypothesis / unknown / not applicable | Evidence, actual result, and limitations |
|---|---|---|
| Architecture and contracts | [Status] | [Scope] |
| Coding practices and dependency/configuration management | [Status] | [Scope] |
| Tests and automation | [Status] | [Scope] |
| Backend permissions, persistence, workers, and side effects | [Status] | [Scope] |
| Data, evaluation validity, and reproducibility | [Status] | [Scope or no-ML reason] |
| RAG/LLM/agent boundaries | [Status] | [Scope or not-applicable reason] |
| Security/privacy indicators | [Status] | [Scope; not a complete security audit] |
| Performance, reliability, deployment, and operations | [Status] | [Static versus measured evidence] |

## Findings and ordered actions

| Finding ID / category | Severity, confidence, and assumptions | Evidence / affected rule | Practical impact | Action and validation | Dependency / owner / blocked activity |
|---|---|---|---|---|---|
| [F-ID] | [Values] | [Path/symbol, evidence level] | [Supported consequence] | [Bounded task and completion evidence] | [Scope; owner or unassigned] |

Include existing strengths worth preserving. Separate verified defects, hypotheses, and unanswered business decisions; do not turn not-assessed areas into fabricated defects.

## Checks and readiness

| Check/command and environment | Executed or not run | Outcome and evidence / reason not run |
|---|---|---|
| [Exact command or planned inspection] | [Status] | [Actual result or limitation] |

- Readiness for the named next activity: [ready / conditionally ready / blocked with evidence]
- Highest-impact open questions or missing evidence: [prioritized]
- Independent work that can proceed: [scope]
- Coding handoff: [logic revision, accepted rule IDs, relevant files/symbols, blockers, and verification cases]
- Specialist follow-up: [task and available skill if verified; otherwise describe the task without claiming installation]
- Mutations and publication: [actual changes or none; requested report location if applicable]
