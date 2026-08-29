# RQIR Research Log — Iteration 011

**Date:** 2026-08-29  
**Topic:** joint Toy 009 second-probe and calibration-time optimization  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Target

Remove a remaining inherited design choice: Toy 009 still used Toy 007's second-probe location and calibration sampling phases. Optimize these variables while keeping the same finite NP3 row structure, state positivity, and non-degradation guards on `eta_R` and normalized `s_min`.

## Step A — baseline reconstruction

Toy 009 was reconstructed deterministically from seed `314159`, trial `811`.

Inherited calibration reproduces:

- `rank(A)=24/25`;
- `eta_R=0.5688230`;
- `s_min=1.512224e-3`;
- condition `~3033.4`;
- D1 `S_eff=1.686343e-4`;
- D2 `S_eff=3.432364e-4`.

This independently reproduces Iteration 010 before changing design variables.

## Step B — one-variable lesson

A preliminary sweep of the second-probe position alone showed no clear free Pareto improvement: gains in detector response typically traded against response survival or calibration conditioning. This motivated varying probe location and sampling phases jointly rather than treating geometry coordinates independently.

## Step C — joint search

Variables:

- second-probe position `y1`;
- six nonzero sampling/target phases within one source period.

Fixed:

- Toy 009 source;
- 24-row NP3 constraint structure;
- state amplitude `EPS=0.08`;
- positive-state requirement;
- accepted design must satisfy at least inherited `eta_R` and inherited `s_min`.

A broad deterministic random search followed by local refinement exposed a gain-conditioning Pareto frontier.

## Step D — aggressive candidate

One candidate reaches approximately

- D1 `x1.81`;
- D2 `x1.81` or better;

relative to inherited Toy 009 while satisfying the original non-degradation guards. However, its normalized `s_min` lies only slightly above the inherited value. It is retained as a frontier point, not promoted to baseline.

## Step E — accepted balanced candidate

Accepted design:

`y1 = -3.7766873837`

`times = (0, 3.09855988, 3.45849306, 2.93830159, 4.13016958, 4.84480925, 4.99085067)`.

Diagnostics:

- `rank(A)=24/25`;
- selected exact residual `<1e-15`;
- positive `rho+/-`;
- `eta_R ~= 0.5734264`;
- `s_min ~= 1.999540e-3`;
- condition `~=2313.05`.

Detector-source information gains relative to inherited Toy 009:

- D1 `S_eff`: `x1.7268`;
- D2 `S_eff`: `x1.6838`.

Calibration robustness also improves:

- `s_min` increases about `32%`;
- condition number decreases about `24%`;
- `eta_R` increases slightly.

Target selected mean/noise remain equal to numerical precision and ordered response remains opposite (`~+/-0.01163`).

## Cumulative comparison to Toy 007

Combining Iteration 010 source gains with Iteration 011 calibration gains gives ideal two-band detector-source information approximately

- D1: `x2.11` versus Toy 007;
- D2: `x2.36` versus Toy 007.

This does not include realistic detector covariance or hardware resource penalties.

## New retained rule

`RQIR-CAL-002`: calibration geometry is an active information resource.

Even at fixed source and fixed number/type of exact NP3 constraints, probe location and calibration phases rotate the surviving state-difference direction relative to detector harmonics. Therefore downstream information can change substantially without weakening the formal calibration grade.

Scope: finite-dimensional numerical result, not a universal theorem.

## Files

- `docs/TOY009_JOINT_CALIBRATION_GEOMETRY.md`
- `analysis/toy009_joint_calibration_geometry.py`

## Next gate

The largest remaining weakness is that `S_eff` still uses detector-agnostic/equal-noise band powers. Next iteration should replace the exact `eta/s_min` proxy objective with a declared detector covariance and directly optimize profiled `F_{beta|theta}`. In parallel, realistic D2 thermal/backaction/imprecision covariance and continuous D1 control remain open.
