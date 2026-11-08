# Training and experiment reproducibility record

- Task/hypothesis, rule IDs, parent/baseline, run IDs/status, owner, reproducibility level and accepted tolerance:
- Code/diff, resolved config, data/feature/label/split manifests, environment/image, runtime/framework/CUDA/driver, hardware/topology and precision:

| Run / rerun | Seeds and determinism | Checkpoint and artifact hashes | Metric/prediction comparison | Outcome / divergence |
|---|---|---|---|---|

## Execution lineage

Record preprocessing/tokenizer, initialization, optimizer/schedule/loss, batch/distribution, RNG and loaders, resume state, tracking completeness, resource/cost, warnings/failures and privacy-safe secret references.

## Conclusion and handoff

State exact, within tolerance, materially different or inconclusive; identify identity mismatches and causal confidence, untested platforms, recipe/test changes, residual risks, owners and next rerun.
