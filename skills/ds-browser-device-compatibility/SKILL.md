---
name: ds-browser-device-compatibility
description: Define, implement, and verify browser and device compatibility for web interfaces connected to backend and data science products. Use for supported-environment matrices, standards and feature detection, progressive enhancement, polyfills, responsive and input behavior, real-device and automated testing, rendering differences, storage and networking APIs, uploads, streaming, localization, and evidence-based support decisions.
---

# Browser and Device Compatibility

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web products; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, analytics, scans, generated artifacts, historical results, and third-party metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, legal, statistical, support, or business choices to the responsible owner. Do not invent support matrices, user needs, acceptance criteria, metric definitions, experiment thresholds, documentation guarantees, license interpretations, or compliance decisions. Protect personal and confidential data and keep mutations within the explicitly authorized environment and scope.

## Define what is supported

1. Read [the compatibility checks](references/checks.md). Record browser engine and version policy, operating system, device class, viewport and pixel density, input methods, locale and time zone, network conditions, installed or standalone mode, and embedded webview where applicable. Derive the matrix from accepted product policy, user analytics, contracts and technical risk; do not silently equate the developer's browser with support.
2. Group environments into required release gates, extended sampled coverage, best effort and unsupported. State version ranges or update rules, review cadence, owners and end-of-support behavior. Keep accessibility assistive-technology combinations in the accessibility workflow while carrying its accepted environment constraints here.
3. Map critical journeys and risky platform features to the matrix. Include authentication, navigation, forms, tables/charts, uploads/downloads, printing, clipboard, camera or media, storage/cookies, workers, offline/install, long jobs, streaming and generated output only where present.

## Engineer from standards and capability

Prefer standardized HTML, CSS, JavaScript and network behavior. Use feature detection and capability negotiation instead of user-agent assumptions. Use progressive enhancement so the core journey remains understandable and safe when an enhancement is unavailable. If a fallback cannot preserve an accepted invariant, fail explicitly with supported guidance.

Define the source and version of transpilation targets, CSS processing, polyfills and compatibility data. Load polyfills only where needed and test both native and fallback paths. Avoid a polyfill that changes security, timing, precision or data semantics without review. Record unsupported APIs and whether build-time transformation, runtime fallback, alternate workflow or explicit exclusion handles them.

Verify cookies and storage policy, SameSite and partitioning behavior, CORS and redirects, TLS and certificates, service workers and cache updates, WebSocket or server-sent events, downloads and filenames, file types and sizes, media codecs, fonts, date/number formatting, time zones, IME and right-to-left layout where applicable. For DS interfaces, cover canvas or WebGL/WebGPU visualization, large data tables, model or index downloads, token streaming, long polling and local inference only when used.

## Test risk, not a combinatorial fantasy

Create a minimal pairwise or risk-based matrix across engine, OS, viewport, input and feature. Automate stable critical journeys in the actual supported engines with production-like builds and API contracts. Preserve screenshots, console errors, network failures and traces for diagnosis, but do not use screenshot similarity as the only functional oracle.

Use emulators and responsive modes for fast coverage and real devices for behaviors they cannot establish, including touch and virtual keyboard, safe areas, viewport resizing, memory pressure, camera/media, installed mode, GPU rendering and OS browser integration. State cloud-device versus physical-device boundaries. Test cold and warm caches, constrained networks, zoom and orientation where relevant.

Make visual comparisons deterministic through controlled data, fonts, animation, clock and viewport. Review baselines intentionally and isolate expected platform rendering variance from broken layout or hidden content. Test resize and dynamic-content transitions, not only initial screenshots.

## Diagnose and maintain support

Record the exact browser/engine, version, OS, device, viewport, input, build, account/data state and reproduction steps for every failure. Reduce the issue to feature, layout, timing, resource or contract behavior before applying a browser-specific workaround. Verify that a workaround does not break another supported environment.

Gate releases on required environments and accepted critical journeys. Sample extended environments at the defined cadence and use privacy-safe field evidence for failures and adoption. Review the matrix when browser behavior, dependency targets, user share, devices or product features change. A green desktop emulator does not prove mobile-device compatibility, and a compatibility-data entry does not prove the product journey.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, legal, user-acceptance, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, tested, observed, accepted, and verified work. Update affected project logic, code, tests, contracts, documentation, ownership, and decision records when accepted behavior changes. Never claim compatibility, product acceptance, causal impact, documentation completeness, license permission, or compliance from one tool result, scan, test environment, or document alone.
