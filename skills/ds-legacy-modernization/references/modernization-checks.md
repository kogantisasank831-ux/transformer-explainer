# Modernization checks

| Boundary | Questions and evidence |
|---|---|
| Callers/contracts | Who consumes imports, routes, files, events, scheduled jobs and CLI behavior? What versions coexist? Preserve error/default/order/permission semantics or explicitly migrate them. |
| Persistent state | Which code owns writes? Can old code read new records? Define expand/backfill/verify/cutover/contract order, duplicate processing, rollback-compatible schemas and nonreversible transformations. |
| Shadow/parallel | Compare the same authorized sanitized workload; isolate writes, notifications, paid calls and external jobs. Differences need adjudication against accepted rules rather than automatic copying of legacy defects. |
| Runtime/dependencies | Supported API/ABI, serialization/pickle or model format, native/GPU stack, plugins and build reproducibility. Never load an untrusted legacy pickle simply to inspect it. |
| Notebook/data/ML | Hidden execution state, preprocessing/features, seeds, data snapshots, leakage boundaries, model/prompt artifacts, evaluation populations, fresh-process execution and batch/output alignment. |
| Cutover/recovery | Traffic/job ownership, in-flight work, checkpoints, observation window, agreed success/abort criteria, responsible owner and recovery from partial progress. Do not assume routing rollback reverses data writes. |

Keep structural refactoring and business correction traceable. Regression fixtures record observed behavior, while rule-based checks determine whether that behavior is acceptable. Use small vertical slices rather than replacing every subsystem and its data schema at once.

Retain compatibility adapters only while needed and document their retirement condition. Do not leave two mutable sources of truth without an explicit consistency/reconciliation design. A migration plan is not an executed migration; a local comparison is not candidate smoke or a measured operating improvement.

When source documentation is missing, reconstruct bounded behavior from code, consumers and sanitized samples and label uncertainty. Resolve only decisions affecting the next slice; keep independent discovery or compatible infrastructure work progressing within scope.
