# Testing and release policy for backend and data science products

Source: user instruction, 2026-10-24. Apply pytest to Python components and the established native test runner to other languages. This document records the required release behavior; application-specific tests, CI jobs, deployment targets and credentials must be implemented for each target product before claiming enforcement.

## Required stages

| Stage | Required scope | Result and gate |
|---|---|---|
| Local development | Run meaningful unit, regression, integration/contract, boundary/error, permission and concurrency/recovery checks relevant to the change. Use an isolated local test environment for deeper security, stress/soak and DS quality experiments when the change/risk requires them. | Fix failures before proposing a release. Record the source revision, command/profile, environment and actual results. A local pass does not replace CI. |
| CI for every deployment candidate | Run the required pytest unit suite and the product's required integration/contract/regression checks in a clean, reproducible environment for the exact candidate commit/artifact. | Required jobs must pass before any deployment job proceeds. Failure, error, interruption, cancellation, timeout, a missing required suite, or a skipped required gate blocks deployment. |
| Deployed server | Run a small, fast smoke suite against the candidate server/artifact: health/readiness, correct version/configuration, authorized API access, critical dependency connectivity, and one representative safe end-to-end path as applicable. | Candidate/staging smoke checks must pass before production promotion. Run basic post-deployment verification against the promoted artifact too; failed verification prevents marking the release successful and follows the documented recovery procedure. |

The intended path is local verification → CI test gate → build/identify candidate artifact → deploy to candidate/staging environment → smoke gate → production promotion → post-deployment verification. For a product without staging, define the candidate/traffic-switch strategy and recovery before claiming an equivalent server gate.

## Pytest and suite selection

- Use `python -m pytest` with the project's actual test paths and registered profiles/markers. Do not invent markers or commands that select no required tests. Keep smoke tests distinguishable from unit/integration/deep suites.
- Preserve pytest's nonzero failure/collection/error exit codes; no collected tests is not a successful required suite. Do not append `|| true`, enable `continue-on-error` for required checks, or suppress the result in a wrapper.
- A zero exit code alone does not prove that required cases ran: review skips/xfails and validate that required suites/cases executed. Keep exceptions explicit and scoped; never silently convert a required check into an optional one.
- Keep tests deterministic and isolated. Use fixtures and test databases/queues/files; mock at external boundaries where appropriate. Verify real integration contracts in an authorized isolated environment as required.
- Assert observable behavior and meaningful failure paths. Do not add tests that merely mirror implementation, arbitrary coverage thresholds, or a requirement that every possible test run for a small change.
- For DS/GenAI changes, couple software tests with applicable data-schema, leakage, preprocessing/inference parity, model/prompt/RAG regression and quality gates. CI unit tests should not require a full training run, live paid model access or a production GPU by default. Run required release evaluations in a separately defined authorized environment when needed; record their evidence for the same candidate.

## CI/deployment enforcement

- Run the required CI profile on relevant PRs and every deployment candidate, including manual/hotfix/redeploy paths. A candidate without a successful applicable gate cannot deploy merely because a local run passed.
- In one GitHub Actions workflow, make build/deployment/promotion jobs depend on required test jobs through `needs`. Do not use `always()` or other bypass conditions on deploy/promotion jobs. Diagnostic/report-upload jobs may use unconditional execution without granting deployment eligibility.
- If deployment is in another workflow or system, verify the trusted successful test result for the exact candidate SHA/artifact and required environment/profile. A green unrelated run, different revision, or upstream workflow trigger alone is insufficient.
- Keep checks mandatory under applicable repository/environment rules. Workflow dependency wiring and repository required-status settings are separate; inspect and configure the actual settings when implementing the target pipeline. Do not claim branch protection is configured from YAML alone.
- Build/promote immutable versioned artifacts and record digest/commit plus config, data/model/prompt versions as applicable. Test and smoke results must identify the actual candidate; do not retest one image and deploy an untracked rebuilt image.
- Save useful test reports/logs and failure diagnostics with redaction. Record what ran, failed, skipped or could not be verified. Required failures block rollout even if report upload succeeds.

## Server smoke checks

- Test deployed interfaces and runtime wiring. Health checks alone do not establish a working business journey, permissions, model load, dependency access or background-worker path.
- Use read-only or dedicated synthetic/test-tenant requests appropriate to the environment. Any write exercise needs bounded fixtures, isolation and cleanup; no broad database resets, production migrations, load attacks or deep/full unit suite against live user data.
- For model-serving products, use a small approved smoke fixture to check schema, model/version loading, permissions and basic response behavior. This does not replace statistically valid model-quality or performance evaluation.
- Use explicit time bounds and report failures. Halt promotion on candidate smoke failure. If post-deployment verification fails, follow a tested recovery/rollback plan; do not blindly reverse incompatible schema/data changes.

## Handoff to future skills and current implementation state

Carry this policy into the unit-test, integration/contract, CI, CD, deployment, smoke-verification and production-readiness skills as they are created. Record target-specific commands, suite membership, failure policy, artifact lineage, staging/server URLs, secrets references, owners and actual evidence in project logic/quality/release documentation.

As inspected on 2026-10-24, `.github/workflows/orbit-desktop.yml` already runs Rust tests, `python -m pytest engine/test_worker.py -q`, interface checks and packaged-conversion checks before building installers. It is an Orbit installer workflow, not a general backend/DS production-deployment workflow. The upstream synchronization workflow does not establish such a gate. This policy update does not claim that server smoke tests or a generic backend deployment pipeline have been implemented.

References: [pytest exit codes](https://docs.pytest.org/en/stable/reference/exit-codes.html) and [GitHub Actions prerequisite jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs).
