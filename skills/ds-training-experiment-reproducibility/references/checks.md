# Training and experiment reproducibility checks

- Define hypothesis/baseline, metric, reproducibility level, environment, tolerance, owner and decision before comparing runs.
- Assign durable run ID/status and capture commit plus dirty diff/source, resolved config, dependency/image/runtime/framework/CUDA/driver, hardware/topology and precision.
- Bind raw/transformed data, features/labels, split/sampling, tokenizer/augmentations/preprocessing and initialization/checkpoint identities.
- Record optimizer/loss/schedule/steps/batch/distribution and all applicable seeds, generators, deterministic flags, kernels and known nondeterminism; a seed alone is insufficient.
- Preserve complete resume state, sharding/order/synchronization and duplicate/skip checks for distributed or interrupted training.
- Atomically retain metric definitions, failures, resources/cost and hashed model/tokenizer/preprocessing/threshold/evaluation artifacts with access and integrity controls.
- Convert release-relevant notebooks into clean parameterized execution and distinguish same-environment repetition from independent replication.
- Repeat stochastic runs to the accepted design, compare manifests before metrics, localize divergence and report exact/within-tolerance/different/inconclusive honestly.

MLflow documents run metadata and artifact tracking in its [Tracking guide](https://mlflow.org/docs/latest/tracking/). PyTorch's [deterministic algorithms documentation](https://docs.pytorch.org/docs/stable/generated/torch.use_deterministic_algorithms.html) also cautions that deterministic settings alone are insufficient; pin and verify the actual framework used by the project.
