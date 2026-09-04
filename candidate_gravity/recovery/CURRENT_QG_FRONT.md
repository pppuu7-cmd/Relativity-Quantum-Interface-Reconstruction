# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated physical-blocking result:** **Iteration 421 — raw-valid `BLOCKED_CONVERGENCE` for index 2**  
**Latest raw parent precision/representation authority:** **Iteration 442 consuming Iteration 441 PASS**  
**Active gate:** **next outward dependency precision closure at Iterations 368/370**

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
- Iteration 438: exact `A_finite` arithmetic core PASS on all 26 frozen signed nodes; max 80-vs-120 scaled discrepancy `9.243186772758836e-84`.
- Iteration 439: binary64 `Acoef` signed-sum conditioning diagnostic found max cancellation amplification `1790391356.9083405`, largest for `(s,a,b)`; diagnostic only.
- Iteration 440: frozen `Acoef/Asub` signed assembly raw-valid arithmetic PASS at 80/120 digits. Run `33904321843`, artifact `9948876125`; max 80-vs-120 discrepancy `1.4149749985220297e-75`; diagnostic binary64-vs-120 discrepancy `1.890704312519492e-10`.
- Iteration 441, raw-consumed as Iteration 442: fixed-h finite-amplitude representation/truncation oracle PASS. Run `33904593636`, artifact `9949120808`, artifact digest `sha256:49e17960074953f502fec7672a6e7c67b471dca4882a8426120dea49d2b55e44`, raw JSON SHA-256 `141aa237b79d3acf8ba428c08dbcfe5ca0d81051abff260c3255e7789d37ffae`. At unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`, independent tensor-product fourth-order derivative oracle gives max central-vs-high-order 120-digit scaled discrepancy `4.47609790628742112552755346023e-6 <= 2e-5`; max 80-vs-120 high-order discrepancy `3.39660363388259398057433228844e-75 <= 1e-30`; 124/124 nodes, 7/7 subsets, all finite. Worst subset `(s,a,b)`.

**Consequence:** Iterations 440+441/442 close arithmetic precision and fixed-h stencil representation/truncation for the frozen Iteration-270 `Acoef/Asub` layer. This is parent numerical-method authority only; it does not promote a physical `D_s` coordinate.

## Frozen Iteration 424 physical fallback

Authorized only after the remaining outward precision chain closes. Acceptance remains:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

No smaller physical mass step, angular-grid escalation, threshold weakening or zero fill.

## Frozen Iteration 412 exact15 assembly

Exactly 15 unique double-double indices are required, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates/missing indices/zero fill. It remains BLOCKED until index 2 gets raw-valid physical authority.

## Exact next gates

1. Certify the next outward dependency layer `368/370` under continuous arbitrary-precision provenance or quantitative retained-binary64 bounds sufficient for final gates.
2. Then proceed `379/374 -> 407` under the same precision discipline.
3. Evaluate frozen Iteration 424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427.
4. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass.
5. If index 2 closes, execute Iteration 412 exact15 assembly, complete `Tr U1^2`, then assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
6. Source/Ward/contact+K2 and fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iteration 442: **0 percentage points**. A parent numerical representation ambiguity closed, but no additional stable model-readiness rubric component closed and no new physical coordinate was promoted.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Authoritative iteration numbers are never reused. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
