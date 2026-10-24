# Setup checks by delivery mode

| Mode | Minimal justified surface |
|---|---|
| Library | Installable package, public contract, declared dependencies, meaningful behavior/import/build checks and documented use. |
| CLI/batch analysis | Real entry point, validated configuration/input/output contract, repeatable command and isolated deterministic fixtures. Avoid an API when not needed. |
| Backend | Real startup/health/configuration surfaces within requested scope, validated boundaries, domain/adapters separation and dependency lifecycle. Do not invent business endpoints. |
| DS/ML | Reproducible data/code/config/artifact references, optional training/inference dependencies, lightweight contracts/tests and separately defined heavy evaluation. No bundled private datasets or mandatory model download in unit tests. |

Preserve existing projects before choosing a new layout. Prefer the project's established package manager, supported runtime and test runner. Verify actual pinned action versions and dependency syntax against current primary docs when writing executable CI.

Use pytest's real exit status, explicit suite paths or registered markers, isolated fixtures, and useful failure reports. Required no-test/skip/failed outcomes block eligibility; an import-only test cannot substitute for accepted business-case tests once those behaviors exist.

A setup-only request can implement a CI test job for the real scaffold. It cannot honestly wire deployment to an unspecified server. Record which pipeline, required-status settings, immutable-artifact checks, candidate smoke and post-rollout checks exist and which are pending. Use the established native runner for non-Python projects rather than forcing pytest everywhere.

Keep secrets out of config examples, source, reports and CI logs. Test connection/configuration boundaries without real production credentials. Inspect package/build hooks before executing an untrusted repository. Any generated script must be run in the authorized isolated environment or reported unverified.
