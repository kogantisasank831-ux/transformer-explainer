# AI security and adversarial testing checks

- Bind exact candidate, prompts/models/tools/corpus/data/artifacts/accounts/environment, assets and trust boundaries, authorization, exclusions, caps, aborts and incident contact.
- Define each security property and deterministic impact oracle; distinguish model text, attempted action, blocked action and committed effect.
- Use isolated identities, synthetic canaries and bounded dependencies; keep real secrets and unrelated personal data out of prompts, corpora, logs and judges.
- Cover direct and indirect injection across users, documents, tools, memory, modalities and agents, with encoded, multilingual, long-context and multi-turn variants.
- Test generated output at interpreter/sink boundaries plus deterministic schema, escaping, authorization, tenant, sandbox and egress controls.
- Test RAG poisoning/authority/ACL/citation paths, agent excessive agency and replay, pipeline provenance/poisoning, and bounded resource/cost abuse where applicable.
- Build a versioned scenario taxonomy with prerequisites, transformations, controls, impact, cleanup and owner; preserve seeds and minimized reproducers.
- Assert external state, permissions, destinations, canaries, operations and budgets; calibrate subjective safety labels and report variance/false positives.
- Fix durable control boundaries, add harmless impact-based regressions and gate the exact candidate; a passed payload list does not prove security.
- Monitor and rehearse disable/quarantine/revoke/contain/evidence/recovery paths. Risk exceptions require accountable ownership and expiry.

Use the current [OWASP GenAI/LLM risk catalog](https://genai.owasp.org/llm-top-10/) to seed, not replace, an application threat model. [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) includes adversarial testing and red-teaming actions within broader GenAI risk management.
