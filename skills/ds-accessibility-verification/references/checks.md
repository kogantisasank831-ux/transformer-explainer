# Accessibility verification checks

- Record exact product/version, pages/components/states/languages/roles, viewports/devices, third parties, AT/browser combinations, and accepted standard and level; do not infer legal applicability.
- Sample critical journeys, templates, forms, tables/charts, dialogs, errors, dynamic content, media and applicable long-job/generated-output states. One scan cannot establish conformance.
- Prefer native semantics; verify headings/landmarks/order/title, accessible names, roles, values, states and visible/programmatic consistency.
- Test keyboard access, focus order/visibility, dialogs and restoration, pointer alternatives, labels/instructions/errors, live regions, timeouts and preserved input.
- Verify accepted contrast, color independence, zoom, spacing, reflow, orientation, reduced motion/flashing and media alternatives; evaluate alternative-text quality.
- For DS/ML, provide non-color chart meaning, equivalent summaries, uncertainty/provenance, bounded stream/status announcements and keyboard-operable filters and sources.
- Combine reviewed automated results with manual inspection and representative assistive-technology journeys. Automation assists testing and cannot determine accessibility alone.
- Map findings to criterion, state, user impact, reproducible evidence and owner; retest exact fixes, add reliable regression checks, and state exceptions and coverage limits.

Use the W3C [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/), [WAI evaluation guidance](https://www.w3.org/WAI/test-evaluate/), and [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) as primary technical references. Verify the target's accepted legal and contractual requirements separately.
