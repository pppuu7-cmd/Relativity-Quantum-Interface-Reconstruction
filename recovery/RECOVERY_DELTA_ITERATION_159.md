# Recovery Delta — RQIR Iteration 159

**Date:** 2026-08-31  
**Authoritative change:** first concrete asymptotic-safety FRG comparator frozen; exact RQIR mapping boundary identified at off-symmetric Lorentzian retarded three-graviton response.  
**MODEL_READINESS: 22%**

## Previous front

Iteration 158 fixed `NL-WNL-001`, the first weakly-nonlocal comparator sub-block, and introduced the stable readiness rubric. It left the form-factor-induced cubic response BLOCKED and preferred one concrete asymptotic-safety vertex truncation as the next independent comparator step.

## New comparator

`AS-FRG-TT-001`, based on Pawlowski & Tränkle, arXiv:2309.17043, with supporting vertex-expansion literature arXiv:1612.07315 and analytic-continuation cross-check arXiv:2603.10168.

The fixed published content includes:

- Euclidean TT two-point momentum dependence;
- TT three-/four-point information at momentum-symmetric configurations;
- reconstructed diffeomorphism-invariant curvature form factors.

## Mapping audit

The RQIR nonlinear protocol requires six unequal off-shell triplets `(p,q,r)` and ordered Lorentzian retarded `chi2R` with source completion.

The published one-variable symmetric-point coefficient `gamma_g^(3)(p)` does not determine the full off-symmetric `Gamma_3(p,q,r)` on these six triplets. Euclidean data also do not by themselves select the required retarded `i0` prescription.

Therefore a numerical `V_AS^(chi2R)` cannot be constructed without adding an interpolation/continuation convention not fixed by the comparator.

## New retained result

`AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`.

Classification: `OPERATIONAL_BLOCKED / PROTOCOL_MISMATCH`.

Retain:

`NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

This is not a consistency FAIL, exact identity, near-degeneracy, or zero response.

## Supplemental Iteration-158 diagnostic

A separately instantiated exponential nonlocal linear TT diagnostic (`QG-NL-EXP-001`) showed that if the full dimension-12 local C5 quadratic TT directions plus common gain are admitted on exactly six linear probe coordinates, the finite base is rank `6/6`. This is protocol saturation and reinforces that the `NL-WNL-001` gain-only linear residual from Iteration 158 is not a novelty certificate. These supplemental files are not the authoritative Iteration-158 comparator definition.

## BLOCKED

- AS six-probe `chi2R_even/odd`;
- AS source-completed nonlinear Ward test;
- AS `N2/C3sym`;
- full AS quotient;
- nonlocal form-factor-induced cubic response;
- several internal C3/C4/C5 sectors.

No `ANSATZ-003`; no Fisher/resources.

## Readiness

`MODEL_READINESS: 22%`

No change from Iteration 158. The AS comparator is concretely specified, but the exact post-Gaussian map needed to close its comparator span is still blocked. Stable rubric remains: comparator foundation `19/25`, unique residual discovery `3/20`, all later blocks `0`.

## Exact restart instruction — Iteration 160

Audit the reconstructed covariant form factors/effective action in arXiv:2309.17043 for sufficient action-level information to derive the required off-symmetric cubic TT vertex directly. If the action reconstruction is sufficient, derive the vertex and define the source-completed retarded continuation on the six frozen triplets. If not, record `BLOCKED_AS_ACTION_DATA_INSUFFICIENT` and do not invent the missing vertex. In parallel, preserve the distinction between gain-only nonlocal residuals and residuals after the full local C5 quadratic quotient.
