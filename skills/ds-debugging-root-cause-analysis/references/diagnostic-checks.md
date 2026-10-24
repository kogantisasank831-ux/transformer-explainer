# Diagnostic checks

## Discriminating evidence

| Failure | Useful comparison |
|---|---|
| API/authorization | Same object under different authenticated scopes, route versus persistence behavior, schema/error status against contract, dependency response and exact request ID. |
| Worker/effects | Enqueue/claim/commit/ack timeline, duplicate delivery, retry policy, partially committed operations, dependency failure and shutdown boundaries. |
| Data/result drift | Input/schema/snapshot identity, join counts, nulls/units/time zones, sorting/index alignment, feature/preprocessing/artifact versions and evaluation population. |
| ML/GenAI variability | Same model/prompt/config/retrieval snapshot and seed scope where meaningful, external-provider changes, leakage, tool traces and approved quality definitions. Do not infer model degradation from a single anecdote. |
| Flaky/concurrent behavior | Controlled event/barrier interleaving, shared mutable state, ordering/atomicity, cancellation and cleanup. Repetition can expose a failure but a passing loop does not prove absence. |
| Slow/memory-heavy paths | Comparable input/workload/environment, trace/profile evidence, query count/plan, CPU/I/O/memory boundary and baseline. Avoid synthetic throughput claims or production load without authorization. |

Record exact diagnostic commands and sanitized output needed to reproduce. Use temporary paths and controlled adapters. Never log full credentials, prompts with sensitive data or raw production tables. Do not run destructive probes, uncontrolled downloads, training or public traffic generators as routine debugging.

Use a compact hypothesis ledger with statuses untested / supported / contradicted / unresolved. Prefer experiments that would produce different observations for competing explanations. Retain contrary evidence. A root-cause statement should explain when and why the defect occurs and how the fix interrupts that chain.

For framework/runtime-specific semantics, verify the project's supported version in primary documentation. Test behavior at the actual boundary; mocking the suspected mechanism away may hide the defect rather than diagnose it.
