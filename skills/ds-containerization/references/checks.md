# Containerization checks

- Define process, command, ports/interfaces, user, filesystems/mounts, config/secrets, dependencies, probes, shutdown, resources, architectures, and orchestrator contract.
- Use a trusted maintained base by immutable digest with reviewed updates; verify certificates, locale/time, native libraries, and accelerator compatibility.
- Restrict build context and layers. Exclude credentials, repository history, data, caches, and unrelated artifacts; never persist build secrets in args, history, or image contents.
- Separate build and runtime stages; copy the exact artifact; remove compilers and package managers when unnecessary; preserve signal, exit, and PID 1 behavior.
- Run non-root where possible, drop privileges, support read-only root filesystems and declared write paths, externalize config, mount secrets, and log to standard streams.
- Verify model/data digest and GPU driver/runtime boundary when applicable. Define startup, readiness, liveness, and warm-up semantics without probe-induced cascades.
- Inspect and run the final image under representative constraints; test startup, smoke, probes, permissions, writes, resources, termination, and digest identity. Build, push, and deploy remain distinct.

Use the [OCI Image Specification](https://specs.opencontainers.org/image-spec/) for interoperable image structure and current [Docker build best practices](https://docs.docker.com/build/building/best-practices/) for multi-stage builds and base-image pinning, adapted to the selected OCI builder.
