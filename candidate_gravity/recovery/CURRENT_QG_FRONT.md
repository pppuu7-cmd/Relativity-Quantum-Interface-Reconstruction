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
- Iteration 373 closes the ordinary-simple prerequisite: all `6/6` simple-simple channels `REGULAR`, `BLOCKED=0`; minimum analytic uncut separation `0.11857864376269048`; maximum shell error `5.551115123125783e-17`.
- Iteration 375 validates the repeated-cut auxiliary-mass/distributional bridge for simple-double and double-double channels. Frozen identities are

\[
D_1^{-2}D_2^{-1}=-\partial_{\mu_1^2}[(D_1+\mu_1^2)^{-1}D_2^{-1}]_{0},
\]

\[
D_1^{-2}D_2^{-2}=+\partial_{\mu_1^2}\partial_{\mu_2^2}[(D_1+\mu_1^2)^{-1}(D_2+\mu_2^2)^{-1}]_{0,0}.
\]

- **Iteration 377 closes the physical auxiliary-mass kinematic prerequisite for every repeated-cut `Tr U1^2` channel:** `51/51 REGULAR`, `BLOCKED=0`; 36 simple-double + 15 double-double; 17 channels in each `q^2` coordinate. Minimum analytically certified uncut absolute denominator over all mass probes and the full cut sphere is `0.11857147221810005`; maximum cut-shell error is `1.2622654386573035e-16`; maximum q2 error `5.551115123125783e-17`; minimum Kallen function `0.019594400000000005`.

Iteration-377 authority: `PASS_TRU1SQ_REPEATED_CUT_MASS_PROBE_KINEMATIC_SEPARATION__REGULAR_51__BLOCKED_0`.

Iteration-377 provenance: run `33813366983`, job `100840032070`, artifact `9915623215`, artifact digest `sha256:f6f1860a74a6d84c24023b2a7e8c1d131f9133e2eba00ed743d098d225946c4b`, raw scientific JSON SHA-256 `e27aa368470c4c0091cf72956b4ef13302f8a6cc979519c199aa2a63444ae2a5`, workflow head `e8de37295817456a36acc6289898342804a143ac`.

## Active computations

- **Iteration 374:** run `33812352303`, job `100836834321`; normalized q2-resolved simple-simple `Tr U1^2` discontinuity for the six Iteration-373 REGULAR channels. No authority until raw artifact validation.
- **Iteration 376:** run `33813179996`; three fixed matrix jobs for global channel ranges `[0:16]`, `[16:32]`, `[32:48]`, prospectively recovering cancelled Iteration 364 with the exact same frozen `channel_derivative`, auxiliary-mass nodes, quadratures and `2e-5` convergence threshold. All three raw chunk artifacts are required before full 48-channel assembly.
- **Iteration 378:** run `33813604738`; one prospectively preselected physical simple-double `Tr U1^2` channel pilot. It uses the full Iteration-370/374 stripped numerator, symmetric mass derivative, h vs h/2, low/high/shifted angular grids and records runtime. One channel can validate the pipeline and resource architecture only; it cannot promote the other 35 channels.
- **Iteration 379:** one prospectively preselected physical double-double `Tr U1^2` channel mixed-derivative pilot is registered. Its resource-aware pilot grid cannot serve as full-sector authority; a full-sector grid/chunk architecture must be frozen prospectively only after pilot validation.

Do not duplicate any active computation.

## Exact next gates

1. Consume Iteration 374 only after raw artifact validation; preserve the three q2 coordinates separately.
2. Consume all three Iteration-376 chunks only after raw chunk/sentinel validation. Reject overlap, gaps or provenance mismatch, then assemble exactly 48 unique global channel indices q2-by-q2 with no threshold change.
3. Consume Iteration 378. If the selected simple-double channel converges, use its measured runtime only to prospectively choose a fixed chunk size for all 36 simple-double channels with identical arithmetic; do not infer the other channel values from the pilot.
4. Consume Iteration 379. If the selected double-double channel validates, use its measured runtime/convergence margin to prospectively freeze the full-sector angular grid and chunk size for all 15 channels. The pilot grid itself is not complete-sector authority.
5. Only after complete physical `Tr U2` and `Tr U1^2` closure may `+(i/2)Tr U2 -(i/4)Tr U1^2` be assembled.
6. Source/Ward/contact completion and matched `K2` subtraction remain downstream. Source/Born subtraction is forbidden before normalized origin accounting.

For signs in the repeated-cut normalized coordinate: Iteration 337 contributes `D_s(simple)=-sphere_mean`; therefore simple-double has `D_s=+sphere_mean[d_mu G]`, while double-double has `D_s=-sphere_mean[d_mu1 d_mu2 G]` under the Iteration-375 identities.

Iteration-297 evanescent/regulator warning remains binding. No Candidate residual may be declared before the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient survives.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through Iteration 377: `0 pp`. Repeated-cut derivative and physical kinematic prerequisites are closed, but neither complete `Tr U1^2`, complete `Tr U2`, nor a robust comparator-subtracted residual has closed a readiness-rubric point.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 discontinuity variables are never summed together. Same `i0` is mandatory under auxiliary-mass differentiation. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
