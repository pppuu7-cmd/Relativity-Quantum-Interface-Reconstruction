# RQIR Candidate Gravity — Polarized `A`/`Q` minimal vertex library

**Iteration:** 262  
**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Iteration 261 established that the physical cubic `B3[s,a,b]` must be multilinearly polarized and that 15 terms survive the frozen null-soft condition. The next task is to identify the smallest same-parent tensor library required to construct those terms without introducing independent resolvent or generator ansatz freedom.

Retain the frozen definitions

`B = U1 W = Q A Q`,

`Q = N_orb^{-1}`,

and the exact same-parent identity

`A_{gamma delta} = R_gamma^i (D_i R_delta^j) E_j = - R_gamma^i R_delta^j H_ij`,

where `H_ij := D_i E_j = D_i D_j S` is the torsion-free covariant Hessian of the same Einstein parent action.

The linear covariant-metric split from Iteration 254 gives an affine diffeomorphism generator,

`R[g] = R0 + R1[h]`,

so every higher generator variation vanishes:

`R_n = 0` for `n >= 2`.

## Exact polarized `A` coefficients

Use distinguishable perturbations `x,y,z` and denote the two gauge-generator factors by `Rg` and `Rd` for the two ghost-pair indices `(gamma,delta)`. With multilinear coefficient convention fixed in Iteration 261:

### Linear

`A1[x] = -(`

- `Rg1[x] Rd0 H0`
- `Rg0 Rd1[x] H0`
- `Rg0 Rd0 H1[x]`

`)`.

Thus `A1[x]` contains exactly **3** leg-resolved subterms.

### Quadratic

For distinct `x,y`,

`A2[x,y] = -(`

- `Rg0 Rd0 H2[x,y]`
- `Rg1[x] Rd0 H1[y]`
- `Rg1[y] Rd0 H1[x]`
- `Rg0 Rd1[x] H1[y]`
- `Rg0 Rd1[y] H1[x]`
- `Rg1[x] Rd1[y] H0`
- `Rg1[y] Rd1[x] H0`

`)`.

Thus `A2[x,y]` contains exactly **7** subterms.

### Cubic

For the physical legs `(s,a,b)`,

`A3[s,a,b]` contains exactly **13** subterms:

1. one `Rg0 Rd0 H3[s,a,b]` term;
2. six one-generator-dressing terms: for each choice of one leg on `Rg1` or `Rd1`, `H2` carries the complementary pair;
3. six two-generator-dressing terms: ordered assignments of two distinct legs to `Rg1` and `Rd1`, with `H1` carrying the remaining leg.

There is no `R2`, `R3`, or three-`R1` contribution because there are only two generator factors and the generator is affine.

Freeze:

`PASS_SCOPED_POLARIZED_A_MINIMAL_3_7_13_LIBRARY`.

## Exact polarized inverse recursion

Let

`N_orb = N0 + sum_x t_x N1[x] + sum_{x<y} t_x t_y N2[x,y] + ...`,

`Q = N_orb^{-1}`.

Coefficient matching in `N_orb Q = I` gives

`Q1[x] = - Q0 N1[x] Q0`,

and for distinct `x,y`,

`Q2[x,y] = Q0 N1[x] Q0 N1[y] Q0 + Q0 N1[y] Q0 N1[x] Q0 - Q0 N2[x,y] Q0`.

Therefore the physical cubic assembly introduces no independent polarized resolvent parameter.

Freeze:

`PASS_SCOPED_POLARIZED_Q1_Q2_INVERSE_RECURSION`.

## Why `Q3` is not required

The flat Einstein background obeys `E0=0`, hence from `A=R(DR)E` equivalently from the gauge identity above,

`A0=0`.

The coefficient of total degree three in `B=Q A Q` can therefore contain at most degree two from either resolvent factor. Any term involving `Q3` would have to multiply `A0` and vanishes identically.

Thus:

`NO_Q3_OR_N3_REQUIRED_FOR_PHYSICAL_U1W_CUBIC_B3`.

This is an exact truncation statement for this cubic `U1 W` sector, not a numerical approximation and not an ansatz choice.

## Minimal physical library after Iteration 262

Before tensor reduction, the complete polarized `U1 W` cubic numerator requires only:

- orbit-metric coefficients `N1[x]` and `N2[x,y]`, from which `Q1,Q2` follow exactly;
- affine generator coefficient `R1[x]` already structurally frozen by Iteration 254;
- same-parent covariant-Hessian coefficients `H1[x]`, `H2[x,y]`, `H3[s,a,b]`;
- the already frozen `Q0,R0,H0` background data.

No `R2/R3`, `N3/Q3`, or independent resolvent ansatz is allowed or needed for this sector.

## Null-soft guardrail

Iteration 246 plus `A=K E` implies the **complete sum** `A1[s]=0` for the frozen physical null-TT soft leg. In the `-RRH` representation this is a cancellation/identity among the three `A1[s]` subterms; it does not authorize setting `H1[s]`, `R1[s]`, or individual subterms to zero.

Freeze guardrail:

`NO_TERM_BY_TERM_SOFT_ZERO_INSIDE_A1`.

Likewise, no additional `A2[s,a]`, `A2[s,b]`, or `A3[s,a,b]` terms are dropped without a separate same-parent proof.

## Classification

This iteration is an exact algebraic reduction of the physical C5 numerator library. It is not a consistency FAIL, not an exact Candidate-vs-GR comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy full-C5 integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 261: **0 percentage points**. The minimal physical vertex library is now finite and sharper, but the actual `H1/H2/H3` tensor coefficients, physical nonzero `B3`, tensor reduction and comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate — Iteration 263

Construct same-parent polarized covariant-Hessian coefficients `H1[x]`, `H2[x,y]`, `H3[s,a,b]` in the frozen `D=4, Lambda=0, a=-1/2` convention and combine them with the already frozen `R0/R1` to produce physical `A1,A2,A3`. In parallel derive polarized `N1[x],N2[x,y]` from the same orbit metric and obtain `Q1,Q2` only through the recursion above. Then assemble the 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical numerator exists.