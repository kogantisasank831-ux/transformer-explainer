# Data science requirements checklist

Use this as a coverage aid, not a questionnaire to send verbatim. Translate relevant items into source-backed requirements or decisions; mark inapplicable areas with a reason.

## Business decision and error costs

- Identify the actor, decision frequency, intended action, existing baseline, and measurable value.
- Define the cost of false positives, false negatives, abstention, delay, and incorrect automated actions.
- Separate predictive performance from business impact. Identify whether causal claims require an experiment or another defensible identification strategy.
- Identify human review capacity, override rules, appeal/correction paths, and audit needs where relevant.

## Data and labels

- Define row/entity/event, schema, units, timezone, event time versus ingestion time, and missing-value semantics.
- Record sources, permitted use, access owner, retention/deletion, lineage, dataset version, and deployment-time availability.
- Confirm whether data and labels exist and are accessible. Treat their availability and quality as unknown until evidence supports them.
- Define target construction, observation and prediction windows, label delay, label disputes, annotation procedure, and reference standard.
- Check duplicates, missingness, outliers, imbalance, selection effects, entity overlap, subgroup support, and representativeness.
- For joins and derived features, establish point-in-time correctness and which information is available at prediction time.
- Identify restrictions on sending data to providers, exporting embeddings, logging prompts, or persisting user feedback.

## Evaluation validity and reproducibility

- Choose splits that match deployment: temporal for forecasting, entity/group separation for dependent observations, and independent test data protected from tuning.
- Require preprocessing, feature selection, resampling, and tuning to learn only from appropriate training partitions.
- Define baseline, primary/guardrail metrics, averaging, thresholds, important slices, and uncertainty reporting appropriate to sample size and dependence.
- Do not reduce an imbalanced classification objective to accuracy alone. Tie metric selection to actual error costs.
- Define experiment configuration, dataset and code versions, seeds where applicable, dependencies, artifact lineage, and reproducibility tolerance. Do not promise bitwise determinism across hardware.
- Define evaluation evidence and who accepts a release. Keep proposed thresholds pending until agreed.
- Record monitoring signals, feedback/label delay, review cadence, and retraining or rollback decision ownership without inventing arbitrary triggers.

## Workload-specific branches

| Workload | Additional requirements to establish |
|---|---|
| Analysis/dashboard | Metric definitions, denominators, aggregation grain, refresh schedule, reconciliation, user access, and interpretation limits. |
| Experiment/causal analysis | Estimand, randomization unit, assignment, contamination, sample-size rationale, stopping policy, guardrails, and causal assumptions. |
| Classification/regression | Target, horizon, imbalance, loss/cost, threshold policy, calibration if decisions use probability, and abstention. |
| Forecasting | Horizon, issue time, grain, hierarchy, seasonality, time-aware backtesting, exogenous feature availability, and intervals. |
| Ranking/recommendation | Candidate generation, relevance labels, cold start, exposure/position bias, offline metrics, and online guardrails. |
| Clustering/anomaly detection | Meaning of usefulness, validation beyond internal scores, review capacity, and investigation/alert burden. |
| Optimization | Objective and units, hard/soft constraints, feasibility tolerances, solver budget, fallback, and safe handling of infeasible results. |
| Batch pipeline | Input cutoff, freshness, schedule, completion deadline, rerun/backfill semantics, and partial-output handling. |
| Online inference | Input/output schema, latency boundary, arrival pattern, concurrency, payload size, saturation policy, and model unavailability. |

## GenAI, RAG, and agents

- Establish whether knowledge must be current and which sources are authoritative; define citation, unsupported-answer, and abstention behavior.
- Specify ingestion formats, corpus ownership, document versions, access filters, deletion propagation, and cross-tenant isolation.
- Define representative evaluation cases, reference answers or rubrics, retrieval and answer metrics, judge limitations, human adjudication, and regression gates.
- Specify structured outputs and handling of malformed, incomplete, unsafe, or contradictory output. Do not treat a prompt as a security boundary.
- Define tool allowlists, argument validation, per-user authority, approval points, and treatment of untrusted retrieved or tool content.
- Define state/checkpoint semantics, cancellation, duplicate requests, replay, partial side effects, and recovery after tool failure.
- Bound steps, tokens, spending, execution time, and parallelism; leave numeric limits unresolved when absent.
- Establish provider/model licensing, data processing and retention constraints, version changes, fallback behavior, and reproducible evaluation artifacts.

## Workload and operational measurements

- Describe traffic or batch volume, peak/burst pattern, input/output distribution, dataset growth, and relevant CPU/RAM/GPU limits.
- Distinguish users from requests; do not infer requests per second from a user count without behavior assumptions.
- Define service objectives, measurement windows, availability exclusions, failure rates, recovery targets, unit cost, and budget ownership as applicable.
- Identify failure behavior for stale data, schema drift, unavailable dependencies, overloaded queues, model failures, and low-quality predictions.
- Avoid carrying another project's hardware, client details, or performance targets into the current baseline without evidence.
