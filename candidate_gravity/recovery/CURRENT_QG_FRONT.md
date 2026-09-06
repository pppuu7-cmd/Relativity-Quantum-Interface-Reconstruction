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
- Latest completed numerical mass-support authority: **Iteration 500**, raw-consumed frozen Iteration-455 rank19 `(u,v)=(-2.5e-6,-2.5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 501**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`24/32 = 75.000%`**, i.e. **`1920/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 500 rank19
Canonical rank19 `(u,v)=(-2.5e-6,-2.5e-6)`, multiplicity 1: run `34035315540`, job `101492185537`, artifact `9991366491`, head SHA `b4d2d2f75412f783f991804dd06f7f8174767c85`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK19_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:ae0fb7a2017c48219dc859632c3496f90911c04ca31272de4a8796d4d8d5f9ef`. Scientific JSON SHA-256: `d3afb8b89fb4a4e7ac41767b84630834c4fc660e1d310e65899392bdd49470f2`. Authority-audit SHA-256: `2ecec2b06bafa3b8c30aa3582b08c3cca6da9ffcd18d3388c76eeb0443006ea3`.

Observed: `80/80` finite; max scaled MP80↔MP120 `3.40027675963242142165008504499e-80 <= 1e-30`; max radial Richardson scaled error `2.57110613298711345992132746523e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, or readiness.

Raw-consumption commit: `7d3666346b68d6a7a968b4a4803aeb64a5aaf30a`.

## Latest exact estimator/provenance authority — Iteration 501
From the frozen Iteration-499 mixed-central4 smooth-field series, the exact BASE-minus-HALF asymptotic discrepancy is

`D_BASE - D_HALF = -h^4/32 S4 - h^6/256 S6 + h^8[-17/73728 Spure8 + 17/15360 Scross8] + O(h^10)`,

where `S4=d_x^5 d_y+d_x d_y^5`, `S6=d_x^7 d_y+d_x d_y^7`, `Spure8=d_x^9 d_y+d_x d_y^9`, and `Scross8=d_x^5 d_y^5`.

Classification: `PASS_BASE_HALF_DISCREPANCY_ASYMPTOTIC_SERIES_EXACT__NON_PROMOTING`. This is smooth-field asymptotic estimator/provenance authority only: no exact mode-independent Richardson identity, no frozen `ds=-d_base` change, no threshold weakening, and no physical promotion. Iterations 489–490 remain authority that exact spectral transfer is mode-dependent outside the low-frequency asymptotic regime.

Iteration 497 exact odd-odd parity projection and Iterations 492/494/495 conditioning/reproduction diagnostics remain retained assembly/provenance authority only. BASE/HALF derivative weights remain level-specific even where a local sampled coordinate is shared.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority. No zero-fill.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

## Active gate — Iteration 501
The frozen Iteration-455 distinct u-major/v-major support order identifies rank20 `(u,v)=(-2.5e-6,+2.5e-6)`, multiplicity 1, as the sole authorized heavy support gate after rank19 raw PASS.

Rank20 provenance: prerequisite/raw-consumption commit `7d3666346b68d6a7a968b4a4803aeb64a5aaf30a`; stage commit `adc06426efed165ce98b9b3cda59b056423f8ef0`; workflow commit `17b54cbea09c9c246ef3d09dcf7bcea2331e42c8`; trigger/head commit `ce1122519bde0e8c56692ebeda7a854c9dc0a9c3`.

Canonical run **`34041245929`** is **`in_progress`** on the Iteration-501 live check. Do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, only the next explicit `UNTESTED` coordinate in the frozen Iteration-455 manifest becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Frozen Candidate Gravity design doctrine

`candidate_gravity/recovery/KG_ARCHITECTURAL_PRINCIPLES.md` is now a frozen recovery-level design doctrine for all future KG construction.

Core rule: **KG = minimal established/surviving physics core + minimal irreducible comparator-subtracted novel sector**, not “new physics only” and not a concatenation of all surviving models. RQIR may use lessons from existing models to constrain the admissible KG design space, but the final novelty result must not be fitted into existence. Training/design, validation, and independent holdout logic must remain distinguishable. A comparator-identical residual receives novelty failure, not promotion. This doctrine is architectural and non-promoting; it does not alter the current numerical gate, physical authority, thresholds, or readiness.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 501 closes an exact assembly-diagnostic subgate only and no additional stable-rubric model component. The architectural doctrine is also non-promoting.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification. Future KG construction must preserve `KG_ARCHITECTURAL_PRINCIPLES.md`: no silent drift to “new physics only”, no mechanical union of comparator models, and no tuning of an independent novelty/holdout gate to force a PASS.
