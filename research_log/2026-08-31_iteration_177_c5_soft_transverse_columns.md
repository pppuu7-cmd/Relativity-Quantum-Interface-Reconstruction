# RQIR Research Log — Iteration 177

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting authority

Iteration 176 proved that finite off-shell C5 cubic response numbers cannot be reused as Ward-subtracted soft2 `B_T` coefficients. It required a new action-level soft deformation.

## Computation

Reused the two covariant curvature-cubic parent operators from Iteration 150, not their old numerical columns. Froze six target-independent soft families with

`k1=eps*(1,0,0,1)`, `k2=q_i`, `k3=-q_i-k1`,

where the six `q_i` are the pre-existing Iteration-150 hard momenta and the soft polarization is the physical null plus-TT tensor of Iteration 175.

Because both operators begin at cubic order around Minkowski, their own quadratic kernel is zero and hence the Ward-determined subtraction `W[K2]` is exactly zero. Their cubic vertices are products of linearized curvatures and are separately gauge invariant; the soft pure-gauge replacement leaves a maximum absolute residue `2.82e-22`.

## Result

For a null TT soft graviton, linearized Ricci vanishes exactly. Therefore

`B_T[Tr(Ricci^3)] = 0`

in this protocol. This is a protocol/regime zero only; it does not erase the nonzero finite off-shell Iteration-150 Ricci-cubed column.

The cyclic Riemann-cubed direction survives. Its six extrapolated `eps^2` coefficients are

`[-1.6411697072, 0.0638588272, 0.8548821188, -0.1705521567, -0.3261917311, -0.1655609265]`.

Maximum discrepancy between two independent extrapolants is `5.27e-6`.

Thus the first action-level local-C5 soft-transverse matrix has

`rank = 1/2`, singular values `[1.8950564368, 0]`.

Classification: **regime-specific non-identifiability**, not consistency FAIL, not exact comparator identity, not near-degeneracy.

## Retained results

- `C5-NG-008 — NULL_TT_SOFT_PROTOCOL_ANNIHILATES_RICCI_CUBED_B_T_BUT_NOT_CYCLIC_RIEMANN_CUBED`.
- `SOFT-NG-004 — FIRST_ACTION_LEVEL_LOCAL_C5_B_T_BASIS_HAS_RANK_ONE_ON_SIX_NULL_SOFT_TT_ROWS`.
- `NG-FUNNEL-037 — PROTOCOL_ZERO_FROM_ONSHELL_SOFT_RICCI_IS_REGIME_SPECIFIC_NOT_OPERATOR_ABSENCE`.

## MODEL_READINESS

`MODEL_READINESS: 24%` — unchanged from Iteration 176. Comparator foundation is sharpened and the first physical C5 `B_T` column is now real, but no robust full-quotient residual, parent dynamics, candidate-specific consistency closure, Fisher identifiability, or resource closure exists.

## Next gate

Iteration 178: complete the target-independent local-C5 `B_T` basis through the already frozen EFT truncation as far as action-level soft projections are supported. In particular test derivative/curvature-cubic operators that need not vanish on a null TT soft leg. Compute rank/SVD before adding fixed C4 and `QG-NL-EXP-001` transverse columns. Preserve C3 ordered and AS real-time entries as BLOCKED. No `ANSATZ-003`, Fisher or resources.
