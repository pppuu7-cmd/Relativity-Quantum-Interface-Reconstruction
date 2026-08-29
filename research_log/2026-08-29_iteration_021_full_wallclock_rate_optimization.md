# RQIR Research Log — Iteration 021: Full Wall-Clock Rate Optimization

**Date:** 2026-08-29

## Starting point

Iteration 019 supplied native detector-rate models for D1/D2. Iteration 020 supplied the Toy009 source-preparation QFI rate. Iteration 015 remains the mandatory hard-constrained nuisance basis; Iterations 013–014 headline allocations remain superseded by that correction.

The open request was to combine detector, preparation, gravitational calibration and reference/control resources into one wall-clock objective.

## Key methodological finding

A unique wall-clock optimum cannot yet be stated from the repository's present physical inputs because hardware-specific Fisher rates per second are still absent for the 14 gravitational mean rows, 8 covariance rows, and independent timing/additive/gain reference channels.

Assigning hours directly from `gamma_mean`, `gamma_cov` or control-prior precisions would therefore invent an unstated sensor noise model.

Recorded as **RQIR-RESOURCE-005**: dimensionless Fisher requirements determine wall-clock cost only after every independent resource channel has a physical information rate.

## Exact parametric optimization

Implemented the corrected 22D hard-constrained Toy009 Fisher with four explicit wall-time pools:

- detector `x_D`;
- independent preparation metrology `x_P`;
- mean gravitational calibration `x_M`;
- covariance gravitational calibration `x_C`.

For rates `(R_D,R_P,R_M,R_C)` and `sum x=1`, the optimizer profiles beta over hidden amplitude plus all 22 source nuisance directions.

Representative normalized benchmark `(R_D,R_P,R_M,R_C)=(1,10,1e6,1e6)` gives:

- D1 optimum approximately `(0.5609,0.1726,0.1880,0.0784)`, `F_beta/T~0.2981`;
- D2 optimum approximately `(0.5393,0.1666,0.2251,0.0690)`, `F_beta/T~0.2777`.

These are rate-ratio diagnostics, not hardware forecasts.

## Regression check

For `R_M=R_C=1e12 R_D`, calibration fractions fall below `1e-3` and the exact optimizer reproduces the Iteration-018 two-resource square-root detector/preparation allocation for `R_P/R_D=1,10,100` to better than `5e-4` in allocation fraction.

## Negative/limiting result

The full requested SI wall-clock answer remains underdetermined until physical calibration/reference noise models are supplied. This is not a blocker to further theory: the parametric optimizer now provides the correct insertion point for those rates and prevents accidental promotion of standardized `xi` bookkeeping into hardware claims.

## Files

- `analysis/full_wallclock_rate_optimizer_iteration021.py`
- `docs/FULL_WALLCLOCK_RATE_OPTIMIZATION.md`
- this log
- `docs/RECOVERY_DELTA_ITERATION_021.md`

## Next gate

Derive branch-specific physical Fisher rates for gravitational calibration and independent controls: D1 phase/reference readout per calibration setting; D2 equivalent-force/reference PSD per mean/covariance setting. Then add timing/additive/gain control channels explicitly and optimize the true complete `F_beta|theta/T_wall`.
