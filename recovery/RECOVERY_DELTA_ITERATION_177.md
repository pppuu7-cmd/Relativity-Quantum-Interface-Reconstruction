# Recovery Delta — RQIR Iteration 177

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 176 established that the finite off-shell curvature-cubic columns from Iteration 150 do not determine the Ward-subtracted soft2 `B_T` coefficients and required a new soft-deformed action-level calculation.

## New authority

The first actual local-C5 `B_T` columns are now instantiated from the same covariant parent operators:

- `Tr(Ricci^3)`;
- cyclic `Riemann^3`.

Frozen soft family:

`k1=eps*(1,0,0,1)`, `k2=q_i`, `k3=-q_i-k1`,

with the physical null plus-TT soft polarization from Iteration 175 and six target-independent hard rows inherited from the Iteration-150 q-list.

For these curvature-cubic directions, `K2=0` around Minkowski, so their operator-specific Ward subtraction is `W[K2]=0`. Pure-gauge replacement gives max residue `2.82e-22`.

## Exact protocol zero

For a null TT soft graviton,

`R_mn^(1)=0`.

Therefore `Tr(Ricci^3)` has an exact zero `B_T` column in this protocol. This is not an operator absence and does not revoke the nonzero finite-off-shell Iteration-150 result.

The cyclic `Riemann^3` column is nonzero:

`[-1.6411697072, 0.0638588272, 0.8548821188, -0.1705521567, -0.3261917311, -0.1655609265]`.

Extrapolation stability: max discrepancy `5.27e-6`.

## Rank certificate

`V_C5_B_T` has rank `1/2` with singular values `[1.8950564368,0]`.

Classification: `REGIME_SPECIFIC_NON_IDENTIFIABILITY`.

Retain:

- `C5-NG-008 — NULL_TT_SOFT_PROTOCOL_ANNIHILATES_RICCI_CUBED_B_T_BUT_NOT_CYCLIC_RIEMANN_CUBED`;
- `SOFT-NG-004 — FIRST_ACTION_LEVEL_LOCAL_C5_B_T_BASIS_HAS_RANK_ONE_ON_SIX_NULL_SOFT_TT_ROWS`;
- `NG-FUNNEL-037 — PROTOCOL_ZERO_FROM_ONSHELL_SOFT_RICCI_IS_REGIME_SPECIFIC_NOT_OPERATOR_ABSENCE`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. This closes the first action-level C5 transverse column but does not close the full comparator quotient or create a robust residual.

## Exact restart instruction

Resume at **Iteration 178**.

1. extend the target-independent local-C5 `B_T` operator basis through the already frozen EFT truncation, using action-level soft deformations only;
2. prioritize derivative/curvature-cubic directions that can survive a null TT soft leg;
3. compute rank/SVD before adding any target;
4. then add fixed C4 and `QG-NL-EXP-001` `B_T` columns;
5. C3 ordered and AS real-time transverse columns remain BLOCKED unless explicitly derived;
6. no `ANSATZ-003`, Fisher or resources before a nonzero residual survives the complete fixed comparator quotient.
