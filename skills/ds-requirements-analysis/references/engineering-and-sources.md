# Engineering requirements and source anchors

## Capture coding expectations without prescribing architecture

Apply repository rules and explicit project constraints first. Record requirements for maintainability, correctness, security, reproducibility, and operability at the level appropriate to the delivery stage.

Apply language-independent software requirements to backend-only services too: explicit contracts, separation of business logic from transport/persistence, validated external input, authorization at trust boundaries, controlled side effects, dependency management, and meaningful verification. Establish the expected coding conventions and existing tools before adding replacements.

For a production Python project, propose the following only where relevant and label unsupplied choices as pending:

- Define typed interfaces and boundary validation. Consider Pydantic for external I/O; keep internal representations and dataclass mutability appropriate to their role rather than requiring frozen objects everywhere.
- Define structured, redacted logging; explicit failure contracts; resource cleanup; and safe configuration/secrets handling.
- Define modular boundaries, dependency/environment reproducibility, code quality tools, and automated checks. Follow established tooling instead of replacing it arbitrarily.
- Define meaningful pytest unit/integration checks for accepted behavior and failure paths; add contract, property, security, or load tests according to risk.
- Define model/data/prompt/config versioning and artifact provenance in addition to source version control.
- Define public API compatibility, data migration needs, permission enforcement, and operational ownership for services.

Keep language-independent intent explicit. Do not force Python, FastAPI, LangGraph, a vector database, or container orchestration onto an unrelated analysis or a project with another established stack.

## Verification examples

Treat these as example formats, not approved targets.

| Weak statement | Better requirement or decision |
|---|---|
| The model must be accurate. | Decide the deployment population, error costs, baseline, metric, evaluation split, and acceptance threshold before a release-quality claim. |
| Support 2,000 users. | Clarify active users versus in-flight requests, arrival pattern, payload/token distribution, latency boundary, and sustained duration before sizing. |
| The API must respond quickly. | Propose a pending latency budget with percentile, end-to-end boundary, named workload, environment, and error-rate policy. |
| The agent can issue refunds. | Specify authorized actors, tool permissions, limits, approval policy, duplicate prevention, audit trail, and partial-failure recovery before enabling this action. |
| Make the notebook production ready. | Identify its intended consumer, rerun/reproducibility needs, data contracts, configuration, tests, delivery mode, and operational owner before selecting a package/API/job architecture. |

## Source anchors

Use these primary references to guide analysis; do not claim certification or full compliance from this checklist. Inspect the currently applicable source/version when the project requires a formal standard, security control, or jurisdiction-specific obligation. Ask which obligations apply rather than inventing them.

- [NASA: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) — requirements quality and verifiability.
- [scikit-learn: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — inconsistent preprocessing, leakage, and reproducibility considerations for ML workflows.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — stakeholder context, evaluation, and risk management across the AI lifecycle.
- [OWASP ASVS](https://owasp.org/projects/asvs) — application security requirements and verification; select applicable controls and versions rather than claiming blanket compliance.

Apply a project's mandated standards and versions explicitly; document applicability and evidence gaps. Do not mistake these guidance links for an exhaustive software engineering standard.
