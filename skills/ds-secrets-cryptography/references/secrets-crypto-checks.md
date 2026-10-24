# Secrets and cryptography checks

| Concern | Verify in the scoped design/code |
|---|---|
| Secret lifecycle | Least-privilege source/provider access, no default production secret, safe startup failure, redaction across logs/errors/serialization, version references and ownership. |
| Passwords | Appropriate audited password-hashing library/current accepted work factors and safe comparison; no plaintext/reversible storage or unsalted fast digest as a substitute. |
| Encryption/authentication | Established construction and key/nonce/associated-data constraints, tamper rejection before use, versioned format and context. A round trip alone cannot show misuse resistance. |
| Key separation | Distinct signing/encryption/password/tenant purposes where required, trusted algorithm/key selection and access scope. A service holding all keys may still bypass tenant boundaries. |
| Rotation/recovery | Active writers/accepted readers, revocation policy, format/backups and rollback compatibility, tested recovery without deleting needed old keys blindly. |

Keep random generation, nonce uniqueness and key material management within audited library/provider contracts. Don't demand deterministic ciphertext or leak keys in snapshots. Key-ID/version metadata can aid provenance without storing secret values. Sanitized fixtures are not real provider/transport/control evidence.

Primary starting points: [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), [Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) and [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html). Verify exact library/provider versions and the project's accepted threat/compliance requirements; guidance is not certification.
