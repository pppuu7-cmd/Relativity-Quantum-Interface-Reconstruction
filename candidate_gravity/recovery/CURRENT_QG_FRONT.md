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
- **Latest prospective coverage authority:** Iteration 448 — selected-slab/full-`F(u,v)` promotion barrier, non-promoting.
- **Active gate:** post-447 class-3 phi/sample MP stage, run `33928248369`, head `8257cda2607fde9ec73245719b00671a17b43aeb` at launch.

## Retained physical coordinates

Timelike `Tr U2` before the `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains the physical blocker authority: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain state

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 remains the exact non-measure-chain oracle. Iteration 428 exposes severe whole-path symmetric-cross conditioning. Iteration 431 localizes the inner precision boundary to Iteration-270 primitives. Iterations 436/437 close `N1/Q1` at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic. Iteration 440 closes `Acoef/Asub` 80/120 arithmetic, and Iteration 442 closes the same-h representation/truncation parent layer. Iterations 445 and 446 close the Y-site and continuous post-parent contraction arithmetic on their frozen scopes.

Iteration 447 showed that full fixed-mass sample generation remained uncertified: representative-parent MP closure is not automatically continuous cut-momentum MP closure. Iteration 448 now prospectively freezes the coverage/promotion rule for the active sample slab: a selected-slab PASS is non-promoting and cannot be called full-`F(u,v)` closure.

### Raw-consumed spectral-algebra PASS

Run `33924198609`, job `101189000423`, artifact `9957221889`, artifact digest `sha256:67da51140222305be3b293f5289ca62ce6eeda799fb144b8692bdff2d5c213c1`, raw scientific JSON SHA-256 `7f3000cd8e83ce6f1c2d81762273f7960c76e716bd1e4a33f2589c92a9f7090b`.

Classification: `PASS_ITER407_SPECTRAL_ALGEBRA_MP80_MP120__NON_PROMOTING`.

Over all 32 frozen mass nodes, max scaled 80/120-digit discrepancy was `2.44054108444388552441376805074e-80 <= 1e-30`. This closes only degree-4 interpolation, affine-denominator logarithmic recurrence, and terminal spectral assembly **given frozen parent samples**. It does not certify phi/sample generation and does not promote index 2.

### Raw-consumed actual-cut parent MP pilot PASS

Run `33926910105`, job `101197313961`, artifact `9957177323`, artifact digest `sha256:bb04a3ff558e9e90dfad8b3badc75b67947475fb703091a472479dc953cd6a34`, raw scientific JSON SHA-256 `bc1c0560e16221e3b34969bb8682d1f4b709f97f9fd2511472906023c47db26a`.

Classification: `PASS_CLASS3_ACTUAL_CUT_PARENT_MP80_MP120_PILOT__NON_PROMOTING`.

On eight actual near-cut index-2 samples, max scaled 80/120 discrepancy was `4.82848380400305053290438160355e-81`; binary64-vs-MP120 diagnostic drift was `6.95379333966267071268483411462e-16`, far below the `2e-5` physical reference. This rules against gross parent binary64 arithmetic at that sampled point as the dominant Iteration-421 blocker, but does not close phi/sample generation, radial Richardson, mass differentiation, or physical `D_s`.

## Active gate: continuous phi/sample MP slab

Run: `33928248369`

Prospectively frozen selected slab:
- index 2 / class 3 / `q^2=-1`;
- mass point `u=v=+5e-6`;
- `z={-0.86,0,+0.86}`;
- all 16 frozen Iteration-407 phi nodes;
- full inherited radial Richardson nodes `{2e-3,1e-3,5e-4}`, both signs;
- direct parent recomputation at 80 and 120 decimal digits for every radial momentum;
- no binary-parent recast;
- cross-precision threshold `<=1e-30`;
- inherited radial Richardson threshold unchanged.

This is exactly 48 output `(z,phi)` rows and 576 direct parent MP evaluations. Iteration 448 freezes that PASS of these 48 rows is only `REPRESENTATIVE_SLAB_PRECISION_PASS__NON_PROMOTING`. It is not full-z support, not mass-family closure, not full `F(u,v)` provenance and not physical `D_s` authority. No staged coverage percentage may be inferred until the complete frozen support denominator is enumerated from the retained Iteration-407 source.

## Downstream gates

1. Raw-consume run `33928248369` fail-closed under Iteration-448 interpretation.
2. If PASS, enumerate and execute every remaining frozen z-support point at the same mass corner with the same 16 phi nodes and radial Richardson nodes; only then extend across every frozen mass-node family required by index-2 `F(u,v)`.
3. If BLOCKED, localize the first failing z/phi/radial sample at unchanged mass point, routing, dynamics, nodes and thresholds. No resampling or threshold weakening.
4. Only after full `F(u,v)` precision provenance closure evaluate frozen Iteration-424 independently at 80 and 120 digits. Physical acceptance remains: mass-step discrepancy `<=2e-5`, direct original-integrand cross-check `<=2e-6`, tensor-degree-(1,1) fit residual `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, all finite; no smaller physical mass step, angular-grid escalation, threshold weakening, or zero fill.
5. Promote index 2 only if every frozen condition passes.
6. Only then execute Iteration 412 exact15, requiring all 15 unique double-double indices and five valid records per q^2, and assemble complete `Tr U1^2` and `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2.
7. Comparator quotient / Source-Ward-contact+K2 / C3-C5 / nonlocal / asymptotic-safety closure remains downstream. Source/Born subtraction only in the matched observable after pole/cut-origin classification. No candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 448 closes a post-hoc numerical-coverage ambiguity, but no new physical coordinate or rubric point has closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
