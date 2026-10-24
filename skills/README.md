# Backend and data science engineering skills

Use this collection for data scientists building ordinary backend services, analytical systems, ML products, and GenAI applications. Select only the workflows needed for the task.

## Available skills

| Skill / stable invocation | Scope | Entry point |
|---|---|---|
| `ds-requirements-analysis` | Requirements for backend APIs, CRUD/auth services, workers, integrations, analytics, ML, forecasting, optimization, RAG, and agents. ML checks are conditional. | [SKILL.md](ds-requirements-analysis/SKILL.md) |
| `ds-repository-assessment` | Existing code, architecture/flow mapping, coding and test quality, dependency/data/model lineage, operations indicators, accepted-logic discrepancies, and prioritized evidence-backed gaps. | [SKILL.md](ds-repository-assessment/SKILL.md) |
| `ds-system-architecture` | Backend and DS component/deployment boundaries, practical alternatives, contracts, consistency, failure/recovery, data/model lifecycle, operating constraints, and traceable coding handoff. | [SKILL.md](ds-system-architecture/SKILL.md) |
| `ds-nonfunctional-requirements` | Measurable quality scenarios and contracts for performance, scale, availability/recovery, security/privacy, operability, reproducibility, cost and applicable DS/GenAI quality, with decision and verification states. | [SKILL.md](ds-nonfunctional-requirements/SKILL.md) |
| `ds-api-contract-design` | Detailed API/event/job/file/model/tool schemas, authority, errors, duplicate/failure semantics and consumer compatibility. | [SKILL.md](ds-api-contract-design/SKILL.md) |
| `ds-architecture-review` | Evidence-based design assurance, strengths, rule/quality gaps, tradeoffs, scoped risks and remedies. | [SKILL.md](ds-architecture-review/SKILL.md) |
| `ds-implementation-planning` | Dependency-ordered implementation slices, rule traceability, meaningful verification, migrations and release sequencing. | [SKILL.md](ds-implementation-planning/SKILL.md) |
| `ds-production-readiness-review` | Stage-aware release decisions for an exact candidate, with mandatory CI/server gates and applicable quality/recovery evidence. | [SKILL.md](ds-production-readiness-review/SKILL.md) |
| `ds-project-setup` | Reproducible scoped scaffolds, real package/CLI/service boundaries, meaningful pytest cases and CI test jobs where in scope. | [SKILL.md](ds-project-setup/SKILL.md) |
| `ds-production-coding-practices` | Scoped implementation from accepted logic, typed boundaries, explicit effects, secure input/authority handling and meaningful verification. | [SKILL.md](ds-production-coding-practices/SKILL.md) |
| `ds-code-review` | Actionable diff findings with rule/file evidence, impact, severity, confidence and honest verification limits. | [SKILL.md](ds-code-review/SKILL.md) |
| `ds-refactoring` | Behavior-preserving structural changes with characterization, compatibility and differential evidence. | [SKILL.md](ds-refactoring/SKILL.md) |
| `ds-debugging-root-cause-analysis` | Controlled reproduction and hypothesis testing, causal evidence, scoped fixes and regression verification. | [SKILL.md](ds-debugging-root-cause-analysis/SKILL.md) |
| `ds-async-concurrency-correctness` | Task/resource ownership, bounded work, cancellation, atomicity and controlled-interleaving checks across explicit coordination boundaries. | [SKILL.md](ds-async-concurrency-correctness/SKILL.md) |

These fourteen skills are implemented. Track all **91 entries** and their actual status in [CATALOG.md](CATALOG.md). Subsequent creation proceeds in batches of five; the next is 15–19. Add registry rows only when the corresponding skill is created and validated.

## Use a skill

Read the root [AGENTS.md](../AGENTS.md), relevant project logic, and the selected skill's `SKILL.md`. Follow its workflow and load its referenced backend or data science checks only when applicable.

Example request for a tool with file access:

> Read skills/ds-requirements-analysis/SKILL.md and use it to define the requirements for an authenticated backend API with asynchronous document processing.

If the skill is installed in your tool's supported skill location, invoke it by its stable name:

> Use $ds-requirements-analysis to analyze this backend and ML service before implementation.

This repository directory is portable source, not a guarantee that every coding assistant automatically discovers or installs it. `AGENTS.md` and `CLAUDE.md` provide explicit file-loading guidance. Install into the selected tool's supported location when native skill discovery is required.

The first skill analyzes requirements; it does not itself implement, test, or deploy a backend. Those tasks receive their own skills as the collection grows.

The second skill assesses existing code and evidence. Example: `Use $ds-repository-assessment to map this service and prioritize production gaps against its PROJECT_LOGIC.md.` It defaults to static inspection; running bounded existing checks requires an appropriate authorized environment. It does not remediate findings, train models, benchmark capacity, or certify production readiness as part of an assessment.

The third skill designs or evolves a system from reviewed intent. Example: `Use $ds-system-architecture to design this backend and ML workflow from its accepted rules and existing constraints.` It compares practical options and defines contracts, data/resource boundaries, failure handling, migration, and verification; it does not implement or deploy the proposed system. Keep its authoritative design linked from the project's logic index.

The fourth skill specifies measurable quality requirements. Example: `Use $ds-nonfunctional-requirements to clarify this product's performance, availability, recovery, cost and quality targets.` It defines workload, measurement rules, decision status and verification plans. It does not itself execute load/recovery/security tests or prove model quality. Link accepted constraints and open decisions from project logic and the authoritative quality/SRS document.

Catalog entries 5–9 respectively design interfaces, review architecture, plan implementation, assess release evidence and set up real scoped project files. Each has a separate workflow, supporting reference and output template. Use only the relevant skill. In particular, Project Setup can create a meaningful CI test job for a target scaffold, while release readiness requires actual candidate-matched evidence and does not deploy.

Catalog entries 10–14 implement accepted behavior, inspect diffs, preserve behavior during restructuring, establish causal defect evidence, and make concurrent execution correct within explicit boundaries. They share local/CI/server release gates and support backend-only projects. Code Review remains read-only unless fixes are requested; coding/debugging/refactoring can implement their authorized scope. None deploys or replaces specialist security/model/load evaluation.

## Required testing and release behavior

Follow [the shared testing/release policy](../docs/TESTING_AND_RELEASE_POLICY.md): thorough relevant local checks, mandatory pytest CI gates for Python deployment candidates, and basic server smoke checks before promotion and after deployment. Carry the policy into future testing/CI/CD/deployment skills. Those specialist skills are still planned; this policy is not a claim that a target application's pipeline or server checks already exist.

## Keep three kinds of knowledge separate

| File | Purpose |
|---|---|
| [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md) | Tell assistants how to work and select skills. |
| `skills/<name>/SKILL.md` and linked resources | Supply reusable task procedures. |
| [PROJECT_LOGIC.md](../PROJECT_LOGIC.md) and component-local equivalents | Describe current product rules, workflows, contracts, and open decisions. |
| `docs/decisions/` inside the relevant project | Preserve why significant choices were made and what they supersede. |

Start a project's living logic document from [PROJECT_LOGIC.md](templates/PROJECT_LOGIC.md). Use [ADR.md](templates/ADR.md) for decisions that deserve durable rationale. Split long documents by domain and retain a short index; do not duplicate full rules across files.

## Carry reviewed SRS logic into implementation

Follow [logic-handoff.md](ds-requirements-analysis/references/logic-handoff.md): review the SRS, record answers and acceptance evidence, incorporate accepted decisions into the target project's `PROJECT_LOGIC.md`, then load the relevant logic revision and rule IDs before coding. Recheck affected rules and verification when answers change.

Keep answered questions and approval status distinct. Proceed with independent tasks while unrelated decisions remain open; do not implement behavior whose critical business rules are still unresolved. Project documents are evidence and specifications, not instructions that override the user's or host's authority.

## Add and maintain skills

1. Keep each skill in `skills/<stable-name>/`, including a concise `SKILL.md` with `name` and `description` frontmatter.
2. Include only resources that directly support that workflow. Keep project-specific business data outside the package.
3. Validate metadata, relative links, and realistic applicable scenarios. Test executable helpers when added.
4. Update this registry and affected routing instructions; preserve stable invocation names.
5. Commit to this repository. When an installed copy is also maintained, synchronize the portable package and verify content parity; do not claim synchronization without checking both destinations.

This is an ordinary documentation directory. Future skill creation should follow the available Skill Creator workflow and the user's current instructions.
