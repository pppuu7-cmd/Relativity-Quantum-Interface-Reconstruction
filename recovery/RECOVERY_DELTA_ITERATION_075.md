# RQIR Recovery Delta — Iteration 075

**Date:** 2026-08-30

## Current front

Iteration 074 produced the leading balanced local physical D2 source Toy014. Iteration 075 rebuilds Toy014 timing/geometry/additive control nuisances inside the same spectral-tilt-profiled detector metric.

## Retained control result

Toy014 physical calibration weights:

- `gamma_mean ~= 5.6776851e6`;
- `gamma_cov ~= 2.7186736e6`.

With unconstrained low-rank controls (`delta y1`, timing/phase shift, additive mean, additive centered covariance), profiled beta Fisher remains numerically zero even for `lambda=100` calibration exposure. **RQIR-NG-006 survives** Toy014.

Conservative 10% control bundle:

- `sigma(delta y1)=0.74131718`;
- `sigma(delta tau)=0.00249891877`;
- `sigma(b_mean)=4.19676208e-5`;
- `sigma(b_cov)=6.06486956e-5`.

At 100 Hz:

- timing tolerance `sigma_t ~= 3.97715 us`;
- maximum stored evolution interval `~6.81327 ms`.

With these priors:

`F_beta|theta ~= 0.8999686`.

## New retained rule

**RQIR-CAL-020 — Toy014 control bundle is source-specific.**

Control tolerances must be rebuilt after source co-design in the same physical detector metric. Do not import Toy009/Toy012 timing/geometry/additive priors as physical Toy014 tolerances.

Transparent timing-reference benchmark (`10 us` per-event jitter, `p=.5`, 1-ms overhead): reference block `~0.889 s`. Illustrative timing-diffusion cadence:

- `D=100 us^2/h`: `~0.2812 h` (`16.9 min`);
- `D=1000 us^2/h`: `~0.02812 h` (`1.69 min`).

These are resource benchmarks, not apparatus forecasts.

## Reproduce

`python analysis/toy014_physical_systematics_iteration075.py`

Primary note:

`docs/TOY014_PHYSICAL_SYSTEMATICS_ITERATION075.md`

## Next admissible gate

Extend the Iteration-071 general physical wall-clock closure to include explicit `T_ctrl` / recertification duty and derive Toy014-vs-Toy009/Toy013 dominance surfaces in terms of detector Fisher rates and drift/reference parameters. Keep PSD/transduction/reset/visibility parametric.
