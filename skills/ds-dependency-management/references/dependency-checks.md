# Dependency checks

| Layer | Evidence to inspect |
|---|---|
| Direct/transitive | Why used, declared API compatibility, resolved constraints, extras/markers, unused import versus dynamic/plugin use, and the transitive diff. |
| Library/application | Library metadata expresses supported ranges; a deployment resolution pins a concrete supported environment. A freeze from an arbitrary laptop is neither by itself. |
| Build/runtime/dev | Build backend and build-isolation requirements; runtime install graph; tests/lint tools separate from shipped runtime. Verify an installed wheel outside the source directory when packaging is in scope. |
| Platform/native | Interpreter ABI, OS/architecture, compiler/system libraries, available wheels, database drivers and target-specific markers. One Linux install cannot prove Windows/macOS support. |
| GPU/model | Driver/runtime/framework compatibility, accelerator wheels/index, tokenizer/serialization/quantization support, artifact loading and model metadata. A successful pip resolver cannot prove CUDA execution or prediction parity. |
| Provenance/reproduction | Trusted indexes/sources, exact versions and relevant artifact hashes, complete applicable graph, immutable references and documented target/tool versions. Do not expose registry credentials in logs or lock URLs. |

For dependency removal, inspect runtime imports, optional entry points/plugins, notebooks/jobs and artifact formats; an absence in one module is insufficient. For upgrades, review official migration/release notes and meaningful affected behavior. Avoid unrelated sweeping updates.

Use the existing manager's locked/frozen install mechanism when appropriate and supported. Keep generated lockfiles regenerated with the actual resolver; verify they apply to the intended platform and extras. Retain upstream integrity checks and avoid unsupported binaries. Hashes improve artifact identity/integrity but do not prove the code is trustworthy.

Primary Python starting point: [pip repeatable installs](https://pip.pypa.io/en/stable/topics/repeatable-installs/). Consult the project's manager and packages' primary documentation for exact version semantics. Mark checks not executed, scanner coverage, unsupported platforms and GPU tests explicitly; do not claim vulnerability-free or fully reproducible operation from pinning alone.
