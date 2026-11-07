---
name: ds-frontend-engineering-quality
description: Design, implement, or review production frontend behavior for backend and data science products. Use for component and state boundaries, typed API contracts, forms, asynchronous work, loading and error states, optimistic updates, security boundaries, rendering, bundles, field and lab performance, testing, observability, long jobs, streaming model output, and release evidence. Route detailed accessibility and browser compatibility to their dedicated workflows.
---

# Frontend Engineering Quality

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web systems; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, dashboards, tickets, telemetry, estimates, generated output, and historical examples as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified outcomes. Continue independent work while routing consequential policy or business choices to the responsible owner. Do not invent severity, recovery, handover, cost, performance, accessibility, quality, or acceptance targets. Keep evidence privacy-safe, preserve normal failures, and keep mutations within the explicitly authorized environment, resources, duration, and blast radius.

## Define the user and contract boundary

1. Read [the frontend quality checks](references/checks.md). Identify supported journeys, roles and tenant boundaries, routes and deep links, frontend framework and version, rendering mode, API/event/file contracts, authentication flow, accepted responsive and performance requirements, build and deployment tooling, telemetry, and current test levels. Keep detailed accessibility and browser/device conformance in their dedicated workflows while preserving their accepted constraints here.
2. Separate domain state, URL state, server/cache state, form drafts and transient view state. Give each state one owner and explicit initialization, persistence and reset behavior. Keep components cohesive and data flow inspectable; avoid a global store for local state or duplicated server truth.
3. Generate or validate types from authoritative contracts where possible and perform runtime validation at untrusted boundaries. Treat client validation as user assistance; the server remains authoritative for security, policy and durable invariants. Render errors from stable codes and fields rather than parsing prose.

## Make asynchronous behavior deterministic

Represent initial, loading, refreshing, empty, success, partial, stale, rejected, unauthorized, rate-limited, offline and unexpected states where applicable. Preserve useful previous data only when the user can see that it is stale or refreshing. Cancel obsolete requests or ignore responses by request identity so slower old work cannot overwrite newer intent.

Define retry ownership and deadline behavior. Avoid multiplying client, gateway and backend retries. Debounce only where accepted, flush or cancel it on navigation, and keep repeated submissions idempotent. For optimistic updates, define temporary identity, reconciliation with authoritative results, rollback, conflict handling and user feedback. Prevent double submission and stale-form overwrites.

Handle pagination, filters, sorting and selection with stable identity and URL semantics where sharing or navigation matters. Preserve focus and user context during updates. Clean up timers, listeners, subscriptions, object URLs, workers, requests and streams on lifecycle changes.

For long-running jobs, show accepted state and progress semantics, durable job identity, reconnect/resume and cancellation behavior. For DS or GenAI output, distinguish generated, retrieved and source data; expose uncertainty or provenance when required; preserve streaming order and partial-output state; apply output validation and guardrails; and make fallback model or stale-index behavior explicit.

## Engineer safe rendering and performance

Use platform semantics, framework escaping and safe URL or content policies. Do not place durable credentials in browser-accessible storage when the accepted authentication design provides a safer mechanism. Cover CSRF, XSS, cross-origin, upload/download and third-party script boundaries through the applicable security workflow.

Measure representative routes, interactions and devices in controlled lab tests and real-user monitoring where authorized. Keep field and lab data separate. Track accepted budgets for JavaScript, CSS, images, fonts, requests, rendering, memory and user-centered metrics. Current Core Web Vitals are useful reference signals, not automatically the product's acceptance criteria.

Reduce work before adding complexity: remove unused code and dependencies, split by real route or feature boundaries, lazy-load noncritical work, optimize images and fonts, avoid render loops and layout thrashing, virtualize only large collections, and move appropriate computation off the main thread. Verify caching and service-worker update behavior so an old shell cannot silently violate a new API contract.

## Test behavior and release evidence

Test pure state and formatting logic at unit level, components through user-visible roles and outcomes, API integration against realistic schemas and failures, and critical journeys end to end. Cover navigation, authorization, form errors, stale and out-of-order responses, offline or dependency failure, optimistic rollback, localization and long-job or model states where applicable. Keep visual snapshots small and intentionally reviewed.

Validate the production build, asset references, source-map policy, configuration, cache headers and exact deployed candidate. Observe browser errors, failed resources, route and API failures, Web Vitals or accepted performance measures and critical journeys after rollout. A development-server test or perfect Lighthouse score does not prove production correctness or field performance.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production, field, assistive-technology, billing, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, exercised, observed, accepted, and verified work. Update affected project logic, runbooks, code, tests, dashboards, ownership, and decision records when accepted behavior changes. Never claim an incident resolved, a corrective action closed, a handover complete, savings realized, frontend quality achieved, or accessibility conformance from a document, tool score, estimate, or successful command alone.
