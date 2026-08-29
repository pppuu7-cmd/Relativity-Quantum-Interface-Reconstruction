# Recovery Delta — RQIR Iteration 030

**Date:** 2026-08-29

## New result

D2 `q_pot` has been given a physically explicit force-integral interpretation. A local force sensor supplies `G=dB/dy`; integrating it gives only a differential potential observable

`Delta B(y;y_ref)=B(y)-B(y_ref)`.

An absolute-potential calibration row therefore requires a declared reference arm/level.

## Exact toy audit

Using the current balanced Toy009/Toy010 calibration and replacing both mean and covariance potential observables consistently by finite-reference differences:

- exact rank remains `24/25` for tested `y_ref=-5,-10,-20,-50,-100,-1000`;
- the differential-calibration null converges rapidly to the old absolute-potential null as `|y_ref|` grows;
- at `y_ref=-10`, null overlap is `0.9992856122`;
- at `y_ref=-100`, null overlap is `0.9999995341`.

## Physical rate model

For one-sided white equivalent-force PSD `S_F`, uniform force integration over path length `L` yields

`q_pot=2||Delta B||^2/(L^2 S_F)`,

while direct force calibration gives

`q_force=2||G||^2/S_F`.

With seven mean settings at each of the two probes, the heterogeneous bundle ratio `x=K_force/K_pot` is approximately:

- `0.62086` at `y_ref=-5`;
- `0.20116` at `-10`;
- `0.05850` at `-20`;
- `0.01036` at `-50`;
- `0.002684` at `-100`;
- `2.776e-5` at `-1000`.

Thus the limit that best reproduces the old absolute-potential geometry makes force-integral potential calibration increasingly expensive.

## New labels

- **RQIR-CAL-010:** relational-potential requirement.
- **RQIR-RESOURCE-010:** finite-reference distance is a joint calibration-geometry/resource variable; after signal saturation `q_pot` falls approximately as `1/L^2`.
- **RQIR-NG-011:** force data alone leave the potential integration constant/reference value unspecified.

## Do not overclaim

This is a Newtonian Toy009/Toy010 observability/resource result. It is not a new-gravity claim, not a relativistic gauge completion, and not an SI apparatus forecast.

## Next mandatory gate

Insert finite-reference calibration rows and heterogeneous per-row native rates into the corrected hard-constrained `F_beta|theta` optimizer, then optimize jointly over D2 branch, exposure, source-preparation metrology and `y_ref`, with timing/reference recertification duty included.
