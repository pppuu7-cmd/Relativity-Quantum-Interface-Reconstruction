# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated physical-blocking result:** **Iteration 421 — raw-valid `BLOCKED_CONVERGENCE` for index 2**  
**Latest validated numerical/conditioning diagnostics:** **Iterations 419, 422, 428**  
**Latest exact non-promoting derivative-coordinate contract:** **Iteration 427**  
**Latest raw-valid implementation manifest:** **Iteration 429**  
**Latest prospective implementation contract:** **Iteration 430**  
**Prospective authorized physical fallback:** **Iteration 424**, constrained by Iterations 425/427/428/429/430

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority.

## Closed operator coordinates retained

### Timelike `Tr U2`

Iteration 405 raw-validates exact 48/48 repeated-cut assembly. Iteration 406 gives the complete timelike coordinate before the `+i/2` effective-action weight:

- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

### Timelike `Tr U1^2`

Frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.

Closed components retained:
- Iteration 374 simple-simple 6/6;
- Iteration 393 simple-double 36/36;
- Iteration 399 double-double index 5 / class 8 / `q^2=-0.14` = `+0.000119747535002548`;
- Iteration 409 index 4 / class 5 / `q^2=-1` = `+0.003562716046166582`;
- Iteration 411 index 11 / class 16 / `q^2=-0.34` = `+0.013050543643260309`.

**Exact unresolved double-double physical set: `[2]`.**

## Index 2 physical authority

Target: double-double index 2 / class 3 / `q^2=-1`.

Iteration 421 is the latest raw-valid physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, digest `sha256:d75c5063b81e02872fe1255421c62e0679de22ae13fce7e2013358eba73152ff`, scientific JSON SHA-256 `c297cb15b707ef59b9d940c159a1fcb7e9f3a1e64135ccebc077b48a869f5e20`.

Classification: `BLOCKED_CONVERGENCE`; diagnostic estimate only `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is **not authority**.

Frozen failures:
- `max_stability_scaled = 2.2720400683804223e-05 > 2e-05`;
- `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`.

Strongly passing checks:
- direct original-integrand cross-check `2.0658997659274425e-09 < 2e-06`;
- polynomial heldout `7.852876335312509e-16 < 2e-06`;
- affine-denominator `2.220446049250313e-16 < 2e-11`;
- radial Richardson `5.29849601693666e-15 < 5e-4`;
- design condition number `362.20107548262695 < 1000`;
- synthetic oracle `1.6653345369377348e-16 < 1e-12`.

This is a narrow convergence/representation block, not a Candidate-Gravity consistency FAIL. No coordinate is promoted and no zero fill is allowed.

## Numerical and representation authority for index 2

### Iteration 419

Raw-valid cancellation audit: summation-level binary64 effects are far below the prospectively frozen materiality threshold and are not materially sufficient by themselves.

### Iteration 422

Raw-valid affine-moment conditioning audit: max float64-vs-80-digit `J_0..J_4` discrepancy `1.8927180676033106e-14`; Vandermonde condition number `32.67245147666588`. Affine moments alone are not the dominant arithmetic problem.

### Iteration 425

The complete frozen fixed-mass function is

`F(u,v)=1/2 beta(u,v) sum_k c_k(u,v) J_k(cc(u,v),aa(u,v))`.

Auxiliary masses enter the complete kinematics, traced numerator / phi-mean coefficients, affine moments and measure factor. Denominator-only differentiation is algebraically incomplete and forbidden.

### Iteration 427

Raw-valid exact chain reduction for the complete non-measure function `H` gives

`D_s = H/s^2 + H_alphaalpha/(8 s^2) - H_rhorho/(8 s)`.

At target `q^2=-1`, `s=1`:

`D_s = H + (H_alphaalpha - H_rhorho)/8`.

This is non-promoting but provides an independent factorized consistency oracle for the fallback.

### Iteration 428

Raw-valid run `33887682539`, job `101071391720`, artifact `9942518066`, digest `sha256:4cc83230f7571a08995ff2008fd9e3b0900e1908ac818019c12431e7345ccca3`, scientific JSON SHA-256 `d79330bb9ca0a5f8dbeffa012dde391f5e549c530db36f8a090d1477d62116a5`.

Classification: `PASS_CHANNEL2_PRECISION_SURFACE_AND_NODE_CONDITIONING_AUDIT__NON_PROMOTING`.

For the Iteration-421 symmetric-cross quotient, the smallest frozen node `|u|=|v|=2.5e-6` permits only `5e-16` absolute perturbation of the complete signed four-corner numerator to preserve the `2e-5` quotient tolerance, about `2.2518` binary64 epsilons at unit `F` scale for the entire signed sum. This establishes severe whole-path conditioning.

Iteration 428 also confirms that Iteration 424 is a distinct frozen geometry with mass steps `{5e-6, 2.5e-6, 1.25e-6}`, required precision levels 80/120 decimal digits, same mass nodes and no smaller `h`. Outer-only arbitrary precision is diagnostic only and cannot be called a complete 80/120-digit `F` evaluation.

### Iteration 429 — raw-valid full-F precision-closure manifest

Run `33887876664`, job `101072041025`, artifact `9942593929`, digest `sha256:18b10e47179e4bcd464d02d7d63cb4fbfa2a087c3a88c37f84523f7044d82a5f`, raw scientific JSON SHA-256 `e45b004510953ddaa1de7f2be84bb9642bfe9cdc91987396b5fc1947c8e54da1`.

Classification: `PASS_CHANNEL2_FULL_F_PRECISION_CLOSURE_MANIFEST__NON_PROMOTING`.

The complete dependency chain relevant to a true Iteration-424 fallback is bound fail-closed as

`407 -> 379 -> 374 -> 370 -> 368`.

A valid 80/120-digit implementation cannot start at the final mass derivative only. Kinematics/basis, phi mean and degree-4 interpolation, affine moments, radial stripped-limit evaluation, traced numerator transport, nested parent derivatives, and final mass-node/cross-precision logic all require arbitrary-precision provenance or a quantitative lower-precision error bound sufficient for the downstream frozen gates.

### Iteration 430 — deepest-first precision-port contract

Classification: `PASS_CHANNEL2_DEEPEST_FIRST_PRECISION_PORT_CONTRACT__NON_PROMOTING`.

The implementation order is prospectively frozen:

1. Iteration 368/370 traced-numerator primitives;
2. Iteration 379/374 radial stripped-limit wrapper;
3. Iteration 407 complete fixed-mass analytic/spectral `F`;
4. Iteration 424 identical frozen mass nodes independently at 80 and 120 decimal digits;
5. Iteration 427 factorized derivative-coordinate oracle comparison.

For every retained binary64 sublayer, a quantitative error bound must be shown tight enough to preserve the final Iteration-424 gates; otherwise that layer must be ported to arbitrary precision. Passing an inner port stage never promotes `D_s`. More arithmetic digits do not alter finite-difference truncation, and no stencil/node/mass-step change is authorized.

## Active Actions

At the latest checked state:

- Iteration 429 run `33887876664`: scientific calculation, raw authority audit and artifact upload completed successfully and is consumed above.
- Iteration 426 phi-mean 16-vs-32 diagnostic run `33886485823`: still `in_progress` and independent/non-promoting.
- no duplicate Iteration-426 run is authorized.

## Authorized fallback — Iteration 424

Because Iteration 421 is raw-valid `BLOCKED_CONVERGENCE`, Iteration 424 remains authorized.

Frozen acceptance remains simultaneous:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- full tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

Guardrails: same parent dynamics, routing, numerator, sign, normalization and mass nodes; no smaller `h`; no angular-grid escalation; no threshold weakening; no zero fill; full `F` precision provenance required under Iterations 425/428/429/430.

## Frozen Iteration 412 exact15 assembly

Iteration 412 requires exactly 15 unique double-double indices, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates, no missing indices and no zero fill. It remains BLOCKED until index 2 obtains raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 426 fail-closed when its artifact appears; it is diagnostic-only and cannot promote index 2 by itself.
2. Begin only the deepest Iteration-368/370 traced-numerator precision-provenance layer under Iteration 430.
3. Continue outward through 379/374 and then 407 only after each inner layer has arbitrary-precision provenance or a quantitative retained-binary64 bound sufficient for the final gates.
4. Evaluate the exact Iteration-424 frozen mass nodes independently at 80 and 120 digits and compare against Iteration 427.
5. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass under raw workflow authority.
6. If index 2 closes, immediately execute frozen Iteration 412 exact15 assembly, then complete `Tr U1^2` and assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
7. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change at Iteration 430: **0 percentage points**. Iterations 429/430 remove implementation ambiguity but do not close index 2, exact15, a comparator-subtracted residual, or any additional stable-rubric block.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
