# SRS gap and business process validation checks

- Bind product scope, SRS and linked evidence revisions/status, owners/decision authorities, evidence hierarchy, next activity and blocking rule.
- Assign stable requirement/rule/process/step/state/entity/interface/question/decision IDs and preserve stated, inferred, proposed, answered, accepted and superseded states.
- Check requirements for one obligation, actor/trigger/outcome, clear terms/conditions, necessity, feasibility, verifiability, traceability and acceptance source.
- Normalize glossary, roles, states, identifiers, units/time/currency/rounding and expose contradictions across prose, diagrams, examples, schemas, prototypes and policy.
- Reconstruct each happy, alternate, exception, cancellation and recovery path with actors, authority, data, decisions, states, integrations, timing, outputs and audit evidence.
- Validate entity state transitions, concurrency, idempotency, retries/reversal, terminal behavior and unreachable/orphaned states.
- Validate human and system handoffs, contracts, ordering/duplicates, timeouts, partial failure, reconciliation, assignment/escalation and ownership.
- Cover data lifecycle, authorization/tenant/duty separation, calculations, NFRs, operations and conditional DS/ML/GenAI lifecycle requirements.
- Create one decision per neutral question with gap/impact, affected IDs, proposal options, blocking stage, owner/authority, status, source and acceptance evidence.
- Use boundary/negative/duplicate/concurrent/recovery scenarios, decision tables and accountable walkthroughs; attendance and a polished diagram are not acceptance.
- Gate coding readiness by process slice and preserve independent work, explicit blockers and authorized waivers without inventing defaults.
- Transfer every accepted answer into the target `PROJECT_LOGIC.md` effective rules and linked requirements/states/contracts/tests; an answer is not acceptance.

IREB publishes current [requirements elicitation resources](https://cpre.ireb.org/en/downloads-and-resources/downloads). The official [BPMN 2.0.2 specification](https://www.omg.org/spec/BPMN/) supports process, event, exception, transaction and compensation modeling, while explicitly leaving data models and business rules outside its scope; supplement diagrams with the required rule, data, authority and quality tables.
