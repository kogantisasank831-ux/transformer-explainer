# Concurrency checks

## Coordination boundaries

| Boundary | Check |
|---|---|
| One event loop | Await points between read/check/write, blocking calls and CPU work, task ownership and event-loop-bound resource lifetime. An asyncio lock coordinates tasks using that lock; it does not coordinate OS threads or replicas. |
| Threads | Appropriate thread synchronization, library/client/model thread safety, context propagation, executor capacity and shutdown. Do not rely on interpreter behavior as an application transaction. |
| Processes/replicas | Independent memory/locks, connection/model initialization after fork/spawn, shared-store atomicity, uniqueness, transaction isolation, idempotency and lease expiry/fencing. |
| Durable queue | Delivery and acknowledgment semantics, claim visibility/lease, retries after commit-before-ack, atomic state/effect recording and deduplication retention/equality policy. |
| Model/GPU work | Framework/model mutation, batch alignment, device-stream semantics, nonpreemptible operations, device memory bounds and safe cleanup. Do not assume async makes CPU inference parallel or releases accelerator memory immediately. |

## Python semantics to verify against the supported version

Use native async clients for I/O where appropriate. Offloading blocking I/O to a thread can protect loop responsiveness, but canceling its awaiting coroutine does not forcibly stop running thread work. CPU-bound work requires a justified execution strategy and library/runtime evidence; threads are not a universal speedup.

Check task-group versus gather failure semantics before selecting either: sibling lifetime and cancellation behavior must match the contract. Clean up in finally/context managers; normally propagate cancellation after cleanup rather than swallowing it. Shielding is a deliberate lifetime choice, not a general cancellation fix. Confirm timeout semantics and whether cleanup can exceed the nominal deadline.

An async semaphore bounds entrants to its protected region; separately bound producers and pending tasks. Async synchronization primitives are not thread-safe. Use database constraints/transactions for cross-worker durable invariants rather than a local asyncio.Lock. A uniqueness constraint alone may prevent duplicate rows while still allowing duplicate external effects; define atomic outbox/idempotency/reconciliation as required by the accepted contract.

## Primary documentation

Start from the project's installed version and choose matching documentation before coding:

- [Python task lifetime, cancellation, task groups, timeouts and thread offloading](https://docs.python.org/3/library/asyncio-task.html).
- [Python asyncio synchronization scope](https://docs.python.org/3/library/asyncio-sync.html).
- [pytest controlled patching of dependencies and environment](https://docs.pytest.org/en/stable/how-to/monkeypatch.html).

Record concrete guarantees tested and what remains unknown. A concurrency regression suite is not a load/capacity benchmark or a distributed-system proof.
