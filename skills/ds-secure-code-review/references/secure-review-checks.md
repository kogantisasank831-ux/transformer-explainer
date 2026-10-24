# Secure review checks

| Surface | Concrete questions |
|---|---|
| Identity/authority | Is token/session verification real? Is tenant/object/function permission enforced from trusted identity on every relevant path, including cache/worker/export? |
| Input to sink | Are query/process/path/template/URL/deserialization operations safe for the actual input and library? Is normalization consistent with the permission check and operation? |
| Data/effects | Are secrets/private data exposed by logs, errors, cache keys, URLs or responses? Can retries, partial failures or untrusted tool arguments perform unauthorized effects? |
| Runtime/config | Are debug/admin/test bypasses reachable? What credentials, egress/filesystem privileges and resource bounds actually apply? |
| DS/GenAI | Does untrusted retrieval/model output cross an authority or execution boundary? Are artifacts loaded safely and data/model/provider scopes explicit? |

Document an actionable mechanism and reachable supported preconditions. Distinguish code evidence from runtime configuration and hypothetical exploitation. Authenticated users can still be adversaries across object/tenant boundaries. A missing test is evidence of a verification gap, not automatically proof of an exploitable flaw.

Primary reference for exposed API boundaries: [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). Use the actual stack's primary documentation for version-sensitive behavior; broad recommendations do not replace tracing the code.
