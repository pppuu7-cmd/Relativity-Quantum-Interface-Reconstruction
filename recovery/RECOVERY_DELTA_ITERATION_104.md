# RQIR Recovery Delta — Iteration 104

**Date:** 2026-08-30  
**Parent front:** Iteration 103.

## What changed

Two late Paper-III resource points are now explicit.

### RQIR-NUM-006 — raw versus final significance

For source-amplitude profiling,

`F_final=A C/(A+C)`.

The historical benchmark `A=25`, `C=225` gives `F_final=22.5`, i.e. `4.74341649 sigma`. It is therefore a **90% retention of a raw 5-sigma detector benchmark**, not a final 5-sigma certificate.

For final `Z=5` with fixed 90% retention use

`A=27.77777778`, `C=250`.

Do not delete the old `C_src=225` convention; retain it as a regression benchmark and label it correctly.

### RQIR-RESOURCE-060 — jointly optimal source metrology

With detector science rate `R_s` and independent source-amplitude rate `R_a`,

`1/F=1/(R_s T_s)+1/(R_a T_a)`.

Minimum total time for final target `F_*` gives

`T_s/T_a=sqrt(R_a/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`,

`r_*=sqrt(R_a)/(sqrt(R_s)+sqrt(R_a))`.

Fixed `r=0.9` is optimal only for `R_a/R_s=81`.

**RQIR-NG-059:** fixed 90% source retention is not a universal minimum-time rule.

### RQIR-RESOURCE-059 — robust campaign simplex

For campaign fractions `x` and apparatus uncertainty `u`,

`R_rob^*=max_x min_u F_beta(sum_k x_k J_k(u))`.

On a fixed identifiable branch with affine Fisher matrices over a polytope uncertainty set, the robust objective is concave in `x` and the uncertainty minimum is attained at a vertex. Thus the robust schedule is a convex finite-vertex problem.

At an optimum with multiple active worst-case vertices, a convex combination of their marginal profile-Fisher rates equalizes across active campaigns.

## Regression

Two vertices `(R_s,R_a)=(1,9)` and `(9,1)` give exact robust fractions `(0.5,0.5)` and guaranteed rate `0.45`. Vertex marginal vectors `(0.81,0.09)` and `(0.09,0.81)` average to `(0.45,0.45)`.

## Files

- `analysis/robust_campaign_source_target_iteration104.py`
- `docs/PAPER_III_ROBUST_CAMPAIGN_SOURCE_TARGET_ITERATION104.md`
- `research_log/2026-08-30_iteration_104_robust_campaign_source_target.md`

## Next admissible gate

Build a unified final-significance Toy009/Toy014 campaign certificate using source metrology as a Fisher campaign and add explicit control/reference recertification scheduling. Keep the old 90%-raw benchmark as regression only. Do not start Toy015 unless the robust dominant marginal resource is source-dependent.
