# C5 numerator degree and finite reconstruction basis — Iteration 283

## Scope
This iteration does not perform a loop integral, source projection, comparator subtraction or fit to scalar master shapes. It closes an exact prerequisite for the p-dependent canonical-sector reconstruction.

## Frozen same-parent facts
On the flat Einstein background, the orbit resolvent obeys `Q0(p)=-eta/p^2`. From the frozen Iteration-270 dynamics, `N1` and `N2` are at most quadratic in the routed loop momentum, and every polarized `A1/A2/A3` coefficient is at most quadratic in the routed loop momentum. Exact inverse recursion then implies `Q1` has numerator degree <=2, the sequential part of `Q2` degree <=4, and the `N2` contact part degree <=2.

Expanding the 23 translation-closed primitive B3 branches therefore gives an exact family census:

- single squared scaleless branch: numerator degree <=2 (1 branch);
- null raised bubble: degree <=4 (2 branches);
- bubble-a: degree <=4 (4 branches);
- bubble-b: degree <=4 (4 branches);
- raised triangle: degree <=6 (12 branches).

No primitive branch requires loop-momentum numerator degree above six.

For the scalar orbit trace at fixed external invariants, a Lorentz-covariant monomial basis can be bounded before interpolation. Using `(l^2)^a prod_i(l.q_i)^b_i` with weighted degree `2a+sum b_i<=d` gives:

- degree-2/no external-q single sector: 2 monomials;
- degree-4 raised bubble with one independent external momentum: 9 monomials;
- degree-6 raised triangle with two independent external momenta: 50 monomials.

These are basis-size ceilings for the scalar trace before symmetry/Gram reductions; they are not claims that every coefficient is nonzero.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_NUMERATOR_DEGREE_AND_FINITE_BASIS_BOUND`.

Guardrail:

`DO_NOT_FIT_CANONICAL_SECTOR_NUMERATORS_WITH_DEGREE_ABOVE_THE_EXACT_2_4_6_BOUNDS_WITHOUT_A_NEW_DYNAMICAL_VERSION`.

## Classification
Exact power-counting/reconstruction-bound result. It is not a consistency PASS/FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy or novelty certificate.

## Consequence
The Iteration-282 blocker is narrowed: the remaining reconstruction is finite and has a certified maximum polynomial degree. Overcomplete unconstrained interpolation is forbidden because it would introduce coefficients unsupported by the frozen parent dynamics.

## Next gate
Apply the Iteration-282 loop shifts to the actual p-dependent branch numerators, sector-sum after the shift, reconstruct bubble sectors only in degree <=4 Lorentz bases and triangle sectors only in degree <=6 bases, validate on held-out loop momenta, and only then tensor/IBP reduce the canonical sums.
