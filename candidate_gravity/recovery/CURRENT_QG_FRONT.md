# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated physical-blocking result:** **Iteration 421 — raw-valid `BLOCKED_CONVERGENCE` for index 2**  
**Latest source/dependency precision-boundary authority:** **Iteration 431**  
**Latest raw parent precision closures:** **436 N1, 437 Q1, 438 A_finite**  
**Latest raw parent conditioning diagnostic:** **Iteration 439 Acoef signed-sum conditioning**  
**Active gate:** **Iteration 440 Acoef/Asub 80/120-digit signed-assembly arithmetic closure**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority. Authoritative iteration numbers are governed by `candidate_gravity/recovery/ITERATION_ID_REGISTRY.md` and may not be reused for a different scientific object.

## Retained operator coordinates

### Timelike `Tr U2`
Iteration 406 complete coordinate before `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

### Timelike `Tr U1^2`
Frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.

Retained closures:
- Iteration 374 simple-simple 6/6;
- Iteration 393 simple-double 36/36;
- Iteration 399 index 5 / `q^2=-0.14` = `+0.000119747535002548`;
- Iteration 409 index 4 / `q^2=-1` = `+0.003562716046166582`;
- Iteration 411 index 11 / `q^2=-0.34` = `+0.013050543643260309`.

**Exact unresolved double-double physical set: `[2]`.**

## Index 2 physical authority

Target: double-double index 2 / class 3 / `q^2=-1`.

Iteration 421 remains latest raw-valid physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, classification `BLOCKED_CONVERGENCE`. Diagnostic estimate `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority.

Frozen failures:
- `max_stability_scaled = 2.2720400683804223e-05 > 2e-05`;
- `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`.

Direct original-integrand and structural checks otherwise pass. This remains a convergence/representation blocker, not a Candidate-Gravity consistency FAIL. No coordinate is promoted and no zero fill is allowed.

## Retained numerical / representation authority

- Iteration 419: summation-level binary64 effects alone insufficient.
- Iteration 422: affine moments `J_0..J_4` stable against 80-digit reference.
- Iteration 425: full fixed-mass `F(u,v)` must be differentiated; denominator-only auxiliary-mass differentiation forbidden.
- Iteration 426, consumed under 432: phi resolution alone not material enough to explain blocker.
- Iteration 427: exact non-measure chain oracle `D_s = H/s^2 + H_alphaalpha/(8s^2) - H_rhorho/(8s)`; at `s=1`, `D_s = H + (H_alphaalpha-H_rhorho)/8`.
- Iteration 428: whole-path symmetric-cross conditioning severe; outer-only high precision insufficient.
- Iteration 429: full-F precision manifest requires arbitrary-precision provenance or quantitative retained-binary64 bounds.
- Iteration 431: true inner precision boundary reaches Iteration-270 parent primitives `Q0/Q1/Asub/y_down` and recursive numerical dependencies.
- Iteration 433/434: `Q0/y_down` multiprecision subclosure plus recursive-parent reconciliation.
- Iteration 435: `Q1/N1` conditioning localized; `s` leg amplification `7.651429239818539e11`.
- Iteration 436: exact `geometry -> nhat -> y_down -> norb -> N1` 80/120-digit closure PASS at frozen `h=3e-5`.
- Iteration 437: exact shifted-Q0 `Q1` 80/120-digit closure PASS.
- Iteration 438: exact `A_finite` arithmetic core PASS on all 26 frozen signed nodes. Raw run `33901348951`, job `101115917242`, artifact `9947778073`, digest `sha256:52442233d7b721ef9196033dd392b02c6af4c5145e2b29bd79e7057466b24f1a`; max 80-vs-120 scaled discrepancy `9.243186772758836e-84`, binary64-vs-120 `6.527324701910789e-19`.
- Iteration 439: exact binary64 `Acoef` signed-sum diagnostic PASS. Raw run `33901517012`, job `101116462908`, artifact `9947813555`, digest `sha256:7dc18bb0754513c6334b792a8602b4157734ee720e31050f9c98b5b9b4330397`; maximum componentwise cancellation amplification `1790391356.9083405`, largest for subset `(s,a,b)`. Amplification is diagnostic only and does not promote or block a physical coordinate by itself.

## Active Actions / anti-idle

Iteration 440 is the active nonduplicating deepest-first gate. It evaluates the exact frozen Iteration-270 `Acoef/Asub` signed assembly at 80 and 120 decimal digits using the already raw-valid Iteration-438 `A_finite_mp` implementation.

Frozen Iteration-440 acceptance before result:
- unchanged `M=POS`, `p=P0`;
- unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`;
- exact 26-node / 7-subset census;
- max scaled 80-vs-120 `Acoef` discrepancy `<=1e-30`;
- finite outputs.

Binary64-vs-120 `Acoef` discrepancy is diagnostic only; no post-hoc threshold is attached to it.

Launch provenance:
- code commit `a1b62afb4936d98b069280d25975fd09cade3a25`;
- workflow commit `c84a9991c8d11c5d863d7f8b39bd01e5eeb4d5f9`;
- run `33904321843`.

A PASS certifies signed-assembly arithmetic only. It does not certify finite-difference truncation, alternate-step stability, 368/370, 379/374, 407, frozen Iteration 424, or physical index-2 `D_s`.

## Frozen Iteration 424 fallback

Still authorized only after the inner precision chain is closed. Acceptance remains:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

No smaller `h`, angular-grid escalation, threshold weakening or zero fill.

## Frozen Iteration 412 exact15 assembly

Exactly 15 unique double-double indices are required, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates/missing indices/zero fill. It remains BLOCKED until index 2 gets raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 440 fail-closed.
2. If 440 PASS, freeze a separate `Acoef/Asub` finite-difference truncation / algebraic-derivative consistency gate before any outward precision claim. No post-hoc step tuning.
3. After `Asub` arithmetic plus truncation representation is closed, certify `368/370 -> 379/374 -> 407` under continuous arbitrary-precision provenance or quantitative retained-binary64 bounds sufficient for final gates.
4. Evaluate frozen Iteration 424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427.
5. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass under raw workflow authority.
6. If index 2 closes, execute Iteration 412 exact15 assembly, complete `Tr U1^2`, then assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
7. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iteration 440 launch: **0 percentage points**. Parent precision closure is advancing, but no physical coordinate, comparator-subtracted residual, or stable readiness-rubric block has closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Authoritative iteration numbers are never reused. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
