# Candidate Gravity C5 — polarized K primitive library, Iteration 265

**Date:** 2026-09-02  
**Scope:** finite Vilkovisky C5 authority improvement  
**MODEL_READINESS: 24%**

## Starting point

Iteration 264 certified nonzero polarized Einstein EOM vertices `E2` and `E3` on the frozen null-soft/hard/hard TT family. Iteration 263 had already fixed the projected same-parent route

`A = K E`,  with  `K = R (D R)`,

and

`D R = P + Gamma R`,

where `P=partial R` is background-independent in the frozen linear covariant-metric split, `R=R0+R1[h]` is affine, and `Gamma` is the configuration-space Christoffel of the frozen DeWitt metric with `a=-1/2`.

## Exact polarized expansion

For one background leg `x`,

`D0 = P + Gamma0 R0`,

`D1[x] = Gamma1[x] R0 + Gamma0 R1[x]`,

and for two distinct legs `x,y`,

`D2[x,y] = Gamma2[x,y] R0 + Gamma1[x] R1[y] + Gamma1[y] R1[x]`.

Multiplying by the left generator `R=R0+R1` gives

`K0 = R0 P + R0 Gamma0 R0`.

Thus `K0` has exactly **2 primitive contractions**.

For each leg `x`,

`K1[x] = R1[x] P + R1[x] Gamma0 R0 + R0 Gamma1[x] R0 + R0 Gamma0 R1[x]`.

Thus `K1[x]` has exactly **4 primitive contractions**.

For distinct legs `x,y`,

`K2[x,y] = R1[x] Gamma1[y] R0 + R1[x] Gamma0 R1[y]`

`          + R1[y] Gamma1[x] R0 + R1[y] Gamma0 R1[x]`

`          + R0 Gamma2[x,y] R0 + R0 Gamma1[x] R1[y] + R0 Gamma1[y] R1[x]`.

Thus `K2[x,y]` has exactly **7 primitive contractions**.

No `R2`, `R3`, or `Gamma3` enters this projected cubic route.

Freeze:

`PASS_EXACT_POLARIZED_K0_K1_K2_PRIMITIVE_LIBRARY_2_4_7`

and guardrail:

`NO_R2_R3_GAMMA3_IN_PHYSICAL_PROJECTED_A3`.

## Null-soft projected A library

With the frozen null-soft condition `E1[s]=0`, the projected cubic coefficient is

`A3[s,a,b] = K0 E3[s,a,b]`

`            + K1[s] E2[a,b] + K1[a] E2[s,b] + K1[b] E2[s,a]`

`            + K2[s,a] E1[b] + K2[s,b] E1[a]`.

Substituting the exact primitive counts gives

`2 + 3*4 + 2*7 = 28`.

Therefore physical projected `A3[s,a,b]` requires exactly **28 primitive K/E contractions before any further index, TT, momentum, or source-projection cancellations**.

Likewise:

- `A1[s]`: 2 primitives before the complete `E1[s]=0` zero, hence 0 after the frozen soft equation;
- `A2[s,a]`: `2+4=6` primitives;
- `A2[a,b]`: `2+4+4=10` primitives.

Freeze:

`PASS_EXACT_NULLSOFT_PROJECTED_A3_PRIMITIVE_COUNT_28`.

This is a finite-library closure result. It is not a statement that all 28 terms are nonzero individually, not a complete physical C5 numerator, and not a comparator residual.

## Independent implementation regression

A noncommuting-matrix realization of

`K(t_x,t_y)=R(t_x,t_y) [P + Gamma(t_x,t_y) R(t_x,t_y)]`

was differentiated numerically and compared with the analytic `K1[x]` and `K2[x,y]` expressions. Centered finite differences converge quadratically. At `h=1e-4`,

`max|K1_fd-K1| = 2.6320710944e-7`,

`max|K2_fd-K2| = 2.3047781283e-7`.

The finite-difference test is only a regression check; the 2/4/7 formulas and 28-count follow algebraically from the frozen affine-R dynamics.

## Scientific interpretation

This closes the `K` bookkeeping ambiguity that remained after Iteration 264. The remaining physical work is no longer to decide which `K` vertices exist, but to instantiate their condensed-index/Fourier kernels using the already frozen `R0/R1` and `Gamma0/Gamma1/Gamma2`, contract them with certified `E1/E2/E3`, and then combine with same-parent `Q1/Q2` dressing.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

This is operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

No robust Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources and blind heavy full-C5 integration remain forbidden.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 264: **0 percentage points**. A genuine C5 numerator-building sub-block is now exactly finite and frozen, but comparator foundation remains `24/25` and unique residual remains `0/20`; the physical contracted `A/B3` numerator and comparator coordinate are still open.
