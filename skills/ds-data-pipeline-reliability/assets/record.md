# Data pipeline reliability record

- Pipeline, rule IDs, owners, engine/orchestrator versions, run identity:
- Inputs/snapshots, interval, schema, code/config/environment, output manifest:

| Stage | Input / grain | Transformation / checkpoint | Quality / publication gate | Retry / recovery |
|---|---|---|---|---|

## Time, quality, and lineage

Record event/processing time, watermark/lateness, dedupe, corrections, tolerances, quarantine, reconciliation, lineage, and consumer visibility.

## Verification and backfill

List duplicate/interruption/late/schema/failure cases, backfill/live-run coordination, commands/results, actual data scale, CI/server gates, residual risks, owners, and whether any production replay occurred.
