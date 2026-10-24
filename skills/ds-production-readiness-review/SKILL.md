---
name: ds-production-readiness-review
description: Assess evidence for releasing a specific backend or data science candidate to a named environment or promotion stage. Use before candidate deployment, production promotion, or release sign-off to verify requirements, immutable artifact identity, mandatory CI pytest and server smoke gates, quality/security/recovery evidence and operating ownership. Produce gate-by-gate outcomes and concrete blockers. Do not treat this as deployment authorization, a generic architecture score, or a substitute for missing tests or benchmarks.
---

# Backend and Data Science Production Readiness Review

Determine whether the exact candidate has the evidence required for the next release stage. Keep documented policy, configured enforcement and observed execution distinct.

## Establish the candidate and release stage

- Read applicable instructions, PROJECT_LOGIC.md, accepted SRS/NFRs/contracts/design, testing/release policy, release plan and relevant evidence. Identify environment and whether the decision concerns candidate deployment, staging promotion, production promotion or post-rollout verification.
- Record immutable source/artifact digest and config/schema/data/model/prompt versions where applicable. Link each report to the actual candidate, environment/profile, time and scope; reject unrelated, stale or unverifiable evidence as proof of a required gate.
- Identify current known risks, rollback/recovery limitations, owners and required decision authority. Respect authorization already supplied, but do not deploy or change external systems during a review-only request.
- Ask up to three highest-impact questions if needed. Continue independent evidence review while blocking only the affected release stage. Never infer sign-off from silence or a completed checklist.

## Assess required gates

Read [release-gates.md](references/release-gates.md). For every applicable gate record required basis, candidate evidence, scope/limitations, decision and owner.

- Verify accepted behavior and contract compatibility; known severe correctness, authorization, data-integrity or scientific-validity defects need a resolved disposition before the affected release.
- Verify thorough relevant local evidence where required and mandatory CI pytest unit/required integration results for Python candidates. Failure, interruption, cancellation, timeout, missing required suites or skipped required gates block deployment. A green status alone does not prove required tests ran.
- Check actual pipeline/deployment dependency enforcement, immutable artifact lineage and relevant repository/environment rules when accessible. A YAML job, a local pass, an unrelated commit or an unexecuted plan does not establish the CI gate.
- Require basic safe smoke checks on the candidate server before production promotion. Require post-deployment verification of the promoted artifact before marking rollout successful. A smoke check is not available before its environment exists: distinguish a candidate-deployment plan from actual promotion evidence and do not require future-stage results prematurely.
- Assess applicable model/data/prompt/RAG quality, leakage/inference parity, permission/grounding and artifact-version evidence separately from unit tests and HTTP success. Mark ML criteria N/A for ordinary backends with a reason.
- Review measured NFR evidence, dependency/capacity limits, security/privacy/egress, secrets/configuration, backup/restore and migration integrity, operational signals/runbooks/ownership and recovery compatibility as applicable. Missing evidence is unknown, not an invented pass or a fabricated vulnerability.

## Decide without weakening mandatory controls

- Use gate outcomes PASS, FAIL, UNKNOWN, NOT YET DUE or NOT APPLICABLE with evidence/rationale. NOT YET DUE is only for a later stage; UNKNOWN/FAIL on a gate required now blocks that stage.
- State READY FOR [stage] only when all applicable gates required for that stage pass and authorized governance requirements are met. Otherwise state NOT READY with exact blockers; separately list independent preparation that can proceed.
- Keep nonblocking recommendations distinct from blockers. For documented risk exceptions, record authorized owner, scope, justification, expiry/revisit and residual exposure. Do not silently waive the user's mandatory passing CI or smoke gates; a change to that policy needs explicit source authority.
- Do not turn hypothetical risks or a preferred architecture pattern into new release obligations. Do not claim blanket compliance, future capacity, model quality or successful recovery from design descriptions alone.

## Deliver and preserve the decision

Use [readiness-review.md](assets/readiness-review.md). Report candidate/stage, gate matrix, actual checks, missing evidence, known risk dispositions, bounded remediation and re-review triggers.

- Include source/evidence references, local/CI/server results and their candidate match. Redact credentials, sensitive records and private payloads.
- If documentation maintenance is requested, persist the readiness record in the project's release records and link from its logic/release index. Preserve older candidate decisions and identify what changed.
- Hand off the release prerequisites and safe recovery plan; a READY assessment does not execute deployment, override user permission or establish future-stage success. Verify specialist skill availability before invoking it.
