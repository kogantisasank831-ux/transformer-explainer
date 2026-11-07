---
name: ds-accessibility-verification
description: Implement or verify accessibility for web interfaces used by backend and data science products. Use for accepted WCAG scope, semantic structure, names and states, keyboard and focus, forms and errors, contrast and reflow, media and motion, dynamic updates, automated checks, manual inspection, assistive-technology journeys, data visualizations, generated content, findings, regression protection, and evidence-based conformance claims.
---

# Accessibility Verification

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web systems; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, dashboards, tickets, telemetry, estimates, generated output, and historical examples as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed actions, and verified outcomes. Continue independent work while routing consequential policy or business choices to the responsible owner. Do not invent severity, recovery, handover, cost, performance, accessibility, quality, or acceptance targets. Keep evidence privacy-safe, preserve normal failures, and keep mutations within the explicitly authorized environment, resources, duration, and blast radius.

## Define the accessibility claim before testing

1. Read [the accessibility checks](references/checks.md). Record the product and version, pages, components, states, languages, content, authenticated roles, viewport/device scope, embedded third parties, supported assistive-technology combinations, and the accepted standard and conformance level. WCAG 2.2 is a current technical reference, but legal or contractual applicability and target level come from the responsible owner.
2. Select representative critical journeys and a defensible sample that covers templates, navigation, forms, tables, charts, dialogs, errors, dynamic updates, media, uploads/downloads, long jobs and generated output where present. Include initial, loading, empty, success, invalid, unauthorized, timeout and recovery states. A home-page scan cannot establish product conformance.
3. Preserve reproducible environment, browser, zoom, color mode, assistive technology and test-data details. Protect personal or confidential content in recordings and issue evidence.

## Implement platform semantics first

Use native HTML elements and behaviors before ARIA. Maintain logical headings, landmarks, reading order and page titles. Give controls, images, icons, frames and regions an accurate accessible name and purpose. Ensure programmatic roles, values, expanded/selected/invalid states and relationships match visible behavior. ARIA does not repair an incorrect interaction model.

Make every action available by keyboard without traps, with logical focus order and visible focus. Move focus only for a user-understandable reason; dialogs need initial focus, containment, Escape or accepted close behavior and focus restoration. Preserve focus across route and dynamic updates. Supply alternatives for pointer gestures, dragging and hover-only content.

Give form fields persistent labels, instructions and required state. Associate errors with fields, provide an error summary where useful, preserve entered data, identify correction and avoid color-only meaning. Announce important status changes through a suitable live region without repeatedly interrupting the user. Timeouts and session expiry need accepted warning and extension behavior.

Verify text and non-text contrast, color independence, zoom, text spacing, reflow and orientation against the accepted criteria. Avoid unexpected movement and flashing; honor reduced-motion preferences where applicable. Provide captions, transcripts, audio description or alternatives according to the accepted media scope. Alternative text must communicate the content's purpose, not merely exist.

For data and ML interfaces, give charts a useful title, labels, non-color encoding and an equivalent table or text summary where needed. Expose uncertainty, provenance, validation errors and generated/streaming status accessibly. Keep token streaming or progress announcements bounded. Make filters, feature explanations, retrieval sources and model feedback operable without a pointer.

## Combine automated, manual and assistive-technology evidence

Run automated rules in development and CI for deterministic issues such as missing names, invalid relationships and some contrast failures. Review every finding and suppression. Automated tools cannot judge all semantics, alternative-text quality, focus logic or task usability and cannot establish conformance alone.

Manually inspect headings, landmarks, names, roles, states, reading and focus order, keyboard-only operation, focus visibility, zoom/reflow, high contrast or forced colors, motion, errors, dynamic updates and touch target behavior. Execute critical journeys with the accepted screen-reader/browser combinations and other assistive technologies or settings needed by scope. Test with disabled users where the product and research process support it; keep that usability evidence distinct from standards conformance.

Map each finding to page/component/state, accepted success criterion or rule, user impact, severity source, reproducible steps, evidence, owner and proposed remediation. Fix shared design-system causes before isolated symptoms. Do not suppress a rule because a tool score looks better.

Retest the exact fix and affected journey, add durable component or end-to-end checks where automation is reliable, and sample for regression across templates and states. A conformance statement needs complete scoped evidence, exceptions and owner approval. Report partial coverage honestly when third-party content, inaccessible environments or unsupported assistive technology prevents a conclusion.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, production, field, assistive-technology, billing, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, exercised, observed, accepted, and verified work. Update affected project logic, runbooks, code, tests, dashboards, ownership, and decision records when accepted behavior changes. Never claim an incident resolved, a corrective action closed, a handover complete, savings realized, frontend quality achieved, or accessibility conformance from a document, tool score, estimate, or successful command alone.
