# Recovery delta — Iteration 285

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

## New authoritative correction

The actual denominator-stripped same-parent primitive numerator oracle has now been evaluated.

Exact oracle cross-check:

- primitive branch count: 23;
- `tr B3 = 0.9605914097678994`;
- `||B3||_F = 1.3106212324929962`;
- primitive-vs-direct matrix residual: `1.32e-12`.

The previous Iteration-283/284 claim that the actual numerator can be reconstructed in denominator-only scalar bases of dimensions 9 (bubble) and 50 (triangle) is **superseded**.

Held-out failures:

- bubble-a 9 basis: relative max error `0.9481`;
- bubble-b 9 basis: relative max error `0.6811`;
- triangle `(0,0.41)` 50 basis: relative max error `33.2056`.

Conservative complete fixed-coordinate polynomial reconstructions pass:

- bubble-a degree<=4 / 70 monomials: relative max residual `9.30e-10`;
- bubble-b degree<=4 / 70 monomials: relative max residual `2.22e-9`;
- triangle `(0,0.41)` degree<=6 / 210 monomials: relative max residual `8.87e-11`.

## Retain

- exact translation closure;
- nonzero translation-closed B3;
- timelike continuation nonzero;
- 23 primitive denominator branches;
- raised bubble/triangle topology with no closed box master;
- repeated-index canonical sectors;
- exact numerator degree ceilings: bubble<=4, triangle<=6;
- scalar master cut-support basis.

## Supersede

Only the sufficiency of the Iteration-283/284 9/50 denominator-only numerator bases.

Reason: the same-parent numerator contains additional frozen external structures, including the null-soft momentum and TT polarization tensors. Propagator topology alone does not exhaust numerator dependence.

## Current blocker

`BLOCKED_COMPLETE_TENSOR_AWARE_NUMERATOR_RECONSTRUCTION_AND_IBP_REDUCTION`.

## Exact next gate — Iteration 286

Run full degree<=6 / 210-monomial held-out reconstruction for triangle sectors `(0,0.21)` and `(0.21,0.41)`. Then translate all validated 70/210 polynomial coefficients into an IBP/tensor-moment or explicitly complete covariant representation before extracting hard-channel log/discontinuity coefficients.

No `ANSATZ-003`. No Fisher/resources. MODEL_READINESS remains 24%.
