# Candidate Gravity C5 — Iteration 292 complete Tr U1 denominator census

**Date:** 2026-09-03  
**MODEL_READINESS:** **24%**

## Purpose

After Iteration 291 established

`U1 = B Y_down`, `B=Q A Q`,

construct the complete primitive denominator census for the mixed cubic coefficient `[Tr U1]_{sab}` rather than for the weighted proxy `tr(B3)`.

## Exact branch census

The rightmost local `Y_down` insertion carries background momentum but no loop propagator. Enumerating all exact Q-recursion branches gives

- total primitive branches: **36**;
- `Y` background degree 0 (`B3Y0`): **23**;
- `Y` background degree 1 (`B2Y1`): **11**;
- `Y` background degree 2 (`B1Y2`): **2** after the exact null-soft `B1[s]=0` elimination.

There are **32 non-scaleless branches**.

The direct complete matrix trace at the frozen Iteration-273 checkpoint is

`0.8049286124063145`,

while the denominator-stripped primitive reconstruction gives

`0.8049286124067728`.

Absolute residual:

`4.583000645652646e-13`.

Freeze:

`PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

## Denominator families

### Retained weighted-B3 families

- one single scaleless branch;
- 10 raised bubbles:
  - 4 hard-a,
  - 4 hard-b,
  - 2 null/scaleless;
- 12 raised triangles:
  - 4 repeated-vertex sector `(0,0.21)`,
  - 4 sector `(0,0.41)`,
  - 4 sector `(0.21,0.41)`.

### New weight-completion families

The `B2Y1` and `B1Y2` terms generate denominator families that were absent from the `tr(B3)` proxy calculation:

- 5 ordinary bubbles:
  - 2 hard-a,
  - 2 hard-b,
  - 1 null/scaleless;
- 8 ordinary one-null two-mass triangles with invariant set
  `(0,0.21,0.41)`.

Thus the previous raised-only master census is incomplete for the actual `Tr U1` insertion.

## Why ordinary families appear

For closed `B3`, the left and right endpoint Q0 propagators coincide, producing the repeated line. For a lower-order `B2` or `B1` block followed by a local `Y_down` insertion, the local weight carries the compensating external momentum. The endpoints of the B block are therefore distinct before the final Y insertion, converting the same routed construction into ordinary two- or three-propagator loop families.

`Y_down` itself remains local and introduces no new propagator.

## Analytic loop-momentum degree ceilings

The exact primitive definitions also sharpen the degree bounds.

From the frozen implementation:

- `N1(p)` and `N2(p)` are polynomial of degree `<=2` in loop momentum;
- numeratorized `Q1` therefore has degree `<=2`;
- sequential numeratorized `Q2` has degree `<=4` and its contact part `<=2`;
- every `A_n(p)` has degree `<=2` because each gauge-generator factor is at most linear in endpoint momentum and the directional/connection product is at most quadratic;
- every `Y_n` is local and independent of loop momentum.

Consequently:

- new ordinary bubbles (`Q0 A2 Q0` or `Q0 A1 Q0`): degree `<=2`;
- new ordinary triangles (`Q1 A1 Q0` or transpose): degree `<=4`;
- retained conservative raised-bubble bound: degree `<=4`;
- retained conservative raised-triangle bound: degree `<=6`.

These are conservative complete coordinate-degree ceilings; Iteration 293 must still certify the actual family-summed polynomial reconstruction on held-out points.

## Null-soft sector inventory

Iteration 246 remains authoritative on the frozen physical null-TT soft branch:

`e=3,c=0` vanishes because each trilinear EOM-degree-three term contains `E^(1)[h_soft]=0`.

Therefore the active C5 sectors on this branch are:

- determinant `e=0,c<=3`;
- connection `e=1,c<=2` — current route;
- connection `e=2,c<=1`.

The exact generic `e=3` Vilkovisky formula remains valid authority but is not an active calculation block on this soft branch.

## Current blocker

`BLOCKED_COMPLETE_TRU1_FAMILY_NUMERATOR_RECONSTRUCTION_AFTER_WEIGHT_COMPLETION`.

## Next gate — Iteration 293

For all eight non-scaleless sectors:

1. canonicalize loop routing by exact shifts/reflections;
2. fit full-coordinate polynomial bases at the proven degree ceilings;
3. require full rank and independent held-out residuals;
4. export coefficients for tensor reduction;
5. only after basis certification run the corrected DR/Laurent reduction.

No Candidate Gravity residual is declared. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
