# RQIR Recovery Delta — Iteration 021

**Date:** 2026-08-29

Use this file together with `docs/RECOVERY_GUIDE.md` (v1.6) until the main guide is next consolidated.

## New retained result

**RQIR-RESOURCE-005:** a dimensionless Fisher requirement (`C_a`, `gamma_mean`, `gamma_cov`, or a prior precision) does not by itself determine wall-clock cost. A unique wall-clock optimum requires a physical Fisher-information rate per second for every independent resource channel.

Iteration 021 implements the exact Iteration-015 hard-constrained 22D Toy009 nuisance problem with four rate-parametric wall-time pools: detector, source-preparation metrology, gravitational mean calibration, gravitational covariance calibration.

For normalized rates `(R_D,R_P,R_M,R_C)=(1,10,1e6,1e6)`:

- D1 optimum fractions approximately `(0.5609,0.1726,0.1880,0.0784)` with `F_beta/T~0.2981`;
- D2 approximately `(0.5393,0.1666,0.2251,0.0690)` with `F_beta/T~0.2777`.

These numbers are diagnostics in rate-ratio space, not SI-time forecasts.

## Regression

As `R_M,R_C -> infinity`, the four-resource optimizer reproduces the Iteration-018 square-root detector/preparation allocation, while calibration fractions tend to zero. This is a mandatory regression test in the new code.

## Important limitation

Iteration 016 remains binding: timing, additive-offset and gain/reference controls are separate resources. Their seconds-to-prior-precision conversion is not yet physically specified. Do not claim a complete wall-clock budget by silently treating those priors as free.

## New files

- `analysis/full_wallclock_rate_optimizer_iteration021.py`
- `docs/FULL_WALLCLOCK_RATE_OPTIMIZATION.md`
- `research_log/2026-08-29_iteration_021_full_wallclock_rate_optimization.md`

## Next priority

Derive physical calibration/control information rates from concrete D1 and D2 readout-noise models, then extend the optimizer with explicit timing/additive/gain reference pools and compute the complete `F_beta|theta/T_wall`.
