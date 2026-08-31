# Candidate Gravity — Iteration 182: executable Ward-subtraction gap before nonlocal B_T

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** definition-level blocker exposed; nonlocal `B_T` remains BLOCKED, not zero

## Objective

Iteration 181 showed that representative analytic exponential form-factor shapes are numerically near-degenerate with the local-C5 rank-4 span on the current six `B_T` rows. The planned next step was a full tensor cubic projection of `QG-NL-EXP-001`.

Before performing that expensive calculation, Iteration 182 audits whether the repository currently defines the required Ward-subtracted observable strongly enough to turn a raw cubic tensor into a unique `B_T` column.

## Frozen conceptual definition

Iteration 175 introduced

\[
\Gamma^{(3)}_{\rm soft}=\mathcal W[K^{(2)}]+R^{(1)}_{\rm soft}:B^{(3)}+\cdots
\]

and conceptually

\[
B_T=P_T[\Gamma^{(3)}_{arr}-\mathcal W[K^{(2)}]].
\]

The Iteration-175 implementation validates the soft linearized-Riemann geometry, gauge invariance and `k_soft^2` scaling, but it does **not** contain an executable source-completed map for `W[K2]` or an explicit numerical tensor projector `P_T`.

## Why Iterations 177–178 were still valid

The local curvature-cubic operators used there begin at `O(h^3)` about Minkowski. Their operator-specific quadratic kernel is exactly zero:

\[
K^{(2)}_{R^3}=0.
\]

Therefore their operator-specific Ward/covariantization subtraction is exactly

\[
\mathcal W[K^{(2)}_{R^3}]=0.
\]

The action-level soft coefficients computed in Iterations 177–178 are therefore genuine transverse operator columns without needing an additional subtraction convention.

## Why QG-NL-EXP-001 is different

For the fixed nonlocal comparator,

\[
K^{(2)}_{\rm NL}\neq0.
\]

Its raw cubic action contains both the nonlinear completion required by covariance of this same quadratic kernel and genuinely independent transverse/nonminimal information. A raw tensor calculation alone does not say which part belongs to the shared `W[K2]` structure.

There is an exact decomposition ambiguity. For any transverse Riemann-symmetry tensor/function `C`,

\[
\mathcal W\to\mathcal W+R^{(1)}:C,
\qquad
B\to B-C,
\]

leaves the full cubic vertex unchanged.

Because `R^(1)` vanishes for a pure-gauge soft polarization, ordinary Ward/gauge checks also cannot fix this transverse shift by themselves.

## Finite certificate

Using the same null soft momentum and plus-TT polarization geometry as Iteration 175:

- pure-gauge soft Riemann norm: `1.5700924587e-16`;
- physical TT soft Riemann norm: `2.0` to floating-point precision;
- deterministic physical transverse contraction: `-1.0411732533`;
- pure-gauge contraction: `0.0`.

A nonzero six-row decomposition shift with norm

`0.2455605832`

changes the split between `W` and `B` but leaves the raw cubic vertex unchanged to

`5.5511151231e-17`.

This demonstrates the ambiguity at machine precision.

## Retained results

### SOFT-NG-008 — TRANSVERSE_RIEMANN_SHIFT_IS_INVISIBLE_TO_WARD_CONSTRAINTS_UNTIL_W_K2_CONVENTION_IS_FIXED

Gauge/Ward consistency alone does not determine the transverse separation between the covariantization part of a nonzero quadratic kernel and the independent soft-Riemann form factor.

### NL-NG-005 — FULL_NONLOCAL_RAW_CUBIC_IS_NECESSARY_BUT_NOT_SUFFICIENT_FOR_B_T_WHEN_K2_IS_NONZERO

A full action-level nonlocal cubic calculation is still required, including the Frechet insertion, but cannot be promoted to an RQIR `B_T` comparator column until the source-completed Ward subtraction is executable.

### NG-FUNNEL-040 — EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_MUST_PRECEDE_NONLOCAL_OR_AS_B_T_RANK_PROMOTION

Any comparator with nonzero `K2` must use the same explicit off-shell/source-completed `W[K2]` and transverse projection convention before rank/SVD comparisons.

## Scientific classification

`QG-NL-EXP-001 B_T = BLOCKED_EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_NOT_YET_FROZEN`.

This is:

- not a consistency FAIL;
- not a zero nonlocal column;
- not exact identity with C5;
- not a novelty certificate.

It prevents a convention-dependent raw soft coefficient from being mistaken for a physical fifth comparator direction.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

The comparator foundation cannot receive its final point until a common executable relation map exists for nonzero-`K2` comparators and the remaining C3/nonlocal/AS boundaries can be placed in one actual quotient.

## Exact next gate — Iteration 183

Freeze an **executable source-completed off-shell Ward projector** in the physical metric/source convention.

Required:

1. derive `W[K2]` for one soft graviton and two off-shell conserved-TT hard source legs from the same quadratic inverse kernel and source coupling;
2. specify the tensor complement/projector `P_T` at `O(k_soft^2)` on the six frozen rows;
3. show the decomposition is invariant under allowed field/source bookkeeping and reproduces the exact source-completed Ward identity;
4. test it first on EH / local operators with known limits;
5. only then evaluate the full `QG-NL-EXP-001` cubic action including `delta F(Box)` and compute its physical `B_T` column;
6. reuse the same projector for asymptotic-safety completion.

No `ANSATZ-003`, Fisher or resource calculation before full comparator-quotient survival.
