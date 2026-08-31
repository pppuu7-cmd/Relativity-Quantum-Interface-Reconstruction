# Candidate Gravity — Iteration 160: asymptotic-safety action / causal-completion audit

**Date:** 2026-08-31  
**Comparator:** `AS-FRG-TT-001`  
**MODEL_READINESS: 22%**  
**Classification:** Euclidean action data `PASS_SCOPED`; RQIR retarded completion `BLOCKED`

## Objective

Iteration 159 established that the published one-variable momentum-symmetric TT three-graviton dressing cannot simply be evaluated as the full off-symmetric Lorentzian `Gamma_3(p,q,r)` required by the six frozen RQIR triplets.

Iteration 160 asks the stronger question:

> Does the reconstructed covariant effective action in Pawlowski & Tränkle contain enough information to derive the off-symmetric vertex without inventing a symmetric-point interpolation?

The answer is **yes in the Euclidean curvature-squared truncation, but no for the final RQIR retarded/in-in completion**.

## 1. Primary-source action data

The fixed source reconstructs a diffeomorphism-invariant Euclidean background effective action in a curvature expansion through second order while keeping covariant momentum dependence. Its relevant structure is

`Gamma[g] = ... + R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn`.

This is stronger information than a single symmetric-point `gamma_g^(3)(p)` curve. Once the action and its form factors are frozen, functional differentiation determines off-symmetric **Euclidean background vertices in principle** within that truncation and within the paper's fluctuation/background reconstruction assumptions.

The source also explains the TT projection logic:

- `R^2` does not overlap the TT graviton propagator or TT three-point function in the declared projection;
- the TT three-point `p^4` contribution fixes the `R_mn^2` form factor;
- the TT four-point information is needed to disentangle `R^2`.

Therefore the Iteration-159 statement `off-symmetric vertex data absent` must be refined: the symmetric-point vertex curve is insufficient by itself, but the reconstructed **action-level** data provide an off-symmetric Euclidean route.

## 2. Frozen Appendix-H form-factor fits

The reproducible audit records the analytic fit forms used by the paper.

For the Ricci-tensor-squared form factor:

`f_Ricci2(p^2) = a0 + sum_i ai / ((p/pi)^2 + 1)`

with

- `a0=-0.023601`;
- `a=(-0.13727, 0.13138, -0.22100, -0.15080)`;
- `p=(0.12436, 1.2476, 0.56405, 0.021230)`.

For the scalar-curvature-squared form factor:

`f_R2(p^2) = a0 + sum_i ai / (((p/pi)^2 + 1)^2)`

with

- `a0=0.028373`;
- `a=(0.012637, 1.2661, 0.57040)`;
- `p=(5.7131, 0.73200, 0.092956)`.

The source fit coefficients are treated as comparator data, not free Candidate-Gravity parameters.

## 3. Coverage on the six frozen RQIR triplets

Iteration 149 froze six Lorentzian spacelike triplets. Their invariant ranges are

- `p^2 = 0.4239 ... 0.7473`;
- `q^2 = 0.2882 ... 0.5076`;
- `r^2 = 0.2278 ... 0.3313`.

Because every leg is spacelike in signature `(-,+,+,+)`, the action-data coverage diagnostic evaluates the Euclidean fit at

`p_E = sqrt(k_L^2)`

for each individual leg. This mapping is used **only** as a flat-space spacelike Euclidean coverage diagnostic; it is not promoted to a real-time response prescription.

Across all 18 legs the reproducible values lie in

`f_Ricci2 = -0.04680592285494515 ... -0.0037039902546036896`,

`f_R2 = 0.261312950235091 ... 0.6649777144616807`.

Authority:

- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`.

This closes the narrow question of whether the published analytic form-factor data are numerically defined on the finite spacelike scales used by the RQIR protocol.

## 4. Why this still does not define `chi2R`

The source reconstructs the Euclidean action first and then promotes the Euclidean Laplace-Beltrami operator to a Lorentzian d'Alembertian by Wick rotation.

For local polynomial operators, the real-time continuation can be fixed by the action/state/source prescription used by RQIR. For the reconstructed nonlocal inverse-operator structures, however, the Lorentzian operator requires a Green function.

The primary source explicitly discusses this Green-function problem and gives expansion around a flat-space **Feynman propagator** as one possible construction, while leaving a thorough treatment of the continuation/nonlocal operators beyond the scope of the paper.

RQIR needs something more specific:

- an in-in / Schwinger-Keldysh prescription;
- the retarded Green function appropriate to the same physical metric/source convention;
- source-completed nonlinear response on the six frozen triplets;
- a fixed handling of any branch cuts/nonlocal spectral structure.

Choosing `Feynman`, `retarded`, `advanced` or another Green function is not a harmless numerical convention for an ordered-response observable. It changes the real-time boundary condition. Therefore RQIR may not select the retarded choice on behalf of the comparator unless it is derived/frozen as part of the comparator dynamics.

## 5. Refined retained result

### AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED

Within the frozen curvature-squared asymptotic-safety truncation, the reconstructed covariant Euclidean effective action contains sufficient action-level information to define off-symmetric Euclidean background vertices in principle. The remaining RQIR blocker is not the absence of all off-symmetric action data; it is the absence of a uniquely frozen **retarded/in-in Green-function prescription** for the nonlocal Lorentzian operators required by ordered response.

Classification:

`BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

This is:

- **not** a consistency failure of asymptotic safety;
- **not** a statement that the AS response is zero;
- **not** evidence that AS is identical to C5;
- **not** permission to choose a retarded continuation ad hoc.

## 6. New funnel guardrail

### NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION

A Euclidean covariant nonlocal effective action can be sufficient to reconstruct Euclidean off-symmetric vertices yet still fail to define an operational RQIR ordered response. For nonlocal operators, the real-time Green-function / contour prescription is part of the physical comparator specification and must be frozen before `chi^(n)R`, Fisher or novelty quotients are computed.

This guardrail applies not only to asymptotic safety but to any nonlocal/form-factor Candidate Gravity or comparator.

## 7. Current AS comparator status

- concrete AS truncation: `FIXED`;
- Euclidean curvature-squared action: `SUPPORTED_SCOPED`;
- Appendix-H form-factor coverage on all 18 frozen spacelike legs: `PASS`;
- off-symmetric Euclidean background vertex: `DERIVABLE_IN_PRINCIPLE_WITHIN_TRUNCATION`;
- Lorentzian causal Green-function prescription: `BLOCKED`;
- six-probe `chi2R_even/odd`: `NOT_COMPUTED`;
- source-completed nonlinear Ward test: `NOT_COMPUTED`;
- AS `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`.

## 8. Readiness accounting

`MODEL_READINESS: 22%` — unchanged from Iteration 159.

Reason:

- provenance and localization of the AS blocker improved;
- Euclidean action coverage is now stronger than previously recorded;
- but no new usable retarded comparator tangent entered the complete RQIR quotient.

Frozen accounting remains:

- comparator foundation `19/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

## Next scientific gate — Iteration 161

Do not stall by inventing an AS causal prescription.

Test the **local IR expansion** of the same reconstructed AS action against the existing local C5 EFT span. The local derivative expansion has an ordinary source-completed retarded interpretation under the already-frozen C5 convention and can therefore answer a well-posed scoped question:

> Are the low-momentum AS curvature-squared directions already contained in the local C5 EFT comparator span?

If yes, record the scoped degeneracy as a negative result and keep the genuinely nonlocal AS sector BLOCKED pending causal completion. If no, freeze the surviving local residual and stress-test it against field redefinitions/source completion before any Candidate-Gravity use.
