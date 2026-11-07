# Capacity planning checks

- Name the decision, boundary, owners, horizon, lead times, regions/failure domains, accepted availability, recovery, cost, and risk constraints.
- Forecast service-demand units with peak window, workload mix, payload/tenant/geography distribution, seasonality, launches, migrations, and confidence scenarios. Reconcile prior forecasts against actuals.
- Bind service capacity to candidate/config/hardware/data and representative tests or telemetry. Record sustainable range, bottleneck, quality/correctness, and non-linear scaling.
- Include compute, memory, I/O, network, storage/retention, connections, database/cache/broker ceilings, external quotas, accelerators, model/token limits, and operational constraints where applicable.
- Calculate headroom, redundancy, maintenance and failure reserve explicitly without double-counting. Check the narrowest end-to-end tier and scale-unit granularity.
- Record required, usable, committed, and shortfall capacity, cost range, procurement/quota lead time, trigger, owner, and contingency for every scenario.
- Treat autoscaling, architecture changes, and optimization as separately verified controls. A plan or reservation is not observed deployed capacity.

Google's SRE guidance describes demand forecasting, capacity planning, and regular load testing to correlate raw resources with service capacity: [Site Reliability Engineering introduction](https://sre.google/sre-book/introduction/).
