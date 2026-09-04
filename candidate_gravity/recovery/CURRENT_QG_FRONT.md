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
**Latest raw parent precision closures:** **436 N1, 437 Q1, 438 A_finite, 440 Acoef/Asub arithmetic**  
**Latest raw parent conditioning diagnostic:** **Iteration 439 Acoef signed-sum conditioning**  
**Active gate:** **Iteration 441 fixed-h Acoef/Asub representation/truncation oracle**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority. Authoritative iteration numbers are governed by `candidate_gravity/recovery/ITERATION_ID_REGISTRY.md`.

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

Iteration 421 remains latest raw-valid physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, classification `BLOCKED_CONVERGENCE`. Diagnostic estimate `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority.

Frozen failures:
- `max_stability_scaled = 2.2720400683804223e-05 > 2e-05`;
- `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`.

Direct original-integrand and structural checks otherwise pass. No coordinate is promoted and no zero fill is allowed.

## Parent precision / representation authority

- Iteration 419: summation-level binary64 effects alone insufficient.
- Iteration 422: affine moments `J_0..J_4` stable against 80-digit reference.
- Iteration 425: full fixed-mass `F(u,v)` must be differentiated; denominator-only auxiliary-mass differentiation forbidden.
- Iteration 427: exact non-measure chain oracle retained.
- Iteration 428: whole-path symmetric-cross conditioning severe; outer-only high precision insufficient.
- Iteration 431: true inner precision boundary reaches Iteration-270 parent primitives and recursive dependencies.
- Iterations 436/437: exact N1 and Q1 80/120-digit closures PASS at frozen conventions.
- Iteration 438: exact `A_finite` arithmetic core PASS on all 26 frozen signed nodes. Run `33901348951`, artifact `9947778073`; max 80-vs-120 scaled discrepancy `9.243186772758836e-84`.
- Iteration 439: exact binary64 `Acoef` signed-sum diagnostic PASS. Run `33901517012`, artifact `9947813555`; maximum componentwise cancellation amplification `1790391356.9083405`, largest for `(s,a,b)`. Diagnostic only.
- Iteration 440: exact frozen `Acoef/Asub` signed assembly raw-valid PASS at 80/120 digits. Run `33904321843`, job `101125537041`, artifact `9948876125`, digest `sha256:244e52df6a951a21d5ea20638fdf0d15875a07f6b0b3c77355d5b336cf4b479d`; raw scientific JSON SHA-256 `36ff8634a6bafae0281e99110739416d4a8a6313a62c918a9d12bfebffb6f964`. Max 80-vs-120 `Acoef` scaled discrepancy `1.4149749985220297e-75 <= 1e-30`; all 26 nodes / 7 subsets finite. Diagnostic-only max binary64-vs-120 discrepancy `1.890704312519492e-10`.

Iteration 440 closes arithmetic precision of the signed parent assembly only. It does not close finite-difference truncation.

## Active Actions / anti-idle

Iteration 441 is the active nonduplicating gate. It compares the frozen central two-point-per-axis `Acoef/Asub` stencil against an independent tensor-product fourth-order first-derivative rule using the same base spacings and only `±h, ±2h` nodes:

`f'(0) ~= [f(-2h)-8f(-h)+8f(h)-f(2h)]/(12h)`.

Frozen spacings remain `h1=1e-4`, `h2=5e-4`, `h3=1e-3`; no smaller amplitude h is introduced.

Frozen Iteration-441 acceptance before result:
- max 80-vs-120 high-order discrepancy `<=1e-30`;
- max central-vs-high-order 120-digit scaled discrepancy `<=2e-5`;
- finite outputs;
- exact 124 high-order node evaluations per precision level / seven subsets.

Launch provenance:
- research-log freeze `10f2cc3ec23f11c54a33d34c0a7d9e058f4dbd78`;
- code `8c7f51e8c84a81a708fc146c6f498f290f264111`;
- workflow `ebd52b26936d7f6d15a9541d0cbdcfe5cb0f66b0`;
- run `33904593636`.

## Frozen Iteration 424 fallback

Still authorized only after the inner precision chain is closed. Acceptance remains:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

No smaller physical mass step, angular-grid escalation, threshold weakening or zero fill.

## Frozen Iteration 412 exact15 assembly

Exactly 15 unique double-double indices are required, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates/missing indices/zero fill. It remains BLOCKED until index 2 gets raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 441 fail-closed.
2. If 441 PASS, certify the next outward dependency layer `368/370` under continuous arbitrary-precision provenance or quantitative retained-binary64 bounds sufficient for final gates.
3. Then proceed `379/374 -> 407` under the same precision discipline.
4. Evaluate frozen Iteration 424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427.
5. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass.
6. If index 2 closes, execute Iteration 412 exact15 assembly, complete `Tr U1^2`, then assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
7. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

If Iteration 441 BLOCKS, localize the failing subset/component and replace the finite-difference representation; do not reduce h or weaken thresholds post hoc.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iteration 441 launch: **0 percentage points**.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Authoritative iteration numbers are never reused. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
