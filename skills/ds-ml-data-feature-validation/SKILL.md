---
name: ds-ml-data-feature-validation
description: Design and implement data and feature validation for machine learning, forecasting, optimization, retrieval, and analytical systems. Use for provenance and immutable snapshots, schema and domain rules, labels, splits, duplicates and contamination, point-in-time correctness, feature transformations, offline-online parity, freshness, skew and drift, slices, unstructured data, quarantine, and release-blocking quality evidence.
---

# ML Data and Feature Validation

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data/model identity, environment, affected users and consumers, owners, and authority. Support ordinary backend retirement where applicable; use ML-specific validation, training, evaluation, and serving controls only for systems that contain those components. Treat documentation, registries, dashboards, experiment trackers, generated reports, and provider metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, data, model-risk, retention, quality, or release choices to the responsible owner. Do not invent usage, retention, quality, reproducibility, fairness, safety, latency, throughput, cost, or acceptance targets. Protect personal, confidential, licensed, and model-sensitive data and keep mutations within the explicitly authorized environment and scope.

## Define fitness for the model use case

1. Read [the ML data and feature checks](references/checks.md). Define the prediction, ranking, forecast or optimization unit; entity and event time; outcome and label availability; training, validation, evaluation and serving populations; intended and excluded uses; owners; and the decision a failed check must trigger. A dataset can be valid for one use and unsafe for another.
2. Record source systems, collection purpose and rights, privacy class, lineage, extraction query or job, schema version, transformation code, immutable snapshot or manifest, partition range, row/object count, checksum and environment. Keep raw, cleaned, labeled, transformed, feature and published identities distinct.
3. Write accepted quality rules from domain and contract evidence. Automatically inferred schemas and historical distributions are proposed baselines, not business acceptance.

## Validate structure, content and relationships

Check required fields, types, encodings, shapes, units, time zones, ranges, categories, null and default semantics, finite numeric values, lengths, uniqueness, keys, referential relationships, temporal ordering, coverage and volume. Distinguish zero, missing, unknown, not applicable and censored values. Check duplicates at the business entity or event grain, not only byte equality.

Validate cross-field and domain invariants, monotonicity, conservation or balance rules, physically feasible values, constraints and downstream contracts. For time series, check interval, gaps, overlap, timezone/DST, late corrections and forecast horizon. For optimization, validate coefficients, bounds, units, feasibility inputs and scenario identity.

For text, image, audio, documents and retrieval corpora, validate format and decode, language, length/resolution, corruption, duplication or near-duplication, metadata, document boundaries, extraction quality and rights. Route personal-data and malicious-content controls to their specialist workflows while preserving findings here.

## Protect labels and evaluation boundaries

Define label source, adjudication, timestamp, delay, observation window, ambiguity, missingness, revisions and quality sampling. Measure agreement or noise where relevant and preserve class prevalence and slice behavior. Do not treat absence of an event as a negative label without an accepted observation rule.

Create splits by entity, group, time or geography according to deployment. Prevent the same entity, near duplicate, future event, derived label, aggregate containing the outcome or preprocessing fitted on all data from crossing the boundary. Keep a locked final evaluation set separate from tuning. Detect contamination against pretraining, retrieval corpora or external benchmarks where relevant and feasible.

## Make features point-in-time correct

For each feature record definition, entity key, source, event and availability time, window, aggregation, units, default/unknown behavior, transformation version, owner, freshness and online source. Join only values available at prediction time. Simulate historical retrieval through the same point-in-time semantics and test late-arriving and corrected data.

Compare offline and online feature names, types, values, transforms, defaults, encoding, precision and freshness on matched entities and timestamps. Bind training and serving code or transformation artifacts where possible. A shared feature name does not prove parity.

Measure distribution and missingness across time and meaningful slices. Distinguish data drift, training-serving skew, seasonality, sampling changes and real population change. Use accepted feature-specific thresholds and sample requirements; do not apply one statistical distance to every feature. Investigate the mechanism before accepting or blocking.

## Gate and publish evidence

Run validation before training, after transformation, before publication and on serving samples where applicable. Quarantine or version failed partitions and prevent partial publication. Make exceptions explicit with rule, scope, owner, rationale, expiry and monitoring. Do not silently update a schema or baseline to make new data pass.

Retain machine-readable results, statistics by slice, failed examples within privacy limits, code/config versions and source manifests. Test validators with known-good and seeded bad cases. Reconcile accepted counts and hashes through the pipeline. Passing validation proves only the encoded rules and sampled boundary; domain review and deployed model behavior remain separate.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, restoration, model quality, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, accepted, released, retired, and verified work. Update affected project logic, code, tests, contracts, data/model records, documentation, ownership, and decisions when accepted behavior changes. Never claim decommissioning, data fitness, reproducibility, model approval, or inference optimization from a plan, successful command, tracked run, aggregate score, or theoretical calculation alone.
