# Measurement contracts and evidence

## Define the population before the statistic

- Identify the exact journey, caller and environment; start/end timestamps; eligible requests/jobs/records; logical operation versus attempts; units; and observation window.
- Record traffic/input distributions, arrival versus closed-loop concurrency model, peak/burst duration, dependency and warm/cold/cache state. Define how the test avoids silently reducing offered load when the system slows.
- Define invalid/unauthorized requests, saturation rejections, retries, timeouts, cancellations, partial outputs, cached responses and fallback outcomes explicitly. Do not remove failed/slow events from every denominator and then claim the system is fast and available.
- Report latency and useful-success together. If latency is measured only for completed successes, keep that condition explicit and pair it with eligible-population success/error/timeout measures and pending acceptance policies.
- Keep per-journey distributions where aggregation would hide important cases. Do not average percentiles across hosts/windows or add component p95 values to assert end-to-end p95.
- Define minimum sample support, duration, repeated runs or uncertainty assessment appropriate to the claim; keep unsupplied numeric test criteria pending rather than inventing them. Insufficient evidence is not a pass.

## SLI, SLO and service commitments

An SLI is the defined measurement; an SLO is a target over a defined window; a contractual/SLA commitment has separate business and contractual consequences. Do not invent a contract or treat a requested SLO as demonstrated capability.

For a request-based success objective, define which logical requests are eligible and which outcomes are good; the observed success ratio is good eligible events divided by all eligible events. If an objective and the population are established, a bad-event budget can be derived from that same population and window. It is not an allowed-downtime figure.

For a time-based availability objective, define service periods, observable usable-state criteria, partial outage treatment, denominator, timezone and approved exclusions. Use the actual calendar/service window when computing time allowances. Do not assume a 30-day month or exclude maintenance without a source-backed policy.

Describe no-traffic windows, missing/corrupt telemetry and boundary gaps; do not silently count unknown periods as successful. Define who owns target changes and what evidence the release or operating decision needs. Leave detailed alert thresholds and error-budget operating policy to the relevant workflow unless requested.

## Recovery and data integrity

- RTO measures the accepted time to restore a defined capability after a defined disruption boundary. Specify whether detection, investigation, failover and verification are included.
- RPO defines the accepted data-loss window/cutoff for that failure scenario. Backup frequency alone does not establish achievable RPO, successful restore, or acknowledged-write integrity.
- Specify restore source, corruption/dependency scenario, consistency/integrity checks, reconciliation, verification and owner. Keep allowed lost transactions and degraded-mode behavior linked to accepted business policy.

## DS/GenAI and resource evidence

- Define dataset/corpus/model/prompt/config versions, deployment population, split/isolation, metric calculation/aggregation, baseline, slice support, uncertainty and decision rule before a quality pass/fail claim.
- Keep offline quality, online useful task success, latency/throughput and token/resource/cost measures separate but coupled through guardrails. A faster model/quantization/cache change needs quality and permission evidence, not a speed claim alone.
- Define currency, time period, included compute/storage/network/provider/labor costs as relevant, idle/shared allocation and retries/failures. Unit cost per useful outcome differs from cost per attempted request or generated token.
- Label memory/capacity/cost estimates with model/workload/version assumptions and measurement gaps. Verify current authoritative prices/specifications when using real values. Do not infer GPU concurrency or latency from weight size alone.

## Verification states and handoff

For Python deployment candidates under the user's testing policy, record three profiles: thorough relevant local verification, mandatory CI pytest unit/required integration checks, and basic candidate/production-server smoke checks. Link the exact commit/artifact, commands, environment, required suite membership, reports and actual pass/fail state. A local pass cannot replace the CI gate; missing/no-test/skipped required gates do not establish release eligibility. Deployed health/readiness and a safe representative journey verify runtime wiring without running deep/destructive suites against production data. Treat these as accepted policy while keeping application-specific implementation and observed enforcement explicit.

| State | Meaning |
|---|---|
| Draft/proposed target | Candidate behavior/threshold with rationale; not accepted by default. |
| Source-supplied, incomplete contract | A value or expectation is known; measurement/workload/policy fields remain unresolved. |
| Accepted, unverified | Decision evidence exists; empirical feasibility or acceptance verification has not been established. |
| Verified for stated conditions | Actual evidence meets the specified decision rule for the recorded scope; not a universal production guarantee. |
| Insufficient evidence / not run | Required measurement conditions, sample support, data or authorization are unavailable. |

Keep decision state and verification state as separate fields, not one status that loses history. Distinguish environment/setup failures from demonstrated product failures. Persist relevant accepted targets and unanswered policy questions in the project's logic/quality documents; hand their IDs and revisions to architecture, coding, testing and operations.

Use these primary references as guidance when needed, not blanket certification criteria:

- [Google SRE: Implementing SLOs](https://sre.google/workbook/implementing-slos/).
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/).
- [OWASP ASVS](https://owasp.org/projects/asvs).
- [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).

Inspect the applicable version/source when making a version-specific or formal compliance claim. Keep evidence plans separate from actual executed checks.
