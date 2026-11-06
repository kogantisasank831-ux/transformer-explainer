# Data pipeline reliability checks

- Fix logical interval, source snapshot/offsets, schema, code/config/environment, and output identity. Avoid implicit latest inputs and wall-clock business rules.
- Define partition/key grain, event versus processing time, time zone, lateness, corrections, deduplication horizon, and replay semantics.
- Stage and validate before atomic publication. Check abandoned staging cleanup and prevent partial consumer visibility.
- Commit checkpoints only after durable sink effects. Bind them to compatible input/code/config/schema/output state.
- Validate schema plus independent business invariants, source-to-target reconciliation, quarantine, completeness, freshness, and distribution. Record accepted tolerances and owners.
- Track lineage through derived tables, feature datasets, embeddings/indexes, and model artifacts. Preserve point-in-time correctness for ML.
- Backfills need isolated scope, resource limits, live-run coordination, stale-write protection, validation, promotion, rollback/roll-forward, and audit.

Consult the selected orchestrator and processing engine documentation. Airflow users can review its current [best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), while verifying behavior against their deployed version.
