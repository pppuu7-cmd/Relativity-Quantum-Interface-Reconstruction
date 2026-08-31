# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **22%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending full fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 160**

## Scientific state in one sentence

The comparator funnel contains fixed scoped C3, nonlinear dRGT C4, local quantum-GR EFT C5, weakly-nonlocal form-factor, and a concrete asymptotic-safety FRG/effective-action comparator. Iteration 160 refines the asymptotic-safety boundary: the reconstructed curvature-squared Euclidean action is rich enough for off-symmetric Euclidean background vertices in principle, but the nonlocal Lorentzian theory does not freeze the retarded/in-in Green-function prescription required for RQIR ordered response, so the AS `chi2R` tangent remains physically BLOCKED rather than zero or failed.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights: comparator foundation 25%; robust unique residual 20%; frozen parent dynamics/ANSATZ 20%; candidate consistency 15%; identifiability/Fisher 10%; resource/experiment closure 10%.

Current accounting remains:

- comparator foundation `19/25`;
- unique residual discovery `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

`MODEL_READINESS: 22%` — unchanged from Iteration 159 because the AS action-level provenance improved but no new usable retarded comparator tangent entered the complete quotient.

## Frozen protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate requires nonzero residual after the complete fixed comparator/nuisance quotient:

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-017`.

## C3 status

Fixed postquantum-classical comparator retained.

- linear `N2=A(5D2+D0)`, rank `1/2` in `(D2,D0)`;
- nonlinear symmetric cumulant from the same covariant OM action gives supported `(N2,C3sym)` rank `2/2` for physical `D2>0`;
- tree causal response `chi2R=-G_R Gamma3_EH G_R G_R` is common GR boundary after hard Newton calibration.

Retain `C3-NG-001/002/003`, `NG-FUNNEL-012/013`.

BLOCKED: diffusion-dependent ordered/MSR-loop corrections, exact `chi2R_odd`, non-TT completion, threshold, full C3 quotient.

## C4 status — `C4-DRGT-001`

Frozen point `m^2=0.04`, `alpha3=0`, `alpha4=0`.

TT tangent `(log m^2,alpha3)` is rank `2/2`. After shared EH/gain quotient:

- `log m^2` residual `0.00126 ... 0.00320` -> `NEAR_DEGENERATE_NOT_PROMOTABLE`;
- `alpha3` residual `0.0472 ... 0.0694` -> `SCOPED_RESIDUAL_SURVIVES`.

Retain `C4-NG-001/002/003`, `NG-FUNNEL-014`.

BLOCKED: helicity-0/1, Vainshtein/nonperturbative response, `N2/C3sym`, alpha4 higher-point, full C4 quotient.

## C5 status

Retained:

- on-shell local amplitude tangent `12x10`, rank `10/10`, on-shell only;
- source-completed six-probe protocol PASS_SCOPED;
- EH + `Ricci^3/Riemann^3` local retarded response `6x2`, rank `2/2`, Ward validated.

BLOCKED: higher local retarded directions, loop/nonanalytic directions, C5 `N2/C3sym` in the same finite CTP map.

## Nonlocal status — `NL-WNL-001` (Iteration 158)

The weakly-nonlocal comparator freezes a TT form factor and independent interaction potential.

Gain-only linear `log sigma` residual fraction: `0.3996471300114534` — known-comparator shape only, not novelty.

The explicitly frozen local cubic potential directions `Ricci^3/Riemann^3` are already in the existing C5 nonlinear span to numerical precision.

Retain:

- `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`;
- `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`;
- `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`.

BLOCKED: form-factor-induced cubic `chi2R`, Lorentzian causal completion, nonlocal `N2/C3sym`, full nonlocal quotient.

Supplemental diagnostic `QG-NL-EXP-001` shows that on exactly six linear TT coordinates, admitting the full dimension-12 local C5 quadratic TT basis plus common gain can saturate the six-row space (`rank 6/6`). This is protocol saturation, not theory identity, and reinforces that gain-only nonlocal residuals are not novelty certificates.

## Asymptotic-safety status — `AS-FRG-TT-001` (Iterations 159–160)

Primary authority: Pawlowski & Tränkle, arXiv:2309.17043 / Phys. Rev. D 110, 086011 (2024).

### Iteration 159 retained warning

The published one-variable momentum-symmetric TT dressing `gamma_g^(3)(p)` is not the full off-symmetric source-completed Lorentzian `Gamma_3(p,q,r)` required by the six frozen RQIR triplets.

Retain:

- `AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`;
- `NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

### Iteration 160 refinement

The same source reconstructs a diffeomorphism-invariant **Euclidean background effective action** through curvature-squared order with covariant momentum-dependent form factors

`R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn`.

Thus action-level information is sufficient to define off-symmetric Euclidean background vertices in principle within the frozen truncation and reconstruction assumptions; the data obstruction is not simply `missing off-symmetric vertex`.

The published analytic form-factor fits were evaluated on every individual leg of the six frozen spacelike RQIR triplets. All 18 legs give finite values:

- `f_Ricci2`: `-0.04680592285494515 ... -0.0037039902546036896`;
- `f_R2`: `0.261312950235091 ... 0.6649777144616807`.

These are Euclidean coverage values only, not `chi2R`.

The remaining physical blocker is the Lorentzian causal completion. The reconstructed nonlocal operators require a Green-function prescription; the primary source discusses possible Green-function constructions, including expansion about a flat-space Feynman propagator, but does not freeze the RQIR retarded/in-in prescription.

Therefore:

`AS six-probe chi2R = BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

Retain:

- `AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED`;
- `NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION`.

Current AS status:

- comparator/truncation: `FIXED_SCOPED`;
- Euclidean curvature-squared action: `SUPPORTED_SCOPED`;
- Appendix-H fit coverage on frozen spacelike legs: `PASS`;
- off-symmetric Euclidean background vertex: `DERIVABLE_IN_PRINCIPLE_WITHIN_TRUNCATION`;
- six-probe `chi2R_even/odd`: `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`;
- source-completed nonlinear Ward test: `NOT_COMPUTED`;
- `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`.

Authorities:

- `candidate_gravity/comparators/AS-FRG-TT-001.md`;
- `candidate_gravity/ASYMPTOTIC_SAFETY_MAPPING_ITERATION159.md`;
- `candidate_gravity/ASYMPTOTIC_SAFETY_ACTION_AUDIT_ITERATION160.md`;
- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`;
- `research_log/2026-08-31_iteration_160_as_action_causal_completion.md`;
- `recovery/RECOVERY_DELTA_ITERATION_160.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION160.md`.

## `ANSATZ-003` state

Still intentionally **not frozen**. No robust Candidate Gravity residual has survived the complete fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 161

Use the **local IR derivative expansion** of the same reconstructed AS action and test it against the existing local C5 EFT span.

1. Freeze the local IR operator directions and their coefficients from the AS source.
2. Map them into the same source-completed local EFT convention used by C5.
3. Test whether the local AS directions are contained in the allowed C5 local tangent space.
4. If contained, record a scoped AS/C5 degeneracy; keep the genuinely nonlocal AS sector BLOCKED.
5. If a residual survives, run source-completion/field-redefinition/Ward checks before promotion.
6. No `ANSATZ-003`, Fisher or resources until a robust residual survives the complete fixed comparator funnel.
