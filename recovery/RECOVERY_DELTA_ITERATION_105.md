# RQIR Recovery Delta — Iteration 105

**Date:** 2026-08-30  
**Parent front:** Iteration 104.

## What changed

Toy009/Toy014 comparison is now expressed directly in final-significance physical rate coordinates after optimal source-amplitude scheduling.

For architecture `i`, compress the already optimized detector/transfer/seven-calibration side to `R_D,i` and independent source-amplitude metrology to `R_A,i`.

`R_final,i = 1/[1/sqrt(R_D,i)+1/sqrt(R_A,i)]^2`.

With multiplicative duty `d_i`, use `Q_i=(1-d_i)R_final,i`.

### RQIR-RESOURCE-061

Define

`u=R_D,14/R_D,09`,

`v=R_A,14/R_A,09`,

`z=R_A,09/R_D,09`,

`delta=(1-d_14)/(1-d_09)`.

Then

`Q_14/Q_09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

With `w=1/sqrt(z)`, a positive finite crossing is

`w_cross=[1/sqrt(u)-sqrt(delta)]/[sqrt(delta)-1/sqrt(v)]`,

`z_cross=1/w_cross^2`.

### RQIR-DESIGN-012

Source domination favors Toy014 exactly when `v>u`; favors Toy009 when `v<u`; if `v=u` the source/detector balance does not change the ranking apart from duty.

### RQIR-NG-060

The Toy014 Ramsey/source ratio alone is not a final architecture certificate. A valid source-rescue statement requires common-normalization `u,v,z,delta` or the underlying robust Fisher matrices.

## Regression only

Using the retained Toy014/Toy009 shared-kernel **science-only** rate ratio

`u_reg=0.2830146574583767`

and zero-reset Ramsey rate ratio

`v_reg=1.4913343179877905`,

equal duty gives

`z_cross=0.042393961570158255`.

This is not the full detector+seven-calibration result; it is only a consistency slice.

With illustrative `d09=.02`, `d14=.08`, `z_cross=0.027135455186203732`.

## Files

- `analysis/final_significance_architecture_crossover_iteration105.py`
- `docs/PAPER_III_FINAL_SIGNIFICANCE_ARCHITECTURE_CROSSOVER_ITERATION105.md`
- `research_log/2026-08-30_iteration_105_final_significance_architecture_crossover.md`

## Next admissible gate

Determine or bound the robust common-apparatus detector-side rate ratio `u=R_D,14/R_D,09` after complex transfer calibration, temporal covariance uncertainty, all seven physical calibration layers and mandatory detector/control scheduling. If no full apparatus matrix is available, derive measurable threshold surfaces rather than fabricate an absolute winner. Do not start Toy015 unless the remaining dominant marginal cost is source-dependent.
