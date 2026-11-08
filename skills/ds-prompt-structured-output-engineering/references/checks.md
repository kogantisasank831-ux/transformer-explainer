# Prompt and structured-output checks

- Define task, supported inputs, authoritative policy, downstream effects, failure/abstention, accepted quality and cost/latency sources.
- Pin model/runtime, tokenizer/template, API/SDK, generation controls, tool definitions, assembled prompt/config digest, examples, schema dialect and evaluator identities.
- Classify trusted instructions versus user/retrieved/tool/history data; preserve provenance and never rely on delimiters as a security boundary.
- Use a typed deterministic prompt builder with variable, encoding, size, multi-turn selection and compaction rules shared by evaluation and production.
- Define a consumer-owned versioned schema with required/closed fields, null semantics, bounds, variants and compatibility; record provider-subset limits.
- Prefer native constraints but validate every returned instance and refusal/filter/timeout/truncation path. JSON mode is not schema enforcement.
- Enforce semantic invariants, references, authorization, tenant and state policy in code; schema-valid is not semantically correct.
- Bound repair attempts/tokens/time/cost, preserve original failures and side-effect idempotency, then return a typed error or abstention.
- Evaluate normal, boundary, ambiguous, adversarial, multilingual, long-context and failure cases on locked data; separate structure, semantics, safety, latency and cost.
- Version and release the exact prompt/schema/model bundle with candidate-matched tests, progressive evidence and privacy-safe monitoring.

Use the pinned implementation's supported subset. [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12) defines the portable core and validation vocabularies; provider-constrained outputs may intentionally implement only part of that dialect.
