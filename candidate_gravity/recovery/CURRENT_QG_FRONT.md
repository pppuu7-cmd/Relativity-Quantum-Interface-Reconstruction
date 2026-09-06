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
- Latest completed numerical mass-support authority: **Iteration 489**, raw-consumed frozen Iteration-455 rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 489**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`19/32 = 59.375%`**, i.e. **`1520/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Iteration 489 numerical authority — rank14
Canonical rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1, run `34008118612`, job `101418951867`, artifact `9982729453`, head SHA `1f0b876dc4178e4aaa4935c01455741dd81fd2c9`.

Raw-consumed classification:

`PASS_RAW_CONSUMED_MANIFEST_RANK14_FULL_Z_MP80_MP120__NON_PROMOTING`.

Scientific JSON SHA-256: `9827e95bdd09e5aa843b1043be0cd7cd1b00c7f415d906d331d457c99499b2ad`.
Authority-audit SHA-256: `2b7f07c56ff2a52d45ab4fb154185a3c1539f7661ba4498d174d8b7ad90eb4f5`.

Observed: `80/80` finite; max scaled MP80↔MP120 `2.89900940877784437592586037613e-80 <= 1e-30`; max radial Richardson scaled error `2.56142529133890963682711797799e-15 <= 5e-4`.

This advances local support coverage only. It does not promote physical index 2, does not constitute assembled BASE/HALF authority, and does not change model readiness.

## Iteration 489 exact BASE↔HALF spectral-transfer authority
For frozen central4

`A(theta)=i sin(theta)(4-cos(theta))/3`,

define away from BASE zeros

`rho(theta)=2 A(theta/2)/A(theta)`.

Exact simplification gives

`rho(theta)=(4-cos(theta/2))/(cos(theta/2)*(4-cos(theta)))`,

hence

`D_half/D_base=rho(theta_x)rho(theta_y)`.

For `0<|theta|<pi`, `rho(theta)>0` but is nonconstant. Near zero,

`rho(theta)=1+theta^4/32-theta^6/256+469 theta^8/368640+O(theta^10)`.

Therefore no exact mode-independent scalar maps BASE to HALF over the resolved spectrum. Generic multimode two-level data do not authorize a universal Richardson factor. Classification: `PASS_BASE_HALF_SPECTRAL_TRANSFER_RATIO_EXACT__NON_PROMOTING`.

This is estimator/provenance authority only. It is not Candidate-Gravity consistency PASS/FAIL, comparator identity, model non-identifiability, near-degeneracy, or novelty certificate. Frozen `ds=-d_base` remains unchanged.

## Retained estimator authorities
Iteration 488: exact central4 Fourier symbol `A(theta)=i sin(theta)(4-cos(theta))/3`, with no additional interior blind spot for `0<|theta|<pi`; mixed symbols `D_h=A(theta_x)A(theta_y)/h^2` and `D_half=4 A(theta_x/2)A(theta_y/2)/h^2`.

Iteration 487: exact two-level truncation mismatch

`D_h-D_{h/2}=-(h^4/32)(f_51+f_15)-(h^6/256)(f_71+f_17)+h^8[-17/73728(f_91+f_19)+17/15360 f_55]+O(h^10)`.

Thus two levels do not identify a single truncation power. No Richardson promotion is authorized.

Iteration 485: every exact BASE/HALF shared coordinate obeys `w_HALF=w_BASE/16` with the same sign. A local sampled precision certificate may be shared for an exact overlap, but derivative weights remain level-specific.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484/486/489 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts.

## Active gate — Iteration 489
The exact next frozen coordinate is rank15

`(u,v)=(+1e-5,+1e-5)`, multiplicity 1.

Canonical run **`34013432799`**, job **`101433057311`**, head SHA `57c3cf21ed654dd2bb522266b2c467006e6d47a7`, is **`in_progress`**. It is the sole authorized heavy support gate; do not duplicate it.

After completion, fail-closed raw-consume the artifact. Only on raw scientific PASS may coverage advance to `20/32 = 62.5%` and the next explicit UNTESTED Iteration-455 coordinate be authorized. On BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 489 closes one additional local numerical-support coordinate and an exact estimator/provenance subgate, but no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
