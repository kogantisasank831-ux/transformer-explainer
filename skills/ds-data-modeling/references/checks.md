# Data-modeling checks

- Define what one row/document/event means and which identity survives rename, merge, and retry. State whether uniqueness is global, tenant-scoped, or time-bounded.
- Distinguish unknown, not-applicable, and absent values. Verify actual engine behavior for nulls, uniqueness, checks, coercion, collation, and foreign-key enforcement.
- Prevent tenant-crossing references with appropriate composite keys/references while retaining application authorization.
- Derive restrict, cascade, archive, history, correction, and retention behavior from accepted rules rather than convenience.
- Separate event/valid time from ingestion/availability time. Define interval boundaries, timezone, precision, ties, and late corrections.
- For features, require event validity and availability before prediction cutoff. Record authoritative and derived copies, freshness, reconciliation, and deletion propagation.
- Map every critical invariant to a constraint, transaction, application check, or unresolved decision and meaningful test. Sequential tests do not establish race safety.

Consult official documentation for the selected database and version. For PostgreSQL, see [constraint guidance](https://www.postgresql.org/docs/current/ddl-constraints.html).
