# RQIR Candidate Gravity — Multilinear polarization of the physical cubic `B3`

**Iteration:** 261  
**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Iteration 260 froze the exact same-parent identity

`B(t)=U1(t)W(t)=Q(t)A(t)Q(t)`

and the one-parameter cubic degree decomposition

`B3 = Q0 A3 Q0 + Q1 A2 Q0 + Q0 A2 Q1 + Q2 A1 Q0 + Q0 A1 Q2 + Q1 A1 Q1`.

Before constructing physical tensor coefficients, this iteration audits whether that six-term bookkeeping is already the physical three-leg numerator required by the frozen C5 observable.

## Result: degree bookkeeping is not yet external-leg polarization

The six structures are correct **degree-pattern families** for a one-parameter background. The physical C5 three-point object has three distinguishable perturbations, here denoted `(s,a,b)` with `s` the frozen physical null-TT soft leg. Therefore the cubic coefficient must be the polarized trilinear map.

Write the homogeneous Fréchet/Taylor maps as

- `Q1[x]`,
- symmetric `Q2[x,y]`,
- `A1[x]`,
- symmetric `A2[x,y]`,
- symmetric complete same-parent `A3[x,y,z]`.

Using coefficient convention in which these objects are the coefficients of the corresponding multilinear monomials (equivalently, derivatives with the factorials absorbed consistently), the coefficient of `t_s t_a t_b` in `B=QAQ` is

`B3[s,a,b] =`

1. `Q0 A3[s,a,b] Q0`;
2. for each `x in {s,a,b}`, with `{y,z}` the complementary pair,
   - `Q1[x] A2[y,z] Q0`,
   - `Q0 A2[y,z] Q1[x]`;
3. for each `z in {s,a,b}`, with `{x,y}` the complementary pair,
   - `Q2[x,y] A1[z] Q0`,
   - `Q0 A1[z] Q2[x,y]`;
4. for every ordered allocation of the three distinct legs `(x,y,z)`,
   - `Q1[x] A1[y] Q1[z]`.

Hence the physical polarized cubic assembly contains

`1 + 6 + 6 + 6 = 19`

explicit leg-resolved terms, grouped into the same six one-parameter degree families.

Freeze:

`PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION`

and guardrail

`NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR`.

This is not a change to the Iteration-257/260 algebra; it is the required polarization of that algebra before source projection.

## Null-soft reduction

Iteration 246 proved for the frozen physical null-TT soft leg

`E1[s]=0`.

Since `A=K E` and the flat background obeys `E0=0`, the linear coefficient in a pure soft direction is

`A1[s]=K0 E1[s]=0`.

Therefore exactly four of the 19 polarized terms vanish algebraically:

- `Q2[a,b] A1[s] Q0`;
- `Q0 A1[s] Q2[a,b]`;
- `Q1[a] A1[s] Q1[b]`;
- `Q1[b] A1[s] Q1[a]`.

The surviving physical null-soft assembly has **15 terms**.

Crucially, the following are *not* killed by `E1[s]=0` and must remain:

- `Q1[s] A2[a,b] Q0` and its right-resolvent partner;
- terms containing `A2[s,a]` or `A2[s,b]` because the soft leg may enter kernel/background dressing while the explicit EOM factor belongs to a hard leg;
- `A3[s,a,b]` for the same reason;
- terms such as `Q1[s] A1[a] Q1[b]`.

Thus the null-soft theorem does not zero-fill the `e=1/e=2` connection sector.

## Why this matters

A one-parameter TT calculation can validate local formulas and recursion, but it cannot by itself supply the distinguishable-leg C5 numerator. Using the unpolarized six-term expression directly as the physical three-point numerator would silently omit leg allocations and could generate false cancellations or false normalization.

The next physical construction must therefore use **multilinear coefficients from the start**.

The exact weighted Ward identity of Iteration 260 remains valid after polarization: since `B(g)^T=B(g)` for every background metric in the same-parent domain, every mixed Fréchet derivative, including `B3[s,a,b]`, is symmetric in the weighted ghost-pair orientation. A transpose mismatch remains an implementation/convention regression.

## Classification discipline

This result is:

- not a consistency FAIL;
- not an exact Candidate-vs-GR comparator identity;
- not regime-specific non-identifiability;
- not near-degeneracy;
- not a novelty certificate.

It is an exact bookkeeping correction/closure needed before the physical C5 tensor numerator is constructed.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

## Reproducibility

See

- `candidate_gravity/code/iteration261_vd_multilinear_b3_polarization.py`;
- `candidate_gravity/results/iteration261_vd_multilinear_b3_polarization.json`.

The script enumerates all 19 distinguishable-leg terms and confirms that exactly four contain `A1[s]`, leaving 15 terms after the frozen null-soft condition.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 260: **0 percentage points**. A necessary physical-assembly ambiguity is removed, but the physical C5 comparator coordinate and robust nonzero residual remain open; no readiness-rubric category closes.

## Exact next gate — Iteration 262

Construct the **polarized** same-parent tensors `A1[x]`, `A2[x,y]`, and complete `A3[s,a,b]` (retaining the exact same-parent cubic completion rather than standalone `K1E2`). Build polarized `Q1[x]` and `Q2[x,y]` only from the frozen orbit-metric recursion. Assemble the 15 surviving null-soft terms of `B3[s,a,b]`. Only after a nonzero physical numerator is obtained may tensor reduction begin. Fisher/resources, blind heavy full-C5 integration and `ANSATZ-003` remain forbidden.