# Token, context and inference cost checks

- Define outcome/workload/tenant classes, accepted quality/safety/latency, budget and price source/effective date, owner and overage action.
- Pin model/runtime/tokenizer/template, prompt/workflow/tools, retrieval/cache/router/settings and hardware/deployment identities.
- Include tokens and modalities, cache, embeddings/reranking, retries/steps, storage/network, compute/idle capacity and operations; separate estimate, meter, allocation, invoice and realized cost.
- Aggregate physical calls to logical outcome and reconcile tokenizer estimates, provider/engine usage, traces, counters and billing for failed/cancelled work too.
- Report distributions and high-percentile unit cost by workflow/model/tenant/version/failure, not only averages or successful calls.
- Allocate context with output reserve and safety margin; count after actual serialization and define relevance, priority, truncation, clarification and async behavior.
- Preserve decisions, prohibitions, identifiers, units, blockers and provenance through tested compaction; a fluent summary is not lossless memory.
- Govern prompt/semantic cache identity, tenant/privacy, freshness, TTL and invalidation; measure useful reuse and false hits.
- Evaluate routing, cascades, batching and retry/agent amplification end to end; keep safety and permissions independent of model tier.
- Enforce atomic fair call/token/time/cost budgets with reservation/reconciliation and typed warning/degrade/stop/exception behavior.
- Compare quality-cost candidates on locked slices and verify realized savings under comparable demand, price, mix and quality after rollout.

OpenTelemetry defines evolving [GenAI usage attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) for common instrumentation. Serving engines may expose computed and cached token measures; for example, vLLM documents [automatic prefix caching](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/). Pin actual versions and reconcile to the provider or infrastructure bill.
