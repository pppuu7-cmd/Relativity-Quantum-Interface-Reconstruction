# RQIR Candidate Gravity — Iteration 179

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

Can the existing fixed C4 comparator `C4-DRGT-001` be projected into the physical null-soft TT `B_T` protocol of Iterations 175–178 without changing its frozen model point?

## Fixed C4 authority

`C4-DRGT-001` is frozen at

`m^2=0.04`, `alpha3=0`, `alpha4=0`,

with massive TT propagators proportional to

`1/(k^2+m^2)`

and cubic TT potential

`V3_dRGT = m^2(3+alpha3)/8 Tr(H^3)`.

The comparator is a ghost-free massive-spin-2 control with five propagating degrees of freedom. Its role is scoped nonlinear C4 comparison; it is not a massless-gravity model.

## Null-soft compatibility test

The current `B_T` carrier was frozen with a physical massless/null soft spin-2 leg

`k_soft=(1,0,0,1)`, `k_soft^2=0`,

and with a Ward/covariantization subtraction appropriate to the same massless soft boundary.

For the fixed dRGT TT inverse kernel,

`K2_dRGT(k_soft)=k_soft^2+m^2=m^2=0.04`,

so the null momentum is **not** a physical dRGT soft pole at the frozen model point.

Therefore the existing physical null-soft `B_T` coordinate is not the same on-shell/soft observable for this fixed massive comparator. A value computed by simply inserting null `k` into the dRGT potential would be an off-shell diagnostic under a different physical boundary, not the frozen comparator column required by the quotient.

Status:

`BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH`.

This is not a consistency FAIL of dRGT, not exclusion of massive gravity, and not a zero comparator column.

## Formal massless boundary is not the same frozen comparator

At fixed `alpha3`,

`V3_dRGT coefficient = m^2(3+alpha3)/8`.

For `alpha3=0`, halving `m^2` halves this coefficient exactly:

`0.015 -> 0.0075 -> 0.00375 -> 0.001875 -> 0.0009375`.

Thus the nonderivative dRGT cubic potential vanishes linearly as `m^2 -> 0`, while the TT propagator approaches the massless EH denominator.

But that formal boundary is not the frozen `m^2=0.04` comparator point and does not authorize using a massless-boundary tangent as the fixed dRGT `B_T` column. In addition, full massive-gravity massless-limit questions involve helicity sectors beyond the scoped TT block and must not be inferred from this calculation.

## Literature consistency

The classification is consistent with standard dRGT authority: ghost-free massive gravity propagates a massive spin-2 multiplet with five degrees of freedom (de Rham, *Living Reviews in Relativity* 17, 7 (2014); see also modern 2026 dRGT propagation analyses). The massless soft-graviton theorem instead constrains amplitudes with an actual massless spin-2 soft state and universal soft pole structure (Cachazo & Strominger, arXiv:1404.4091; Elvang, Jones & Naculich, arXiv:1611.07534).

## Retained results

### `C4-NG-009 — FIXED_NONZERO_MASS_DRGT_COMPARATOR_DOES_NOT_SHARE_THE_PHYSICAL_NULL_SOFT_POLE_OF_THE_B_T_PROTOCOL`

The frozen nonzero-mass dRGT comparator cannot be assigned a physical null-soft `B_T` column without changing the observable/model boundary.

### `SOFT-NG-006 — COMPARATOR_PROTOCOL_MISMATCH_MUST_BE_BLOCKED_NOT_ZERO_FILLED`

A comparator incompatible with the frozen physical soft carrier is `BLOCKED`, not numerically zero.

### `C4-NG-010 — FORMAL_DRGT_MASSLESS_TT_BOUNDARY_REMOVES_THE_NONDERIVATIVE_CUBIC_POTENTIAL_AND_COLLAPSES_TOWARD_THE_SHARED_EH_TT_BOUNDARY`

Within the scoped TT sector, the dRGT-specific nonderivative cubic coefficient vanishes with `m^2`; this is a boundary statement, not an identification of the full massive theory with GR.

## Consequence for the funnel

The two-dimensional complement left after local C5 in Iteration 178 is still not a novelty certificate. The fixed dRGT comparator cannot fill it under the current physical null-soft definition, but that does not remove the whole C4 family.

The next C4 task is to freeze a **compatible massless ordinary-quantum-mediator control** with explicit parent dynamics and source/transduction convention, rather than use a class capability mask. Under standard locality/unitarity assumptions, a genuinely massless interacting spin-2 mediator is tightly constrained by soft-gauge consistency and universal coupling, so its distinction from the C5 gravitational boundary must be stated operationally rather than assumed.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Readiness

`MODEL_READINESS: 24%`, unchanged.

This iteration removes an invalid comparator projection route but does not close the full C4 comparator foundation or produce a unique residual.

## Next gate

Iteration 180 should define the strongest compatible finite C4 massless-mediator control for the same `B_T` observable. If every local/unitary massless spin-2 realization with the required universal stress coupling falls into the same soft/Ward structure already represented by C5 at the frozen order, record that as a scoped comparator-boundary merger; otherwise instantiate its independent transverse columns explicitly.
