# RQIR Research Log — Iteration 292

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Question

What loop denominator families remain after replacing the weighted proxy `tr(B3)` by the actual cubic `Tr U1 = Tr(B Y_down)` coefficient?

## Result

The exact primitive census contains 36 branches and reconstructs the direct complete trace to `4.58e-13` at the frozen checkpoint.

The main new fact is topological: local weight insertions create lower-background-order B blocks whose endpoint momenta differ. This adds ordinary bubbles and ordinary triangles to the previously raised-only family set.

Counts:

- raised bubbles 10;
- raised triangles 12;
- ordinary bubbles 5;
- ordinary triangles 8;
- single scaleless 1.

After the null ordinary/raised bubbles and the single squared-denominator branch are declared scaleless in massless DR, 32 primitive branches remain non-scaleless.

## Degree bounds

Analytic primitive power counting gives ordinary bubble degree `<=2`, ordinary triangle degree `<=4`, while the previous conservative raised bounds `<=4` and `<=6` remain.

## Classification

`PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

## Next

Held-out family-summed polynomial reconstruction for all eight non-scaleless sectors, then corrected tensor/Laurent reduction.
