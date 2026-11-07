# SLOs and alerting checks

- Define user/consumer, journey, boundary, owner, good and eligible events, threshold/unit, measurement point/source and treatment of retries, errors, maintenance and missing data.
- Use user-visible availability, latency, correctness, freshness, durability, completeness or quality indicators; specify populations, windows, weighting, percentiles and exclusions.
- Record target, window, source and acceptance. Calculate event- or time-based error budget consistently and define launch/remediation/exception policy; keep SLAs distinct.
- For DS/ML, separate service health from data freshness/completeness and delayed quality/safety/fairness signals with datasets, segments, sample and label delay.
- Page only for timely human action; use tickets or review for slower risks. Every alert needs owner, evidence, objective, dashboard, runbook, escalation and resolution.
- Define burn-rate or equivalent windows, traffic floor, low-volume and seasonality behavior, missing/stale/reset data, grouping, deduplication and inhibition.
- Replay incidents and healthy periods, test notification and runbook safely, and review false positives/negatives and data quality. Quiet paging does not prove SLO compliance.

Google SRE's [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) chapter provides primary guidance on error-budget burn-rate alerts; adapt the method to accepted objectives and actual telemetry.
