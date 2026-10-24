# Integration checks

| Surface | Real boundary and failure evidence |
|---|---|
| Database | Actual target engine/driver/schema, separate committed reads, uniqueness/FK/tenant constraints, transaction rollback, null/precision/time behavior and old/new schema compatibility when relevant. |
| Queue/worker | Supported broker/delivery/ack semantics, worker consumption, duplicate/replay and commit-before-ack failures; count durable results and external effects separately. A fake queue cannot prove broker behavior. |
| Cache | Tenant/version key identity, serialization, invalidation/expiry and stale-read policy with controlled clock or bounded observation; cache success is not authorization. |
| File/object | Real supported adapter, metadata/content equality, partial write/publication behavior, access scope and test-owned cleanup. Emulator success is not cloud-policy or outage proof. |
| Inference/data | Real installed preprocessing/serialization/runtime boundary, artifact identity and output alignment. Stubbed prediction validates plumbing only; actual-model correctness/quality needs its own evidence. |
| External API | Local stub for fault/protocol branches versus authorized provider sandbox for real compatibility; document which is used. Do not claim a provider test from self-authored stub responses. |

Use explicit startup readiness checks and bounded retries only for environment readiness, preserving timeout failures. Don't rerun a failed business assertion until it happens to pass. Isolate parallel tests without assuming transaction rollback covers background workers, sequences, external effects or schema changes.

For Python, preserve established pytest fixtures and cleanup semantics; [fixture documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html) is a primary starting point. Confirm the actual database/broker/client version in its official documentation before relying on transaction, pool or acknowledgment behavior.

List all crossed boundaries and label each real, emulator, fake or not exercised. Test count and green mocks do not upgrade that classification. Missing required dependency services block the gate instead of becoming an automatic skip.
