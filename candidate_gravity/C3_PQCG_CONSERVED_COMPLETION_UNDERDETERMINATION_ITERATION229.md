# Candidate Gravity — Iteration 229: C3 conserved-completion underdetermination certificate

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Purpose

Start from the declared PRX-2026 Eq.-(26) metric-dependent generalized Wheeler-DeWitt parent and test the exact Iteration-228 gate: does conservation/Bianchi projection uniquely determine the first nonlinear conserved response kernel around Minkowski, without adding a new model choice?

Answer: **no**. Conservation fixes only an inhomogeneous divergence equation. A nontrivial homogeneous doubly-transverse `O(h)` family remains, can preserve the linear two-point authority, and can survive TT soft perturbations. This is a formal underdetermination certificate.

No C3 zero-fill, no `ANSATZ-003`, no Fisher/resources.

## Authority and literature check

Freshly rechecked:

1. J. Oppenheim and Z. Weller-Davies, *Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time*, Phys. Rev. X 16, 031007 (2026), published 15 July 2026, DOI `10.1103/2rcd-dzcf`. Eq. (26) fixes the metric-dependent generalized Wheeler-DeWitt tensor density used by the declared parent.
2. J. Oppenheim and M. Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:`2605.05375` (6 May 2026). Appendix A explicitly distinguishes the non-conserved DeWitt choice from a conserved diffusion matrix and, at linear level, uses transverse Barnes-Rivers projectors. The paper states that the conserved choice restores the OM/JD two-point agreement, while gauge-fixing freedom can drop out when saturated by conserved tensors.

This supports the precise gate tested here: published linear conserved authority does not by itself select a unique nonlinear completion.

## Frozen Eq.-(26) expansion

Use

`D0^{munu,rhosigma}(g) = c (-g)^(-1/2) [g^{murho}g^{nusigma}+g^{musigma}g^{nurho}-2 beta g^{munu}g^{rhosigma}]`,

with `c=1/(8 D2)`, `g_{munu}=eta_{munu}+h_{munu}`, signature `(-,+,+,+)`, and indices on `h` raised with `eta` at this order.

Then

`g^{munu}=eta^{munu}-h^{munu}+O(h^2)`

and

`(-g)^(-1/2)=1-(1/2) h+O(h^2)`.

Therefore the ordinary first metric variation is fixed:

`delta D0 = c[-(1/2) h B0 - h^{murho}eta^{nusigma} - eta^{murho}h^{nusigma} - h^{musigma}eta^{nurho} - eta^{musigma}h^{nurho} + 2 beta(h^{munu}eta^{rhosigma}+eta^{munu}h^{rhosigma})]`,

where

`B0 = eta^{murho}eta^{nusigma}+eta^{musigma}eta^{nurho}-2 beta eta^{munu}eta^{rhosigma}`.

This confirms the Iteration-228 correction: the ordinary `O(h)` metric dependence is not a free `lambda` once Eq. (26) is frozen.

## Conservation equation and homogeneous sector

For the physical response kernel, conservation around Minkowski has the schematic first-order form

`k_mu delta Dc^{munu,rhosigma}(k,k') = S_L^{nu,rhosigma}[h;Dc^(0)]`,

and analogously on the second index pair with momentum `k'`. The source terms contain the variation of the covariant divergence/connection and any declared projection prescription.

If `delta Dc_part` is one particular solution, then

`delta Dc = delta Dc_part + H`

is equally conserved for every `H` satisfying

`k_mu H^{munu,rhosigma}=0`,

`k'_rho H^{munu,rhosigma}=0`.

The crucial question is whether a nonzero `O(h)` `H` exists that also leaves the frozen linear two-point sector untouched. It does.

Define

`Q_k^{munu}=k^2 eta^{munu}-k^mu k^nu`,

so `k_mu Q_k^{munu}=0`, and similarly for `k'`.

Let `R1_{abcd}[h](q)` be the linearized Riemann tensor of the soft perturbation and define a scalar curvature dressing

`S_R[h;q,u,v] = u^a v^b u^c v^d R1_{abcd}[h](q)`.

For arbitrary symmetric scalar form factor `F(k,k',q)`, the family

`H^{munu,rhosigma} = lambda F S_R Q_k^{munu} Q_k'^{rhosigma}`

is:

- `O(h)` and therefore vanishes on the Minkowski background;
- transverse in both response-index pairs;
- linearly diffeomorphism invariant through the linearized Riemann dressing;
- compatible with pair symmetry after choosing/symmetrizing `F`;
- invisible to the background linear two-point diffusion kernel;
- generically nonzero on TT perturbations.

Thus `lambda` and, more generally, `F` are not fixed by conservation/Bianchi plus the Eq.-(26) background parent.

## Explicit TT-survival certificate

The reproducible script

`candidate_gravity/code/iteration229_c3_conserved_completion_ambiguity.py`

uses a null soft momentum `q=(1,0,0,1)` and plus TT polarization `h_xx=1`, `h_yy=-1`. It verifies

- `q^mu h_{munu}=0` exactly;
- `h=0` exactly;
- a curvature contraction `S_R=-2`, hence the homogeneous family is not annihilated by TT;
- exact transversality of `Q_k` and `Q_k'` for two generic response momenta;
- exact left/right divergence zero for the explicit nonzero `H`;
- nonzero Frobenius norm `||H||=198.030300711785` for the representative `lambda F=1`.

Result authority:

`candidate_gravity/results/iteration229_c3_conserved_completion_ambiguity.json`.

The numerical representative is only a concrete witness; the underdetermination is analytic because the family exists for arbitrary `lambda F`.

## Why an ultralocality objection does not restore uniqueness automatically

The linear conserved construction in arXiv:`2605.05375` is itself expressed with transverse Barnes-Rivers projectors. Such projectors contain longitudinal inverses in momentum/position-space language. Therefore excluding the homogeneous family by imposing a new strict ultralocal completion rule would be an additional model assumption, not a consequence of Eq. (26) plus conservation alone.

A unique nonlinear completion could still exist if the parent theory supplies an extra principle — e.g. a specific nonlinear stochastic equation, a fixed covariant projector/Green-function prescription with boundary conditions, or a derived quotient-space measure that removes the homogeneous sector. None of those has yet been established as same-parent RQIR authority.

## Classification

Primary result:

`FORMAL_UNDERDETERMINATION_CERTIFICATE`

C3 status remains:

`BLOCKED_C3_CTP_ORDERED_COMPLETION`

with refined sub-classification:

`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`.

This is **not** a consistency FAIL of PQCG, not an exact comparator identity, not a near-degeneracy statement, not evidence that the C3 column is zero, and not Candidate Gravity novelty.

## New retained labels

- `C3-NG-009 — CONSERVATION_BIANCHI_DOES_NOT_UNIQUELY_FIX_THE_FIRST_NONLINEAR_CONSERVED_RESPONSE_COMPLETION`.
- `C3-NG-010 — AN_EXPLICIT_OH_DOUBLY_TRANSVERSE_HOMOGENEOUS_FAMILY_LEAVES_LINEAR_TWO_POINT_AUTHORITY_UNCHANGED`.
- `REL-NG-009 — A_CURVATURE_DRESSED_HOMOGENEOUS_COMPLETION_CAN_SURVIVE_TT_SOFT_PROJECTION`.
- `C3-BLOCK-003 — C3_REQUIRES_AN_ADDITIONAL_NONLINEAR_COMPLETION_PRINCIPLE_BEYOND_EQ26_PLUS_CONSERVATION`.
- `NG-FUNNEL-085 — FORMAL_COMPARATOR_UNDERDETERMINATION_IS_A_NEGATIVE_RESULT_NOT_A_CANDIDATE_NOVELTY_CERTIFICATE`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 228.

Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The C3 blocker became stronger and more formal, but the C3 comparator coordinate did not close, so no rubric block is awarded.

## Exact next gate

Iteration 230 should test whether the **declared parent literature itself** supplies an additional nonlinear completion principle that removes this homogeneous family without a new model choice. Specifically audit for a same-parent nonlinear conserved stochastic equation / covariant transverse projector / quotient-space construction with fixed Green-function and boundary prescription. If no such authority exists, freeze C3 as `BLOCKED_FORMAL_UNDERDETERMINATION` for the current comparator funnel and move to the remaining C5/AS linked-relation closure rather than inventing a C3 column. If such a prescription exists, derive its cubic response vertex in the same `beta,D2` convention and test whether the Iteration-229 `H` family is genuinely excluded before any soft-row evaluation.
