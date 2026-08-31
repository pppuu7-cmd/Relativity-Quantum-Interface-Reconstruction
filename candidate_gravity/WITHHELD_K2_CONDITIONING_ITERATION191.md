# Candidate Gravity — Iteration 191: withheld K2 conditioning breaks six-row saturation

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Preregistered test

Evaluate only comparator `K2` information on `RQIR-WITHHELD-NULLSOFT-12-v1`, frozen in Iteration 190 before any candidate test.

Local C5 quadratic dimension-12 basis:

`A=[x,x^2,x^3,x^4,x^5,x^6]`.

Fixed nonlocal lambda tangent at `lambda=1`:

`v_NL=x^2 exp(x)`.

## Result

On the twelve withheld hard rows:

- `rank(A)=6`;
- `rank([A,v_NL])=7`;
- smallest augmented singular value `1.3903846e-7`.

The best local polynomial fit leaves

- L2 residual `2.5194898e-7`;
- max absolute residual `1.4983505e-7`;
- relative L2 residual `1.2699307e-7`.

Because the augmented system is ill-conditioned, a high-precision certificate was added. The first seven withheld rows in preregistered row-id order give the 7x7 minor

`det = 1.08954106917884588546e-28 != 0`

at 70-digit evaluation.

Thus the augmented rank increase is not double-precision noise.

## Interpretation

The exact local compensation of the nonlocal `K2` tangent on the original six rows was **finite-sample saturation**: six local polynomial coefficients were evaluated on six points.

The prospectively frozen twelve-row extension breaks that degeneracy. Within the frozen seven-parameter block there is no nontrivial parameter direction containing the nonlocal lambda variation that preserves all twelve `K2` rows exactly.

Therefore exact `K2` hard calibration removes this nonlocal nuisance direction from a zero-`delta K2` conditional soft2 quotient on the withheld block.

This is not Candidate Gravity novelty and no candidate has been evaluated.

## Retained results

- `NL-NG-006 — WITHHELD_ROWS_BREAK_THE_SIX_POINT_LOCAL_POLYNOMIAL_COMPENSATION_OF_THE_NONLOCAL_K2_TANGENT`.
- `REL-NG-008 — EXACT_K2_CALIBRATION_REMOVES_THE_NONLOCAL_LAMBDA_NUISANCE_DIRECTION_ON_THE_WITHHELD_12ROW_BLOCK`.
- `NG-FUNNEL-046 — FINITE_ROW_HARD_CONSTRAINT_SATURATION_MUST_BE_RETESTED_ON_PROSPECTIVELY_FROZEN_ROWS`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. AS/C3 remain blocked and no future model has yet survived the withheld comparator construction.
