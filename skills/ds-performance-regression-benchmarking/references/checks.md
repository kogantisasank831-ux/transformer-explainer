# Performance regression benchmark checks

- Define decision, benchmark level, operation, correctness/quality oracle, metric/unit, input/data/model, candidate, immutable baseline, budget and owner.
- Pin or fingerprint hardware, image, OS/kernel, runtime/compiler, dependencies, driver/accelerator, services, limits, topology, config, data and background work.
- Separate cold and warm states; calibrate harness overhead; use independent repetitions and record raw samples, errors/timeouts, throttling, GC/allocation, I/O and noise.
- Report sample count, distribution, variability or confidence, and predefined outlier policy. A single timing or average without context is insufficient.
- Set absolute/relative gates above a characterized noise floor. Treat missing, noisy, drifted or incomparable evidence as inconclusive; do not auto-update baselines.
- Use a fast stable exact-candidate CI subset and dedicated runners for longer or hardware suites. Preserve artifacts, environment fingerprints and trend history.
- Confirm regressions before bisection/profiling; preserve correctness and applicable model-quality or resource guardrails; remeasure the fix at the claimed level.

For Python package benchmarks, the official [airspeed velocity usage](https://asv.readthedocs.io/en/stable/using.html) and [timing guidance](https://asv.readthedocs.io/en/stable/tuning.html) describe historical tracking, regression search, timing calibration, and environmental drift.
