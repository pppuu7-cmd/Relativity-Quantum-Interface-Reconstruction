# AS-FRG-TT-001 — asymptotic-safety FRG TT/effective-action comparator

**Frozen in:** Iteration 159  
**Refined in:** Iterations 160–161  
**Status:** concrete literature comparator; Euclidean action supported, strict local IR C5-degenerate, full RQIR retarded nonlocal mapping BLOCKED  
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

## Euclidean action coverage — Iteration 160

Iteration 159 correctly forbade replacing the full off-symmetric three-variable tensor vertex by the one-variable symmetric-point dressing `gamma_g^(3)(p)`.

Iteration 160 established a stronger action-level statement:

**The reconstructed covariant Euclidean action contains enough information to define off-symmetric Euclidean background vertices in principle within the frozen curvature-squared truncation and reconstruction assumptions.**

The published analytic form-factor fits were evaluated on every individual leg of the six frozen spacelike RQIR triplets. All 18 legs return finite Euclidean fit values.

Authority:

- `candidate_gravity/ASYMPTOTIC_SAFETY_ACTION_AUDIT_ITERATION160.md`;
- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`.

## Full nonlocal RQIR mapping boundary

The source Wick-rotates the Euclidean Laplace-Beltrami operator into a Lorentzian d'Alembertian. Because the reconstructed form factors contain nonlocal inverse-operator structure, a Green function must be chosen to define those Lorentzian operators. The source discusses possible constructions, including expansion around a flat-space Feynman propagator, but does not freeze the RQIR-specific in-in/retarded Green-function prescription needed for ordered response.

RQIR requires:

- the same physical metric/source convention as the six-probe protocol;
- a Schwinger-Keldysh/in-in contour or equivalent real-time definition;
- the corresponding retarded nonlocal Green functions;
- source-completed `Gamma_3` and `chi2R_even/odd`;
- a Ward/constraint test in that same real-time convention.

Therefore the following remain forbidden without an explicitly derived/frozen causal prescription:

- evaluating full nonlocal AS `chi2R_even/odd` on the six frozen triplets;
- treating Euclidean form-factor values as retarded response values;
- selecting Feynman, retarded or another Green function merely for convenience;
- zero-filling unsupported ordered or stochastic coordinates;
- adding an AS Fisher column.

## Local IR sector — Iteration 161

The same primary source explicitly Taylor-expands its form factors in the strict IR and obtains the local action built from

- `R`;
- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

Published rounded coefficients are

- `g_Ricci2 ~= -0.40`;
- `g_R2 ~= 1.9`;
- `c1=344.09`;
- `c2=-136.75`.

The Iteration-149 C5 off-shell convention is a complete unreduced local diffeomorphism-invariant covariant EFT basis through dimension 12, including Ricci/EOM-redundant directions. Therefore every operator in this AS local IR action is already an allowed C5 local Wilson direction.

Result:

`AS strict local IR action subset C5 local EFT family`.

This is an exact **structural** comparator degeneracy in the controlled local IR regime, not an asymptotic-safety consistency failure.

However, the local IR expansion cannot be used as a surrogate on the current six RQIR probes. Direct comparison of the first-order Taylor approximation with the full Appendix-H fits on all 18 legs gives relative-error ranges

- Ricci2: `1666.969 ... 69310.077`;
- R2: `45.023 ... 384.894`.

Thus the present `k^2 ~= 0.23 ... 0.75 M_Pl^2` probes are outside the controlled first-order IR Taylor regime for these fits.

Authority:

- `candidate_gravity/ASYMPTOTIC_SAFETY_IR_C5_AUDIT_ITERATION161.md`;
- `analysis/as_ir_c5_embedding_iteration161.py`;
- `results/as_ir_c5_embedding_iteration161.json`.

## Retained results

### AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT

The published symmetric-point TT dressing alone is not the full off-symmetric RQIR retarded tangent.

### AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED

Within the frozen curvature-squared truncation, action-level information supports off-symmetric Euclidean reconstruction in principle, but the real-time retarded/in-in Green-function prescription required by RQIR is not fixed by the source.

### AS-NG-003 — LOCAL_IR_AS_SUBSET_OF_C5_EFT

In the strict local IR derivative-expansion regime, the selected AS action contains only operators already allowed by the complete local C5 gravitational EFT family.

## Funnel guardrails

- `NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`;
- `NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION`;
- `NG-FUNNEL-018 — LOCAL_LIMIT_DEGENERACY_DOES_NOT_COMPLETE_NONLOCAL_COMPARATOR`.

## Current status

- AS comparator/truncation: `FIXED_SCOPED`;
- AS Euclidean curvature-squared action: `SUPPORTED_SCOPED`;
- Appendix-H form-factor coverage on frozen spacelike legs: `PASS`;
- AS off-symmetric Euclidean background vertex: `DERIVABLE_IN_PRINCIPLE_WITHIN_TRUNCATION`;
- AS strict local IR vs C5: `EXACT_STRUCTURAL_DEGENERACY_WITH_LOCAL_C5_EFT_FAMILY`;
- AS local IR surrogate on current six probes: `FAIL_DOMAIN_OF_VALIDITY`;
- AS full nonlocal six-probe `chi2R`: `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`;
- AS source-completed nonlinear Ward test: `NOT_COMPUTED`;
- AS `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.
