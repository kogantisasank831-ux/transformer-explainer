# Migration checks

- Confirm current migration heads and database state before editing. Preserve applied history; add a merge migration when the framework and project call for it.
- Identify lock level, table scan/rewrite, transaction behavior, replication lag, log/disk amplification, timeout, and cancellation consequences for the actual engine/version.
- Treat non-null additions, volatile defaults, type changes, unique constraints, index creation, foreign keys, partitions, and large deletes as potentially expensive until measured.
- Separate schema expansion, application compatibility, backfill, validation, read/write switch, and contraction. Define the gate and owner for each stage.
- Backfills need stable ordering, bounded batches, resumable checkpoints, idempotent writes, concurrent-write strategy, error accounting, and reconciliation.
- Test fresh install plus supported upgrades. Verify rollback/roll-forward against realistic data; do not describe a backup without a tested restore path.
- Preserve tenant boundaries, row policies, grants, triggers, generated columns, views, CDC/replication, and downstream schemas.

Consult the current migration framework documentation, such as the [Alembic cookbook](https://alembic.sqlalchemy.org/en/latest/cookbook.html), and official engine documentation. PostgreSQL users should review [ALTER TABLE locking and rewrite behavior](https://www.postgresql.org/docs/current/sql-altertable.html) for their deployed version.
