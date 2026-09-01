# Recovery Delta — RQIR Iteration 243

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Previous front

Iteration 242 selected `C5_full_Vilkovisky_finite_CPT3` as the highest-priority comparator authority-improvement route.

## New theorem

Frozen scope: Minkowski expansion, `Lambda=0`, finite one-loop effective action through `O(R^3)`.

Because the Einstein EOM satisfy `epsilon=O(R)` on this scope, a Vilkovisky insertion contribution with explicit EOM degree `e` and additional background-curvature dressing `c` can enter only if

`e+c <= 3`.

Thus the full infinite EOM insertion series is not required:

- `e=0`: background expansion through `R^3`;
- `e=1`: through extra `R^2`;
- `e=2`: through extra `R^1`;
- `e=3`: leading flat kernels only;
- `e>=4`: irrelevant to this scoped target.

The cubic trace-topology classes are `Tr(U3_a)`, `Tr(U1 U2)` and `Tr(U1^3)`, but the exact coefficients and primitive `U3_a` content are not fixed by the published UV-truncated Eq. (14).

## Status

`FINITE_CUBIC_VD_BOOKKEEPING_CLOSED_OEPS3_FORMULA_STILL_BLOCKED`.

Heavy finite-CPT3 calculation remains NOT AUTHORIZED until the exact `O(epsilon^3)` reduced operator formula is frozen.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Restart

Iteration 244:

1. recover explicit `O(epsilon^3)` terms from Cho–Kantowski / Barvinsky–Vilkovisky primary authority if possible;
2. test whether the operator formula is general-dimensional;
3. otherwise rederive it from exact one-loop Vilkovisky Eq. (11), reproducing Eq. (14) through `O(epsilon^2)` as a mandatory unit test;
4. do not guess cubic coefficients from the quadratic series pattern.
