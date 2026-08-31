# RQIR Candidate Gravity — Iteration 180

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

What is the strongest finite C4 ordinary-quantum-mediator control that is physically compatible with the same null-soft spin-2 `B_T` observable after Iteration 179 showed that fixed nonzero-mass dRGT is not compatible with that soft pole?

## Scoped control

Freeze the control class narrowly enough to be finite and physically meaningful:

- one local unitary massless spin-2 field;
- conserved stress-tensor source;
- universal coupling required by soft-gauge consistency;
- self-consistent nonlinear parent dynamics rather than a linear mediator plus independently tuned cubic vertex;
- local EFT corrections through the same frozen dimension-12 order relevant to the Iteration-178 `B_T` basis.

This is a deliberately strong C4 control. It does **not** represent all possible hidden sectors or all non-gravitational mediators.

## Consistency boundary

Massless spin-2 soft consistency strongly constrains this control. Soft-gauge arguments require universal coupling of a physical massless spin-2 state, while consistent two-derivative self-interaction/deformation results return Einstein-type nonlinear sectors under the standard assumptions. Local EFT operators can first modify the sub-subleading soft-graviton structure; these are precisely the kind of local higher-curvature directions already admitted in C5.

Literature anchors:

- Cachazo & Strominger, arXiv:1404.4091;
- Elvang, Jones & Naculich, arXiv:1611.07534;
- Hertzberg & Sandora, arXiv:1704.05071;
- Deser, arXiv:0910.2975;
- Boulanger, Damour, Gualtieri & Henneaux, arXiv:hep-th/0009109.

The scoped operational conclusion is therefore not that a hidden field is metaphysically "gravity". It is that once its massless spin-2 parent dynamics, source coupling and local EFT freedom coincide with the C5 massless-spin-2 boundary, the label `ordinary mediator` supplies no independent RQIR tangent.

## Finite `B_T` certificate

At the frozen dimension-12 local order the strongest compatible C4 massless-spin-2 control is represented by the same four physical soft-transverse basis vectors found for C5 in Iteration 178:

`Riemann3 * {1, (-q^2), (q^2)^2, (-q^2)^3}`

(up to fixed normalization).

Therefore

`rank(V_C5)=4`,

`rank(V_C4_massless)=4`,

`rank([V_C5,V_C4_massless])=4`,

and the residual of the C4 boundary after projection onto C5 is exactly zero by the frozen boundary construction.

Classification:

`SCOPED_EXACT_BOUNDARY_MERGER_WITH_C5_LOCAL_MASSLESS_SPIN2_EFT`.

This is an exact comparator-boundary identity within the declared assumptions/order. It is not a theorem excluding all C4 models.

## Retained results

### `C4-NG-011 — CONSISTENT_LOCAL_MASSLESS_SPIN2_MEDIATOR_CONTROL_MERGES_WITH_C5_SOFT_BOUNDARY_AT_FROZEN_ORDER`

A C4 control that genuinely shares the same physical massless spin-2 soft state and the required consistent local parent dynamics adds no independent `B_T` direction beyond C5 at the frozen local EFT order.

### `SOFT-NG-007 — SEMANTIC_GRAVITY_VS_MEDIATOR_LABEL_IS_NOT_AN_OPERATIONAL_DISCRIMINATOR_WHEN_PARENT_DYNAMICS_AND_SOURCE_MAP_COINCIDE`

RQIR compares observables and dynamics, not names assigned to an otherwise identical massless-spin-2 sector.

### `NG-FUNNEL-038 — C4_NULL_SOFT_CONTROL_SPLITS_INTO_PROTOCOL_INCOMPATIBLE_MASSIVE_CASE_OR_C5_BOUNDARY_MASSLESS_CASE_UNDER_SCOPED_ASSUMPTIONS`

For the currently frozen controls, nonzero-mass dRGT is physically incompatible with the null-soft carrier, whereas the strongest consistent local massless-spin-2 control merges with the C5 boundary.

## Scope guard

Do not generalize this to scalar/vector hidden mediators, nonlocal mediator sectors, multiple-field constructions, Lorentz-violating models, nonunitary models or models with different source/transduction maps. Such models must be tested separately if they can reproduce the exact physical tensor observable.

## Readiness

`MODEL_READINESS: 24%`, unchanged.

C4 is substantially clarified in this `B_T` protocol, but the remaining comparator foundation still includes the fixed nonlocal projection, asymptotic-safety real-time transverse completion and the C3 ordered/transverse boundary.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Next gate

Iteration 181 should project the already-fixed `QG-NL-EXP-001` covariant nonlocal parent action into the exact same six null-soft TT `B_T` rows, including its Frechet operator insertion rather than using propagator-only reasoning. Determine whether it enlarges the current C5 rank-4 span toward rank 5 or 6, or is absorbed by the finite local basis on these rows.
