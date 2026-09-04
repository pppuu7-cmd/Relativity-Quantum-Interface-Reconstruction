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
**Latest raw diagnostic consumption:** **Iteration 432**  
**Active deepest-first precision subclosure:** **Iteration 433**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority.

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

Direct original-integrand and structural checks otherwise pass strongly. This remains a convergence/representation blocker, not a Candidate-Gravity consistency FAIL. No coordinate is promoted and no zero fill is allowed.

## Numerical / representation authority retained

- Iteration 419: summation-level binary64 effects alone are insufficient.
- Iteration 422: affine moments `J_0..J_4` stable against 80-digit reference.
- Iteration 425: full fixed-mass `F(u,v)` must be differentiated; denominator-only auxiliary-mass differentiation is forbidden.
- Iteration 426, consumed in 432: phi resolution alone is not material enough to explain the blocker.
- Iteration 427: exact non-measure chain oracle `D_s = H/s^2 + H_alphaalpha/(8s^2) - H_rhorho/(8s)`; at `s=1`, `D_s = H + (H_alphaalpha-H_rhorho)/8`.
- Iteration 428: whole-path symmetric-cross conditioning is severe; outer-only high precision is insufficient.
- Iteration 429: full-F precision manifest requires arbitrary-precision provenance or quantitative retained-binary64 error bounds.
- Iteration 430: deepest-first order originally frozen as `368/370 -> 379/374 -> 407 -> 424 -> 427`.
- Iteration 431 corrected the true inner boundary to Iteration 270 parent primitives `Q0/Q1/Asub/y_down` and recursive numerical dependencies.

## Iteration 432 parent recursive closure

Workflow run `33894344918`, job `101093336026`, completed and uploaded artifact `9945106288`, digest `sha256:4232ad499e6cba069477ce2cad08502b78fd0623306fd303bed3ab101ece8b7a`. Scope is diagnostic/source-provenance only; no physical coordinate is promoted.

The source-level recursive closure confirms that the precision port must begin inside Iteration 270 before any 368/370 certificate can be scientific authority.

## Iteration 433 deepest-first multiprecision subclosure

Purpose: establish 80/120-digit closure first for Iteration-270 primitives `Q0` and `y_down` at frozen representative inputs before moving to `Q1/N1` and `Asub/Acoef/A_finite`.

Prospective frozen acceptance:
- max 80-vs-120 digit discrepancy `<=1e-40`;
- binary64 parent reproduction against 120-digit reference `<=1e-12`;
- finite outputs;
- diagnostic-only scope; no physical `D_s` promotion.

Runs `33898986792` and `33899067536` failed before artifact creation because the clean runner lacked required numerical packages. These are operational failures, not scientific FAILs. The only repair was pinning runner dependencies `numpy==2.1.3`, `mpmath==1.3.0`; scientific inputs, thresholds and conventions were unchanged.

Repaired code commit: `c72b3b27dfec924940b7cdb871e6bb09df1ada0d`.

Current run `33899226761`, job `101109097164`: scientific evaluation, raw authority audit and artifact upload have completed successfully; final workflow teardown was still in progress at the last check. Artifact `9946960234`, digest `sha256:6805d65e4abae5e8cdfbcd34f7e55e84eaaf7fc7e98463d952331bd9387bede8`. The raw payload must be consumed fail-closed before the result is promoted even as diagnostic authority.

## Active Actions / anti-idle

Iteration 433 run `33899226761` is the active useful run. No duplicate heavy run is authorized.

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

1. Raw-consume Iteration 433 fail-closed.
2. If `Q0/y_down` pass, implement a separately auditable 80/120-digit `Q1/N1` closure.
3. Only after `Q1/N1` closure, move to `Asub/Acoef/A_finite` and recursive geometry/traced-numerator layers.
4. Then certify `368/370 -> 379/374 -> 407` under continuous arbitrary-precision provenance or quantitative retained-binary64 bounds sufficient for final gates.
5. Evaluate frozen Iteration 424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427.
6. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass under raw workflow authority.
7. If index 2 closes, execute Iteration 412 exact15 assembly, complete `Tr U1^2`, then assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
8. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change at Iteration 433: **0 percentage points**. No physical coordinate, comparator-subtracted residual or new rubric block has closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
