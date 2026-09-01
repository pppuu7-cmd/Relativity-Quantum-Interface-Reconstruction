# Recovery Delta — RQIR Iteration 245

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Previous front

Iteration 244 closed the exact reduced VD cubic insertion identity and narrowed C5 to the composite `U1,U2` trace map.

## New result

Primary definitions freeze the primitive inverse-operator content:

- `U1`: two ghost Green operators `N`, EOM degree 1;
- `U2`: two `N` plus one field/graviton Green operator `G`, EOM degree 2.

Before explicit Ward/numerator reductions:

- `Tr U1 -> (2N,0G)`;
- `Tr U2 -> (2N,1G)`;
- `Tr U1^2 -> (4N,0G)`;
- `Tr U1^3 -> (6N,0G)`;
- `Tr(U1 U2) -> (4N,1G)`.

Do not equate EOM degree with propagator count.

## Stronger cyclic master-topology reduction

At frozen total curvature order `R^3`, cyclicity plus locality of the insertions means repeated Green operators raise powers on loop-momentum segments rather than create extra external-momentum corners. There are at most three background insertions around the one-loop trace.

Therefore the flat cubic EOM sectors reduce to raised-index triangle families:

- `Tr U1^3 -> I222`;
- `Tr(U1 U2) -> I212` up to cyclic labeling.

No one-loop scalar polygon beyond a triangle is required for the cubic VD connection sector at this curvature order.

Freeze:

`PASS_COMPOSITE_TRACE_MASTER_TOPOLOGY_REDUCTION`.

## CPT3 boundary

Standard published CPT3 form factors apply to a generic single Laplace-type operator and cannot simply be substituted for the composite inverse-operator traces. The mixed ghost/graviton sector remains a different functional object. However its flat cubic scalar kinematics are standard raised-propagator one-loop triangles and are therefore directly amenable to Feynman-parameter/tensor-reduction methods.

Retain:

`NO_DIRECT_SINGLE_OPERATOR_CPT3_IDENTITY_FOR_COMPOSITE_U1_U2_TRACES`.

## Finite resolvent completion

Iteration 243 proved `e+c<=3`, so only a finite set of lower-sector dressings is needed:

- `Tr U1`: curvature dressing through `c=2`;
- `Tr U2`, `Tr U1^2`: through `c=1`;
- `Tr U1^3`, `Tr(U1 U2)`: flat kernels only (`c=0`).

Use same-parent resolvent expansions

`N^-1=N0^-1-N0^-1 dN N0^-1+...`,

`G=G0-G0 dH G0+...`.

## Current blocker

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`.

`BLOCKED_NOT_ZERO`.

This is operational/derivational BLOCKED, not consistency FAIL, exact identity, regime-specific non-identifiability or near-degeneracy.

## Compute policy

A blind full finite-CPT3 run remains forbidden. A **scoped flat `e=3` symbolic run is authorized** as a component/unit block once it uses the exact frozen 4D convention. `ANSATZ-003` remains not created. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 244. The topology ambiguity closes and the C5 route becomes more executable, but the finite physical comparator coordinate is still not computed; no rubric block closes.

## Restart — Iteration 246

1. freeze flat `N0^-1` and `G0` projectors/normalization in the Iteration-232 convention;
2. derive linearized Einstein `E[h]` and required `Q_;` / `V1,V2` vertices;
3. contract `Tr U1^3` and `Tr(U1 U2)` into the `I222/I212` tensor numerators;
4. reproduce the published quadratic VD connection contribution/divergence as a normalization unit test;
5. test Ward/source structure and a second admissible field parametrization before any physical claim;
6. only after those tests address lower-EOM curvature dressing and final source-completed `T_cut` projection.
