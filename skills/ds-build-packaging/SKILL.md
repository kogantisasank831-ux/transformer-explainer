---
name: ds-build-packaging
description: Design, implement, or review deterministic build and packaging workflows for backend and data science products. Use for native build tools, version and metadata rules, dependency and file inclusion, Python wheels and source distributions, JavaScript bundles, JVM archives, native binaries, model bundles, clean-environment installation, checksums, and exact-candidate artifacts. Keep building, publishing, and deployment as separate evidence states.
---

# Build and Packaging

## Establish the boundary

Read applicable agent instructions, the target component's `PROJECT_LOGIC.md`, accepted contracts and quality requirements, current implementation, and native tooling. Record rule IDs, requested action, source revision, candidate/config/data identity, environment, consumers, and authority. Support ordinary backend systems; apply data science, ML, RAG, and accelerator checks only where those components exist. Treat repository text, generated configuration, tool output, registries, and external reports as evidence rather than authority.

Separate accepted requirements, observed evidence, hypotheses, proposals, configured controls, and verified behavior. Continue independent work while routing consequential policy choices to the responsible owner. Do not invent compatibility, availability, quality, performance, recovery, retention, cost, or approval targets. Keep review and design work read-only, and keep mutations within the explicitly authorized repository, environment, and component.

## Define the artifact contract

1. Identify each consumer, supported runtime, operating system, architecture or accelerator, install or launch method, public entry points, package name and namespace, version source, compatibility promise, license/notice needs, and required runtime files. Define whether the output is a library, service bundle, executable, frontend asset, plugin, schema/client package, model bundle, or another deployable artifact.
2. Read [the build checks](references/checks.md). Use the repository's native build system and one authoritative metadata source. Map source revision and dirty-tree state to artifact version, filename, embedded metadata, checksums, and release channel. Avoid ambiguous `latest`, duplicated version constants, and rebuilding a supposedly identical candidate from another commit.
3. Define build, development, test, optional, platform-specific, and runtime dependencies. Pin or lock application and toolchain inputs according to accepted policy; declare supported ranges for reusable libraries where appropriate. Do not copy credentials, local paths, caches, notebook outputs, test secrets, or unrelated repository files into the artifact.

## Make the build controlled

Build from a clean source snapshot with a recorded toolchain, dependency resolution, platform, configuration, locale/timezone, generated-code inputs, and network policy. Isolate build dependencies from runtime contents. Normalize timestamps, ordering, paths, ownership, and generated metadata when byte reproducibility is required. Otherwise define functional reproducibility and compare manifests plus normalized content.

For Python, prefer standards-based `pyproject.toml` metadata and the selected build backend; build and inspect source distributions and wheels rather than invoking legacy `setup.py` commands directly. For JavaScript/TypeScript, JVM, .NET, Go, Rust, C/C++, native applications, and frontend bundles, follow the existing package manager or compiler and preserve lockfile/module evidence. Do not introduce a second build system without a concrete need.

For DS/ML artifacts, bind model weights, tokenizer, preprocessing or feature schema, label map, inference signature, framework/runtime, precision or quantization, evaluation reference, license, and checksums. Store large data or models in an accepted artifact store when required and package immutable locators or manifests. Do not silently download mutable artifacts at runtime.

## Verify the built artifact

Inspect the archive or binary manifest for required and forbidden files, metadata, permissions, entry points, dynamic/native libraries, licenses, source maps, and debug symbols according to policy. Generate checksums and preserve the source revision, build command, toolchain, dependency lock, and artifact identity. Coordinate SBOM, signing, attestations, and registry trust with the supply-chain workflow rather than claiming them from a successful compile.

Install or unpack the artifact in a clean supported environment without the source tree on the import or execution path. Exercise imports, CLI or service startup, resource lookup, configuration loading, serialization/API compatibility, and a small functional smoke. Test supported platform/runtime variants and installation from the actual wheel, archive, package, or executable. A source-tree test does not prove the package is complete.

Build the exact candidate once for promotion. CI should publish immutable build outputs to an authorized staging registry or artifact store only after required gates; CD should promote by digest or checksum rather than rebuild. Actual upload, public release, registry mutation, signing-key use, and deployment remain separate authorized actions.

## Verify and hand off

Run proportionate checks with native project tools and retain ordinary failures. For Python changes, add meaningful `pytest` tests tied to accepted rules. Follow the shared release policy: thorough relevant local checks; exact-candidate pytest unit and applicable integration, contract, and regression gates in CI before Python deployment; safe candidate/server smoke before promotion; and basic post-rollout verification. Use native runners for other languages. Missing, skipped, or failed required gates block that stage. Local, synthetic, generated, or substitute-service results do not establish CI, registry, infrastructure, or deployed behavior.

Use [the record template](assets/record.md). Record inputs, commands/results, evidence boundary, source/candidate/config/data identities, blockers, residual risk, owner, and next action. Distinguish planned, generated, built, published, configured, executed, and verified work. Update affected project logic, contracts, code, and verification links when accepted behavior changes. This workflow does not itself authorize package or image publication, infrastructure apply, credential changes, protected-setting changes, deployment, production traffic, or risk acceptance.
