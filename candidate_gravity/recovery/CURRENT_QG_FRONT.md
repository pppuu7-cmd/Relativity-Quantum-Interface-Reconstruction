# Candidate Gravity Current Front

**Updated:** 2026-09-05  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority

- **Latest validated physical/operator authority:** Iteration 411.
- **Latest validated structural authority:** Iteration 410.
- **Latest raw-valid physical blocker:** Iteration 421 — `BLOCKED_CONVERGENCE`, unresolved double-double index 2 / class 3 / `q^2=-1`.
- **Exact unresolved physical set:** `[2]`.
- **Latest completed numerical mass-support authority:** Iteration 453 raw-consumes run `33935454815` as PASS at `u=v=-1e-5`; non-promoting.
- **Latest authoritative research iteration:** Iteration 454 — source/algebra audit rejects any assumed `u<->v` mass-support deduplication beyond exact coordinate overlaps; non-promoting shortcut no-go.
- **Frozen sample-support denominator:** `32 source occurrences x 5 training-z x 16 phi = 2560` output-row occurrences. There are 28 distinct mass coordinates because BASE/HALF overlap at four exact coordinates. Iteration 454 confirms that off-diagonal transposed coordinates are not authorized duplicates.
- **Certified occurrence-weighted precision coverage:** 3/32 source occurrences = 240/2560 row occurrences = 9.375%. This includes the overlap certificate at `(+5e-6,+5e-6)` with multiplicity two and `(-1e-5,-1e-5)` with multiplicity one.
- **Active numerical gate:** run `33940931120`, launched at head `cca4489a7a9458234fc5f64d8be3391f4ad90f14`, exactly at `u=-1e-5, v=-5e-6`, all five training-z, NPHI16, full unchanged radial Richardson, direct MP80/120. It remains the sole authorized numerical gate; do not duplicate.

## Iteration 454 mass-swap shortcut no-go

Frozen Iteration-407 kinematics use `lambda=s^2+u^2+v^2-2su-2sv-2uv` and `alpha=-(s+u-v)/(2s)`. The Kallen function, hence `rho` and `beta`, is symmetric under `u<->v`, but

`alpha(v,u)-alpha(u,v)=(u-v)/s`.

Therefore at fixed angular unit an off-diagonal mass swap changes the routed momentum by `p(v,u)-p(u,v)=((u-v)/s)q`. Both Iteration-407 `numerator_at` and `direct_uncut` depend on that routed momentum, and no frozen identity establishes invariance under the q-directed shift. Thus no exact `F(u,v)=F(v,u)` identity is available for support reduction. Retain all 28 distinct coordinates; only the four exact BASE/HALF overlaps established by Iteration 452 may share precision certificates. Classification: `PASS_MASS_SWAP_SHORTCUT_REJECTED__NON_PROMOTING`. This is not a physics consistency FAIL.

## Iteration 453 raw PASS

Run `33935454815`, job `101222379474`, artifact `9961449686`, artifact digest `sha256:800fa05a9891c7cb3890d07c92bc3ab37df8ce22d94d5a2219ca5f58668e9792`, scientific JSON SHA-256 `6da491178860fa75f73e009973e65e1d6ad805648c1717d89219f1c19e7256e8`.

Frozen scope at `u=v=-1e-5`: all five training-z `{-0.86,-0.43,0,+0.43,+0.86}`, all 16 phi nodes, radial h=`{2e-3,1e-3,5e-4}` with both signs, direct MP80/MP120 parent recomputation. 80/80 rows finite; max scaled 80↔120 discrepancy `2.14713728875952584644057620487e-80 <= 1e-30`; max radial Richardson scaled error `2.55677406158203497847579626974e-15`. Numerical precision provenance only; no physical promotion.

## Retained physical coordinates

Timelike `Tr U2` before the `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains the physical blocker authority: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain state

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 remains the exact non-measure-chain oracle. Iteration 428 exposes whole-path symmetric-cross conditioning. Iteration 431 localizes the inner precision boundary to Iteration-270 primitives. Iterations 436/437 close `N1/Q1` at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic. Iteration 440 closes `Acoef/Asub` arithmetic; Iteration 442 closes the same-h representation/truncation parent layer. Iterations 445 and 446 close the Y-site and continuous post-parent contraction arithmetic on frozen scopes. Post-447 spectral algebra and actual-cut parent MP pilot passed on their bounded scopes. Iterations 449/450/453 progressively close direct-parent full-training-z sample support. Iteration 454 forbids further support reduction by an unproved mass-transposition symmetry.

## Active gate

Run `33940931120` is the only authorized next-mass-node calculation at `u=-1e-5`, `v=-5e-6`, all five training-z, NPHI16, radial `{2e-3,1e-3,5e-4}` with both signs, direct MP80/120 parent recomputation, exact 80-row census, MP discrepancy `<=1e-30`, unchanged inherited radial threshold, all finite. No later mass coordinate may be launched before raw consumption of this run.

## Exact next gate

Raw-consume run `33940931120` fail-closed. PASS closes full training-z precision provenance at `(-1e-5,-5e-6)` and permits only the next untested Iteration-407 BASE source-order coordinate under unchanged z/phi/radial/precision conventions. BLOCKED requires localization of the first failing z/phi/radial sample at exactly this mass coordinate.

Only after full `F(u,v)` precision-provenance closure may frozen Iteration 424 be evaluated independently at 80 and 120 digits. Physical acceptance remains: mass-step discrepancy `<=2e-5`, direct original-integrand cross-check `<=2e-6`, tensor-degree-(1,1) fit residual `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, all finite; no smaller physical mass step, angular-grid escalation, threshold weakening or zero fill. Only a full physical PASS can promote index 2 and unblock Iteration 412 exact15.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 454 prevents an invalid support shortcut but closes no stable readiness-rubric point.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
