# RECOVERY DELTA — Candidate Gravity Iteration 257

**Date:** 2026-09-02  
**Authoritative iteration:** 257  
**MODEL_READINESS: 24%**

## Delta from Iteration 256

Iteration 256 froze the correct weighted cubic Ward object

`B3=[U1 W]_3 = Q0A3Q0 + Q1A2Q0 + Q0A2Q1 + Q2A1Q0 + Q0A1Q2 + Q1A1Q1`,

with `Q=N_orb^-1` and `A3=K0E3+K1E2+K2E1`.

Iteration 257 proves that the inverse coefficients are not independent. For

`N=N0+tN1+t^2N2+...`, `Q=Q0+tQ1+t^2Q2+...`, `NQ=I`,

we have exactly

`Q0=N0^-1`,

`Q1=-Q0N1Q0`,

`Q2=Q0N1Q0N1Q0-Q0N2Q0`.

Because the orbit metric coefficients are symmetric, these `Qn` are symmetric. Therefore the cubic Ward test decomposes pairwise:

- `Q0A3Q0` symmetric;
- `(Q1A2Q0)^T=Q0A2Q1`;
- `(Q2A1Q0)^T=Q0A1Q2`;
- `Q1A1Q1` symmetric,

provided the complete same-parent `A1,A2,A3` are symmetric.

Freeze:

`PASS_SCOPED_CUBIC_WEIGHTED_WARD_PAIRWISE_REDUCTION`

and guardrail:

`NO_INDEPENDENT_Q2_RESOLVENT_ANSATZ`.

A deterministic certificate gives inverse-series error `5.55e-17`, pair residuals `2.17e-19` and `6.78e-20`, and total `B3` symmetry residual `8.67e-19`.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or a novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 256: **0 percentage points**. The upstream cubic assembly is more constrained and one false independent branch is eliminated, but no physical comparator coordinate or robust residual closes a rubric block. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct the physical same-parent second-order orbit-metric coefficient `N2` in the frozen `D=4, Lambda=0, a=-1/2` convention and derive `Q2` only from the recursion above. Finish `A1,A2,A3`, with `A3=K0E3+K1E2+K2E1`, then apply the pairwise weighted-Ward certificate before tensor reduction. Do not create a separate `Q2` ansatz. Do not launch heavy integration, Fisher/resources, or `ANSATZ-003`.
