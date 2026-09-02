# Candidate Gravity C5 — Iteration 282 raised-index canonicalization

## Purpose
Iteration 281 rejected fitting constant master coefficients directly to the pre-integration family trace. Before reconstructing genuine p-dependent family numerators, the remaining loop-routing ambiguity must be removed exactly so that branches related by a loop shift are not fitted as if they were different functions.

## Exact census
Using the frozen translation-closed B3 primitive branch structure, all 23 branches were enumerated with their routed Q0 denominator shifts and multiplicities.

The multiplicity/invariant census is:

- one single squared scaleless family: `(2)`;
- two null raised bubbles: `(2,1)` with `q^2=0`;
- four bubble-b branches: `(2,1)` with `q^2=0.21`;
- four bubble-a branches: `(2,1)` with `q^2=0.41`;
- twelve raised triangles: `(2,1,1)` with pairwise edge invariants `(0,0.21,0.41)`.

Therefore every nontrivial closed branch contains exactly one doubled denominator and no higher propagator power.

## New triangle substructure
The twelve triangle branches cannot yet be treated as one numerator family before fixing which denominator is squared. Taking the doubled propagator as the canonical loop origin, the two incident edge invariants split the triangle branches into three equal sectors:

- `(0,0.21)`: 4 branches;
- `(0,0.41)`: 4 branches;
- `(0.21,0.41)`: 4 branches.

Thus the scalar triangle topology remains one kinematic family, as frozen previously, but the numerator reconstruction must first respect three raised-index vertex sectors. Only after applying the corresponding loop shift to both denominators and numerator may sector sums be compared or combined.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_RAISED_INDEX_SECTOR_CANONICALIZATION`.

Guardrail:

`DO_NOT_COMBINE_TRIANGLE_BRANCHES_BEFORE_MAPPING_THE_SQUARED_DENOMINATOR_TO_A_CANONICAL_VERTEX_AND_TRANSFORMING_THE_NUMERATOR_WITH_THE_SAME_LOOP_SHIFT`.

## Scientific classification
This is an exact routing/canonicalization result. It is not a consistency PASS of a Candidate Gravity model, not a comparator identity, not a unique residual, not a near-degeneracy statement and not a novelty certificate.

It strengthens the operational path to the C5 coefficient extraction by reducing the genuine reconstruction problem to two non-scaleless raised-bubble sectors plus three canonical raised-triangle vertex sectors. The null bubble and single-denominator sectors remain scaleless in the frozen massless-DR treatment.

## Next gate
For bubble-a, bubble-b and each of the three raised-triangle vertex sectors, apply the canonical loop shift placing the doubled denominator at `l^2`; reconstruct the sector-summed numerator in a finite Lorentz-covariant basis in `l` and external invariants; validate on held-out loop-momentum points; then tensor/IBP reduce the combined canonical sectors. No fitted surrogate master coefficients are allowed.
