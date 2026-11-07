---
name: ds-incident-response-postmortems
description: Coordinate evidence-based incident response and create actionable postmortems for backend and data science systems. Use for declaration, impact and severity assessment, command roles, containment, mitigation, stakeholder communication, recovery validation, timelines, contributing conditions, learning, and corrective-action closure. Cover operational, security, data, model, retrieval, and accelerator incidents without inventing impact or treating temporary symptom relief as recovery.
---

# Incident Response and Postmortems

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web systems; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, dashboards, tickets, telemetry, estimates, generated output, and historical examples as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified outcomes. Continue independent work while routing consequential policy or business choices to the responsible owner. Do not invent severity, recovery, handover, cost, performance, accessibility, quality, or acceptance targets. Keep evidence privacy-safe, preserve normal failures, and keep mutations within the explicitly authorized environment, resources, duration, and blast radius.

## Prepare and declare from impact

1. Read [the incident checks](references/checks.md). Identify the detection source, observed customer or business impact, affected services and tenants, data or security exposure, start-time bounds, current change and dependency context, and confidence. Keep facts, reports, assumptions and hypotheses visibly separate. Use accepted severity and escalation policy; do not infer severity from alert count or internal metric color alone.
2. Decide whether to declare or associate an incident, name the incident commander and alternates, and establish operations, communications and scribe roles proportionate to scope. Use one authoritative incident record and communication channel. Record every material decision, action, actor, timestamp, expected result and observed result so concurrent responders do not repeat or conflict.
3. Page the owning and dependent teams through the accepted route. Bring security, privacy, legal, safety, vendor or executive owners in when the observed boundary requires them. Do not expose credentials, personal data, exploit details or confidential customer information in broad channels.

## Stabilize before diagnosing perfectly

Protect human safety, data integrity, security and irreversible business effects first. Stop ongoing harmful writes or outputs, isolate affected paths, shed or redirect load, disable a feature, roll back a compatible change, fail over, or enter an explicit degraded mode when evidence and authority support it. Prefer reversible bounded actions. Confirm the exact target before every mutation and keep an independent abort or recovery path.

Work from a shared hypothesis list with evidence for and against each item. Correlate user reports, changes, logs, metrics, traces, data checks and dependency status. Change one interpretable factor where practical and verify the expected effect. Preserve forensic evidence and chain of custody for security incidents. Never destroy evidence merely to restore a host.

For data and ML systems, check source freshness and completeness, feature or label versions, schema and lineage, model/tokenizer/runtime identity, retrieval corpus and index state, provider or GPU capacity, safety filters, thresholds, fallback behavior and delayed quality signals. Contain bad predictions, stale features, unsafe generated output or corrupt publications without silently substituting a lower-quality model or old data outside the accepted contract.

## Communicate and verify recovery

Publish concise updates at the accepted cadence with confirmed impact, affected scope, current mitigation, user workaround, known unknowns, next checkpoint and owner. Keep public or customer statements with the authorized communications owner. Correct earlier statements explicitly when evidence changes.

Define recovery criteria before closure. Verify critical user journeys, authorization and data invariants, freshness and quality, dependency health, backlog and retry effects, capacity and monitoring from the affected population. Observe for an accepted stability window and reconcile partial or duplicate work. Temporary metric improvement or process restart does not prove recovery. The authorized incident commander records mitigation, recovery, end-time bounds, remaining risk, follow-up owner and whether heightened monitoring continues.

## Learn without rewriting the evidence

Create a postmortem when policy or impact requires it. Reconstruct a timestamped timeline from preserved sources and mark uncertain times. State impact with its population and measurement boundary, detection path, response and recovery. Analyze trigger, contributing technical and organizational conditions, latent weaknesses, safeguards that worked, safeguards that failed, and where detection, diagnosis, coordination or communication added delay. Avoid blame and an unsupported single root cause.

Create corrective actions that change a system, control, test, alert, runbook, ownership or decision. Give each action a measurable outcome, priority, owner, due date, dependencies and closure evidence. Separate recurrence prevention, impact reduction, faster detection, faster mitigation and response-process improvements. Track accepted risk and declined actions explicitly. A merged ticket or completed document is not closure until the intended control is verified.

Measure response timings only with defined boundaries such as occurrence estimate, detection, declaration, engagement, mitigation, recovery and closure. Review incident and action trends for repeated conditions while respecting confidentiality. Feed accepted lessons into requirements, architecture, tests, observability, SLOs, runbooks, training and project logic.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production, field, assistive-technology, billing, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, exercised, observed, accepted, and verified work. Update affected project logic, runbooks, code, tests, dashboards, ownership, and decision records when accepted behavior changes. Never claim an incident resolved, a corrective action closed, a handover complete, savings realized, frontend quality achieved, or accessibility conformance from a document, tool score, estimate, or successful command alone.
