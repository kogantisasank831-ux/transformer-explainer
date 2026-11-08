---
name: ds-model-serving-inference-optimization
description: Design, profile, and optimize production model serving for classical, deep learning, embedding, reranking, multimodal, and generative workloads. Use for exact model and runtime identity, workload and SLO contracts, queue-prefill-decode profiling, GPU and KV-cache capacity, batching and scheduling, prefix caching, quantization, parallelism, compilation, speculative decoding, streaming, backpressure, autoscaling, multi-tenancy, quality equivalence, load evidence, and safe rollout.
---

# Model Serving and Inference Optimization

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data/model identity, environment, affected users and consumers, owners, and authority. Support ordinary backend retirement where applicable; use ML-specific validation, training, evaluation, and serving controls only for systems that contain those components. Treat documentation, registries, dashboards, experiment trackers, generated reports, and provider metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, data, model-risk, retention, quality, or release choices to the responsible owner. Do not invent usage, retention, quality, reproducibility, fairness, safety, latency, throughput, cost, or acceptance targets. Protect personal, confidential, licensed, and model-sensitive data and keep mutations within the explicitly authorized environment and scope.

## Define the serving contract and exact stack

1. Read [the inference optimization checks](references/checks.md). Record request types and populations, arrival rate and bursts, concurrency, input/prompt and output length distributions, context maximum, modalities, streaming, priority and tenant mix, batch/offline versus online behavior, accepted latency/throughput/goodput, quality, availability, memory and cost requirements. Do not optimize a single average request when production has a tail.
2. Bind model family and exact revision/digest, tokenizer and chat template, preprocessing/postprocessing, adapters, dtype and quantization, engine and version, framework/compiler/kernels, container, API schema and generation defaults. Record GPU/accelerator type and count, memory, interconnect, CPU/RAM/storage/network, driver and CUDA/runtime. GQA/MQA/MHA, layers, head dimensions and context behavior come from the model architecture, not a tuning guess.
3. Establish a reproducible baseline using production-like traffic and fixed candidate/config. Warm up explicitly and separate cold start. Record errors, timeouts and rejected work rather than measuring only successful requests.

## Measure the complete inference path

Decompose client/network, admission and queue, preprocessing/tokenization, model load, prefill/encoder, decode/generation, retrieval/tools where present, postprocessing and streaming delivery. For generative serving measure end-to-end latency, time to first token, inter-token or time per output token, output completion, tokens or requests per second and goodput within SLO. Use percentile distributions by request class and concurrency.

Measure GPU utilization, memory and bandwidth, compute, CPU, RAM, transfer, cache hit, KV-cache use, blocks/evictions, preemption/recompute, batch occupancy, scheduler queues, prefix lengths, speculative acceptance, power and cost. Correlate server and client timestamps. A high GPU utilization number alone does not prove efficient or useful service.

Estimate weight, KV-cache, activation, workspace, graph/compile and safety margin from the actual architecture, precision, context and parallel layout. Treat the calculation as a feasibility bound and verify with engine-reported capacity and controlled load. Account for fragmentation, replicas, adapters and non-model processes.

## Tune one evidence-backed bottleneck

Adjust concurrency and admission, continuous/dynamic batching, maximum sequences, batched tokens, chunked prefill, scheduling and priorities against the measured length and arrival distributions. Balance prefill throughput against decode latency and prevent long prompts from starving interactive requests. Bound queues and return actionable overload behavior.

Use prefix or prompt caching only for stable repeated prefixes with explicit key semantics, invalidation, memory bounds and tenant/privacy isolation. Verify actual hit rate and saved compute; a configured cache with unique prompts may add overhead. Never share sensitive cache entries across an unauthorized boundary.

Evaluate weight, activation or KV-cache quantization, optimized kernels, compilation/graphs, fused operations and CPU offload with exact compatibility and quality gates. Measure load/warm-up, memory, throughput and tail latency. Quantization support in a file or engine does not prove numerical or task quality.

Choose tensor, pipeline, data or expert parallelism from model fit, topology, communication and workload. Measure scaling efficiency and failure domain. More GPUs can reduce efficiency. For speculative decoding, choose draft or n-gram method from workload, measure acceptance and overhead, and verify output/quality behavior; feature support and result stability depend on the pinned engine version.

## Engineer production behavior and release

Define health/readiness, model load and warm-up, startup and shutdown, request cancellation and deadlines, streaming disconnect, retry/idempotency, backpressure/rate limits, priority/fairness, autoscaling signals and stabilization, draining, replicas and failure recovery. Prevent a retry storm or autoscaler from exceeding GPU, provider or downstream capacity.

For multi-model or adapter serving, bound residency, load/unload, fragmentation and noisy-neighbor effects. Validate model selection and response metadata. Ensure fallback preserves schema, safety and accepted quality; fail explicitly when it cannot.

Compare each candidate against the same immutable model, workload, hardware and quality set with repeated trials and uncertainty. Run applicable unit/contract tests, load and stress/spike/soak tests, memory-leak and recovery checks. Retain ordinary OOM, rejection and timeout evidence. A microbenchmark does not establish service capacity.

Roll out the exact image/model/config progressively with abort and rollback. Monitor request mix, queue, TTFT and decode latency, throughput/goodput, errors/OOM, cache/preemption, utilization, cost and delayed quality. Revisit tuning when model, engine, driver, hardware, traffic or quality requirements change; copied settings from another model or vLLM version are not a validated configuration.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, restoration, model quality, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish planned, configured, executed, observed, accepted, released, retired, and verified work. Update affected project logic, code, tests, contracts, data/model records, documentation, ownership, and decisions when accepted behavior changes. Never claim decommissioning, data fitness, reproducibility, model approval, or inference optimization from a plan, successful command, tracked run, aggregate score, or theoretical calculation alone.
