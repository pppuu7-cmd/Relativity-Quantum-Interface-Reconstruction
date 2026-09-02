# Research Log — Iteration 282

Authoritative front read from `candidate_gravity/recovery/CURRENT_QG_FRONT.md`: Iteration 281. Latest recovery delta and research log were read, recent commits checked, and GitHub Actions showed no active run (the only recent workflow was already completed successfully).

Iteration 282 addressed an exact prerequisite to the p-dependent tensor/IBP step. The 23 translation-closed primitive B3 branches were re-enumerated with routed Q0 denominator multiplicities, keeping the frozen kinematics and topology.

Exact result:

- 1 branch has multiplicity pattern `(2)`;
- 2 branches have `(2,1)` with null separation `q^2=0`;
- 4 branches have `(2,1)` with `q^2=0.21`;
- 4 branches have `(2,1)` with `q^2=0.41`;
- 12 branches have `(2,1,1)` with triangle edge invariants `(0,0.21,0.41)`.

Thus every nontrivial closed branch has exactly one squared denominator. No cubic or higher propagator power appears.

A new exact substructure was found for the 12 raised triangles. If the doubled propagator is chosen as the canonical loop origin, the two invariant edges incident on it split the branches into exactly three sectors of four branches each:

- `(0,0.21)`: 4;
- `(0,0.41)`: 4;
- `(0.21,0.41)`: 4.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_RAISED_INDEX_SECTOR_CANONICALIZATION`.

Guardrail:

`DO_NOT_COMBINE_TRIANGLE_BRANCHES_BEFORE_MAPPING_THE_SQUARED_DENOMINATOR_TO_A_CANONICAL_VERTEX_AND_TRANSFORMING_THE_NUMERATOR_WITH_THE_SAME_LOOP_SHIFT`.

Classification: exact routing/canonicalization result. It is not a consistency FAIL or PASS of a candidate model, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy and not a novelty certificate.

The current operational blocker is refined to:

`BLOCKED_CANONICAL_SECTOR_P_DEPENDENT_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

MODEL_READINESS: 24%

Change from previous recorded estimate: 0 percentage points. Comparator foundation remains 24/25 and robust unique residual remains 0/20. The iteration removes a routing ambiguity required for a valid IBP extraction, but does not yet create the physical linked comparator coordinate or comparator-subtracted residual.

Exact next gate: for bubble-a, bubble-b and each of the three raised-triangle vertex sectors, apply the canonical loop shift placing the squared denominator at `l^2`; reconstruct each sector-summed numerator in a finite Lorentz-covariant basis of `l` and external invariants; validate on held-out loop momenta; then tensor/IBP reduce the canonical sector sums. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
