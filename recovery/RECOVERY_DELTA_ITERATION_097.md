# RQIR Recovery Delta — Iteration 097

**Date:** 2026-08-30  
**Parent front:** Iteration 096.

## Retain

For locally smooth independent characterization coordinates with

`W ~= W_const + sum_i c_i/sqrt(I_i0+R_i t_i)`

and `sum_i t_i=T_char`, the global no-floor optimum is

`boxed{t_i(lambda)=max(0,[(c_i R_i/(2 lambda))^(2/3)-I_i0]/R_i}`

with `lambda` fixed by the total time budget.

Active channels obey equal marginal decision-band shrink rate

`c_i R_i/[2(I_i0+R_i t_i)^(3/2)] = lambda`.

### New labels

- **RQIR-RESOURCE-050:** characterization water-filling.
- **RQIR-NG-050:** equal-time/equal-contraction characterization is generally suboptimal.

This is the finite-time continuation of RESOURCE-048/049.  For floors use the Iteration-096 floor-aware contraction law.  For correlated characterization posteriors use joint Fisher updates.  NG-048 remains active at nonsmooth eigenvalue/corner/active-set changes.

## Files

- `analysis/characterization_waterfill_iteration097.py`
- `docs/PAPER_III_CHARACTERIZATION_WATERFILL_ITERATION097.md`
- `research_log/2026-08-30_iteration_097_characterization_waterfill.md`

## Next gate

Construct a declared primitive Toy009/Toy014 characterization table: central values, uncertainties, physical `R_char`, floors/correlations, duty/cost.  Then run RESOURCE-050 together with RESOURCE-045/NG-030. Do not start Toy015 unless a source-dependent physical bottleneck survives.
