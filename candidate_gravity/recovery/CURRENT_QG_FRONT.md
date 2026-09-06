# Candidate Gravity Current Front

**Updated:** 2026-09-06  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused. Detailed retained history remains in prior recovery deltas and research logs.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest validated structural authority: **Iteration 410**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: **`[2]`**.
- Latest completed numerical mass-support authority: **Iteration 491**, raw-consumed frozen Iteration-455 rank15 `(u,v)=(+1e-5,+1e-5)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 492**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`20/32 = 62.5%`**, i.e. **`1600/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial Iteration-455 baseline and must not be relaunched.

## Iteration 491 numerical authority — rank15
Canonical rank15 `(u,v)=(+1e-5,+1e-5)`, multiplicity 1: run `34013432799`, job `101433057311`, artifact `9984278621`, head SHA `57c3cf21ed654dd2bb522266b2c467006e6d47a7`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK15_FULL_Z_MP80_MP120__NON_PROMOTING`.

Scientific JSON SHA-256: `315321a3be63beb64b475365c5cfc9279d1cde955aabb75dfe77c0e61e5ce83e`. Authority-audit SHA-256: `260e5eecbf2970ced14b1e353c67d6eb061b725a8abdc91bcac5d809eb4853b3`.

Observed: `80/80` finite; max scaled MP80↔MP120 `2.36613888732032373699649050709e-80 <= 1e-30`; max radial Richardson scaled error `2.57035803242852824531172395409e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, or readiness.

## Retained estimator authority
Iteration 492 gives the exact worst-case uniform sample-error amplification for the frozen mixed central4 estimator. With `c=[1/12,-2/3,2/3,-1/12]`, `sum_i |c_i|=3/2`, hence `sum_ij |c_i c_j|=9/4`. If every sampled value obeys `|delta F_ij|<=eps`, then `|delta D_BASE| <= (9/4) eps/h^2`; for HALF at step `h/2`, `|delta D_HALF| <= 9 eps/h^2`, exactly four times the BASE bound for the same per-sample absolute-error cap. This is a worst-case estimator/provenance bound only; it neither assumes saturation nor changes frozen MP or BASE↔HALF thresholds.

Iteration 490 proves exact BASE↔HALF single-mode transfer monotonicity. With `t=cos(theta/2)`, `rho(t)=(4-t)/(t*(5-2t^2))` and `d rho/dt = -4 (t-1)(t^2-5t-5) / [t^2 (2t^2-5)^2] < 0`; since `dt/dtheta<0`, `d rho/dtheta>0` on `0<theta<pi`, with `rho(0+)=1`, `rho(pi-)=+infinity`. This is estimator/provenance authority only and gives no generic multimode scalar-transfer or Candidate-Gravity PASS/FAIL.

Iteration 489 retains positive but nonconstant exact transfer `rho(theta)=2A(theta/2)/A(theta)`. Iteration 488 retains exact central4 symbol `A(theta)=i sin(theta)(4-cos(theta))/3`. Iteration 487 retains the exact two-level truncation mismatch showing two levels do not identify a single truncation power. Iteration 485 retains `w_HALF=w_BASE/16` for exact BASE/HALF shared coordinates while derivative weights remain level-specific.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero-fill.

## Frozen numerical/assembly contract
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484/486/489/491 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while derivative weights remain distinct.

After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Iteration 492 additionally supplies the exact absolute sample-error amplification bounds that future assembly diagnostics may compare against without weakening any frozen gate.

## Active gate — Iteration 492
The frozen Iteration-455 manifest explicitly identifies the next UNTESTED coordinate as rank16 `(u,v)=(-5e-6,-2.5e-6)`, HALF local index 1, multiplicity 1.

Rank16 provenance: raw-consumption result commit `8b288f9e7b5b6c6632f0a66484d7dc363331449a`; stage commit `3e513a1f6e41df29fabf702d98c41f08ed418314`; workflow commit `0ddedcfe14fabcce0219616cf4ef0ca99cd5ecdc`; trigger/head commit `097ad5d60787270d4ed3b78f680b34e583c91453`.

Canonical run **`34018646528`**, job **`101447018675`**, remains **`in_progress`** on the latest live check. It is the sole authorized heavy support gate; do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, coverage may advance to `21/32 = 65.625%` and only frozen rank17 `(u,v)=(-5e-6,+2.5e-6)`, multiplicity 1, becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 492 closes an estimator/provenance subgate but no additional stable-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
