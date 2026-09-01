# Recovery Delta — RQIR Iteration 225

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## New authority

Iteration 225 resolves the Iteration-224 numerical global-bulk blocker for `MSSC-001` without changing any physics subtraction. The Iteration-222 authority `R_in=R_out=-8 M_Born` remains fixed, and the Iteration-223 local `delta^2` cap-shell integrability result remains retained.

The sphere is partitioned into exact spherical Voronoi cells around the two certified collinear directions. Each cell is integrated in its own local polar coordinates, with exact radial boundary

`rho_max(phi)=atan2(1-cos(gamma), sin(gamma) cos(phi))`.

Two independent deterministic cubatures are compared: Gauss-Legendre radial x midpoint azimuth and Gauss-Legendre radial x Gauss-Legendre azimuth.

Across the frozen five scattering angles and both independent linear spin-2 polarizations, order 32 gives a worst relative disagreement of `2.584334806770234e-7`. For the two slowest rows (`theta_ext=2.1`), order 40 reduces the discrepancy to at most `6.135670833005235e-9`.

Freeze a conservative relative numerical envelope `3e-7` for this comparator hard remainder.

## Classification

- local IR completion: `PASS_FROM_ITERATION223`;
- global finite source hard remainder: `PASS_NUMERICAL_GLOBAL_COMPLETION`;
- Iteration-224 operational blocker: `RESOLVED`;
- physics consistency FAIL: `NO`;
- exact comparator identity: `NO`;
- near-degeneracy: `NO`;
- Candidate Gravity residual: `NONE`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.

## Retained labels

- `NUM-NG-014 — SINGULARITY_ADAPTED_VORONOI_CUBATURE_REMOVES_THE_GLOBAL_CHART_ALIASING_BLOCKER`;
- `SRC-CUT-006 — MSSC001_BORN_SUBTRACTED_GLOBAL_HARD_REMAINDER_IS_NUMERICALLY_STABLE_ACROSS_TWO_INDEPENDENT_CUBATURES`;
- `NG-FUNNEL-081 — NUMERICAL_SOURCE_COMPARATOR_CLOSURE_IS_COMPARATOR_AUTHORITY_NOT_CANDIDATE_NOVELTY`.

## Readiness

`MODEL_READINESS: 24%` — increased from 23% by exactly one percentage point. The increase is assigned only to comparator foundation because one previously blocked comparator component has actually closed. Unique residual discovery remains `0/20`; parent dynamics/ANSATZ and all downstream candidate-specific blocks remain `0`.

## Exact restart instruction

Iteration 226: use the stable `MSSC-001` finite hard remainder to extract its frozen regular+log/nonanalytic structure in the same convention, then compare that structure with the distinct pure-graviton positive control without identifying the two observables. If the structure is not robust under the frozen numerical envelope, classify it as numerical/operational BLOCKED rather than novelty. AS remains `BLOCKED_AS_REALTIME_RELATION_COMPLETION`; C3 remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`; neither may be zero-filled. No `ANSATZ-003`, Fisher, or resources are authorized.
