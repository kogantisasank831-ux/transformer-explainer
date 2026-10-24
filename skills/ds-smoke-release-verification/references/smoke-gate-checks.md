# Smoke gate checks

| Gate | Evidence and limit |
|---|---|
| Candidate lineage | Exact artifact digest/commit plus relevant config/model identity and trusted build/deploy evidence; same candidate's required CI suites actually executed. Green on another SHA or an untracked rebuild is ineligible. |
| Runtime identity | Trusted platform/runtime digest where available plus expected app/model/config indicators. Self-reported endpoint data alone may be insufficient provenance; say what is trusted. |
| Readiness/dependencies | Required services/model loaded and one actual supported path works; liveness alone is insufficient. Keep environment readiness retries bounded and don't retry business assertions until green. |
| Authority/journey | Safe authenticated action/read with independent expected outcome and relevant denial check; test-owned records/accounts only. Count effects only when authorized and observable. |
| Post-rollout | Exact promoted identity and a small representative check; defined observation/recovery ownership. A later-stage check is not yet due before rollout, not already passed. |

Keep smoke bounded and explicit. Missing routes, credentials, candidate identity or required dependencies are unknown/blocked evidence, not invented defaults or silent skips. Record failed, inconclusive, not run and not yet due accurately. Clean fixture resources and redact tokens, connection strings and sensitive bodies from reports.

Workflow dependency wiring, repository required-status settings and cross-workflow candidate matching are separate enforcement evidence. This workflow may assess or implement authorized checks, but doesn't publish, promote, change traffic or grant a CI exception. Native/desktop/package products use their appropriate installed artifact smoke path rather than pretending every product has an HTTP server.
