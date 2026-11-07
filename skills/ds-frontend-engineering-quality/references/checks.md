# Frontend engineering quality checks

- Record journeys, roles/tenants, routes, rendering mode, framework, API/auth contracts, accepted responsive/performance constraints, build/deployment and telemetry.
- Separate domain, URL, server/cache, draft and view state with one owner, lifecycle and reset rule. Validate untrusted runtime data and use stable error codes.
- Cover initial/loading/refresh/empty/success/partial/stale/error/auth/rate/offline states. Cancel or identify requests so stale responses cannot overwrite current intent.
- Define retry, deadline, debounce, idempotent submission, optimistic reconciliation/rollback, pagination identity and cleanup behavior.
- For long jobs or DS/GenAI, preserve durable job and stream state, cancel/resume, output contracts, provenance/uncertainty, guardrails and explicit fallback behavior where required.
- Protect rendering/auth/cross-origin/upload/third-party boundaries with platform and framework controls; route specialist security testing appropriately.
- Measure representative lab and field performance separately against accepted budgets; inspect bundles, assets, rendering, memory, caching and service-worker compatibility.
- Test user-visible behavior across unit, component, realistic integration and critical E2E layers; validate the exact production build and post-rollout errors and journeys.

Use the [HTML Living Standard](https://html.spec.whatwg.org/) for platform behavior and current [Web Vitals guidance](https://web.dev/articles/vitals) for field-oriented performance signals. Verify current metric definitions when creating a target-specific gate.
