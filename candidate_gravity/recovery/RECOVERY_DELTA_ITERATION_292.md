# Recovery Delta — Iteration 292

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Frozen result

The complete mixed-cubic `Tr U1` denominator census after exact `Y_down` weight completion contains 36 primitive branches:

- `B3Y0`: 23;
- `B2Y1`: 11;
- `B1Y2`: 2 nonzero after null-soft elimination.

There are 32 non-scaleless branches.

Direct complete trace at the frozen checkpoint:

`0.8049286124063145`.

Primitive denominator reconstruction:

`0.8049286124067728`.

Residual:

`4.58e-13`.

Freeze:

`PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

## New denominator families

In addition to the old raised B3 families, weight completion introduces:

- ordinary bubbles: 5 total = 2 hard-a + 2 hard-b + 1 null/scaleless;
- ordinary triangles: 8, all in the one-null two-mass invariant class `(0,0.21,0.41)`.

The old raised-only master census is therefore incomplete for `Tr U1`.

## Degree ceilings

From the exact primitive momentum dependence:

- ordinary bubble numerator degree `<=2`;
- ordinary triangle degree `<=4`;
- raised bubble retained bound `<=4`;
- raised triangle retained bound `<=6`.

These still require held-out family-summed reconstruction certification.

## Soft-branch sector correction

Iteration 246 already proves the `e=3,c=0` Vilkovisky connection sector vanishes on the frozen null-TT soft branch. Active sectors are `e=0`, `e=1`, `e=2`; do not reopen e=3 as an active soft-branch blocker.

## Next

Iteration 293: canonicalize all eight non-scaleless sectors, fit complete coordinate polynomial numerators at the proven ceilings, require held-out validation, and export coefficients for corrected tensor/Laurent reduction.

No Candidate Gravity residual. `ANSATZ-003` not created. Fisher/resources forbidden.
