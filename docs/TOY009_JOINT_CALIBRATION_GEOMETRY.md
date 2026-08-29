# RQIR Toy 009 — Joint Calibration Geometry

**Date:** 2026-08-29  
**Status:** finite NP3 calibration redesign; detector-design result, not new physics.

## Target

Toy 009 improved the source while inheriting Toy 007's second-probe position and calibration times. Iteration 011 asks whether the calibration geometry itself can be improved without weakening NP3, state positivity, response survival, or conditioning.

The exact 24-row calibration structure is retained. Variables are the second probe position `y1` and the six nonzero calibration/target times. The source remains Toy 009.

## Baseline

Inherited settings:

`y1 = -3.5955271928522547`

`times = (0, 3.0709312961, 3.5839288992, 3.7352146497, 4.18983, 4.8970328749, 5.6572697959)`.

Baseline diagnostics:

- `rank(A)=24/25`;
- `eta_R = 0.5688230`;
- normalized `s_min = 1.512224e-3`;
- condition number `kappa ~= 3033.4`;
- D1 `S_eff = 1.686343e-4`;
- D2 `S_eff = 3.432364e-4`.

## Accepted balanced redesign

A deterministic random/local search found a robust Pareto point:

`y1 = -3.7766873837`

`times = (0, 3.09855988, 3.45849306, 2.93830159, 4.13016958, 4.84480925, 4.99085067)`.

The row ordering need not be chronological; these are independent calibration sampling phases in one source period.

Exact-algebra diagnostics remain valid:

- `rank(A)=24/25`;
- maximum selected equality residual below `1e-15`;
- mean difference below `1e-15`;
- centered selected-noise difference below `1e-15`;
- both `rho+` and `rho-` remain positive.

State eigenvalues are approximately

`rho+ = (0.12221, 0.17104, 0.18663, 0.24012, 0.28000)`

`rho- = (0.12000, 0.15988, 0.21337, 0.22896, 0.27779)`.

The target ordered responses remain opposite:

`D+ ~= +0.0116278`, `D- ~= -0.0116278`.

## Calibration improvement

The accepted redesign gives

`eta_R ~= 0.5734264`,

`normalized s_min ~= 1.999540e-3`,

`condition ~= 2313.05`.

Relative to inherited Toy 009 this means:

- response survival increases slightly (`~0.8%`);
- normalized smallest singular value increases by about `32.2%`;
- condition number improves by about `23.8%`.

Thus the detector gain is not purchased by a more fragile exact-null calibration.

## Detector information improvement

Accepted harmonics are approximately

`H2 = +0.00245460 - i 0.01049981`,

`H4 = -0.00395383 - i 0.01338211`,

`G2 = +0.00285553 - i 0.01750306`,

`G4 = -0.00463232 - i 0.01567853`.

Two-band profiled source information becomes

`S_eff(D1) ~= 2.912e-4`,

`S_eff(D2) ~= 5.780e-4` (rounding depends on stored phase digits).

Using full-precision scan values, the gains relative to inherited Toy 009 are

- D1: approximately `x1.7268`;
- D2: approximately `x1.6838`.

Relative to the older Toy 007 baseline, the cumulative ideal two-band gains are therefore approximately

- D1: `1.22184 * 1.7268 ~= x2.11`;
- D2: `1.40358 * 1.6838 ~= x2.36`.

These are detector-source Fisher proxies, not experimental SNR forecasts.

## Aggressive alternative

A second Pareto point reaches roughly `x1.81` in both D1 and D2 relative to inherited Toy 009 while still satisfying the original non-degradation guards. Its `s_min` sits only slightly above the inherited baseline, so it is not promoted to the operational baseline. It is retained as evidence of a gain-versus-conditioning frontier.

## Result

### RQIR-CAL-002 — calibration geometry is an active information resource

For a fixed source and a fixed number/type of exact NP3 constraints, changing probe location and sampling phases can rotate the surviving null direction relative to detector-response harmonics and materially change downstream Fisher information.

Therefore calibration is not merely a passive verification step. It is part of the experiment-design map

`source -> calibration/Fisher geometry -> gravity transfer -> detector -> profiled likelihood`.

This is a finite-dimensional numerical design result, not a universal theorem.

## Reproducibility

Code: `analysis/toy009_joint_calibration_geometry.py`.

The code reconstructs Toy 009 from seed/trial, verifies baseline and accepted designs, state positivity, exact equality residuals, calibration conditioning, response survival, and D1/D2 two-band information.
