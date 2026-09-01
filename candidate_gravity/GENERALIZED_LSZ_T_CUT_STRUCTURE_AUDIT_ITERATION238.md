# Candidate Gravity — Iteration 238: generalized-LSZ causal-response vs frozen `T_cut` structure audit

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Starting authority

Started from repository authority at Iteration 237 after reading:
- `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
- `recovery/RECOVERY_DELTA_ITERATION_237.md`;
- `research_log/2026-09-01_iteration_237_onshell_retarded_observable_identity_audit.md`;
- recent commits through `21439cf9ab8df318f94c4eeefaa635bfa19036d3`;
- current Actions state: no workflow runs.

The unchanged frozen observable from Iteration 205 is

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`,

where `Gamma3_ret,soft` is the source-completed amputated retarded **three-point gravitational response**, `K2` is the same-parent inverse **two-point gravitational kernel**, and `W` is the corresponding Ward/soft map.

Iteration 237 established that a single in-out `2 -> 3` discontinuity is not the complete causal radiation observable. The present iteration tests whether the *completed* generalized-LSZ response has the same functional structure as frozen `T_cut`.

## Fresh causal-response authority

The relevant published authority is:

1. S. Caron-Huot, M. Giroux, H. S. Hannesdottir, S. Mizera, JHEP 01 (2024) 139, arXiv:2308.02125. Asymptotic radiation observables are in-in observables computable either by generalized LSZ or by amplitudes plus products/cuts of amplitudes. Their one-loop gravitational-radiation example explicitly shows that the cut term changes the causal prescription and restores retarded propagation.
2. S. Biswas, J. Parra-Martinez, JHEP 07 (2025) 037, arXiv:2411.09016. Classical asymptotic observables are obtained from a particular soft limit of **five-point amputated causal response functions** in the Schwinger-Keldysh basis; the paper computes the radiated waveform and related observables in that framework.
3. D. Bini et al., Phys. Rev. D 109, 125008 (2024), arXiv:2402.06604. The one-loop gravitational waveform contains a five-point amplitude contribution plus a distinct unitarity-cut contribution.

These results materially settle the valence/observable question.

## Functional-valence audit

For the minimally coupled massive-scalar GR branch, the generalized-LSZ causal radiation object has the schematic amputated structure

`R5_ret ~ < phi phi ; h_rad ; phi phi >_causal,amp`,

or, in effective-action/source language, a mixed functional derivative with four matter-source/external scalar legs and one radiative metric leg. The causal completion can be represented by amplitude plus cut/product terms, but that completion does **not** change the number or species of external legs.

The frozen RQIR object instead requires

`Gamma3_ret ~ delta^3 Gamma / delta h delta h delta h`

with source/Ward completion in one gravitational field convention, together with

`K2 ~ delta^2 Gamma / delta h delta h`.

Therefore the generalized-LSZ massive-scalar radiation response and frozen `Gamma3_ret` do not live in the same functional derivative sector:

- causal radiative branch: `phi phi phi phi h` (five-point mixed response);
- frozen nonlinear gravity coordinate: `h h h` linked to `h h`.

This mismatch remains after LSZ amputation, after adding the required cut/product terms, and after taking the soft emitted-graviton limit. Soft factorization relates the five-point observable to lower-point **matter scattering** data; it does not by itself convert the four scalar legs into two additional metric legs or turn the lower-point scalar amplitude into the metric inverse kernel `K2`.

## Missing map that would be required

To identify the two objects one would need an extra same-parent, source-complete reduction rule of the form

`R5_ret[phi phi -> phi phi + h]  ->  Gamma3_ret[h,h,h]`

and simultaneously

`A4[phi phi -> phi phi]  ->  K2[h,h]`

with all normalizations, contact terms, Ward identities, boundary conditions and IR prescriptions fixed uniquely.

No such identity follows from generalized LSZ, the gravitational soft theorem, KMOC, or the cited causal-response construction. Introducing one by integrating out or replacing the matter sources would define an additional comparator/source model and would violate the frozen no-post-hoc-redefinition rule unless independently derived and frozen beforehand.

## Result

The Iteration-236/237 massive-scalar branch is executable as a physical causal observable, but it is **structurally comparator-incompatible with the unchanged frozen `T_cut` target**.

Freeze:

`CAUSAL_RESPONSE_BRANCH_PHYSICALLY_VALID_BUT_T_CUT_VALENCE_INCOMPATIBLE`

and

`BLOCKED_COMPARATOR_INCOMPATIBLE_FUNCTIONAL_VALENCE_MIXED_PHI4H_VS_H3_LINKED_H2`.

This closes the Iteration-238 identity audit negatively.

## Scoped claims

### `REL-NG-018 — GENERALIZED_LSZ_CAUSAL_COMPLETION_DOES_NOT_CHANGE_EXTERNAL_FIELD_VALENCE`

Amplitude-plus-cut completion restores the correct in-in/retarded observable but does not turn the mixed five-point `phi^4 h` response into a pure-gravity `h^3` response.

### `REL-CUT-018 — MASSIVE_SCALAR_CAUSAL_RADIATION_IS_EXECUTABLE_BUT_NOT_THE_FROZEN_LINKED_GRAVITY_CUT_COORDINATE`

The branch remains scientifically useful as a physical control but cannot populate frozen `T_cut` without a new reduction model.

### `REL-BLOCK-003 — FROZEN_T_CUT_REQUIRES_H3_LINKED_TO_H2_NOT_PHI4H_LINKED_TO_PHI4`

The exact blocker is functional-sector mismatch, not absence of causal perturbation theory.

### `NG-FUNNEL-094 — PHYSICAL_ONSHELL_OR_ININ_EXECUTABILITY_IS_INSUFFICIENT_WHEN_OBSERVABLE_IDENTITY_FAILS`

A calculable observable from the same Lagrangian is not automatically a valid comparator coordinate if it is not the same frozen functional observable.

## Classification guardrails

This is:
- a **comparator-incompatibility / observable-identity negative result**;
- not a consistency FAIL of GR;
- not an exact comparator identity;
- not regime-specific non-identifiability;
- not near-degeneracy;
- not a zero comparator column;
- not a Candidate Gravity novelty certificate.

No `ANSATZ-003` is created. No Fisher/resources are allowed. No heavy computation is justified because the branch fails an upstream exact observable-identity constraint.

## Readiness

`MODEL_READINESS: 24%`.

Change from Iteration 237: **0 percentage points**. The massive-scalar causal branch is now classified correctly and removed from the promotable `T_cut` path, but no rubric block closes: comparator foundation remains `24/25`, robust unique residual remains `0/20`.

## Exact next gate

Iteration 239 should search only for a branch whose *native* causal functional sector is already `h^3` linked to `h^2` in one convention. Highest priority is perturbative Einstein gravity / gravity EFT in Schwinger-Keldysh or causal-response form with a directly defined retarded three-metric response and same-parent two-point kernel. Do not use matter `2 -> 3` radiation as a proxy again. If no executable pure-gravity causal `h^3` object exists, freeze that route as operationally blocked and reassess whether the linked target itself is presently computable rather than changing it post hoc.