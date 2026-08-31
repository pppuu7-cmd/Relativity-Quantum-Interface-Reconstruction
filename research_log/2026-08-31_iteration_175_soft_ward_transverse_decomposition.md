# RQIR Research Log — Iteration 175

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting point

Iteration 174 proved that the current coarse CTP relation map annihilates a fixed closed-unitary, diffeomorphism-invariant nonlocal tree comparator even though its raw cubic vertex is nontrivial. Therefore `WardLock=0` plus the generic unitary `r/a` relation is too coarse for gravity-family discrimination.

## New protocol principle

Replace the scalar Ward pass/fail coordinate by a tensor soft decomposition of the source-completed amputated cubic vertex:

`Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order`.

Here `W[K2]` is the part fixed by the same quadratic inverse kernel through the 1PI diffeomorphism Ward/covariantization relation. It is shared consistency structure. The `Rlin:B3` term is separately gauge invariant and contains independent three-point/nonminimal information.

## Literature authority

The 1PI soft-graviton analyses of Sen and Laddha–Sen show that universal soft structure is fixed by general covariance while additional theory-dependent three-point information enters through gauge-invariant soft-curvature structures. Local EFT soft-theorem analyses show that the subleading graviton theorem is protected in the frozen setting whereas sub-subleading terms can receive local-operator corrections.

This matches the RQIR rule already established in Iteration 145: `soft0/soft1` are locks; `soft2` belongs to comparator space rather than being an automatic novelty witness.

## Tensor certificate

For null `k=(1,0,0,1)` and pure-gauge polarization `eps=k⊗xi+xi⊗k`, `xi=(0.3,0.7,-0.2,0.4)`:

- `max |Rlin| = 5.55e-17`;
- `||Rlin|| = 1.36e-16`.

For normalized TT plus polarization:

- `max |Rlin| = 0.35355339059327373`;
- `||Rlin|| = 2` to floating-point precision.

Thus the tensor structure is pure-gauge null but physically nonzero.

## Soft-order certificate

Under `k -> a k`, the TT linearized-Riemann norm scales as `a^2`:

- `a=0.5`: ratio `0.25`;
- `a=2`: ratio `4`;
- `a=3`: ratio `9.000000000000002`.

Maximum error: `1.78e-15`.

Therefore the independent transverse/nonminimal form factor enters at sub-subleading `O(k^2)` order.

## Frozen next relation space

For each of the six frozen amputated rows define conceptually

`B_T(i) = P_T [ Gamma_arr(i) - W_i[K2] ]`.

The Ward-determined longitudinal piece is projected as hard shared structure. Six transverse row coordinates remain before comparator subtraction.

This is not a novelty certificate. C5 local EFT, C4 nonlinear mediators, nonlocal gravity and asymptotic-safety vertices can populate the same transverse space.

## Retained results

- `SOFT-NG-001 — WARD_DETERMINED_SOFT_CUBIC_PART_IS_SHARED_STRUCTURE_FIXED_BY_THE_TWO_POINT_KERNEL`;
- `SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER`;
- `NG-FUNNEL-035 — REPLACE_SCALAR_WARDLOCK_WITH_WARD_SUBTRACTED_TRANSVERSE_CUBIC_COORDINATES`.

## Comparator status

- C3 ordered transverse completion: BLOCKED;
- C4 transverse parent projection: required;
- C5 local EFT transverse basis: next priority;
- `QG-NL-EXP-001`: tree `B_T` fixed in principle by the parent action but not yet projected;
- AS real-time/source-completed `B_T`: BLOCKED.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

A physically sharper residual space is now frozen, but no full comparator-subtracted residual exists.

## Next gate

Iteration 176: instantiate a target-independent finite **C5 transverse soft comparator basis** in the six `B_T` rows from local diffeomorphism-invariant EFT operators that can modify sub-subleading soft structure at the declared order. Compute rank/SVD before adding C4/nonlocal columns.
