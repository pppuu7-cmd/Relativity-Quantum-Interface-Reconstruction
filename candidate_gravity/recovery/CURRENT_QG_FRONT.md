# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **22%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending a robust residual after the complete fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 163**

## Scientific state in one sentence

The explicit local C5 ordered-response block is now rank `5/6` on the six frozen TT probes, and when combined with the already-frozen shared dRGT boundary/reference direction the fixed comparator matrix becomes rank `6/6`; both dRGT nonlinear target tangents (`alpha3`,`alpha4`) are therefore absorbed to numerical precision in this finite protocol. This is **finite-protocol saturation / regime-specific non-identifiability**, not a theory identity or consistency FAIL, and it removes the Iteration 157 `alpha3` residual from promotable novelty evidence.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights: comparator foundation 25%; robust unique residual 20%; frozen parent dynamics/ANSATZ 20%; candidate consistency 15%; identifiability/Fisher 10%; resource/experiment closure 10%.

Current accounting:

- comparator foundation `22/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS: 22%` — down from `24%` in Iteration 162. Comparator foundation improved by one point, but the previously scoped dRGT residual lost all three residual-readiness points because it is absorbed by the expanded authoritative quotient. Infrastructure progress is not counted.

## Frozen protocol and gate discipline

Reduced coordinates after hard locks remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate requires a nonzero residual after the complete fixed comparator/nuisance quotient:

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled. No frozen gate may be weakened post hoc.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-020`.

## C3 status

Fixed postquantum-classical comparator retained.

- linear `N2=A(5D2+D0)`, rank `1/2` in `(D2,D0)`;
- nonlinear symmetric cumulant from the same covariant OM action gives supported `(N2,C3sym)` rank `2/2` for physical `D2>0`;
- tree causal response `chi2R=-G_R Gamma3_EH G_R G_R` is common GR boundary after hard Newton calibration.

BLOCKED: diffusion-dependent ordered/MSR-loop corrections, exact `chi2R_odd`, non-TT completion, threshold, full C3 quotient.

## C4 status — `C4-DRGT-001`

Frozen point remains `m^2=0.04`, `alpha3=0`, `alpha4=0`; the underlying tangent definitions and parameter convention are unchanged.

Iteration 157 found a scoped `alpha3` residual relative to the smaller then-implemented C5 basis. Iteration 163 recomputes the quotient after the Iteration 162 C5 expansion and supersedes that residual **for promotion decisions**.

Expanded six-row matrix

`M=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`

has rank `6/6` under raw and all three fixed row-conditioning audits. Raw `s_min/s_max=4.2957925700833976e-4`; the base-row-L2 audit gives `5.500461215995698e-3`.

Both `alpha3` and `alpha4` projection residuals are numerical zero: max absolute residual across all audits `<3.71e-14`, max relative residual `<1.42e-13`.

Retain:

- `C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES`;
- `NG-FUNNEL-020 — SIX_ROW_TT_PROTOCOL_SATURATED_BY_FIXED_C5_PLUS_SHARED_BOUNDARY`.

Classification: `REGIME_SPECIFIC_NON_IDENTIFIABILITY / FINITE_PROTOCOL_SATURATION`.

Not claimed: exact dRGT=EFT identity, dRGT consistency failure, or degeneracy outside the six TT rows.

BLOCKED: helicity-0/1, Vainshtein/nonperturbative response, C4 `N2/C3sym`, full enriched-protocol quotient.

## C5 status

Retained:

- on-shell local amplitude tangent `12x10`, rank `10/10`, on-shell only;
- source-completed six-probe protocol PASS_SCOPED;
- EH + `Ricci^3/Riemann^3` retarded response Ward validated;
- Iteration 162 adds full response tangents for `Ricci^2` and `Ricci Box Ricci`, including required propagator insertions and operator-specific completed Ward checks;
- implemented explicit local ordered-response block `[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full]` has rank `5/6` on the six TT probes;
- `R^2` and `R Box R` are exact TT-cubic blind directions at this order because `R^(1)[h_TT]=0`; this is scoped blindness, not absence from full off-shell C5.

Retain:

- `C5-NG-001 — CURVATURE_SQUARED_RESPONSE_REQUIRES_PROPAGATOR_INSERTIONS`;
- `C5-NG-002 — SCALAR_CURVATURE_SQUARED_DIRECTIONS_TT_CUBIC_BLIND`;
- `NG-FUNNEL-019 — LOWER_DERIVATIVE_KERNEL_DEFORMATIONS_REQUIRE_FULL_RESPONSE_TANGENT`.

BLOCKED: remaining non-TT/full off-shell local directions, loop/nonanalytic C5, C5 `N2/C3sym` in one finite CTP map.

## Nonlocal status — `NL-WNL-001`

The weakly-nonlocal comparator remains fixed/scoped. Local cubic potential directions already lie in the existing C5 nonlinear span. Full form-factor-induced Lorentzian cubic response, causal completion, and nonlocal `N2/C3sym` remain BLOCKED.

Earlier supplemental six-row linear-TT diagnostics also showed possible local-C5 saturation; Iteration 163 now establishes an analogous saturation directly in the current nonlinear ordered-response quotient relevant to the dRGT target.

## Asymptotic-safety status — `AS-FRG-TT-001`

The Pawlowski–Tränkle FRG/effective-action comparator remains fixed/scoped.

- published symmetric-point Euclidean three-graviton data are not by themselves the required off-symmetric Lorentzian retarded tangent;
- reconstructed Euclidean curvature-squared action is sufficient to define off-symmetric Euclidean background vertices in principle within its truncation;
- strict local IR expansion is structurally contained in the local C5 EFT family;
- that strict IR Taylor surrogate fails its domain of validity on the current finite Planck-scale probes;
- full nonlocal six-probe `chi2R_even/odd` remains `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

Retain `AS-NG-001/002/003` and `NG-FUNNEL-016/017/018`.

## `ANSATZ-003` state

Still intentionally **not frozen**. No robust Candidate Gravity residual survives the authoritative fixed comparator quotient.

Fisher/resources remain forbidden.

## Iteration 163 authorities

- `analysis/c4_c5_protocol_saturation_iteration163.py`;
- `results/c4_c5_protocol_saturation_iteration163.json`;
- `candidate_gravity/C4_C5_PROTOCOL_SATURATION_ITERATION163.md`;
- `research_log/2026-08-31_iteration_163_c4_c5_protocol_saturation.md`;
- `recovery/RECOVERY_DELTA_ITERATION_163.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION163.md`.

## Immediate next scientific priority — Iteration 164

The six-row TT space is saturated; adding more comparator columns inside those same coordinates cannot generate an orthogonal novelty residual. Therefore **enrich the observable protocol before any new candidate promotion test**.

Freeze more independent rows while preserving every existing comparator definition and parameter convention. Preferred first extension is a source-completed non-TT/helicity-sensitive response block; if that is not yet derivable without new arbitrary conventions, add independently frozen off-shell triplets from the same operational metric/source convention.

Required order:

1. freeze enriched rows before seeing target residuals;
2. derive comparator columns from their already-declared dynamics only;
3. compute fixed comparator rank/SVD and conditioning;
4. then test target residuals;
5. only if a nonzero algebraic residual survives may parent-ansatz work resume.

No `ANSATZ-003`, Fisher or resource calculations yet.
