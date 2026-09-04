# Candidate Gravity Current Front

**Updated:** 2026-09-05  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest raw-valid physical blocker:** **Iteration 421 — `BLOCKED_CONVERGENCE`, double-double index 2 / class 3 / q^2=-1**  
**Latest parent precision/representation authority:** **Iteration 442 consuming Iteration 441 PASS**  
**Latest methodological post-parent contract authority:** **Iteration 444**  
**Latest raw numerical sublayer authority:** **Iteration 445 — Y-site `y1` 80/120 + same-h fourth-order PASS, non-promoting**  
**Active gate:** **Iteration-444 frozen continuous post-parent 7-matmul + trace certificate**, descriptive stage run `33920431333`, job `101177249464`.

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority. Authoritative iteration IDs are never reused; race-created newer registry/recovery state wins.

## Retained physical operator coordinates

Timelike `Tr U2` from Iteration 406 before `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Timelike `Tr U1^2` frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / q^2=-0.14 = `+0.000119747535002548`, Iteration 409 index 4 / q^2=-1 = `+0.003562716046166582`, and Iteration 411 index 11 / q^2=-0.34 = `+0.013050543643260309`.

**Exact unresolved double-double physical set: `[2]`.**

Iteration 421 remains the latest physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain authority

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 is retained as exact non-measure-chain oracle. Iteration 428 exposes severe whole-path symmetric-cross conditioning. Iteration 431 localizes the true inner precision boundary to Iteration-270 primitives. Iterations 436/437 close N1/Q1 at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic over 26 frozen nodes. Iteration 439 diagnoses severe binary64 Acoef cancellation. Iteration 440 closes Acoef/Asub 80/120 arithmetic. Iteration 441, raw-consumed as Iteration 442, closes the fixed-h fourth-order Acoef/Asub representation oracle with unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`.

Iteration 443 identifies the still-uncovered Iteration-368 Y-site derivative and downstream NumPy contraction boundary. Iteration 444 freezes the exact post-parent arithmetic graph: each traced routed amplitude has 3 matrix products per U1 block plus one joining product, exactly **7 matrix multiplications + 1 trace**; the certificate requires continuous 80/120-digit arithmetic, complete representative 368/370 coverage, finite outputs, and max scaled `80-vs-120 <= 1e-30`. Binary64-vs-120 is diagnostic only; outer-only precision around already-binary64 products/trace is forbidden.

## Iteration 445 raw Y-site authority

Prospectively frozen Iteration-443 Y-site stage was raw-consumed after Actions run `33919939617`, job `101175715064`, artifact `9954611316`, artifact digest `sha256:b42764f0b076544e24ab4aec61de824093158afc4f9c7356b2c432df533d87f6`, raw scientific JSON SHA-256 `432499fd8afa13d7acf560ae112c87c11858d3840eaeedd117fcd7607724c5c9`.

At unchanged `h=4e-5`, 80/120 digits and all 3 frozen Y-site pairs:
- max `|y1_80-y1_120| = 4.09656958147226919955796882988e-77 <= 1e-30`;
- max central-vs-same-h-fourth-order scaled discrepancy `3.74207475261066955599469102919e-11 <= 2e-5`;
- 3/3 pairs finite.

Classification: `PASS_ITER445_YSITE_Y1_MP80_MP120_AND_FIXED_H_FOURTH_ORDER_ORACLE__NON_PROMOTING`. Physical authority is unchanged. A race-misnumbered result file under Iteration 444 was removed in commit `bb826570bdbec0695f7dbd7590dfe49963bc8969`; the correct result was stored as Iteration 445 in commit `1abffb0ecb28b3f0d480d46ee2cb36025cc66f27`.

## Active post-parent gate

Code commit `626887eb9a453003383b999103d751bbbb73d0b4`; workflow commit `74910896d64feed84b1f913dfa6803e8020b5387`. Run `33920431333`, job `101177249464` is active. The gate retains the exact Iteration-368 parent matrix values/routing/orientation before any post-parent product, then evaluates all seven matrix products and final trace continuously in multiprecision for all 126 representative contractions = 21 routed classes x 2 probes x orientations A/B/A_SHIFT. Acceptance is max scaled 80-vs-120 `<=1e-30`, 126/126 finite, with binary64-vs-120 diagnostic only. No physical value can be promoted by this gate.

## Downstream exact gates

1. Raw-consume the active post-parent certificate fail-closed. If PASS, close this retained 368/370 post-parent arithmetic sublayer and continue `379/374 -> 407` under the same continuous-precision discipline.
2. Then evaluate the frozen Iteration 424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427. Physical acceptance remains: mass-step discrepancy `<=2e-5`, direct original-integrand cross-check `<=2e-6`, tensor-degree-(1,1) fit residual `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, all finite; no smaller physical mass step, angular-grid escalation, threshold weakening or zero fill.
3. Promote index 2 only if every frozen condition passes.
4. Only then execute Iteration 412 exact15, requiring all 15 unique double-double indices and five valid records per q^2, then assemble complete `Tr U1^2` and `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2.
5. Comparator quotient / Source-Ward-contact+K2 / C3-C5 / nonlocal / asymptotic-safety closure remains downstream. Source/Born subtraction only in the matched observable after pole/cut-origin classification. No candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iteration 445: **0 percentage points**. Numerical sublayers closed, but no additional readiness-rubric component and no new physical coordinate closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Authoritative IDs are never reused. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
