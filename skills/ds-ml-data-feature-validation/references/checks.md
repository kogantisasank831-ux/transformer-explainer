# ML data and feature validation checks

- Define use-case unit, entity/event time, outcome/label availability, populations, intended/excluded use, owners and failure decision.
- Preserve source purpose/rights/privacy, lineage, extraction and transform versions, immutable manifests/snapshots, counts and checksums across raw to published stages.
- Validate schema, encoding/shape/units/time, missing/default/finite/range/category, keys/relationships, temporal/volume and domain invariants at the correct grain.
- Validate unstructured decode, language/size/quality, metadata, duplication, extraction and rights; route specialist privacy/security findings without losing traceability.
- Define label source/time/delay/window/revision/noise and construct entity/group/time-safe splits with no future, duplicate, fitted-transform or outcome leakage.
- Specify feature key, event/availability time, window, source, transform, default and freshness; prove point-in-time and offline-online value parity.
- Analyze missingness, slices, drift, skew, seasonality and sampling with accepted feature-specific thresholds and sufficient population; investigate mechanisms.
- Gate each stage, quarantine failed partitions, govern temporary exceptions and retain machine-readable evidence. Inferred schema and passing checks cover only encoded rules.

TensorFlow Data Validation documents schema checks, [training-serving skew and drift detection](https://www.tensorflow.org/tfx/guide/tfdv). Its inferred schemas are best-effort and require domain review, matching this workflow's acceptance boundary.
