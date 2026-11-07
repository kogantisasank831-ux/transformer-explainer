# Incident response and postmortem checks

- Establish observed impact, affected population, start-time bounds, evidence confidence and accepted severity/escalation policy; keep facts, hypotheses and reports separate.
- Assign incident command, operations, communications and scribe roles with one authoritative timeline, channel and decision log.
- Protect safety, data integrity and security; use bounded reversible containment or mitigation, exact target checks, evidence preservation and independent recovery paths.
- Cover service, dependency, data, queue and applicable model/feature/index/provider/GPU failures. Do not silently degrade quality or compatibility.
- Communicate confirmed scope, mitigation, unknowns, next checkpoint and owner at the accepted cadence without leaking sensitive information.
- Verify recovery through affected user journeys, invariants, freshness/quality, backlog, capacity and a stability window; a restart or green dashboard is not recovery.
- Produce a blameless evidence-linked timeline and contributing-condition analysis. Actions need measurable outcomes, owners, dates and verified closure.
- Define timing boundaries before reporting response metrics and feed accepted learning into durable code, tests, controls, runbooks and project logic.

Use current [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) for cybersecurity incident-response integration and Google's [incident management guidance](https://sre.google/resources/practices-and-processes/incident-management-guide/) and [postmortem analysis](https://sre.google/workbook/postmortem-analysis/) for operational learning. Adapt them to accepted organizational policy.
