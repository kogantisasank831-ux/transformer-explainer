# Query optimization checks

- Preserve accepted rows, duplicates, order, nulls, tenant/authorization filters, precision, and time semantics with an independent oracle.
- Capture query fingerprint, bindings class, schema/statistics version, table/index size, distribution/skew, concurrency, and cache state.
- Compare planner estimates to actual rows and identify scans, joins, sorts, aggregates, loops, spill, I/O, lock waits, and repeated calls. `EXPLAIN ANALYZE` executes the statement; use a safe environment or transaction strategy.
- Check N+1 access, unnecessary columns/rows, offset pagination growth, implicit casts, functions on indexed columns, wildcard patterns, correlated subqueries, and unstable ordering.
- Evaluate index column order, selectivity, coverage, partial predicate, uniqueness, build method, storage, write cost, and redundancy. More indexes are not automatically faster.
- Measure cold and warm behavior where relevant, multiple parameter classes, concurrent load, and production-like volume. Report percentiles and repetitions, not one best run.
- For vector/approximate search, pair latency with recall/ranking and filter correctness.

Use official documentation for the actual engine. PostgreSQL users can consult [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) and [examining index usage](https://www.postgresql.org/docs/current/indexes-examine.html).
