# Failure and lifetime checks

| Boundary | Inspect and verify |
|---|---|
| Acquisition | If acquisition B fails after A succeeds, A is released. Register cleanup immediately after successful acquisition. Check whether a partially failing constructor/factory owns its own cleanup. |
| Body and close | Attempt all owned releases even if one fails. Preserve the accepted primary-error contract and expose secondary failures through a safe documented mechanism. Verify the context manager does not accidentally suppress errors. |
| Shared dependency | Borrowed clients/pools/models stay alive. Application shutdown owns their closure; per-operation sessions/transactions have their own scope. |
| Async/stream | Parent owns child tasks and resources through cancellation/iteration completion. Handle early consumer exit, generator closure and response disconnect. Bounded cleanup requires real cooperative semantics; an arbitrary timeout is not proof of release. |
| Persistence/effects | Differentiate pending, committed, publication unknown and compensated outcomes. Resource release is not transaction rollback; rollback cannot undo an already completed external effect. |
| Data/model | Invalid records are errors or explicit rejects under accepted policy, never hidden imputation. Model-load failure is distinct from a valid empty result. Temporary files, device resources and process ownership need supported-library cleanup semantics. |

For Python, catch the narrow exception family needed. Preserve causal context internally with appropriate chaining, translate at a stable boundary, and normally re-raise cancellation after cleanup. Avoid catching BaseException indiscriminately or returning from finally. A transaction manager or ExitStack may replace a raised exception with a cleanup exception unless the implementation deliberately preserves the required primary-error contract; test rather than assume.

Choose an explicit secondary-error approach compatible with the supported runtime and public contract: safe attached diagnostics/logging or an approved aggregate-error contract, for example. Do not change a public single-error interface to ExceptionGroup without considering consumers. Never attach credentials or raw records as diagnostic context.

Primary starting point: [Python context managers and exit stacks](https://docs.python.org/3/library/contextlib.html). Select the supported runtime's documentation and inspect the actual client/framework contract before implementing closure or cancellation behavior.
