# Recovery Delta — RQIR Iteration 246

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Previous front

Iteration 245 reduced the exact cubic Vilkovisky connection terms to raised one-loop triangle topologies and authorized a scoped flat `e=3` symbolic subproblem.

## New result

On the frozen physical null-TT soft branch (`k=(1,0,0,1)`, plus TT polarization), the linearized Einstein EOM vanishes exactly while the linearized Riemann tensor remains nonzero.

The exact cubic connection terms

`+(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)`

are, at `e=3,c=0`, trilinear in three explicit linearized EOM insertions with all other kernels frozen flat. Every cubic permutation containing the soft leg therefore carries the factor

`E^(1)[h_soft]=0`.

Freeze:

`PASS_SCOPED_VD_E3_NULL_SOFT_TT_VANISHING`.

## Scope

Only the `e=3,c=0` connection block is eliminated in the frozen null-soft branch.

Still required:

- determinant `e=0` through curvature order 3;
- connection `e=1` with curvature/operator dressing through order 2;
- connection `e=2` with dressing through order 1;
- causal/source-completed hard-channel discontinuity projection.

Do not zero-fill the full C5 comparator.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Restart

Iteration 247: enumerate surviving soft-leg placements in `e=0,1,2`, identify which insertions vanish because the soft leg sits in an explicit EOM factor, and freeze the minimal surviving C5 calculation graph before any heavy tensor run.
