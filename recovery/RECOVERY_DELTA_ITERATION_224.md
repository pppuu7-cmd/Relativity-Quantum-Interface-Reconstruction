# Recovery Delta — RQIR Iteration 224

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New authority

Iteration 222 fixed the source-cut collinear residues to `R_in=R_out=-8 M_Born` without cap fitting. Iteration 223 proved that the corresponding Born-subtracted cap shells vanish as `delta^2`.

Iteration 224 tests the global cap-excised finite bulk integral using two deterministic angular decompositions: a laboratory Gauss-Legendre(`mu`) x midpoint(`phi`) chart and the same quadrature after a fixed `0.371 rad` y-rotation. Resolutions `N={12,16,20}` and cap radii `delta={0.08,0.04}` were checked over five external scattering angles and both independent linear spin-2 polarizations.

The finest-grid relative chart disagreement ranges from `3.10e-4` to `1.3819475e-1`. Worst case: `theta_ext=0.45`, cross polarization, `delta=0.04`, with values `49.0040889813` and `56.8621379324`.

## Classification

- local IR completion: `PASS_FROM_ITERATION223`;
- global finite source hard remainder: `BLOCKED_NUMERICAL_BULK_HARD_REMAINDER`;
- physics consistency FAIL: `NO`;
- exact comparator identity: `NO`;
- near-degeneracy: `NO`;
- Candidate Gravity residual: `NONE`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.

## Retained labels

- `NUM-NG-013 — TWO_FIXED_ANGULAR_DECOMPOSITIONS_DO_NOT_YET_CONVERGE_TO_A_COMMON_MSSC001_GLOBAL_HARD_REMAINDER_ON_THE_TESTED_GRIDS`;
- `SRC-CUT-005 — LOCAL_DELTA2_CAP_COMPLETION_DOES_NOT_GUARANTEE_GLOBAL_BULK_QUADRATURE_STABILITY`;
- `NG-FUNNEL-080 — A_COORDINATE_DEPENDENT_BULK_NUMBER_MUST_NOT_BE_FROZEN_AS_A_PHYSICAL_COMPARATOR_REMAINDER`.

## Readiness

`MODEL_READINESS: 23%` — unchanged from Iteration 223. This iteration localizes a numerical blocker but closes no readiness rubric block.

## Exact restart instruction

Iteration 225: implement singularity-adapted domain decomposition. Keep the two certified collinear neighborhoods in local polar coordinates, integrate only the smooth cap-excised bulk with two independent high-order cubatures, and combine with the separately controlled cap contribution. Require common convergence under both cubatures and cap-size variation before freezing any finite `MSSC-001` hard remainder. AS/C3 remain BLOCKED and must not be zero-filled. No Candidate Gravity ansatz, Fisher, or resource calculation is authorized.
