# Planning checks

For each task answer: what accepted outcome changes, what input/prerequisite is needed, which boundary owns it, how is completion demonstrated, what failure/compatibility risk exists, and which work is blocked until it completes?

Prefer vertical behavior slices when practical: contract and expected cases → implementation with verification → integration/operational proof. Use test-first work where it clarifies behavior, not mechanically generated tests or a demand to test every reversible documentation edit.

Distinguish business policy decisions from reversible technical choices. A missing production capacity measurement should block a capacity promise, not all local implementation. A missing cancellation authority should block that mutation path, not unrelated read endpoints.

Record read/write integration contracts between tasks and shared schema ownership. Concurrent tasks touching the same migration or public contract need sequencing or a defined integration point; saying they are parallel does not make them independent.

For migrations include current/target versions, compatibility period, backfill validation, idempotent reruns, cutover proof and recovery limits. For external side effects include unknown-outcome reconciliation before unsafe automatic retries. For DS work include data rights/provenance, labels/time, evaluation isolation and artifact compatibility before quality claims.

A release plan must retain the user's local → mandatory CI pytest → candidate server smoke → promotion → post-deployment verification policy. Tie every required result to the candidate and required profile. A task list or green unrelated CI run is not execution evidence.
