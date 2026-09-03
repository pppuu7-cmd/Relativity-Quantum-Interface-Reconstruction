# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 377**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green workflow colour alone is never scientific authority.

## Authoritative state

- `e=3,c=0` remains closed by Iteration 246; actual `e=1,c=2 Tr U1` normalized cut remains frozen by Iteration 307.
- Determinant `e=0,c<=3`: three bubbles NONZERO, two triangle channels NONZERO; `q^2=-1` triangle remains analytic/symbolic BLOCKED.
- Timelike `Tr U2`: ordinary-simple sector (361) closes and cancels q2-by-q2; repeated-family simple-simple sector (366) closes and is NONZERO q2-by-q2. The 48 cut-through-double-pole channels remain open because Iteration 364 was operationally cancelled at its fixed 40-minute workflow timeout before sentinel/schema/artifact. This is no scientific PASS/FAIL authority.
- Iteration 367 invalidates historical singleton-soft `Tr U1^2` pruning on the timelike fixture.
- Iteration 368 freezes full physical timelike `Tr U1^2` routing: all `42/42` ordered placements NONZERO; cyclic routing leaves 21 classes.
- Iterations 369-370 show all 21 cyclic classes remain physically distinct numerator+denominator families.
- Iteration 371 freezes all 36 multiplicity-two raw denominator targets as surviving physical double poles (`SURVIVE=36`, `CANCEL=0`, `BLOCKED=0`).
- Iteration 372 freezes 57 timelike channels, exactly 19 per q2 coordinate: 6 simple-simple, 36 simple-double, 15 double-double.
- Iteration 373 closes the ordinary-simple prerequisite: all `6/6` simple-simple channels `REGULAR`, `BLOCKED=0`.
- **Iteration 374 closes the physical ordinary-simple `Tr U1^2` discontinuity:** all `6/6 CONVERGED`, `BLOCKED=0`. q2-resolved sums are `6.253219881951187e-05` at `q^2=-1`, `3.5044107116946374e-05` at `q^2=-0.34`, and `2.9297648005638963e-05` at `q^2=-0.14`; all three are `NONZERO`. Maximum scaled angular error `9.023987581011366e-10` under frozen `2e-5`; maximum radial Richardson error `3.1484214649442344e-17`; maximum shell error `7.35968036186944e-17`; minimum sampled uncut denominator `0.12097829436145643`.
- Iteration 375 validates the repeated-cut auxiliary-mass/distributional bridge:

\[
D_1^{-2}D_2^{-1}=-\partial_{\mu_1^2}[(D_1+\mu_1^2)^{-1}D_2^{-1}]_{0},
\]

\[
D_1^{-2}D_2^{-2}=+\partial_{\mu_1^2}\partial_{\mu_2^2}[(D_1+\mu_1^2)^{-1}(D_2+\mu_2^2)^{-1}]_{0,0}.
\]

- **Iteration 377 closes the physical auxiliary-mass kinematic prerequisite for every repeated-cut `Tr U1^2` channel:** `51/51 REGULAR`, `BLOCKED=0`; 36 simple-double + 15 double-double; 17 channels in each q2 coordinate. Minimum analytic uncut separation `0.11857147221810005`; maximum shell error `1.2622654386573035e-16`; minimum Kallen function `0.019594400000000005`.

Iteration-374 provenance: run `33812352303`, job `100836834321`, artifact `9915759849`, artifact digest `sha256:2293a37961230bed7eaed2298fcfaddfcffb342c2e5579b29b9e73986b47450d`, raw JSON SHA-256 `ad84a0e59751171f906e0fbd9b868357e19b3cf8ce948970b3b529e134e84c3c`, workflow head `cb2ddc7d838d0ba1844339d447445b3a8a613124`.

Iteration-377 provenance: run `33813366983`, job `100840032070`, artifact `9915623215`, artifact digest `sha256:f6f1860a74a6d84c24023b2a7e8c1d131f9133e2eba00ed743d098d225946c4b`, raw JSON SHA-256 `e27aa368470c4c0091cf72956b4ef13302f8a6cc979519c199aa2a63444ae2a5`, workflow head `e8de37295817456a36acc6289898342804a143ac`.

## Active computations

- **Iteration 376:** run `33813179996`; three fixed jobs for channel ranges `[0:16]`, `[16:32]`, `[32:48]`, recovering cancelled Iteration 364 with the exact frozen `channel_derivative`, mass nodes, quadratures and `2e-5` convergence threshold. All three raw chunk artifacts are required before 48-channel assembly.
- **Iteration 378:** run `33813604738`, job `100840748044`; one prospectively selected physical simple-double `Tr U1^2` pilot with full stripped numerator, h vs h/2 and low/high/shifted angular checks. It may validate pipeline/runtime only, never the other 35 channels.
- **Iteration 379:** run `33813761466`, job `100841217582`; one prospectively selected physical double-double mixed-derivative pilot. Its resource-aware pilot grid is not full-sector authority.

Do not duplicate any active computation.

## Exact next gates

1. Consume all three Iteration-376 chunks only after raw chunk/sentinel validation. Reject overlap, gaps or provenance mismatch, then assemble exactly 48 unique global channel indices q2-by-q2 with no threshold change.
2. Consume Iteration 378. If it converges, use measured runtime only to prospectively freeze a fixed chunk architecture for all 36 simple-double channels with identical arithmetic.
3. Consume Iteration 379. If it validates, use measured runtime and convergence margin to prospectively freeze the full-sector angular grid and chunk architecture for all 15 double-double channels; the pilot grid itself is not full-sector authority.
4. Only after complete physical `Tr U2` and `Tr U1^2` closure may `+(i/2)Tr U2 -(i/4)Tr U1^2` be assembled.
5. Source/Ward/contact completion and matched `K2` subtraction remain downstream. Source/Born subtraction is forbidden before normalized origin accounting.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

Iteration-297 evanescent/regulator warning remains binding. No Candidate residual may be declared before the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient survives.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through validated Iteration 377 plus late-consumed Iteration 374: `0 pp`. The ordinary-simple `Tr U1^2` sub-sector and all repeated-cut method/kinematic prerequisites are closed, but complete `Tr U1^2`, complete `Tr U2`, and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 discontinuity variables are never summed. Same `i0` is mandatory. No effective-action weight is folded before the corresponding operator coordinate is complete. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
