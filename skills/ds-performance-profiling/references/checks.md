# Performance profiling checks

- Record candidate/config, environment/hardware/runtime, input/data/model identity, concurrency, warm-up, repetitions, cache state, and correctness oracle.
- Start with system-level CPU, memory, I/O, queue/lock, dependency, and accelerator metrics; choose profiler from a named hypothesis.
- Distinguish sampling from deterministic tracing and measure tool overhead. Interpret self versus cumulative time and on-CPU versus waiting.
- For memory, inspect peak/live/retained/allocation/native/GPU categories and compare equivalent lifecycle points. Protect sensitive profile data.
- For async/concurrency, include event-loop lag, pool/queue/lock wait, runnable state, backpressure, and cancellation.
- For ML/GPU, separate load/preprocess, transfer, kernels, synchronization, compilation, batching, collectives, and postprocess; record framework sync behavior.
- Confirm a hotspot independently, change one dominant cost, rerun the same baseline, and report tradeoffs. Profiling does not prove load capacity.

Use official tooling for the actual runtime. Python users can consult the current [profiling documentation](https://docs.python.org/3/library/profiling.html) and version-matched `cProfile`/sampling guidance.
