# Recovery Delta — RQIR Iteration 176

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 175 froze the next finite relation space as six Ward-subtracted transverse soft coordinates `B_T`, with the Ward-determined longitudinal part projected as shared consistency structure.

## Compatibility result

The existing Iteration-150 local C5 cubic response columns cannot be reused numerically as `B_T` columns.

Iteration 150 uses six finite off-shell momentum triplets `(p,-q,-r)`, `p=q+r`. Iteration 175 requires a soft family `k_soft(epsilon)=epsilon k0`, exact momentum conservation for all epsilon, subtraction of `W[K2]`, transverse projection and extraction of the `epsilon^2` coefficient.

A finite response value does not determine that coefficient.

## Exact analytic non-identifiability

For any analytic reference `f0`,

`f_c(epsilon)=f0(epsilon)+c epsilon^2(1-epsilon)^2`

has identical `f(0)`, `f'(0)` and `f(1)` for all real `c`, while the `epsilon^2` coefficient shifts by `c`.

Thus preserving leading soft, subleading soft and one finite response point still leaves soft2 arbitrary.

## Preserved authority

Iteration 150 remains fully valid in its frozen finite-off-shell scope:

- `Tr(Ricci^3)` and cyclic `Riemann^3` are explicit local C5 columns;
- finite six-probe rank `2/2`;
- singular values `[4.83562189,1.10930485]`;
- `s_min/s_max=0.2294027268`.

Iteration 151 source-completed EH Ward identity remains `PASS_SCOPED`.

No historical result is revoked.

## Current classification

`C5_B_T = BLOCKED_NEW_SOFT_DEFORMED_ACTION_LEVEL_COMPUTATION_REQUIRED`.

Never relabel Iteration-150 finite columns as Iteration-175 soft-transverse columns.

## Retained results

- `C5-NG-007 — FINITE_OFFSHELL_CUBIC_RESPONSE_DOES_NOT_DETERMINE_WARD_SUBTRACTED_SOFT2_COEFFICIENT`;
- `SOFT-NG-003 — PRESERVING_SOFT0_SOFT1_AND_ONE_FINITE_POINT_STILL_LEAVES_SOFT2_FREE`;
- `NG-FUNNEL-036 — TRANSVERSE_SOFT_COMPARATOR_COLUMNS_MUST_BE_RECOMPUTED_FROM_SOFT_DEFORMED_PARENT_ACTION`.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

No robust unique residual or parent dynamics exists.

## Exact restart instruction

Resume at **Iteration 177 — first action-level C5 soft-transverse columns**.

Required order:

1. reuse the covariant parent operators from Iteration 150, not their finite response numbers;
2. freeze six target-independent soft-deformed kinematic families with `k_soft=epsilon k0` and exact momentum conservation;
3. compute the source-completed cubic response as a function of epsilon;
4. subtract `W[K2]`, project `P_T`, and extract the converged epsilon^2 coefficient;
5. form the `Tr(Ricci^3)` and cyclic `Riemann^3` six-row `B_T` columns;
6. compute rank/SVD with no target optimization;
7. only then add further C5/C4/nonlocal transverse directions;
8. preserve C3 ordered and AS real-time columns as BLOCKED unless explicitly derived;
9. no `ANSATZ-003`, Fisher or resources before a nonzero full comparator-subtracted transverse residual.
