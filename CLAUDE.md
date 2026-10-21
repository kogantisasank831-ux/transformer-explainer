# Shared engineering guidance

Read and follow [AGENTS.md](AGENTS.md), then [PROJECT_LOGIC.md](PROJECT_LOGIC.md) and the target component's more specific guidance.

Use [skills/README.md](skills/README.md) to select a relevant skill. Read its `SKILL.md` and only the references needed for the task. For backend or data science requirements, use [ds-requirements-analysis](skills/ds-requirements-analysis/SKILL.md).

Keep detailed operating rules in `AGENTS.md` so the two entry points do not drift. Keep business logic in the relevant project's `PROJECT_LOGIC.md`, not in this file or in reusable skills. If this tool does not resolve these Markdown links automatically, open the files explicitly.

After SRS review or clarification, persist accepted answers and updated rules in that project's logic document. Before coding, load its current revision, applicable rules, and open blockers following the handoff section in `AGENTS.md`.
