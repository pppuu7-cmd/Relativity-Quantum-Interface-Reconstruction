# Candidate Gravity Current Front

**Updated:** 2026-09-06  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest validated structural authority: **Iteration 410**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: **`[2]`**.
- Latest completed numerical mass-support authority: **Iteration 505**, raw-consumed frozen Iteration-455 rank21 `(u,v)=(-2.5e-6,+5e-6)`, HALF local index 7, multiplicity 1.
- Latest authoritative research iteration: **Iteration 507**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`26/32 = 81.25%`**, i.e. **`2080/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 505 rank21
Canonical rank21 `(u,v)=(-2.5e-6,+5e-6)`, HALF local index 7, multiplicity 1: run `34048058915`, job `101526571416`, artifact `9995075679`, head SHA `b4f0bef2a3a55ea2186f3508aacf336e98292320`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK21_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:2d36e21cee40d46ac8ea66c9e62588567d34459ea5d5d6d8bc4322a1c2de56a5`. Scientific JSON SHA-256: `a032df9c94b2eecbf41aade69b94c12522b4893f5d0942f5958054eb8d052f43`. Authority-audit SHA-256: `11004f720fd0e34f86b89b30258190beb7292e4862d1c0e6bfc06318ab1201da`.

Observed: `80/80` finite; max scaled MP80↔MP120 `2.85307369375164535133530348086e-80 <= 1e-30`; max radial Richardson scaled error `2.56469779948098174399002859023e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, comparator novelty, or readiness.

Machine-readable raw-consumption record: `candidate_gravity/results/post504_rank21_raw_consumption.json`.

## Active heavy gate — rank22
The frozen Iteration-455 manifest identifies rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1, as the sole authorized heavy support gate after rank21 raw PASS.

Reproducible stage: `candidate_gravity/code/post505_manifest_rank22_full_z_mp_stage.py`. Workflow: `.github/workflows/rqir-post505-manifest-rank22-full-z-mp.yml`. Trigger/head commit: `3c50345c19fff8e41b8333921ff25a6cbf7dbc38`.

Canonical run **`34053331578`**, job **`101540723619`**, is **`in_progress`** on the Iteration-507 live check. Do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, advance only to the preregistered rank23 coordinate below. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Iteration 506 — rank22 prerequisite dynamics/parameter-chain audit
Classification: `PASS_RANK22_PREREQUISITE_DYNAMICS_PARAMETER_CHAIN_EXACT__NON_PROMOTING`.

The active rank22 stage was audited against raw-valid rank21 authority and its frozen parent source chain. It requires the exact rank21 PASS and exact rank22 manifest successor; inherits the sampling/dynamics definitions from `post447_class3_phi_sample_mp_stage.py`; inherits frozen mass binding from `iteration379_tru1sq_double_double_one_channel_pilot.py`; requires `BASE_H=5e-6`; sets `MASS_U=0.5*BASE_H`, `MASS_V=-BASE_H`; preserves the five training-z points, inherited NPHI, MP80/MP120 convention, radial thresholds, and no-promotion/no-threshold-weakening guardrails.

This is source/provenance and parameter-convention authority only. It is not Candidate-Gravity consistency PASS or FAIL, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, not novelty certification, and not physical promotion. Failure of this audit would be operational/provenance BLOCKED.

Reproducible audit: `candidate_gravity/code/iteration506_rank22_prerequisite_dynamics_chain_audit.py`. Machine-readable record: `candidate_gravity/results/iteration506_rank22_prerequisite_dynamics_chain_audit.json`.

## Iteration 507 — frozen post-rank22 successor and suffix preregistration
Classification: `PASS_RANK23_SUCCESSOR_AND_RANK22_27_SUFFIX_PREREGISTERED_EXACT__NON_PROMOTING`.

The frozen Iteration-455 manifest and raw-valid rank21 authority were re-audited without inspecting or predicting the active rank22 numerical result. The remaining manifest suffix is deterministic and all six coordinates have multiplicity 1:
- rank22 `(+2.5e-6,-5e-6)`, HALF local index 8;
- rank23 `(+2.5e-6,-2.5e-6)`, HALF local index 9;
- rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10;
- rank25 `(+2.5e-6,+5e-6)`, HALF local index 11;
- rank26 `(+5e-6,-2.5e-6)`, HALF local index 13;
- rank27 `(+5e-6,+2.5e-6)`, HALF local index 14.

Therefore, if and only if rank22 later receives raw-valid PASS, the sole authorized successor is rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9. No post-hoc coordinate choice, u/v symmetry deduplication, support reordering, threshold change, or surrogate fallback is permitted.

Conditional occurrence-weighted coverage after sequential future raw-valid PASS is preregistered as: rank22 `27/32=84.375%`; rank23 `28/32=87.500%`; rank24 `29/32=90.625%`; rank25 `30/32=93.750%`; rank26 `31/32=96.875%`; rank27 `32/32=100%`. These are arithmetic consequences only and are not PASS claims for unfinished ranks.

Reproducible audit: `candidate_gravity/code/iteration507_rank23_successor_suffix_preregistration_audit.py`. Machine-readable record: `candidate_gravity/results/iteration507_rank23_successor_suffix_preregistration_audit.json`.

No literature refresh was required for Iterations 506–507 because neither advances an external comparator, novelty, phenomenology, or consistency claim.

## Retained comparator preflight authority
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`. The frozen downstream chain places `Source/Ward/contact+K2` before the fixed `C3/C4/C5/nonlocal/asymptotic-safety` comparator quotient. The concrete upstream algebraic target is not yet assembled, so comparator identity, rank loss, near-degeneracy, and novelty are not currently evaluable. This is operational BLOCKED, not scientific FAIL.

## Retained exact estimator/provenance authority
Iteration 502 exact h^10 BASE-minus-HALF sector remains `PASS_BASE_HALF_DISCREPANCY_H10_EXACT__NON_PROMOTING`. Iterations 501 and 499 retain lower-order smooth-field asymptotic discrepancy/truncation series; Iterations 489–490 remain authority that exact spectral transfer is mode-dependent outside the low-frequency asymptotic regime. Iteration 497 odd-odd projection and Iterations 492/494/495 conditioning/reproduction diagnostics remain assembly/provenance authority only. No Richardson promotion; frozen `ds=-d_base` remains unchanged.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority. No zero-fill.

Iteration 507 re-audited the numerical margin: max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` narrowly exceed their frozen `2e-05` limits, while structural, design-conditioning, analytic-denominator, radial and direct-original-integrand crosschecks remain healthy. Thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics, forbids smaller `h`, angular-grid escalation, threshold weakening and zero fill, and does not authorize bypassing ranks 22–27.

## Frozen Candidate Gravity design doctrine
`candidate_gravity/recovery/KG_ARCHITECTURAL_PRINCIPLES.md` remains frozen recovery-level doctrine: KG = minimal established/surviving physics core + minimal irreducible comparator-subtracted novel sector. A comparator-identical residual receives novelty failure, not promotion. No tuning of an independent novelty/holdout gate to force PASS.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 507 removes post-rank22 successor discretion and strengthens recovery/provenance, but no additional stable-rubric Candidate-Gravity component is completed.

## Exact downstream chain
After complete support closure: independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
