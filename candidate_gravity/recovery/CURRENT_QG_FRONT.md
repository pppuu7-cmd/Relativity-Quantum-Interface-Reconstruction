# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 396**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 380 closes the former `q^2=-1` triangle numerical blocker analytically/numerically without threshold weakening.
- Iteration 383 closes the complete channel-resolved ordinary-two-simple-particle determinant absorptive vector:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
- Iteration 387 preserves the evanescent/R2 warning: the full finite local/rational DR remainder is still blocked, but the frozen hard-branch discontinuity above remains valid. It is not a full finite determinant and not a Candidate residual.

### Timelike `Tr U2`

- Iteration 361 ordinary-simple sector closes and cancels exactly q2-by-q2.
- Iteration 366 repeated-family simple-simple sector closes, 18/18 CONVERGED, with q2 sums:
  - `q^2=-1`: `-6.812363349599648e-05`;
  - `q^2=-0.34`: `-8.405976034846215e-05`;
  - `q^2=-0.14`: `-7.069545900379072e-05`.
- Iteration 382 raw-validates the frozen repeated-cut arithmetic on global channel 0: `D_s TrU2=-1.1437983592303379e-05`, convergence `8.280353369982061e-10`, shell `1.6132928326584306e-16`.
- Iteration 391 resolves preserved indices 12-13 without reintegration:
  - index 12, `q^2=-1`: `D_s TrU2=-1.6409523141466878e-05`;
  - index 13, `q^2=-0.14`: `D_s TrU2=-0.0004977890941608628`.
- Iteration 392 freezes the exact 48-channel topology mask. No-uncut indices are
  `[4,13,22,27,28,29,30,33,36,39,42,45]`; only these 12 may use `+Infinity` as an empty-set sentinel for minimum uncut denominator. The remaining 36 must have finite positive uncut separation.
- At least indices `0,1,2,3,6,7,8,9,10,11,12,13,18,19,20,21` are raw-resolved CONVERGED. No q2 sum is authorized before exact 48-index coverage.
- Iteration 390 topology-aware recovery completed as **cancelled**; this is operational cancellation, not scientific FAIL and not zero. Any produced raw artifacts must be consumed individually; no cancelled job may be zero-filled.

### Timelike `Tr U1^2`

- Iteration 367 invalidates historical null-soft singleton pruning on the timelike fixture.
- Iteration 368 freezes all 42 ordered placements NONZERO; cyclic routing leaves 21 classes.
- Iterations 369-370 show all 21 cyclic classes remain physically distinct numerator+denominator families.
- Iteration 371 freezes all 36 multiplicity-two denominator targets as surviving physical double poles.
- Iteration 372 freezes 57 physical channels, exactly 19 per q2: 6 simple-simple, 36 simple-double, 15 double-double.
- Iteration 374 closes the 6/6 physical simple-simple discontinuity:
  - `q^2=-1`: `6.253219881951187e-05`;
  - `q^2=-0.34`: `3.5044107116946374e-05`;
  - `q^2=-0.14`: `2.9297648005638963e-05`.
- Iteration 377 closes the repeated-cut kinematic prerequisite: 51/51 REGULAR, BLOCKED=0.
- Iteration 393 closes the complete 36-channel simple-double operator coordinate, no `-i/4` folded:
  - `q^2=-1`: `D_s TrU1^2=-0.002329411286740447`;
  - `q^2=-0.34`: `D_s TrU1^2=-0.0005948791870822445`;
  - `q^2=-0.14`: `D_s TrU1^2=-7.368142632096214e-05`.
  Envelope: max convergence `1.2832512405556301e-08`, max radial Richardson `9.7822954164134e-15`, max shell `1.9796472878401243e-16`, min uncut denominator `0.1209736845785128`.
- Iteration 385 validates the complete double-double physical pipeline on the first prospectively selected channel: class 1, `q^2=-1`, `D_s TrU1^2=-0.0021448992853041436`, convergence `1.7976503775178967e-06 < 2e-5`.
- **Iteration 395 is a scoped negative convergence result for the sole currently observed blocked double-double channel, global index 4 / class 5 / `q^2=-1`.** It is execution-valid but `BLOCKED_CONVERGENCE`:
  - old 6x12 high mixed derivative `-3.0932102687618925e-4`;
  - new 8x16 base `-2.8139677551950804e-4`;
  - 8x16 phi-shift `-2.900091468025436e-4`;
  - 8x16 h/2 `-2.8071606451092837e-4`;
  - base vs h/2 `6.807110085796765e-7`;
  - base vs phi-shift `8.612371283035585e-6`;
  - base vs old 6x12 `2.792425135668121e-5 > 2e-5` frozen threshold;
  - shell `2.42471651481016e-16`, radial Richardson `8.725618426581871e-15`, min uncut denominator `0.12097107482337414`, serial/parallel oracle `0.0`.
  The diagnostic candidate `+2.8139677551950804e-4` is **not authority** while blocked.
- **Iteration 396** materializes the exact Iteration-395 raw result in-repository without recomputation and freezes its provenance: run `33821555831`, job `100865120160`, artifact `9918963191`, artifact digest `sha256:ecf6b54dea9a2eb8d0231782015b02335c799baa32d5948b385e11cf3c40d30c`, raw SHA-256 `605d121616c36eb144b657d45de7be8a4dfd0d167402ec06eb48308daa8e5634`. Classification: `PASS_MATERIALIZE_ITERATION395_RAW_WITHOUT_RECOMPUTATION`.
- Complete `Tr U1^2` remains BLOCKED until all 15 double-double indices are scientifically resolved; no partial double-double q2 sum may be promoted.

## Active computations / resource recovery

- **Iteration 384:** original 48-channel repeated-`Tr U2` matrix/recovery provenance remains active source material. Do not duplicate already resolved or still-running original jobs.
- **Iteration 389:** run `33820063115`, workflow head `dbc0f1a622b3998132fcf3c1686c2e1033af5add`; full 15-channel double-double matrix, one channel/job, `max-parallel=5`, identical Iteration-385 arithmetic. Current observed state: `in_progress`; multiple per-channel artifacts are already preserved. Do not duplicate active jobs.
- **Iteration 397:** run `33824685271`, head `da7d1ab495551e7257952430ae94d7079ece901d`; prospectively frozen next angular level for **channel 4 only**. It changes only angular quadrature 8x16 -> 10x20; all physics arithmetic and the `2e-5` convergence threshold are unchanged. It tests 10x20 base against preserved 8x16 base, 10x20 half-phi shift and 10x20 h/2. If it remains blocked, no further blind grid escalation is authorized; move channel 4 to analytic/spectral angular reduction.

## Post-e2 dependency authority

Iteration 386 restores the downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder: scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction: scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains `T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;
- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at Iteration-239/240 authority. No same-parent retarded pure-gravity hhh 1PI object with linked K2 normalization and source/Ward completion has been established.

## Exact next gates

1. Consume Iteration 397 raw artifact without threshold weakening. If `CONVERGED`, replace only channel-4 Iteration-389 BLOCKED record with Iteration-397 authority. If still `BLOCKED_CONVERGENCE`, move only channel 4 to analytic/spectral angular reduction; do not launch another blind grid ladder.
2. Consume remaining Iteration-389 per-channel artifacts. Assemble double-double q2 sums only after exactly 15 unique scientifically resolved channel indices exist.
3. Continue consuming original Iteration-384 and preserved Iteration-390 raw artifacts under the immutable Iteration-392 topology mask; merge Iteration-391 indices 12-13 exactly once. Exact 48/48 coverage is mandatory before a repeated-`Tr U2` q2 sum.
4. After complete double-double closure, assemble complete `Tr U1^2` q2-by-q2 as Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without `-i/4`.
5. After complete repeated-`Tr U2`, assemble complete `Tr U2` q2-by-q2 as Iteration-361 ordinary-simple + Iteration-366 repeated-family simple-simple + complete cut-through-double-pole sector, still without `+i/2`.
6. Only then assemble

\[
D_s\Gamma_{e=2}=+\frac{i}{2}D_s\mathrm{Tr}U_2-\frac{i}{4}D_s\mathrm{Tr}U_1^2
\]

q2-by-q2.
7. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No source/Born subtraction before origin accounting. No Candidate residual before comparator quotient closure.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Change through validated Iteration 396: `0 pp`. The remaining double-double blocker is now precisely classified and provenance-complete, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 mask. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
