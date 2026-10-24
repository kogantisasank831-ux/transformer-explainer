# Implementation checks

Select only checks implicated by the change; record why an excluded concern is not applicable.

| Surface | Inspect and verify |
|---|---|
| Backend/API | Schema and error compatibility, auth/object ownership, transaction atomicity, duplicate requests, pagination/order, connection lifetime, realistic timeout/failure behavior. |
| Pure transformation | Input mutation, nulls/NaN/infinity, empty/boundary inputs, precision, ordering, time units/time zones, deterministic output and bounded memory. |
| Data pipeline | Schema drift, partial batches, checkpoint/publication atomicity, retries/replay, provenance, rejected records, no implicit overwrite or silent data loss. |
| ML/inference | Feature order/types, preprocessing parity, versioned artifacts/config, safe loading, batch/output alignment, resource bounds and explicit invalid-input/failure behavior. Never train on evaluation data or manufacture quality evidence. |
| RAG/agent | Untrusted retrieved/tool content, permission checks per resource/tool, validated outputs, bounded tool/retrieval steps, trace IDs without secret payloads, approved refusal/fallback behavior. |

For notebook extraction, isolate a deterministic callable from I/O, declare dependencies/configuration, remove hidden state and verify from a fresh process. Do not move exploratory charts, training or expensive downloads into application imports.

Use real tests for observable invariants. For external systems, test the adapter with controlled responses and separately record integration evidence; a mock cannot prove the remote schema, transaction or permission enforcement. Prefer existing project style/lint/type tooling; justify dependency changes and verify APIs against official documentation for the supported version.
