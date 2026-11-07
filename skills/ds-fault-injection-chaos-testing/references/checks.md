# Fault injection and chaos testing checks

- Name resilience hypothesis, target/candidate/config, environment, workload/data, steady-state outputs and invariants, experiment and recovery owners, authority and decision.
- Define one fault variable, target, magnitude, duration, cohort, observation window, expected response, blast radius, aborts, independent stop, cleanup and recovery deadline.
- Establish a stable representative baseline and working telemetry; validate the mechanism in lower risk first. Production scope must be explicit.
- Protect tenants, shared dependencies, third parties, state, cost and operators. Abort on integrity/security harm, escaped impact, missing telemetry or inability to stop.
- Verify the injection actually occurred and measure service outputs, amplification, queues, dependencies, fallbacks, data/model invariants, detection and recovery independently.
- For state, jobs and ML, cover quorum/fencing, duplicates/checkpoints/publication, GPU/provider/model/feature/index failures, fallback quality and stale workers.
- Remove the fault, reconcile partial work, verify steady state and cleanup, and classify supported/falsified/inconclusive with remediation and retest ownership.

The [Principles of Chaos Engineering](https://principlesofchaos.org/) describe measurable steady state, real-world variables and minimizing blast radius; explicit task authorization and target safety still govern execution.
