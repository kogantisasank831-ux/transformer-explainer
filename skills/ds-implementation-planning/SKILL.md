---
name: ds-implementation-planning
description: Turn reviewed requirements, project logic, contracts, architecture and assessment findings into a dependency-ordered implementation plan for backend and data science products. Use before coding a feature, migration, productionization effort or coordinated change. Produce bounded tasks with rule traceability, interfaces, verification, release gates and scoped blockers. Do not invent effort commitments, execute implementation or deploy from a planning-only request.
---

# Backend and Data Science Implementation Planning

Create a plan a coding harness can execute and verify without guessing business intent. Keep evidence, accepted decisions, assumptions and work status explicit.

## Establish the baseline and scope

- Read applicable instructions, PROJECT_LOGIC.md, accepted requirements, NFRs, contracts, architecture/ADRs and relevant repository/review evidence. Record revisions and intended delivery stage.
- Identify the requested outcome, existing behavior, constraints and dependencies. Preserve established code boundaries and test tools; do not plan a rewrite merely for style.
- Separate accepted business rules from authorized technical decisions, unresolved policy, feasibility risks and external prerequisites. Ask up to three high-impact questions while continuing independent planning.
- Use the current logic and linked source documents as the coding baseline. Do not infer missing authorization, retention, expiry, fallback or numeric targets from convenience.

## Plan slices and dependencies

Read [planning-checks.md](references/planning-checks.md). Break the change into bounded, reviewable slices that establish observable behavior, not a long undifferentiated list of files to edit.

- Use stable task IDs and an explicit dependency graph/order. Each task records relevant rule/requirement/contract IDs, preconditions, scope/files or modules, inputs/outputs, acceptance evidence, test cases and owner or unassigned.
- Separate discovery/feasibility work from implementation. Put high-impact unknowns such as data access/labels, inference fit, provider contracts, migration integrity and ambiguous external effects early; define an exit criterion without fabricating results.
- Identify which tasks can proceed independently and which are blocked by specific question/decision IDs. Avoid cycles; split tasks whose prerequisites or acceptance cannot be reviewed coherently.
- Include contract/schema evolution, old/new version coexistence, data backfills/cutover, idempotency, concurrency, recovery and compatibility tasks when relevant. Do not claim every migration is reversible.
- For DS, plan data contracts, leakage-safe evaluation, baselines, fitted preprocessing/artifact lineage, inference parity and quality/rollback evidence. For RAG/agents, add permissions, grounding, tool/state boundaries, budgets and failure/replay behavior. Omit ML infrastructure from ordinary backends.
- Preserve dependency/resource conflicts, sequencing of shared migrations and integration points when identifying parallelizable tasks. Do not automatically launch agents or execute planned work.

## Make verification and release part of the plan

- Attach meaningful success, boundary/error, permission, duplicate/race and recovery checks to behavior-changing tasks. Reuse existing tests where appropriate rather than mirroring implementation or imposing arbitrary coverage numbers.
- Plan thorough relevant local checks and the mandatory CI pytest unit/required integration gate for each Python deployment candidate. Missing, skipped or failed required checks block deployment; identify the actual commit/artifact and expected reports.
- Plan safe candidate/staging smoke checks before promotion and post-deployment verification of the promoted artifact. Deep/load/destructive checks belong in authorized isolated environments, not against live user data.
- Couple model/data/prompt quality and compatibility gates to release changes where relevant. Passing unit tests does not replace empirical model-quality, capacity or restore evidence.
- Define packaging/configuration, operational ownership, observability, release/cutover, rollback/recovery and documentation tasks at the appropriate depth. Use the project’s governance without inventing blanket approvals.

## Deliver and maintain the execution handoff

Use [implementation-plan.md](assets/implementation-plan.md). Preserve requested scope and a clear definition of done per slice; mark estimates as estimates with assumptions only when requested or supported. Do not invent deadlines, staffing or business acceptance.

- Provide the dependency order, task register, critical risks/decisions, verification/release sequence and independent work. Keep planned, in-progress, verified and blocked states separate; never mark a planned test passed.
- When project-document maintenance is requested, update the authoritative plan and link it from PROJECT_LOGIC.md. Supply logic/design/contract/NFR revisions, task/rule IDs, known code locations and test expectations to the coding harness.
- If the baseline changes, map the changed rules to tasks and acceptance cases and replan affected dependencies. Preserve history and superseded tasks rather than silently changing scope.
- State readiness for the named next activity with scoped blockers. Check specialist skill availability before invoking another workflow. Do not implement code, install tools, run experiments or deploy unless separately requested.
