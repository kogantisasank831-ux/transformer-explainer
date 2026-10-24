---
name: ds-api-contract-design
description: Design or evolve API, event, job, file, inference, and tool contracts for backend and data science products from reviewed logic and architecture. Use before implementing interfaces or changing consumer-visible schemas, errors, authorization, idempotency, streaming, or compatibility. Produce source-linked contracts and verification cases with explicit unresolved policy. Do not substitute this workflow for full system design, implementation, live integration tests, or deployment.
---

# Backend and Data Science API and Contract Design

Make interfaces explicit enough for independent producers, consumers, and tests. Preserve accepted business semantics and existing consumers.

## Establish the contract baseline

- Read applicable agent guidance, PROJECT_LOGIC.md, SRS, architecture, NFRs, existing schemas/clients and relevant code. Record revisions, accepted rules, consumers, protocol and compatibility obligations.
- Separate observed current behavior, accepted intended behavior, authorized technical choices, proposed changes and unanswered policy. Do not silently turn an undocumented implementation into an accepted rule.
- Identify caller identity/tenant, resource ownership, authoritative state, side effects, and synchronous versus asynchronous completion. Use the existing stack unless requirements justify a change.
- Ask up to three high-impact questions when needed and continue independent work. Leave cancellation authority, expiry/refresh rules, payload equivalence, retention, fallback and other user-visible defaults unresolved unless supported by sources.

## Specify interfaces and outcomes

Read [contract-checks.md](references/contract-checks.md). Define only applicable interfaces, including API endpoints, commands, events, job submission/status, files, model inference and agent tools.

- Assign stable contract IDs linked to rule/requirement IDs. Specify operation, caller authority, preconditions, validated inputs, output/error schema, postconditions, side effects, timing and versioning.
- Define field types, required/optional/null distinctions, units/timezones, identifier formats, enum/transition constraints, size/range limits and extra-field behavior. Keep missing numeric limits explicitly pending rather than inventing them.
- Define authentication and per-resource/tenant authorization, including list/read/download/status/retry paths. Do not trust a client-supplied owner or model output as authority.
- Define error categories and transport mapping, safe messages, retryability and correlation. Keep application errors distinct from transport failure and avoid exposing secrets or sensitive records in examples.
- Specify stable pagination/filter/sort semantics, optimistic concurrency/version preconditions and lost-response behavior where relevant. Do not promise snapshot-consistent pagination or exactly-once effects without a supporting mechanism.
- For jobs and external effects, distinguish receipt, durable acceptance, execution, completion and delivery. Define idempotency scope, payload comparison, window semantics, conflict, retries, cancellation races, replay and unknown outcomes, or link precise open decisions.
- For streaming, specify framing/content type, event order, partial output, final status, cancellation/disconnect, bounded buffering and errors after headers have been sent. First-token delivery does not mean full task completion.

## Apply data science and integration constraints

- For data/model interfaces, define input feature names/order/types/shape, missing/invalid/NaN semantics, units, preprocessing/model/config versions, batch limits, output schema and lineage as applicable. Do not add ML fields to an ordinary backend contract.
- Distinguish calibrated probability, score, confidence heuristic, abstention and error. Preserve evaluation requirements separately; schema-valid output is not proof of predictive quality.
- For RAG, specify evidence/citation identity, source version, permission scope and insufficient-evidence behavior. For tools, enforce arguments, user authority, side-effect boundaries and recovery outside prompts.
- For uploads/webhooks/events, define content and signature validation, replay/deduplication/ordering, delivery assumptions and compatibility. Use only supplied file/type/size rules or clearly proposed options.

## Check compatibility and deliver

- Compare old and new producer/consumer behavior, including stricter validation, defaults, enum growth, error changes and model/schema coupling. Classify breakage and plan coexistence, deprecation and migration without inventing dates.
- Define positive, malformed, unauthorized, boundary, duplicate/concurrent, timeout and recovery cases for applicable contracts. Carry thorough local tests, mandatory CI pytest gates for Python candidates, and safe deployed-server smoke checks into the handoff. Do not claim tests executed from a plan.
- Use [contract-baseline.md](assets/contract-baseline.md). Produce the complete schema in the project's existing format when requested; validate it with available appropriate tools and identify fragments as fragments. Verify version-specific capabilities against current primary documentation before relying on them.
- When documentation maintenance is in scope, update authoritative contract files/docs and link their revisions and accepted decisions from PROJECT_LOGIC.md. Keep proposals/open decisions labeled and use established decision records for significant rationale.
- Hand coding/testing workflows the logic/schema revisions, contract/rule IDs, examples, expected failures, consumer migration and scoped blockers. Report actual validation and persistence. Do not implement handlers, run live side effects, change data, or deploy unless separately requested.
