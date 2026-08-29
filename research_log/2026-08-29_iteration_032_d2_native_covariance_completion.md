# RQIR Research Log — Iteration 032

**Date:** 2026-08-29

## Target

Make the D2 calibration branches physically consistent at the covariance/noise level before continuing wall-clock optimization.

## Starting point

Iteration 026 replaced 14 potential-mean rows by force-gradient means but kept the old eight potential covariance rows. Iterations 030–031 later established that D2 observable families must be transformed consistently. The old `native-replace` branch is therefore a mixed force-mean/potential-covariance protocol, not a fully force-native one.

## Method

The calculation uses the corrected hard trace+energy constrained Toy009/Iteration-011 basis, the fixed hidden source, 22 orthogonal source nuisances, corrected D2 detector response, and row weights `gamma_mean=2.414e6`, `gamma_cov=0.929e6`.

Eight force-covariance rows were generated from the same gradient operator family and the same probe/time pattern as the existing covariance bundle. The full profiled `F_beta|theta` was evaluated, and all 256 subsets of the eight new covariance rows were scanned at `y_ref=-4`.

## Results

Fully force-native `14 force means + 8 force covariances` remains rank `22/23` on the hard source tangent space. Its new exact null has old-hidden overlap `~0.95003346` and detector alignment `~0.99003961`. At `lambda=1`, `C_a=0`, `F_beta|theta~0.0194450`. Reaching 90% at `lambda=1` requires `C_a*~8.29464`; with strong preparation metrology the minimum calibration multiplier is `~0.1537665`.

For relational-potential + force means plus both relational and force covariance bundles, rank is `23/23`. At `y_ref=-4`, `F_beta|theta~0.8994327` already at `lambda=1`, `C_a=0`; only `C_a*~0.06708` is needed for 90%, or calibration-only 90% is reached at `lambda~1.00632`.

At `y_ref=-4`, the best four added force-covariance rows are indices `(0,1,3,7)`. They raise `F_beta|theta` from `~0.819539` to `~0.894857` and reduce `C_a*` from `~5.82122` to `~0.58896`. With no source prior this four-row version reaches 90% at `lambda~1.05755`.

## New rules

**RQIR-CAL-011:** mean and covariance/noise calibration must belong to the same declared physical observable family, or the protocol must be explicitly labeled hybrid.

**RQIR-CAL-012:** targeted detector-native covariance observables can provide most of the remaining nuisance closure after complementary mean calibration; covariance-row selection is therefore an active resource-design variable.

## Scope

These are finite Toy009 inference/resource results. They do not establish a cheaper laboratory protocol until physical covariance Fisher rates are supplied.

## Files

- `analysis/d2_native_covariance_completion_iteration032.py`
- `docs/D2_NATIVE_COVARIANCE_COMPLETION.md`
- `recovery/RECOVERY_DELTA_ITERATION_032.md`

## Next gate

Derive common-apparatus Fisher rates for relational-potential covariance and force covariance from one D2 PSD/bandwidth/duty model. Then minimize wall-clock cost over `y_ref`, `lambda`, `C_a`, and covariance-row subset.
