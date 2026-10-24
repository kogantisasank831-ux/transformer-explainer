# Shared engineering guidance

Read [AGENTS.md](AGENTS.md), the relevant project's `PROJECT_LOGIC.md` and more specific component instructions before work. Keep detailed operating rules in AGENTS.md so the entry points do not drift.

Select an available workflow from [skills/README.md](skills/README.md); read its SKILL.md and only relevant references. If native discovery is unavailable, open the files explicitly. Scope workflows to the requested backend, native or data science component; apply ML concerns only where relevant.

Before coding, load the current logic revision, applicable rules/contracts and unresolved blockers. After SRS clarification, persist accepted answers and effective rules in that project's logic document; do not leave them only in chat or treat proposals as accepted policy.

Keep review/modeling/planning-only tasks within scope. Keep test oracles independent and report actual execution, failed/skipped gates and evidence limits. Follow the shared local/CI/server test policy in AGENTS.md; diagnostic or smoke success does not waive required candidate gates or authorize deployment.

Track actual availability and the next five-skill batch in [CATALOG.md](skills/CATALOG.md). The registry now covers requirements through threat modeling (entries 1–29); load only what the task needs rather than copying all skill instructions into this file.
