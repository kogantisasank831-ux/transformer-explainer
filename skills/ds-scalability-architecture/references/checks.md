# Scalability architecture checks

- Ground the design in accepted workload, growth, latency/throughput, consistency, availability/recovery, residency, tenant, cost, and operational requirements.
- Map end-to-end flows, state ownership, partition keys, pools/queues, connections, failure domains, shared stores, quotas, and measured constraints before changing boundaries.
- Compare vertical and horizontal scale, decomposition, partitioning, replication, caching, batching, async work, locality, and demand shaping with bottleneck movement and cost.
- For partitions, test skew, hot keys/tenants, cross-partition operations, rebalancing, resharding, stale routing, replica lag, failure, and tenant isolation.
- Bound fan-out, queues, retries, and concurrency. Specify overload, degraded mode, dependency failure, regional failure, and recovery behavior.
- For applicable DS/ML paths, cover data/model/index locality, training versus serving, accelerator scheduling, batching, transfers, collectives, loading, and fairness.
- Define reversible migration slices, compatibility, reconciliation, observability, capacity/correctness gates, and owner. Design is not measured production scalability.

Google SRE's discussion of [cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) provides primary guidance on overload, capacity, queues, and graceful degradation; verify selected platform behavior against its official documentation.
