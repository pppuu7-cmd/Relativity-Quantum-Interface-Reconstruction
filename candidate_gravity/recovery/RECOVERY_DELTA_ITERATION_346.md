# Recovery Delta — Candidate Gravity Iteration 346

Date: 2026-09-03

## Scope

Operator-level assembly/validation of the complete 12 surviving cubic-background `Tr U2` routes from frozen Iteration 308, using the binding U2 order/orientation and routing authorities from Iterations 339-345. Physical `A1/A2`, `N/Y`, and graviton inverse component values were not rederived; this gate isolates route assembly and momentum provenance.

## Raw Actions authority

- run: `33771412442`
- job: `100702287231`
- artifact: `9899772352` (`iteration346-result`)
- artifact digest: `sha256:109079c6f4e2f47f096fc3a3ba10c7930f34260f111f97c54d6e5c898c2ad63a`
- scientific JSON SHA-256: `8fae654f1c713770b6d6f91e0dfe646d37ffa9b2c11ccffe4ebaca189d5e3d4e`
- workflow head: `3f2212743bf376c8947bb2a15e6199bba6dd4a56`

The artifact is schema-valid and was independently inspected; workflow green status alone was not treated as scientific authority.

## Result

Frozen operator order:

`U2 = N_L @ A_T @ Hinv_VD @ A_R @ N_R @ Y`, with `Hinv_VD=-K^-1`.

Independent brute-force full-product coefficient extraction reproduces exactly the Iteration-308 census:

- raw cubic placements: `30`
- exact singleton-soft kills: `18`
- surviving routes: `12`
- survivor site census: `2` each on `N_L`, `A_T`, `Hinv_VD`, `A_R`, `N_R`, `Y`.

Route-by-route explicit survivor construction agrees exactly with the brute-force coefficient extraction:

- max route matrix mismatch: `0.0`
- max route trace mismatch: `0.0`
- summed matrix mismatch: `0.0`
- summed trace mismatch: `0.0`
- max closed-triad loop error: `5.551115123125783e-17`
- max norm among the 18 null-soft killed routes: `0.0`.

The gate also proves the previously frozen routing details are nontrivial rather than cosmetic: deliberately using a same-input-momentum transpose changes every tested route by at least `8.593309331286214`, while deliberately suppressing incoming momentum shifts changes routes by at least `1.900214417122233`, both vastly above the frozen `1e-6` discrimination floor.

Authority:

`PASS_U2_COMPLETE_12_SURVIVING_CUBIC_ROUTE_OPERATOR_ASSEMBLY_WITH_FUNCTIONAL_TRANSPOSE_AND_MOMENTUM_PROVENANCE__PHYSICAL_CUT_REDUCTION_AUTHORIZED_NEXT`.

## Scientific classification

This is an operator-routing assembly PASS. It is not an integrated `Tr U2` cut, not a Candidate Gravity residual, not a comparator identity, not a consistency FAIL, not regime-specific non-identifiability, and not a novelty certificate.

Iterations 343-344 remain preserved implementation/gate-design FAILs; no threshold was weakened and no old failed oracle was retroactively repaired.

## Status

- frozen: Iteration-308 12-route cubic placement/pruning map;
- frozen: Iteration-340 `A.T/A` orientation and `Hinv_VD=-K^-1`;
- frozen: Iteration-341 physical same-parent `A1/A2`;
- frozen: Iteration-342 `N/Y` bridge;
- frozen: Iteration-345 functional-transpose Fourier routing;
- frozen now: complete executable 12-route `Tr U2` operator assembly with exact momentum provenance;
- authorized next: substitute the already-frozen physical components on the matched timelike fixture and canonicalize the 12 physical `Tr U2` numerator/denominator families before any cut integration;
- still forbidden: Source/Born subtraction, `ANSATZ-003`, Fisher/resources, blind full-C5.

Independent determinant Iteration 335 replacement run `33759144658` remains active and must not be duplicated while active.

MODEL_READINESS: 24%

Change from Iteration 345: `0 pp`; the complete U2 route-assembly prerequisite closed, but no full readiness-rubric bucket and no robust comparator-subtracted residual closed.
