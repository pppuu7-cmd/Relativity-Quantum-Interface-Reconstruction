# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated numerical-method diagnosis:** **Iterations 419 + 422 under prospective Iteration-420 contract**  
**Latest source-of-truth reconciliation:** **Iteration 423**  
**Latest prospective numerical fallback contract:** **Iteration 424**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority.

## Authoritative physical/operator state

### Determinant `e=0,c<=3`

Iteration 383 closes the ordinary-two-simple-particle determinant absorptive vector: `q^2=-1 -> -0.002357789063884683 i`, `q^2=-0.34 -> +0.001462759351572654 i`, `q^2=-0.14 -> +0.0012389565044298413 i`. Iteration 387 preserves the evanescent/R2 warning: the hard-branch discontinuity is valid but the full finite local/rational DR remainder remains BLOCKED. This is not a Candidate residual.

### Timelike `Tr U2` — COMPLETE OPERATOR COORDINATE

Iteration 405 raw-validates exact 48/48 repeated-cut assembly: run `33832181526`, artifact `9922054102`, digest `sha256:1dd9bbc6c863954059263171c5a160510ce3605bb416a46498c3453b48343729`, result SHA-256 `f766c6641fb9a89838784ae7572fa1f8459dd0260fd71007f8de93e727840cab`.

Iteration 406 complete timelike coordinate, still before `+i/2`:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Iterations 416/417 do not reopen this authority; both had post-science raw-output parsing/audit failures and are operational/audit failures, not scientific FAILs.

### Timelike `Tr U1^2`

Frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.

Closed components:
- Iteration 374 simple-simple 6/6: `[-1:+6.253219881951187e-05, -0.34:+3.5044107116946374e-05, -0.14:+2.9297648005638963e-05]`;
- Iteration 393 simple-double 36/36: `[-1:-0.002329411286740447, -0.34:-0.0005948791870822445, -0.14:-7.368142632096214e-05]`;
- Iteration 399 double-double index 5 / class 8 / `q^2=-0.14`: `+0.000119747535002548`;
- Iteration 409 index 4 / class 5 / `q^2=-1`: `+0.003562716046166582`, mass-step error `1.694511628814576e-05 < 2e-05`, direct original-integrand cross-check `2.0657185788308663e-09 < 2e-06`;
- Iteration 411 index 11 / class 16 / `q^2=-0.34`: `+0.013050543643260309`, mass-step error `5.421327239850046e-06 < 2e-05`, direct cross-check `1.1526331104849685e-12 < 2e-06`.

**Exact unresolved double-double physical set: `[2]`.** Index 2 / class 3 / `q^2=-1` remains `BLOCKED_CONVERGENCE`. Iteration 411 discrepancy was `5.0042074065288766e-05 > 2e-05`. Iteration 413 refined-step discrepancy worsened to `2.769196909034482e-04 > 2e-05`; its diagnostic value is not authority. No blind angular-grid escalation or further blind `h` refinement is authorized.

## Numerical-method authority for index 2

Iteration 415 established observed refinement order `-2.4682571634198707` instead of expected `+4`, localizing the issue to cancellation/conditioning or the derivative representation.

### Iteration 419 — raw-valid cancellation audit

Run `33867065291`, job `101004215030`, artifact `9936648612`, artifact digest `sha256:6d6c12547c85df99444a9ca18bceee43cd1cd335af149598b143507d9e8b32fd`, raw scientific JSON SHA-256 `978f611512859a618175da5e5c9d54ab05475c58c929e4dd105635906601a3c5`.

Classification: `PASS_CHANNEL2_MASS_DERIVATIVE_CANCELLATION_AUDIT__DIAGNOSTIC_ONLY`.

Prospectively frozen Iteration-420 materiality threshold: `6.922992272586205e-05`.

Observed:
- `max_binary64_roundoff_bound_scaled = 6.830096385136159e-07`;
- `max_naive_vs_compensated_scaled_delta = 1.4886690874290067e-08`.

Both are far below the frozen threshold, so the canonical decision is `SUMMATION_LEVEL_BINARY64_CANCELLATION_NOT_MATERIALLY_SUFFICIENT`. The mixed derivative is severely conditioned, but summation-level binary64 effects do not materially explain the observed physical mass-step drift. Iteration 419 is diagnostic-only and promotes no `D_s` coordinate.

### Iteration 422 — raw-valid affine-moment conditioning audit

Run `33872242674`, artifact `9936404619`, digest `sha256:44dc4cedd992bc402e773592c34aa51e9e65c039671c1393ceaa12913bb0aa43`, scientific JSON SHA-256 `790631db3b782f684653292ca45633839f8de396f3fe0d7d8c3d08869cf73075`.

Classification: `PASS_CHANNEL2_AFFINE_MOMENT_CONDITIONING__FLOAT64_STABLE_DIAGNOSTIC_ONLY`.

- max float64-vs-80-digit `J_0..J_4` discrepancy: `1.8927180676033106e-14 < 1e-10`;
- degree-4 interpolation Vandermonde condition number: `32.67245147666588 < 1e3`;
- max analytic recurrence cancellation factor: `17.53621242151807`;
- minimum affine endpoint denominator magnitude: `0.11857147221810008`.

Therefore arbitrary-precision replacement of the affine analytic moments alone is not justified. Remaining numerical suspicion is localized to mass-cancellation itself and/or traced-numerator / phi-mean / radial fixed-mass evaluation.

## Active computation — Iteration 421

Repaired symmetric-cross physical gate run `33871920373`, job `101019660127` is `in_progress` and is the useful active physical computation. It is not duplicated.

Raw consumption is fail-closed. Besides the unchanged physical threshold `2e-5` and existing direct/original-integrand requirements, the prospectively frozen addendum requires the full tensor-degree-(1,1) fit residual `<=2e-5`.

## Prospective Iteration 424 high-precision fallback contract

Iteration 424 is methodological-only and promotes no physical coordinate. It is authorized only if Iteration 421 remains `BLOCKED_CONVERGENCE`.

The fallback preserves the same parent dynamics, routing, numerator, sign, normalization, fixed mass nodes and existing mass-step set `{5e-6, 2.5e-6, 1.25e-6}`. It forbids smaller `h`, angular-grid escalation, threshold weakening and zero fill.

Before any fallback result exists, fail-closed acceptance is frozen to require simultaneously:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- full tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

Cross-precision failure is `NUMERICAL_PRECISION_BLOCKED`; cross-precision PASS together with physical mass-step FAIL is `REPRESENTATION_OR_TRUE_MASS_STEP_BLOCKED`; direct-integrand or tensor-fit failure is `REPRESENTATION_CONSISTENCY_BLOCKED`. No branch promotes a coordinate without raw-valid workflow authority.

## Frozen Iteration 412 exact15 assembly

Iteration 412 requires exactly 15 unique double-double indices, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates, no missing indices and no zero fill. It remains BLOCKED until index 2 obtains raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 421 fail-closed.
2. If Iteration 421 is `CONVERGED`, append exactly index 2 to frozen 14/15 staging authority and execute Iteration 412 exact15 assembly; do not invoke the Iteration-424 fallback.
3. If Iteration 421 remains `BLOCKED_CONVERGENCE`, implement the prospectively frozen Iteration-424 80/120-digit fixed-mass fallback exactly as specified. Do not shrink `h`, weaken thresholds, or escalate angular grids.
4. Only after complete `Tr U1^2`, assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
5. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No Candidate residual before comparator quotient closure.

Repeated-cut signs remain frozen: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

No readiness point is added by Iterations 419, 420, 422, 423, or 424. Index 2 remains physically unresolved, exact15 `Tr U1^2` is blocked, and no robust comparator-subtracted residual exists.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
