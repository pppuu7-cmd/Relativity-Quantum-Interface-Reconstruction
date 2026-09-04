# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 409**  
**Latest validated structural authority:** **Iteration 410**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 380 closes the former `q^2=-1` triangle numerical blocker analytically/numerically without threshold weakening.
- Iteration 383 closes the ordinary-two-simple-particle determinant absorptive vector:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
- Iteration 387 preserves the evanescent/R2 warning: hard-branch discontinuity is valid, but full finite local/rational DR remainder remains blocked. This is not a full finite determinant and not a Candidate residual.

### Timelike `Tr U2` — COMPLETE OPERATOR COORDINATE

- Iteration 361 ordinary-simple sector closes and cancels q2-by-q2.
- Iteration 366 repeated-family simple-simple sector closes 18/18:
  - `q^2=-1`: `-6.812363349599648e-05`;
  - `q^2=-0.34`: `-8.405976034846215e-05`;
  - `q^2=-0.14`: `-7.069545900379072e-05`.
- Iteration 392 freezes the exact 48-channel topology mask. No-uncut indices are `[4,13,22,27,28,29,30,33,36,39,42,45]`; only these may use `+Infinity` as empty-set minimum-uncut sentinel. All other indices require finite positive uncut separation.
- Iteration 405 raw-validates exact 48/48 repeated-cut assembly. Workflow run `33832181526`, artifact `9922054102`, digest `sha256:1dd9bbc6c863954059263171c5a160510ce3605bb416a46498c3453b48343729`, result SHA-256 `f766c6641fb9a89838784ae7572fa1f8459dd0260fd71007f8de93e727840cab`. Exactly 16 channels occur in each q2 bucket; all 48 records are CONVERGED.
- Authoritative repeated-cut vector:
  - `q^2=-1`: `+0.0006026660521292439`;
  - `q^2=-0.34`: `-0.0006500414994361118`;
  - `q^2=-0.14`: `-0.0015019714311265522`.
- Iteration 406 assembles the complete timelike operator coordinate, still without `+i/2`:
  - `q^2=-1`: `D_s TrU2=+0.0005345424186332474`;
  - `q^2=-0.34`: `D_s TrU2=-0.000734101259784574`;
  - `q^2=-0.14`: `D_s TrU2=-0.001572666890130343`.

### Timelike `Tr U1^2`

- Iterations 367-371 invalidate old null-soft pruning, freeze 21 physically distinct numerator+denominator families, and establish 36 surviving multiplicity-two denominator targets.
- Iteration 372 freezes 57 physical channels: 6 simple-simple, 36 simple-double, 15 double-double; exactly 19 per q2.
- Iteration 374 closes 6/6 simple-simple:
  - `q^2=-1`: `6.253219881951187e-05`;
  - `q^2=-0.34`: `3.5044107116946374e-05`;
  - `q^2=-0.14`: `2.9297648005638963e-05`.
- Iteration 393 closes all 36 simple-double channels:
  - `q^2=-1`: `-0.002329411286740447`;
  - `q^2=-0.34`: `-0.0005948791870822445`;
  - `q^2=-0.14`: `-7.368142632096214e-05`.
- Iteration 402 raw census found double-double blockers 2,4,11 and operational gap 5.
- Iteration 399 closes index 5 / class 8 / `q^2=-0.14` as CONVERGED: `D_s TrU1^2 double-double=0.000119747535002548`, scaled convergence error `1.8393013149631406e-7`.
- Classes 3,5,16 have multiplicities `2,2,1`; one-affine-denominator analytic/spectral reduction is topologically available. Iteration 403 proves exact central4×central4 auxiliary-mass stencil commutation with the sphere mean as a finite linear combination.
- Iteration 401 is raw-validated as `PASS_TRU1SQ_CHANNEL4_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE`: run `33830352712`, artifact `9922183136`, digest `sha256:82ebf8b245f61365474c6180a772619854ece34b64a897c649c7afa35690b0eb`, scientific JSON SHA-256 `046ef14ba3ab7baf0552adcd233907c9f6078f37dcb1b1af347765d789417d4b`. It is structural only: max affine-denominator error `1.1102230246251565e-16`, max Fourier tail `4.4190104140298897e-16`, max phase-mean error `6.534223913356486e-16`, and max held-out degree-4 polynomial error `1.7438316162996242e-06 < 2e-6`. It promotes no physical `D_s` value.
- Iteration 409 raw-consumes Iteration 407 and removes physical blocker index 4 / class 5 / `q^2=-1`: run `33835806522`, job `100907970715`, artifact `9924759934`, digest `sha256:eec059d48944771897d09341d888a4f0691664ce12f6c6258ff4cc3aad8947ae`, raw scientific JSON SHA-256 `bba7c203ca9694c70b79f762820cdcd26768ee6bb286d1dbc8c31c8ee93eee68`. Authoritative `D_s TrU1^2 double-double channel=+0.003562716046166582`; scaled mass-step convergence error `1.694511628814576e-05 < 2e-05`; max direct original-integrand cross-check error `2.0657185788308663e-09 < 2e-06`; minimum analytic uncut separation `0.11857147221810008`.
- Iteration 410 raw-validates the structural oracle separately for both remaining physical blockers. Run `33847425175` completed success, but raw artifacts were independently checked:
  - index 2 / class 3 / `q^2=-1`: artifact `9928039298`, digest `sha256:0f2d759480a688fb71db5542c20429f79beea1737708ec92665c82cb8ba7db2f`, raw SHA-256 `dbaea9b9d015d6df7ab465c0748596462949eb682a8a2a662f88b5d667e8d2c7`; structural PASS;
  - index 11 / class 16 / `q^2=-0.34`: artifact `9928100131`, digest `sha256:efdeb91cf58ed05c7b06bf300823e20e9b1f46dcb8c01b8dec24112bef662114`, raw SHA-256 `2ecfc9d9812a8258803e20e6e402df3c93dac2f0245bf61e390517839605693b`; structural PASS.
- Iteration 410 promotes no physical `D_s` value. Exact unresolved double-double physical set remains **`[2,11]`** until Iteration 411 physical reductions are raw-validated.
- No further blind angular-grid escalation is authorized for blockers 2 and 11.

## Iteration 408 operational classification

- Run `33839449598` attempt 2 completed `cancelled`; job `100928697231` was cancelled during the scientific oracle step at the 45-minute resource boundary. Raw authority audit was skipped.
- Artifact `9926539839`, digest `sha256:f7d8d24b3ed9ce6f9cb29f4d19daa5f714b08837bde253f1910c7443f2e1e67f`, contains a zero-byte `iteration408_result.json`.
- Therefore Iteration 408 is `OPERATIONAL_CANCELLATION`: neither structural PASS nor structural FAIL, and it promotes no physical value.
- A later repaired Iteration-408 run may still execute due to a race. It is superseded operationally by validated Iteration 410 and cannot override Iteration 411 physical authority.

## Active computation

- **Iteration 411:** run `33851983789`, evaluator commit `1e01f7f4abf3ee00daafcf3580019a74ada9a670`, workflow/head commit `a50b25c408903112dc6962487b58478a7f34e3f3`, is the active split physical analytic/spectral reduction for indices 2 and 11.
- It applies the already-frozen Iteration-407 physical architecture separately per target after Iteration-410 structural PASS.
- Parent Iteration-379/389 physical integrand, central4×central4 auxiliary-mass stencil, normalized sign `D_s=-sphere_mean[d_u d_v G]`, held-out original-integrand checks, structural thresholds and physical convergence threshold `2e-5` are unchanged.
- Iteration 411 is ACTIVE / NOT YET SCIENTIFIC AUTHORITY. Each per-target raw artifact must be consumed fail-closed; `CONVERGED` removes only its own blocker, while `BLOCKED_CONVERGENCE` remains a physical blocker.

No useful heavy physical run is duplicated.

## Post-e2 dependency authority

Iteration 386 restores the downstream DAG:
- local source-completed dimension-12 C5 soft2 ladder: scoped closed by Iteration 185;
- calibrated nonlocal C5 lambda direction: scoped closed by Iteration 186;
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` from Iteration 230, not zero;
- frozen linked target remains `T_cut = D_s Gamma3_ret,soft - W[D_s K2]`;
- native causal/source-completed pure-gravity `h^3` executability remains `BLOCKED_NOT_ZERO` at Iteration 239/240 authority.

## Exact next gates

1. Raw-consume both Iteration-411 per-index physical artifacts fail-closed.
2. Assemble double-double q2 sums only after all 15 unique channels are scientifically resolved. Then assemble complete `Tr U1^2` = Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without `-i/4`.
3. Only after complete `Tr U1^2` assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2, using the complete Iteration-406 `Tr U2` coordinate.
4. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No Candidate residual before comparator quotient closure.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Change through validated physical/operator Iteration 409 / validated structural Iteration 410 / active physical Iteration 411: `0 pp`. Structural executability alone does not close a readiness-rubric bucket. Complete `Tr U1^2`, linked Source/Ward/K2 closure and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 mask. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
