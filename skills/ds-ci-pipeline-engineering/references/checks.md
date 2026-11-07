# CI pipeline engineering checks

- Define triggers, protected branches, fork/bot/merge/release contexts, exact commit, required statuses, matrix, runner trust, duration, and artifact/retention contract.
- Minimize permissions; pin actions/plugins/images; isolate secrets and write/cloud/package tokens from untrusted code; use short-lived identity for narrowly authorized publication.
- Use native commands. Require exact-candidate pytest unit plus applicable integration, contract, and regression gates for Python deployment candidates; use equivalent native gates elsewhere.
- Treat missing, skipped, canceled, quarantined, and failed required matrix jobs as blocking. Preserve ordinary failures and do not make retry or aggregation hide a bad leg.
- Run real ephemeral dependencies for integration claims with readiness, migrations, fixture isolation, and cleanup. Version DS data/models and bound sensitive data and resources.
- Key caches by lock, toolchain, platform, config, and trust boundary; never treat restore as a pass. Preserve reports, environment metadata, and immutable artifact checksums.
- Exercise passing and failing workflow paths, fork-equivalent permissions, artifact install and smoke, and effective repository required-check rules. CI must not implicitly deploy.

The current [GitHub Actions CI guidance](https://docs.github.com/en/actions/get-started/continuous-integration) is one platform example; verify trigger, permission, runner, and protection semantics in the selected CI system's official documentation.
