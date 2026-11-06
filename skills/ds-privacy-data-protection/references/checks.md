# Privacy checks

- For each field and derived output ask: whose data, why collected, which accepted purpose permits use, who accesses it, where copied, how long retained, and how removal propagates?
- Include identifiers in URLs, traces, exceptions, filenames, support tools, analytics, prompts, and provider logs. Aggregates may expose small groups.
- Separate accepted policy, implementation facts, and vendor claims. Determine contractual or jurisdiction scope before presenting legal conclusions.
- Handle aliases, multi-tenant membership, event versus processing time, holds, tombstones, failure queues, stale replicas, backup expiry, and restore suppression. Do not override holds or invent indefinite retention.
- Treat anonymization, model unlearning, and retraining effectiveness as evaluated claims. A local deletion test does not establish organization-wide compliance.

Consult the current [NIST Privacy Framework](https://www.nist.gov/privacy-framework) for risk-management structure plus official regulator and provider guidance relevant to the accepted requirement. Record source/version and keep legal decisions with the responsible owner.
