# RQIR Research Log — Iteration 034

**Date:** 2026-08-29  
**Target:** audit the physical parameter coordinates and the actual centered-noise derivative before attaching D2 covariance Fisher rates.

## Trigger

Iteration 033 required row-specific physical covariance rates. Two prerequisites were checked first:

1. whether the Iteration-020 source QFI and the later `C_a` nuisance prior use the same amplitude coordinate;
2. whether the noisy `cov` rows are derivatives of the centered symmetrized noise kernel or only raw second moments.

Both required correction.

## Source-QFI coordinate correction

Iteration 020 QFI remains correct:

`F_Q^(a)(a=0.08) ~= 13.27068619`

for `rho(a)=I/5+a Delta0`.

The later Fisher uses a fractional amplitude `alpha`, with

`a=EPS alpha`, `EPS=0.08`.

Therefore

`F_Q^(alpha)=EPS^2 F_Q^(a) ~= 0.0849323916`

per accepted single-branch copy.

At normalized detector Fisher `S_D=1`, 90% retention needs `C_alpha=9`, corresponding to about `105.97` accepted single-branch copies or `52.98` independent plus/minus pair equivalents.

At historical `S_D=25`, `C_alpha=225` corresponds to about `2649.17` single-branch copies or `1324.58` pair equivalents.

The old `~17 copies for C_a=225` mapping is withdrawn for the current fractional-amplitude Fisher. The QFI formula itself is retained.

New rule: **RQIR-NUM-002 — Fisher-coordinate Jacobian rule.**

## Centered covariance correction

For a symmetric pair around `rho0=I/5`, the centered covariance-difference row is

`C_AB = sym(A,B) - <A>0 B - <B>0 A`

up to an irrelevant identity term.

Raw second-moment rows and centered rows have the same exact nullspace when the mean rows are also imposed exactly:

- both rank `24/25`;
- null overlap `1.0` numerically.

But finite-noise Fisher differs because mean directions are not known exactly.

New rule: **RQIR-CAL-013 — centered-noise linearization rule.**

## Recomputed normalized 90% weights

Using the hard trace+energy basis and the Iteration-015 900-point allocation convention:

D1:

- uniform `gamma ~=1.12758e6`;
- `gamma_mean ~=1.26572e6`;
- `gamma_cov ~=0.621783e6`;
- allocation gain `~1.09308`.

D2:

- uniform `gamma ~=1.63750e6`;
- `gamma_mean ~=1.83026e6`;
- `gamma_cov ~=0.590127e6`;
- allocation gain `~1.18719`.

These replace the raw-second-moment numbers as the preferred normalized baseline for the RQIR centered noise kernel. They do not yet imply SI-time savings.

## D2 centered branch update

Fully force-native centered branch:

- rank `22/23`;
- detector-aligned exact null survives;
- `F_beta(C_alpha=0,lambda=1) ~=0.0195153`;
- `C_alpha90 ~=7.78026`;
- strong-preparation threshold `lambda ~=0.10013`.

Complementary relational+force branch at `y_ref=-4` with both centered covariance families:

- `F_beta(C_alpha=0,lambda=1) ~=0.905293`;
- no source-amplitude prior is required for 90% at this normalized benchmark;
- calibration-only threshold `lambda ~=0.94149`.

Best centered force-covariance subset remains `(0,1,3,7)`:

- 0 added rows: `C_alpha*=4.55511`;
- best 4: `C_alpha*=0.0500614`;
- best 5 `(0,1,3,6,7)`: `C_alpha*=0`.

Updated equal-row local break-even:

- first four: `q_cov/R_P^(alpha) > ~5.24e5`;
- fifth after the first four: `> ~1.18e7`.

## Downstream impact

The following require revalidation before being called current physical requirements:

- Iteration-016 timing/additive priors;
- wall-clock allocations using those priors;
- D2 raw-covariance branch resource numbers;
- stationary PSD examples for current nonstationary Toy009 covariance rows.

Exact Toy009/Toy010 results and structural no-go results remain intact.

## Files

- `analysis/physical_coordinate_centered_covariance_audit_iteration034.py`
- `docs/PHYSICAL_COORDINATE_CENTERED_COVARIANCE_CORRECTION.md`
- `recovery/RECOVERY_DELTA_ITERATION_034.md`

## Next gate

Audit stationarity and operator ordering of the high-value centered covariance rows, then derive a phase-referenced/cyclostationary or repeated two-time physical Fisher-rate model before assigning SI covariance time.
