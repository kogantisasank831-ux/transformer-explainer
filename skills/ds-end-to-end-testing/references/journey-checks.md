# Journey checks

| Journey surface | Observable evidence |
|---|---|
| API/CLI | Actual request/process invocation, identity and authorization, response/error contract, durable outcome and relevant exit/output semantics. Direct service calls alone exclude transport wiring. |
| UI | Actual navigation and supported user interactions with stable semantic locators; assert meaningful state and accessible controls. Screenshots alone do not establish backend behavior. |
| Async | Submission through real entry point, actual queue/worker path, completion/failure, persisted state and retrieval. Bound polling by a monotonic deadline and keep last observed state in safe diagnostics. |
| Tenant/effects | Two independent synthetic scopes, overlapping IDs where appropriate, rejected cross-scope reads/mutations, separate receiver/store counts for notifications or other effects. |
| Data/model | Representative synthetic documents/features, independent expected schema/order/content and exact model/config. A controlled model stub is valid for deterministic plumbing tests only if the claim names it. |
| Teardown | Stop test-owned workers/servers, join processes/threads, release clients and delete only owned data; preserve cleanup failure as evidence. |

Choose the narrowest environment that actually crosses the requested boundaries. A loopback HTTP test with real worker/storage can be application E2E for that stack; it does not establish TLS/proxy/cloud deployment behavior. A test-client in-process journey may be useful but must not claim network/server startup verification.

Handle asynchronous completion as a business state, not a timing guess. A timeout or unexpected terminal error fails the journey; it is not an optional skip. Do not assert a universal latency threshold unless it is an accepted measurement contract; a test timeout is a deadlock budget, not a performance benchmark.

Preserve the project's native Python/browser/CLI runner and required plugins. Select actual paths/profiles and inspect collection. For pytest, [fixture lifecycle guidance](https://docs.pytest.org/en/stable/how-to/fixtures.html) is a primary starting point; consult the project's browser/client documentation before using version-specific APIs.
