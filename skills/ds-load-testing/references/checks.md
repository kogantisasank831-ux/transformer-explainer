# Load testing checks

- Name the decision, target/candidate/config/data, authorized environment, topology, dependencies, and owner. Isolate third parties and production data unless explicitly approved.
- Derive scenario weights, arrival/concurrency model, think time, payload/key/tenant distribution, cache/cold state, background load, ramp, duration, and retries from evidence.
- Predefine per-journey percentiles, throughput, errors/timeouts, correctness, queues, saturation, scaling, and recovery gates with windows/populations.
- Smoke-test scripts and assertions first. Verify generator capacity, offered versus achieved rate, connection behavior, clocks, and result loss.
- Observe every relevant tier and correlate timestamps/traces without logging secrets. Report autoscaling and warm-up separately.
- Preserve ordinary failures and aborted/inconclusive runs. Repeat comparable runs and document variance; one run does not establish a stable capacity.
- For ML/GenAI, include input/token/context/model mix, batch/queue behavior, GPU/CPU memory, quality/fallback, and provider limits.

Consult the selected tool's official guidance. Grafana k6 users can review its current [load-testing guidance](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites/) and workload/scenario documentation.
