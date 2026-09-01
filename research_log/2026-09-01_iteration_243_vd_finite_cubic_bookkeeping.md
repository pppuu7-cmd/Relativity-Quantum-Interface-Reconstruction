# RQIR Research Log — Iteration 243

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Goal

Bound the Vilkovisky EOM/insertion order required for the finite pure-Einstein `O(R^3)` comparator on the frozen Minkowski, `Lambda=0` target.

## Result

Since `epsilon_i=S_,i=O(R)` around flat space, introduce EOM degree `e` and additional background-curvature degree `c`. Only terms with

`e+c <= 3`

can contribute to the frozen curvature-cubic target.

Therefore:

- determinant sector `e=0`: need background order 3;
- `Tr U1`, `e=1`: need dressing through order 2;
- `Tr U2`, `Tr U1^2`, `e=2`: need dressing through order 1;
- complete `e=3` sector: leading flat kernels only;
- all `e>=4`: provably irrelevant in this scope.

Cubic trace topology can contain primitive `Tr(U3_a)`, mixed `Tr(U1 U2)` and `Tr(U1^3)`, but coefficients/operator content are not fixed by the published quadratic UV truncation.

## Classification

`FINITE_CUBIC_VD_BOOKKEEPING_CLOSED_OEPS3_FORMULA_STILL_BLOCKED`.

## Heavy compute

Not authorized yet. Exact `O(epsilon^3)` Vilkovisky reduced operator formula is required first.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next

Iteration 244: recover from primary authority or rederive the exact cubic EOM insertion formula, reproducing the published `O(epsilon^2)` formula as a unit check.
