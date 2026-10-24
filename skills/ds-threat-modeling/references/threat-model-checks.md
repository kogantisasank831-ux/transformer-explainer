# Threat modeling checks

| Surface | Concrete abuse paths to consider when applicable |
|---|---|
| Backend authority | Authentication versus object/function/tenant permission, guessed IDs, cache/key scope, stale authorization, admin paths, worker identity and cross-tenant queue/state handling. |
| Inputs/effects | Injection, unsafe file/path/deserialization, external URL fetching, retry/replay/idempotency abuse, transaction gaps and consequential tool/payment/notification effects. |
| Data/operations | Secrets/log disclosure, storage/backup/access scope, integrity/poisoning, privileged CI/artifact/config changes, resource exhaustion and recovery ownership. |
| ML lifecycle | Unauthorized data/artifact changes, leakage, unsafe model loading, feature/preprocessing skew and untrusted evaluation provenance; actual efficacy needs dedicated evidence. |
| RAG/agents | Untrusted retrieved/tool content, cross-tenant retrieval/cache, prompt injection leading to authority misuse, output/tool-argument validation, credential scope and bounded tool/compute budgets. A prompt instruction is not an access-control boundary. |

For each threat record actor and preconditions, flow/asset/rule, mechanism and impact, evidence/confidence, controls and their verification status, proposed mitigation and residual risk/owner. Don't prescribe encryption, queues or new infrastructure without a concrete boundary/need. Don't confuse detection logs with prevention or a proposed control with a tested implementation.

Primary process reference: [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html). Apply it to the observed architecture; framework labels organize inquiry, not prove coverage. Confirm version-sensitive control behavior in the actual technology's primary documentation when needed.
