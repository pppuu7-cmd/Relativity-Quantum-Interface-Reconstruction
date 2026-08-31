# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending a robust residual after the complete fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 165**

## Scientific state in one sentence

The 12-row TT residual exposed in Iteration 164 does **not** survive target-independent completion of the already-authorized local C5 cubic sector through the frozen dimension-12 cutoff: a 12-column local-C5 subset itself has rank `12/12` and absorbs both corrected dRGT tangents to machine precision, so the current 12-row ordered-TT protocol is saturated and cannot support a novelty certificate.

## Mandatory provenance correction

Iteration 163 used the correct numerical dRGT tangent arrays but mislabeled them. Correct mapping from Iteration 156:

- first target: `d/d log(m^2)`;
- second target: `d/d alpha3`;
- `alpha4`: cubic-TT blind because `L4[K]` starts quartic.

Preserve historical Iteration-163 files and cite:

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights: comparator foundation 25%; robust unique residual 20%; frozen parent dynamics/ANSATZ 20%; candidate consistency 15%; identifiability/Fisher 10%; resource/experiment closure 10%.

Current accounting:

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS: 24%` — up from `23%` in Iteration 164 by one comparator-foundation point only. The Iteration-164 temporary residual earns no residual-readiness points because it is absorbed by the authorized Iteration-165 C5 completion.

## Frozen protocol and gate discipline

Reduced conceptual coordinates after hard locks remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

For the current ordered-response subproblem, the authoritative finite protocol contains exactly **12 frozen TT rows**: the original six plus the six deterministic target-independent rows from Iteration 164.

The novelty pre-gate remains

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled. No frozen gate may be weakened post hoc.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-023`.

## C3 status

Fixed postquantum-classical comparator retained.

- linear `N2=A(5D2+D0)`, rank `1/2` in `(D2,D0)`;
- nonlinear symmetric cumulant from the same covariant OM action gives supported `(N2,C3sym)` rank `2/2` for physical `D2>0`;
- tree causal response `chi2R=-G_R Gamma3_EH G_R G_R` is the common GR boundary after hard Newton calibration and is already represented by the EH column.

BLOCKED: diffusion-dependent ordered/MSR-loop corrections, exact `chi2R_odd`, non-TT completion, threshold, full enriched C3 quotient.

## C4 status — `C4-DRGT-001`

Frozen point remains `m^2=0.04`, `alpha3=0`, `alpha4=0`.

Historical results:

- Iteration 163: six-row finite-protocol saturation;
- Iteration 164: target-independent extension to 12 rows exposed nonzero corrected `dlogm2` and `dalpha3` residuals against the then-smaller local-C5 basis;
- Iteration 165: both residuals are absorbed to machine precision by target-independent local-C5 cubic completion through dimension 12.

Retain:

- `C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES`;
- `C4-NG-005 — SIX_ROW_SATURATION_DOES_NOT_PERSIST_UNDER_TARGET_INDEPENDENT_TT_ROW_ENRICHMENT`;
- `C4-NG-006 — DRGT_DLOGM2_DIRECTION_IS_NEAR_DEGENERATE_AFTER_ENRICHED_LOCAL_C5_QUOTIENT` as historical Iteration-164 classification;
- `C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

Current classification in the 12-row TT protocol: **REGIME_SPECIFIC_NON_IDENTIFIABILITY / FINITE_PROTOCOL SATURATION**. This is not exact dRGT=C5 identity and not a dRGT consistency FAIL.

BLOCKED: helicity-0/1, Vainshtein/nonperturbative response, C4 `N2/C3sym`, full non-TT quotient.

## C5 status

Retained:

- on-shell local amplitude tangent `12x10`, rank `10/10`, on-shell only;
- source-completed off-shell TT protocol;
- EH + curvature-cubic retarded response Ward validation;
- `Ricci^2` and `Ricci Box Ricci` full response tangents with propagator insertions and completed Ward checks;
- `R^2` and `R Box R` remain exact TT-cubic blind at this order because `R^(1)[h_TT]=0`;
- Iteration 165 adds target-independent mixed `Ricci Ricci Riemann` plus `Box^n`, `n=1,2,3`, descendants of the existing Ricci and Riemann cubic chains through dimension 12;
- resulting local-C5 matrix shape `12x12`, rank `12/12`;
- raw `s_min/s_max=2.8317567788e-6`;
- new cubic gauge-leg regressions pass to machine precision.

Retain:

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

This is a sufficient finite-space saturation certificate, not a claim that the implemented subset is a complete covariant dimension-12 EFT operator basis.

BLOCKED: remaining non-TT/full off-shell local directions, loop/nonanalytic C5, C5 `N2/C3sym` in one finite CTP map.

## Nonlocal status — `NL-WNL-001`

The weakly-nonlocal comparator remains fixed/scoped. Its local cubic potential directions are already contained in the local C5 nonlinear span. Full form-factor-induced Lorentzian cubic response, causal completion, and nonlocal `N2/C3sym` remain BLOCKED.

Within the already saturated 12-row TT space these blocked columns cannot restore a nonzero orthogonal residual, but they remain required outside that space and for theory-level claims.

## Asymptotic-safety status — `AS-FRG-TT-001`

The Pawlowski–Tränkle FRG/effective-action comparator remains fixed/scoped.

- symmetric-point Euclidean three-graviton data are not the required off-symmetric Lorentzian retarded tangent;
- reconstructed Euclidean curvature-squared action defines off-symmetric Euclidean background vertices in principle within its truncation;
- strict local IR expansion is structurally contained in local C5;
- strict IR Taylor surrogate is invalid on the finite Planck-scale probes;
- full nonlocal retarded `chi2R_even/odd` remains `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

These blockers cannot alter zero residual inside the already full-rank 12-row C5 span, but remain relevant in an expanded observable protocol.

## New Iteration-165 funnel consequences

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE, ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL_IN_THAT SAME SPACE`.

The Iteration-164 `dalpha3` residual is therefore historical/scoped only and may not motivate candidate promotion.

## `ANSATZ-003` state

Still intentionally **not frozen**. No residual has survived the complete currently authorized comparator treatment in the 12-row TT space.

Fisher/resources remain forbidden.

## Iteration 165 authorities

- `analysis/c5_dimension12_cubic_completion_iteration165.py`;
- `results/c5_dimension12_cubic_completion_iteration165.json`;
- `candidate_gravity/C5_DIMENSION12_CUBIC_COMPLETION_ITERATION165.md`;
- `research_log/2026-08-31_iteration_165_c5_dimension12_completion.md`;
- `recovery/RECOVERY_DELTA_ITERATION_165.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION165.md`.

## Immediate next scientific priority — Iteration 166

Do **not** search for novelty inside the saturated 12-row TT space and do not optimize any new row around dRGT target residuals.

Required order:

1. freeze a target-independent observable extension with dimension greater than 12, preferably additional source-completed off-shell rows generated before target evaluation and/or an independently defined non-TT/helicity-sensitive block;
2. keep the Iteration-165 local C5 dynamics and parameter convention fixed;
3. evaluate the fixed C5 basis first and obtain rank/SVD on the enlarged row space;
4. only then evaluate corrected dRGT `dlogm2/dalpha3` and any other fixed comparator targets;
5. instantiate C3/nonlocal/AS columns only where the same enlarged protocol and causal convention make them physically supported; otherwise preserve BLOCKED;
6. only a nonzero residual surviving the expanded fixed C3/C4/C5/nonlocal/AS quotient can earn residual-readiness points or reopen `ANSATZ-003`, Fisher, or resources.
