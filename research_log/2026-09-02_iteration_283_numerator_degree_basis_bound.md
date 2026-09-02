# Research Log — Iteration 283

Authoritative front read from `candidate_gravity/recovery/CURRENT_QG_FRONT.md`: Iteration 282. Latest recovery delta and research log were read, recent commits checked, and GitHub Actions showed no active run; the only recent workflow was completed successfully.

Iteration 283 addressed the next exact prerequisite before canonical-sector p-dependent interpolation/IBP. Using the same frozen parent dynamics and inverse-resolvent recursion, the routed loop-momentum degree of every primitive B3 branch was bounded without fitting or integration.

At flat background `Q0(p)=-eta/p^2` exactly. The frozen same-parent `N1,N2` kernels are at most quadratic in routed `p`, and the physical polarized `A1,A2,A3` kernels are at most quadratic in routed `p`. Therefore `Q1` carries numerator degree <=2; sequential `Q2` carries degree <=4; the `N2` contact part carries degree <=2.

Expanding all 23 translation-closed primitive branches yields the exact family/degree census:

- single squared scaleless: 1 branch, degree <=2;
- null raised bubble: 2 branches, degree <=4;
- bubble-a: 4 branches, degree <=4;
- bubble-b: 4 branches, degree <=4;
- raised triangle: 12 branches, degree <=6.

For scalar orbit-trace reconstruction at fixed external invariants, the Lorentz basis `(l^2)^a prod_i(l.q_i)^b_i` with weighted degree `2a+sum b_i<=d` has ceiling sizes 2 (single), 9 (raised bubble with one external q) and 50 (raised triangle with two independent external q's). These are upper bounds before symmetry/Gram reductions, not claims that all coefficients are nonzero.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_NUMERATOR_DEGREE_AND_FINITE_BASIS_BOUND`.

Guardrail:

`DO_NOT_FIT_CANONICAL_SECTOR_NUMERATORS_WITH_DEGREE_ABOVE_THE_EXACT_2_4_6_BOUNDS_WITHOUT_A_NEW_DYNAMICAL_VERSION`.

Classification: exact power-counting/reconstruction-bound result. It is not consistency FAIL/PASS of a candidate model, exact comparator identity, regime-specific non-identifiability, near-degeneracy or a novelty certificate.

The operational blocker is refined to:

`BLOCKED_CANONICAL_SHIFTED_P_DEPENDENT_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

MODEL_READINESS: 24%

Change from previous recorded estimate: 0 percentage points. Comparator foundation remains 24/25 and robust unique residual remains 0/20. The iteration proves the remaining p-dependent reconstruction is finite and bounded by the frozen dynamics, but it does not yet produce a linked comparator coordinate or comparator-subtracted residual.

Exact next gate: apply the Iteration-282 canonical loop shifts to the actual p-dependent branch numerators; sector-sum after the shifts; reconstruct bubble sectors only in degree<=4 Lorentz bases and triangle sectors only in degree<=6 bases; validate on held-out loop momenta; then perform scoped tensor/IBP reduction. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
