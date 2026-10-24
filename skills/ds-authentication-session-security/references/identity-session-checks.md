# Identity and session checks

| Boundary | Evidence to verify when applicable |
|---|---|
| Token/provider | Trusted issuer/key source, intended audience/token use, validated signature/algorithm constraints, time/required-claim checks and key rotation behavior via supported library/provider configuration. Decoding is not verification. |
| Browser/session | TLS/cookie scope and flags, login/privilege renewal, CSRF origin/token defenses as required, server expiry/invalidation and safe logout. Don't confuse deleting a cookie with revoking a reusable server credential. |
| Refresh/recovery | Atomic one-time token/rotation semantics, replay handling, account enumeration controls, reauthentication and revocation after sensitive changes under accepted policy. |
| Worker/service | Credential audience/scope, least-privilege identity propagation, no trust in user/model-provided tenant headers and no logging tokens. |

Use the installed framework/IdP's primary documentation before selecting APIs and cookie/provider defaults. Define accepted behavior for unavailable identity/revocation services, clock skew and stale sessions; don't silently fail open. Password storage belongs to an appropriate audited password-hashing library and current accepted parameters, not reversible encryption.

Primary starting points: [OWASP Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), and [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html). Scope these to the project's actual browser, API or service identity flow.
