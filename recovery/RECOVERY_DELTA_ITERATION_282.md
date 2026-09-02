# RECOVERY DELTA — ITERATION 282

## Authority
Source-of-truth front before this iteration: Iteration 281. Latest research log/recovery and recent commits were checked. No active GitHub Action was running.

## New exact result
The translation-closed B3 primitive denominator routing was canonicalized before any p-dependent numerator fit or IBP reduction.

Across all 23 primitive branches:

- single squared scaleless: 1 branch, multiplicity `(2)`;
- null raised bubble: 2 branches, `(2,1)`, `q^2=0`;
- bubble-b: 4 branches, `(2,1)`, `q^2=0.21`;
- bubble-a: 4 branches, `(2,1)`, `q^2=0.41`;
- raised triangle: 12 branches, `(2,1,1)`, pairwise invariants `(0,0.21,0.41)`.

Every nontrivial branch contains exactly one doubled propagator; no denominator power >2 occurs.

Choosing the doubled triangle propagator as canonical loop origin resolves the 12 triangle branches into three raised-index sectors, four branches each, labeled by incident squared-momentum pairs:

- `(0,0.21)`;
- `(0,0.41)`;
- `(0.21,0.41)`.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_RAISED_INDEX_SECTOR_CANONICALIZATION`.

Guardrail:

`DO_NOT_COMBINE_TRIANGLE_BRANCHES_BEFORE_MAPPING_THE_SQUARED_DENOMINATOR_TO_A_CANONICAL_VERTEX_AND_TRANSFORMING_THE_NUMERATOR_WITH_THE_SAME_LOOP_SHIFT`.

This preserves the previously frozen statement that the scalar nontrivial master topology consists of two raised bubbles and one triangle kinematic family; the new result concerns raised-index numerator routing inside that triangle family.

## Current blocker

`BLOCKED_CANONICAL_SECTOR_P_DEPENDENT_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

This is operational BLOCKED. It is not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy or absence/presence of a novelty certificate.

## Readiness

MODEL_READINESS: 24%

Change from previous recorded estimate: 0 percentage points. Comparator foundation remains 24/25; robust unique residual remains 0/20. Exact routing ambiguity was removed but no comparator-subtracted C5 coordinate was produced.

## Exact next gate
For bubble-a, bubble-b and each of the three canonical raised-triangle vertex sectors, shift the doubled denominator to `l^2`, transform the numerator with the identical loop shift, reconstruct the combined p-dependent numerator in a finite Lorentz-covariant tensor/rational basis, validate it on held-out loop momenta, then perform tensor/IBP reduction on sector sums. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
