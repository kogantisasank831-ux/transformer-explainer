---
name: ds-training-experiment-reproducibility
description: Make machine learning training and experiments traceable and reproducible across code, data, features, configuration, environments, hardware, randomness, distributed execution, checkpoints, metrics, and artifacts. Use for experiment tracking, immutable run manifests, deterministic and statistical reproducibility, notebook hardening, resume semantics, repeated trials, artifact lineage, privacy-safe metadata, and independent reruns.
---

# Training and Experiment Reproducibility

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data/model identity, environment, affected users and consumers, owners, and authority. Support ordinary backend retirement where applicable; use ML-specific validation, training, evaluation, and serving controls only for systems that contain those components. Treat documentation, registries, dashboards, experiment trackers, generated reports, and provider metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, data, model-risk, retention, quality, or release choices to the responsible owner. Do not invent usage, retention, quality, reproducibility, fairness, safety, latency, throughput, cost, or acceptance targets. Protect personal, confidential, licensed, and model-sensitive data and keep mutations within the explicitly authorized environment and scope.

## Define what reproducible means

1. Read [the training reproducibility checks](references/checks.md). Record the hypothesis or purpose, parent/baseline run, task and metric definitions, requested reproducibility level, allowed tolerance, owner and decision. Distinguish rerunning the same artifact, repeating training in the same environment, reproducing within statistical tolerance and replicating a finding through an independent implementation or dataset.
2. State the comparison environment. Bitwise equality may be impossible across framework versions, hardware, kernels, distributed topology or numerical precision. Define accepted metric, prediction, parameter or behavioral equivalence before running; do not declare failure or success after seeing the difference.
3. Give every run a durable ID and status such as queued, running, succeeded, failed, cancelled or incomplete. Never register an interrupted run as a completed training result because a checkpoint exists.

## Capture complete immutable lineage

Record repository and commit, dirty diff or source bundle, entry point, parameters and resolved configuration, environment variables by safe name, dependency lock and image digest, Python/runtime/framework/compiler, CUDA and driver, libraries, hardware/GPU type and count, topology, precision and numerical settings. Exclude secret values while recording their versioned reference where required.

Bind exact raw and transformed data/feature/label manifests, extraction and preprocessing versions, split assignment, sampling and weighting, schema, tokenizer/vocabulary, augmentations and fitted preprocessing artifacts. Record model architecture and initialization, pretrained checkpoint and revision, optimizer, scheduler, loss, regularization, epochs/steps, batch and accumulation, distributed strategy, gradient clipping, early stopping and selection rule.

Capture random seeds and generators for language, framework, data loader, sampler, augmentation and workers as applicable. Record deterministic flags, kernel/autotune settings and known nondeterministic operations. A seed alone does not establish reproducibility.

For distributed or resumed training, preserve rank/world size, sharding, ordering, synchronization, failure/retry behavior and complete checkpoint state including optimizer, scheduler, scaler, RNG, sampler and progress. Define whether resumption must be exact or only behaviorally equivalent and detect duplicated or skipped data.

## Track results and artifacts atomically

Log metric definition and aggregation, step/epoch and wall time, validation population, resource and cost evidence, warnings and ordinary failures. Store checkpoints, final weights, tokenizer, preprocessing, calibrator, signature/schema, thresholds, evaluation report and model card with hashes and lineage. Separate candidate selection metrics from final locked evaluation.

Make tracking writes idempotent or detect duplicates, and finalize a run only after required artifacts and manifests exist and verify. Protect tracking and artifacts with access, retention and integrity controls. A UI row or autolog call does not prove complete lineage.

Convert exploratory notebook logic into parameterized modules or pipelines for release-relevant runs. Restart from a clean kernel and environment; eliminate hidden state, manual cells and local paths. Preserve the notebook as exploration evidence when useful, not as an unreviewed production procedure.

## Reproduce and explain differences

First rerun in the same pinned environment and data, then perform an independent clean reconstruction when warranted. Repeat stochastic training enough times for the accepted comparison and report distribution, not the best seed. Compare manifests before metrics so identity mismatches are diagnosed early.

Use deterministic algorithms where available and proportionate, recognizing their performance cost and incomplete coverage. Compare data order and transformations, initial and intermediate checkpoints, loss curves, predictions and final metrics to localize divergence. Preserve failed reruns and numerical warnings.

Record reproduced, within tolerance, materially different, or inconclusive with evidence and root-cause confidence. Update the run recipe and tests for verified gaps. Reproducing a metric does not independently validate the dataset, evaluation design, fairness, safety or production suitability.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, restoration, model quality, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, accepted, released, retired, and verified work. Update affected project logic, code, tests, contracts, data/model records, documentation, ownership, and decisions when accepted behavior changes. Never claim decommissioning, data fitness, reproducibility, model approval, or inference optimization from a plan, successful command, tracked run, aggregate score, or theoretical calculation alone.
