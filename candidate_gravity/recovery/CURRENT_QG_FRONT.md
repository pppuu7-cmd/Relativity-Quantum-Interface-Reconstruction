# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **23%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending a robust residual after the complete fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 164**

## Scientific state in one sentence

The six-row TT saturation of Iteration 163 is a valid finite-protocol result but is **not stable under target-independent enrichment**: after adding six deterministically frozen spacelike TT rows, the same fixed local-C5 plus shared dRGT-boundary matrix remains rank `6` while the correctly labelled dRGT tangents `d/d log(m^2)` and `d/d alpha3` raise the combined rank to `8`; `dlogm2` is near-degenerate and `dalpha3` leaves a scoped residual, but neither is promotable until the enriched C3/nonlocal/asymptotic-safety/full-C5 quotient is closed.

## Mandatory provenance correction

Iteration 163 used the correct two numerical dRGT tangent arrays but mislabeled them as `alpha3` and `alpha4`.

Correct Iteration-156 mapping:

- first target: `d/d log(m^2)`;
- second target: `d/d alpha3`;
- `alpha4`: **cubic-TT blind** because `L4[K]` starts quartic.

The Iteration-163 six-row saturation numerics are unchanged.  Preserve the historical files and cite:

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights: comparator foundation 25%; robust unique residual 20%; frozen parent dynamics/ANSATZ 20%; candidate consistency 15%; identifiability/Fisher 10%; resource/experiment closure 10%.

Current accounting:

- comparator foundation `23/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS: 23%` — up from `22%` in Iteration 163 by one comparator-foundation point only.  The temporary enriched `dalpha3` residual receives **zero** residual-readiness points because missing comparator columns are BLOCKED, not zero.

## Frozen protocol and gate discipline

Reduced conceptual coordinates after hard locks remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

For the current ordered-response subproblem, the authoritative finite protocol now contains **12 frozen TT rows**: the original six plus six new rows fixed in Iteration 164 by target-independent kinematics.

New-row generator:

- RNG seed `164031`;
- time components uniform `[0.08,0.24]`;
- spatial components iid uniform `[-0.68,0.68]`;
- accept only `0.18<=p^2,q^2,r^2<=1.05`;
- require spatial `|cos(q,r)|<=0.82`;
- require invariant ratio `max/min<=4`;
- take the first six accepted proposals (after 16 proposals);
- polarization seeds `2000+3*i+leg`.

No target value enters row generation or acceptance.

Novelty pre-gate remains

`r_beta=(I-MM^+)b`.

Hard constraints precede profiling/Fisher. Unsupported comparator entries are BLOCKED, never zero-filled. No frozen gate may be weakened post hoc.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-021`.

## C3 status

Fixed postquantum-classical comparator retained.

- linear `N2=A(5D2+D0)`, rank `1/2` in `(D2,D0)`;
- nonlinear symmetric cumulant from the same covariant OM action gives supported `(N2,C3sym)` rank `2/2` for physical `D2>0`;
- tree causal response `chi2R=-G_R Gamma3_EH G_R G_R` is the common GR boundary after hard Newton calibration and is therefore already represented by the EH column on the enriched TT rows.

BLOCKED: diffusion-dependent ordered/MSR-loop corrections, exact `chi2R_odd`, non-TT completion, threshold, full enriched C3 quotient.

## C4 status — `C4-DRGT-001`

Frozen point remains `m^2=0.04`, `alpha3=0`, `alpha4=0`.

Iteration 163 six-row matrix

`M6=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`

has rank `6/6`; both **correctly labelled** targets `dlogm2,dalpha3` are absorbed to numerical precision there.  Classification remains `REGIME_SPECIFIC_NON_IDENTIFIABILITY / SIX_ROW FINITE_PROTOCOL SATURATION`.

Iteration 164 enriched matrix with the same six columns has shape `12x6`, rank `6`, and no longer saturates the row space.

With the two corrected target columns:

- `rank([M12,dlogm2])=7`;
- `rank([M12,dalpha3])=7`;
- `rank([M12,dlogm2,dalpha3])=8`.

Across the four fixed row normalizations:

- `dlogm2` residual fraction = `7.4567e-4 ... 4.7412e-3` -> **near-degenerate, not promotable**;
- `dalpha3` residual fraction = `6.7428e-3 ... 9.1427e-2` -> **scoped residual survives implemented enriched local quotient**, but not the full comparator quotient.

Retain:

- `C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES` (historical scoped six-row result; corrected target labels);
- `C4-NG-005 — SIX_ROW_SATURATION_DOES_NOT_PERSIST_UNDER_TARGET_INDEPENDENT_TT_ROW_ENRICHMENT`;
- `C4-NG-006 — DRGT_DLOGM2_DIRECTION_IS_NEAR_DEGENERATE_AFTER_ENRICHED_LOCAL_C5_QUOTIENT`;
- `NG-FUNNEL-020 — SIX_ROW_TT_PROTOCOL_SATURATED_BY_FIXED_C5_PLUS_SHARED_BOUNDARY`;
- `NG-FUNNEL-021 — PROTOCOL_SATURATION_MUST_BE_TESTED_FOR STABILITY UNDER PRE-FROZEN ROW ENRICHMENT`.

BLOCKED: helicity-0/1, Vainshtein/nonperturbative response, C4 `N2/C3sym`, full enriched quotient.

## C5 status

Retained:

- on-shell local amplitude tangent `12x10`, rank `10/10`, on-shell only;
- source-completed off-shell TT protocol;
- EH + `Ricci^3/Riemann^3` retarded response Ward validated;
- `Ricci^2` and `Ricci Box Ricci` full response tangents include required propagator insertions and completed Ward checks;
- `[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full]` is rank `5` in the original six rows and is evaluated on all 12 frozen rows in Iteration 164;
- `R^2` and `R Box R` remain exact TT-cubic blind directions at this order because `R^(1)[h_TT]=0`.

Retain `C5-NG-001`, `C5-NG-002`, `NG-FUNNEL-019`.

BLOCKED: remaining non-TT/full off-shell local directions, loop/nonanalytic C5, C5 `N2/C3sym` in one finite CTP map.

## Nonlocal status — `NL-WNL-001`

The weakly-nonlocal comparator remains fixed/scoped.  Its local cubic potential directions are already contained in the local C5 nonlinear span.  Full form-factor-induced Lorentzian cubic response, causal completion, and nonlocal `N2/C3sym` remain BLOCKED.  Do not fill the new 12-row columns with a guessed retarded prescription.

## Asymptotic-safety status — `AS-FRG-TT-001`

The Pawlowski–Tränkle FRG/effective-action comparator remains fixed/scoped.

- symmetric-point Euclidean three-graviton data are not the required off-symmetric Lorentzian retarded tangent;
- reconstructed Euclidean curvature-squared action defines off-symmetric Euclidean background vertices in principle within its truncation;
- strict local IR expansion is structurally contained in local C5;
- that strict IR Taylor surrogate is invalid on the current finite Planck-scale probes;
- full nonlocal 12-row `chi2R_even/odd` remains `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

Retain `AS-NG-001/002/003` and `NG-FUNNEL-016/017/018`.

## `ANSATZ-003` state

Still intentionally **not frozen**.  No residual has yet survived the complete enriched fixed C3/C4/C5/nonlocal/AS quotient.

Fisher/resources remain forbidden.

## Iteration 164 authorities

- `analysis/enriched_tt_protocol_iteration164.py`;
- `results/enriched_tt_protocol_iteration164.json`;
- `candidate_gravity/ENRICHED_TT_PROTOCOL_ITERATION164.md`;
- `research_log/2026-08-31_iteration_164_enriched_tt_protocol.md`;
- `recovery/RECOVERY_DELTA_ITERATION_164.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION164.md`.

## Immediate next scientific priority — Iteration 165

Keep all 12 rows frozen.  Do **not** optimize rows around the temporary `dalpha3` residual.

Required order:

1. recognize the C3 tree ordered response as the already-present EH boundary; do not double-count it;
2. instantiate the strongest physically supported enriched nonlocal and/or asymptotic-safety causal ordered-response column from the already-declared dynamics;
3. if the retarded/in-in prescription is not uniquely specified, retain the blocker rather than inventing a column;
4. advance any other fixed comparator component that can be derived without new arbitrary conventions (non-TT/helicity only if its operational source/polarization map can be frozen independently of the target);
5. recompute the full enriched quotient;
6. only if a nonzero residual survives C3/C4/C5/nonlocal/AS may residual-readiness points, `ANSATZ-003`, Fisher, or resources resume.
