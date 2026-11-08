# Model evaluation and release-gate checks

- Define decision, intended/excluded use, unit/environment, affected groups, error consequences, human role, baseline, exact candidate identities, owners and authority.
- Prespecify each metric/rubric, population/slices, direction, threshold/margin, sample/uncertainty, severity and failure action; keep quality categories separate.
- Use rights-cleared, provenance-bound, leakage-safe independent data with label quality, time, weights, duplicates/contamination and locked final evaluation.
- Cover normal, rare/high-impact, boundary, missing/corrupt, OOD and prior-failure cases; choose task-appropriate quality, calibration, feasibility, retrieval or generative evidence.
- Govern human and model judges through instructions, blinding/randomization, agreement/adjudication and bias calibration; judge confidence is not truth.
- Report effect, uncertainty, missingness, practical significance, multiplicity and slice distributions; evaluate robustness, fairness, privacy, safety/security and safe failure as mapped.
- Measure end-to-end performance/cost and API, fallback and degraded compatibility under the accepted serving workload; offline quality is not online proof.
- Bind every required gate and exception to the immutable deployable artifact, runtime, monitoring and rollback. Missing/skipped/stale/failed gates block release by default.

NIST's AI RMF [Measure function](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and 2026 [ARIA Evaluation Planning Manual](https://www.nist.gov/publications/aria-evaluation-planning-manual-elements-aria-style-ai-evaluations) provide primary risk-based evaluation references. Tailor the evaluation to the accepted context and risk.
