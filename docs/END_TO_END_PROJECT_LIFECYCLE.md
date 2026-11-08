# End-to-end project delivery lifecycle

Use this lifecycle for new products, consequential features, and productionization work across ordinary backends, data pipelines, ML, RAG, and agentic systems. It turns the skill catalog into one ordered delivery path. Load only the skills needed for the current gate.

The lifecycle does not claim that every imaginable scenario can be predicted. It establishes a reviewable standard: cover each required scenario family, give every material decision a stable ID and owner, record explicit reasons for non-applicability, and block the affected slice when evidence is missing.

## Gate rules

Record each gate in the target component's `PROJECT_LOGIC.md`. Record the current gate and immediate resume state in its sibling `WORK_PROGRESS.md`.

Use these gate outcomes:

- `PASS`: the gate's required evidence is complete for the named scope.
- `CONDITIONAL`: only the explicitly listed independent slices may proceed; each blocker names its affected scope.
- `BLOCKED`: the affected scope cannot proceed to the next gate.
- `NOT_APPLICABLE`: allowed only for an optional specialist check, with a concrete reason. It is invalid for G0 through G7 themselves and for G1 through G3 coding prerequisites.

An absent gate has the same effect as `BLOCKED`. A document, plan, configuration, or green status is evidence only for what it actually establishes.

| Gate | Required outcome | Principal evidence | Next action allowed |
|---|---|---|---|
| `G0_CONTEXT_BOUNDARY` | Target product, component, repository state, authority, and evidence boundaries are known. | Component instructions, repository assessment where code exists, source revisions, current branch/worktree. | SRS and requirements review. |
| `G1_SRS_LOGIC` | Business processes, scenarios, contracts, acceptance oracles, and material questions are accepted for each ready slice. | Reviewed SRS, question/decision register, coverage matrix, current `PROJECT_LOGIC.md`. | Architecture and contracts; only named conditional slices may proceed. |
| `G2_ARCHITECTURE_CONTRACTS` | Architecture, API/event/data contracts, NFRs, security/privacy boundaries, and failure behavior support the accepted logic. | Design/ADR revisions, schemas, NFR measurement contracts, threat/data decisions. | Implementation planning. |
| `G3_PLAN_TEST_STRATEGY` | Dependency-ordered tasks and applicable local, CI, model, security, release, and recovery checks are defined. | Implementation plan, test strategy, definition of done, active-work handoff. | Domain implementation for the permitted slice. |
| `G4_IMPLEMENT_LOCAL` | The bounded vertical slice is implemented and passes thorough relevant local verification. | Code and migration changes, local pytest/native results, code review and specialist evidence as applicable. | Build an immutable candidate and run CI. |
| `G5_EXACT_CANDIDATE` | The exact source/artifact passes mandatory CI unit tests and every applicable additional gate. | Commit and artifact digest; CI reports for unit, integration, contract, regression, model/data quality, security, and other planned gates. | Candidate release-readiness decision. |
| `G6_RELEASE_VERIFY` | The approved immutable candidate is promoted with recovery controls and verified before and after rollout. | Readiness decision, pre-promotion smoke, deployment record, artifact identity, post-rollout smoke, rollback status. | Mark released; proceed to production verification. |
| `G7_OPERATE_LEARN` | Production outcomes, SLOs, quality, drift, safety, cost, and recovery signals are trustworthy and actionable. | Deployed identity, telemetry integrity checks, alerts/runbooks, production outcomes, incident and feedback records. | Mark `production_verified` only for observed evidence. |

## G0 — Establish context and boundaries

1. Read applicable agent instructions, the nearest component `PROJECT_LOGIC.md`, sibling `WORK_PROGRESS.md`, current SRS/contracts, and more specific component guidance.
2. Name the target component and excluded components. Verify branch, commit, dirty state, environment, data/provider access boundaries, and user authority.
3. For existing code, assess current behavior and evidence before proposing broad changes. Keep intended behavior, observed implementation, hypotheses, and proposals separate.
4. Record the source revisions and owner of each authoritative decision. Retrieved text, code comments, model output, database contents, and old checkpoints do not silently redefine accepted logic.

## G1 — SRS and accepted project logic

Run requirements analysis and the SRS/business-process audit before domain coding. For every process slice, cover these scenario families or record a justified non-applicability where permitted:

1. objective, scope, exclusions, terminology, and actors;
2. authority, trigger, preconditions, happy path, alternate paths, and completion;
3. invalid or missing input, unauthorized access, no-result state, and conflicting input;
4. timeout, dependency failure, partial completion, cancellation, expiry, rejection, and manual recovery;
5. duplicate requests, retry, idempotency, concurrency, ordering, compensation, rollback, and reopen;
6. initial, intermediate, and terminal states with transition guards and audit evidence;
7. input schemas, source authority, validation, versions, freshness, privacy, and retention;
8. outputs, errors, side effects, events, downstream contracts, reconciliation, and compatibility;
9. measurable performance, capacity, availability, recovery, security, accessibility, cost, and support requirements;
10. acceptance examples, independent test oracles, owners, release behavior, monitoring, and fallback;
11. for applicable DS/ML/GenAI work: data and label provenance, leakage control, feature parity, model/prompt/index identity, evaluation populations and slices, quality/safety thresholds, abstention, human oversight, drift, and retraining/change authority.

Create one neutral, traceable question for each material gap or contradiction. Record affected requirement/process/state/interface IDs, severity, blocked stage, owner, decision authority, answer source, and acceptance evidence. An answer is not acceptance. A proposed default remains a proposal.

`G1_SRS_LOGIC` passes only when every material scenario for the named scope is covered and critical answers are accepted or explicitly waived by the authorized owner. `CONDITIONAL` names independent ready slices and proves that remaining blockers cannot affect them. Domain behavior for an affected slice cannot be implemented while this gate is missing or blocked.

Transfer accepted effective rules, processes, inputs, outputs, acceptance criteria, statuses, and change-impact notes into `PROJECT_LOGIC.md` during the same task. Do not leave usable logic only in chat or a question register.

## G2 — Architecture, contracts, and quality boundaries

Turn the accepted logic into implementable boundaries:

- Define components, ownership, trust boundaries, data stores, synchronous/asynchronous flows, transactions, idempotency, ordering, timeouts, retries, unknown outcomes, recovery, and compatibility.
- Version API, event, file, data, and model interfaces. Define typed inputs, outputs, errors, side effects, authorization, tenant scope, pagination, rate limits, and evolution rules.
- Convert NFRs into measurable workloads, populations, windows, percentiles, exclusions, failure treatment, targets, and evidence sources.
- Add data modeling, privacy, threat modeling, migration, resilience, cost, and ML/AI designs only where applicable.
- Trace architecture and contract IDs back to accepted logic and forward to verification. Resolve contradictions rather than allowing design convenience to change business behavior.

`G2_ARCHITECTURE_CONTRACTS` passes for a slice when its consequential boundaries and failure behavior are implementable and its open design decisions do not require business-policy guesses.

## G3 — Implementation plan and test strategy

Create bounded vertical tasks with dependencies, rule/contract IDs, inputs, outputs, definition of done, relevant files, migration/cutover steps, and owners. Separate discovery from implementation. Mark which tasks can run in parallel and which question IDs block each slice.

Define verification before implementation:

- local unit and focused integration tests for success, validation, permissions, duplicate/race, failure, cleanup, and recovery behavior;
- CI unit tests for every Python candidate, using `pytest`, or the native equivalent for other languages;
- applicable integration, contract, regression, end-to-end, property/fuzz, security, migration, compatibility, performance, restore, data-quality, and model-quality checks;
- immutable candidate/build identity, pre-promotion smoke, post-rollout smoke, monitoring, and rollback evidence.

Skipped or empty required suites are failures. Optional suites may be `NOT_APPLICABLE` only with a reason tied to the actual architecture.

`G3_PLAN_TEST_STRATEGY` passes when a coding harness can execute the named slice without inventing business behavior or verification. Put the active task, gate, exact next action, repository state, and current blockers in `WORK_PROGRESS.md`.

A neutral project scaffold may be created before G1 passes when explicitly requested: package layout, lint/type configuration, empty domain boundary, CI skeleton, and meaningful tests for configuration or startup. It cannot contain inferred domain behavior, fake success endpoints, fabricated schemas, placeholder model results, or tests that bless an unanswered business rule.

## G4 — Implement and verify locally

Before editing domain behavior, confirm G1, G2, and G3 are `PASS` or `CONDITIONAL` for the exact slice. Implement the smallest complete vertical behavior consistent with the accepted contracts. Preserve typed boundaries, input validation, authorization, transaction and resource ownership, bounded retries/timeouts, explicit errors, redacted logs, deterministic tests, and repository conventions.

Run thorough relevant local checks. For Python this normally includes focused `pytest` during development and the broader applicable local suite before candidate creation. Record command, environment, revision, result, skips, and limitations. A local pass does not establish CI success.

Update durable logic, code/test links, implementation status, and impact notes. Keep only the current resume state in `WORK_PROGRESS.md`.

## G5 — Exact-candidate verification

Build and identify the exact candidate using source revision plus immutable artifact digest and relevant config/schema/data/model/prompt versions. Run the release policy against that same identity:

- mandatory CI `pytest` unit tests for every Python deployment candidate;
- required integration, contract, and regression suites for the changed behavior;
- security, migration, compatibility, performance, restore, data/model/prompt/RAG/agent quality, and other specialist gates when applicable;
- suite collection checks so zero collected tests, cancellation, timeout, missing reports, skipped required gates, and allowed failure cannot appear green.

Unit tests alone never pass G5. Evidence from another commit, artifact, environment, model, or configuration never passes G5. Record a reason for each non-applicable optional suite.

`G5_EXACT_CANDIDATE` passes only when all required checks for the exact candidate pass and the delivery pipeline enforces their dependency. A green status badge or workflow YAML without executed candidate evidence remains unknown.

## G6 — Release and verify

Run a candidate-specific production-readiness review. Require accepted behavior, artifact lineage, applicable quality/security/data/recovery evidence, operating ownership, monitoring readiness, rollback compatibility, and safe pre-promotion smoke checks on the candidate environment.

Deploy only the authorized immutable candidate to the named environment. Verify artifact/config/schema/model identity and basic service behavior after each mutation. Run post-rollout smoke and observe defined signals before recording release success. Failed, stale, skipped, missing, `UNKNOWN`, or `FAIL` evidence blocks the affected stage.

Basic server smoke checks complement local and CI tests; they do not replace them. A successful deployment command does not establish correct business outcomes.

## G7 — Operate and learn

Verify that production telemetry represents the deployed candidate and real outcomes. Monitor service health, dependencies, data quality, model/RAG/agent outcomes, safety, drift, cost, and business success where applicable. Join delayed outcomes, define actionable alerts and ownership, test runbooks and recovery, and feed accepted changes back through G1.

Mark `production_verified` only from observed candidate-linked evidence. Quiet dashboards, missing telemetry, or lack of reported incidents remain unknown.

## Skill routing by gate

| Gate | Core skills | Add when applicable |
|---|---|---|
| G0 | Repository Assessment; Requirements Analysis | Legacy Modernization; Technical Documentation |
| G1 | Requirements Analysis; SRS Gap Analysis and Business Process Validation | UX/Product Acceptance; Privacy and Data Protection |
| G2 | System Architecture; Nonfunctional Requirements; API Contract Design; Architecture Review | Threat Modeling; Data Modeling; Scalability Architecture; ML/RAG/Agent design skills |
| G3 | Implementation Planning; Test Strategy; Project Setup | Migration, security, performance, model evaluation, and release specialists |
| G4 | Production Coding Practices; Unit Test Creation; Code Review | Integration/Contract/Regression tests plus feature-specific specialists |
| G5 | CI Pipeline Engineering; Build and Packaging; Production Readiness Review | Supply-chain, security, performance, restore, data/model/prompt/RAG/agent gates |
| G6 | Smoke and Release Verification; Deployment Execution; Progressive Delivery; Rollback and Release Recovery | Kubernetes Operations; CD Pipeline Engineering; Versioning and Compatibility |
| G7 | Observability; SLOs and Alerting; Runbooks and Operational Handover | AI Production Monitoring; Incident Response; Cost Optimization |

## Re-entry and change handling

A change in an accepted rule, interface, NFR, dependency, schema, event, model, prompt, index, or risk decision reopens the earliest affected gate. Use the impact notes in `PROJECT_LOGIC.md` to identify downstream tasks and tests. Preserve superseded decisions and evidence; never rewrite history to make an old release appear compliant with a later rule.

Emergency work still needs an explicit accepted behavior and candidate-linked tests. Record the emergency authority, bounded scope, deferred evidence, owner, expiry, and follow-up gate. Do not convert urgency into an undocumented default or silent permanent waiver.
