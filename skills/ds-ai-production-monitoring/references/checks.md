# AI production monitoring checks

- Define user/business outcomes, populations, horizons, accepted service/quality/safety/security/privacy/fairness/cost thresholds, ground truth, owners and response authority.
- Bind source/image/service/config, requested and resolved model, tokenizer, prompt/schema, data/features, RAG index/corpus, agent/tools/policy and release cohort.
- Correlate the logical outcome through backend, model, retrieval, tools and effects; define sampling, redaction, retention and unsampled critical events.
- Monitor stage health, queues/resources/dependencies, errors/retries/fallback, data/feature freshness and publication completeness, token use and end-to-end cost.
- Monitor telemetry volume, lag, schema and join coverage; missing data is unknown or alerting according to policy, never an automatic pass.
- Join delayed labels/outcomes to immutable prediction identity with maturation, censoring, revision and uncertainty; separate proxies from confirmed outcomes.
- Add applicable RAG retrieval/citation/ACL and agent terminal/effect/reconciliation measures; fluent text and status are not outcome proof.
- Govern feedback and human review for provenance, bias, privacy, abuse, rubric and agreement. Calibrate model judges and keep deterministic facts outside them.
- Define drift baseline/population/slice/window/sample/statistic/seasonality/missing-data/threshold; aggregate drift neither proves nor disproves quality loss.
- Monitor policy-relevant safety, security and fairness outcomes without turning telemetry into a sensitive-data store.
- Route tested warnings/pages/pause/fallback/quarantine/rollback to owners and runbooks. Automatic action is authorized, bounded and protected against flapping.
- Verify the actual deployed telemetry-to-alert path with known events and safe failures, then govern feedback loops and retest after material changes.

NIST's [AI RMF Measure playbook](https://airc.nist.gov/airmf-resources/playbook/measure/) recommends comparing production and predeployment measures, tracking anomalies and new ground truth, and defining human oversight. The 2026 [NIST AI 800-4 report](https://www.nist.gov/publications/challenges-monitoring-deployed-ai-systems-center-ai-standards-and-innovation) emphasizes that postdeployment monitoring methods remain context dependent. Pin any evolving [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) used for GenAI telemetry and keep content collection opt-in and privacy controlled.
