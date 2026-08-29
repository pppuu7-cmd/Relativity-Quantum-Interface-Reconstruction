# RQIR Iteration 021 — Full Wall-Clock Rate Optimization

**Date:** 2026-08-29  
**Status:** parametric resource theorem + exact hard-constrained Toy009 optimization; not a hardware forecast.

## 1. Question

Iterations 019–020 replaced two standardized sensitivity placeholders by native rate models:

- D1/D2 detector Fisher rates;
- source-preparation amplitude metrology through the Toy009 quantum Fisher information.

The next requested step is to optimize the complete profiled Fisher information per wall time.

The crucial issue is that the repository still does **not** contain hardware-specific per-second Fisher rates for:

1. the 14 gravitational mean-calibration rows;
2. the 8 gravitational covariance/noise rows;
3. the independent timing/additive/reference-control priors introduced in Iteration 016.

Therefore a unique answer in seconds or hours is mathematically underdetermined. Assigning one would require inventing an unstated sensor-noise model.

## 2. RQIR-RESOURCE-005 — wall-clock identifiability condition

Let

\[
R_D,\;R_P,\;R_M,\;R_C
\]

be Fisher-information rates per wall second for detector, independent source preparation metrology, gravitational mean calibration, and gravitational covariance calibration.

Then the optimal wall-clock allocation is well-defined only after these rates (and the separate control-prior rates) are specified.

**RQIR-RESOURCE-005:** dimensionless Fisher requirements such as `gamma_mean`, `gamma_cov`, or `C_a` do not determine wall-clock cost by themselves. A wall-clock optimum requires a physical information rate for every independent resource channel.

This is a resource-identifiability statement, not a physical no-go theorem.

## 3. Exact reduced Fisher used here

The calculation uses the corrected Iteration-015 construction:

- trace and energy constraints are eliminated exactly;
- the source nuisance sector is 22 dimensional;
- no `1e12` pseudo-prior is used;
- D1 and D2 are treated separately.

For wall-time fractions

\[
x_D+x_P+x_M+x_C=1,
\]

the information strengths are

\[
S=R_Dx_D,
\quad C_a=R_Px_P,
\quad \gamma_M=R_Mx_M,
\quad \gamma_C=R_Cx_C.
\]

The local detector model has parameters `(beta,a,u)` and is profiled over the hidden source amplitude `a` plus the 22 hard-constrained source nuisances.

## 4. Numerical rate-ratio map

Set `R_D=1` only to define the time unit. The following are **dimensionless rate-ratio diagnostics**, not experimental forecasts.

### D1

| `R_P/R_D` | `R_M/R_D=R_C/R_D` | detector | preparation | mean cal | cov cal | `F_beta/T` |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1e4 | 0.249 | 0.167 | 0.377 | 0.206 | 0.0280 |
| 1 | 1e6 | 0.408 | 0.398 | 0.137 | 0.057 | 0.1581 |
| 10 | 1e4 | 0.282 | 0.060 | 0.426 | 0.233 | 0.0357 |
| 10 | 1e6 | 0.561 | 0.173 | 0.188 | 0.078 | 0.2981 |
| 100 | 1e6 | 0.636 | 0.062 | 0.213 | 0.089 | 0.3832 |
| 100 | 1e8 | 0.867 | 0.087 | 0.033 | 0.014 | 0.7506 |

### D2

| `R_P/R_D` | `R_M/R_D=R_C/R_D` | detector | preparation | mean cal | cov cal | `F_beta/T` |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1e4 | 0.255 | 0.149 | 0.413 | 0.183 | 0.0221 |
| 1 | 1e6 | 0.397 | 0.387 | 0.165 | 0.051 | 0.1501 |
| 10 | 1e4 | 0.284 | 0.052 | 0.460 | 0.204 | 0.0273 |
| 10 | 1e6 | 0.539 | 0.167 | 0.225 | 0.069 | 0.2777 |
| 100 | 1e6 | 0.609 | 0.060 | 0.254 | 0.078 | 0.3537 |
| 100 | 1e8 | 0.862 | 0.086 | 0.040 | 0.012 | 0.7421 |

The large change in allocation with the calibration-rate ratio is the important result. A fixed statement such as “90% of detector information should be retained” is not generally wall-clock optimal.

## 5. Regression to Iteration 018

If gravitational calibration becomes effectively free,

\[
R_M,R_C\rightarrow\infty,
\]

the optimum must reduce to the two-resource detector/preparation problem.

The numerical optimizer reproduces

\[
x_D=\frac{\sqrt{R_P}}{\sqrt{R_D}+\sqrt{R_P}},
\qquad
x_P=\frac{\sqrt{R_D}}{\sqrt{R_D}+\sqrt{R_P}},
\]

with calibration fractions tending to zero.

This provides an independent regression check of RQIR-RESOURCE-003.

## 6. New design consequence

At equal normalized calibration rates, D2 consistently allocates somewhat more time to mean calibration than D1 in the tested intermediate regime. This is consistent with the earlier finding that the two detector branches couple differently to the same source nuisance space.

The stronger conclusion is general:

> The resource bottleneck can migrate between detector statistics, source-state metrology, mean calibration, and covariance calibration as the physical rate ratios change.

Therefore branch ranking must use the full profiled Fisher per second, not detector-only Fisher or a fixed-retention convention.

## 7. Why this is not yet the final wall-clock answer

Iteration 016 proved that uncontrolled timing/additive systematics can drive `F_beta` to zero even with arbitrarily large gravitational calibration exposure. Those independent control priors therefore cannot be omitted from a final resource budget.

The current optimizer deliberately does not fabricate a conversion from reference-channel seconds to prior precision. Its output is an upper-bound/core allocation conditional on adequate systematic control.

A complete hardware-level objective must add at least:

\[
R_{\tau},\;R_{b_M},\;R_{b_C},\;R_g
\]

for clock/timing, mean offset, covariance offset, and gain-reference information rates.

## 8. Next gate

Measure or adopt explicit physical noise models for the gravitational calibration and reference channels, then insert their Fisher rates into this optimizer. The highest-value next theoretical step is to derive those rates from concrete measurement models rather than standardized `xi` values.

For D1 this means a phase/reference readout model for each calibration setting. For D2 it means equivalent-force PSD and reference-channel PSD for the mean/covariance settings. Only then is a unique `F_beta|theta/T_wall` in SI wall time scientifically justified.

## Reproducibility

Code: `analysis/full_wallclock_rate_optimizer_iteration021.py`.
