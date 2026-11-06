# Cache engineering checks

- Document authoritative source, acceptable staleness, consistency point, miss/outage behavior, data classification, and completion/invalidity events.
- Include tenant, authorization/policy, locale, representation, schema, query, feature, model/prompt/retriever, and config dimensions in keys as applicable.
- Define source/cache write order, invalidation loss, TTL/jitter, negative caching, namespace rotation, replay, and reconciliation. TTL alone is not immediate revocation.
- Prevent stampedes with bounded ownership-aware coordination and protect the source from fallback floods.
- Estimate memory including metadata; test max-memory and eviction behavior. Cache values are disposable unless the design explicitly creates a durable system with separate guarantees.
- Verify serialization compatibility and reject unsafe executable formats. Do not log sensitive keys or payloads.
- For semantic or inference caches, evaluate correctness/quality, safety policy, privacy, model/config version, and tenant isolation in addition to latency.

Consult official documentation for the chosen cache. Redis users can review the current [cache-aside guidance](https://redis.io/docs/latest/develop/use-cases/cache-aside/) and eviction/expiration behavior for their deployed version.
