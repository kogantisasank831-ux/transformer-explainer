# Test quality assessment checks

| Concern | Evidence and useful discriminating question |
|---|---|
| Oracle | Would a plausible wrong output/error/effect still pass? Is expected data independent of production helpers? Does a snapshot hide meaningful fields? |
| Coverage | Which accepted rule/boundary/population is exercised? Percentage coverage alone says little about assertion strength or missing tenant/error cases. |
| Mocking | Is actual consumer/adapter/logic called? Does patching the subject or database remove the claimed invariant? What real contract/transaction evidence exists separately? |
| Reliability | Shared mutable fixtures, resource leaks, ordering, retries hiding flakes, unbounded sleeps/waits, random seeds/provider nondeterminism and isolated/parallel execution evidence. |
| Data/ML | Leakage, representative slices, preprocessing/feature alignment, real versus fake model, independently reviewed labels and candidate-matched evaluation. |
| Gate | Collection/selection, ignored exits, missing services, required skips/xfails, exact candidate identity and implemented enforcement versus merely proposed policy. |

Severity reflects consequence and exposure; confidence reflects evidence. A missing test is not proof a production defect exists. A test can be useful within a smaller boundary even when its name claims too much; recommend accurate scope and complementary evidence instead of deleting it reflexively.

Use safe minimal counterexamples to establish weak assertions. If mutation tooling is used, inspect its scope and denominator and distinguish equivalent/untested mutants; don't rank suites by a fabricated or incomparable percentage. Preserve source/tests during assessment unless edits are explicitly requested.
