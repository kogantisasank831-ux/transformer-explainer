---
name: ds-ux-product-acceptance
description: Turn accepted user needs and business processes into product acceptance evidence for backend and data science products. Use for actors and contexts, end-to-end journeys, usability research, prototypes, task success, qualitative findings, acceptance criteria, UAT, business state and side effects, error recovery, DS explanations and overrides, release decisions, and traceable unresolved questions.
---

# UX and Product Acceptance

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web products; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, analytics, scans, generated artifacts, historical results, and third-party metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, legal, statistical, support, or business choices to the responsible owner. Do not invent support matrices, user needs, acceptance criteria, metric definitions, experiment thresholds, documentation guarantees, license interpretations, or compliance decisions. Protect personal and confidential data and keep mutations within the explicitly authorized environment and scope.

## Start with the user, task and context

1. Read [the UX and acceptance checks](references/checks.md). Identify intended and excluded users, roles and permissions, goals, frequency, domain knowledge, environment, devices, constraints, accessibility needs, assisted or offline steps and consequences of error. Trace each need to an accepted SRS or project-logic source and preserve unanswered process questions.
2. Map the end-to-end journey, including entry, prerequisites, identity, handoffs, waiting, notifications, downstream systems, support, recovery and completion outside the screen. Distinguish user goals from requested features and business rules from current implementation behavior.
3. Define what product decision the research or acceptance activity will support. Do not use a usability session to approve security, statistical model quality, load capacity or legal compliance outside its evidence boundary.

## Make acceptance outcome based

Write criteria in observable user and business terms with actor, preconditions, input state, action, expected visible result, authoritative state change, external effects, timing where accepted, and recovery. Cover happy path, validation, authorization, duplicates, cancellation, timeout, partial failure, retry, stale data and support escalation as applicable. Avoid criteria that merely say a component exists or matches an internal implementation.

Link criteria to rule IDs, contracts and planned tests. Mark the owner and decision status. Separate functional correctness, usability, accessibility, compatibility, performance, security, privacy and DS quality so one passing category cannot conceal another failing gate.

For analytics or optimization products, verify that users understand units, filters, time windows, constraints, feasibility and export semantics. For ML or GenAI, cover input scope, uncertainty or confidence, provenance and freshness where required, harmful or invalid output, human review and override, fallback and escalation. A plausible model answer is not accepted business correctness.

## Research with representative tasks and people

Define research questions before recruiting. Select actual or likely users across relevant experience, roles, constraints and edge cases; record the sampling limit. Obtain appropriate consent and minimize, control and delete recordings and personal data according to policy. Keep incentives and observers from coercing or exposing participants.

Use realistic neutral tasks that state a goal without revealing the interface steps. Capture task completion and correctness, time and abandonment where useful, errors, assists, navigation path, confidence and comments. Define success and measurement before sessions. Observe behavior and ask follow-ups without teaching the product during the task.

Synthesize repeated patterns and material individual barriers with evidence. Keep participant statements, researcher observation and interpretation distinct. Do not turn a small convenience sample into a population percentage. Update designs and rerun affected tasks rather than treating research as a one-time approval ceremony.

## Execute accountable product acceptance

Plan UAT against an exact candidate, environment, configuration, schemas, integrations and representative privacy-safe data. Name independent business acceptors and their authority. Provide reproducible scenarios and expected outcomes while allowing exploratory use. Capture evidence, defects, severity source, workaround, owner and retest state.

Reconcile backend state and side effects, not only the visible confirmation. Include notifications, jobs, audit, downstream integration and data/model version where applicable. Keep test-data cleanup and external effects controlled.

Issue an acceptance decision per criterion or release scope as accepted, rejected, conditionally accepted or not tested. Conditional acceptance needs explicit conditions, expiry, risk owner and follow-up evidence. Missing critical criteria, blocked representative users or unresolved consequential business logic prevents full acceptance. A stakeholder meeting, signed screenshot or local demo alone does not prove the product meets the need.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, legal, user-acceptance, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, tested, observed, accepted, and verified work. Update affected project logic, code, tests, contracts, documentation, ownership, and decision records when accepted behavior changes. Never claim compatibility, product acceptance, causal impact, documentation completeness, license permission, or compliance from one tool result, scan, test environment, or document alone.
