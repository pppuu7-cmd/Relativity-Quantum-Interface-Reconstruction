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
- Latest completed numerical mass-support authority: **Iteration 503**, raw-consumed frozen Iteration-455 rank20 `(u,v)=(-2.5e-6,+2.5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 503**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`25/32 = 78.125%`**, i.e. **`2000/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 503 rank20
Canonical rank20 `(u,v)=(-2.5e-6,+2.5e-6)`, HALF local index 6, multiplicity 1: run `34041245929`, job `101508280675`, artifact `9993124996`, head SHA `ce1122519bde0e8c56692ebeda7a854c9dc0a9c3`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK20_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:c657bd01dbfff21b4bb37c6cfccaadc421cc68a2d6d397da7cdbd254e7e7f02f`. Scientific JSON SHA-256: `5bd5af97df1524997ab52a10a58cc4842b65c49091325ba1b57aba6e3d253f1a`. Authority-audit SHA-256: `a38d1260678c07a1c180916a081e86b8bbcc2a2f7fe28713f6dcd3029f09178a`.

Observed: `80/80` finite; max scaled MP80↔MP120 `3.02217788257280141868089115421e-80 <= 1e-30`; max radial Richardson scaled error `2.56742621216093884196200081234e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, comparator novelty, or readiness.

Machine-readable raw-consumption record: `candidate_gravity/results/post502_rank20_raw_consumption.json`.

## Active gate — Iteration 503
The frozen Iteration-455 distinct u-major/v-major support manifest directly identifies rank21 `(u,v)=(-2.5e-6,+5e-6)`, HALF local index 7, multiplicity 1, as the sole authorized heavy support gate after rank20 raw PASS.

Reproducible stage: `candidate_gravity/code/post503_manifest_rank21_full_z_mp_stage.py`. Workflow: `.github/workflows/rqir-post503-manifest-rank21-full-z-mp.yml`. Trigger/head commit: `b4f0bef2a3a55ea2186f3508aacf336e98292320`.

Canonical run **`34048058915`** was **`queued`** on the first Iteration-503 live check. Do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, only frozen manifest rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1, becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Retained exact estimator/provenance authority
Iteration 502 exact h^10 BASE-minus-HALF sector remains `PASS_BASE_HALF_DISCREPANCY_H10_EXACT__NON_PROMOTING`. Iterations 501 and 499 retain the lower-order smooth-field asymptotic discrepancy/truncation series; Iterations 489–490 remain authority that exact spectral transfer is mode-dependent outside the low-frequency asymptotic regime. Iteration 497 odd-odd projection and Iterations 492/494/495 conditioning/reproduction diagnostics remain assembly/provenance authority only. No Richardson promotion; frozen `ds=-d_base` remains unchanged.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority. No zero-fill.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

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

Readiness change: **0 percentage points**. Iteration 503 closes one genuine numerical-support subgate and advances coverage, but no additional stable-rubric model component is completed.

## Exact downstream chain
After complete support closure: independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
