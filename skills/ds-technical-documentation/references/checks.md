# Technical documentation checks

- Define audience, prior knowledge, task/decision, supported versions/environments, sensitivity, discovery path, owner and review trigger.
- Separate tutorials, how-to guides, reference and explanation; give each fact one canonical source and link instead of duplicating it.
- Cover only applicable quick start, architecture, contracts, operations, troubleshooting, security/privacy, migration and contribution needs; preserve authoritative ADR/project logic links.
- Verify commands, config/defaults, permissions, fields, errors and limits from exact source/schema/artifact or execution. Add meaning around generated reference.
- Use copy-safe placeholders and privacy-safe licensed examples; state side effects, expected output, recovery and cleanup. Never publish credentials or destructive defaults.
- For DS/ML, document provenance, versions, intended/excluded use, evaluation/limits, contracts, reproducibility, safety and monitoring only where present.
- Build docs and test links, schemas, snippets, examples and generated drift in clean representative environments; keep failures visible.
- Validate with a target-reader cold task and maintain per release and change trigger. Automated checks and page views do not prove usefulness.

The [Diátaxis framework](https://www.diataxis.fr/) provides a useful separation of tutorials, how-to guides, reference and explanation. Use the authoritative [OpenAPI specification](https://spec.openapis.org/) when documenting HTTP API contracts while pinning the version supported by the target tooling.
