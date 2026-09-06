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
- Latest completed numerical mass-support authority: **Iteration 486**, raw-consumed frozen Iteration-455 rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 487**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`18/32 = 56.25%`**, i.e. **`1440/2560`** row occurrences pending rank14 raw-consume.
- Frozen rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Iteration 487 exact two-level truncation authority
For frozen one-dimensional central4 coefficients `c=[1/12,-2/3,2/3,-1/12]` on nodes `[-2,-1,+1,+2]`, exact moments through k=11 are `[0,1,0,0,0,-4,0,-20,0,-84,0,-340]`. The derivative expansion coefficients are therefore `a5=-1/30`, `a7=-1/252`, `a9=-1/4320`.

For the tensor mixed estimator `D_h=L_h^x L_h^y`, comparing BASE step `h` with HALF step `h/2`, the exact asymptotic mismatch through `h^8` is

`D_h-D_{h/2} = -(h^4/32)(f_51+f_15) -(h^6/256)(f_71+f_17) + h^8[-17/73728(f_91+f_19)+17/15360 f_55] + O(h^10)`.

Classification: `PASS_CENTRAL4_TWO_LEVEL_TRUNCATION_MISMATCH_EXACT__NON_PROMOTING`.

This sharpens the retained no-Richardson rule: the two-level BASE↔HALF discrepancy is generically a mixture of independent higher-derivative tensors rather than one identifiable `h^p` mode. Two levels alone therefore do not identify truncation order and do not authorize Richardson promotion. Frozen `ds=-d_base`, assembled MP80↔MP120 threshold `2e-6`, and BASE↔HALF threshold `2e-5` remain unchanged. Violation of the exact estimator identity is implementation/provenance `BLOCKED`, not Candidate-Gravity consistency FAIL.

## Iteration 486 numerical authority
Canonical rank13 run `34003038811`, job `101405200967`, artifact `9981274527`, artifact digest `sha256:020b0bcc7f5dc9addb305d999996c60dce3b39755df0d33ab621567e82eb7e6a`, scientific JSON SHA-256 `a4dda8d7e6ec15a40f09bc8d996850a5d13eba078ed6f14fb91aebdcba9ff2f1`.

At `u=+1e-5, v=-5e-6`: `80/80` finite; max scaled MP80↔MP120 `2.73638650835045783979016930046e-80 <= 1e-30`; max radial Richardson scaled error `2.57164812525073028434007436334e-15 <= 5e-4`. Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK13_FULL_Z_MP80_MP120__NON_PROMOTING`.

This advances local support coverage only. It does not promote physical index 2, does not constitute assembled BASE/HALF derivative authority, and does not alter readiness.

## Iteration 485 exact shared-overlap weight authority
For frozen central4 mixed-derivative weights `w_ij=c_i c_j/h^2`, each of the four exact BASE/HALF shared physical coordinates `(±5e-6,±5e-6)` obeys the exact identity

`w_HALF = w_BASE / 16`

with the same sign. BASE sees these points as inner `±h_B` nodes with `|c|=2/3`; HALF has `h_H=h_B/2` and sees the same physical points as outer `±2h_H` nodes with `|c|=1/12`. Hence the coefficient-product ratio is `1/64`, the inverse-step-squared ratio is `4`, and the net HALF/BASE weight ratio is `1/16`.

This strengthens Iteration 457 without changing it: an exact overlap may share a local MP precision certificate for the sampled `F(u,v)`, but the derivative contribution weight must remain level-specific. Reusing the BASE contribution weight in HALF (or vice versa) would be an exact factor-16 assembly error. Classification: `PASS_SHARED_BASE_HALF_CERTIFICATE_WEIGHT_RATIO_EXACT__NON_PROMOTING`. Any violation is implementation/provenance `BLOCKED`, not a Candidate-Gravity consistency FAIL.

## Iteration 483 retained stencil-sensitivity authority
Occurrence-weighted support coverage is not a proxy for derivative-sensitivity coverage. For frozen central4×central4, total absolute stencil weight per assembly is `9/4`. At raw-certified ranks `0..11`, BASE certified absolute weight is `17/8 = 17/18` of BASE stencil-L1 sensitivity, while HALF certified weight is only `1/36 = 1/81`. HALF-exclusive ranks `19,20,23,24` alone carry `16/9 = 64/81` of HALF absolute stencil weight. No source reorder is authorized.

The exact partial-stencil moment audit was repaired after an infrastructure expectation bug at k=5. Correct full moments for nodes `[-2,-1,+1,+2]` with coefficients `[1/12,-2/3,+2/3,-1/12]` are `[0,1,0,0,0,-4]`. This confirms that partial high-weight coverage is not derivative completion; missing rows must never be zero-filled or promoted.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484/486 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct. Iteration 485 makes that distinction quantitative: at every shared overlap the HALF mixed-derivative weight is exactly `1/16` of the BASE weight, with the same sign. Iteration 487 fixes the exact two-level central4 truncation mismatch structure and reinforces that two levels cannot identify a unique truncation power.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Two-level truncation order is not identifiable and cannot authorize Richardson promotion.

## Active gate — Iteration 487
Rank13 raw-passed and was consumed in Iteration 486. The exact next frozen coordinate remains rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1. Canonical rank14 run **`34008118612`**, job **`101418951867`**, head SHA `1f0b876dc4178e4aaa4935c01455741dd81fd2c9`, is the sole authorized heavy gate and remains `in_progress`. It is not scientific PASS until its raw artifact is downloaded and fail-closed audited. If rank14 is BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen thresholds. If and only if rank14 raw-passes, raw-consume it and advance only to the next UNTESTED coordinate from the frozen Iteration-455 manifest. Do not infer alternatives by symmetry and do not run blind remaining-grid sweeps.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 487 closes an exact estimator/truncation provenance subgate but no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
