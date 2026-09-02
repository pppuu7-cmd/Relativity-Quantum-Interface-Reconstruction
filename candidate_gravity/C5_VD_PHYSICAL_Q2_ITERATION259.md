# C5 Vilkovisky physical Q2 — Iteration 259

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Scope

This iteration continues the finite Vilkovisky C5 authority-improvement route from authoritative Iteration 258. It does not create a new Candidate Gravity ansatz and does not alter any frozen comparator gate.

Frozen convention remains `D=4`, `Lambda=0`, DeWitt `a=-1/2`, signature `(-,+,+,+)`, linear covariant-metric split.

Iteration 258 fixed the physical orbit-metric coefficients of

`N_orb(t)=N0+t N1+t^2 N2+...`

from the same-parent factorization `Nhat=W N_orb`. The inverse is

`Q(t)=N_orb(t)^-1=Q0+t Q1+t^2 Q2+...`.

No independent inverse coefficient is allowed.

## Exact inverse recursion

From `N_orb Q = I`, coefficient matching gives

`Q0=N0^-1`,

`Q1=-Q0 N1 Q0`,

and

`Q2=Q0 N1 Q0 N1 Q0-Q0 N2 Q0`.

Iteration 259 evaluates the same finite-amplitude TT background used in Iteration 258, directly forms `Q(t)=N_orb(t)^-1`, extracts its first and second coefficients by centered finite differences, and compares them with the recursion above.

## Reproducible validation

At step `h=1e-4`,

`max|Q1_direct-Q1_recursion| = 3.2350440104522704e-8`,

`max|Q2_direct-Q2_recursion| = 6.316712886089704e-8`,

and

`||Q2_direct||_F = 3.90439593779004`.

The mismatch decreases approximately quadratically across `h=1e-2, 3e-3, 1e-3, 3e-4, 1e-4`, until finite-precision effects become relevant. Thus the physical second-order inverse coefficient is independently validated against direct inversion of the same parent orbit metric.

Freeze:

`PASS_SCOPED_PHYSICAL_Q2_RECURSION_AND_DIRECT_INVERSE_VALIDATION`.

Retain and strengthen the guardrail:

`NO_INDEPENDENT_Q2_ANSATZ`.

## Scientific classification

This is a scoped constructive comparator-authority PASS. It is not:

- a complete C5 comparator coordinate;
- a robust Candidate Gravity residual;
- an exact comparator identity between Candidate Gravity and a comparator;
- regime-specific non-identifiability;
- near-degeneracy;
- a consistency FAIL;
- a novelty certificate.

The umbrella C5 status remains

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

with

`BLOCKED_NOT_ZERO`.

`ANSATZ-003` remains uncreated. Fisher/resources and heavy loop integration remain forbidden.

## Consequence for the cubic weighted numerator

The `Q` side of the six-term cubic weighted object

`B3=[U1 W]_3`

is now fixed through second order by the same physical orbit metric. The unresolved upstream work is the same-parent construction of `A1,A2,A3`, especially

`A3=K0 E3+K1 E2+K2 E1`,

followed by assembly of

`B3=Q0A3Q0+Q1A2Q0+Q0A2Q1+Q2A1Q0+Q0A1Q2+Q1A1Q1`

and the frozen weighted transpose/index/TT certificate before tensor reduction.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 258: **0 percentage points**. A genuine second-order physical inverse-resolvent ingredient is now closed and independently validated, but no full comparator coordinate or robust algebraic residual closes an additional readiness-rubric category.
