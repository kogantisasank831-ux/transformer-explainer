# Containerization record

- Component, rule IDs, owner, source/artifact identity, builder/runtime versions, and target platforms:
- Base tag/digest, final image tag/digest, command, user, ports, mounts, config/secrets, and resource contract:

| Stage / layer | Inputs and purpose | Identity / cache boundary | Runtime contents / privilege | Verification |
|---|---|---|---|---|

## Runtime behavior

Record PID 1 and signal behavior, shutdown deadline, readiness/liveness/warm-up, filesystems and writes, network/dependencies, logging, architecture/native libraries, GPU/model boundary if applicable, and prohibited-content inspection.

## Handoff

List build/run/inspect commands and results, clean image smoke, digest and artifact references, scan/SBOM/signature status, registry/deployment status, failures, residual risks, owners, and next actions.
