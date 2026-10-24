# Generated test checks

| Target | Useful property and domain boundary |
|---|---|
| Parser/serializer | Accepted round-trip plus independent canonical examples, malformed rejection, Unicode/escaping, lengths/depth, ambiguity and byte/text boundaries. Never run a generated command string as shell code. |
| Transform/numerics | Input preservation, row/feature alignment, accepted conservation/order relations, duplicates/nulls, bool versus int, huge integers/NaN/infinity and justified tolerances. |
| Stateful backend | Rule-derived preconditions and model state, tenant/object isolation, duplicate/rollback/replay effects and invalid sequences. Do not approximate real database isolation with a model-only proof. |
| Protocol/files | Structured valid frames plus bounded mutations, size/truncation/encoding behavior and accepted error shapes. Separate a local harness from real provider/broker compatibility. |

Use independent oracles and diagnose assumptions before declaring a defect. A self-inverse or differential check can share the same bug on both sides. Over-filtering or returning early can make a property vacuous; inspect generated coverage/examples and keep explicit boundary cases.

Hypothesis examples may share fixture state if lifecycle is broader than each generated call. Build/reset per example where required, and never disable the function-scoped-fixture warning without proving lifecycle isolation. Preserve sanitized failure corpora and tool versions; mutable examples must be fresh objects.

Primary starting point: [Hypothesis strategies](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html). Select installed-version documentation for settings, state machines, shrinking and replay. Do not copy a version-specific reproduction blob without its runtime/tool identity.
