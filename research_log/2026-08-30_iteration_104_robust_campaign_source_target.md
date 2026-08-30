# RQIR Research Log — Iteration 104

**Date:** 2026-08-30

## Goal

Continue Paper III from Iteration 103 by robustifying the campaign simplex and auditing whether the historical `C_src=225` 90%-retention convention is a final-significance certificate or only a raw-detector regression benchmark.

## Numerical consistency correction

For local source-amplitude profiling,

`F_final=A C/(A+C)`.

The mature benchmark `A=25`, `C=225` gives

`F_final=22.5`, `sqrt(F_final)=4.74341649`.

Therefore **RQIR-NUM-006** distinguishes:

- raw detector 5-sigma Fisher `A=25` with 90% retained information;
- final post-source-profile 5-sigma Fisher target `F_final=25`.

For final `F=25` at fixed 90% retention the consistent requirements are

`A=25/0.9=27.77777778`,

`C=25/0.1=250`.

The old `C_src=225` remains valid as a raw-5-sigma 90%-retention regression convention; it is not deleted.

## Joint source-time optimum

With raw detector science rate `R_s` and independent source-amplitude rate `R_a`,

`1/F=1/(R_s T_s)+1/(R_a T_a)`.

Minimum total time for a final target gives

`T_s/T_a=sqrt(R_a/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`,

and optimal retained fraction

`r_*=sqrt(R_a)/(sqrt(R_s)+sqrt(R_a))`.

Thus fixed 90% retention is wall-clock optimal only for `R_a/R_s=81`.

Registered as **RQIR-RESOURCE-060** and **RQIR-NG-059**.

## Robust campaign theorem

For apparatus uncertainty `u` and campaign fractions `x`, define

`R_rob^*=max_x min_u F_beta(sum_k x_k J_k(u))`.

On a fixed identifiable affine uncertainty branch, the profile Fisher is concave; for a polytope uncertainty set the minimum is attained at an extreme point. The robust simplex optimization is therefore convex and finite-vertex auditable.

Registered as **RQIR-RESOURCE-059**.

At a robust optimum with several active worst-case vertices, a convex combination of their efficient-direction marginal rates equalizes across active campaigns.

## Regression

Two uncertainty vertices `(R_s,R_a)=(1,9)` and `(9,1)` have robust optimum fractions `(0.5,0.5)` and guaranteed rate `0.45`. Their marginal campaign rates are `(0.81,0.09)` and `(0.09,0.81)`; equal scenario weights produce `(0.45,0.45)`, verifying the robust KKT rule.

## Files

- `analysis/robust_campaign_source_target_iteration104.py`
- `docs/PAPER_III_ROBUST_CAMPAIGN_SOURCE_TARGET_ITERATION104.md`
- `recovery/RECOVERY_DELTA_ITERATION_104.md`

## Next gate

Build the unified final-significance Toy009/Toy014 campaign certificate with source metrology as a Fisher campaign rather than a fixed `C_src` add-on, while retaining the historical 90%-raw benchmark for regression. Add control/reference recertification constraints next. Do not open Toy015 unless the residual robust marginal cost is source-dependent.
