# Review checks

## Evidence standard

Use a reproducible input, path, interleaving or compatibility scenario. A finding should explain why the current change causes an undesirable outcome under supported conditions. Include code location and rule/contract source, or clearly explain the generally required invariant (for example isolation of different authenticated tenants). Mark unverified assumptions. Keep pre-existing issues distinct from introduced regressions; omit unrelated issues unless scope warrants them.

Use repository severity conventions. If none exist, classify critical for demonstrated broad compromise/irrecoverable severe harm, high for serious correctness/security/data loss under supported conditions, medium for bounded material failure, low for limited maintainability/edge impact. Confidence is separate from severity. Reserve merge-blocking claims for supported requirements and findings, not taste.

## Applicable surfaces

- Backend: schema/error compatibility, object/tenant authorization, unsafe input/SQL/path use, transaction boundaries, retry duplication, idempotency equality, migration coexistence, null/time/precision semantics, cancellation and resource lifetime.
- Data/ML: changed joins/cardinality, split contamination and leakage, feature/preprocessing parity, output/index alignment, changed denominators, artifact/config lineage and approved thresholds. Quality improvement requires relevant evaluation evidence, not a metric asserted by code.
- RAG/agents: resource-level permission checks in retrieval/cache/tool execution, prompt injection trust boundaries, side effects, structured-output validation and bounded budgets. A model response cannot substitute for an authorization check.
- Tests/CI: behavior assertions, representative negative cases, meaningful integration boundaries, required skips/no-test exit handling and exact candidate identity. Green unrelated CI is not evidence for this diff.

Consult official documentation for version-sensitive API behavior. Do not demand a complete rewrite or new framework when a focused correction addresses the finding.
