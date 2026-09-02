# Candidate Gravity C5 — Iteration 286 complete non-scaleless numerator reconstruction

**Date:** 2026-09-02  
**MODEL_READINESS:** **24%**

## Purpose

Iteration 285 established the actual denominator-stripped same-parent numerator oracle and corrected the incomplete denominator-only 9/50 reconstruction bases. Bubble-a and bubble-b were already certified in complete degree-`<=4` 70-monomial fixed-coordinate bases, and triangle sector `(0,0.41)` was certified in a complete degree-`<=6` 210-monomial basis.

Iteration 286 closes the two remaining raised-triangle sectors with independent train/held-out oracle samples.

## Results

### Raised triangle `(0,0.21)`

- basis size: `210`;
- train points: `220`;
- held-out points: `28`;
- train rank: `210/210`;
- condition number: `6935.030221597978`;
- held-out max absolute residual: `3.411443627587829e-10`;
- held-out RMS residual: `9.833419662207988e-11`;
- held-out relative max residual: `2.7698947208544858e-11`.

Status: `PASS`.

### Raised triangle `(0,0.41)`

Retained from Iteration 285:

- rank `210/210`;
- condition number `5186.568989589245`;
- held-out relative max residual `8.872284498320589e-11`.

Status: `PASS`.

### Raised triangle `(0.21,0.41)`

- basis size: `210`;
- train points: `220`;
- held-out points: `28`;
- train rank: `210/210`;
- condition number: `8545.513087076448`;
- held-out max absolute residual: `1.242611014085071e-10`;
- held-out RMS residual: `5.204178930132884e-11`;
- held-out relative max residual: `1.0083215501606952e-11`.

Status: `PASS`.

## Full non-scaleless reconstruction status

The complete translation-closed non-scaleless scalar orbit-trace numerator is now covered by held-out actual-oracle reconstructions:

- bubble-a: degree `<=4`, 70-monomial basis, relative max residual `9.30e-10`;
- bubble-b: degree `<=4`, 70-monomial basis, relative max residual `2.22e-9`;
- triangle `(0,0.21)`: degree `<=6`, 210-monomial basis, relative max residual `2.77e-11`;
- triangle `(0,0.41)`: degree `<=6`, 210-monomial basis, relative max residual `8.87e-11`;
- triangle `(0.21,0.41)`: degree `<=6`, 210-monomial basis, relative max residual `1.01e-11`.

The null raised bubbles and single squared sector remain scaleless in the frozen massless dimensional-regularization treatment.

Freeze:

`PASS_COMPLETE_NONSCALELESS_ACTUAL_ORACLE_NUMERATOR_RECONSTRUCTION_ALL_BUBBLE_AND_TRIANGLE_SECTORS`.

## Scientific consequence

The numerator-reconstruction blocker is now closed. This is not yet a physical hard-channel discontinuity coefficient and not a Candidate Gravity residual. The next task is to reduce these complete numerator polynomials against the canonical raised propagator families using tensor moments / IBP while preserving the retarded hard-channel normalization.

## Current blocker

`BLOCKED_IBP_TENSOR_MOMENT_REDUCTION_AND_HARD_CHANNEL_COEFFICIENT_EXTRACTION`.

## Readiness

`MODEL_READINESS = 24%`, unchanged. No comparator-subtracted linked observable exists yet.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Exact next gate — Iteration 287

Start with bubble-a and bubble-b because their complete numerator degree is only four. Reduce every 70-monomial coefficient into Lorentz tensor moments of

`1 / [(l^2)^2 ((l+q)^2)]`

and extract the coefficient multiplying the retarded logarithmic/discontinuity term. Verify loop-reflection invariance and dimensional-regularization scaleless cancellations. Then perform the analogous reduction for the three degree-six triangle sectors. Do not use the superseded 9/50 numerator bases.
