# Strategy checks

## Select boundaries and meaningful oracles

| Risk/surface | Verification evidence |
|---|---|
| Domain/transform | Accepted examples plus boundary/invalid/invariant cases. Derive expected values independently; don't mirror implementation branches. |
| API/worker/storage | Schema/error/permission contracts, real transaction and constraint behavior, duplicate/retry/partial-failure cases, migrations and consumer compatibility. An in-memory fake cannot prove database isolation. |
| Concurrency/recovery | Controlled interleavings, cancellation/cleanup, worker restart/replay, state/effect count and consistency. Repeated sleeps or a passing loop do not establish absence of races. |
| Security/privacy | Tenant/object access, untrusted input boundaries and redaction at relevant layers; specialist security testing needs its own scope/environment and does not become a generic unit-test claim. |
| NFR/performance | Match accepted workload/population/window, success/failure denominator, percentile and resource budget. Define isolated benchmark/load tasks; don't invent thresholds or use flaky unit-test stopwatch assertions. |
| Data/ML/GenAI | Schema/quality/leakage/preprocessing parity, independent evaluation data, model/prompt/retrieval versions, representative negative/adversarial cases and accepted quality/fallback criteria. Pinning random seeds does not guarantee provider-level determinism. |

## Gate integrity

For Python, require the applicable `python -m pytest` unit suite in CI on every deployment candidate and additional required integration/contract/regression checks. Preserve nonzero failure/collection codes and verify meaningful required cases executed; zero exit alone may include only skipped/xfail cases. Never use `|| true`, continue-on-error or unrelated green runs to satisfy a required gate. For native projects preserve their established runner and equivalent enforcement.

Specify exact commit/immutable artifact, config and relevant data/model/prompt identity on evidence. A rebuilt image or new config/model may require fresh relevant evidence. Unit/CI success comes before candidate deployment; safe server smoke must identify the deployed version and exercise an authorized representative path plus dependencies as applicable. Health alone is insufficient. Post-deployment verification records release success or invokes documented recovery. Do not run deep/full unit/load suites against live users.

Keep failing, blocked, not run, not yet due and not applicable separate. N/A requires a scope reason. Missing tooling is not a pass; a later-stage check can be not yet due for the current stage. Record enforcement separately: workflow dependencies, cross-workflow trusted candidate matching and repository required-status configuration are distinct.

Primary source: [pytest exit-code semantics](https://docs.pytest.org/en/stable/reference/exit-codes.html). Confirm installed tool/profile behavior rather than inventing configuration.
