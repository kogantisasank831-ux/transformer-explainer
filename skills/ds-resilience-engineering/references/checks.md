# Resilience engineering checks

- Map critical user, job and data flows; state owners; dependencies; failure domains; shared quotas; owners; and accepted availability, consistency, recovery and cost.
- Cover crash, slow, partial, stale, corrupt, overload, network/DNS/identity/storage/control-plane, data/model/GPU and operator failures with invariants and degraded semantics.
- Propagate deadlines and bounded dependency timeouts; cancel or fence work and reconcile ambiguous completion. A timeout does not stop the remote effect.
- Bound retries by attempts and time with jitter, idempotency and server dedupe; prevent layered amplification and use retry budgets during overload.
- Bound queues, concurrency and pools; apply fair backpressure/load shedding, bulkheads and measurable circuit behavior before saturation.
- Prove redundancy independence, quorum/fencing, lag, failover and reintegration. Make degraded output explicit, compatible, observable and time-bounded.
- Test failure and recovery paths with work-amplification, queue, data and business invariants; separate controlled fault experiments and DR evidence from design claims.

Google SRE's [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) discusses overload, retries and load shedding; apply controls to the target system's accepted semantics and measured limits.
