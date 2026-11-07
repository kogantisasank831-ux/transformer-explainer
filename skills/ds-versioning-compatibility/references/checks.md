# Versioning and compatibility checks

- Inventory independently consumed packages, APIs, events, schemas, config, state/checkpoints, images/artifacts, models/features/indexes/prompts and output formats with owners and consumers.
- Define the public contract, version signal, comparison rules, discovery and support promise for each surface. Separate version labels from immutable content identity.
- State source, binary, wire, behavioral, data, operational and semantic compatibility by actor and direction; include rolling and rollback combinations.
- Classify package/API/event/schema/config changes under the selected ecosystem policy. Preserve additive defaults, unknown-field and enum behavior, replay, migrations and consumer adoption evidence.
- For DS/ML, version the complete data, features, model, tokenizer, preprocessing, prompts/guardrails, thresholds, index, runtime/precision and output-schema set with bound evaluation.
- Define deprecation notice, telemetry, coexistence, migration, support/EOL, security fixes, exceptions and removal owner. Repository search alone does not establish zero consumers.
- Test supported cross-version producer/consumer and client/server matrices, mixed rollouts, persisted data/state, replay, upgrade/downgrade and rollback; document unsupported combinations.

Use [Semantic Versioning 2.0.0](https://semver.org/) only when its declared public-API contract fits the artifact, and follow the official versioning specification of each selected protocol or package ecosystem.
