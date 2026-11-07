# Progressive delivery checks

- Bind immutable baseline/candidate artifacts and config/schema/data/model identities, target, hypothesis, eligible population, maximum exposure, invariants, owner and authority.
- Select canary, blue-green, shadow, cohort or flag strategy from state, routing, capacity and rollback needs. Define stickiness, async work and side-effect boundaries.
- Make baseline and candidate populations comparable across topology, tenants, workload/input distribution, warm/cache state, dependencies, retries, autoscaling and time; record confounders.
- Predefine steps, dwell/warm-up, minimum evidence, maximum duration, promotion, pause and abort gates for service, dependency, correctness, security, business, cost and applicable model quality.
- Block automatic promotion on missing, stale, biased or insufficient telemetry. Hard integrity failures stop immediately; small samples do not prove safety.
- Verify actual traffic/cohort and replica exposure. Prevent shadow writes and double-processing; include jobs, messages, caches and background workers in the impact boundary.
- On abort, remove or drain exposure, reconcile in-flight work and side effects, verify baseline capacity and recovery; after promotion verify exact identity, stabilization and safe retirement.

Google SRE's [canarying releases](https://sre.google/workbook/canarying-releases/) guidance describes limiting release cost through staged comparison; implement it with the selected controller and routing platform's official semantics.
