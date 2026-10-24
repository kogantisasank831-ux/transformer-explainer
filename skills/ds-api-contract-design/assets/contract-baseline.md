# Interface contracts: [project]

- Baseline: [logic/SRS/architecture/NFR/schema revisions and consumers]
- Current versus proposed behavior: [source evidence and compatibility constraints]

| Contract ID / rule IDs | Operation / caller / ownership | Input and validation | Success/output/postconditions | Errors/retry/cancel/unknown outcome | Side effects and versioning |
|---|---|---|---|---|---|
| [ID] | [Authority] | [Types, limits, units; pending fields] | [Durability/completion distinction] | [Observable semantics] | [Scope] |

## Schema and examples

[Complete authoritative schema or clearly labeled fragment; valid, invalid and boundary examples without sensitive data. Include relevant job/event/model/tool contracts.]

## Compatibility and verification

| Contract IDs | Old/new consumer behavior and migration | Verification cases and environment | Planned/executed evidence |
|---|---|---|---|
| [IDs] | [Breakage and coexistence] | [Positive/negative/concurrency/recovery] | [Actual state] |

## Decisions and handoff

- Open policy questions and blocked work: [IDs, options, owner or unknown]
- Independent implementation that can proceed: [scope]
- Authoritative files and logic/schema revisions to read: [paths/IDs]
- Local, required CI pytest and server smoke coverage: [candidate/profile; actual enforcement status]
- Actual schema validation and persistence: [evidence or pending]
