# Repository and engineering toolkit logic

Last reviewed: 2026-10-21. Scope: repository navigation and the shared engineering toolkit. This is not a completed specification of every application in this repository.

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

## Workflow and outputs

1. Identify the target component and read its current contracts and project logic.
2. Select an available skill from the registry; read only the applicable resources.
3. For requirements work, establish evidence, scope, process, backend/data contracts, acceptance checks, and unanswered decisions.
4. Resolve decisions that block the next activity while continuing independent work.
5. Update project-specific requirements and logic when decisions or behavior change; record significant rationale separately.
6. Verify the change, update the skill registry if needed, and report actual publication and validation status.

Current available workflow: backend and data science requirements analysis. Architecture, coding, unit testing, security testing, deployment, scaling, and the dedicated SRS gap-audit workflows remain planned unless subsequently added to the registry.

## Keep each product's logic local

For a component-specific task, establish a `PROJECT_LOGIC.md` inside that component using [the template](skills/templates/PROJECT_LOGIC.md), or preserve its existing equivalent documentation and link it here. Keep its rules and decision records scoped to that product. Do not share one unqualified rule table across unrelated products.

Use a linked SRS for full requirements, API/event schemas for interface details, and `docs/decisions/` for major choices and tradeoffs. This file remains the entry point, not a copy of every document. See [the layout decision](docs/decisions/0001-engineering-knowledge-layout.md).

## Open decisions and limits

- Application-specific rules for the existing components have not been reverse-engineered in this task. Their deeper logic remains unverified here.
- Skill creation order remains one at a time from the agreed catalog; only the first skill is currently available.
- Organizational file layout is implemented for review; it is not evidence of product approval or production readiness.
