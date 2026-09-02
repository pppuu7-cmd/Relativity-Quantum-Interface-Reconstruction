# RQIR Candidate Gravity — Iteration 257

## Exact inverse-resolvent recursion and pairwise cubic weighted Ward reduction

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Starting authority

Repository source of truth is Iteration 256. The exact frozen factorization is

`U1 W = Q A Q`,

with `Q=N_orb^-1`, `A=R.(D R).E`, and the cubic coefficient

`B3=[U1 W]_3 = Q0A3Q0 + Q1A2Q0 + Q0A2Q1 + Q2A1Q0 + Q0A1Q2 + Q1A1Q1`,

where `A3=K0E3+K1E2+K2E1`.

The correct Ward object is weighted; ordinary `U1=U1^T` is not a valid FAIL criterion.

## Exact inverse recursion

Write the symmetric orbit metric and its inverse as

`N(t)=N0+t N1+t^2 N2+O(t^3)`,

`Q(t)=Q0+t Q1+t^2 Q2+O(t^3)`,

with `N(t)Q(t)=I`. Matching powers of `t` gives

`Q0=N0^-1`,

`Q1=-Q0 N1 Q0`,

`Q2=Q0 N1 Q0 N1 Q0-Q0 N2 Q0`.

Thus `Q1` and `Q2` are not independent vertices. Once `N0,N1,N2` are frozen in the same orbit-metric convention, the inverse-resolvent coefficients are fixed algebraically. In particular, because every `Nn` is symmetric, every displayed `Qn` is symmetric.

This removes an avoidable branch of the numerator library: do not derive a separate second-order inverse-resolvent ansatz.

## Pairwise reduction of the cubic weighted Ward test

Assume the same-parent Ward kernel coefficients satisfy

`A1=A1^T`, `A2=A2^T`, `A3=A3^T`.

Then the six cubic terms organize into four symmetry units:

1. `T1=Q0 A3 Q0`, individually symmetric;
2. `T2=Q1 A2 Q0` and `T3=Q0 A2 Q1`, with `T2^T=T3`;
3. `T4=Q2 A1 Q0` and `T5=Q0 A1 Q2`, with `T4^T=T5`;
4. `T6=Q1 A1 Q1`, individually symmetric.

Therefore

`B3=B3^T`

follows algebraically from order-by-order symmetry of `N0,N1,N2` and `A1,A2,A3`. No unexplained cancellation across all six terms is required.

This is scientifically useful because a future weighted-Ward mismatch can now be localized upstream: it must arise from a broken same-parent orbit-metric coefficient, a broken complete `A_n` coefficient, or an index/convention error. It must not be repaired by tuning cross-term coefficients.

Freeze:

`PASS_SCOPED_CUBIC_WEIGHTED_WARD_PAIRWISE_REDUCTION`

and guardrail:

`NO_INDEPENDENT_Q2_RESOLVENT_ANSATZ`.

## Reproducible certificate

`candidate_gravity/code/iteration257_vd_u1_cubic_inverse_recursion.py` uses deterministic symmetric matrices and independently checks the inverse expansion and pairwise transpose relations. Stored result:

- inverse-series error at `eps=1e-5`: `5.55e-17`;
- symmetry residual `Q1`: `3.47e-18`;
- symmetry residual `Q2`: `5.42e-19`;
- `T2^T-T3` residual: `2.17e-19`;
- `T4^T-T5` residual: `6.78e-20`;
- total `B3-B3^T` residual: `8.67e-19`.

The matrix realization is only an algebraic certificate of the exact recursion/pairing identities, not a substitute for the physical 4D tensor numerator.

## Scientific classification

This is a scoped exact algebraic PASS and false-branch elimination result. It is not a physical C5 comparator coordinate, not an exact comparator identity to a competing model, not a Candidate Gravity residual, not near-degeneracy, not regime-specific non-identifiability, and not a consistency FAIL.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

with

`BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 256: **0 percentage points**. The cubic Ward gate is now factored into local upstream symmetry checks and the inverse-resolvent branch is reduced, but no physical comparator coordinate or robust residual closes a readiness-rubric block. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate — Iteration 258

Construct the physical same-parent orbit-metric coefficient `N2` in the frozen `D=4, Lambda=0, a=-1/2` convention and obtain `Q2` only through the exact recursion above. In parallel finish the complete `A1,A2,A3` coefficients, with `A3=K0E3+K1E2+K2E1`. Apply the pairwise weighted-Ward certificate before tensor reduction. Do not create a separate `Q2` ansatz, do not launch heavy integration, and do not create `ANSATZ-003` or run Fisher/resources.
