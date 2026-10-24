# Authorization checks

| Surface | Verify |
|---|---|
| Policy | Explicit resource/action/tenant matrix and trusted identity; missing/unknown access denied; no accidental privilege from naming a role or supplying another tenant ID. |
| Data/API | Object lookup, filtered lists/counts, bulk mutations, exports/files, nested resources and consistent safe errors. Check the actual acted-on object, not an unrelated precheck. |
| Cache/retrieval | Scope by relevant tenant/resource/policy/version and revalidate under accepted freshness/revocation rules. Cross-tenant same-key fixtures must exercise hits and misses. |
| Worker/tool | Trusted origin/context, execution-time policy as specified, no identity from untrusted content, credential scope, side-effect authority and safe retry behavior. |
| Storage/index | Actual constraint/RLS/filter/ACL configuration and privileged bypasses; application stubs cannot prove enforcement or distributed revocation. |

Role checks alone may not express object relationships or tenant scope; choose the simplest model that implements accepted rules. Keep authentication and permission independent. Test positive and negative cases with synthetic actors; do not enumerate actual tenant/customer identifiers or grant live access to verify a local policy fix.

Primary reference: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Use actual framework/database/index documentation for version-sensitive enforcement; documented intent and reported controls remain distinct from executed evidence.
