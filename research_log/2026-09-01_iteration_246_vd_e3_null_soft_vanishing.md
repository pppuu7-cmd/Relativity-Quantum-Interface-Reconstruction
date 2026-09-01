# RQIR Research Log — Iteration 246

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Goal

Test the exact `e=3,c=0` Vilkovisky connection sector on the physical null-TT soft branch frozen by the RQIR soft protocol.

## Reproducible geometry

For `k=(1,0,0,1)` and normalized plus TT polarization:

- `k^2=0`;
- trace = 0;
- transversality residual = 0;
- linearized Ricci = 0;
- linearized Einstein tensor = 0;
- linearized Riemann is nonzero with Frobenius norm `~2`.

## Structural result

`Tr(U1^3)` and `Tr(U1 U2)` are both cubic in explicit Einstein-EOM insertions at `e=3,c=0`. With flat kernels frozen, their cubic functional derivative is trilinear in the three linearized EOM factors. Every permutation with one physical null-TT soft leg therefore contains

`E^(1)[h_soft]=0`.

Hence the complete `e=3,c=0` connection contribution vanishes on this scoped soft branch.

Freeze:

`PASS_SCOPED_VD_E3_NULL_SOFT_TT_VANISHING`.

## Guardrail

This does not set the full C5 comparator to zero. Determinant `e=0`, `e=1,c=2` and `e=2,c=1` sectors remain required and can contain the soft leg through curvature/operator dressing.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next

Iteration 247: enumerate the surviving soft placements in `e=0,1,2` and build the minimal surviving-sector graph before heavy calculation.
