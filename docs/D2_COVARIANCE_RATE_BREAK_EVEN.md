# RQIR Iteration 033 — D2 Covariance-Rate / Preparation-Metrology Break-Even

**Date:** 2026-08-29  
**Scope:** resource closure for Iteration-032 D2 covariance complementarity.  
**Status:** hard-constrained Toy009/Toy010 resource result; no SI apparatus forecast and no new-physics claim.

## 1. Question

Iteration 032 found a strong Fisher-geometry effect: at `y_ref=-4`, adding four selected detector-native force-covariance rows to the relational-potential + force-mean calibration reduces the independent preparation Fisher required for 90% detector-information retention from

`C_a*=5.82122`

to

`C_a*=0.5889578885`.

Adding all eight force-covariance rows reduces it further to

`C_a*=0.0670833727`.

That result was intentionally not called a wall-clock advantage because the physical Fisher rates of those covariance rows were still unspecified.

This iteration asks the missing resource question:

> How fast must the covariance channel accumulate Fisher information, relative to independent source-state metrology, before the extra covariance measurements actually save wall-clock time?

## 2. Physical covariance Fisher rate

For a stationary Gaussian calibration output with spectral density depending on a nuisance coordinate `u`, the Fisher rate is controlled by the spectral derivative, not by the noise floor alone.

For a multi-channel spectral matrix `S(f;u)`, the local rate has the generic form

`R_u proportional to eta_duty * integral Tr[S^-1 S_,u S^-1 S_,u] df`,

with the exact factor determined by the declared one-sided/two-sided spectral convention.

For the scalar one-sided convention already used in Iteration 022, this reduces to

`q_cov = eta_duty * B_eff * kappa_eff^2`,

where

`kappa_eff = d ln S / du`

for an approximately white band.

This formula is deliberately expressed in the physical nuisance coordinate entering the detector spectrum. Row normalization cannot supply `kappa_eff`.

## 3. New experimental obstruction

### RQIR-NG-013 — covariance-transduction derivative obstruction

An equivalent-force noise PSD `S_F(f)` and a bandwidth are **not sufficient** to assign a physical Fisher rate to a source covariance calibration row.

One also needs the derivative

`d S_detector(f) / d u_cov`

or the corresponding cross-spectral derivative for the declared source covariance coordinate.

Thus a mean-force transduction model does not automatically close the covariance-resource budget. The stochastic/covariance transfer function is an independent experimental input.

This is a G13 measurability/resource obstruction, not a gravity-physics no-go.

## 4. Break-even inequality against source metrology

Suppose a set of covariance rows, each with target row Fisher `gamma_cov`, reduces the required preparation Fisher by `Delta C_a` at fixed calibration scale. If row `i` accumulates physical covariance Fisher at rate `q_i`, its wall-clock cost is

`T_cov = sum_i gamma_cov/q_i`.

The saved source-metrology time is

`Delta T_prep = Delta C_a/R_P`,

where `R_P` is the physical independent preparation Fisher rate from Iteration 020.

Therefore the covariance set is locally wall-clock beneficial only if

`sum_i gamma_cov/q_i < Delta C_a/R_P`.

This is the correct rate comparison; Fisher improvement alone is insufficient.

For equal per-row covariance rate `q_cov`,

`q_cov/R_P > N_rows * gamma_cov / Delta C_a`.

Use the corrected D2 covariance target

`gamma_cov = 0.929e6`.

## 5. Iteration-032 break-even numbers

At `y_ref=-4`, `lambda=1`:

### First, best four force-covariance rows `(0,1,3,7)`

They reduce

`C_a*: 5.82122 -> 0.5889578885`,

so

`Delta C_a = 5.2322621115`.

For four equal-rate rows, wall-clock benefit requires

`q_cov/R_P > 7.102090684e5`.

### Remaining four rows

They reduce

`C_a*: 0.5889578885 -> 0.0670833727`,

only

`Delta C_a = 0.5218745158`.

Their equal-row break-even is much harsher:

`q_cov/R_P > 7.120485648e6`.

### All eight rows at once

Relative to no added force covariance,

`Delta C_a = 5.7541366273`,

and the equal-row threshold is

`q_cov/R_P > 1.291592550e6`.

This converts the Iteration-032 diminishing-Fisher-return observation into a direct physical rate statement.

## 6. Interpretation

The four-row subset is geometrically highly efficient but still demands a covariance Fisher rate about seven hundred thousand times the independent preparation Fisher rate before it beats preparation metrology in wall-clock time at this fixed `lambda=1` comparison.

The second four rows require about seven million times the preparation rate. Therefore their final small gain toward `C_a*=0` is very unlikely to be resource-optimal unless source preparation metrology is extraordinarily slow or the covariance channel has exceptionally large bandwidth/spectral sensitivity.

This is a stronger and more useful statement than saying that all eight rows produce `F_beta|theta~0.8994`.

## 7. Transparent bandwidth examples

Use the Iteration-020 ideal accepted-copy value

`F_Q=13.2707`

and, only for transparent scaling, take `p_P eta_P=1`, so

`R_P=F_Q/t_P`.

For `B_eff=1 kHz`, duty 1, the first-four break-even requires approximately:

- `t_P=1 s`: `kappa_eff > 97.1`;
- `t_P=100 s`: `kappa_eff > 9.71`;
- `t_P=10^4 s`: `kappa_eff > 0.971`.

For the second four rows the corresponding values are roughly

- `307`;
- `30.7`;
- `3.07`.

These are scaling examples, not apparatus predictions. The large change with `t_P` is precisely why the experiment cannot be ranked from Fisher geometry alone.

## 8. New resource rule

### RQIR-RESOURCE-011 — covariance/preparation substitution criterion

A covariance calibration observable should be added only after comparing its physical Fisher acquisition time against the preparation Fisher it removes:

`sum_i gamma_i/q_i < Delta C_a/R_P`.

This rule makes covariance-row selection a **rate-weighted** optimization problem rather than a rank or Fisher-gain problem.

It also shows that the Iteration-032 best four-row subset is only a geometric candidate; the physical best subset may differ once row-specific `q_i` are known.

## 9. Consequence for the D2 phase diagram

The old Iteration-028 phase diagram treated a covariance bundle through one aggregate cost. Iterations 032–033 show that the final physical phase diagram must instead allow row-specific covariance costs:

`K_cov = sum_i gamma_cov,i/q_cov,i`.

The optimization variables should be

`(branch, y_ref, lambda, C_a, covariance subset)`.

The current data already suggest a screening strategy:

1. measure/derive `kappa_i(f)` for the four high-value force-covariance rows `(0,1,3,7)` first;
2. compute their physical `q_i` from the same D2 PSD/bandwidth/duty model;
3. compare `sum gamma/q_i` with `5.232262/R_P`;
4. only if that gate passes consider the remaining four rows.

## 10. Reproducibility

Code:

`analysis/d2_covariance_rate_break_even_iteration033.py`

The script reproduces the documented Iteration-032 `Delta C_a` values, the three rate-ratio thresholds, and the transparent bandwidth/preparation examples with regression assertions.

## 11. Next gate

The next scientifically admissible step is apparatus-level stochastic transduction closure:

- derive `dS_F/d u_cov` and the relevant cross-spectral derivatives for the selected force-covariance rows;
- derive the analogous finite-reference relational covariance derivatives;
- use measured/justified `S_F(f)`, bandwidth and duty;
- insert row-specific `q_i` into the full wall-clock optimizer together with `R_P` and timing recertification duty.

If those derivatives are not experimentally specified, no honest SI-hour ranking of the covariance-complementary branch is possible.
