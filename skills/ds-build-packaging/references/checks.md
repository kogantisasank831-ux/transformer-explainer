# Build and packaging checks

- Define consumers, artifact type, name/version source, supported runtimes/platforms/architectures, entry points, compatibility, licenses, contents, and install or launch contract.
- Record source revision and dirty state, native build tool, toolchain, dependency lock/resolution, config, generated inputs, platform, and network use.
- Separate build/test/dev/optional/runtime dependencies. Exclude secrets, local paths, caches, notebook outputs, and unrelated files; inspect the final manifest.
- Make ordering, timestamps, paths, ownership, and generated metadata reproducible where required, or define and test functional reproducibility explicitly.
- For DS/ML bundles, bind weights, tokenizer, preprocessing/features, signature, runtime, precision/quantization, evaluation reference, licenses, and immutable checksums or locators.
- Install and run the actual artifact in clean supported environments; verify metadata, entry points, resources, native dependencies, permissions, compatibility, and a meaningful smoke.
- Preserve artifact checksum and build evidence. Keep build, publish, sign, promote, and deploy states distinct; never rebuild an already identified promotion candidate.

Python projects should use the current [PyPA packaging flow](https://packaging.python.org/en/latest/flow/) and version-matched build-backend guidance for source distributions and wheels.
