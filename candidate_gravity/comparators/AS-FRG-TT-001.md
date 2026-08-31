# AS-FRG-TT-001 — asymptotic-safety FRG TT/effective-action comparator

**Frozen in:** Iteration 159  
**Refined in:** Iteration 160  
**Status:** concrete literature comparator; Euclidean action supported, RQIR retarded mapping BLOCKED  
**Not a Candidate Gravity ansatz.**

## Literature authority

Primary fixed source:

- J. M. Pawlowski and J. Tränkle, *Effective action and black hole solutions in asymptotically safe quantum gravity*, arXiv:2309.17043 / Phys. Rev. D 110, 086011 (2024).

Supporting convergence/vertex-expansion source:

- T. Denz, J. M. Pawlowski and M. Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, arXiv:1612.07315.

Recent continuation/scattering cross-check:

- A. P. Chiesa, J. M. Pawlowski and M. Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168.

## Fixed published truncation content

The primary construction reconstructs a diffeomorphism-invariant Euclidean background effective action from momentum-dependent graviton correlation functions. In a curvature expansion about flat Euclidean space it retains full covariant momentum dependence through curvature-squared form factors, schematically

`Gamma[g] = ... + R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn + ...`.

The TT fluctuation vertices are used to reconstruct these background form factors through an approximate Nielsen-identity mapping. In the declared projection:

- the TT propagator/three-point sector is insensitive to `R^2` at the relevant order;
- the TT three-point `p^4` structure determines `R_mn^2` information;
- the TT four-point structure supplies the additional information needed for `R^2`.

The paper provides analytic fits to both curvature-squared form factors.

## Why this is a concrete comparator

This is not the broad label `asymptotic safety`. The frozen comparator is specifically the published TT/effective-action truncation and its stated reconstruction assumptions.

Supported objects:

- Euclidean TT two-point momentum dependence;
- Euclidean TT three-/four-point information in the published projection;
- reconstructed covariant curvature-squared form factors;
- action-level off-symmetric Euclidean background vertices in principle, obtained by differentiating the reconstructed action within that truncation.

Iteration 160 evaluates the published analytic form-factor fits on every individual leg of the six frozen spacelike RQIR triplets. All 18 legs lie at finite positive Euclidean momenta for the flat-space spacelike coverage map and return finite fit values.

Authority:

- `candidate_gravity/ASYMPTOTIC_SAFETY_ACTION_AUDIT_ITERATION160.md`;
- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`.

## Refined RQIR mapping boundary

Iteration 159 correctly forbade replacing the full off-symmetric three-variable tensor vertex by the one-variable symmetric-point dressing `gamma_g^(3)(p)`.

Iteration 160 refines the reason for the remaining block:

**The reconstructed covariant Euclidean action contains enough information to define off-symmetric Euclidean background vertices in principle. The unresolved step is the physical Lorentzian causal completion.**

The source Wick-rotates the Euclidean Laplace-Beltrami operator into a Lorentzian d'Alembertian. Because the reconstructed form factors contain nonlocal inverse-operator structure, a Green function must be chosen to define those Lorentzian operators. The source discusses possible constructions, including expansion around a flat-space Feynman propagator, but does not freeze the RQIR-specific in-in/retarded Green-function prescription needed for ordered response.

RQIR requires:

- the same physical metric/source convention as the six-probe protocol;
- a Schwinger-Keldysh/in-in contour or equivalent real-time definition;
- the corresponding retarded nonlocal Green functions;
- source-completed `Gamma_3` and `chi2R_even/odd`;
- a Ward/constraint test in that same real-time convention.

Therefore the following remain forbidden without an explicitly derived/frozen causal prescription:

- evaluating AS `chi2R_even/odd` on the six frozen triplets;
- treating Euclidean form-factor values as retarded response values;
- selecting Feynman, retarded or another Green function merely for convenience;
- zero-filling unsupported ordered or stochastic coordinates;
- adding an AS Fisher column.

## Retained results

### AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT

The published symmetric-point TT dressing alone is not the full off-symmetric RQIR retarded tangent.

### AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED

Within the frozen curvature-squared truncation, action-level information supports off-symmetric Euclidean reconstruction in principle, but the real-time retarded/in-in Green-function prescription required by RQIR is not fixed by the source.

Classification:

`BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

This is **not** a consistency failure of asymptotic safety and **not** evidence that the AS response is zero.

## Funnel guardrails

- `NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`;
- `NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION`.

## Current status

- AS comparator/truncation: `FIXED_SCOPED`;
- AS Euclidean curvature-squared action: `SUPPORTED_SCOPED`;
- Appendix-H form-factor coverage on frozen spacelike legs: `PASS`;
- AS off-symmetric Euclidean background vertex: `DERIVABLE_IN_PRINCIPLE_WITHIN_TRUNCATION`;
- AS six-probe `chi2R`: `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`;
- AS source-completed nonlinear Ward test: `NOT_COMPUTED`;
- AS `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.
