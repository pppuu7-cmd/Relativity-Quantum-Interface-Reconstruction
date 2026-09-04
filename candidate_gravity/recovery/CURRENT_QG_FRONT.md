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
- Iteration 392 freezes the exact 48-channel topology mask. No-uncut indices are `[4,13,22,27,28,29,30,33,36,39,42,45]`; only these 12 may use `+Infinity` as an empty-set minimum-uncut sentinel. The remaining 36 require finite positive uncut separation.
- Iteration 391 resolves preserved indices 12-13 without reintegration.
- Raw authority from original Iteration 384, topology-aware Iteration 390, Iteration 391, and completed Iteration 394 now resolves **44/48 cut-through-double-pole indices**, all CONVERGED. The exact resolved set is every index `0..47` except `14,15,16,17`.
- Newly consumed Iteration-394 run `33821387558` contributes 14/14 CONVERGED indices `24,25,26,27,32,33,36,37,38,39,42,43,44,45`; all seven Actions authority audits PASS and every `+Infinity` occurs only on the Iteration-392 mask.
- Newly consumed late original-384 artifacts close `34,35,40,41,46,47`, all CONVERGED.
- Newly consumed Iteration-390 artifacts close `4,5,22,23,28,29,30,31`, all CONVERGED; cancelled 390 jobs `14-15` and `16-17` have no scientific value.
- Therefore **the only unresolved repeated-`Tr U2` indices are exactly `[14,15,16,17]`**. No repeated-U2 q2 sum is promoted before those four are raw-resolved.

### Timelike `Tr U1^2`

- Iterations 367-371 invalidate old null-soft pruning, freeze 21 physically distinct numerator+denominator families, and establish 36 surviving multiplicity-two denominator targets.
- Iteration 372 freezes 57 physical channels: 6 simple-simple, 36 simple-double, 15 double-double; exactly 19 per q2.
- Iteration 374 closes 6/6 simple-simple:
  - `q^2=-1`: `6.253219881951187e-05`;
  - `q^2=-0.34`: `3.5044107116946374e-05`;
  - `q^2=-0.14`: `2.9297648005638963e-05`.
- Iteration 393 closes the complete 36-channel simple-double operator coordinate, without `-i/4`:
  - `q^2=-1`: `-0.002329411286740447`;
  - `q^2=-0.34`: `-0.0005948791870822445`;
  - `q^2=-0.14`: `-7.368142632096214e-05`.
- Iteration 398 fail-closed census of Iteration 389 shows 14/15 double-double jobs reached raw authority audit. Channel 5 is the sole pure operational gap; its original scientific step was cancelled with empty raw JSON.
- Channel 4 remains governed by Iteration 395 `BLOCKED_CONVERGENCE`: 8x16 base vs old 6x12 discrepancy `2.792425135668121e-5 > 2e-5`; same-grid phase and h/2 checks pass. The diagnostic candidate is not authority.
- Latest corrected Iteration 397 10x20 attempt was operationally cancelled before producing scientific JSON and has no scientific authority. No further blind angular-grid escalation is authorized.
- Structural inspection of channel 4 / class 5 shows raw denominator multiplicities `2,2,1`: the two repeated groups are the cut pair and exactly one simple uncut propagator remains. On the cut sphere that denominator is affine in the unit direction and can be made `c+a z` by aligning one transverse axis with its projection. This motivates Iteration 401; it does not itself promote a physical value.

## Active computations / resource recovery

- **Iteration 399:** run `33828617524`, job `100886566359`; targeted recovery of only double-double channel 5 using exact Iteration-389 arithmetic under a 70-minute one-channel envelope. Currently in progress. Do not duplicate.
- **Iteration 400:** run `33829453920`; exact targeted recovery of the only unresolved repeated-U2 indices `14,15,16,17`, one channel/job, `max-parallel=4`. It imports Iteration-364 `channel_derivative` verbatim with the same low/high grids, `h`, `h/2`, phase check, normalization and thresholds; Iteration-392 topology mask is binding. Currently all four scientific steps are in progress. Do not duplicate.
- **Iteration 401:** structural analytic-azimuth oracle for double-double channel 4. It is not a new physical integration and may not replace Iteration-395 authority by itself. It prospectively tests: one affine uncut denominator, finite low phi-harmonic content of the stripped numerator, and held-out polynomial representation of its azimuthal mean. If the oracle passes, the next gate is analytic `P(z)/(c+a z)` integration at each frozen auxiliary-mass node plus an independent original-integrand cross-check under the unchanged physical `2e-5` threshold.

## Post-e2 dependency authority

Iteration 386 restores the downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder: scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction: scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains `T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;
- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at Iteration 239/240 authority.

## Exact next gates

1. Consume Iteration 400 fail-closed. If all four indices 14-17 are scientifically resolved, construct an exact one-record-per-index 0..47 manifest and assemble the repeated-cut `Tr U2` q2 vector. Any `BLOCKED_CONVERGENCE` remains BLOCKED; no zero-fill.
2. Once repeated-cut `Tr U2` is exact 48/48, assemble complete `Tr U2` q2-by-q2 as Iteration-361 ordinary-simple zero + Iteration-366 repeated-family simple-simple + complete repeated-cut sector, still without `+i/2`.
3. Consume Iteration 399 fail-closed. If channel 5 resolves, double-double `Tr U1^2` still remains blocked only by channel 4 unless another raw-audited Iteration-389 channel is nonconverged.
4. Consume Iteration 401 structural oracle. If PASS, implement controlled analytic/spectral angular reduction for channel 4; do not launch another blind grid ladder. Any final physical value must pass the unchanged `2e-5` gate and an independent original-integrand cross-check.
5. Assemble double-double q2 sums only after exactly 15 unique scientifically resolved indices exist.
6. After double-double closure, assemble complete `Tr U1^2` as Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without `-i/4`.
7. Only after both operator coordinates are complete assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2.
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

Change through validated Iteration 398 plus exact consumed U2 raw coverage and active Iterations 399-401: `0 pp`. Major operator sub-sectors are close to closure, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 mask. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
