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
- Latest completed numerical mass-support authority: **Iteration 498**, raw-consumed frozen Iteration-455 rank18 `(u,v)=(-2.5e-6,-5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 498**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`23/32 = 71.875%`**, i.e. **`1840/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 498 rank18
Canonical rank18 `(u,v)=(-2.5e-6,-5e-6)`, multiplicity 1: run `34029482604`, job `101476261793`, artifact `9989492191`, head SHA `f14bffa6705217a45ab661378dec9d08bdb058d5`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK18_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:03c0f613abc04d3653b8ec2152a07ddf22c275b93fcbbf72c9ad1826b6e4ddc3`. Scientific JSON SHA-256: `f1dbbb575bfe9d1c531214912039d0bc92ca0f7b0fc11a340204d81a419b8542`. Authority-audit SHA-256: `3c823309226fdc5ef817481d9d9c51ef5e757c7a7270a3581ae1ea531df39021`.

Observed: `80/80` finite; max scaled MP80↔MP120 `1.85854765131259206880892292545e-80 <= 1e-30`; max radial Richardson scaled error `2.56923687047759737861125588118e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, or readiness.

Raw-consumption commit: `44185dd9f05bc996b84a7e4f6fdc85dd8af2b2d8`.

## Retained assembly/provenance authority
Iteration 497 proves exact odd-odd parity projection of the frozen mixed central4 assembly: `D_h[F]=D_h[F_oo]`. This is assembly/checksum authority only and does not license skipping any remaining HALF support node. The post497 HALF parity-orbit audit confirms every remaining rank 18..27 belongs to an incomplete nonzero-coefficient orbit absent an additional independently frozen field-symmetry identity.

Iterations 492/494/495 retain exact error amplification, signed-cancellation, tensor reproduction/nullspace and bilinear normalization diagnostics. BASE/HALF derivative weights remain level-specific even where a local sampled coordinate is shared.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority. No zero-fill.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

## Active gate — Iteration 498
The frozen Iteration-455 manifest identifies rank19 `(u,v)=(-2.5e-6,-2.5e-6)`, multiplicity 1, as the sole authorized heavy support gate after rank18 raw PASS.

Rank19 provenance: prerequisite/raw-consumption commit `44185dd9f05bc996b84a7e4f6fdc85dd8af2b2d8`; stage commit `1f0c7ca747953016abe14f1e0248f8c0c712f378`; workflow commit `10e7d0c74d31de32851d4f7b90f0fe4c789c0870`; trigger/head commit `b4d2d2f75412f783f991804dd06f7f8174767c85`.

Canonical run **`34035315540`**, job **`101492185537`**, is **`in_progress`** on the latest live check. Do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, only the next explicit `UNTESTED` coordinate in the frozen Iteration-455 manifest becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
