# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 391**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 380 closes the former `q^2=-1` triangle numerical blocker analytically/numerically without threshold weakening.
- Iteration 383 closes the complete channel-resolved ordinary-two-simple-particle determinant absorptive vector:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
- Iteration 387 sharpens the Iteration-297 regulator warning: evanescent/R2 ambiguity still blocks the **full finite local/rational DR remainder**, but does not invalidate the frozen off-shell one-loop hard branch discontinuity. Therefore the Iteration-383 absorptive vector is retained as hard-cut authority; it is not a full finite determinant and not a Candidate residual.

### Timelike `Tr U2`

- Iteration 361 ordinary-simple sector closes and cancels exactly q2-by-q2.
- Iteration 366 repeated-family simple-simple sector closes, 18/18 CONVERGED, with q2 sums:
  - `q^2=-1`: `-6.812363349599648e-05`;
  - `q^2=-0.34`: `-8.405976034846215e-05`;
  - `q^2=-0.14`: `-7.069545900379072e-05`.
- Iteration 382 raw-validates the frozen repeated-cut arithmetic on global channel 0: `D_s TrU2=-1.1437983592303379e-05`, convergence `8.280353369982061e-10`, shell `1.6132928326584306e-16`.
- Iteration 384 is the complete 48-channel cut-through-double-pole computation, split into fixed two-channel jobs. Raw-valid CONVERGED original chunks currently include `00-01`, `02-03`, `06-07`, `08-09`, `10-11`, `18-19`, `20-21`. These cover indices `{0,1,2,3,6,7,8,9,10,11,18,19,20,21}`.
- The old Iteration-384 wrapper incorrectly required `minimum_sampled_uncut_abs_denominator` to be finite. For topologies in which the cut exhausts all denominator groups, the correct empty-minimum sentinel is `+Infinity`; rejecting it is a wrapper-classification bug, not a physics failure.
- Iteration 388 preserved the formerly lost raw result for indices 12-13. Index 12 was directly CONVERGED. Index 13 had excellent numerical diagnostics but was falsely labelled `FAIL_EXECUTION` only because `umin=+Infinity`.
- **Iteration 391 formally closes that diagnosis without reintegration:** frozen Iteration-359 topology gives index 13 exactly two denominator groups with cut pair `[0,1]`, hence zero uncut groups. Both indices 12 and 13 are therefore CONVERGED. Values:
  - index 12, `q^2=-1`: `D_s TrU2=-1.6409523141466878e-05`;
  - index 13, `q^2=-0.14`: `D_s TrU2=-0.0004977890941608628`.
  Iteration-391 run `33820559335`, job `100862111192`, artifact `9918118094`, raw result SHA-256 `ec9bced6138f631f6d426b69ec5f88cad22afe0e72623e0bac215176bf6bd839`, source Iteration-388 raw SHA-256 `5e7ab80c114f0c178adb4277cc65f161e7fa55a45d8e846c455042d14aa540dd`.
- Thus at this front update **16/48 cut-through-double-pole U2 indices are already raw-resolved CONVERGED**: `0,1,2,3,6,7,8,9,10,11,12,13,18,19,20,21`. No full q2 sum is authorized yet.

### Timelike `Tr U1^2`

- Iteration 367 invalidates historical null-soft singleton pruning on the timelike fixture.
- Iteration 368 freezes all 42 ordered placements NONZERO; cyclic routing leaves 21 classes.
- Iterations 369-370 show all 21 cyclic classes remain physically distinct numerator+denominator families.
- Iteration 371 freezes all 36 multiplicity-two denominator targets as surviving physical double poles.
- Iteration 372 freezes 57 physical channels, exactly 19 per q2: 6 simple-simple, 36 simple-double, 15 double-double.
- Iteration 374 closes the 6/6 physical simple-simple discontinuity, q2 sums:
  - `q^2=-1`: `6.253219881951187e-05`;
  - `q^2=-0.34`: `3.5044107116946374e-05`;
  - `q^2=-0.14`: `2.9297648005638963e-05`.
- Iteration 377 closes the repeated-cut kinematic prerequisite: 51/51 REGULAR, BLOCKED=0.
- Iteration 381 is the full 36-channel simple-double matrix. At this front update **33/36 raw channels are CONVERGED, BLOCKED=0**; validated indices are all except `6,7,8`. The last chunk `06-08` remains in progress. Partial q2 sums are not physical coordinates and must not be promoted before exact 36/36 coverage.
- **Iteration 385 raw-validates the complete double-double physical pipeline on the first prospectively selected channel:** class 1, `q^2=-1`, `D_s TrU1^2=-0.0021448992853041436`, convergence `1.7976503775178967e-06 < 2e-5`, radial Richardson `5.16535599015544e-15`, shell `2.639515599904378e-16`, serial-vs-parallel oracle exactly `0.0`, runtime `944.963664277 s`. Run `33817847310`, artifact `9917692253`, raw SHA-256 `9455e75eaf0e12510113de3bf9e644866a1668ffcc3b629ef8cf15449304c966`.

## Active computations / resource recovery

- **Iteration 381:** run `33816213900`; only simple-double chunk `06-08` remains in progress. Full authority requires exact 36/36 raw index coverage.
- **Iteration 384:** run `33817712381`; original full-48 matrix continues for still-running chunks. Do not duplicate active original jobs.
- **Iteration 389:** run `33820063115`, workflow head `dbc0f1a622b3998132fcf3c1686c2e1033af5add`; full 15-channel `Tr U1^2` double-double matrix, one channel/job, `max-parallel=5`, identical Iteration-385 arithmetic, raw artifact preserved even on non-success status.
- **Iteration 390:** run `33820418026`, workflow head `54a200a941b487cb81940f5256ff94a15d1a1c36`; topology-aware recovery only for previously failed/cancelled Iteration-384 chunks `04-05`, `14-15`, `16-17`, `22-23`, `28-29`, `30-31`. The physical Iteration-364 channel arithmetic and all thresholds are unchanged; only the empty-uncut-set classification is repaired. Chunk `12-13` is excluded because Iteration 391 already resolved it from preserved raw authority.

Do not duplicate active computations.

## Post-e2 dependency authority

Iteration 386 restores the correct downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder was already scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction was already scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;

- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at the Iteration-239/240 authority boundary. Fresh 2025-2026 searches have not supplied a same-parent retarded pure-gravity hhh 1PI object with linked K2 normalization and source/Ward completion.

## Exact next gates

1. Consume the final Iteration-381 chunk `06-08`. If raw-valid, run the existing fail-closed 36-index assembly contract and freeze the complete simple-double q2 vector.
2. Consume Iteration 389 only from raw per-channel artifacts. Assemble double-double q2 sums only after exactly 15 unique channel indices are resolved; any `BLOCKED_CONVERGENCE` remains BLOCKED.
3. Continue consuming original Iteration-384 successes and Iteration-390 recovery artifacts. Merge Iteration-391 indices 12-13 exactly once. Run the fail-closed exact-48 assembly only after every index 0..47 has one authoritative resolved record.
4. After complete `Tr U1^2`, assemble its q2 operator coordinate as simple-simple + simple-double + double-double, still without the `-i/4` effective-action weight.
5. After complete `Tr U2`, assemble its q2 operator coordinate as Iteration-361 ordinary-simple + Iteration-366 repeated-family simple-simple + complete cut-through-double-pole sector, still without the `+i/2` weight.
6. Only then assemble

\[
D_s\Gamma_{e=2}=+\frac{i}{2}D_s\mathrm{Tr}U_2-\frac{i}{4}D_s\mathrm{Tr}U_1^2
\]

q2-by-q2.
7. Source/Ward/contact completion + matched K2 and the fixed comparator quotient remain downstream. No source/Born subtraction before origin accounting. No Candidate residual before comparator quotient closure.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Change through validated Iteration 391 plus active 381/384/389/390 work: `0 pp`. Major one-loop sub-sectors are closing, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Empty uncut topology may use `+Infinity` only after explicit topology proof; it is never a generic exemption. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
