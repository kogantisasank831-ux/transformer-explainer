# Licensing and compliance assessment checks

- Define product/candidate, repositories and final artifacts, delivery/use model, jurisdictions/customers, policy, accountable owner and legal escalation; do not present the workflow as legal advice.
- Inventory exact direct/transitive dependencies, base images/packages, vendored/generated/copied code, frontend/assets/docs, data, models/tokenizers, prompts/index corpora and external services where present.
- Collect authoritative release license text, notices, headers, upstream source and contracts; inspect artifact contents and keep unknown or missing-license items visible.
- Normalize SPDX identifiers/expressions, exceptions, dual choices and file-level differences without flattening evidence or confusing component and outbound licenses.
- Map license/data/model obligations and compatibility to actual use and delivery. Separate legal/contract, policy and optional-standard requirements in an evidence-linked matrix.
- Remediate through removal/replacement, permission, architecture or fulfilled notice/source/attribution obligations; verify product and DS behavior after change.
- Automate reliable inventory and policy gates, review transitive paths and false positives, and require owner/rationale/scope/expiry for exceptions.
- Verify the exact release artifact, notices, source materials and delivery locations. Reassess identity or use changes; scans, SBOMs and a top-level license are not approval.

Use current [SPDX specifications](https://spdx.dev/use/specifications/) and the [SPDX License List](https://spdx.dev/learn/handling-license-info/) for machine-readable identities. The [OpenChain ISO/IEC 5230 license compliance specification](https://openchainproject.org/licensecompliancespecification) provides a process reference; legal interpretation remains with the authorized legal owner.
