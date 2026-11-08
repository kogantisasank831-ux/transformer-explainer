---
name: ds-technical-documentation
description: Create, restructure, validate, and maintain technical documentation for backend and data science products. Use for audience and task analysis, tutorials, how-to guides, reference and explanation, README and onboarding, architecture and decisions, APIs and schemas, operations and troubleshooting, executable examples, docs-as-code, versioning, ownership, data and model documentation, link and snippet tests, and cold-reader validation.
---

# Technical Documentation

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web products; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, analytics, scans, generated artifacts, historical results, and third-party metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, legal, statistical, support, or business choices to the responsible owner. Do not invent support matrices, user needs, acceptance criteria, metric definitions, experiment thresholds, documentation guarantees, license interpretations, or compliance decisions. Protect personal and confidential data and keep mutations within the explicitly authorized environment and scope.

## Design documentation around a reader's need

1. Read [the documentation checks](references/checks.md). Identify audiences, prior knowledge, tasks and decisions, supported product versions and environments, language, access and sensitivity, discovery path, owner and review trigger. Inspect existing documents and analytics or support evidence without assuming a missing page is the only problem.
2. Separate learning-oriented tutorials, goal-oriented how-to guides, precise reference and conceptual explanation. A page may link across types, but unclear purpose creates incomplete instructions and bloated reference. Define the canonical home for each fact and link instead of copying it into several guides.
3. Establish a documentation map covering quick start, installation/configuration, architecture and data flow, APIs/events/files, CLI or jobs, operations and recovery, security/privacy, troubleshooting, release/migration and contribution only as applicable. Preserve ADRs and project logic as authoritative decisions rather than rewriting rationale as current commands.

## Write from authoritative behavior

Verify every prerequisite, version, command, path, configuration key, default, permission, API field, example response, error and limitation against the exact source, schema, artifact or executed environment. Generate reference from contracts such as OpenAPI or configuration schemas where useful, but add human meaning, workflows, constraints and failure behavior. Generated output is not automatically accurate or usable.

Make tutorials safe, bounded and repeatable with a known starting state and visible outcome. Make how-to guides solve one real task with preconditions, alternatives and cleanup. Keep reference complete, consistent and searchable. Use explanation to connect design, tradeoffs and concepts without hiding required operational steps.

Use copy-safe examples with explicit placeholders and shell/language context. Never include credentials, personal data, internal hosts or unsafe destructive defaults. State side effects, cost, expected output, rollback and cleanup where material. Keep sample data small, licensed and privacy-safe.

For backend systems, document authentication and authorization, schemas, pagination, idempotency, errors, limits, async jobs, retries, versioning and examples as applicable. For DS/ML, document data and feature provenance, training and evaluation identities, model/tokenizer/runtime, intended and excluded use, metrics and limitations, inference contracts, prompts or retrieval configuration, safety controls, uncertainty, reproducibility and monitoring where present.

## Version and validate docs as product artifacts

Keep source with an explicit ownership and review workflow. Tie documentation to supported releases and make selectors, deprecation and migration paths clear. Mark stale, preview and unsupported material visibly. Avoid publishing internal-only operations or security details to a public surface.

Build documentation in CI and check local links, anchors, images, schemas and code fences. Execute commands and snippets in clean representative environments when feasible; compile or type-check examples and test API requests against a controlled implementation or contract. Check generated reference drift. Preserve ordinary failures rather than editing output to look successful.

Have a reader from the target audience perform a cold start or task using only the documentation. Record where they needed undocumented context, chose a wrong branch or could not recover. Automated link and spelling checks do not establish comprehension or task success.

Review after interface, configuration, schema, workflow, architecture, security, dependency, model/data, support-policy or incident changes. Track unanswered questions and known gaps with owners. Measure search failure, abandonment, feedback and support cases only with privacy-safe definitions. A page view does not prove usefulness, and a merged documentation change does not prove deployed behavior.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, legal, user-acceptance, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, tested, observed, accepted, and verified work. Update affected project logic, code, tests, contracts, documentation, ownership, and decision records when accepted behavior changes. Never claim compatibility, product acceptance, causal impact, documentation completeness, license permission, or compliance from one tool result, scan, test environment, or document alone.
