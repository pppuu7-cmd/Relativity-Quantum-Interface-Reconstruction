# Recovery Delta — RQIR Iteration 184

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 183 froze the split-invariant joint relation `Y=(K2,S_soft2)` and showed that the six-row nonlocal lambda `K2` tangent is exactly compensable by the local dimension-12 quadratic kernel basis. The physical discriminator is therefore the full soft2 cubic response of the K2-preserving parameter combination.

## New computed soft2 cubic columns

Same six null-soft TT rows, amputated metric cubic kernel, symmetric soft second derivative plus two Richardson levels:

- EH/common normalization:
  `[1.5075719591,0.2125004724,2.8203238064,-1.9851779883,-0.1902862337,0.5362481602]`;
- `R_mn R^mn`:
  `[-1.7423297741,-0.1323560370,-3.3439158197,1.3579882480,0.2206726509,0.2169373627]`;
- `R_mn Box R^mn`:
  `[1.5754151008,0.0489981406,2.5059613346,-0.6443314817,-0.2558359645,-0.3828535821]`.

Maximum convergence error estimates are respectively `1.66e-7`, `1.83e-7`, `2.92e-7`.

Source-completed Ward checks pass with residual reduction factors `4.000076` and `4.000001` for Ricci2 and RicciBoxRicci.

## Rank result and hard-constraint interpretation

Zero-K2 local curvature-cubic soft2 span: rank 4.

- add EH soft2 -> raw rank 5;
- add Ricci2 soft2 -> raw rank 6/6;
- add RicciBoxRicci -> raw rank remains 6.

Final raw singular values:

`[6.23544511,2.17522779,1.08511093,0.09623304,0.04245038,7.53404e-4]`.

Do **not** interpret this as calibrated comparator saturation. The six local quadratic K2 directions `[x,...,x^6]` have rank 6/6, hence their own exact-calibration parameter nullspace is zero. These soft2 columns re-enter only in fixed compensation combinations with nonlocal/AS K2 changes.

## Retained results

- `C5-NG-011 — EH_AND_RICCI2_SOFT2_COLUMNS_COMPLETE_THE_RAW_SIX_ROW_LOCAL_C5_SOFT2_RANK_BUT_NOT_THE_HARD_CONDITIONED_SPAN`;
- `REL-NG-002 — RAW_CUBIC_ROW_SATURATION_BY_PARAMETERS_ELIMINATED_BY_EXACT_K2_CALIBRATION_IS_NOT_CONDITIONED_COMPARATOR_SATURATION`;
- `C5-NG-012 — HIGHER_QUADRATIC_DERIVATIVE_SOFT2_COLUMNS_MUST_BE_DERIVED_COVARIANTLY_AND_NOT_INFERRED_FROM_N0_N1`.

## Remaining local gap

Still required through the frozen dimension-12 quadratic basis:

- `R_mn Box^2 R^mn`;
- `R_mn Box^3 R^mn`;
- `R_mn Box^4 R^mn`.

Their cubic soft2 completions require full covariant operator calculus; simple q2 multiplication is forbidden.

## Readiness

`MODEL_READINESS: 24%` — unchanged. Comparator foundation remains `24/25`.

## Exact restart instruction

Resume at **Iteration 185**:

1. derive/validate covariant cubic soft2 columns for the n=2,3,4 Ricci-Box quadratic ladder;
2. compute full `QG-NL-EXP-001` soft2 lambda tangent including Frechet variation;
3. use the Iteration-183 K2-null vector to form the single calibrated nonlocal soft2 direction;
4. compare it against the zero-K2 local curvature-cubic conditional span and the numerical envelope;
5. if current q2 leverage remains sub-resolution, freeze a wider target-independent hard-row protocol before any rank promotion;
6. then proceed to AS and C3 closure.

No ANSATZ-003, Fisher or resources before full quotient survival.
