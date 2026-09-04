# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 393**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 380 closes the former `q^2=-1` triangle numerical blocker analytically/numerically without threshold weakening.
- Iteration 383 closes the complete channel-resolved ordinary-two-simple-particle determinant absorptive vector:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
- Iteration 387 sharpens the Iteration-297 regulator warning: evanescent/R2 ambiguity still blocks the **full finite local/rational DR remainder**, but does not invalidate the frozen off-shell one-loop hard branch discontinuity. The Iteration-383 absorptive vector remains hard-cut authority; it is not a full finite determinant and not a Candidate residual.

### Timelike `Tr U2`

- Iteration 361 ordinary-simple sector closes and cancels exactly q2-by-q2.
- Iteration 366 repeated-family simple-simple sector closes, 18/18 CONVERGED, with q2 sums:
  - `q^2=-1`: `-6.812363349599648e-05`;
  - `q^2=-0.34`: `-8.405976034846215e-05`;
  - `q^2=-0.14`: `-7.069545900379072e-05`.
- Iteration 382 raw-validates the frozen repeated-cut arithmetic on global channel 0: `D_s TrU2=-1.1437983592303379e-05`, convergence `8.280353369982061e-10`, shell `1.6132928326584306e-16`.
- Iteration 384 is the complete 48-channel cut-through-double-pole computation split into fixed two-channel jobs. Raw-valid original chunks already cover indices `{0,1,2,3,6,7,8,9,10,11,18,19,20,21}`.
- Iteration 391 resolves preserved indices 12-13 without reintegration. Index 13 has no uncut denominator and its `+Infinity` minimum is the correct empty-set sentinel. Values:
  - index 12, `q^2=-1`: `D_s TrU2=-1.6409523141466878e-05`;
  - index 13, `q^2=-0.14`: `D_s TrU2=-0.0004977890941608628`.
- **Iteration 392 freezes the full prospective topology mask for all 48 repeated-cut channels.** Exactly 12 channels have only two distinct denominator momentum groups, so the cut exhausts all groups and no uncut denominator exists; exactly 36 channels have three groups and retain one uncut denominator. The no-uncut indices are

  `[4,13,22,27,28,29,30,33,36,39,42,45]`.

  There are exactly four no-uncut channels in each q2 bucket. Therefore `minimum_sampled_uncut_abs_denominator=+Infinity` is authorized **only** on those 12 indices; it is never a generic exemption. Iteration-392 run `33820820805`, job `100862890933`, artifact `9918201690`, raw result SHA-256 `d2ba75a4ba98afb28fc187bd28715fe999f55553323695f083013cac2040ad3d`.
- At this front, at least 16/48 repeated-cut indices are already raw-resolved CONVERGED: `0,1,2,3,6,7,8,9,10,11,12,13,18,19,20,21`. No full q2 sum is authorized until exact 48-index coverage is closed.

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
- **Iteration 393 closes the complete 36-channel simple-double operator coordinate from the preserved Iteration-381 raw manifest.** Exact indices `0..35` occur once each, 12/12 chunks are present, 36/36 channels are CONVERGED, all thresholds PASS, and each q2 bucket contains 12 channels. The normalized sums, with no `-i/4` weight folded, are:
  - `q^2=-1`: `D_s TrU1^2=-0.002329411286740447`;
  - `q^2=-0.34`: `D_s TrU1^2=-0.0005948791870822445`;
  - `q^2=-0.14`: `D_s TrU1^2=-7.368142632096214e-05`.
  Numerical envelope: max convergence `1.2832512405556301e-08`, max radial Richardson `9.7822954164134e-15`, max shell error `1.9796472878401243e-16`, min uncut denominator `0.1209736845785128`. Iteration-393 run `33820949571`, artifact `9918228922`, raw result SHA-256 `8eec56bd5d0d48e36c4490407bcc88c9d2ee3d3e59d976a9a0e1ad5f16d86226`.
- Iteration 385 raw-validates the complete double-double physical pipeline on the first prospectively selected channel: class 1, `q^2=-1`, `D_s TrU1^2=-0.0021448992853041436`, convergence `1.7976503775178967e-06 < 2e-5`, radial Richardson `5.16535599015544e-15`, shell `2.639515599904378e-16`, serial-vs-parallel oracle exactly `0.0`.
- Complete `Tr U1^2` remains BLOCKED only by the unresolved 15-channel double-double operator coordinate; no partial double-double sum may be promoted.

## Active computations / resource recovery

- **Iteration 384:** run `33817712381`; original full-48 repeated-`Tr U2` matrix continues for still-running chunks. Do not duplicate active original jobs.
- **Iteration 389:** run `33820063115`, workflow head `dbc0f1a622b3998132fcf3c1686c2e1033af5add`; full 15-channel `Tr U1^2` double-double matrix, one channel/job, `max-parallel=5`, identical Iteration-385 arithmetic, raw artifact preserved even on non-success status. Current run state at this front update: queued.
- **Iteration 390:** run `33820418026`, workflow head `54a200a941b487cb81940f5256ff94a15d1a1c36`; topology-aware recovery for previously failed/cancelled Iteration-384 chunks `04-05`, `14-15`, `16-17`, `22-23`, `28-29`, `30-31`. The physical Iteration-364 arithmetic and all thresholds are unchanged; only empty-uncut-set classification is repaired. Current run state at this front update: queued.

Iteration 381 is no longer active: its complete raw manifest has been consumed and scientifically assembled by Iteration 393.

Do not duplicate active or queued computations.

## Post-e2 dependency authority

Iteration 386 restores the correct downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder was already scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction was already scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;

- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at the Iteration-239/240 authority boundary. Fresh 2025-2026 searches have not supplied a same-parent retarded pure-gravity hhh 1PI object with linked K2 normalization and source/Ward completion.

## Exact next gates

1. Consume Iteration 389 only from raw per-channel artifacts. Assemble double-double q2 sums only after exactly 15 unique channel indices are resolved; any `BLOCKED_CONVERGENCE` remains BLOCKED.
2. Continue consuming original Iteration-384 successes and Iteration-390 recovery artifacts using the immutable Iteration-392 topology mask. Merge Iteration-391 indices 12-13 exactly once. Run the fail-closed exact-48 assembly only after every index `0..47` has one authoritative resolved record.
3. After complete double-double closure, assemble complete `Tr U1^2` q2-by-q2 as Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without the `-i/4` effective-action weight.
4. After complete repeated-`Tr U2`, assemble complete `Tr U2` q2-by-q2 as Iteration-361 ordinary-simple + Iteration-366 repeated-family simple-simple + complete cut-through-double-pole sector, still without the `+i/2` weight.
5. Only then assemble

\[
D_s\Gamma_{e=2}=+\frac{i}{2}D_s\mathrm{Tr}U_2-\frac{i}{4}D_s\mathrm{Tr}U_1^2
\]

q2-by-q2.
6. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No source/Born subtraction before origin accounting. No Candidate residual before comparator quotient closure.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Change through validated Iterations 392-393: `0 pp`. A major `Tr U1^2` sub-sector is now complete and the `Tr U2` recovery topology is fully certified, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 topology mask; it is never a generic exemption. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
