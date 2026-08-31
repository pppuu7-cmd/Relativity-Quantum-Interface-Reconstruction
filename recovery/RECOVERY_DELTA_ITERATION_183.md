# Recovery Delta — RQIR Iteration 183

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 182 exposed a definition-level ambiguity in the off-shell split `Gamma_soft=W[K2]+Rlin:B` when `K2!=0`. The fixed nonlocal comparator could not be assigned a unique `B_T` column by raw cubic calculation plus Ward checks alone.

## Protocol repair

Do not promote the internal split to an observable. Freeze the joint source-completed relation vector

`Y=(K2_rows,S_soft2_full_rows)`.

Let comparator/nuisance parameter tangents be

`A=dK/dtheta`, `B=dS/dtheta`.

Exact quadratic calibration is a hard constraint:

`A delta_theta=0`.

If `N_A` spans `ker(A)`, use

`B_cond=B N_A`

as the allowed cubic comparator span after calibration.

This is invariant under internal Ward/transverse repartition because only the full source-completed `S_soft2` is used. Numerical split-repartition discrepancy is `4.44e-16`.

## Six-row quadratic certificate

Frozen hard invariants:

`x=q^2=[0.5076,0.3854,0.4260,0.3153,0.4004,0.2882]`.

Local C5 quadratic inverse-kernel basis through the dimension-12 convention, with common EH/normalization direction:

`[x,x^2,x^3,x^4,x^5,x^6]`.

Certificate:

- local rank `6/6`;
- condition number `2.398198742e7`;
- append `QG-NL-EXP-001` lambda tangent `x^2 exp(x)`: row rank remains `6`;
- parameter null dimension `1`;
- normalized nonlocal coefficient `+1` is compensated by local coefficients `[3.72282e-5,-1.00059168,-0.99612543,-0.51334123,-0.14137283,-0.06615095]`;
- null residual `1.65e-16`.

Thus the nonlocal quadratic variation is exactly locally compensable on this finite six-row sample. The discriminator is the corresponding conditional **full soft2 cubic response**, not the raw nonlocal cubic alone.

## New required comparator data

The local quadratic EFT directions used to compensate `delta K` require their own source-completed soft2 cubic completions through the same frozen dimension-12 order. These were not included in Iterations 177–178 because those iterations intentionally treated `K2=0` curvature-cubic operators.

## Retained results

- `REL-NG-001 — JOINT_K2_SOFT2_HARD_CONDITIONING_IS_INVARIANT_UNDER_INTERNAL_WARD_TRANSVERSE_REPARTITION`;
- `C5-NG-010 — LOCAL_QUADRATIC_EFT_SOFT2_COMPLETIONS_ARE_REQUIRED_WHEN_THEIR_K2_DIRECTIONS_COMPENSATE_NONLOCAL_CALIBRATION`;
- `NL-NG-006 — SIX_ROW_NONLOCAL_K2_TANGENT_HAS_AN_EXACT_LOCAL_POLYNOMIAL_COMPENSATION_DIRECTION_AT_FROZEN_DIMENSION12_RESOLUTION`;
- `NG-FUNNEL-041 — CONDITION_FULL_SOURCE_COMPLETED_SOFT2_ON_CALIBRATED_K2_INSTEAD_OF_PROMOTING_AN_OFFSHELL_W_B_SPLIT`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. Comparator foundation remains `24/25`; robust residual remains `0/20`.

## Exact restart instruction

Resume at **Iteration 184 — local quadratic C5 soft2 completion**.

1. compute the source-completed `O(k_soft^2)` cubic response for `R_mn R^mn` and `R_mn Box^n R^mn` through the frozen dimension-12 order on the same six rows;
2. include the common EH/normalization cubic response consistently if its quadratic direction participates in the hard-calibration null vector;
3. verify the source-completed Ward identity rather than isolated cubic transversality;
4. compute the full `QG-NL-EXP-001` soft2 tangent from the parent action including Frechet variation;
5. form the single K2-preserving conditional nonlocal cubic direction using the Iteration-183 null vector;
6. compare it to the zero-K2 local curvature-cubic span and numerical envelope;
7. only then proceed to AS and C3 closure.

No `ANSATZ-003`, Fisher or resources before full quotient survival.
