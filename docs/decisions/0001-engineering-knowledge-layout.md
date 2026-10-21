# 0001: Separate agent guidance, reusable skills, and project logic

- Status: implemented organizational choice; user review pending for detailed layout.
- Date: 2026-10-21.
- Source: user request to publish engineering skills under `skills/`, support backend and data science work, and add agent guidance plus project-logic documentation.
- Scope: shared engineering toolkit; no application architecture changes.

## Context and options

A single large agent file mixes instructions, reusable workflows, and product-specific rules. Putting business rules inside skills makes those skills harder to reuse across products. A separate current-logic document plus small decision records keeps these concerns independently maintainable.

## Implemented organization

- Keep the shared operating rules and skill routing in root `AGENTS.md`.
- Keep root `CLAUDE.md` as a short pointer to the same guidance.
- Publish portable workflows under `skills/<stable-name>/` and list available packages in `skills/README.md`.
- Use root `PROJECT_LOGIC.md` for repository/toolkit navigation and component-local equivalents for each product's current rules.
- Keep important decision rationale under the relevant project's `docs/decisions/`, using the shared templates.

## Consequences and verification

Agents must read the applicable documents explicitly when their tool does not automatically discover them. Current business rules must not be duplicated across skill packages. Native skill installation remains tool-specific. If installed and repository copies are both maintained, their portable content must be compared after changes.

Verify metadata and links, backend-only applicability, and the distinction between requirements analysis and implementation. This record does not claim that the existing applications' business logic has been audited or that future skills exist.
