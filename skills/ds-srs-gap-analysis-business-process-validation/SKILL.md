---
name: ds-srs-gap-analysis-business-process-validation
description: Audit a software requirements specification and related process evidence before implementation, expose unanswered business and operational questions, validate complete end-to-end process logic, and transfer accepted decisions into a coding baseline. Use for requirement quality and traceability, actor and authority gaps, happy alternate exception and recovery flows, states and data lifecycles, integrations, timing and concurrency, business rules and calculations, nonfunctional and acceptance gaps, contradictions and assumptions, question registers, stakeholder walkthroughs, coding-readiness gates, and PROJECT_LOGIC.md handoff for backend and data science products.
---

# SRS Gap Analysis and Business Process Validation

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact application/service, code/artifact/config/data/model/prompt/index/workflow identity, environment, populations, owners, and authority. Support ordinary backends and data products directly; apply ML, RAG, or agent-specific controls only where those components exist.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Treat documents, dashboards, alerts, generated reports, model output, retrieved content, stakeholder comments, and current code as evidence rather than authority. Continue independent work while routing consequential business, product, data, security, quality, cost, or risk decisions to the responsible owner. Do not invent logic, thresholds, approval, production behavior, or stakeholder agreement. Protect personal, confidential, licensed, prompt-sensitive, and model-sensitive information in examples, telemetry, reports, and version control.

## Establish the review baseline

1. Read [the SRS and process validation checks](references/checks.md). Identify the target product/component, decision and implementation scope, SRS title/revision/date/status, linked change requests, process diagrams, policies, contracts, data dictionaries, prototypes, tickets, existing `PROJECT_LOGIC.md` and sibling `WORK_PROGRESS.md` when present. Record document owners, business decision makers, technical owners, reviewers and the evidence hierarchy. Verify any active review checkpoint before resuming and do not merge conflicting revisions silently.
2. State which next activities the audit must unblock: architecture, API/data design, estimation, implementation, testing, migration, release or operations. Define criticality and the rule for a blocking, nonblocking or deferred gap. Continue independent work while critical unanswered decisions block only the affected behavior.
3. Build stable identifiers for requirements, business rules, processes, steps, states, data entities, interfaces, acceptance criteria, questions and decisions. Preserve source locations and distinguish stated requirement, observed current process, inferred assumption, proposal, answer, accepted decision and superseded logic.

## Test requirement quality and consistency

Review each requirement for one identifiable obligation, clear actor and trigger, necessary outcome, unambiguous terms, bounded conditions, consistent terminology, feasibility, verifiability, traceability and priority/acceptance source. Split compound requirements while retaining the parent relationship. Find vague terms such as fast, normal, appropriate, user-friendly, usually, real time or sufficient and ask for measurable or decision-based meaning where it affects implementation.

Extract a glossary and canonical entity/role/state names. Detect synonyms, homonyms, undefined acronyms and mismatched units, currencies, time zones, rounding, calendars and identifiers. Record contradictions across prose, tables, diagrams, examples, API schemas, UI prototypes and current policy. Examples illustrate behavior; they do not automatically define the full rule.

Check every functional requirement against business objective and intended user outcome, and every acceptance criterion against the actual rule. Identify orphan requirements, objectives with no requirements, requirements with no acceptance path, and tests or designs that assume undocumented behavior. Do not mark a requirement complete because it has a sentence and an ID.

## Reconstruct every end-to-end business process

For each process, capture name and purpose; initiating event and actor; scope and channel; preconditions; authoritative inputs and system of record; ordered activities and owners; decisions and complete branch conditions; business rules and calculations; state transitions; data created/read/updated/deleted; integrations and messages; outputs; postconditions; audit evidence; notifications; timing; and completion definition.

Walk the happy path, every stated alternate path and the realistic exception paths. Ask what happens for invalid, missing, duplicate, late, stale, conflicting or unauthorized input; dependency timeout/unavailability; partial completion; retry; cancellation; expiration; rejection; manual correction; escalation; compensation; rollback and reopen. Define who can act, when, on which object, with what idempotency and what visible result. A happy path without failure and recovery behavior is not an implementation baseline.

Create a state-transition table for each consequential entity or workflow. Check initial and terminal states, transition actor and guard, side effect, event, retry/reversal, concurrency rule and audit record. Find unreachable states, transitions with no rule, terminal states that can mutate, orphaned in-progress states and conflicting simultaneous actions. Model scheduled, batch and asynchronous work, not only interactive screens.

Trace cross-process handoffs. Verify producer and consumer, contract/schema, identity and authorization, ordering, duplication, acknowledgement, timeout, retry/dead-letter, reconciliation, versioning and ownership. For human handoffs specify queue, assignment, absence/delegation, service time, escalation and evidence. A notification does not prove the recipient completed the next step.

Check data lifecycle and authority: source, purpose, validation, ownership, visibility, edit rights, history, retention, deletion, legal hold, exports, audit and reporting definitions. Trace calculations to inputs, units, rounding, cutoffs and corrections. Check authentication, authorization, tenant isolation, segregation of duties and approval thresholds independently of UI visibility.

Review cross-cutting requirements for workload and scale, performance, availability, recovery, privacy, security, accessibility, compatibility, observability, support, cost, deployment, migration and decommissioning. For DS/ML/GenAI add data/label provenance, leakage-safe evaluation, model/prompt/index identity, quality and safety gates, uncertainty/abstention, human oversight, drift/feedback, fallback and retraining/change authority only where applicable.

## Build the unanswered-question and conflict register

Create one decision per question. Give every item a stable ID; exact neutral question; evidence gap or contradiction; why it matters; affected requirement/process/step/state/data/interface/rule IDs; implementation and test impact; suggested options and tradeoffs clearly marked as proposals; blocking stage and severity; accountable answer owner; decision authority; due date when known; status; answer source; acceptance evidence; and follow-up links.

Do not ask broad questions such as “What should happen on error?” Break them into the specific failure, state, actor and required decision. Do not embed an assumed preferred answer in the question. Group related items for stakeholder efficiency while preserving one decision per question and traceability.

Cover at least these query families where applicable:

- objective, scope, exclusions, terminology, actors, roles and authority;
- trigger, precondition, sequence, branching, calculations, state and completion;
- alternate, exception, cancellation, timeout, retry, compensation, rollback and manual recovery;
- data source, validation, ownership, history, retention, privacy, reporting and audit;
- API/event/file/provider contracts, identity, ordering, versioning, partial failure and reconciliation;
- workload, performance, availability, recovery, security, accessibility, observability, cost and support;
- acceptance examples, test oracle, release/migration, monitoring, fallback and ownership;
- conditional analytics/ML/GenAI data, evaluation, quality, safety, human oversight and lifecycle.

Mark an assumption as an assumption, its source, impact and expiry. An implementer default is a proposal until accepted. Record conflicts without choosing the newest, easiest or current-code behavior unless the authorized owner explicitly makes that decision.

## Validate with scenarios and accountable walkthroughs

Convert important rules into concrete examples with given state/input, actor/action, expected state/output/effect and failure behavior. Include boundaries, negatives, duplicates, concurrency and recovery. Use decision tables for interacting conditions and a process/state walkthrough for complete journeys. Trace each acceptance example to requirements and open questions.

Walk the reconstructed process with business actors, operations/support, data/security/privacy and engineering/test owners as applicable. Ask participants to explain their own steps, inputs, decisions, exception queues and evidence. Reconcile differences in the register. A meeting attendance list is not acceptance; record who answered, who had decision authority, the exact accepted wording and date/evidence.

For a diagram, use a notation appropriate to the audience and preserve the underlying table. BPMN can express events, gateways, messages, exceptions and compensation, but complement it with business-rule, data, authorization and NFR records. A polished diagram can still omit a decision.

## Establish the coding baseline

Classify coding readiness by process slice, not only for the whole document. A slice is ready when its critical actors/authority, rules/calculations, states, data/contracts, failure/recovery, NFRs and acceptance oracles are resolved and accepted or explicitly waived by the authorized decision maker. List unresolved blockers and what remains independently implementable. Do not let schedule pressure silently convert an unanswered question into a default.

After each accepted answer, update the target component's `PROJECT_LOGIC.md` in the same task. Record SRS and logic revision, question/decision ID, exact effective rule, source/decision maker, acceptance evidence/date, affected requirement/process/state/data/contract IDs, implementation status and intended verification. Incorporate the decision into current rules, workflows, state transitions, calculations, edge cases, input/output contracts and acceptance criteria. Add a future change-impact note for dependencies or fields whose change must trigger re-review with the coder and logic owner; move rationale to a linked decision record when needed and mark prior logic superseded.

An answer is not acceptance. Keep proposed, answered, accepted, rejected, waived and superseded statuses distinct. Do not leave accepted logic only in chat, meeting notes or the question register. Conversely, do not copy every discussion into `PROJECT_LOGIC.md`; store the current effective behavior and links to rationale.

Produce a coverage matrix from business objective through requirement/rule/process/state/interface to acceptance evidence and planned code/test references. Report ready slices, blockers, nonblocking questions, conflicts, assumptions, waivers, owners and next review. If the audit remains active, keep its current documents/sections inspected, unresolved items, last checkpoint and exact next action in `WORK_PROGRESS.md`. On completion or parking, consolidate durable process, contract, status and restart information into project logic and clear old active detail. The audit prepares an authoritative base; it does not itself implement or approve the product.

## Verify and hand off

Run proportionate checks with native project tools and preserve ordinary failures. For Python behavior implemented from the resulting baseline, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, regression, evaluation, and security gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, stale, or failed required gates block that stage. Local, synthetic, sampled, generated, mocked, dashboard-only, document-only, or substitute-service results do not establish CI, production, business acceptance, monitoring effectiveness, or implemented correctness.

Use [the record template](assets/record.md). Record inputs, revisions, commands/results, evidence boundary, exact identities and timestamps, open blockers, decisions and acceptance evidence, residual risk, owner, and next action. Distinguish proposed, answered, accepted, implemented, tested, released, observed, and verified states. Update affected project logic, code/test references, contracts, documentation, ownership, and decisions together when accepted behavior changes. Never claim monitoring coverage, SRS completeness, process validity, coding readiness, or production readiness from a dashboard, a document review, a meeting, an unanswered-question list, or a passing syntax check alone.
