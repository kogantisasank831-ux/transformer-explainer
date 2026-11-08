# Model serving and inference optimization checks

- Define request/tenant classes, arrival/burst/concurrency, input/output/context distributions, modalities/streaming and accepted latency/throughput/goodput/quality/availability/memory/cost.
- Pin model/tokenizer/template/pre/postprocess/adapters/dtype/quantization, engine/framework/kernels/image/API/defaults and hardware/interconnect/driver/CUDA identities.
- Establish warm/cold reproducible baselines with errors and rejected work; decompose queue, preprocessing, prefill/encoder, decode, tools/retrieval, postprocess and delivery.
- Measure percentile TTFT/inter-token/end-to-end and throughput/goodput plus GPU/CPU/memory/KV/cache/preemption/batch/queue/power/cost by workload class.
- Calculate weight/KV/activation/workspace/margin from actual architecture and parallelism, then verify engine capacity under load.
- Tune batching/sequences/tokens/chunked prefill/scheduling, cache, quantization, kernels/compile, parallelism and speculation one measured bottleneck at a time with quality guards.
- Engineer deadlines/cancel, bounded queues/backpressure/fairness, health/warmup/drain, autoscaling, multi-model isolation, fallback compatibility and recovery.
- Compare immutable candidates under identical workload/hardware, run load and abnormal/recovery checks, and roll out with monitoring and rollback; copied settings and microbenchmarks are insufficient.

Pin the deployed version and consult its native documentation. Current vLLM references include the versioned [`serve` options](https://docs.vllm.ai/en/stable/cli/serve/) for prefix caching, chunked prefill and scheduling, plus [speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/) limitations and validation notes.
