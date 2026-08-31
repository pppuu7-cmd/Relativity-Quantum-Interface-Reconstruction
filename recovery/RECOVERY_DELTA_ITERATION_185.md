# Recovery Delta — RQIR Iteration 185

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 184 instantiated the EH, Ricci2 and RicciBoxRicci soft2 bridge in the split-invariant joint relation `Y=(K2,S_soft2)` but left the dimension-12 `R_mn Box^n R^mn`, n=2..4, cubic soft2 completions BLOCKED.

## New result

The missing n=2..4 local quadratic C5 soft2 columns are now derived with a formal multilinear plane-wave expansion through cubic order and a recursive fully covariant Box acting on the rank-2 Ricci tensor. No row-wise q2 extrapolation is used.

Columns:

- n=2: `[-1.1165183849,-0.0138751458,-1.6820857577,0.2756448325,0.2663354180,0.2728910445]`;
- n=3: `[0.7133600700,0.0017605282,1.0529592750,-0.1111297369,-0.2235239287,-0.1459711976]`;
- n=4: `[-0.4308356613,0.0013520156,-0.6274976618,0.0431046862,0.1618211492,0.0674407295]`.

Maximum soft extrapolation error: `3.04e-10`.

Source-completed Ward check: maximum relative residual `<5.3e-14`, status `PASS_MACHINE_PRECISION_SCOPED`.

## Numerical correction to Iteration 184

The formal expansion shifts the n=0 and n=1 columns by maxima `2.30e-7` and `6.54e-7`. The earlier error estimate covered soft Richardson convergence but not the nested finite-position derivative used to build Ricci derivatives. This is a numerical provenance correction, not a consistency FAIL.

Retain `NUM-NG-003` and use the formal Iteration-185 values for subsequent compensation.

## Hard-conditioned local compensation now complete

For the Iteration-183 K2-null vector with normalized nonlocal coefficient +1, the complete local soft2 compensation piece is

`[0.6749106619,0.0904184173,1.6058813167,-0.8456710924,-0.0817908525,0.0404129788]`.

This closes the local dimension-12 compensation data required before the nonlocal comparator can be tested.

## Retained results

- `C5-NG-013 — COVARIANT_RICCI_BOX2_TO_BOX4_SOFT2_LADDER_IS_NONTRIVIAL_AND_NOT_GENERATED_BY_ROW_WISE_Q2_MULTIPLICATION`;
- `NUM-NG-003 — NESTED_POSITION_SPACE_DIFFERENCING_CAN_UNDERSTATE_TOTAL_OPERATOR_CALCULUS_ERROR_EVEN_WHEN_SOFT_RICHARDSON_ERROR_IS_SMALL`;
- `REL-NG-003 — DIMENSION12_LOCAL_K2_COMPENSATION_NOW_HAS_A_COMPLETE_SOURCE_COMPLETED_SOFT2_VECTOR`.

## Classification

- local C5 quadratic soft2 ladder: `COMPLETE_SCOPED`;
- full nonlocal lambda soft2 tangent: `BLOCKED_NEXT_GATE`;
- robust novelty residual: none;
- `ANSATZ-003`: NOT CREATED;
- Fisher/resources: FORBIDDEN.

## Readiness

`MODEL_READINESS: 24%` — unchanged. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Exact restart instruction

Resume at **Iteration 186**:

1. compute the full source-completed `QG-NL-EXP-001` lambda soft2 tangent at the frozen lambda=1 convention from the same parent action, including the Frechet/operator variation of the exponential form factor;
2. add the fixed Iteration-185 local compensation soft2 vector so the combined direction preserves all six K2 rows exactly;
3. project this single conditioned nonlocal direction against the zero-K2 curvature-cubic rank-4 span;
4. compare the residual to the frozen Iteration-178 numerical envelope `5.2625580e-6` and explicitly classify exact identity / near-degeneracy / resolvable residual;
5. only if a resolvable residual survives proceed toward AS/C3 quotient; otherwise widen the target-independent hard-row lever arm before novelty promotion.

No `ANSATZ-003`, Fisher or resources before full quotient survival.
