---
name: ds-model-evaluation-release-gates
description: Design and execute contextual model evaluation and release gates for classical ML, forecasting, optimization, ranking, retrieval, and generative AI systems. Use for intended and excluded use, independent datasets and slices, metric and threshold contracts, uncertainty, baseline comparison, robustness, fairness, safety, privacy, latency and cost, human and red-team evaluation, exact artifact identity, approval, rollback, and monitoring readiness.
---

# Model Evaluation and Release Gates

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data/model identity, environment, affected users and consumers, owners, and authority. Support ordinary backend retirement where applicable; use ML-specific validation, training, evaluation, and serving controls only for systems that contain those components. Treat documentation, registries, dashboards, experiment trackers, generated reports, and provider metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, data, model-risk, retention, quality, or release choices to the responsible owner. Do not invent usage, retention, quality, reproducibility, fairness, safety, latency, throughput, cost, or acceptance targets. Protect personal, confidential, licensed, and model-sensitive data and keep mutations within the explicitly authorized environment and scope.

## Write the evaluation contract first

1. Read [the model evaluation checks](references/checks.md). Define the user and business decision, intended and excluded use, prediction or generation unit, operating environment, affected groups, consequences of errors, human role, baseline, exact candidate model/tokenizer/preprocessing/threshold/config identities, owners and release authority.
2. For each gate record metric or rubric, population and slices, direction, accepted threshold or non-inferiority margin, sample requirements, uncertainty method, severity, owner and action on failure. Do not choose the winning metric or threshold after inspecting candidate results.
3. Separate model capability, system behavior, safety/security, usability, performance/cost, legal/policy and operational readiness. One aggregate quality score cannot waive another required gate.

## Build independent representative evaluation evidence

Record dataset and label provenance, rights/privacy, collection and annotation process, time range, inclusion/exclusion, duplicates, contamination checks, sample weights, snapshot hash and relation to training/tuning. Keep a locked final set from repeated selection. Use time, group or entity splits that match deployment and prevent preprocessing leakage.

Cover normal, rare, high-impact, boundary, missing/corrupt, out-of-distribution and previously failed cases with meaningful slices. Assess label quality and ambiguity. For changing populations, evaluate temporal and geographic generalization and document unsupported conditions rather than extrapolating.

Choose task-appropriate evidence. Examples include class-specific precision/recall and calibration, regression error in business units and tails, ranking quality and exposure, forecast horizon and interval coverage, survival/censoring rules, optimization feasibility and constraint violations, retrieval relevance and groundedness, and generative factuality, instruction following, safety and structured-output validity. These are options, not universal gates.

For human or rubric scoring, define instructions, blind/randomized presentation, sampling, adjudication, agreement and conflicts of interest. Calibrate any model-based judge against suitable human evidence and test position, verbosity and self-preference bias. Do not use a judge model's confidence as ground truth.

## Quantify comparison and harms

Report per-example or paired comparison where appropriate, effect size and uncertainty interval, sample size, missing results and practical significance against baseline. Address multiple candidates, metrics and repeated looks with the accepted method. Report distribution and slices, not only means.

Evaluate robustness to accepted perturbations, missing inputs, distribution shift, dependency failure and abuse. Assess fairness and differential performance for justified groups, privacy leakage, security and adversarial risk, harmful output, human override and safe failure according to the mapped risk. Route deep security testing to the specialist workflow while retaining gate status.

Measure end-to-end latency, throughput, resource and cost under the accepted serving workload, including preprocessing, retrieval/tools, queueing and postprocessing. Check output/API compatibility, explainability or provenance, fallback and degraded behavior. Offline quality does not establish online system behavior.

## Make release a traceable decision

Run gates on the immutable deployable artifact and exact runtime configuration. Verify reproducible loading, signatures, dependencies, license/provenance, observability, monitoring thresholds, feedback and appeal paths, rollback/fallback compatibility, capacity and runbook readiness. Link all evidence to the candidate digest.

Required missing, skipped, stale or failed gates block release unless the accountable risk authority records a scoped exception, rationale, expiry and controls. Keep evaluator and approver independence proportionate to impact. Record accepted, rejected, conditional or inconclusive rather than averaging failures away.

After offline approval, use separately authorized shadow, canary or experiment evidence before broad exposure where required. Monitor the same operational definitions and detect performance, quality, fairness and safety changes with delayed labels accounted for. A registry stage change, model card or leaderboard rank alone does not approve production release.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, restoration, model quality, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, accepted, released, retired, and verified work. Update affected project logic, code, tests, contracts, data/model records, documentation, ownership, and decisions when accepted behavior changes. Never claim decommissioning, data fitness, reproducibility, model approval, or inference optimization from a plan, successful command, tracked run, aggregate score, or theoretical calculation alone.
