# RQIR Research Log — Iteration 030

**Date:** 2026-08-29  
**Target:** close the missing physical meaning of `q_pot` in the D2 native-rate model without identifying potential and force by assumption.

## Starting point

Iteration 029 mapped the D2 resource phase diagram to `(q_pot,q_force,q_cov,R_P)` but left `q_pot` physically open. The next gate required a common transduction model.

## Main observation

A local force detector measures `G=dB/dy`, not the absolute potential row `B(y)`. Force integration gives only

`Delta B=B(y)-B(y_ref)`.

Therefore any force-based implementation of the NP3 potential calibration needs an explicit reference arm/level. The reference coordinate changes both calibration geometry and wall-clock rate.

## White-force derivation

For one-sided flat `S_F`, averaging for `T` gives variance `S_F/(2T)`. Uniform spatial integration over path length `L` gives

`Var[int F dy]=L^2 S_F/(2T)`.

Hence

`q_pot=2||Delta B||^2/(L^2 S_F)`

and direct force calibration has

`q_force=2||G(y)||^2/S_F`.

## Exact numerical audit

The full normalized 24-row calibration was rebuilt using differential-potential mean and covariance rows consistently.

Absolute baseline: rank `24/25`, `s_min=0.001999540405542146`.

For `y_ref=-5,-10,-20,-50,-100,-1000`, rank remains `24/25`.

Null overlaps with the old absolute-potential null are respectively approximately

`0.9968101, 0.9992856, 0.9998904, 0.9999943, 0.99999953, 0.99999999994`.

Thus the old null is recovered smoothly as the reference is moved outward.

## Resource tradeoff

At `y_ref=-10`, `q_pot/q_force` is about `0.01136` for probe 0 and `0.21491` for probe 1. With seven mean settings per probe, the heterogeneous bundle ratio is

`x=K_force/K_pot ~=0.20116`.

At `y_ref=-100`, null overlap is already `0.99999953`, but `x~=0.002684`.

At `y_ref=-1000`, `x~=2.776e-5`.

So making the reference sufficiently distant to emulate the old absolute-potential geometry makes force-integral potential calibration parametrically expensive relative to direct force calibration.

## New rules

**RQIR-CAL-010 — relational-potential requirement:** force integration implements potential differences, not an absolute potential row, unless an independent reference fixes the integration constant.

**RQIR-RESOURCE-010 — reference-distance tradeoff:** moving the reference outward restores the declared absolute-potential calibration geometry but suppresses native `q_pot` approximately as `1/L^2` after signal saturation.

**RQIR-NG-011 — force-to-potential integration-constant obstruction:** assigning absolute potential rows the same native readout as force rows without an explicit reference is physically under-specified.

## Files

- `analysis/d2_finite_reference_potential_iteration030.py`
- `docs/D2_FINITE_REFERENCE_POTENTIAL_TRANSDUCTION.md`
- `recovery/RECOVERY_DELTA_ITERATION_030.md`

## Next gate

Promote `y_ref` into the corrected hard-constrained D2 Fisher/resource optimizer. Recompute `F_beta|theta` for finite-reference rows, use heterogeneous per-row native rates, source QFI and timing/reference duty, and optimize jointly over branch, exposure and reference distance.
