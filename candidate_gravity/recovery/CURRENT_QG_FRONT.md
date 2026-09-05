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
- **Latest exhaustive support-denominator authority:** Iteration 449 — `32 mass nodes x 5 z x 16 phi = 2560` output rows.
- **Active gate:** post-449 same-corner remaining-z MP stage for z=`{-0.43,+0.43}` at `u=v=+5e-6`; workflow intentionally unnumbered until raw consumption.

## Retained physical coordinates

Timelike `Tr U2` before the `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains the physical blocker authority: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain state

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 remains the exact non-measure-chain oracle. Iteration 428 exposes severe whole-path symmetric-cross conditioning. Iteration 431 localizes the inner precision boundary to Iteration-270 primitives. Iterations 436/437 close `N1/Q1` at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic. Iteration 440 closes `Acoef/Asub` 80/120 arithmetic, and Iteration 442 closes the same-h representation/truncation parent layer. Iterations 445 and 446 close the Y-site and continuous post-parent contraction arithmetic on their frozen scopes.

Iteration 447 showed that full fixed-mass sample generation remained uncertified. The post-447 Iteration-407 spectral algebra PASS then closed degree-4 interpolation, affine-log recurrence and terminal spectral assembly **given frozen parent samples** over all 32 mass nodes, with max 80/120 discrepancy `2.4405410844438855e-80`. The actual-cut parent MP pilot likewise passed on eight near-cut samples with max 80/120 discrepancy `4.82848380400305e-81`.

## Iteration 449 selected-slab raw PASS

Run `33928248369`, job `101201330811`, artifact `9958661360`, artifact digest `sha256:16d70f63275c451c15cb13243240612dcdc2fc09f598fe08194b1b91c2ecd3c8`, head `8257cda2607fde9ec73245719b00671a17b43aeb`, raw scientific JSON SHA-256 `d7a148b1f55364145612e3c032aaa13a24634b87bad965a9f40a4d1db2b478bb`.

Classification: `PASS_RAW_CONSUMED_SELECTED_PHI_SAMPLE_SLAB__FULL_SUPPORT_DENOMINATOR_ENUMERATED__NON_PROMOTING`.

Frozen selected slab:
- mass point `u=v=+5e-6`;
- z=`{-0.86,0,+0.86}`;
- all 16 phi nodes;
- radial h=`{2e-3,1e-3,5e-4}`, both signs;
- direct parent recomputation at 80/120 digits.

Observed:
- 48/48 output rows finite;
- max scaled 80/120 discrepancy `1.8767421144249155e-80 <= 1e-30`;
- max radial Richardson scaled error `2.570403982427955e-15`;
- 576 direct parent MP evaluations.

This is a genuine numerical precision PASS for the selected slab only. It does not promote physical index 2.

## Exhaustive frozen sample-support denominator

The retained raw-consumed Iteration-407 support fixes 32 mass nodes, training z=`{-0.86,-0.43,0,+0.43,+0.86}`, and 16 phi nodes. Therefore full sample-generation provenance requires exactly:

`32 x 5 x 16 = 2560` output `(mass-node,z,phi)` rows.

Each row requires 3 radial h x 2 signs x 2 precision levels = 12 direct parent MP evaluations, hence exhaustive support requires `30720` direct parent MP evaluations.

The Iteration-449 selected slab covers `48/2560 = 1.875%` of this numerical-provenance support. This is **not** MODEL_READINESS and not a physical-closure percentage.

At the already-tested mass corner, only z=`{-0.43,+0.43}` remain: 32 output rows / 384 direct parent MP evaluations. That stage has been launched under an unnumbered collision-safe workflow and must be raw-consumed before further mass-node expansion.

## Downstream gates

1. Raw-consume the post-449 same-corner remaining-z stage fail-closed.
2. PASS closes all five frozen z values only at `u=v=+5e-6`; then extend the exact same 80/120 direct-parent sample generation across the remaining frozen mass-node support, without changing phi/radial nodes or thresholds.
3. BLOCKED requires localization of the first failing z/phi/radial sample at unchanged conventions. No resampling, threshold weakening or precision cherry-picking.
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

Readiness change: **0 percentage points**. Iteration 449 closes a real selected-slab precision subgate and enumerates the full numerical support denominator, but no new stable model-readiness rubric point has closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
