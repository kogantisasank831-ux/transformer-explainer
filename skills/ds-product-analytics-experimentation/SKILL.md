---
name: ds-product-analytics-experimentation
description: Design, implement, and assess trustworthy product analytics and controlled experiments for backend and data science products. Use for decision-linked metrics, event contracts, identity and attribution, privacy and consent, exposure and assignment, A/A and A/B tests, sample-ratio mismatch, guardrails, power and duration, statistical and practical significance, segmentation, experiment decisions, and feedback-loop risks.
---

# Product Analytics and Experimentation

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web products; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, analytics, scans, generated artifacts, historical results, and third-party metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, legal, statistical, support, or business choices to the responsible owner. Do not invent support matrices, user needs, acceptance criteria, metric definitions, experiment thresholds, documentation guarantees, license interpretations, or compliance decisions. Protect personal and confidential data and keep mutations within the explicitly authorized environment and scope.

## Begin with a decision and measurement contract

1. Read [the analytics and experimentation checks](references/checks.md). State the product decision, behavior or outcome, target population, unit of analysis, owner and action that different results would trigger. Separate descriptive monitoring, product analytics, causal experimentation and business reporting.
2. Define every metric with numerator, denominator, entity and identity, eligibility, event-time and processing-time rules, attribution window, deduplication, late and missing data, bots/test/internal traffic, aggregation and segments. Version the definition and trace it to accepted product logic. A dashboard label is not a metric contract.
3. Inventory personal, device, tenant, prompt, model and sensitive data. Establish purpose, consent or other accepted basis, minimization, pseudonymization, access, retention, deletion and regional rules before collection. Do not use a stable identifier merely because the SDK provides one.

## Engineer trustworthy events

Define event names, producers, trigger semantics, required and optional fields, types, units, schema version, safe context and ownership. Choose the authoritative producer for outcomes and monetary or durable state; client events can describe interaction but may be blocked, duplicated or forged. Correlate client intent and server result without placing high-risk payloads in analytics.

Validate schemas at ingestion, quarantine or visibly count invalid events, and monitor volume, uniqueness, missingness, duplicates, delay and version adoption. Test instrumentation across control and treatment, retries, offline queues, multiple tabs/devices, authorization failures and long-running jobs. Reconcile critical events against an independent source. Instrumentation deployed is not instrumentation trustworthy.

For DS/ML, bind analytics to model, prompt/guardrail, feature, index and data versions where safe. Separate delayed ground-truth quality from immediate engagement. Guard against feedback loops where measured behavior changes training data or ranking, and avoid treating clicks as correctness without an accepted causal model.

## Design experiments before looking at outcomes

Write a falsifiable hypothesis, primary decision metric, guardrails, practical minimum effect, assignment unit, target population, randomization and stratification, variants, exposure/trigger rule, exclusions, expected allocation, power/sample-size method, duration and stopping rule. Freeze the analysis plan or version deviations. Do not invent a significance threshold or minimum effect after observing results.

Make assignment stable and mutually exclusive where required. Log assignment separately from actual exposure and analyze the accepted population, normally preserving intention-to-treat. Avoid conditioning on post-treatment behavior. Address cross-device identity, household or tenant clustering, network effects, carryover, novelty, seasonality and concurrent experiments.

Run A/A or pre-launch checks when risk warrants. Verify assignment balance and sample-ratio mismatch before outcome interpretation; diagnose it rather than waiving it. Check exposure parity, event loss, invariant metrics, contamination, version/config mismatch and guardrail collection. A significant result from a broken experiment is not evidence.

## Analyze and decide without result shopping

Use the prespecified method and report population, sample, exposure, duration, effect size, uncertainty interval and practical significance for primary and guardrail metrics. Control the accepted error rate for multiple metrics, variants and repeated looks. Use a valid sequential method when peeking or early stopping is allowed.

Treat subgroup findings as exploratory unless prespecified and adequately powered. Inspect heterogeneous effects and harm without hiding an adverse segment in an average. Record missing data, outliers, delayed outcomes and sensitivity analyses. Keep correlation from observational analytics separate from randomized causal effect.

Make the ship, stop, iterate or collect-more-data decision against the predeclared rule and all guardrails. Record decision owner, tradeoffs, follow-up and long-term measurement. Preserve negative and inconclusive results in an experiment registry. For model, retrieval or prompt changes, combine online product evidence with applicable offline quality, safety and latency gates; neither replaces the other.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, legal, user-acceptance, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, tested, observed, accepted, and verified work. Update affected project logic, code, tests, contracts, documentation, ownership, and decision records when accepted behavior changes. Never claim compatibility, product acceptance, causal impact, documentation completeness, license permission, or compliance from one tool result, scan, test environment, or document alone.
