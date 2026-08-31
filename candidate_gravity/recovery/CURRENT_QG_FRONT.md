# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **23%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending full fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 161**

## Scientific state in one sentence

The fixed comparator funnel now contains scoped C3, nonlinear dRGT C4, local quantum-GR EFT C5, weakly-nonlocal form-factor, and a concrete asymptotic-safety FRG/effective-action comparator. Iteration 161 proves that the selected AS action's **strict local IR derivative expansion is structurally contained in the local C5 EFT family**, while direct comparison to the full AS fits shows that this IR expansion is unusable on the current finite Planck-scale RQIR probes; the genuinely nonlocal AS ordered response remains BLOCKED by its unfrozen retarded/in-in Green-function prescription.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights: comparator foundation 25%; robust unique residual 20%; frozen parent dynamics/ANSATZ 20%; candidate consistency 15%; identifiability/Fisher 10%; resource/experiment closure 10%.

Current accounting:

- comparator foundation `20/25`;
- unique residual discovery `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

`MODEL_READINESS: 23%` — increased by one point from Iteration 160 because a genuine comparator sector is now classified: strict local-IR AS is inside C5 EFT, and the boundary preventing its misuse on the current probes is quantitatively certified.

## Frozen protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate requires nonzero residual after the complete fixed comparator/nuisance quotient:

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-018`.

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

The complete off-shell C5 family is frozen as an unreduced local diffeomorphism-invariant covariant operator/source basis through dimension 12, so Ricci/EOM-redundant curvature-squared and derivative operators are allowed comparator directions even where their explicit six-probe retarded columns have not yet been implemented.

BLOCKED: explicit retarded columns for the remaining local off-shell basis, loop/nonanalytic directions, C5 `N2/C3sym` in the same finite CTP map.

## Nonlocal status — `NL-WNL-001` (Iteration 158)

The weakly-nonlocal comparator freezes a TT form factor and independent interaction potential.

Gain-only linear `log sigma` residual fraction: `0.3996471300114534` — known-comparator shape only, not novelty.

The explicitly frozen local cubic potential directions `Ricci^3/Riemann^3` are already in the existing C5 nonlinear span to numerical precision.

Retain:

- `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`;
- `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`;
- `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`.

BLOCKED: form-factor-induced cubic `chi2R`, Lorentzian causal completion, nonlocal `N2/C3sym`, full nonlocal quotient.

Supplemental diagnostic `QG-NL-EXP-001` shows that on exactly six linear TT coordinates, admitting the full dimension-12 local C5 quadratic TT basis plus common gain can saturate the six-row space (`rank 6/6`). This is protocol saturation, not theory identity.

## Asymptotic-safety status — `AS-FRG-TT-001` (Iterations 159–161)

Primary authority: Pawlowski & Tränkle, arXiv:2309.17043 / Phys. Rev. D 110, 086011 (2024).

### Iteration 159

The published one-variable momentum-symmetric TT dressing `gamma_g^(3)(p)` is not the full off-symmetric source-completed Lorentzian `Gamma_3(p,q,r)` required by the six frozen RQIR triplets.

Retain:

- `AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`;
- `NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

### Iteration 160

The same source reconstructs a diffeomorphism-invariant Euclidean background effective action through curvature-squared order with covariant momentum-dependent form factors

`R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn`.

Action-level information is sufficient to define off-symmetric Euclidean background vertices in principle within the frozen truncation/reconstruction assumptions. All 18 individual legs of the frozen spacelike RQIR triplets return finite values under the published analytic form-factor fits.

The remaining full nonlocal blocker is the Lorentzian causal completion: inverse operators require a Green-function prescription, and the primary source does not freeze the RQIR retarded/in-in prescription.

Retain:

- `AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED`;
- `NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION`.

### Iteration 161 — local IR / C5 result

The source's strict local IR expansion contains

- `R`;
- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`,

with rounded coefficients

- `g_Ricci2 ~= -0.40`;
- `g_R2 ~= 1.9`;
- `c1=344.09`;
- `c2=-136.75`.

All of these operators belong to the complete local C5 off-shell EFT family. Therefore:

`AS strict local IR action = point/subset inside C5 local EFT family`.

Retain:

`AS-NG-003 — LOCAL_IR_AS_SUBSET_OF_C5_EFT`.

This is a regime-specific exact structural comparator degeneracy, not an AS theory failure.

Directly comparing the first-order IR Taylor expansion with the full Appendix-H fits on all 18 legs of the current six probes gives relative-error ranges

- Ricci2: `1666.9691403682948 ... 69310.07731333924`;
- R2: `45.02312154387796 ... 384.89448594867974`.

Therefore the local IR action is **not** an admissible surrogate for the full AS response at current probe scales `k^2 ~= 0.23 ... 0.75 M_Pl^2`.

Retain:

`NG-FUNNEL-018 — LOCAL_LIMIT_DEGENERACY_DOES_NOT_COMPLETE_NONLOCAL_COMPARATOR`.

Current AS status:

- comparator/truncation: `FIXED_SCOPED`;
- Euclidean curvature-squared action: `SUPPORTED_SCOPED`;
- off-symmetric Euclidean background vertex: `DERIVABLE_IN_PRINCIPLE_WITHIN_TRUNCATION`;
- strict local IR vs C5: `EXACT_STRUCTURAL_DEGENERACY_WITH_LOCAL_C5_EFT_FAMILY`;
- local IR surrogate on current six probes: `FAIL_DOMAIN_OF_VALIDITY`;
- full nonlocal six-probe `chi2R_even/odd`: `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`;
- source-completed nonlinear Ward test for full nonlocal AS: `NOT_COMPUTED`;
- `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`.

Authorities:

- `candidate_gravity/comparators/AS-FRG-TT-001.md`;
- `candidate_gravity/ASYMPTOTIC_SAFETY_ACTION_AUDIT_ITERATION160.md`;
- `candidate_gravity/ASYMPTOTIC_SAFETY_IR_C5_AUDIT_ITERATION161.md`;
- `analysis/as_ir_c5_embedding_iteration161.py`;
- `results/as_ir_c5_embedding_iteration161.json`;
- `research_log/2026-08-31_iteration_161_as_ir_c5_embedding.md`;
- `recovery/RECOVERY_DELTA_ITERATION_161.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION161.md`.

## `ANSATZ-003` state

Still intentionally **not frozen**. No robust Candidate Gravity residual has survived the complete fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 162

Turn the structural local C5 coverage into explicit finite ordered-response columns.

Implement source-completed six-probe retarded response for the four local operators appearing in the AS IR correction sector:

1. `R_mn R^mn`;
2. `R^2`;
3. `R_mn Box R^mn`;
4. `R Box R`.

Required checks:

- same physical metric/source convention as Iterations 147–149;
- same six triplets/projectors/windows;
- source-completed Ward identity;
- rank/SVD after EH/gain and existing `Ricci^3/Riemann^3` columns;
- detect and record finite-protocol saturation if present.

Do not use AS IR coefficients as a surrogate for the full nonlocal AS response. No `ANSATZ-003`, Fisher or resource calculations yet.
