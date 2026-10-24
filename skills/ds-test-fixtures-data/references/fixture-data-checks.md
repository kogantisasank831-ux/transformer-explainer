# Fixture and data checks

| Fixture surface | Verify |
|---|---|
| Factory | Fresh nested values; overrides copied/owned deliberately; valid versus invalid modes explicit; stable IDs/timestamps where meaningful; no import-time services or side effects. |
| Tenant/state | Overlapping IDs across tenants, same/different idempotency keys, pending/success/failure variants and independent authority context. Don't make IDs globally unique in every fixture and miss tenant-key bugs. |
| Resource | Unique owned namespace/path, immediate cleanup registration, partial setup/failure handling, correct close order, parallel safety and cleanup diagnostics. Transaction rollback alone may not isolate workers/external effects. |
| Evaluation | Versioned immutable expected cases, independent acceptance/provenance, entity/time separation and no tuning on held-out evaluation data. Synthetic schemas cannot replace representative evaluation populations. |
| Privacy | No real credentials, production rows/prompts or sensitive logs by default. Replacing names is not an anonymity proof; linkage/rare attributes and copied outputs may remain sensitive. |

Use bounded representative data: minimal happy paths plus meaningful schema/numeric/Unicode/time/duplicate cases. Keep huge corpora and models outside ordinary unit CI; reference approved versioned artifacts when a dedicated gate needs them. Don't silently normalize away a tested edge condition.

For Python use established pytest fixture/factory conventions. Primary reference: [pytest fixtures and safe teardown](https://docs.pytest.org/en/stable/how-to/fixtures.html). Test fresh-object behavior and requested lifecycle guarantees, not private fixture call counts without a meaningful ownership invariant.
