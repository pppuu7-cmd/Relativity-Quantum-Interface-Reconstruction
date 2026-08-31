# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **22%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending full fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 159**

## Scientific state in one sentence

The comparator funnel now contains fixed scoped C3, nonlinear dRGT C4, local quantum-GR EFT C5, weakly-nonlocal form-factor, and a concrete asymptotic-safety FRG TT comparator. Iteration 159 localizes the asymptotic-safety blocker: published symmetric-point Euclidean three-graviton information does not determine the off-symmetric source-completed Lorentzian retarded `Gamma_3(p,q,r)` required by the six frozen RQIR triplets, so the AS post-Gaussian tangent is operationally BLOCKED rather than zero or failed.

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

`MODEL_READINESS: 22%` — unchanged from Iteration 158 because the new AS block is concretely specified but its required retarded off-symmetric tangent remains blocked.

## Frozen protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate requires nonzero residual after the complete fixed comparator/nuisance quotient:

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-016`.

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

## Asymptotic-safety status — `AS-FRG-TT-001` (Iteration 159)

Primary literature authority: Pawlowski & Tränkle, arXiv:2309.17043. Supporting vertex-expansion source: arXiv:1612.07315. Recent continuation cross-check: arXiv:2603.10168.

Supported published content:

- Euclidean TT two-point momentum dependence;
- TT three-/four-point information at momentum-symmetric configurations;
- reconstructed diffeomorphism-invariant curvature form factors.

RQIR requires six unequal off-shell triplets and ordered Lorentzian retarded `chi2R`. The published one-variable symmetric-point `gamma_g^(3)(p)` does not determine full off-symmetric `Gamma_3(p,q,r)` on those triplets, and Euclidean data alone do not fix the required retarded prescription.

Retain:

- `AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`;
- `NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

Classification: `OPERATIONAL_BLOCKED / PROTOCOL_MISMATCH`, not consistency FAIL, exact identity, near-degeneracy, or zero response.

BLOCKED: AS six-probe `chi2R_even/odd`, source-completed nonlinear Ward test, AS `N2/C3sym`, full AS quotient.

Authorities:

- `candidate_gravity/comparators/AS-FRG-TT-001.md`;
- `candidate_gravity/ASYMPTOTIC_SAFETY_MAPPING_ITERATION159.md`;
- `research_log/2026-08-31_iteration_159_asymptotic_safety_mapping.md`;
- `recovery/RECOVERY_DELTA_ITERATION_159.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION159.md`.

## `ANSATZ-003` state

Still intentionally **not frozen**. No robust Candidate Gravity residual has survived the complete fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 160

Audit the reconstructed covariant effective action/form factors in arXiv:2309.17043 to determine whether they contain enough action-level information to derive the required off-symmetric cubic TT vertex directly.

1. If sufficient: derive the off-symmetric cubic vertex from the reconstructed action, then define the source-completed retarded continuation on the six frozen triplets and run the Ward/quotient checks.
2. If insufficient: freeze `BLOCKED_AS_ACTION_DATA_INSUFFICIENT`; do not invent interpolation or analytic continuation.
3. Preserve the distinction between gain-only nonlocal residuals and residuals after the full local C5 quadratic quotient.
4. No `ANSATZ-003`, Fisher, or resources until a robust residual survives the full fixed comparator funnel.
