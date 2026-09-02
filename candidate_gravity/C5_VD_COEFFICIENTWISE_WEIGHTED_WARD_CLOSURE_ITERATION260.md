# RQIR Candidate Gravity — Iteration 260

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Iteration 259 closed the physical inverse-orbit coefficients through `Q2` and left the next gate as construction of physical `A1,A2,A3`, assembly of the six cubic terms in `B3=[U1 W]_3`, and a weighted pairwise Ward/transpose certificate. Before spending effort on a component-level TT Ward test, this iteration checks whether that transpose condition is actually an independent scientific gate or follows identically from the already frozen same-parent geometry.

## Frozen definitions

Retain the Iteration-256 weighted factorization

`B(t) := U1(t) W(t) = Q(t) A(t) Q(t)`,

with

`Q(t)=N_orb(t)^-1`,

`A_{gamma delta}(t)=R^i_gamma (D_i R^j_delta) E_j`.

Iteration 253 established the exact same-parent identity

`A_{gamma delta} = - R^i_gamma R^j_delta D_i E_j`.

Because `D_i E_j=D_i D_j S` is the torsion-free covariant Hessian of the scalar parent action, the complete `A(t)` is symmetric in the two gauge/orbit indices for every background amplitude `t`:

`A(t)^T=A(t)`.

The physical orbit metric is symmetric for every `t`, hence

`N_orb(t)^T=N_orb(t)`

and therefore wherever the inverse exists

`Q(t)^T=Q(t)`.

## Exact all-orders consequence

Transpose the weighted object:

`B(t)^T = [Q(t) A(t) Q(t)]^T`

`= Q(t)^T A(t)^T Q(t)^T`

`= Q(t) A(t) Q(t)`

`= B(t)`.

Thus

`B(t)^T=B(t)`

is an exact same-parent identity, not merely a numerical property of one TT channel.

If the background family is expanded formally,

`B(t)=sum_{n>=0} t^n B_n`,

then equality of formal power series gives coefficientwise

`B_n^T=B_n`

for every `n`. In particular

`B3^T=B3`.

The same argument separately implies coefficientwise `Q_n^T=Q_n` and `A_n^T=A_n` because the full functions `Q(t)` and `A(t)` are symmetric for all `t`.

## Cubic organization

Retain exactly

`A3=K0E3+K1E2+K2E1`.

With

`Q=Q0+tQ1+t^2Q2+...`,

`A=tA1+t^2A2+t^3A3+...`,

the cubic coefficient remains

`B3 = Q0 A3 Q0`
`   + Q1 A2 Q0 + Q0 A2 Q1`
`   + Q2 A1 Q0 + Q0 A1 Q2`
`   + Q1 A1 Q1`.

Iteration 257 showed the explicit pairwise transpose organization. The present iteration strengthens that result: the final weighted-transpose Ward property of this `U1 W` sector is theorem-level once the same-parent symmetric `N_orb` and complete same-parent `A` are used. A component TT transpose test can still be retained as an implementation regression test, but it is not an independent scientific PASS/FAIL gate.

## Reproducible regression certificate

`candidate_gravity/code/iteration260_vd_weighted_ward_coefficientwise.py` constructs seeded random symmetric `N0,N1,N2,A1,A2,A3`, obtains `Q0,Q1,Q2` only from the exact inverse recursion, assembles the six cubic terms, and checks the transpose pairs.

The stored result gives

- `max|Q0-Q0^T| = 6.938893903907228e-18`,
- `max|Q1-Q1^T| = 6.938893903907228e-18`,
- `max|Q2-Q2^T| = 1.0408340855860843e-17`,
- first transpose-pair residual `2.8189256484623115e-18`,
- second transpose-pair residual `3.550762114890027e-18`,
- `max|B3-B3^T| = 1.0408340855860843e-17`.

This numerical calculation is only a reproducible implementation certificate for the exact algebra above; it is not the physical tensor numerator calculation.

## Scientific classification

Freeze

`PASS_EXACT_U1W_COEFFICIENTWISE_WEIGHTED_WARD_IDENTITY`.

Freeze guardrail

`NO_INDEPENDENT_TT_TRANSPOSE_GATE_FOR_COMPLETE_U1W_COEFFICIENTS`.

Meaning: a TT/component transpose mismatch in a future implementation is an implementation/convention inconsistency to debug, not evidence that the same-parent Vilkovisky `U1 W` sector physically violates its Ward identity. It must not be promoted to a Candidate Gravity consistency FAIL.

This result is **not** an exact comparator identity between Candidate Gravity and GR, not a complete C5 Ward/positivity/causality closure, not a unique residual, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

## Consequence for the C5 blocker

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

The blocker is narrowed: the weighted-transpose Ward condition for the complete `U1 W` coefficient is no longer an independent unknown. The remaining hard work is to compute the **values** of the physical same-parent `A1,A2,A3` (with `A3=K0E3+K1E2+K2E1`), assemble the physical `B3`, and then perform the still-open tensor reduction, source/contact completion, Lorentzian continuation/discontinuity, and comparator projection.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 259: **0 percentage points**. A real consistency sub-gate has been analytically removed as an independent uncertainty, but the rubric awards consistency/positivity/Ward/causality only when the relevant physical comparator gates close; the physical C5 coordinate and robust residual remain absent. Comparator foundation remains `24/25`, unique residual `0/20`.

## Exact next gate — Iteration 261

Do not spend a scientific iteration merely re-testing weighted transpose symmetry. Instead construct the physical same-parent `A1,A2,A3`, preserving exactly `A3=K0E3+K1E2+K2E1`. Use the exact identity `A=-R R (D E)` as an independent derivation/cross-check against the direct `R.(D R).E` construction where this reduces component work. Then assemble the physical six-term `B3` with the already frozen `Q0,Q1,Q2`. Any transpose mismatch is a regression/debug failure, not a new physical Ward FAIL. Only after a nonzero physical numerator exists may tensor reduction proceed; Fisher/resources and `ANSATZ-003` remain forbidden.
