# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 398**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 380 closes the former `q^2=-1` triangle numerical blocker analytically/numerically without threshold weakening.
- Iteration 383 closes the ordinary-two-simple-particle determinant absorptive vector:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
- Iteration 387 preserves the evanescent/R2 warning: the hard-branch discontinuity is valid, but the full finite local/rational DR remainder is still blocked. This is not a full finite determinant and not a Candidate residual.

### Timelike `Tr U2`

- Iteration 361 ordinary-simple sector closes and cancels q2-by-q2.
- Iteration 366 repeated-family simple-simple sector closes 18/18, with q2 sums:
  - `q^2=-1`: `-6.812363349599648e-05`;
  - `q^2=-0.34`: `-8.405976034846215e-05`;
  - `q^2=-0.14`: `-7.069545900379072e-05`.
- Iteration 382 raw-validates frozen repeated-cut arithmetic on global channel 0.
- Iteration 391 resolves preserved indices 12-13 without reintegration.
- Iteration 392 freezes the exact 48-channel topology mask. No-uncut indices are `[4,13,22,27,28,29,30,33,36,39,42,45]`; only these 12 may use `+Infinity` as an empty-set sentinel. The remaining 36 require finite positive uncut separation.
- At least indices `0,1,2,3,6,7,8,9,10,11,12,13,18,19,20,21` are raw-resolved CONVERGED. No q2 sum is authorized before exact 48-index coverage.
- Iteration 390 completed as operationally cancelled; produced raw artifacts must be consumed individually and never zero-filled.

### Timelike `Tr U1^2`

- Iterations 367-371 invalidate old null-soft pruning, freeze 21 physically distinct numerator+denominator families, and establish 36 surviving multiplicity-two denominator targets.
- Iteration 372 freezes 57 physical channels: 6 simple-simple, 36 simple-double, 15 double-double; exactly 19 per q2.
- Iteration 374 closes 6/6 simple-simple:
  - `q^2=-1`: `6.253219881951187e-05`;
  - `q^2=-0.34`: `3.5044107116946374e-05`;
  - `q^2=-0.14`: `2.9297648005638963e-05`.
- Iteration 377 closes repeated-cut kinematics: 51/51 REGULAR, BLOCKED=0.
- Iteration 393 closes the 36-channel simple-double operator coordinate, without `-i/4`:
  - `q^2=-1`: `-0.002329411286740447`;
  - `q^2=-0.34`: `-0.0005948791870822445`;
  - `q^2=-0.14`: `-7.368142632096214e-05`.
- Iteration 385 validates the double-double pipeline on the prospectively selected pilot channel.
- Iteration 395 is the scoped negative convergence result for global double-double index 4 / class 5 / `q^2=-1`: preserved 8x16 base vs old 6x12 discrepancy `2.792425135668121e-5 > 2e-5`, while same-grid phi and h/2 checks pass. Diagnostic `D_s TrU1^2=+2.8139677551950804e-4` is not authority.
- Iteration 396 materializes the exact Iteration-395 raw result and provenance without recomputation.
- **Iteration 398 fail-closed execution census:** Iteration-389 run `33820063115` is now completed/cancelled. Fourteen of fifteen channel jobs reached the raw authority audit. **Channel 5 is the sole pure operational gap:** its scientific step was cancelled at the 35-minute resource boundary, audit skipped, and uploaded scientific JSON is empty. It is not zero, not `BLOCKED_CONVERGENCE`, and not scientific FAIL.
- **Iteration 397 has no scientific authority.** Latest corrected run `33825015898`, job `100875702157`, artifact `9920798871`, digest `sha256:29f6688b9d7b8b670ebe3215d6d68090d532523f1b766b3264ad17256f422ecd`, was cancelled during the 10x20 scientific step at the 55-minute resource boundary. Audit was skipped and scientific JSON is empty. Therefore Iteration 395 remains the channel-4 authority.
- Complete `Tr U1^2` remains BLOCKED until all 15 double-double indices are scientifically resolved; no partial double-double q2 sum may be promoted.

## Active computations / resource recovery

- **Iteration 399:** run `33828617524`; targeted resource recovery for **only Iteration-389 channel 5** is active. It executes the exact existing `iteration389_tru1sq_double_double_full15_parallel_channel.py` with `CHANNEL_INDEX=5`, unchanged physics arithmetic and thresholds, under a 70-minute one-channel resource envelope. No full-15 rerun is authorized and no value may be extrapolated to another channel.
- **Iteration 384 / preserved Iteration 390 material:** continue consumption for repeated `Tr U2` under the immutable Iteration-392 topology mask. Do not duplicate already resolved artifacts.

## Post-e2 dependency authority

Iteration 386 restores the downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder: scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction: scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains `T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;
- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at Iteration 239/240 authority.

## Exact next gates

1. Consume Iteration 399 raw artifact fail-closed. If its inherited Iteration-389 channel-5 result is execution-valid, classify it by the unchanged `2e-5` convergence threshold. If the 70-minute single-channel recovery is again cancelled, do not launch another blind resource repeat; move channel 5 to reduced/analytic angular treatment.
2. Channel 4 remains Iteration-395 `BLOCKED_CONVERGENCE`. Because the corrected 10x20 Iteration-397 attempt ended operationally before producing a value, do not infer convergence or failure. No further angular-grid escalation is authorized; next channel-4 method is analytic/spectral angular reduction or an algebraically reduced equivalent of the same frozen integral.
3. Assemble double-double q2 sums only after exactly 15 unique scientifically resolved indices exist.
4. Continue consuming Iteration-384/390 repeated-`Tr U2` artifacts under Iteration-392 mask; exact 48/48 coverage is mandatory before any repeated-`Tr U2` q2 sum.
5. After double-double closure, assemble complete `Tr U1^2` q2-by-q2 as Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without `-i/4`.
6. After repeated-`Tr U2` closure, assemble complete `Tr U2` q2-by-q2 as Iteration-361 ordinary-simple + Iteration-366 repeated-family simple-simple + complete cut-through-double-pole sector, still without `+i/2`.
7. Only then assemble `D_s Gamma_{e=2}=+(i/2) D_s TrU2-(i/4) D_s TrU1^2` q2-by-q2.
8. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No Candidate residual before comparator quotient closure.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Change through validated Iteration 398: `0 pp`. Execution provenance and the remaining double-double gaps are now exact and fail-closed, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 mask. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
