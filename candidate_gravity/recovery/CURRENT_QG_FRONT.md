# Candidate Gravity Current Front

**Updated:** 2026-09-06  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: Iteration 411.
- Latest validated structural authority: Iteration 410.
- Latest raw-valid physical blocker: Iteration 421 — `BLOCKED_CONVERGENCE`, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: `[2]`.
- Latest completed numerical mass-support authority: **Iteration 484**, raw-consumed frozen Iteration-455 rank 12 `(u,v)=(+1e-5,-1e-5)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 484**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`17/32 = 53.125%`**, i.e. **`1360/2560`** row occurrences pending rank13 raw-consume.
- Frozen rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Iteration 484 numerical authority
Canonical rank12 run `33997856739`, job `101391409387`, artifact `9979716360`, artifact digest `sha256:ade9b2fbdb7f5ef623dc63c8d757db356c7426f20b6ac2ae5f09528884ce7112`, scientific JSON SHA-256 `a7512548da32e8a5545241d179532dc8b92aec69e5e91d4e4cd40429e83fc8e1`.

At `u=+1e-5, v=-1e-5`: `80/80` finite; max scaled MP80↔MP120 `2.07719600745524401993175741985e-80 <= 1e-30`; max radial Richardson scaled error `2.56858312184114196282042364589e-15 <= 5e-4`. Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK12_FULL_Z_MP80_MP120__NON_PROMOTING`.

This advances local support coverage only. It does not promote physical index 2, does not constitute assembled BASE/HALF derivative authority, and does not alter readiness.

## Iteration 483 retained stencil-sensitivity authority
Occurrence-weighted support coverage is not a proxy for derivative-sensitivity coverage. For frozen central4×central4, total absolute stencil weight per assembly is `9/4`. At raw-certified ranks `0..11`, BASE certified absolute weight is `17/8 = 17/18` of BASE stencil-L1 sensitivity, while HALF certified weight is only `1/36 = 1/81`. HALF-exclusive ranks `19,20,23,24` alone carry `16/9 = 64/81` of HALF absolute stencil weight. No source reorder is authorized.

The exact partial-stencil moment audit was repaired after an infrastructure expectation bug at k=5. Correct full moments for nodes `[-2,-1,+1,+2]` with coefficients `[1/12,-2/3,+2/3,-1/12]` are `[0,1,0,0,0,-4]`. This confirms that partial high-weight coverage is not derivative completion; missing rows must never be zero-filled or promoted.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Two-level truncation order is not identifiable and cannot authorize Richardson promotion.

## Active gate — Iteration 484 anti-idle advance
Before launch, useful RQIR Actions were `0 queued / 0 in_progress`. The exact next frozen coordinate after rank12 PASS is rank13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1.

Rank12 raw-consumption commit `fb341fbd24c90e20a89c5d7725e3432d80a77eb6`; rank13 stage commit `79fc53a326f51cf74ed4ac1bb886a81b1a5a5b91`; workflow commit `d7b337be60781bca4e2b61be9d10fd5b2aea1632`; trigger/head commit `3eb81dee858b86e825939b9fabac65b57f8a1ee5`.

Canonical rank13 run **`34003038811`**, job **`101405200967`**, is active. It is not scientific PASS until its raw artifact is downloaded and fail-closed audited. If and only if rank13 raw-passes, certified occurrence-weighted coverage advances to `18/32 = 56.25%` and the next permitted heavy coordinate is frozen rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1. If rank13 is BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen thresholds. Do not infer alternatives by symmetry and do not run blind remaining-grid sweeps.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 484 closes one additional local numerical support coordinate but no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
