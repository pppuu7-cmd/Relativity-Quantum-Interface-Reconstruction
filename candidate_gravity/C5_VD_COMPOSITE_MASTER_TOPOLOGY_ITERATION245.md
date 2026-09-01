# RQIR Candidate Gravity — Vilkovisky Composite-Trace Master Topology

**Iteration:** 245  
**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Starting authority

Iteration 244 fixed the 4D connection-sector cubic terms as

`Gamma_conn^(3) = + i/2 Tr(U1 U2) - i/6 Tr(U1^3)`.

Giacchini–de Paula Netto–Shapiro Eq. (16)–(17) defines

`U1 = N R (D R) epsilon N Y = N V2 N Y`,

`U2 = N (D R) epsilon H^{-1} (D R) epsilon N Y = N V1 H^{-1} V1 N Y`,

where Eq. (54) defines `V1` and `V2`.

For `a=-1/2`, the same authority makes both the graviton operator `H` and ghost operator `N_hat` minimal. At `Lambda=0` and leading flat kernel,

- ghost Green denominator: `1/k^2`;
- graviton Green denominator: `1/k^2` times a symmetric-tensor projector;
- the species difference therefore survives in tensor numerators/projectors, not in the scalar denominator location.

## Cyclic trace reduction

Treat `Y` as a local factor in the frozen flat-kernel denominator bookkeeping. Under a cyclic trace, the two ghost Green functions adjacent across a local `Y` insertion lie on the same loop-momentum segment.

This gives the following scalar denominator topology.

### `Tr U1`

One `V2` insertion and one closed ghost segment with power two.

This one-EOM sector by itself is not the final `R^3` object; Iteration 243 requires two more background-curvature dressings.

### `Tr U2`

Two `V1` insertions with one graviton segment and one doubled ghost segment:

`I_(1,2)` up to cyclic labeling.

At total `R^3`, one further background-curvature dressing is required.

### `Tr U1^2`

Two `V2` insertions and two doubled ghost segments:

`I_22`.

Again one additional background-curvature dressing is needed for total `R^3`.

### `Tr U1^3`

Three linear `V2` insertions. Between each neighboring pair lies a doubled ghost segment:

`I_222`.

This is a one-loop **triangle with raised propagator powers**, not a six-vertex polygon.

### `Tr(U1 U2)`

Three background insertions: one `V2`, two `V1`. The loop segments are

- doubled ghost;
- one graviton;
- doubled ghost.

Scalar denominator family:

`I_212`

up to cyclic labeling.

This is a mixed ghost–graviton one-loop triangle.

## Why no polygon beyond a triangle is needed at `R^3`

Iteration 243 already proved that total curvature order is bounded by three. Every extra curvature dressing is a local background insertion. Therefore the full one-loop `R^3` problem has at most three independent external background insertions around the loop.

Repeated Green functions increase **denominator powers**, but do not increase the number of distinct external-momentum corners.

Hence the scalar integral family required for the finite-cubic target is at most:

- tadpole/local one-insertion structures;
- two-point bubbles with raised powers;
- three-point triangles with raised powers.

No box, pentagon, hexagon or higher one-loop scalar topology is required by the Vilkovisky connection sector at this curvature order.

## Relation to generic CPT3

Generic covariant perturbation theory already supplies finite nonlocal one-loop form factors for minimal differential-operator determinants through third curvature order.

The connection sector is not automatically equal to those determinant form factors because `U1,U2` are composite inverse-operator structures. However, at the scalar-integral level their flat-kernel cubic pieces belong to the same one-loop triangle kinematics, with raised propagator powers. These admit standard Feynman-parameter representations and can be treated as parameter moments / raised-index relatives of the ordinary massless triangle family.

Thus the missing problem is no longer a new loop topology. It is:

1. tensor numerator/projector algebra;
2. curvature dressing of the lower-EOM sectors;
3. assembly into gauge-safe invariant form factors;
4. causal/source-completed projection into frozen `T_cut`.

## Additional simplification at cubic EOM degree

At `e=3,c=0`, all propagators are taken at their flat values and only the **linear-curvature** parts of `V1` and `V2` contribute. The quadratic-curvature terms explicitly present in Eq. (56) would raise the total order beyond `R^3` and must be dropped in this sector.

Therefore the first executable symbolic subproblem is completely finite:

- standard linear metric parametrization may be used as a computational coordinate only if the unique-action parametrization-independence check is retained;
- `D=4`, `Lambda=0`, `a=-1/2`;
- flat ghost propagator;
- flat graviton projector;
- linearized `V1` and `V2`;
- two traces `Tr(U1^3)` and `Tr(U1 U2)`;
- one-loop triangle families `I222` and `I212`.

## New scoped results

- `C5-CUT-028 — VD_CUBIC_U1CUBED_REDUCES_TO_RAISED_GHOST_TRIANGLE_I222`.
- `C5-CUT-029 — VD_CUBIC_U1U2_REDUCES_TO_MIXED_RAISED_TRIANGLE_I212`.
- `C5-CUT-030 — FINITE_R3_CONNECTION_SECTOR_REQUIRES_NO_ONE_LOOP_POLYGON_BEYOND_TRIANGLE`.
- `C5-NG-022 — COMPOSITE_VD_NONLOCALITY_IS_TENSOR_MASTER_MAP_PROBLEM_NOT_NEW_LOOP_TOPOLOGY`.
- `NG-FUNNEL-099 — SCOPED_FLAT_E3_SYMBOLIC_C5_RUN_NOW_AUTHORIZED`.

## Classification

`PASS_COMPOSITE_TRACE_MASTER_TOPOLOGY_REDUCTION`.

## Compute authorization

A **full** finite-CPT3 calculation remains premature because `e=1,2` curvature dressing and final source projection are not yet frozen.

A **scoped flat `e=3` symbolic calculation is now authorized**. It cannot by itself be promoted as the full C5 comparator; it is a component/unit block.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next gate — Iteration 246

Freeze the explicit flat-space cubic numerator block:

1. choose the standard linear quantum-metric coordinate only as a computational parametrization and state the parametrization-independence unit test;
2. specialize the published `V1,V2` formulas to `D=4`, `Lambda=0`, `gamma1=1`, `gamma2=0`;
3. freeze `K^{-1}=2 delta_sym - eta eta`, ghost numerator and momentum-flow convention;
4. derive the linear-curvature momentum-space vertices;
5. contract the two cubic traces into tensor triangle numerators before integration;
6. check transversality/Ward structure and parametrization-coordinate independence on a second admissible `(gamma1,gamma2)` choice before any physical claim.
