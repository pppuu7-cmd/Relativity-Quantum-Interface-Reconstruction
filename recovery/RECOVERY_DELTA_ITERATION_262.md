# RECOVERY DELTA — Candidate Gravity Iteration 262

**Date:** 2026-09-02  
**Authoritative iteration:** 262  
**MODEL_READINESS: 24%**

## Delta from Iteration 261

Iteration 261 established the physical multilinear `B3[s,a,b]` assembly and the 15 surviving null-soft terms. Iteration 262 reduces the independent same-parent vertex library required to construct those terms.

Retain

`B=Q A Q`, `Q=N_orb^{-1}`,

and the exact gauge-identity form

`A_{gamma delta}=-R_gamma^i R_delta^j H_ij`, `H_ij=D_iD_jS`.

In the frozen linear covariant-metric split the diffeomorphism generator is affine, `R=R0+R1[h]`, so `R_n=0` for every `n>=2`.

Multilinear polarization then gives exact finite counts:

- `A1[x]`: 3 subterms;
- `A2[x,y]`: 7 subterms;
- `A3[s,a,b]`: 13 subterms.

The inverse orbit-metric recursion for distinct legs is

`Q1[x]=-Q0N1[x]Q0`,

`Q2[x,y]=Q0N1[x]Q0N1[y]Q0 + Q0N1[y]Q0N1[x]Q0 - Q0N2[x,y]Q0`.

Because the flat Einstein background has `E0=0`, the complete `A0=0`. Hence cubic `B3` never requires `Q3`: every possible degree-three resolvent insertion would multiply `A0`. Therefore `N3/Q3` are outside the required cubic `U1 W` library.

Freeze:

`PASS_SCOPED_POLARIZED_A_MINIMAL_3_7_13_LIBRARY`

`PASS_SCOPED_POLARIZED_Q1_Q2_INVERSE_RECURSION`

`NO_Q3_OR_N3_REQUIRED_FOR_PHYSICAL_U1W_CUBIC_B3`

`NO_TERM_BY_TERM_SOFT_ZERO_INSIDE_A1`.

The remaining independent dynamic inputs for this sector are `N1[x]`, `N2[x,y]`, `R1[x]`, `H1[x]`, `H2[x,y]`, `H3[s,a,b]`, plus frozen background data.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This is not a consistency FAIL, exact Candidate-vs-GR comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 261: **0 percentage points**. The necessary cubic library is now finite and smaller, but physical `H1/H2/H3`, nonzero `B3`, tensor reduction and the complete C5 comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct polarized same-parent covariant-Hessian coefficients `H1[x]`, `H2[x,y]`, `H3[s,a,b]` in frozen `D=4, Lambda=0, a=-1/2`; combine them with frozen `R0/R1` into physical `A1,A2,A3`. Derive `N1[x],N2[x,y]` from the same orbit metric and obtain `Q1,Q2` only through the recursion above. Assemble the 15 surviving null-soft `B3[s,a,b]` terms. Do not start tensor reduction until a nonzero physical numerator exists. Fisher/resources, blind heavy integration and `ANSATZ-003` remain forbidden.
