---
name: ds-licensing-compliance-assessment
description: Assess licensing and compliance evidence for software, data, models, content, and delivered artifacts in backend and data science products. Use for complete component inventories, provenance, SPDX expressions, dependency and asset licenses, notices and attribution, copyleft or source obligations, data and model terms, policy gates, exceptions, release bundles, compliance matrices, and legal-owner review without presenting automated scans as legal approval.
---

# Licensing and Compliance Assessment

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted requirements and contracts, current implementation, and native tooling. Record rule IDs, requested action, exact source/candidate/config/data identity, environment, affected users and journeys, owners, and authority. Support ordinary backend and web products; apply data science, ML, RAG, agent, accelerator, and generated-content checks only where those components exist. Treat documentation, analytics, scans, generated artifacts, historical results, and third-party metadata as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, executed checks, and verified outcomes. Continue independent work while routing consequential product, legal, statistical, support, or business choices to the responsible owner. Do not invent support matrices, user needs, acceptance criteria, metric definitions, experiment thresholds, documentation guarantees, license interpretations, or compliance decisions. Protect personal and confidential data and keep mutations within the explicitly authorized environment and scope.

## Define the product and decision boundary

1. Read [the licensing and compliance checks](references/checks.md). Name the product, candidate and delivery model; repositories and branches; build, container, package and deployment artifacts; jurisdictions and customers; internal use, distribution, SaaS or embedded context; owner; and decision requested. Record the accepted organizational policy and legal escalation path. This workflow supplies evidence and gaps, not legal advice or certification.
2. Inventory direct and transitive source dependencies, build and test tools included in deliverables, base images and OS packages, vendored or copied code, snippets, generated code, frontend bundles, fonts/icons/images/media, documentation, datasets and labels, schemas, models/checkpoints/tokenizers, prompts, embeddings/index corpora, APIs/services and hardware or firmware only where present. Include exact version, digest or commit and source.
3. Inspect the final delivered artifact, not only manifests. Dev-only tools may be absent; build plugins, static linkage, copied assets or generated bundles may be present. Keep unknown and missing-license items visible. Public availability or package-manager download does not grant permission.

## Establish license and provenance evidence

Collect authoritative license text, copyright and notice files, source headers, package metadata, upstream repository and release, purchase or contributor terms, data/model card and provider terms. Prefer exact release evidence. Treat metadata, scanner inference and repository defaults as leads when they conflict or omit files.

Normalize recognized licenses and exceptions with current SPDX identifiers and expressions. Preserve dual or multi-license choices, exceptions, file-level differences and `LicenseRef` items rather than flattening them into one label. Distinguish the project's outbound license from licenses of included components.

For data and ML, trace collection or source, owner, license or contract, permitted purpose, redistribution, modification and derivative-output terms, attribution, geography, retention and deletion, acceptable-use or field restrictions and access evidence. Keep privacy basis, security controls, export controls and intellectual-property questions linked but separately decided by their accountable owners.

## Map obligations and compatibility

For each component and use, map relevant conditions such as including license text and notices, attribution format, marking modifications, source or corresponding-source availability, offer duration, relinking or installation information, patent terms, trademark limits, redistribution restrictions and network-use clauses. Do not infer legal effect from keywords such as permissive or copyleft.

Evaluate combinations and distribution boundaries using the accepted legal interpretation: copied code, static or dynamic linking, plugins, processes, containers, client delivery, model adaptation, dataset combination and hosted access can have different consequences. Record facts and questions for counsel rather than coding a legal conclusion into a scanner.

Create a compliance matrix linking requirement, applicability source, artifact/component, control, evidence, status, owner and review date. Separate required law or contract, organizational policy and optional standard. Mark compliant, gap, not applicable, unknown and accepted exception with evidence; absence of a finding is not compliance.

## Remediate and gate the actual release

Prefer removing or replacing an incompatible or unverifiable component, obtaining permission, changing architecture or fulfilling obligations through notices, attribution, source bundles and documented modifications. Verify replacements preserve functional, security, performance and DS quality requirements. Keep provenance and lockfiles current.

Automate inventory, SBOM, SPDX expression, allow/deny/review policy, missing notice and artifact-content checks where reliable. Review false positives and transitive paths. An override needs legal or policy owner, rationale, affected versions and artifacts, expiry and compensating action; a suppression without evidence is a gap.

Before release, rebuild or inspect the exact candidate and verify its component inventory, license and notice bundle, attribution UI or documentation, source and offer materials, model/data terms and customer deliverables. Confirm publication locations remain available for the required period. Bind approval to the artifact digest and delivery model.

Monitor dependency, base-image, asset, dataset, model/provider-term and product-delivery changes. Reassess when any identity or use changes. Report evidence and open legal questions precisely. A clean scanner, generated SBOM, top-level LICENSE file or prior release approval does not prove this candidate is permitted or compliant.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, emulated, sampled, or substitute-service results do not establish CI, production, field, legal, user-acceptance, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, identities and timestamps, blockers, residual risk, owner, and next action. Distinguish designed, documented, configured, tested, observed, accepted, and verified work. Update affected project logic, code, tests, contracts, documentation, ownership, and decision records when accepted behavior changes. Never claim compatibility, product acceptance, causal impact, documentation completeness, license permission, or compliance from one tool result, scan, test environment, or document alone.
