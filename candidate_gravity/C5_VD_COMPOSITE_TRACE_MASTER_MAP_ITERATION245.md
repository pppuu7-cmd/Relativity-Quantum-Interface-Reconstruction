# RQIR Candidate Gravity — Vilkovisky Composite-Trace Master Map

**Iteration:** 245  
**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Scope

Continue the selected C5 authority-improvement route from the exact Iteration-244 insertion identity. Frozen target: pure Einstein gravity, 4D, Minkowski expansion, `Lambda=0`, one loop, finite effective action through total curvature order `R^3`. No `ANSATZ-003`; no Fisher/resources.

## Primary operator authority

Cho–Kantowski general gauge-theory reduction defines, in condensed notation,

`U1^mu_nu = N^{mu gamma} Q^k_gamma Q^i_{alpha;k} E_i N^{alpha beta} c_{beta nu}`

and

`U2^mu_nu = N^{mu gamma} Q^i_{gamma;j} E_i G^{jk} Q^l_{alpha;k} E_l N^{alpha beta} c_{beta nu}`,

where `E_i=S_,i`, `N` is the ghost Green operator and `G` the gauge-fixed field/graviton Green operator. These definitions precede the Kaluza–Klein specialization and are the same reduced VD algebra whose series was fixed in Iteration 244.

For the frozen 4D gravity convention, the local graviton and ghost operators are already fixed by Iteration 232; the remaining task is evaluation of these nonlocal composite traces, not a new gauge choice.

## Primitive inverse-operator count

Before any Ward identity, integration by parts or numerator cancellation, define

`nu(T) = (n_N, n_G)`

as the number of explicit ghost and graviton Green operators in a trace monomial. Then

- `nu(U1)=(2,0)`;
- `nu(U2)=(2,1)`.

Additivity under products gives

- `Tr U1`: `(2,0)`;
- `Tr U2`: `(2,1)`;
- `Tr U1^2`: `(4,0)`;
- `Tr U1^3`: `(6,0)`;
- `Tr(U1 U2)`: `(4,1)`.

This is a structural correction to any shorthand that labels the sectors merely by one/two/three propagators according to EOM degree. Such a shorthand is not authority-preserving before explicit operator reduction.

## Curvature-order requirements

Iteration 243 proved `e+c<=3`, with `e` the explicit EOM degree and `c` additional curvature dressing. Therefore the finite cubic target requires only

- `Tr U1` through extra dressing `c<=2`;
- `Tr U2` and `Tr U1^2` through `c<=1`;
- `Tr U1^3` and `Tr(U1 U2)` at leading flat-kernel order `c=0`.

No `e>=4` insertion sector is required.

## CPT3 applicability audit

Barvinsky–Vilkovisky covariant perturbation theory through third order supplies the nonlocal heat-kernel/effective-action form factors for a generic single Laplace-type differential operator in terms of its background curvatures and potential. That authority is sufficient for the determinant/minimal-operator sector after the operator convention is fixed.

It does **not by itself** evaluate the VD composite traces above, because they contain explicit products of inverse operators and, in `U2`, mixed inverse operators acting on different bundles (ghost vector and graviton symmetric-tensor sectors). Treating these composite traces as though they were ordinary single-operator CPT3 coefficients would splice distinct objects and is forbidden.

Classification:

`NO_DIRECT_SINGLE_OPERATOR_CPT3_IDENTITY_FOR_COMPOSITE_U1_U2_TRACES`.

This is not a consistency FAIL and not proof that the traces are unavailable.

## Executable replacement: finite Minkowski resolvent expansion

The frozen target is a perturbative Minkowski expansion, so a fully covariant mixed heat-kernel formalism is not mandatory. Once the same-parent VD operators are fixed, expand their inverses around the flat minimal operators:

`N^{-1}=N0^{-1}-N0^{-1} dN N0^{-1}+N0^{-1} dN N0^{-1} dN N0^{-1}-...`

and

`G=G0-G0 dH G0+G0 dH G0 dH G0-...`.

Expand `Q_;`, `E` and local metric factors in the same background-field convention. Truncate strictly by `e+c<=3`.

Consequences:

1. every required composite contribution reduces to a finite set of **one-loop** flat-space tensor integrals with one loop momentum;
2. the apparent many-propagator chains are not extra loops; they are repeated denominators/projector chains in a single trace;
3. the cubic EOM terms `Tr U1^3` and `Tr(U1 U2)` need only the flat kernels `N0^{-1},G0` and the leading linearized EOM/gauge-generator vertices;
4. lower-EOM sectors require only a finite number of `dN,dH,dQ,dE` insertions determined by the curvature-order table above.

Thus the Iteration-244 blocker is narrowed again. The missing object is no longer a generic finite-CPT3 master formula for arbitrary composite traces; it is the explicit frozen 4D Einstein **resolvent vertex library and tensor reduction** needed to evaluate those traces and then project to the source-completed causal comparator.

New blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_AND_SOURCE_PROJECTION`.

`BLOCKED_NOT_ZERO`.

## Heavy-compute decision

A blind full CPT3 tensor contraction remains forbidden. A bounded symbolic computation is now scientifically authorized once it implements exactly the frozen flat `N0,G0,Q,E` convention and records the resolvent insertion order. This is upstream of any Fisher/resources work.

## New scoped results

- `C5-CUT-028 — U1_U2_PRIMITIVE_INVERSE_OPERATOR_CONTENT_FROZEN_FROM_PRIMARY_VD_AUTHORITY`.
- `C5-NG-022 — EOM_DEGREE_IS_NOT_PROPAGATOR_COUNT_FOR_VD_COMPOSITE_TRACES`.
- `C5-NG-023 — SINGLE_OPERATOR_CPT3_DOES_NOT_DIRECTLY_EVALUATE_MIXED_U1_U2_COMPOSITE_TRACES`.
- `C5-CUT-029 — FINITE_R3_MINKOWSKI_TARGET_REDUCES_COMPOSITE_VD_SECTOR_TO_FINITE_FLAT_RESOLVENT_EXPANSION`.
- `NG-FUNNEL-099 — C5_BLOCKER_NARROWED_TO_4D_EINSTEIN_RESOLVENT_VERTEX_LIBRARY_AND_SOURCE_PROJECTION`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 244. The C5 route became explicitly executable in finite perturbative pieces, but the comparator coordinate itself is not yet computed; no readiness rubric block closes.

## Next gate — Iteration 246

Derive and freeze the leading flat-space 4D pure-Einstein kernels in the exact Iteration-232 convention:

1. `N0^{-1}` and `G0` projectors/normalization;
2. linearized `E_i[h]` and the needed `Q^i_{alpha;j}` vertices;
3. construct `U1^(1)` and `U2^(2)` as momentum-space kernels;
4. reproduce the known quadratic VD connection contribution/divergence as a mandatory normalization test before using the cubic terms;
5. only after that generate the flat `Tr U1^3` and `Tr(U1 U2)` tensor integrands and test Ward/source compatibility.
