# Supply-chain checks

- Trace resolver precedence across private/public indexes, similarly named packages, VCS/editable dependencies, build hooks, native binaries, and platform-specific resolution. Reproducible resolution does not prove reproducible bytes or trustworthy origin.
- Separate development, build, and runtime graphs. For models, record immutable revision, digest, format, loader settings, license, and origin before loading. Do not deserialize arbitrary objects merely to inspect them.
- Inspect fork/event permissions, privileged follow-up jobs, persistent runners, artifact naming collisions, cache boundaries, and secret exposure. An untrusted artifact does not gain trust from its filename.
- Derive signer, builder, source, and parameter expectations from trusted configuration rather than from the attestation being verified. Promote the same immutable bytes; a rebuild is a new candidate.
- Record exceptions with scope, decision maker, expiry, and compensating controls. Do not grant exceptions or claim a SLSA level from isolated configuration review.

Consult the current [SLSA artifact verification guidance](https://slsa.dev/spec/v1.2/verifying-artifacts) and official documentation for the actual package ecosystem, verifier, registry, CI provider, and artifact format.
