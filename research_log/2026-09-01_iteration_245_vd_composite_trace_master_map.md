# RQIR Research Log — Iteration 245

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Starting authority

Recent commits superseded the lagging `CURRENT_QG_FRONT`: Iteration 244 had already closed the exact cubic VD insertion-series coefficients,

`Gamma_conn^(3) = +(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)`,

with no primitive reduced `U3` term required.

## Goal

Determine the actual operator topology of the required `U1,U2` traces and whether ordinary single-operator CPT3 can be used directly.

## Primary-definition audit

Cho–Kantowski / the same Barvinsky–Vilkovisky reduction used in the 4D authority gives `U1` with two ghost Green operators and `U2` with two ghost Green operators plus one graviton Green operator. Before Ward/numerator reduction:

- `Tr U1`: `(n_N,n_G)=(2,0)`;
- `Tr U2`: `(2,1)`;
- `Tr U1^2`: `(4,0)`;
- `Tr U1^3`: `(6,0)`;
- `Tr(U1 U2)`: `(4,1)`.

EOM degree is therefore not propagator count.

## Stronger cyclic/topology reduction

Using cyclicity of the trace and treating the local `Y`/vertex factors as insertions, repeated inverse operators on one loop-momentum segment raise denominator powers rather than create new external-momentum corners. At the frozen total curvature order `R^3` there are at most three external background insertions around the loop.

Therefore the cubic flat-kernel sectors reduce to one-loop triangle families with raised powers:

- `Tr U1^3 -> I222`: three ghost segments, each with doubled denominator power;
- `Tr(U1 U2) -> I212` up to cyclic labeling: two doubled ghost segments and one graviton segment.

No box, pentagon, hexagon or higher one-loop scalar polygon is required by the cubic VD connection sector at this curvature order. The species distinction survives in tensor numerators/projectors, not in introducing a new loop topology.

Freeze:

`PASS_COMPOSITE_TRACE_MASTER_TOPOLOGY_REDUCTION`.

## CPT3 audit

Published Barvinsky–Vilkovisky CPT3 supplies finite third-order form factors for a generic single Laplace-type operator. It does not automatically equal the composite `U1,U2` inverse-operator traces, especially the mixed ghost/graviton sector. However the flat cubic pieces lie in ordinary one-loop raised-index triangle kinematics and admit standard Feynman-parameter/tensor-reduction treatment.

Therefore both statements are retained:

`NO_DIRECT_SINGLE_OPERATOR_CPT3_IDENTITY_FOR_COMPOSITE_U1_U2_TRACES`,

but

`SCOPED_FLAT_E3_SYMBOLIC_C5_RUN_AUTHORIZED`.

## Finite resolvent reduction

Because Iteration 243 proved `e+c<=3`, lower-EOM sectors require only finite resolvent dressings around the frozen flat operators:

`N^-1=N0^-1-N0^-1 dN N0^-1+...`,

`G=G0-G0 dH G0+...`.

Required orders:

- `Tr U1`: through `c=2`;
- `Tr U2`, `Tr U1^2`: through `c=1`;
- `Tr U1^3`, `Tr(U1 U2)`: flat kernels only (`c=0`).

Thus the remaining C5 calculation is a finite one-loop tensor/projector problem plus lower-sector curvature dressing and final source-completed projection.

## Classification

Current blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`.

`BLOCKED_NOT_ZERO`.

This is operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability or near-degeneracy.

## Compute decision

A blind full finite-CPT3 run remains premature. A scoped flat `e=3` symbolic calculation is now authorized as a component/unit block, provided it uses the exact frozen 4D convention and is checked for parametrization-coordinate independence/Ward structure before any physical claim. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%`.

Change from Iteration 244: **0 percentage points**. The C5 authority path is materially more executable and the loop-topology ambiguity is closed, but the physical finite C5 comparator coordinate is not yet computed; no readiness-rubric block closes.

## Next gate

Iteration 246: freeze the explicit flat-space numerator block in the Iteration-232 convention: `N0^-1`, `G0`, linearized Einstein `E[h]`, and the required `Q_;` / `V1,V2` vertices; contract `Tr U1^3` and `Tr(U1 U2)` into `I222/I212` tensor numerators; reproduce the published quadratic VD connection contribution/divergence as normalization control; then test Ward/source compatibility and a second admissible field parametrization before any physical comparator claim.
