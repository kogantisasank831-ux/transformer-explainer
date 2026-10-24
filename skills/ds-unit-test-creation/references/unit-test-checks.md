# Unit test checks

| Behavior | Useful cases and assertions |
|---|---|
| Validation/decision | Missing versus explicit null/empty/zero/False; supported numeric types including bool exclusion, NaN/infinity/precision; boundary equality; approved exception/code and no unauthorized effects. |
| Transform/data | Independent expected rows/values, ordering/index/feature alignment, duplicates, join/cardinality/null/time-unit semantics, empty input and input preservation. |
| Service orchestration | Controlled success, rejection and dependency failure; correct tenant/object scope forwarded; intended side-effect counts and cleanup. Mock evidence does not prove the real dependency honored them. |
| ML/GenAI boundary | Controlled prediction/tool output validation, preprocessing/output alignment, bounded fallback according to accepted policy, version/config passed correctly. No accuracy claim from a fake model. |

Avoid deriving the expected value by calling the same production helper or copying its algorithm. Use hand-calculated examples, independent invariants or accepted fixtures. Parametrization should make a failed case diagnosable, not hide an enormous opaque loop. Compare numerical tolerances only from a justified accepted contract; don't relax them after failure without evidence.

Use temporary paths, injected environments/clocks and minimal fakes. Restore patches and close owned resources even when setup partly fails. Mock patch location and lifecycle must match how code looks up its dependency; otherwise the test may accidentally call the real service. Assertions on private implementation details tend to break harmless refactors.

Do not confuse coverage with correctness: a high percentage can coexist with no meaningful oracle. Do not write an assertion for each line or require 100% by default. Preserve mandatory test failures, and record optional/skipped cases explicitly.

Primary pytest references: [fixtures and teardown](https://docs.pytest.org/en/stable/how-to/fixtures.html) and [test/package layout](https://docs.pytest.org/en/stable/explanation/goodpractices.html). Match the installed version and project configuration before selecting APIs.
