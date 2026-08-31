# RQIR Research Log — Iteration 176

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting point

Iteration 175 replaced the scalar Ward pass/fail coordinate by six Ward-subtracted transverse soft coordinates `B_T`, defined at sub-subleading `O(k_soft^2)` order.

The repository already contains two explicit local C5 curvature-cubic finite-response columns from Iteration 150, so the immediate compatibility question is whether those numbers can be reused directly in `B_T`.

## Result

They cannot.

Iteration 150 evaluates six fixed finite off-shell triplets `(p,-q,-r)`, `p=q+r`. Iteration 175 requires a controlled family `k_soft(epsilon)=epsilon k0`, exact momentum conservation for all epsilon, source-completed Ward subtraction and extraction of the `epsilon^2` transverse coefficient.

A finite response value does not determine that Taylor coefficient.

## Analytic certificate

For arbitrary analytic `f0`, define

`f_c(epsilon)=f0(epsilon)+c epsilon^2(1-epsilon)^2`.

All members have identical

- `f(0)`;
- `f'(0)`;
- `f(1)`;

but the `epsilon^2` coefficient changes by `c`.

Toy reference `f0=1.25-0.7 epsilon+2.4 epsilon^2` and `c=[-5,-1,0,2,7.5]` gives common `f(0)=1.25`, `f'(0)=-0.7`, `f(1)=2.95`, while soft2 coefficients range from `-2.6` to `9.9`.

Hence even exact soft0, soft1 and one finite response point do not identify soft2.

## Preserved old authority

Iteration 150 remains valid in its frozen finite-off-shell scope:

- `Tr(Ricci^3)` and cyclic `Riemann^3`;
- rank `2/2`;
- singular values `[4.83562189,1.10930485]`;
- `s_min/smax=0.2294027268`.

Iteration 151 EH source-completed off-shell Ward PASS remains valid.

No old result is revoked; only cross-protocol numeric reuse is forbidden.

## Retained results

- `C5-NG-007 — FINITE_OFFSHELL_CUBIC_RESPONSE_DOES_NOT_DETERMINE_WARD_SUBTRACTED_SOFT2_COEFFICIENT`;
- `SOFT-NG-003 — PRESERVING_SOFT0_SOFT1_AND_ONE_FINITE_POINT_STILL_LEAVES_SOFT2_FREE`;
- `NG-FUNNEL-036 — TRANSVERSE_SOFT_COMPARATOR_COLUMNS_MUST_BE_RECOMPUTED_FROM_SOFT_DEFORMED_PARENT_ACTION`.

## Status

`C5_B_T = BLOCKED_NEW_SOFT_DEFORMED_ACTION_LEVEL_COMPUTATION_REQUIRED`.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next gate

Iteration 177: build the first actual C5 `B_T` columns from soft-deformed versions of the two authoritative curvature-cubic parent actions, with Ward subtraction and controlled `epsilon^2` extraction on six target-independent rows.
