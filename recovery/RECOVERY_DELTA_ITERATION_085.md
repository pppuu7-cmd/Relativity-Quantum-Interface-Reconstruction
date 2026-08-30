# RQIR Recovery Delta — Iteration 085

**Date:** 2026-08-30  
**Authority:** read after `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, `recovery/CURRENT_FRONT.md`, and Iteration-084 materials.

## New retained result

Iteration 085 closes the simultaneous two-band detector cross-PSD algebra.

For two matched-filter science channels with raw single-band Fisher rates `r2,r4` and effective noise correlation `rho_eff` after phase/sign convention,

`R_beta = 4 r2 r4 /(r2+r4+2 rho_eff sqrt(r2 r4))`.

This is obtained by exact Schur profiling of the antisymmetric spectral-tilt nuisance in the full `2x2` covariance likelihood.

### RQIR-RESOURCE-039

The Iteration-084 independent-band law is exactly the `rho_eff=0` special case of the matrix result.

### RQIR-NG-036

A physical simultaneous two-band forecast cannot be normalized from marginal ASD/PSD values alone when cross-channel noise may be present. Require the full positive-definite spectral matrix/covariance or a justified negligible-cross-term approximation.

Balanced case:

`r2=r4=r -> R_beta=2r/(1+rho_eff)`.

Weak-band ceiling survives finite correlation:

`r_partner -> infinity -> R_beta -> 4 r_weak`.

Therefore NG-035 remains active.

## Numerical certificate

`analysis/correlated_dual_band_fisher_iteration085.py` verifies 1000 random positive-definite covariance cases. Maximum Schur-vs-closed-form absolute error in the stored deterministic test is about `1.0644e-12`.

## Files

- `analysis/correlated_dual_band_fisher_iteration085.py`
- `docs/PAPER_III_CORRELATED_DUAL_BAND_FISHER_ITERATION085.md`
- `research_log/2026-08-30_iteration_085_correlated_dual_band_fisher.md`

## Next admissible gate

Obtain/build one declared simultaneous detector spectral matrix and transfer vector at the two retained science bands:

`{g2,g4,S_F,2,S_F,4,S_F,24}`

with finite-window transfer and uncertainty intervals. Convert it to `R_beta` using Iteration 085, then use the same apparatus noise/transfer model for all seven calibration layers to derive `R_cal,j`, add `R_src` and control duty, and only then perform NG-030 Toy009/Toy014 robust wall-clock dominance.

Do not start Toy015 merely to avoid the apparatus closure problem.
