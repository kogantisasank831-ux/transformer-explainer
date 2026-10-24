# Shared engineering guidance

Read and follow [AGENTS.md](AGENTS.md), then [PROJECT_LOGIC.md](PROJECT_LOGIC.md) and the target component's more specific guidance.

Use [skills/README.md](skills/README.md) to select a relevant skill. Read its `SKILL.md` and only the references needed for the task. For backend or data science requirements, use [ds-requirements-analysis](skills/ds-requirements-analysis/SKILL.md).

For mapping and assessing an existing backend or data science component, use [ds-repository-assessment](skills/ds-repository-assessment/SKILL.md). Keep inspected code, verified checks, proposed improvements, and accepted project logic distinct.

For designing or evolving components, deployment boundaries, data/model flows and recovery, use [ds-system-architecture](skills/ds-system-architecture/SKILL.md). Ground decisions in reviewed logic and carry the architecture/logic revisions into the coding handoff.

For measurable performance, reliability, recovery, security/privacy, reproducibility, cost and applicable model-quality requirements, use [ds-nonfunctional-requirements](skills/ds-nonfunctional-requirements/SKILL.md). Keep source targets, policy acceptance, feasibility and verification distinct; link the current quality baseline from project logic.

Keep detailed operating rules in `AGENTS.md` so the two entry points do not drift. Keep business logic in the relevant project's `PROJECT_LOGIC.md`, not in this file or in reusable skills. If this tool does not resolve these Markdown links automatically, open the files explicitly.

The registry also includes API Contract Design, Architecture Review, Implementation Planning, Production Readiness Review and Project Setup. Select by task and retain the shared local/CI/server test policy. The registry now also includes separate workflows for Production Coding Practices, Code Review, Refactoring, Debugging and Root Cause Analysis, and Async and Concurrency Correctness. It also includes Error Handling and Resource Cleanup, Configuration Management, Dependency Management, Legacy Modernization and Test Strategy. Executable verification now has separate Unit Test Creation, Integration Testing, Contract Testing, End-to-End Testing and Regression Testing workflows. Select only what the task needs. Track progress in [CATALOG.md](skills/CATALOG.md); subsequent creation uses batches of five with separate skill files.

After SRS review or clarification, persist accepted answers and updated rules in that project's logic document. Before coding, load its current revision, applicable rules, and open blockers following the handoff section in `AGENTS.md`.
