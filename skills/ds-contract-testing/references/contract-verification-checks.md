# Contract verification checks

| Interface | Verify against accepted expectations |
|---|---|
| HTTP/RPC | Method/path/query/body/headers, auth context handling, status/error envelope, required/optional/null fields, enum/type/precision/date semantics, pagination and streaming frame rules. |
| Async job/event | Producer/consumer schema and version, pending/success/failure variants, correlation/idempotency fields and ordering expectations. Delivery/retry guarantees require separate real integration evidence. |
| File/data | Column names/types/order where contractual, delimiter/encoding, null/missing/units and schema evolution; preserve independent example files and real readers/writers. |
| Inference/tool | Feature order/schema, model/tool version, structured-output variants, permitted error/fallback shape and tool arguments. Schema success does not prove truthful or accurate model output. |

Keep fixtures independent: actual consumer code should use contract-governed inputs, and actual provider code must produce checked outputs. Hand-building an expected provider response in the test instead of calling the provider is not provider verification. A generated client and schema from the same new source can agree while both break existing consumers.

For consumer-driven tooling, provider states must be reproducible and scoped, verification tied to the exact contract revision, and results tied to real provider/consumer versions. Don't publish contracts/results to shared brokers or claim deployability unless that operation is authorized and counterpart compatibility is established. Local contract files are sufficient when the scoped workflow supports them.

Check additive versus breaking behavior from the actual consumer contract. An unknown field may be tolerated; a new enum value or changed numeric representation may not be. Keep security negatives and business validation in their appropriate provider unit/integration tests while checking agreed external error shapes here.

Primary reference for the consumer/provider distinction: [How Pact works](https://docs.pact.io/getting_started/how_pact_works). Use installed tooling's primary documentation before selecting version-specific matcher/verifier APIs. Using this distinction does not require adopting Pact.
