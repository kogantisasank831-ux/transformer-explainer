# RAG engineering and evaluation checks

- Define decision/query/answer populations, source authority and effective time, privacy/tenant policy, permitted model knowledge, citation and abstention behavior, quality, latency and cost.
- Pin corpus and ACL manifests, parser/chunker/dedup, metadata, embedding, index, retrieval/query/reranker and prompt/model/schema identities.
- Preserve source-to-passage lineage, structure and parsing coverage; quarantine ineligible content and prevent partial mixed-version publication.
- Enforce authorization before retrieval crosses the boundary and again at assembly; propagate update, revocation and deletion through every derived store.
- Compare lexical/dense/hybrid retrieval, filters, fusion and reranking on relevant slices. Preserve original queries and bound generated rewrites or decomposition.
- Assemble sufficient nonredundant context under a budget, retain provenance and handle empty, stale or conflicting evidence explicitly.
- Verify claim-level citation support, stable revisions and user access. Citation presence is not correctness; faithfulness is not truth or authority.
- Evaluate ingestion/retrieval and generation separately, then end to end with locked answerable/no-answer/temporal/ACL/adversarial cases and calibrated judges.
- Use ablations and counterfactual context to expose whether the generator uses evidence; do not let fluent answers hide retrieval misses.
- Monitor index/freshness/ACL/retrieval/answer/latency/cost behavior and define dependency degradation, exact-version rollout and rollback.

The original [RAG paper](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) distinguishes parametric and retrieved memory. ARES evaluates context relevance, answer faithfulness and answer relevance, illustrating why retrieval and generation need separate evidence; use domain-appropriate independent labels rather than adopting one framework's score as policy.
