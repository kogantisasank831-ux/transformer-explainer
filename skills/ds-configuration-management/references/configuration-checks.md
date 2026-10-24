# Configuration checks

| Concern | Required distinction |
|---|---|
| Precedence | A source's presence versus truthiness; independent fields versus full/nested replacement; constructor/CLI/environment/file/default order as actually implemented. |
| Parsing | Strict versus permitted coercion, enum spelling/case, bool encodings, integer versus bool, finite numeric values, units/time zones, null/empty and duplicate keys. |
| Startup | Validate complete snapshot before external effects; supported import path must not require production credentials merely to import pure logic. |
| Secrets | Never include values in repr/validation messages, full connection URLs, crash logs, copied fixtures or fingerprints. Redaction of a field type does not guarantee every serialization/exception path is safe. |
| Reload | Reject invalid new settings without partial activation; preserve the old valid snapshot. Define in-flight requests/jobs and secret/client lifetime explicitly. |
| Reproducibility | Record nonsecret effective settings, source revisions and model/data/prompt/config identities. Host env changes between runs must not silently alter an already established snapshot. |

Use isolated mappings or fixtures for environment tests and restore modifications. Verify conflicts at each source boundary, not just the final happy path. Keep development `.env` examples nonsecret, do not auto-load a surprising parent-directory file, and avoid unscoped reads of a user's real environment or secret store.

Keep operational policy distinct from parsing. A loader may validate an accepted timeout or threshold; it does not decide a product's acceptable latency, inference confidence or data-retention duration. Unknown settings should follow the component's documented strict/compatibility behavior rather than a universal new rule.

For schema tooling, consult [Pydantic Settings primary documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) if applicable, then select the installed version. Source priority, aliases, dotenv handling and secret serialization are version/tool-specific; do not copy latest-only APIs into an older project.
