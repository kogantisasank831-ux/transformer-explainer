# Contract checks

| Interface | Questions to resolve |
|---|---|
| Request/response | Which caller can perform the operation on which resource? What validates every trust boundary? What are the exact success/error outcomes and persistence effects? |
| Files | What content, encoding, sizes and counts are accepted? How are paths/names isolated, ownership checked, partial uploads cleaned, and downloads authorized? |
| Async jobs | When is acceptance durable? Which states/transitions and terminal outcomes exist? Who may cancel/retry, and what happens when start/completion/cancel race? |
| Idempotency | What is the caller/key scope, payload equivalence, window anchor/refresh/expiry and conflicting reuse behavior? Are retries attempts of one logical operation? |
| Events/webhooks | Who authenticates the sender? How are signatures/replays, duplicates, order, retries, dead letters and schema compatibility handled? |
| Inference | What feature/preprocessing/model versions and shapes are compatible? How are invalid values, missing inputs, uncertainty, abstention and resource limits represented? |
| RAG/tools | Do citations identify authorized evidence versions? Can a tool enforce caller authority independently of generation? How are partial effects reconciled? |

Treat additive changes as potentially breaking when consumers reject unknown fields/enums or depend on ordering/defaults. Distinguish documented compatibility from observed client behavior. Inspect middleware and service/storage checks before claiming authorization is absent.

Use machine-readable OpenAPI/JSON Schema/event schemas only in the project's supported versions; avoid mixing dialects. Mark examples as synthetic and constraints as supplied, proposed or unresolved. For Python, Pydantic can implement validated boundaries when it fits the project, but a Python type alone does not establish wire validation.

Contract tests should establish observable semantics and consumer compatibility. Unit and schema tests cannot alone establish real integration, model quality, performance or security. Preserve their planned/executed status and the exact candidate revision. Keep live providers and production data out of default unit tests.
