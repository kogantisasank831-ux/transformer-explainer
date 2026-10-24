---
name: ds-project-setup
description: Create or adapt a reproducible development scaffold for an authorized backend or data science project. Use to establish package/layout, environment/configuration, tooling, meaningful pytest tests, CI test gates, documentation and local commands from reviewed scope. Preserve existing projects and supported native tooling; add ML dependencies only when needed. Do not interpret setup as permission to implement the entire product, train/download models, provision infrastructure or deploy.
---

# Backend and Data Science Project Setup

Establish a small runnable base whose contracts and checks support the accepted scope. Produce actual files when setup is requested, preserving established project conventions.

## Inspect and select the minimal scaffold

- Read applicable instructions, PROJECT_LOGIC.md, accepted requirements/design/NFRs, testing policy and current repository/manifests/tests/CI before writing. Identify target component, delivery mode and constraints; record missing business behavior rather than inventing it.
- Preserve user edits and existing packaging, language, lockfiles and layout. An ordinary backend or analysis does not automatically need a model, vector store, queue, Docker or Kubernetes.
- For a new Python project, select supported runtime/build/package/dependency tools consistent with the requirements; pin or lock reproducibly using the chosen tools. Verify current primary documentation before relying on version-specific configuration or actions.
- Make routine reversible setup choices within scope. Ask only consequential missing questions and continue independent work. Do not overwrite populated projects, replace tools wholesale or execute arbitrary repository scripts without inspecting them.

## Create bounded project files

Read [setup-checks.md](references/setup-checks.md). Create only files needed for the chosen library/CLI/job/service; use [setup-record.md](assets/setup-record.md) for the handoff rather than copying a large generic application.

- Establish package/import boundaries, declared runtime/development dependencies, configuration validation, secret-free example configuration and appropriate ignore rules. Keep domain code independent of framework/storage/model adapters where useful.
- For Python, use typed public boundaries, appropriate schema validation such as Pydantic when it fits, explicit errors, context-managed resources and useful redacted logging. Avoid speculative abstractions or frozen dataclasses everywhere.
- Provide deterministic meaningful pytest cases for actual scaffold behavior: package/CLI/service startup or configuration/schema behavior that exists. Add accepted domain examples only when implementing them is within scope. Do not create assert-True tests, fake endpoints or success stubs to make CI green.
- Register any test markers/profiles actually used; distinguish unit/integration and deployed smoke tests. Required suites must contain and execute required cases, with nonzero failures/collection errors preserved.
- Configure actual local commands and CI test jobs for Python setup where a repository CI platform is in scope. Use clean reproducible dependency installation, least needed job permissions and the actual project working directory; do not fabricate lockfiles by hand.
- Wire deployment/promotion jobs only if those jobs and their authorization are in scope; otherwise document the required dependency gate and missing target details. Never claim deployment is blocked in a pipeline that does not exist.

## Carry the user's release policy

- Support thorough relevant local tests, mandatory pytest unit/required integration checks for every Python deployment candidate, and safe deployed-server smoke verification before promotion and after rollout.
- CI jobs must preserve failure and no-test outcomes. Do not use continue-on-error, unconditional deploy, shell suppression or misleading path filters to bypass required gates. Inspect skips/xfails and prove the required suites ran, not merely that an empty command exited zero.
- If deploy jobs exist, make them depend on successful candidate checks and use immutable artifact identity; a local pass or unrelated green run is insufficient. Repository/environment required-status settings need separate verification from YAML.
- Define smoke interfaces/commands only for real implemented surfaces; mark missing server URLs, credentials, target environments and checks as pending. Use isolated synthetic fixtures and bounded safe server checks; do not run deep/destructive suites on live user data.
- For DS work add lightweight data/schema and preprocessing/inference contract checks when applicable, with optional heavy/GPU/evaluation profiles. Do not force training, large model downloads, live paid providers or secret access into default unit tests. Preserve data/model/prompt/config lineage and quality-gate requirements.

## Verify, document and deliver

- Inspect scripts before execution. Use the authorized local isolated environment; installing declared dependencies may be in setup scope, but do not contact production, provision resources, spend on providers or download large artifacts without scope supporting it.
- Run the applicable import/build/CLI/service and pytest checks for the files created; use available schema/YAML/CI validation as appropriate. Record commands, environment, results, skips and limitations. Static workflow validation does not prove GitHub CI or a server smoke run passed.
- If dependencies/network/tool access block execution, preserve the scaffold and report not-run evidence and exact next steps. Do not substitute fake passing tests or suppress a required failure.
- Provide concise project-specific setup/run/test commands, configuration needs, extension points, file changes and remaining decisions. When maintaining project docs is in scope, update logic and link the setup/CI records, preserving accepted versus proposed decisions.
- State readiness for local development only to the extent verified. Check specialist skill availability before handoff. Do not implement unrelated features, push/deploy externally or claim production readiness unless separately requested and evidenced.
