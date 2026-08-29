# RQIR Research Log — Iteration 011 — Toy 010 Calibration Geometry Co-Optimization

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`

## Goal

Keep the accepted Toy 009 source fixed and test whether the finite NP3 calibration geometry itself can be redesigned to improve detector-level information and calibration stability simultaneously.

Variables allowed to change:

- second Newtonian calibration-probe position;
- five non-target calibration times.

Frozen:

- Toy 009 source operator and five-site embedding;
- energy spectrum `(1,2,3,4,6)`;
- probe 0 at `y0=0`;
- target response time `tR=3.583928899215236`;
- number and type of mean/noise calibration rows;
- D1/D2 detector definitions.

## Search

A first scan over `y1` alone showed no free Pareto improvement: detector response, `eta_R` and conditioning trade against one another.

A joint local random search over `y1` plus the five free time samples found multiple simultaneous non-degraded designs.

Search seeds:

- broad local search: `2026082903`;
- short deterministic refinement: `2026082904`.

Accepted geometry:

- `y1 = -3.764531439702698`;
- times approximately `(0, 2.99076642, tR, 2.86845279, 4.17773776, 4.88882082, 4.99774842)`.

## Exact checks

- `rank(A)=24/25`;
- maximum equality residual `~1.7e-16`;
- both null-pair density matrices positive;
- target mean equality preserved;
- target centered self-noise equality preserved.

State eigenvalues:

`rho+ ~ (0.12226,0.17604,0.18370,0.23800,0.28000)`

`rho- ~ (0.12000,0.16200,0.21630,0.22396,0.27774)`

Target response:

`D+ ~ +0.01328591`, `D- ~ -0.01328591`.

## Calibration improvement

Inherited Toy 009 calibration:

- `eta_R ~ 0.568823`;
- `smin ~ 1.51222e-3`;
- condition `~3033.4`.

Toy 010:

- `eta_R ~ 0.600174`;
- `smin ~ 2.21101e-3`;
- condition `~2084.2`.

Thus `eta_R` improves by about 5.5%, `smin` by about 46.2%, and the condition number improves by a factor about 1.46.

## Detector improvement

Toy 010 D1 harmonics:

`H2 ~ 0.00286032 - 0.01044850 i`

`H4 ~ -0.00455057 - 0.01255465 i`

Two-band profiled source information:

- `D1 Toy010 / Toy009 ~ 1.67881`;
- `D1 Toy010 / Toy007 ~ 2.05123`.

Toy 010 D2 harmonics:

`G2 ~ 0.00331456 - 0.01716597 i`

`G4 ~ -0.00533146 - 0.01470909 i`

Two-band profiled source information:

- `D2 Toy010 / Toy009 ~ 1.58406`;
- `D2 Toy010 / Toy007 ~ 2.22336`.

## Null-direction steering

The exact one-dimensional null direction rotates by approximately `37.7 degrees` between the inherited Toy 009 calibration and Toy 010.

For smooth rank-`p-1` calibration `A(q)` with normalized null vector `n(q)`, differentiating `A n=0` gives

`n' = -A^+ A' n`,

and therefore

`||n'|| <= ||A'||/smin(A)`.

Recorded as **RQIR-CAL-002 — null-direction steering and fragility**.

Interpretation: finite calibration is an active design layer, while poor conditioning amplifies sensitivity of the surviving null direction to small geometry/timing changes.

## D1 control consequence

An analytic four-switch family optimized for the Toy 010 harmonics gives approximately:

- `a ~ 2.24169`;
- `|W2| ~ 0.49864`;
- `|W4| ~ 0.31000`;
- Fisher `~1.819 x` the old Toy 007 eight-switch bounded-window value.

Under the same purely illustrative physical assumptions used previously:

- D1 mass-product benchmark scales from `8.1e-29 kg^2` to `~6.01e-29 kg^2`;
- equal-mass illustration `~7.75e-15 kg`;
- optimistic D2 force benchmark scales to `~1.61e-18 kg^2`.

These remain scaling illustrations, not feasibility claims.

## Main conclusion

Toy 010 gives a stronger version of RQIR-DESIGN-001:

`(source, calibration, detector, noise) -> F_beta|theta`

must be treated as one coupled design problem.

The same source can yield substantially different usable ordered-response discriminants solely because finite calibration geometry rotates and constrains the allowed state/nuisance direction differently.

## Reproducibility

- `analysis/toy010_calibration_geometry_optimization.py`
- `docs/TOY_MODEL_010_CALIBRATION_GEOMETRY_COOPTIMIZATION.md`

## Next

Replace exact equality calibration by noisy calibration covariance/Fisher geometry. Optimize the same probe/time variables with finite measurement errors and a finite measurement budget, then profile source-state nuisance directions statistically together with D1 detector covariance.
