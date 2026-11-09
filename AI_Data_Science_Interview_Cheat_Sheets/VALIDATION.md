# Validation Record

**Documentation set:** AI and Data Science Interview Cheat Sheets  
**Environment:** document generation and static checks in the project workspace  
**Checked:** 10 November 2026

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

## Batch 4

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 11,361 |
| Python fenced blocks parsed | 7/7 |
| Dependency-free Python blocks executed | 4/4 |
| Framework-dependent examples | 3 LangGraph snippets syntax-checked; runtime execution intentionally version-dependent |
| Markdown code fences | Balanced in all sheets |
| Required revision sections | Thirty-second revision, rapid Q&A, lead case, checklist, and primary references present in all sheets |
| DOCX integrity | ZIP container test passed |
| Combined PDF | 35 A4 pages, unencrypted |
| Visual review | Cover, overview, all four section starts, code layout, tables, and final page reviewed |

## Batch 5

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 9,586 |
| Python fenced blocks parsed | 3/3 |
| Dependency-free Python blocks executed | 3/3 |
| Behavior assertions | KV-cache memory, immutable release identity, and replica capacity passed |
| Markdown code fences | Balanced in all sheets |
| Required revision sections | Thirty-second revision, rapid Q&A, lead case, checklist, and primary references present in all sheets |
| DOCX integrity | ZIP container test passed |
| Combined PDF | 33 A4 pages, tagged, unencrypted |
| PDF text extraction | 9,326 words extracted |
| Visual review | Cover, overview, all four section starts, equations/code, representative dense pages, and final page reviewed |

## Batch 6

| Check | Result |
|---|---|
| Source sheets | 4 |
| Approximate source words | 11,683 |
| Python fenced blocks parsed and executed | 2/2 |
| Behavior assertions | Partition sizing and security-scenario validation passed |
| Markdown code fences | Balanced in all sheets |
| Required revision sections | Thirty-second revision, rapid Q&A, lead case, checklist, and primary references present in all sheets |
| DOCX integrity | ZIP container test passed |
| Combined PDF | 33 A4 pages, tagged, unencrypted |
| PDF text extraction | 11,420 words extracted |
| Visual review | Cover, overview, all four section starts, code layout, representative dense pages, and final page reviewed |

## Content checks

- Topic boundaries match the master index.
- Lead cases include requirements, data, metrics, risk, rollout, and monitoring.
- Transformer coverage distinguishes training, prefill, decode, KV cache, MHA/MQA/GQA, FlashAttention, long context, and MoE.
- LLM coverage distinguishes prompting, RAG, fine-tuning, SFT, LoRA/QLoRA, preference optimization, quantization, evaluation, security, and ecosystem roles.
- Library descriptions distinguish Nemotron, NeMo Framework, NeMo Guardrails, serving engines, and training/post-training libraries.
- RAG coverage separates embeddings/vector search, ingestion/chunking, online architecture, generation/citations, evaluation, security, and production operations.
- Retrieval coverage includes sparse/dense/hybrid search, bi-encoders/cross-encoders, exact/ANN, HNSW/IVF/PQ, RRF, reranking, and late interaction.
- Security coverage includes poisoning, indirect prompt injection, current ACL/tenant isolation, cache leakage, privacy, deletion, incident response, and release gates.
- Agent coverage distinguishes deterministic workflows, bounded agents, model-directed loops, single/multi-agent patterns, tools, state, context, memory, HITL, and termination budgets.
- LangGraph coverage distinguishes state updates/reducers, `Command`, `Send`, checkpoints/threads/stores, interrupts, durable execution, streaming, and node caching.
- Framework coverage compares LangChain/LangGraph, Google ADK, OpenAI Agents SDK, LlamaIndex, Haystack, PydanticAI, Microsoft Agent Framework, CrewAI, Agno, Strands, DSPy, and LiteLLM.
- NVIDIA coverage distinguishes Nemotron models, NeMo Framework/Guardrails, NIM, Relay, Helix, and Fabric, and records the official NeMo Agent Toolkit deprecation lifecycle.
- Protocol coverage distinguishes MCP, A2A, service APIs, and events, with identity, authorization, idempotency, retries, backpressure, fault injection, observability, and release evaluation.
- System-design coverage starts from requirements and scale, then covers data/control and serving planes, APIs, storage, caching, queues, consistency, multi-tenancy, security, release, and failure handling.
- Inference coverage separates admission, queueing, prefill, decode, KV-cache memory, continuous batching, prefix caching, quantization, speculative decoding, parallelism, capacity, benchmarking, and autoscaling.
- MLOps/LLMOps coverage records complete release identity across code, runtime, data, model, prompt, index, agent, evaluation, and deployment, with CI/CD/CT gates and progressive rollout/rollback.
- Production monitoring coverage separates service, data, model, GenAI/RAG/agent behavior, safety, business outcome, cost, telemetry health, delayed labels, capacity, and actionable incident response.
- Distributed-compute coverage distinguishes local versus distributed choices, partitions/stages/shuffles, skew, files/table formats, idempotent pipelines, backfills, streaming event time/watermarks, Kafka delivery semantics, and distributed training strategies.
- Security/governance coverage threat-models the application, AI component, data, and action planes; covers prompt injection, RAG/agent/tool boundaries, privacy, supply chain, resource abuse, red-team evidence, NIST/OWASP/MITRE/ISO awareness, and regulation verification.
- Lead-level coverage connects problem framing, metric trees, uncertainty reduction, roadmaps, build/buy/self-host decisions, architecture review, delegation, mentoring, rollout, incidents, fairness, and executive communication.
- Project-defense coverage includes portfolio selection, 30-second/two-minute/20-minute explanations, ownership, leakage, evaluation, impact attribution, production/security follow-ups, behavioral stories, mock cases, and a scoring rubric.

## Known limits

- Syntax parsing does not execute examples against every external dependency or version.
- External links and framework APIs can change after publication.
- Interview coverage varies by employer, domain, level, and project history.
- Production choices still require pinned-version integration, security, load, and model-quality testing.

