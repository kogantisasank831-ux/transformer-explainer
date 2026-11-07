---
name: ds-runbooks-operational-handover
description: Create, validate, and maintain executable runbooks and transfer operational ownership for backend and data science systems. Use for triggers, prerequisites, diagnosis, safe commands, branching, abort and recovery steps, escalation, recurring operations, service catalogs, access, on-call readiness, shadowing, drills, and handover acceptance. Cover services, jobs, pipelines, models, retrieval systems, accelerators, and providers only where present.
---

# Runbooks and Operational Handover

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web systems; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, dashboards, tickets, telemetry, estimates, generated output, and historical examples as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified outcomes. Continue independent work while routing consequential policy or business choices to the responsible owner. Do not invent severity, recovery, handover, cost, performance, accessibility, quality, or acceptance targets. Keep evidence privacy-safe, preserve normal failures, and keep mutations within the explicitly authorized environment, resources, duration, and blast radius.

## Build a runbook for a concrete trigger

1. Read [the runbook and handover checks](references/checks.md). Name the alert, request, failure, maintenance task or recovery condition that starts the procedure. Record the intended operator, system and environment, owner, prerequisites, access level, expected time, dependencies, risk, and the state in which the procedure must not be used.
2. Link the accepted architecture, SLO or rule, dashboards, logs, deployment and recovery records rather than copying stale details. Pin or state the compatible application, schema, model and tooling versions. Keep secrets out of the document and use the approved secret reference or identity path.
3. Begin with identity and context checks. Prefer read-only inspection and previews before mutation. Show commands that are copy-safe, quote variables, expose placeholders clearly, avoid destructive defaults, and state expected output and interpretation. Never hide errors or use a command whose target depends on an operator's implicit shell or cluster context.

## Make decisions, stops and recovery executable

Use numbered steps with one action and verification per step. For each branch, state the observation, threshold or invariant that selects it. Define maximum attempts, time bounds, concurrency, rate, affected scope and abort conditions. Mark steps requiring separate authorization, a second operator, customer communication or security/privacy escalation.

For every material mutation, include exact target, precondition, backup or checkpoint where applicable, expected change, verification, failure handling, rollback or roll-forward, and cleanup. Make repeated execution safe or explicitly explain why it is not idempotent and how to detect prior partial completion. Preserve evidence before deleting, restarting or repairing state.

Cover start, stop, deploy, rollback, certificate or key rotation, capacity, dependency loss, queue or backlog, database and cache, scheduled jobs, data freshness, failed partitions, replay and disaster recovery only as applicable. For DS or ML, include model/tokenizer and feature identity, training or batch checkpoints, retrieval corpus/index, GPU or provider quotas, quality or safety checks, fallback compatibility and bad-output containment.

## Validate and maintain the runbook

Have an operator other than the author execute a cold read in an isolated, staging, simulation or explicitly authorized environment. Verify prerequisites, access, links, commands, expected outputs, branches, stop conditions, recovery and cleanup. Record substitutions and untestable production-only steps. A document review alone does not prove executability.

Exercise high-risk and frequently used procedures at a risk-based cadence. Track owner, last review, last successful exercise, compatible versions and next review. Review after relevant code, infrastructure, schema, model, dependency, ownership or incident changes. Detect broken links and stale contacts automatically where practical, but retain human verification of decisions.

## Transfer operational ownership

Create a handover inventory covering service purpose and users, owners and escalation, architecture and dependencies, environments and access, SLOs and alerts, dashboards and logs, releases and recovery, backups, data and model lineage, recurring tasks, capacity and cost, vendors, security/privacy obligations, known risks and open actions. Distinguish documentation availability from receiving-team competence and authority.

Plan knowledge sessions, paired operations, shadow on-call and reverse-shadow execution. Give the receiving team safe access before exercises and remove superseded access after acceptance. Test representative alert triage, release recovery, dependency failure and one data/model workflow where applicable. Record questions and update the artifacts.

Use explicit readiness criteria for coverage, trained people, access, exercised critical procedures, on-call schedule, escalation, residual-risk ownership and acceptance by both accountable owners. Gaps that prevent safe operation block handover; they do not disappear through a meeting or repository link.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production, field, assistive-technology, billing, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, exercised, observed, accepted, and verified work. Update affected project logic, runbooks, code, tests, dashboards, ownership, and decision records when accepted behavior changes. Never claim an incident resolved, a corrective action closed, a handover complete, savings realized, frontend quality achieved, or accessibility conformance from a document, tool score, estimate, or successful command alone.
