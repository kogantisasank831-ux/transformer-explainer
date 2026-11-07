# Rate limiting and backpressure checks

- Define protected resource, trusted subject/tenant, operation, cost unit, scope, window, sustained rate, burst, concurrency, policy owner, override and exhausted behavior.
- Select token bucket, pacing/leaky bucket, fixed/sliding window, weighted quota or concurrency control from accepted semantics. Record distribution, atomicity, time, precision and failure tradeoffs.
- Enforce on every costly path with authenticated keys, normalized cost, bounded cardinality, expiry, privacy-safe identifiers and tenant isolation.
- For HTTP, distinguish client rate exhaustion from service overload; implement standard `429` and `Retry-After` semantics and treat draft `RateLimit` fields as versioned advisory metadata.
- Bound queues, bytes, age, pools and worker concurrency; admit before expensive work; propagate pressure and cancellation upstream; prevent retry amplification.
- Define retry/idempotency budgets, jitter, priorities, fairness, load shedding, exemptions, audit and limiter-store outage behavior.
- Test bursts, sustained use, boundaries, races, replicas, clock skew, hot keys, weighted cost, fairness, full queues, retries, failure and recovery against actual protected-resource use.

Use the IETF definitions for [429 Too Many Requests in RFC 6585](https://datatracker.ietf.org/doc/html/rfc6585#section-4) and [Retry-After in RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110#section-10.2.3). The current [RateLimit header-fields draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) is evolving and must be version-checked.
