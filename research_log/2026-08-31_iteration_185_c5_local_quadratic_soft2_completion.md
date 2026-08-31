# RQIR Research Log — Iteration 185

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Completed the remaining local quadratic C5 soft2 ladder required by the Iteration-183 joint `(K2,S_soft2)` hard-conditioning protocol.

A formal multilinear plane-wave expansion through cubic order was used to evaluate `sqrt(-g) R_mn Box^n R^mn` with a recursive fully covariant rank-2 Box. This includes connection, inverse-metric and operator-variation terms and therefore does not infer n=2..4 by multiplying lower-order columns by powers of q2.

New six-row soft2 columns:

- `R_mn Box^2 R^mn`: `[-1.1165183849,-0.0138751458,-1.6820857577,0.2756448325,0.2663354180,0.2728910445]`;
- `R_mn Box^3 R^mn`: `[0.7133600700,0.0017605282,1.0529592750,-0.1111297369,-0.2235239287,-0.1459711976]`;
- `R_mn Box^4 R^mn`: `[-0.4308356613,0.0013520156,-0.6274976618,0.0431046862,0.1618211492,0.0674407295]`.

Maximum soft extrapolation errors are below `3.1e-10`. Source-completed Ward residuals are at machine precision: maximum relative residual below `5.3e-14`.

The formal calculus also exposed an Iteration-184 numerical bookkeeping issue: previous quoted soft Richardson errors did not include the nested finite-position derivative error. The n=0/1 values shift by at most `2.30e-7` and `6.54e-7`. This is `NUM-NG-003`, not a physics FAIL.

Using the exact Iteration-183 K2-null vector, the now-complete local soft2 compensation piece for the normalized nonlocal direction is

`[0.6749106619,0.0904184173,1.6058813167,-0.8456710924,-0.0817908525,0.0404129788]`.

Retain:

- `C5-NG-013 — COVARIANT_RICCI_BOX2_TO_BOX4_SOFT2_LADDER_IS_NONTRIVIAL_AND_NOT_GENERATED_BY_ROW_WISE_Q2_MULTIPLICATION`;
- `NUM-NG-003 — NESTED_POSITION_SPACE_DIFFERENCING_CAN_UNDERSTATE_TOTAL_OPERATOR_CALCULUS_ERROR_EVEN_WHEN_SOFT_RICHARDSON_ERROR_IS_SMALL`;
- `REL-NG-003 — DIMENSION12_LOCAL_K2_COMPENSATION_NOW_HAS_A_COMPLETE_SOURCE_COMPLETED_SOFT2_VECTOR`.

No Candidate Gravity residual is promoted. `ANSATZ-003` is not created. Fisher/resources remain forbidden.

**MODEL_READINESS: 24%** — unchanged from Iteration 184. Comparator completion improved, but the fixed calibrated nonlocal direction is still missing and robust unique residual remains `0/20`.

Next: Iteration 186, full `QG-NL-EXP-001` lambda soft2 tangent including Frechet/operator variation, followed by addition of the fixed local compensation vector and quotient against the zero-K2 curvature-cubic span.
