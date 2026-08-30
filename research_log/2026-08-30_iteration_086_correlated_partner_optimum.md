# RQIR Research Log — Iteration 086

**Date:** 2026-08-30

## Goal

Audit the new Iteration-085 correlated two-band Fisher law for hidden monotonicity assumptions before using it as an apparatus specification.

## Result

For

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`,

fix `r_weak=b` and write `t=sqrt(r_partner/b)`. Then

`R_beta/b = 4 t^2/(t^2+1+2 rho t)`

and

`d(R_beta/b)/dt = 8 t(1+rho t)/(t^2+1+2 rho t)^2`.

For `rho>=0`, partner strength is monotone useful and the supremum is the familiar asymptotic `4 b`.

For `rho<0`, the rate has a finite maximum at

`r_partner/b = 1/rho^2`,

with

`R_beta,max = 4 b/(1-rho^2)`.

Therefore the Iteration-085 asymptotic statement was correct, but its conversion into a global correlated-band ceiling and blanket `r_n>R_*/4` requirement was too strong.

Explicit counterexample:

`rho=-0.5`, `r_weak=1`, `r_partner=4` gives

`R_beta=16/3=5.3333333333 > 4 r_weak`.

New **RQIR-CORR-001:** `4 r_weak` is a global ceiling only for nonnegative correlation. Under negative correlation the finite optimum is `4 r_weak/(1-rho^2)`.

The corrected weak-band feasibility floor is

- `r_weak >= R_*/4` for `rho>=0`;
- `r_weak >= (1-rho^2)R_*/4` for `rho<0`, subject to measured/stable covariance and conditioning.

At fixed total raw rate `r2+r4`, balanced bands remain optimal for every `|rho|<1`.

## Numerical regression

The deterministic script checks the explicit counterexample, exact finite optimum, positive-correlation monotonic limit, fixed-total balance, and 1000 random negative-correlation cases. Maximum relative discrepancy between scan and analytic optimum is about `3.33e-15`.

## Decision

Do not optimize a simultaneous detector from marginal ASD/rates alone, and do not assume more raw rate in one band is always useful when the matched-filter outputs are anti-correlated. Optimize the full `(r2,r4,rho_eff)` likelihood and propagate correlation uncertainty/conditioning.

## Reproduce

`python analysis/correlated_partner_optimum_iteration086.py`

## Document

`docs/PAPER_III_CORRELATED_PARTNER_OPTIMUM_ITERATION086.md`
