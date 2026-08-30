# RQIR Iteration 075 — Toy014 Physical Systematics / Control Revalidation

**Date:** 2026-08-30  
**Status:** source-specific control/nuisance audit inside the spectral-tilt-profiled D2 likelihood; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 074 promoted Toy014 to the leading balanced locality-constrained D2 source candidate. The next mandatory gate is to rebuild control tolerances for Toy014 rather than importing Toy009/Toy012 timing, geometry or additive priors.

The detector metric remains the physical Iteration-063 spectral-tilt-profiled D2 likelihood. The Toy014 900-point calibration optimum is reused:

- `gamma_mean ~= 5.6776851e6`;
- `gamma_cov ~= 2.7186736e6`.

Four low-rank calibration systematics are introduced:

1. second-probe geometry drift `delta y1`;
2. common phase/timing shift `delta tau`;
3. normalized additive mean offset;
4. normalized additive covariance offset.

The source's 22 hard-constrained nuisance directions and the detector spectral-tilt nuisance are profiled simultaneously.

## 2. NG-006 survives the physical Toy014 redesign

With the four control systematics left unconstrained, profiled beta Fisher remains numerically zero at calibration exposure multipliers

`lambda = 1, 2, 10, 100`.

The regression values stay below `~2e-9` in magnitude (numerical solve noise around zero).

Therefore Toy014 has **not** removed the low-rank control degeneracy.

This is an important consistency result: Toy014's much better local physical resource vector did not arise by accidentally deleting the mature control nuisance problem.

## 3. Conservative 10% control bundle

Using the same conservative rule as the centered systematics work — each systematic contribution limited to 10% of the row-statistical scale — the Toy014 normalized tolerances are

- `sigma(delta y1) = 0.74131718` in the current dimensionless radius coordinate;
- `sigma(delta tau) = 0.00249891877`;
- `sigma(b_mean) = 4.19676208e-5`;
- `sigma(b_cov) = 6.06486956e-5`.

At `f_gap=100 Hz`, the phase/timing tolerance corresponds to

`boxed{sigma_t ~= 3.97715 us}`.

With these independent priors the full profiled result returns to

`F_beta|theta ~= 0.8999686`.

### RQIR-CAL-020 — Toy014 control bundle is source-specific

> A source that Pareto-improves science/calibration/source-metrology resources must still have timing, geometry and additive control tolerances rebuilt in the same physical detector metric. Control priors are not portable source-design constants.

## 4. Coherence / scheduling consequence

Toy014's largest stored phase is `4.28090150`, so at a 100-Hz gap the largest source evolution interval is

`T_coh/evol ~= 6.81327 ms`.

This is somewhat shorter than the mature Toy009 `~7.943 ms` benchmark, so Toy014 does not pay a worse maximum evolution-time floor.

For the transparent timing-reference benchmark

- accepted-event jitter `10 us`;
- acceptance `p=0.5`;
- 1-ms dead/read time;
- reference target allocated at one third of the final timing tolerance,

the required timing-reference block is only

`~0.889 s`.

The more important issue is drift recertification. With the earlier illustrative diffusion convention:

- `D=100 us^2/h` -> cadence `~0.2812 h` (`~16.9 min`);
- `D=1000 us^2/h` -> cadence `~0.02812 h` (`~1.69 min`).

These are transparent drift benchmarks, not oscillator/apparatus predictions.

## 5. Additive offsets in raw row units

Undoing row normalization gives representative Toy014 ranges for the 10% bundle:

- mean-offset raw range `~1.18e-5` to `5.76e-5`;
- centered-covariance offset raw range `~2.05e-6` to `3.70e-5`.

As before, conversion to SI detector units requires the actual row transduction Jacobian.

## 6. Interpretation

Toy014 remains the strongest balanced local source found so far, but its physical experiment still requires an independent control/reference subsystem.

The current source-design improvement and the control problem are therefore separable:

- **improved:** physical D2 science signal, spectral-profiled calibration geometry, Ramsey source metrology;
- **not solved:** low-rank timing/geometry/additive degeneracy.

This is scientifically preferable to a design that appears cheap only because systematics were omitted.

## 7. Reproducibility

Code:

`analysis/toy014_physical_systematics_iteration075.py`

The script rebuilds Toy014, recalculates its physical `gamma` values, finite-differences geometry/timing nuisance columns, profiles source+tilt+control nuisances, and verifies the timing/reference/drift regressions.

## 8. Next gate

Insert Toy014 into the Iteration-071 general Fisher-rate wall-clock closure including a separate control term:

`T_total = T_sci + T_cal + T_src + T_ctrl`.

Keep the result parametric in the detector transfer/PSD matrix and source-metrology reset/visibility. The next useful quantity is the control-aware Toy014-vs-Toy009/Toy013 dominance surface and the required fractional reference duty cycle under explicit drift parameters.
