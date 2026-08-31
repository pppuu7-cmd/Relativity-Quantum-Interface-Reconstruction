# RQIR Research Log — Iteration 160

**Date:** 2026-08-31  
**Front:** Candidate Gravity comparator funnel  
**MODEL_READINESS: 22%**

## Question

Iteration 159 froze a concrete asymptotic-safety comparator but classified the required six-probe ordered response as BLOCKED because the published symmetric-point Euclidean TT three-graviton dressing is not the full off-symmetric Lorentzian retarded vertex.

Iteration 160 audited whether the reconstructed covariant effective action in the same primary source removes the off-symmetric data obstruction.

## Primary-source finding

Pawlowski & Tränkle, arXiv:2309.17043v2 / Phys. Rev. D 110, 086011 (2024), reconstruct a diffeomorphism-invariant **Euclidean** background effective action from momentum-dependent graviton correlation functions. The curvature expansion is retained through second order with covariant momentum dependence:

`Gamma[g] = ... + R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn`.

Therefore the paper contains more information than the one-variable symmetric-point TT dressing alone. Within the frozen curvature-squared truncation, functional differentiation of the reconstructed action can in principle determine off-symmetric **Euclidean** background vertices.

This refines Iteration 159 rather than overturning it.

## Reproducible form-factor coverage audit

Created:

- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`.

The script records the Appendix-H analytic fit coefficients and evaluates them independently on each individual leg of the six frozen spacelike RQIR triplets from Iteration 149.

With the flat-space spacelike Euclidean coverage map `p_E=sqrt(k_L^2)`, all 18 legs return finite values.

Ranges:

- `f_Ricci2`: `-0.04680592285494515 ... -0.0037039902546036896`;
- `f_R2`: `0.261312950235091 ... 0.6649777144616807`.

These values are **not** treated as real-time response values. They establish only that the published action-level fit data cover the frozen spacelike momentum magnitudes used by RQIR.

## Causal-completion audit

The source reconstructs the Euclidean action first and then performs a Wick rotation to a Lorentzian d'Alembertian. For nonlocal inverse operators, the Lorentzian theory requires a Green function. The paper explicitly discusses this Green-function issue and gives an expansion around a flat-space Feynman propagator as one possible construction, while leaving a thorough analysis beyond its scope.

RQIR ordered response requires a different level of specification:

- a real-time in-in / Schwinger-Keldysh definition;
- retarded Green functions in the same source/state convention;
- source-completed nonlinear response on the six triplets.

RQIR cannot silently replace a Feynman or unspecified Green function by a retarded one.

## Retained result

### AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED

The frozen AS curvature-squared effective action supplies sufficient action-level data for off-symmetric Euclidean reconstruction in principle. The remaining blocker is the absence of a uniquely fixed RQIR retarded/in-in Green-function prescription for the nonlocal Lorentzian operators.

Classification:

`BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

This is not a consistency FAIL, zero-response statement, or theory-identity result.

## New funnel rule

### NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION

A Euclidean nonlocal effective action does not by itself define an ordered real-time observable. The Green-function/contour prescription is part of the physical model and must be frozen before `chi^(n)R`, Fisher or novelty quotient calculations.

## Candidate-design implication

This rule applies symmetrically to our future Candidate Gravity. If `ANSATZ-003` contains nonlocal operators, its parent dynamics must generate/fix the real-time retarded/CTP prescription. A convenient post-hoc Green-function choice is not admissible.

## Readiness

`MODEL_READINESS: 22%` — unchanged from Iteration 159.

Reason: the AS comparator specification is materially sharper and Euclidean action coverage is established, but no new **usable retarded comparator tangent** has entered the complete quotient.

Accounting remains:

- comparator foundation 19/25;
- robust unique residual 3/20;
- parent dynamics 0/20;
- consistency 0/15;
- Fisher 0/10;
- resources 0/10.

## Next gate — Iteration 161

Use the **local IR derivative expansion** of the same AS effective action, where a standard local source-completed retarded interpretation is available under the frozen C5 convention, and test whether these AS IR directions are contained in the local C5 EFT comparator span.

Do not assign a causal completion to the genuinely nonlocal AS sector by fiat.
