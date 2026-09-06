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
- Latest completed numerical mass-support authority: **Iteration 496**, raw-consumed frozen Iteration-455 rank17 `(u,v)=(-5e-6,+2.5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 497**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`22/32 = 68.75%`**, i.e. **`1760/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 496 rank17
Canonical rank17 `(u,v)=(-5e-6,+2.5e-6)`, multiplicity 1: run `34023698421`, job `101460814699`, artifact `9987620391`, head SHA `53073d90567b5008cdf3e6abbdeeaef28729a3da`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK17_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:2261cc2f614d05d37430911767bda269d580a34eed245f2de8a031f7d2e4d454`. Scientific JSON SHA-256: `17b9bbd89c52870e1dd9d9bc2078eef073da289ee5763e520a78bc20496d8264`. Authority-audit SHA-256: `6271ede85b66902fe7e83107d238e7992ec7679330c880e32f01603ee355818a`.

Observed: `80/80` finite; max scaled MP80↔MP120 `3.38081360859608568677860852537e-80 <= 1e-30`; max radial Richardson scaled error `2.56431014631589331516267196272e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, or readiness.

## Latest exact assembly/provenance authority — Iteration 497
Frozen mixed central4 coefficients satisfy `c(-x)=-c(x)` on nodes `[-2,-1,+1,+2]`. Therefore tensor weights obey `w(-x,y)=-w(x,y)`, `w(x,-y)=-w(x,y)`, and `w(-x,-y)=w(x,y)` exactly.

For arbitrary sampled data define

`F_oo(x,y)=[F(x,y)-F(-x,y)-F(x,-y)+F(-x,-y)]/4`.

Exact coefficient comparison proves `D_h[F]=D_h[F_oo]`. Hence every even-in-x or even-in-y sector is annihilated exactly, and the full 16-sample signed assembly equals four positive-quadrant odd-odd orbit differences. Classification: `PASS_CENTRAL4_ODD_ODD_PARITY_PROJECTION_EXACT__NON_PROMOTING`.

This is estimator/assembly provenance only. A violation is implementation/provenance `BLOCKED`, not Candidate-Gravity consistency FAIL. Frozen thresholds, dynamics, source order, BASE/HALF convention and `ds=-d_base` are unchanged.

Reproducible audit: `candidate_gravity/code/iteration497_central4_odd_odd_parity_projection_audit.py`. Result: `candidate_gravity/results/iteration497_central4_odd_odd_parity_projection_audit.json`.

## Retained estimator authority
Iteration 495 gives exact tensor-product reproduction/nullspace: moments through degree four are `M_0..M_4=[0,1,0,0,0]`; tensor moments factor, `D_h(x*y)=1`, and every arbitrary additive field `F_ij=f_i+g_j+const` is annihilated exactly.

Iteration 494 gives exact signed cancellation: positive and negative absolute weight masses are each `9/8`, net weight mass is `0`, L1 mass is `9/4`; `kappa_cancel=(|P|+|N|)/|P-N|` is diagnostic only.

Iteration 492 gives exact worst-case sample-error amplification: `|delta D_BASE| <= (9/4) eps/h^2`; `|delta D_HALF| <= 9 eps/h^2`, exactly four times BASE for the same per-sample absolute-error cap.

Iteration 490 proves exact BASE↔HALF single-mode transfer monotonicity. Iteration 489 retains positive but nonconstant exact transfer `rho(theta)=2A(theta/2)/A(theta)`. Iteration 488 retains exact central4 symbol `A(theta)=i sin(theta)(4-cos(theta))/3`. Iteration 487 retains the exact two-level truncation mismatch showing two levels do not identify a single truncation power. Iteration 485 retains `w_HALF=w_BASE/16` for exact BASE/HALF shared coordinates while derivative weights remain level-specific.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero-fill.

## Frozen numerical/assembly contract
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484/486/489/491/493/496 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while derivative weights remain distinct.

After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Iterations 492, 494, 495 and 497 supply exact error-amplification, signed-cancellation, tensor reproduction/nullspace, and odd-odd parity-projection diagnostics without weakening any frozen gate.

## Active gate — Iteration 497
The frozen Iteration-455 manifest identifies rank18 `(u,v)=(-2.5e-6,-5e-6)`, HALF local index 4, multiplicity 1, as the sole authorized heavy support gate.

Rank18 provenance: raw-consumption prerequisite commit `8d7286167b7f21f73963399be34787772ab96d1b`; stage commit `eac66c603874a3f3fe5edf261dcdfa7088f8adbf`; workflow commit `51f27f468306c0ee4551c26cdf547ddec0a5f122`; trigger/head commit `f14bffa6705217a45ab661378dec9d08bdb058d5`.

Canonical run **`34029482604`**, job **`101476261793`**, is **`in_progress`** on the latest live check. Do not duplicate it. Raw authority audit and artifact consumption are required before any scientific PASS.

If raw PASS, only manifest rank19 `(-2.5e-6,-2.5e-6)`, multiplicity 1, becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 497 closes an exact assembly/provenance subgate but no additional stable-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. Future BASE/HALF assembly must satisfy bilinear normalization, additive nullspace, degree-4 tensor reproduction, and odd-odd parity projection before physical interpretation. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
