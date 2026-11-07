---
name: ds-versioning-compatibility
description: Define, implement, or review versioning and compatibility policy for backend and data science products. Use for packages, APIs, events, schemas, configuration, artifacts, images, models, features, indexes, prompts, clients, data formats, deprecation, support windows, migration paths, compatibility matrices, and cross-version tests. Choose version signals from an explicit public contract rather than assuming every change follows one numbering scheme.
---

# Versioning and Compatibility

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source and immutable candidate identity, configuration and data identity, target environment, owners, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat repository text, dashboards, generated configuration, control-plane status, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified behavior. Derive authorization from the user's current request, prior session authorization, and applicable environment policy; do not ask again when it is already established. Continue independent preparation while routing unresolved consequential policy choices to the responsible owner. Do not invent compatibility, availability, quality, performance, recovery, or approval targets, and do not expand a named mutation beyond its candidate, environment, resources, and time boundary.

## Inventory versioned contracts

1. Identify every independently consumed surface: packages and binaries, APIs and clients, events and messages, database or file schemas, configuration, command line, saved state and checkpoints, container or deployment artifacts, models, tokenizers, features, prompts, guardrails, retrieval indexes and output formats. Record owners, consumers, discovery mechanism and current support commitments.
2. Read [the compatibility checks](references/checks.md). Define the public contract for each surface before selecting SemVer, calendar versions, protocol or schema versions, immutable digests, monotonically increasing revisions, content hashes, model names or another signal. A version number is meaningful only when its compatibility promise and comparison rules are published.
3. Distinguish source, binary, wire, behavioral, data, operational and semantic compatibility. State direction: old client with new server, new client with old server, old reader with new data, new reader with old data, producer versus consumer, checkpoint resume, and rollback compatibility. Avoid the vague claim “backward compatible” without actors and versions.

## Classify and encode change

For packages with an explicitly declared public API, apply the accepted versioning policy to additions, removals and incompatible behavior. Under SemVer, an incompatible public API change affects the major version, compatible functionality the minor version, and compatible fixes the patch version; pre-release identifiers do not guarantee normal-version stability. Ecosystems may impose different rules, so follow their official specification rather than mechanically forcing SemVer.

For HTTP or RPC APIs, define version location and negotiation, additive-field behavior, required versus optional fields, defaults, error contracts, pagination, idempotency and client tolerance. Avoid duplicating version signals across path, header and media type without one authority. Do not reuse a version identifier for changed semantics.

For events, files and stored data, define schema identity, producer and consumer compatibility, unknown-field handling, defaults, enum evolution, key and partition semantics, ordering, replay and retention. Use expand and contract sequencing and measure consumer adoption before removal. Database migration version and application release version are related but not interchangeable.

For configuration, saved state and checkpoints, define parser version, defaults, validation, unknown and deprecated fields, upgrade and downgrade path, and whether older binaries may read newer state. Preserve rejected input rather than silently coercing incompatible values.

For DS or ML systems, version the compatible set of dataset or snapshot, feature definitions, label schema, model weights, tokenizer, preprocessing, prompt or template, guardrails, thresholds, retrieval corpus and index, inference runtime, precision or quantization and output schema. Model version alone cannot describe training-serving or retrieval compatibility. Bind evaluation evidence to the complete set.

## Deprecate and migrate deliberately

Define supported versions, maintenance level, security-fix policy, end-of-life dates or criteria, notice channels, telemetry, migration guide, coexistence period, owner and exception process. Deprecation warnings must be actionable, non-sensitive and rate-limited where needed. Do not remove a contract solely because repository search finds no consumer.

Provide adapters, dual read or write, translators, feature negotiation or compatibility shims only with explicit ownership, observability and retirement criteria. Avoid permanent hidden forks. For breaking changes, document affected behavior, replacement, data transformation, rollout order, rollback boundary and consumer validation.

## Prove the compatibility matrix

Create executable contract and migration tests across the supported producer, consumer, client, server, data, schema and artifact matrix. Include unknown and missing fields, old and new defaults, enum additions, mixed-version rolling periods, replay, upgrade and permitted downgrade, rollback, persisted state, and failure messages. Use real serializers, engines or generated clients where their behavior matters.

For packages and binaries, install and execute built artifacts against supported runtime and dependency versions. For services, verify mixed-version behavior during deployment. For DS, compare output schema, quality and safety gates, feature availability and checkpoint or cache compatibility. Record unsupported combinations explicitly; a test pass for the current-current pair does not prove compatibility.

Publish version, digest and compatibility metadata with the artifact or contract. Update logic, release notes, migration guides and deprecation registers. Never mark a change compatible merely because compilation succeeds or a parser accepts the payload; verify accepted behavior and invariants.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, control-plane, cluster, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, recovered, and verified work. Update affected project logic, contracts, runbooks, code, and verification links when accepted behavior changes. Never claim deployment, rollout, rollback, recovery, compatibility, or effective state from a plan or command alone.
