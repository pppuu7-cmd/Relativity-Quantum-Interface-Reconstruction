# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 375**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green workflow colour alone is never scientific authority.

## Authoritative state

- `e=3,c=0` remains closed by Iteration 246; actual `e=1,c=2 Tr U1` normalized cut remains frozen by Iteration 307.
- Determinant `e=0,c<=3`: three bubbles NONZERO, two triangle channels NONZERO; `q^2=-1` triangle remains analytic/symbolic BLOCKED.
- Timelike `Tr U2`: ordinary-simple sector (361) closes and cancels q2-by-q2; repeated-family simple-simple sector (366) closes and is NONZERO q2-by-q2. The 48 cut-through-double-pole channels remain open because Iteration 364 was operationally cancelled at the fixed 40-minute workflow timeout before sentinel/schema/artifact. This is no scientific PASS/FAIL authority.
- Iteration 367 invalidates historical singleton-soft `Tr U1^2` pruning on the timelike fixture.
- Iteration 368 freezes full physical timelike `Tr U1^2` routing: all `42/42` ordered placements NONZERO; cyclic routing leaves 21 classes.
- Iterations 369-370 show all 21 cyclic classes remain physically distinct numerator+denominator families.
- Iteration 371 freezes all 36 multiplicity-two raw denominator targets as surviving physical double poles (`SURVIVE=36`, `CANCEL=0`, `BLOCKED=0`).
- Iteration 372 freezes 57 timelike channels, exactly 19 per q2 coordinate: 6 simple-simple, 36 simple-double, 15 double-double.
- Iteration 373 closes the ordinary-simple prerequisite: all `6/6` simple-simple channels `REGULAR`, `BLOCKED=0`; minimum analytic uncut separation `0.11857864376269048`; maximum shell error `5.551115123125783e-17`.
- **Iteration 375 validates the repeated-cut auxiliary-mass/distributional bridge for both singularity classes required downstream:**

\[
D_1^{-2}D_2^{-1}=-\partial_{\mu_1^2}[(D_1+\mu_1^2)^{-1}D_2^{-1}]_{0},
\]

\[
D_1^{-2}D_2^{-2}=+\partial_{\mu_1^2}\partial_{\mu_2^2}[(D_1+\mu_1^2)^{-1}(D_2+\mu_2^2)^{-1}]_{0,0}.
\]

Iteration-375 authority: `PASS_TRU1SQ_SIMPLE_DOUBLE_AND_DOUBLE_DOUBLE_AUXMASS_DISTRIBUTIONAL_ORACLE`.

Iteration-375 provenance: run `33813067035`, job `100839109162`, artifact `9915525281`, artifact digest `sha256:0ba79d4f8fced6714d7483a253fc14df49251f8e892e7f93ae62d618b3841599`, raw scientific JSON SHA-256 `f9bd2f186f55338bd73783ff9cd575f9176be29b316529af2f18053ee72209d6`, workflow head `6f01b300fec1cb9bd6e0cd3d1eb475422001b183`.

Maximum Iteration-375 method errors remain below prospectively frozen thresholds: simple-double direct-vs-aux `1.7408297026122455e-13`; double-double direct-vs-aux `3.7337533065340267e-10`; simple-double epsilon->0 `8.446889955493475e-06`; double-double epsilon->0 `1.1110216624476976e-05`; exact shifted-delta oracle `1.6468437724626028e-10`.

## Active computations

- **Iteration 374:** run `33812352303`, job `100836834321`; normalized q2-resolved simple-simple `Tr U1^2` discontinuity for the six Iteration-373 REGULAR channels. No authority until raw artifact validation.
- **Iteration 376:** run `33813179996`; three fixed matrix jobs, chunks `[0:16]`, `[16:32]`, `[32:48]`, prospectively recovering cancelled Iteration 364 with the exact same frozen `channel_derivative`, quadratures, auxiliary-mass nodes and `2e-5` convergence threshold. All three chunk artifacts are required before full 48-channel assembly.
- **Iteration 377:** run `33813366983`; physical mass-probe kinematic-separation prerequisite for all 36 simple-double and 15 double-double `Tr U1^2` channels under `mu^2={-1e-5,0,+1e-5}`. No integration is performed in this gate.

Do not duplicate any of these active computations.

## Exact next gates

1. Consume Iteration 374 only after raw artifact validation; preserve the three q2 coordinates separately.
2. Consume all three Iteration-376 chunks only after raw chunk/sentinel validation, reject any overlap/gap/provenance mismatch, then assemble exactly 48 unique global channel indices q2-by-q2. Do not weaken the frozen threshold.
3. If Iteration 377 validates all 51 repeated-cut channels as kinematically REGULAR, integrate 36 simple-double channels with one symmetric auxiliary-mass derivative and 15 double-double channels with a mixed symmetric derivative, with independent step-size/angular convergence checks.
4. Only after complete physical `Tr U2` and `Tr U1^2` closure may `+(i/2)Tr U2 -(i/4)Tr U1^2` be assembled.
5. Source/Ward/contact completion and matched `K2` subtraction remain downstream. Source/Born subtraction is forbidden before normalized origin accounting.

Iteration-297 evanescent/regulator warning remains binding. No Candidate residual may be declared before the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient survives.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through Iteration 375: `0 pp`. Repeated-cut `Tr U1^2` derivative machinery is validated, but neither complete `Tr U1^2`, complete `Tr U2`, nor a robust comparator-subtracted residual has closed a readiness-rubric point.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 discontinuity variables are never summed together. Same `i0` is mandatory under auxiliary-mass differentiation. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
