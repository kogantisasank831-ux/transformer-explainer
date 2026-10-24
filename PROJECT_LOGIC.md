# Repository and engineering toolkit logic

Last reviewed: 2026-10-24. Scope: repository navigation and the shared engineering toolkit. This is not a completed specification of every application in this repository.

## Evidence and component boundary

| Evidence | What is established | Limit |
|---|---|---|
| Root README.md | Describes the Transformer Explainer browser-based learning application. | This change does not audit its implementation or deployment. |
| Repository root directories | `src/`, `static/`, `AlphaLink/`, and `Orbit/` are present. | Directory presence alone does not verify application features or readiness. |
| User instructions, 2026-10-21 | Keep reusable engineering skills in this repository's `skills/`; cover backend and data science; add agent guidance and project-logic documentation. | Future catalog entries are not implemented until their packages exist. |

## Current toolkit behavior

| Rule ID | Rule | Status / evidence | Location / verification |
|---|---|---|---|
| TOOLKIT-001 | Store completed reusable skills beneath `skills/<skill-name>/`. | Confirmed user requirement. | `skills/README.md`; package metadata and link checks. |
| TOOLKIT-002 | Support ordinary backend work and DS/ML/GenAI work through applicable profiles. | Confirmed user requirement. | `skills/ds-requirements-analysis/`; backend-only and combined-workload scenario review. |
| TOOLKIT-003 | Keep agent instructions concise and load skill details only when relevant. | Implemented organization; detailed wording subject to user review. | `AGENTS.md`, `CLAUDE.md`; link and routing review. |
| TOOLKIT-004 | Keep project-specific rules separate from generic workflows. | Implemented organization; detailed wording subject to user review. | This index and `skills/templates/PROJECT_LOGIC.md`. |
| TOOLKIT-005 | Preserve explicit unknowns and acceptance status; do not infer approval or fabricate quality targets. | Implemented workflow control. | Requirements skill, baseline template, and scenario review. |
| TOOLKIT-006 | Persist reviewed SRS logic and resolved questions in the target project's logic document so the coding harness can use them. | Confirmed user requirement, 2026-10-21; no project SRS supplied in this task. | `AGENTS.md`, logic template, and requirements skill handoff procedure. |
| TOOLKIT-007 | Assess existing backend/DS code with scoped evidence, compare it with accepted logic, and prioritize findings without inventing runtime results or changing business acceptance. | Implemented workflow for catalog skill 2, requested as the next skill. | `skills/ds-repository-assessment/`; metadata/link checks and isolated scenario reviews. |
| TOOLKIT-008 | Design backend/DS systems from reviewed intent, compare consequential alternatives, and preserve contract/failure decisions and logic/design revisions for coding. | Implemented workflow for catalog skill 3. | `skills/ds-system-architecture/`; metadata/link checks and isolated architecture scenarios. |
| TOOLKIT-009 | Define measurable backend/DS quality requirements with source targets, measurement contracts, acceptance, feasibility and verification states; carry accepted constraints into project logic. | Implemented workflow for catalog skill 4. | `skills/ds-nonfunctional-requirements/`; metadata, resource-link and specification review. |
| TOOLKIT-010 | Require thorough relevant local tests, mandatory pytest CI gates for Python deployment candidates, and basic deployed-server smoke verification, with failures blocking release progression. | Confirmed user policy, 2026-10-24; target-specific pipeline implementation and enforcement must be verified. | [Testing/release policy](docs/TESTING_AND_RELEASE_POLICY.md); existing Orbit pytest installer check is not a generic backend/server deployment gate. |
| TOOLKIT-011 | Create subsequent catalog skills in batches of five, retaining separate packages and validation per skill. Catalog entries 5–9 cover contracts, architecture review, implementation planning, release readiness and project setup. | Confirmed batching instruction, 2026-10-24; implemented workflow packages, not an application deployment. | [91-skill catalog](skills/CATALOG.md); per-skill metadata/link checks and isolated scenario validation. |
| TOOLKIT-012 | Implement catalog entries 10–14 as distinct coding, review, refactoring, debugging and concurrency workflows, grounded in accepted logic and proportionate behavioral verification. Keep review-only scope, intentional behavior changes, causal uncertainty and coordination boundaries explicit. | Implemented workflow packages in the requested five-skill cadence, 2026-10-24. | Per-skill metadata/resource checks and isolated forward tasks; application CI/deployment evidence remains target-specific. |
| TOOLKIT-013 | Implement catalog entries 15–19 as separate failure/lifetime, configuration, dependency, legacy-modernization and test-strategy workflows. Preserve accepted semantics, compatibility and evidence boundaries; test strategy designs required local/CI/server gates without claiming execution. | Implemented workflow packages in the requested five-skill cadence, 2026-10-24. | Per-skill metadata/resource checks and isolated forward tasks; actual target pipeline enforcement and release evidence remain separate. |

## Workflow and outputs

1. Identify the target component and read its current contracts and project logic.
2. Select an available skill from the registry; read only the applicable resources.
3. For requirements work, establish evidence, scope, process, backend/data contracts, acceptance checks, and unanswered decisions.
4. Resolve decisions that block the next activity while continuing independent work. Preserve answers, their sources, and acceptance evidence.
5. Materialize accepted answers into the target project's current logic rules, workflows, contracts, edge cases, and acceptance criteria; record significant rationale separately.
6. Before coding, load the applicable logic revision and rule IDs, check critical open decisions and conflicts, and derive the implementation's verification cases.
7. Verify the change, update logic/code/test links together, update the skill registry if needed, and report actual publication and validation status.

Current available workflows: the first nineteen catalog entries, from requirements analysis through test strategy. The catalog and registry identify their boundaries. Dedicated test-creation/execution, CI/CD/deployment, scaling and SRS gap-audit workflows remain planned. Test Strategy defines verification scope and gates; it does not implement all suites or establish a pass. Project Setup may create a real scoped CI test job, while Production Readiness Review assesses release evidence; neither means that this repository now has a generic product deployment pipeline.

## Keep each product's logic local

For a component-specific task, establish a `PROJECT_LOGIC.md` inside that component using [the template](skills/templates/PROJECT_LOGIC.md), or preserve its existing equivalent documentation and link it here. Keep its rules and decision records scoped to that product. Do not share one unqualified rule table across unrelated products.

Use a linked SRS for full requirements, API/event schemas for interface details, and `docs/decisions/` for major choices and tradeoffs. This file remains the entry point, not a copy of every document. See [the layout decision](docs/decisions/0001-engineering-knowledge-layout.md).

Use [the SRS-to-logic handoff procedure](skills/ds-requirements-analysis/references/logic-handoff.md) to transfer review outcomes into a versioned coding baseline. The target project's document must contain the effective rules and accepted answers, rather than only a link back to a conversation. Keep source SRS links and decision history for traceability.

Harness contract: load the target logic baseline before implementation, select rules for the task, respect unresolved blockers, and update code/test references after changes. These are agent operating instructions; an external programmatic harness must explicitly read the documents if it does not already load repository guidance. This task does not add a runtime document loader.

## Open decisions and limits

- Application-specific rules for the existing components have not been reverse-engineered in this task. Their deeper logic remains unverified here.
- The first nineteen catalog skills are available. Subsequent creation uses batches of five in catalog order; the next batch is 20–24. The final batch may be smaller. Maintain actual available/planned status rather than treating the backlog as installed.
- Organizational file layout is implemented for review; it is not evidence of product approval or production readiness.
