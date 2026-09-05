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
- **Latest parent precision/representation authority:** Iteration 442 consuming Iteration 441 PASS.
- **Latest Y-site authority:** Iteration 445 PASS, non-promoting.
- **Latest post-parent contraction authority:** Iteration 446 PASS, non-promoting.
- **Latest source/provenance boundary authority:** Iteration 447 PASS, non-promoting.
- **Latest spectral arithmetic authority:** raw-consumed post-447 Iteration-407 spectral-algebra MP PASS, non-promoting.
- **Latest actual-cut parent arithmetic authority:** raw-consumed post-447 class-3 actual-cut parent MP pilot PASS, non-promoting.
- **Latest selected-slab phi/sample authority:** Iteration 449 raw-consumes run `33928248369` as PASS, non-promoting.
- **Latest one-mass-coordinate full-training-z authority:** Iteration 450 raw-consumes run `33932061794` as PASS, non-promoting.
- **Latest authoritative research iteration:** Iteration 451, prospective bounded next-mass-node gate plus provenance-reconciliation guard; non-promoting.
- **Frozen sample-support denominator:** `32 mass nodes x 5 training-z x 16 phi = 2560` output rows.
- **Active numerical gate:** run `33935454815` at first untested Iteration-407 base-stencil source-order coordinate `u=v=-1e-5`, all five training-z, NPHI16, full unchanged radial Richardson, direct MP80/120. Do not duplicate.

## Retained physical coordinates

Timelike `Tr U2` before the `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains the physical blocker authority: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain state

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 remains the exact non-measure-chain oracle. Iteration 428 exposes severe whole-path symmetric-cross conditioning. Iteration 431 localizes the inner precision boundary to Iteration-270 primitives. Iterations 436/437 close `N1/Q1` at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic. Iteration 440 closes `Acoef/Asub` 80/120 arithmetic, and Iteration 442 closes the same-h representation/truncation parent layer. Iterations 445 and 446 close the Y-site and continuous post-parent contraction arithmetic on their frozen scopes. The post-447 spectral algebra closes degree-4 interpolation, affine-log recurrence and terminal spectral assembly given frozen parent samples over all 32 stencil evaluations; actual-cut parent MP pilot also passed on its sampled scope.

## Iteration 450 raw PASS

Run `33932061794`, job `101212520875`, artifact `9959560285`, scientific JSON SHA-256 `2467e807b8b5f1c8a93a83a1e5be2107d2c5ae3d8747bb2f5f586b16501d1c03`.

Raw classification: `PASS_SAME_CORNER_FULL_Z_SUPPORT_MP80_MP120__NON_PROMOTING`.

At mass `u=v=+5e-6`, newly consumed z=`{-0.43,+0.43}`, all 16 phi nodes and radial h=`{2e-3,1e-3,5e-4}` with both signs:
- 32/32 rows finite;
- max scaled 80↔120 discrepancy `2.78393261527753298550080747733e-80 <= 1e-30`;
- max radial Richardson scaled error `1.96385912050971757112266495724e-15`.

Combined with Iteration 449, all five frozen training-z values `{-0.86,-0.43,0,+0.43,+0.86}` are precision-closed at this one mass coordinate. Under the already-frozen Iteration-449 denominator convention this is `80/2560 = 3.125%` numerical sample-provenance coverage. This is not MODEL_READINESS and not physical closure.

## Iteration 451 active gate and provenance guard

Run `33935454815`, head `1b906b9bb9f4061d849a791b14184f1b71fc5cf1`, is the only authorized next-mass-node calculation and was `in_progress` when Iteration 451 was recorded. Frozen scope: `u=v=-1e-5`, all five training-z, NPHI16, radial `{2e-3,1e-3,5e-4}` both signs, direct MP80/120 parent recomputation, exact 80-row census, MP discrepancy `<=1e-30`, unchanged inherited radial threshold, all finite.

GitHub Actions API metadata for Iteration-450 artifact `9959560285` currently reports artifact digest `sha256:ac18e784e54414c89e08830d917679ffe0403028abc5ecf6e4e2cdd289158909`, whereas the committed Iteration-450 records contain `sha256:84509a60d16e660e52c7873261694249e1167f1d95d6a34bd5e91e4026199c54`. The raw scientific JSON SHA-256 above matches the downloaded authority audit. Treat this as an **operational provenance discrepancy**, not a physics FAIL, and reconcile the artifact-digest convention before publication-grade provenance claims. It does not authorize changing any numerical gate.

## Exact next gate

Raw-consume run `33935454815` fail-closed. PASS closes full training-z precision provenance only at `u=v=-1e-5`; then choose the next retained source-order frozen mass coordinate without altering z/phi/radial/precision conventions. BLOCKED requires localization of the first failing z/phi/radial sample at exactly `u=v=-1e-5`. No later mass-node run before raw consumption and no duplicate of the active run.

Only after full `F(u,v)` precision-provenance closure may frozen Iteration 424 be evaluated independently at 80 and 120 digits. Physical acceptance remains: mass-step discrepancy `<=2e-5`, direct original-integrand cross-check `<=2e-6`, tensor-degree-(1,1) fit residual `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, all finite; no smaller physical mass step, angular-grid escalation, threshold weakening or zero fill. Only a full physical PASS can promote index 2 and unblock Iteration 412 exact15.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 451 launches a bounded numerical-support gate and closes a provenance-interpretation ambiguity, but no stable model-readiness rubric point.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
