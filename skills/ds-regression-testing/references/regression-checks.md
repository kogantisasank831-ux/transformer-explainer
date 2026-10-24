# Regression checks

| Change/risk | Preserve with evidence |
|---|---|
| Software defect | Minimal trigger, accepted expected result, original failure mechanism, before/after identities and nearby negative/boundary cases. |
| Refactor/dependency | Stable contracts, errors/defaults/order, side-effect counts, persistent formats and supported consumers. Differential comparison supplements independent rule assertions; old code can also be wrong. |
| Data/ML | Row/feature alignment, preprocessing/schema, leakage boundaries and versioned representative evaluation data. Software/schema regressions and statistical quality gates are distinct. |
| Prompt/RAG/agent | Versioned prompts/retrieval fixtures/tool traces, permissions and structured outcomes; deterministic stubs isolate plumbing while independent relevant evaluations establish actual behavior. |
| Numerical/performance | Accepted tolerance/workload/hardware/window and comparable measurements. Do not use an arbitrary stopwatch unit assertion or widen a tolerance after failure without accepted rationale. |

Golden/snapshot baselines need source/acceptance, stable meaningful fields and deliberate review of differences. Normalize only irrelevant volatility; don't strip authorization fields, errors, order or semantic content to force agreement. Do not regenerate expected output from the current implementation and call it independent proof.

Control clocks, random input, dependency responses and interleavings. Reproduce the original condition; a test can pass while never reaching the failing path. Retain normal runner failure status and compare actual outputs, not just an expected exception raised by the test itself.

For known bad/good comparisons use isolated modules/worktrees or fixtures and make import identity explicit. Keep the product test asserting accepted behavior; don't make a suite green by treating the known current defect as its expected output. Supplemental harness checks can verify a bad implementation fails, but do not replace the real regression.

Primary pytest starting point: [test/package layout and imports](https://docs.pytest.org/en/stable/explanation/goodpractices.html). Confirm the project runner/version and [exit semantics](https://docs.pytest.org/en/stable/reference/exit-codes.html); no-tests and skipped mandatory cases cannot establish protection.
