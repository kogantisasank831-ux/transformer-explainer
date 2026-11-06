# Infrastructure checks

- Inspect role assumption conditions, audiences, subjects, wildcard resources/actions, resource-policy interactions, workload tokens, and metadata access without retrieving real secrets.
- Separate administration, delivery, and runtime identities. Preserve accountable recovery access while removing excess privilege.
- Trace management API, SSH, database, notebook, and storage exposure through the full route. A public CIDR is source evidence; reachability also depends on bindings, routes, and other controls.
- Review privilege, host mounts/networking, runtime user/capabilities, service-account token mounts, supported patch levels, and resource bounds. Do not apply blanket settings that break required GPU or storage behavior.
- Compare source, rendered plan, and observed state with account/resource identity and timestamps. Treat unknown plan values as unresolved. Separate mocked policy checks from actual enforcement.

Consult [OWASP Infrastructure as Code Security](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html) and current official documentation for the actual provider, orchestrator, policy evaluator, and versions.
