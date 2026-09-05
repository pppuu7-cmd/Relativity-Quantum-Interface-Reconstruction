# Candidate Gravity Current Front

**Updated:** 2026-09-05  
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
- Latest completed numerical mass-support authority: Iteration 463 raw-consumes canonical run `33957232727` as PASS at `u=-5e-6, v=-1e-5`; non-promoting.
- Latest authoritative research iteration: Iteration 465.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: `7/32 = 21.875%`, i.e. `560/2560` row occurrences.
- Active numerical gate: run `33962417750`, job `101296485227`, at Iteration-455 distinct rank 5, `u=-5e-6, v=-5e-6`, all five training-z, NPHI16, unchanged radial Richardson, direct MP80/120. This is the sole authorized numerical gate; do not duplicate.

## Retained physical authority
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Numerical precision chain
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic. Iteration 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463 progressively close direct-parent full-training-z mass support. Iteration 454 rejects `u<->v` deduplication. Iteration 455 freezes exact support order. Iteration 457 proves the four exact BASE/HALF coordinate overlaps may share one `F(u,v)` precision certificate but must retain separate derivative weights.

## Iteration 458 assembly-level precision barrier
The authoritative Iteration-407 mixed auxiliary-mass derivative uses tensor-product central4 first derivatives with coefficients `[1/12,-2/3,+2/3,-1/12]/h`. BASE and HALF are formed separately; the frozen physical quantity retains `ds=-d_base`, while BASE/HALF disagreement is a separate mass-step convergence test. There is no BASE/HALF Richardson extrapolation.

The first-derivative coefficient L1 sum is exactly `3/2`, hence the tensor mixed-derivative pre-scaling L1 sum is `9/4`. Therefore error-amplification norms are BASE `9.0e10` and HALF `3.6e11`. Local fixed-mass MP80/120 PASSes are necessary but do not by logic alone certify the assembled derivative.

After all 28 distinct `F(u,v)` coordinates have local certificates, assemble BASE and HALF independently at MP80 and MP120, require all finite, require each assembled scaled MP80↔120 discrepancy `<=2e-6`, retain BASE↔HALF physical mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Only after that PASS may frozen Iteration 424 be reevaluated.

## Iteration 460 cancellation/provenance augmentation
The post-support assembly gate must additionally report, independently for BASE/HALF and MP80/MP120, `D=sum_i w_i F_i`, `S_abs=sum_i |w_i F_i|`, `kappa_cancel=S_abs/max(|D|,tiny)`, and `B_80_120=sum_i |w_i||F_i^80-F_i^120|`. The triangle inequality requires direct `|D80-D120| <= B_80_120` apart from explicitly bounded assembly roundoff. Violation is implementation/provenance `BLOCKED`, not physics FAIL. Large `kappa_cancel` is conditioning/near-cancellation evidence only; it cannot weaken frozen thresholds or support novelty/non-identifiability claims. The Iteration-458 scaled assembled MP80↔MP120 threshold `<=2e-6` remains unchanged.

## Iteration 462 exact operator sanity contract
For the frozen central4 nodes `(-2,-1,+1,+2)` and coefficients `(1/12,-2/3,+2/3,-1/12)`, exact rational moments are `m0=0, m1=1, m2=m3=m4=0, m5=-4`; `L1=3/2` and tensor pre-scaling `L1=9/4`. Hence for every normalized monomial `u^a v^b` with `0<=a,b<=4`, the tensor mixed-derivative moment is exactly 1 only for `(a,b)=(1,1)` and exactly 0 otherwise. After full local support closure, BASE/HALF assembly code must pass exact synthetic probes: constants and pure-u/pure-v degree<=4 annihilate; normalized `u*v` returns one. Failure is implementation/provenance `BLOCKED`, never physics FAIL. This does not alter any Iteration-458/460 threshold.

## Iteration 464 exact truncation diagnostic
Extending the same frozen central4 moments gives exactly `m6=0`, `m7=-20`, `m8=0`, `m9=-84`. Therefore the one-dimensional derivative has the asymptotic form `D_h f = f' - h^4 f^(5)/30 - h^6 f^(7)/252 + O(h^8)`, and the tensor mixed derivative obeys `D_uv,h F = F_uv - h^4(F_{5,1}+F_{1,5})/30 - h^6(F_{7,1}+F_{1,7})/252 + O(h^8)`, with the first product cross-term entering at `+h^8 F_{5,5}/900`. Since `h_HALF=h_BASE/2`, isolated leading `h^4` and `h^6` truncation pieces scale BASE/HALF by exactly `16` and `64`. `(16 D_half-D_base)/15` may be reported only as a diagnostic h4-cancelling combination; it is forbidden as a promoted estimator and cannot replace retained `ds=-d_base` or weaken any frozen threshold. Absence of 16/64 scaling is not itself a physics FAIL because mixed orders/non-asymptotic terms may coexist.

## Iteration 465 two-level truncation-order non-identifiability
With only BASE `B=D(h)` and HALF `H=D(h/2)`, the leading truncation exponent is not empirically identifiable. Under `D(h)=D0+a h^p`, every assumed `p!=0` fits the same pair exactly with `D0(p)=(2^p H-B)/(2^p-1)`. In particular, `p=4` gives `(16H-B)/15` and `p=6` gives `(64H-B)/63`; both exactly fit the same two levels, while their inferred continua differ by `16(H-B)/315`. Classification is `REGIME_SPECIFIC_NON_IDENTIFIABILITY__TWO_LEVEL_TRUNCATION_ORDER__NON_PROMOTING`, scoped strictly to numerical truncation-order identification. It is not Candidate-Gravity model non-identifiability, consistency FAIL, comparator identity, near-degeneracy, or novelty certificate. Iteration-464 factors 16/64 are theoretical single-term signatures only; BASE/HALF alone cannot select between them. A third independent step level or an external continuum/truncation prior would be required to identify order, but no new level is authorized because that would alter the frozen design. No Richardson promotion; retained `ds=-d_base` and all frozen thresholds are unchanged.

## Iteration 463 raw authority
Canonical run `33957232727`, job `101282656909`, artifact `9968019110`, artifact digest `sha256:fa1c16c9860a2f929be9595251ce382ca5fae033ca97fbca869adb021a5e82cd`, scientific JSON SHA-256 `18d2fe2a9eb5a9a6cdbef4010916ef6d045addad8141d269f9a4dc0dbb94db44`. At `u=-5e-6, v=-1e-5`: `80/80` finite, max scaled MP80↔MP120 `2.7478339564891277832684813337e-80 <= 1e-30`, max radial Richardson scaled error `2.56287746810567343755321966286e-15 <= 5e-4`. Non-promoting PASS. The race-duplicate rank-4 run is not independent support and does not increment coverage.

## Active gate
Run `33962417750`, job `101296485227`: raw-consume fail-closed at `u=-5e-6, v=-5e-6` (Iteration-455 distinct rank 5). This exact coordinate has BASE/HALF source multiplicity two; one local `F(u,v)` precision certificate may be shared, but level-specific derivative weights remain distinct. PASS closes only that exact coordinate and permits only distinct rank 6 under the deterministic manifest and unchanged five-z/NPHI16/radial/direct-MP80/120 conventions. BLOCKED requires localization of the first failing sample at exactly the active coordinate. No later coordinate may be launched before raw consumption.

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
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Only exact BASE/HALF coordinate overlaps may share precision certificates, and shared certificates never erase level-specific central4 derivative weights. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact central4 tensor moment sanity probes are mandatory before interpreting assembled failures physically. Central4 BASE/HALF 16/64 asymptotic scaling signatures are theoretical diagnostics only and cannot be empirically identified from two levels alone; no Richardson promotion is authorized. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
