# Product analytics and experimentation checks

- Tie each metric to a product decision, population, unit, owner and action. Define numerator/denominator, identity, eligibility, time, attribution, dedupe, late/missing data and segments.
- Establish purpose, consent/basis, minimization, access, retention, deletion and regional policy before collecting personal, device, prompt/model or sensitive data.
- Version event schemas and authoritative producers; validate and monitor volume, invalidity, uniqueness, duplicates, delay and adoption, and reconcile critical outcomes independently.
- Bind DS events to safe model/feature/index/data versions, separate delayed quality from engagement and assess feedback-loop risk where applicable.
- Prespecify hypothesis, primary and guardrail metrics, practical effect, unit, variants, exposure, exclusions, allocation, power, duration and stopping rule.
- Preserve stable randomization and accepted analysis population; address clustering, identity, interference, carryover, novelty, seasonality and concurrent experiments.
- Check A/A where warranted, sample-ratio mismatch, exposure parity, contamination, invariants and instrumentation before interpreting outcomes.
- Report effect and uncertainty, practical significance and multiplicity/sequential method; govern exploratory segments and record ship/stop/iterate/inconclusive decisions.

Microsoft Research's guidance on [diagnosing sample-ratio mismatch](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) provides a primary reference for a critical experiment-quality check. Use an accepted statistical design appropriate to the product and decision.
