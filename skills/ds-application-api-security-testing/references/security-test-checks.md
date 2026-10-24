# Application/API security checks

| Boundary | Scoped verification |
|---|---|
| Identity/authority | Missing/invalid/expired credentials as supported, cross-object/function/tenant access, cache and worker/tool bypasses. Use synthetic identities; authentication alone doesn't grant all actions. |
| Input/sink | Relevant type/length/encoding/canonicalization cases and safe query/path/process/URL adapters with controlled sinks. Parameterize only supported scenarios; no arbitrary external payload targeting. |
| Protocol/browser | Actual method/status/content-type/redirect/header/cookie/CSRF behavior when supplied; CORS/header checks alone do not prove access control. |
| Data/errors/logs | Minimal synthetic sentinels to detect inappropriate response/log exposure; redact evidence and don't preserve credential values. |
| Effects/recovery | Rejected operations have no unauthorized effects; duplicates/retries/partial failures preserve accepted security invariants. Use bounded fixtures, not real payments/notifications. |

State target and stop conditions before execution. Infrastructure or dependency absence is unverified/blocked evidence, not a green skip. Deep load/fuzz/exploit chains need their own scoped environment and budgets; a local security test suite isn't a full penetration test.

Primary starting points: [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) and [REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). Select relevant versioned guidance and actual stack docs; do not copy an evolving checklist into a claim that all controls were tested.
