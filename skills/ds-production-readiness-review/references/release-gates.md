# Stage-aware release gates

| Gate | Evidence and important distinction |
|---|---|
| Candidate identity | Immutable artifact/source/config/schema/data/model/prompt references match every required result. A rebuilt untracked image is another candidate. |
| Behavior/contracts | Accepted rule/contract cases, important failures/permissions/concurrency and compatibility evidence for this change. A report that merely lists tests is insufficient. |
| Local verification | Relevant thorough local results and environment/profile; deep tests appropriate to risk use isolated fixtures. Local evidence cannot replace required CI. |
| Mandatory CI | Required pytest unit/integration/regression suites for Python passed on the candidate; no-test/skipped/failed/missing gates do not qualify. Verify dependency wiring and actual required checks separately. |
| Candidate smoke | Deployed candidate version, readiness, permissions, dependencies and safe representative journey passed before promotion. Health alone is insufficient. |
| Post-rollout | Verification identifies the promoted artifact and environment. Candidate-deployment readiness can plan it; final rollout success requires actual results. |
| DS/GenAI validity | Applicable dataset/split/rubric/baseline/slice support, preprocessing/inference parity, provenance, quality and permission/grounding evidence; software tests alone do not prove it. |
| Operations/recovery | Applicable objectives, workload evidence, migration/coexistence, restore/cutover/rollback tests or scoped required evidence, redacted observability and accountable ownership. |

Do not require a particular cloud, orchestrator or number of services to pass. Apply accepted constraints and actual risk. Inspect evidence status and limits: unknown capacity can block a capacity commitment without proving a system defect.

A failed/missing required CI gate blocks candidate deployment; a failed/missing candidate smoke blocks promotion; missing post-rollout checks block a successful-rollout conclusion. Do not mark a later-stage gate PASS merely because it is not yet due. Record exceptions for nonmandatory risks explicitly without bypassing the user's mandatory test policy.

Do not run intrusive verification against production as part of an evidence review. If live checks are requested, use only the authorized safe scope and report actual outcomes. Keep rollback conditional on data/schema compatibility; stop and use the documented recovery path when reversal is unsafe.
