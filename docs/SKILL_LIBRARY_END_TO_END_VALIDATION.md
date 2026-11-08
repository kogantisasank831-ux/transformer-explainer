# Skill library end-to-end validation

Validated: 2026-11-08  
Scope: the 91 backend and data-science engineering skills, repository routing guidance, project-memory templates, and end-to-end delivery gates.

## Assessment

The library can guide a project from SRS review through implementation, testing, release, and production operation after the delivery-gate integration described in this report. The individual skills already covered the required engineering controls. The material gap was orchestration: their order and stop conditions were distributed across many workflows. The lifecycle now makes those transitions explicit and machine-checkable.

Result: 91/91 skill packages passed metadata validation, all 91 were discovered without duplicate names or broken relative resource links, all 20 lifecycle-critical skills were present, and 76/76 executable lifecycle scenarios passed.

This assessment means a coding harness has a complete procedural path. It does not mean every future SRS is complete, every repository is production-ready, or an environment has passed tests. Those conclusions require project-specific evidence.

## Validation method

The validation combined four checks:

1. **Catalog structure:** discover every skill by frontmatter name; require independent package metadata, checks reference, and output record; verify all lifecycle-critical skills exist.
2. **Workflow trace:** follow one product from SRS through G0–G7 and inspect handoffs among requirements, design, planning, coding, testing, CI, readiness, deployment, smoke, and monitoring.
3. **Executable policy tests:** exercise incomplete and complete SRS coverage, conditional slices, coding prerequisites, exact-candidate release evidence, failed/skipped/stale suites, rollback/monitoring, and post-rollout verification.
4. **Representative product scenario:** apply the gates to a backend plus AI ticket-routing API with deliberately missing authority, duplicate, timeout, partial-failure, state, contract, privacy, NFR, model fallback, acceptance, and monitoring decisions.

## Lifecycle coverage

| Project need | Primary coverage | Validated handoff |
|---|---|---|
| Understand a new or existing product | Requirements Analysis; Repository Assessment | Target component, evidence revisions, intended-versus-observed behavior, and current state enter G0. |
| Find unanswered SRS and process questions | SRS Gap Analysis and Business Process Validation | Complete process/state/scenario review and question register feed accepted logic into G1. |
| Define ordinary backend and DS/AI design | System Architecture; NFRs; API Contract Design; threat/data/ML/RAG/agent specialists | Accepted logic IDs trace into architecture, contracts, failure behavior, and measurable gates in G2. |
| Prepare coding without guesses | Implementation Planning; Test Strategy; Project Setup | Dependency-ordered slices, tests, blockers, and active handoff produce G3. |
| Build maintainable behavior | Production Coding Practices; Code Review; specialist implementation skills | G1/G2/G3 are checked before domain behavior; local evidence produces G4. |
| Test the candidate | Unit, Integration, Contract, E2E, Regression, Fuzz, Security, Performance, Model/Data evaluation | Mandatory unit plus applicable suites are tied to the exact candidate in G5. |
| Release safely | Build/Packaging; CI/CD; Production Readiness; Smoke; Deployment; Rollback | Immutable identity, pipeline enforcement, smoke, rollback, and post-rollout verification produce G6. |
| Operate and improve | Observability; SLOs; Runbooks; Incident Response; AI Production Monitoring | Deployed identity and real outcomes produce G7 and reopen earlier gates when behavior changes. |

## Executable scenarios

The validator contains 76 focused pytest cases. It verifies:

- omission of each one of the 20 SRS coverage areas blocks G1;
- core SRS areas cannot be declared not applicable;
- optional non-applicability requires a concrete reason;
- an open critical question blocks its affected scope;
- a conditional gate permits only its explicitly named independent slice;
- missing, blocked, or not-applicable G1/G2/G3 blocks domain coding;
- passing unit tests alone cannot authorize deployment;
- every applicable failed, skipped, missing, stale, or candidate-mismatched suite blocks deployment;
- non-applicable model or specialist evidence requires a reason;
- candidate/source/artifact identity, rollback readiness, and monitoring readiness are mandatory;
- post-deployment smoke is required before production verification.
- purpose-specific skill resource names are allowed while missing metadata and broken relative links are rejected.
- a backend plus AI ticket-routing project remains blocked with unresolved process and model decisions, advances after accepted G1–G3 evidence, rejects unit-only release evidence, and verifies the complete candidate lifecycle.

The representative ticket-routing SRS begins at `G1_SRS_LOGIC=BLOCKED`. It cannot move to domain coding while authority, state transitions, duplicate behavior, provider failure/fallback, contracts, privacy, quality targets, and acceptance oracles are unanswered. After those decisions are accepted and transferred into project logic, a named independent slice can pass G1, then G2 and G3. At release time, a local and CI unit pass still fails G5 until applicable integration, contract, regression, security, model-quality, candidate identity, and smoke evidence are present.

## Controls added by this validation

- One G0–G7 lifecycle defines ordered entry, evidence, stop conditions, and re-entry on change.
- `PROJECT_LOGIC.md` stores durable gate status, scope, blockers, evidence, owner, and next gate.
- `WORK_PROGRESS.md` stores the current gate and exact next action for resumption.
- SRS validation owns `G1_SRS_LOGIC` and slice readiness.
- Implementation planning owns `G3_PLAN_TEST_STRATEGY` and the executable handoff.
- Production coding checks G1/G2/G3 before domain behavior and records local verification at G4.
- Project setup may create only a neutral scaffold while G1 is blocked.
- Production readiness records `G5_EXACT_CANDIDATE`; unit-only or stale evidence cannot pass it.

## Practical limits

- No finite checklist guarantees that every domain-specific scenario has been imagined. Stable coverage areas, explicit non-applicability, scenario walkthroughs, traceability, and accountable acceptance make omissions visible and reviewable.
- A harness must actually read `AGENTS.md` or `CLAUDE.md`, the component project logic, current progress, and the selected skills. A tool that ignores repository guidance cannot receive these controls automatically.
- Human product, legal, security, privacy, and risk owners must answer and accept decisions within their authority. The skills do not manufacture approval.
- Integration, security, performance, recovery, model-quality, deployment, and monitoring claims require the real applicable services and environments. Local simulations remain scoped evidence.
- The library supports ordinary backends without requiring ML. DS/ML/RAG/agent gates activate only when those components exist, with a recorded reason when an optional specialist gate is not applicable.

## Repeatable checks

From the repository root, run:

```bash
python -m pytest -q skills/validation/test_end_to_end_skill_validator.py
python skills/validation/end_to_end_skill_validator.py --repo-root . --json
```

The structural command expects all 91 portable skill packages in `skills/`. The behavioral suite is deterministic and does not call production systems.
