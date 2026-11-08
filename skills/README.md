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
| `ds-error-handling-resource-cleanup` | Explicit error contracts, owned/borrowed resource lifetimes, partial acquisition, cleanup failures, cancellation and safe recovery boundaries. | [SKILL.md](ds-error-handling-resource-cleanup/SKILL.md) |
| `ds-configuration-management` | Typed settings, explicit source precedence/merge, secret redaction, startup/reload snapshots and reproducible effective configuration. | [SKILL.md](ds-configuration-management/SKILL.md) |
| `ds-dependency-management` | Bounded manifest/lock changes, dependency resolution, provenance and actual platform/runtime/install compatibility evidence. | [SKILL.md](ds-dependency-management/SKILL.md) |
| `ds-legacy-modernization` | Incremental legacy migration with preserved contracts, consumer coexistence, isolated shadow comparison and cutover/recovery gates. | [SKILL.md](ds-legacy-modernization/SKILL.md) |
| `ds-test-strategy` | Risk-based rule-to-test mapping, meaningful oracles/fixtures, required local/CI/server gates and honest coverage/evidence gaps. | [SKILL.md](ds-test-strategy/SKILL.md) |
| `ds-unit-test-creation` | Focused pytest/native unit cases with independent oracles, deterministic fixtures and explicit mocked-boundary limits. | [SKILL.md](ds-unit-test-creation/SKILL.md) |
| `ds-integration-testing` | Real supported component/dependency checks, committed state, constraints, failures, isolated resources and reliable teardown. | [SKILL.md](ds-integration-testing/SKILL.md) |
| `ds-contract-testing` | Actual consumer/provider verification from accepted independent contracts, interface evolution and version-pair evidence. | [SKILL.md](ds-contract-testing/SKILL.md) |
| `ds-end-to-end-testing` | Critical journeys through actual entry points, workers/storage and terminal outcomes, with explicit substitutions and cleanup. | [SKILL.md](ds-end-to-end-testing/SKILL.md) |
| `ds-regression-testing` | Defect-linked tests, governed baselines, safe bad/good comparisons and normal failure evidence for unresolved regressions. | [SKILL.md](ds-regression-testing/SKILL.md) |
| `ds-property-based-fuzz-testing` | Bounded generated domains, independent invariants, minimized reproducers and explicit exploration limits. | [SKILL.md](ds-property-based-fuzz-testing/SKILL.md) |
| `ds-test-fixtures-data` | Fresh synthetic factories/data, safe lifecycle and parallel isolation, provenance and leakage-aware split constraints. | [SKILL.md](ds-test-fixtures-data/SKILL.md) |
| `ds-test-quality-assessment` | Evidence-based assessment of test oracles, real/fake boundaries, reliability, meaningful coverage and gate integrity. | [SKILL.md](ds-test-quality-assessment/SKILL.md) |
| `ds-smoke-release-verification` | Safe exact-candidate diagnostics and stage-aware smoke gates, trusted identity, authority/journey checks and recovery handoff. | [SKILL.md](ds-smoke-release-verification/SKILL.md) |
| `ds-threat-modeling` | Assets, actors, concrete trust-boundary abuse paths, control status, prioritized remedies and residual-risk decisions. | [SKILL.md](ds-threat-modeling/SKILL.md) |
| `ds-secure-code-review` | Scoped code/config security tracing, actionable mechanisms, trust-boundary evidence and proportionate remedies. | [SKILL.md](ds-secure-code-review/SKILL.md) |
| `ds-authentication-session-security` | Established identity/provider verification and session lifecycle controls with explicit unit versus real integration evidence. | [SKILL.md](ds-authentication-session-security/SKILL.md) |
| `ds-authorization-tenant-isolation` | Trusted object/action/tenant decisions across data/cache/retrieval/worker/tool paths with meaningful negatives. | [SKILL.md](ds-authorization-tenant-isolation/SKILL.md) |
| `ds-application-api-security-testing` | Bounded security cases against exact authorized boundaries, synthetic proof, normal failures and honest coverage limits. | [SKILL.md](ds-application-api-security-testing/SKILL.md) |
| `ds-secrets-cryptography` | Audited secret/crypto usage, redaction, purpose separation, safe format/key lifecycle and recoverable rotation. | [SKILL.md](ds-secrets-cryptography/SKILL.md) |

| `ds-software-supply-chain-security` | Dependency/build trust, SBOM coverage, immutable artifacts, and policy-bound provenance verification. | [SKILL.md](ds-software-supply-chain-security/SKILL.md) |
| `ds-infrastructure-security` | Cloud/IaC identity, exposure, storage, and workload isolation with desired-versus-effective evidence. | [SKILL.md](ds-infrastructure-security/SKILL.md) |
| `ds-privacy-data-protection` | Purpose-aware data inventory, minimization, lifecycle/deletion, and derived-data controls. | [SKILL.md](ds-privacy-data-protection/SKILL.md) |
| `ds-vulnerability-remediation` | Evidence-based vulnerability triage, scoped fixes, regression checks, and artifact/deployment closure. | [SKILL.md](ds-vulnerability-remediation/SKILL.md) |
| `ds-data-modeling` | Entity grain, keys, relationships, tenant constraints, temporal semantics, and schema verification. | [SKILL.md](ds-data-modeling/SKILL.md) |

| `ds-database-migrations` | Compatible schema/data evolution, backfills, lock impact, recovery, and exact-state verification. | [SKILL.md](ds-database-migrations/SKILL.md) |
| `ds-query-optimization` | Query correctness, representative plans, indexes, access patterns, and measured regressions. | [SKILL.md](ds-query-optimization/SKILL.md) |
| `ds-transactions-consistency` | Transaction boundaries, isolation, constraints, retries, and cross-resource consistency. | [SKILL.md](ds-transactions-consistency/SKILL.md) |
| `ds-cache-engineering` | Authoritative-source caching, keys, invalidation, freshness, stampedes, and failure behavior. | [SKILL.md](ds-cache-engineering/SKILL.md) |
| `ds-messaging-background-jobs` | Message delivery, worker lifecycle, retries, idempotency, ordering, schemas, and recovery. | [SKILL.md](ds-messaging-background-jobs/SKILL.md) |

| `ds-idempotency-workflow-recovery` | Operation identity, durable state machines, checkpoints, retries, compensation, and reconciliation. | [SKILL.md](ds-idempotency-workflow-recovery/SKILL.md) |
| `ds-data-pipeline-reliability` | Deterministic batch/stream processing, lineage, quality gates, atomic publication, and backfills. | [SKILL.md](ds-data-pipeline-reliability/SKILL.md) |
| `ds-performance-profiling` | Representative CPU, memory, I/O, concurrency, and GPU profiling with controlled overhead. | [SKILL.md](ds-performance-profiling/SKILL.md) |
| `ds-load-testing` | Expected workload models, representative scenarios, tail latency, resource saturation, and gates. | [SKILL.md](ds-load-testing/SKILL.md) |
| `ds-stress-spike-soak-testing` | Breaking-point, sudden-surge, endurance, degradation, and recovery evidence with safety controls. | [SKILL.md](ds-stress-spike-soak-testing/SKILL.md) |

| `ds-capacity-planning` | Demand forecasts, service-capacity curves, bottlenecks, redundancy, lead time, and headroom decisions. | [SKILL.md](ds-capacity-planning/SKILL.md) |
| `ds-scalability-architecture` | State-aware scale-up and scale-out design, partitioning, shared bottlenecks, locality, and safe evolution. | [SKILL.md](ds-scalability-architecture/SKILL.md) |
| `ds-autoscaling` | Metric-driven scaling policies, bounds, stabilization, startup, draining, dependency limits, and control-loop evidence. | [SKILL.md](ds-autoscaling/SKILL.md) |
| `ds-rate-limiting-backpressure` | Trusted admission, quotas and bursts, bounded queues, retry guidance, fairness, and overload propagation. | [SKILL.md](ds-rate-limiting-backpressure/SKILL.md) |
| `ds-performance-regression-benchmarking` | Repeatable benchmark contracts, controlled baselines, statistical gates, CI evidence, and regression diagnosis. | [SKILL.md](ds-performance-regression-benchmarking/SKILL.md) |

| `ds-build-packaging` | Native builds, versioned artifact contracts, clean installation, reproducibility, and exact-candidate verification. | [SKILL.md](ds-build-packaging/SKILL.md) |
| `ds-containerization` | OCI image construction, minimal runtime contents, non-root operation, lifecycle correctness, and image-level tests. | [SKILL.md](ds-containerization/SKILL.md) |
| `ds-infrastructure-as-code` | Versioned desired infrastructure, state and locking, reviewed plans, drift/import controls, and safe environment changes. | [SKILL.md](ds-infrastructure-as-code/SKILL.md) |
| `ds-ci-pipeline-engineering` | Trusted CI triggers, exact-revision tests and builds, matrices, caches, artifacts, permissions, and required status gates. | [SKILL.md](ds-ci-pipeline-engineering/SKILL.md) |
| `ds-cd-pipeline-engineering` | Immutable promotion, protected environments, progressive rollout gates, migration compatibility, verification, and recovery. | [SKILL.md](ds-cd-pipeline-engineering/SKILL.md) |

| `ds-deployment-execution` | Authorized exact-candidate deployment, preflight, controlled mutation, rollout observation, smoke verification, and closure. | [SKILL.md](ds-deployment-execution/SKILL.md) |
| `ds-kubernetes-operations` | Context-safe Kubernetes inspection, controller diagnosis, workload and node operations, declarative ownership, and effective-state checks. | [SKILL.md](ds-kubernetes-operations/SKILL.md) |
| `ds-progressive-delivery` | Canary, blue-green and shadow exposure, comparable cohorts, analysis gates, staged promotion, abort, and recovery. | [SKILL.md](ds-progressive-delivery/SKILL.md) |
| `ds-rollback-release-recovery` | Failed-release containment, rollback versus roll-forward decisions, data and model compatibility, reconciliation, and verified recovery. | [SKILL.md](ds-rollback-release-recovery/SKILL.md) |
| `ds-versioning-compatibility` | Public version contracts, compatibility directions, deprecation, migration, cross-version matrices, and DS artifact sets. | [SKILL.md](ds-versioning-compatibility/SKILL.md) |

| `ds-observability` | Correlated logs, metrics, traces and profiles, semantic schemas, cardinality, sampling, privacy, pipelines, and diagnostic validation. | [SKILL.md](ds-observability/SKILL.md) |
| `ds-slos-alerting` | User-centered SLIs and SLOs, error budgets, burn-rate alerts, paging ownership, missing-data rules, and alert validation. | [SKILL.md](ds-slos-alerting/SKILL.md) |
| `ds-resilience-engineering` | Failure-mode analysis, deadlines and retry budgets, isolation, degradation, redundancy, consistency, and recovery design. | [SKILL.md](ds-resilience-engineering/SKILL.md) |
| `ds-fault-injection-chaos-testing` | Hypothesis-driven fault experiments, steady-state measures, blast-radius limits, abort controls, recovery, and learning evidence. | [SKILL.md](ds-fault-injection-chaos-testing/SKILL.md) |
| `ds-backup-disaster-recovery` | State inventory, RPO/RTO, consistent protected copies, restore validation, DR topology, failover/failback, and recovery drills. | [SKILL.md](ds-backup-disaster-recovery/SKILL.md) |

| `ds-incident-response-postmortems` | Incident declaration, command, containment, communication, recovery evidence, blameless analysis, and verified corrective actions. | [SKILL.md](ds-incident-response-postmortems/SKILL.md) |
| `ds-runbooks-operational-handover` | Executable runbooks, safe decision paths, validation and freshness, ownership inventory, training, and evidence-based handover acceptance. | [SKILL.md](ds-runbooks-operational-handover/SKILL.md) |
| `ds-cost-resource-optimization` | Cost allocation and unit economics, measured utilization, optimization options and guardrails, safe execution, and realized-savings verification. | [SKILL.md](ds-cost-resource-optimization/SKILL.md) |
| `ds-frontend-engineering-quality` | Component and state design, API and async correctness, failure states, performance, security boundaries, testing, and measurable release quality. | [SKILL.md](ds-frontend-engineering-quality/SKILL.md) |
| `ds-accessibility-verification` | Accepted accessibility scope, semantic implementation, keyboard/focus and visual checks, assistive-technology journeys, findings, and regression evidence. | [SKILL.md](ds-accessibility-verification/SKILL.md) |

| `ds-browser-device-compatibility` | Supported environment matrix, standards and fallbacks, responsive/input/API behavior, risk-based automation and real-device evidence, and defect triage. | [SKILL.md](ds-browser-device-compatibility/SKILL.md) |
| `ds-ux-product-acceptance` | User needs and journeys, research and task evidence, outcome-based acceptance criteria, exact-candidate UAT, defects, and accountable acceptance. | [SKILL.md](ds-ux-product-acceptance/SKILL.md) |
| `ds-product-analytics-experimentation` | Decision-linked metric and event contracts, privacy-safe instrumentation, experiment assignment/exposure, quality diagnostics, analysis, and governed decisions. | [SKILL.md](ds-product-analytics-experimentation/SKILL.md) |
| `ds-technical-documentation` | Audience and task-oriented documentation architecture, authoritative references and examples, versioning and ownership, executable validation, and maintenance. | [SKILL.md](ds-technical-documentation/SKILL.md) |
| `ds-licensing-compliance-assessment` | Component and obligation inventory, provenance and SPDX normalization, policy and legal review, artifact-level notices and source obligations, exceptions, and evidence-based release assessment. | [SKILL.md](ds-licensing-compliance-assessment/SKILL.md) |

| `ds-service-decommissioning` | Usage and dependency discovery, replacement migration, staged disablement, data retention and sanitization, access/infrastructure removal, and verified closure. | [SKILL.md](ds-service-decommissioning/SKILL.md) |
| `ds-ml-data-feature-validation` | Data provenance and snapshots, schema/domain and label quality, leakage-safe splits, feature semantics and point-in-time parity, drift/skew, slices, and quality gates. | [SKILL.md](ds-ml-data-feature-validation/SKILL.md) |
| `ds-training-experiment-reproducibility` | Experiment intent and lineage, immutable code/data/config/environment identities, randomness and numerical limits, checkpoints, tracking integrity, and independent reruns. | [SKILL.md](ds-training-experiment-reproducibility/SKILL.md) |
| `ds-model-evaluation-release-gates` | Contextual evaluation plans, independent data and slices, task metrics and uncertainty, robustness and harm evidence, exact-candidate gates, approval and monitoring readiness. | [SKILL.md](ds-model-evaluation-release-gates/SKILL.md) |
| `ds-model-serving-inference-optimization` | Exact serving identities and workload, phase-level latency and capacity, engine tuning, caching/quantization/parallelism, quality guardrails, overload behavior, and rollout evidence. | [SKILL.md](ds-model-serving-inference-optimization/SKILL.md) |

| `ds-prompt-structured-output-engineering` | Versioned prompt assembly, instruction and data boundaries, schema-first outputs, validation and repair, semantic enforcement, regression evaluation, compatibility, and lineage. | [SKILL.md](ds-prompt-structured-output-engineering/SKILL.md) |
| `ds-rag-engineering-evaluation` | Corpus and index lineage, access-aware ingestion, hybrid retrieval and reranking, grounded generation and citations, component and end-to-end evaluation, freshness, security, and operations. | [SKILL.md](ds-rag-engineering-evaluation/SKILL.md) |
| `ds-agent-workflow-reliability` | Explicit workflow state, typed least-privilege tools, durable side-effect recovery, bounded loops and budgets, memory and handoffs, trajectory/outcome evaluation, and operations. | [SKILL.md](ds-agent-workflow-reliability/SKILL.md) |
| `ds-ai-security-adversarial-testing` | Authorized AI threat scenarios, impact-based adversarial harnesses, prompt injection and poisoning, output/tool/tenant controls, resource abuse, mitigation verification, regression, and residual risk. | [SKILL.md](ds-ai-security-adversarial-testing/SKILL.md) |
| `ds-token-context-inference-cost-control` | End-to-end AI unit economics, token and billing reconciliation, context allocation and compaction, caching and routing, budget enforcement, quality-cost evaluation, allocation, and anomalies. | [SKILL.md](ds-token-context-inference-cost-control/SKILL.md) |

| `ds-ai-production-monitoring` | Exact deployed lineage, telemetry integrity, service and dependency health, production quality and drift, RAG and agent outcomes, safety and cost signals, alerts, feedback, and response. | [SKILL.md](ds-ai-production-monitoring/SKILL.md) |
| `ds-srs-gap-analysis-business-process-validation` | SRS quality and traceability, end-to-end process and state validation, unanswered and contradictory decisions, question ownership and blocking status, stakeholder walkthrough, and accepted logic handoff. | [SKILL.md](ds-srs-gap-analysis-business-process-validation/SKILL.md) |

These ninety-one skills are implemented. The complete catalog and current status are recorded in [CATALOG.md](CATALOG.md). Maintain each package independently and update the registry only after validation.

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

Catalog entries 15–19 handle failure/lifetime contracts, validated runtime settings, compatible dependency graphs, incremental legacy migration and risk-based verification strategy. They retain backend-only and conditional DS profiles. Test Strategy plans meaningful local/CI/server gates; the specialist unit/integration/contract/end-to-end/regression workflows are now available as entries 20–24. No target CI/deployment success is inferred from these packages.

Catalog entries 20–24 create and run scoped executable tests, preserving the difference between unit isolation, real integration, consumer/provider compatibility, complete journeys and regression protection. Each records its actual boundary and test results. Tests-only requests retain ordinary failures and report product defects; they do not silently change production code, approve new baselines or claim CI/server success from local runs.

Catalog entries 25–29 add bounded property/fuzz exploration, safe fixture/data creation, test-quality assessment, candidate-aware smoke verification and concrete threat modeling. Ordinary failing examples remain visible; synthetic/server-fixture success is scoped to that boundary. Assessment/modeling workflows do not silently modify products, execute attacks or grant release/risk acceptance.

Catalog entries 30–34 add concrete secure code review, authentication/session controls, trusted authorization/tenant isolation, bounded application/API security tests and audited secrets/crypto lifecycle work. Review/tests-only scope stays explicit; local fixtures and mocked providers do not establish deployed identity, storage or key-service enforcement. These workflows do not grant risk acceptance, security certification or deployment authority.

Catalog entries 35–39 cover software supply-chain trust, infrastructure controls, privacy/data lifecycle, vulnerability remediation, and data modeling. Bind evidence to actual artifacts and environments, distinguish desired state from deployed enforcement, preserve accepted privacy/domain policy, and separate source fixes from verified deployed closure. Data modeling creates traceable constraints and a coding handoff; it does not implicitly execute live migrations.

Catalog entries 40–44 handle database migrations, query optimization, transactions/consistency, cache engineering, and messaging/background jobs. Preserve accepted data semantics and invariants, measure representative workloads, state consistency and delivery boundaries, and distinguish local or simulated evidence from actual engine, cache, broker, CI, and deployed behavior. Migration, replay, repair, and deployment remain separately authorized actions.

Catalog entries 45–49 cover idempotent workflow recovery, data-pipeline reliability, performance profiling, expected-load testing, and stress/spike/soak testing. Define operation and data identities, publish only validated complete outputs, profile representative workloads, keep load-generator evidence separate from system behavior, and require explicit safety and recovery controls for abnormal load. Production replay, destructive recovery, traffic generation, and deployment remain separately authorized.

Catalog entries 50–54 cover capacity planning, scalability architecture, autoscaling, rate limiting/backpressure, and performance regression benchmarking. Tie demand to measured service capacity, design state-aware scale paths, treat autoscaling as a bounded control loop, propagate overload through fair bounded admission, and compare performance against immutable comparable baselines. Plans and configured policies remain distinct from deployed behavior; production traffic, scaling, quota changes, and deployment remain separately authorized.

Catalog entries 55–59 cover build and packaging, containerization, infrastructure as code, CI pipeline engineering, and CD pipeline engineering. Build exact installable artifacts, create runtime-correct OCI images, review stateful infrastructure plans, enforce candidate-matched test gates, and promote immutable digests through protected environments. Building, publishing, applying infrastructure, and deploying remain distinct evidence and authorization states.

Catalog entries 60–64 cover deployment execution, Kubernetes operations, progressive delivery, rollback and release recovery, and versioning/compatibility. Execute one authorized immutable candidate, operate clusters from exact context and ownership, limit exposure through evidence-gated stages, recover from current effective state, and prove cross-version contracts. Mutations stay within the named environment and authority, and command success never substitutes for functional or data verification.

Catalog entries 65–69 cover observability, SLOs and alerting, resilience engineering, bounded fault experiments, and backup/disaster recovery. Correlate privacy-safe signals, define user-centered budgets and actionable pages, bound failure amplification, test one authorized hypothesis with safe aborts, and prove recovery by restoring and validating data and service behavior. Configuration, quiet alerts, surviving processes, completed experiments, replicas, and backup-job success remain distinct from verified outcomes.

Catalog entries 70–74 cover incident response and learning, executable runbooks and operational transfer, measured cost/resource optimization, frontend engineering quality, and accessibility verification. Coordinate from user impact and preserved evidence, prove procedures with cold readers, reconcile cost to demand and quality guardrails, make asynchronous interfaces deterministic, and combine automated accessibility checks with manual and assistive-technology journeys. Meetings, documents, estimates, development builds, and automated scores remain distinct from accepted and verified outcomes.

Catalog entries 75–79 cover supported browser/device behavior, user and product acceptance, trustworthy analytics and controlled experiments, task-oriented technical documentation, and licensing/compliance evidence. Define actual support and user populations, verify authoritative state and side effects, diagnose experiment data quality before causal decisions, execute documentation examples, and bind obligations to exact release artifacts. Compatibility metadata, demos, dashboards, page views, scans and top-level license files remain distinct from verified outcomes and accountable decisions.

Catalog entries 80–84 cover verified service retirement, ML data and feature correctness, training reproducibility, contextual model release evaluation, and measured inference optimization. Discover hidden consumers before staged shutdown, preserve point-in-time data semantics, capture complete immutable run lineage, bind independent gates to exact model artifacts, and tune serving from representative queue and GPU evidence. Quiet dashboards, inferred schemas, seeds, aggregate scores, theoretical capacity and copied engine settings remain distinct from verified outcomes.

Catalog entries 85–89 cover prompt and structured-output contracts, traceable RAG, recoverable agent workflows, impact-based AI adversarial testing, and end-to-end token/context cost control. Keep generated and retrieved content untrusted, enforce semantics and authority in code, preserve corpus/workflow/cost identities, bound retries and side effects, and compare exact candidates on representative quality, security, reliability and unit economics. Schema validity, citations, agent narratives, payload-list passes, token estimates and lower averages remain distinct from verified outcomes.

Catalog entries 90–91 complete the collection with production AI monitoring and SRS gap/business-process validation. Bind live evidence to exact deployed identities, treat missing telemetry as unknown, join delayed outcomes, and connect alerts to tested response. Before implementation, reconstruct complete processes and states, expose every material unanswered decision or contradiction, record accountable acceptance, and transfer effective rules into the target `PROJECT_LOGIC.md`. Dashboards, meetings, answers and polished diagrams remain distinct from verified monitoring, accepted logic and coding readiness.

## Required testing and release behavior

Follow [the shared testing/release policy](../docs/TESTING_AND_RELEASE_POLICY.md): thorough relevant local checks, mandatory pytest CI gates for Python deployment candidates, and basic server smoke checks before promotion and after deployment. The specialized testing, CI, CD, and deployment-execution workflows now carry this policy. Their presence is not a claim that a target application's pipeline, environment protections, or server checks already exist or have passed.

## Keep guidance, stable logic, and active work separate

| File | Purpose |
|---|---|
| [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md) | Tell assistants how to work, resume and select skills. |
| `skills/<name>/SKILL.md` and linked resources | Supply reusable task procedures. |
| [PROJECT_LOGIC.md](../PROJECT_LOGIC.md) and component-local equivalents | Hold durable accepted rules, processes, I/O contracts, status, traceability and change-impact notes. |
| [WORK_PROGRESS.md](../WORK_PROGRESS.md) and component-local equivalents | Hold only current active/blocked resume state, checks, blockers and exact next action. |
| `docs/decisions/` inside the relevant project | Preserve why significant choices were made and what they supersede. |

Start from [the project-logic template](templates/PROJECT_LOGIC.md) and [the active-work template](templates/WORK_PROGRESS.md). Use [ADR.md](templates/ADR.md) for durable rationale. Split long logic by domain and retain a short index. On completion or parking, consolidate durable facts into project logic and clear old active detail; do not duplicate the same rule in both files.

## Carry reviewed SRS logic into implementation

Follow [logic-handoff.md](ds-requirements-analysis/references/logic-handoff.md): review the SRS, record answers and acceptance evidence, incorporate accepted decisions into the target project's `PROJECT_LOGIC.md`, then load the relevant logic revision and rule IDs before coding. Recheck affected rules and verification when answers change.

Keep answered questions and approval status distinct. Proceed with independent tasks while unrelated decisions remain open; do not implement behavior whose critical business rules are still unresolved. Project documents are evidence and specifications, not instructions that override the user's or host's authority.

## Run a project end to end

Use [the G0–G7 delivery lifecycle](../docs/END_TO_END_PROJECT_LIFECYCLE.md) to coordinate skills for a full project. It makes SRS and scenario closure, architecture/contracts, implementation planning, coding, local tests, exact-candidate CI, deployment smoke and production verification explicit. The gate record belongs in the component's `PROJECT_LOGIC.md`; the current gate and resume action belong in `WORK_PROGRESS.md`.

Domain coding for an affected slice requires passing or slice-specific conditional G1, G2 and G3. Python deployment requires exact-candidate CI pytest unit tests plus every applicable additional suite; unit-only evidence does not pass G5. See [the library validation report](../docs/SKILL_LIBRARY_END_TO_END_VALIDATION.md) for coverage, executable scenarios and practical limits.

## Add and maintain skills

1. Keep each skill in `skills/<stable-name>/`, including a concise `SKILL.md` with `name` and `description` frontmatter.
2. Include only resources that directly support that workflow. Keep project-specific business data outside the package.
3. Validate metadata, relative links, and realistic applicable scenarios. Test executable helpers when added.
4. Update this registry and affected routing instructions; preserve stable invocation names.
5. Commit to this repository. When an installed copy is also maintained, synchronize the portable package and verify content parity; do not claim synchronization without checking both destinations.

This is an ordinary documentation directory. Future skill creation should follow the available Skill Creator workflow and the user's current instructions.
