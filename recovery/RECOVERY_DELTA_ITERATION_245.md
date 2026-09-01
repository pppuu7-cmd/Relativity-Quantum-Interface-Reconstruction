# Recovery Delta — RQIR Iteration 245

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Previous front

Iteration 244 closed the exact reduced VD cubic insertion identity and narrowed C5 to the composite `U1,U2` trace map.

## New result

Primary definitions freeze the primitive inverse-operator content:

- `U1`: two ghost Green operators `N`, EOM degree 1;
- `U2`: two `N` plus one field/graviton Green operator `G`, EOM degree 2.

Hence, before explicit Ward/numerator reductions,

- `Tr U1 -> (2N,0G)`;
- `Tr U2 -> (2N,1G)`;
- `Tr U1^2 -> (4N,0G)`;
- `Tr U1^3 -> (6N,0G)`;
- `Tr(U1 U2) -> (4N,1G)`.

Do not equate EOM degree with propagator count.

## CPT3 boundary

Standard published CPT3 form factors apply to a generic single Laplace-type operator and cannot simply be substituted for these composite inverse-operator traces, especially the mixed ghost/graviton `U2` sector.

Freeze:

`NO_DIRECT_SINGLE_OPERATOR_CPT3_IDENTITY_FOR_COMPOSITE_U1_U2_TRACES`.

## Executable replacement

On the frozen Minkowski `Lambda=0` finite-`R^3` target, use finite resolvent expansions of the already-fixed operators:

`N^-1=N0^-1-N0^-1 dN N0^-1+...`,

`G=G0-G0 dH G0+...`.

Together with the Iteration-243 bound `e+c<=3`, this requires only:

- `Tr U1`: curvature dressing through `c=2`;
- `Tr U2`, `Tr U1^2`: through `c=1`;
- `Tr U1^3`, `Tr(U1 U2)`: flat kernels only (`c=0`).

All remaining pieces are finite one-loop flat-space tensor-integral sectors once the frozen 4D vertices are written explicitly.

## Current blocker

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_AND_SOURCE_PROJECTION`.

`BLOCKED_NOT_ZERO`.

This is an operational/derivational blocker, not a consistency FAIL, exact identity, non-identifiability result, or near-degeneracy.

## Compute policy

Blind heavy CPT3 remains forbidden. A bounded symbolic flat-kernel/resolvent derivation is authorized next. `ANSATZ-003` remains not created. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 244. No rubric block closes because the finite physical C5 comparator coordinate is still not computed.

## Restart — Iteration 246

1. freeze `N0^-1` and `G0` in the Iteration-232 4D convention;
2. derive linearized Einstein `E[h]` and required `Q_;` vertices;
3. build `U1^(1)` and `U2^(2)` momentum-space kernels;
4. reproduce the published quadratic VD connection contribution/divergence as a normalization unit test;
5. only then construct cubic `Tr U1^3` and `Tr(U1 U2)` integrands and test Ward/source projection.
