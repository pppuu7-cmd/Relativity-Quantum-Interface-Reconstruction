# RECOVERY DELTA — Candidate Gravity Iteration 263

**Date:** 2026-09-02  
**Authoritative iteration:** 263  
**MODEL_READINESS: 24%**

## Delta from Iteration 262

Iteration 262 identified full `H1/H2/H3` as an apparent remaining same-parent library for `A=-RRH`. Iteration 263 proves that the physical cubic numerator should instead be constructed by the exactly equivalent projected identity

`A = K E`, `K=R(DR)`,

before expanding the covariant Hessian.

Because flat Einstein `E0=0`,

`A1[x]=K0E1[x]`,

`A2[x,y]=K0E2[x,y]+K1[x]E1[y]+K1[y]E1[x]`,

and generic polarized `A3` contains `K0E3`, three `K1E2`, and three `K2E1` partitions. For the frozen null-soft leg `E1[s]=0`, the `K2[a,b]E1[s]` partition vanishes and `A3[s,a,b]` has six surviving projected terms.

This removes the need to build full unprojected `H3`: direct `H3=D D S` would expose fifth action variation `S5`, while the projected route reaches only `E3` (fourth action variation) plus `K2`. The `-RRH` representation is retained only as an independent regression/cross-check route.

The affine generator and `D R=P+Gamma R` imply that `K0,K1,K2` need only `Gamma0,Gamma1,Gamma2`, `R0,R1`, and the background-independent `P=partial R`. No `Gamma3`, `R2`, or `R3` is required.

The second polarized DeWitt field-space Christoffel `Gamma2[x,y]` was explicitly constructed as the mixed derivative of the same frozen `Gamma(g)` and independently checked against the direct 10-dimensional field-space metric Christoffel. The maximum mismatch is `9.4322526123e-08` on a component scale `0.500008028696`, with zero tested symmetry residuals.

Freeze:

`PASS_EXACT_PROJECT_BEFORE_EXPAND_A_EQUALS_K_E_CUBIC_REDUCTION`

`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_SECOND_POLARIZED_VARIATION`

`NO_FULL_UNPROJECTED_H3_OR_S5_REQUIRED_FOR_PHYSICAL_U1W_B3`

`NO_INDEPENDENT_GAMMA2_ANSATZ`.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 262: **0 percentage points**. The primary numerator route is materially shorter and `Gamma2` is closed, but `E2/E3`, nonzero physical `B3`, tensor reduction and the final C5 comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct polarized Einstein EOM coefficients `E2[x,y]` and `E3[s,a,b]` in the same frozen convention. Build `K0,K1,K2` from `R0/R1`, `P=partial R`, and frozen `Gamma0/Gamma1/Gamma2`, then projected `A1,A2,A3`. Derive physical `N1,N2` from the same orbit metric and obtain `Q1,Q2` only by exact recursion. Assemble the 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical numerator exists; Fisher/resources, blind heavy integration, and `ANSATZ-003` remain forbidden.