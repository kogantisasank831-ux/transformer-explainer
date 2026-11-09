# Validation Record

**Documentation set:** AI and Data Science Interview Cheat Sheets  
**Environment:** document generation and static checks in the project workspace  
**Checked:** 9 November 2026

## Batch 1

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 11,430 |
| Python fenced blocks parsed | 22/22 |
| Statistical worked examples | Recalculated during review |
| Combined PDF | 42 A4 pages |
| Visual review | Cover and representative topic pages reviewed |

## Batch 2

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 12,072 |
| Python fenced blocks parsed | 7/7 |
| Markdown code fences | Balanced in all sheets |
| DOCX integrity | ZIP container test passed |
| Combined PDF | 38 A4 pages, tagged, unencrypted |
| PDF text extraction | 12,035 words extracted |
| Visual review | Cover, all four section starts, dense content, and final page reviewed |

## Batch 3

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 11,479 |
| Python fenced blocks parsed and executed | 6/6 |
| Behavior assertions | Cosine similarity, RRF, deterministic IDs, Recall@K, reciprocal rank passed |
| Markdown code fences | Balanced in all sheets |
| DOCX integrity | ZIP container test passed |
| Combined PDF | 38 A4 pages, tagged, unencrypted |
| PDF text extraction | 11,297 words extracted |
| Visual review | Cover, all four section starts, representative dense pages, and final page reviewed |

## Content checks

- Topic boundaries match the master index.
- Lead cases include requirements, data, metrics, risk, rollout, and monitoring.
- Transformer coverage distinguishes training, prefill, decode, KV cache, MHA/MQA/GQA, FlashAttention, long context, and MoE.
- LLM coverage distinguishes prompting, RAG, fine-tuning, SFT, LoRA/QLoRA, preference optimization, quantization, evaluation, security, and ecosystem roles.
- Library descriptions distinguish Nemotron, NeMo Framework, NeMo Guardrails, serving engines, and training/post-training libraries.
- RAG coverage separates embeddings/vector search, ingestion/chunking, online architecture, generation/citations, evaluation, security, and production operations.
- Retrieval coverage includes sparse/dense/hybrid search, bi-encoders/cross-encoders, exact/ANN, HNSW/IVF/PQ, RRF, reranking, and late interaction.
- Security coverage includes poisoning, indirect prompt injection, current ACL/tenant isolation, cache leakage, privacy, deletion, incident response, and release gates.

## Known limits

- Syntax parsing does not execute examples against every external dependency or version.
- External links and framework APIs can change after publication.
- Interview coverage varies by employer, domain, level, and project history.
- Production choices still require pinned-version integration, security, load, and model-quality testing.

