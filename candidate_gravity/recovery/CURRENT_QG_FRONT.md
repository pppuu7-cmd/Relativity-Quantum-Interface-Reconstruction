# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity authority:** **Iteration 383**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green workflow colour alone is never scientific authority.

## Authoritative state

- `e=3,c=0` remains closed by Iteration 246; actual `e=1,c=2 Tr U1` normalized cut remains frozen by Iteration 307.
- Determinant `e=0,c<=3`: Iteration 333 froze three NONZERO bubble channels and two NONZERO triangle channels while leaving only the `q^2=-1` triangle numerically BLOCKED. **Iteration 380 closes that last triangle obstruction analytically/numerically without threshold weakening:** normalized angular mean `0.006875651912582228`, direct-original-integrand cross-check `0.006875651912566607`, scaled disagreement `8.354002293824815e-13`, exact uncut-denominator range `[0.11857864376269048, 0.40142135623730957]`; status NONZERO.
- **Iteration 383 closes the complete channel-resolved ordinary-two-simple-particle determinant absorptive vector** using the frozen Iterations-337/338 normalization `D_s Gamma_det=-i*sphere_mean`, without reapplying internal graviton/ghost weights:
  - `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
  - `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
  - `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.
  All three coordinates are NONZERO and remain separate. The Iteration-297 finite-DR/evanescent warning remains binding; Iteration 383 is not a full finite-DR determinant or a candidate residual.
- Timelike `Tr U2`: ordinary-simple sector (361) closes and cancels q2-by-q2; repeated-family simple-simple sector (366) closes and is NONZERO q2-by-q2. The 48 cut-through-double-pole channels require repeated-cut treatment. Iterations 364 and 376 were operationally cancelled before complete authority and remain non-scientific.
- **Iteration 382 raw-validates the frozen repeated-cut `Tr U2` arithmetic on prospectively fixed global channel 0:** `q^2=-1`, `D_s Tr U2=-1.1437983592303379e-05`, half-step `-1.1437983587686573e-05`, shifted-phi `-1.1438001667849296e-05`, scaled convergence error `8.280353369982061e-10 < 2e-5`, shell error `1.6132928326584306e-16`, minimum uncut denominator `0.12097568457851282`, runtime `341.30850966599996 s`. This is authority for channel 0 and resource architecture only; no extrapolation to the other 47 channels.
- Iteration 367 invalidates historical singleton-soft `Tr U1^2` pruning on the timelike fixture.
- Iteration 368 freezes full physical timelike `Tr U1^2` routing: all `42/42` ordered placements NONZERO; cyclic routing leaves 21 classes.
- Iterations 369-370 show all 21 cyclic classes remain physically distinct numerator+denominator families.
- Iteration 371 freezes all 36 multiplicity-two raw denominator targets as surviving physical double poles (`SURVIVE=36`, `CANCEL=0`, `BLOCKED=0`).
- Iteration 372 freezes 57 timelike `Tr U1^2` channels, exactly 19 per q2 coordinate: 6 simple-simple, 36 simple-double, 15 double-double.
- Iteration 373 closes the ordinary-simple prerequisite: all `6/6` simple-simple channels `REGULAR`, `BLOCKED=0`.
- **Iteration 374 closes the physical ordinary-simple `Tr U1^2` discontinuity:** all `6/6 CONVERGED`, `BLOCKED=0`; q2-resolved sums are `6.253219881951187e-05` at `q^2=-1`, `3.5044107116946374e-05` at `q^2=-0.34`, and `2.9297648005638963e-05` at `q^2=-0.14`, all NONZERO.
- Iteration 375 validates the repeated-cut auxiliary-mass/distributional bridge:

\[
D_1^{-2}D_2^{-1}=-\partial_{\mu_1^2}[(D_1+\mu_1^2)^{-1}D_2^{-1}]_{0},
\]

\[
D_1^{-2}D_2^{-2}=+\partial_{\mu_1^2}\partial_{\mu_2^2}[(D_1+\mu_1^2)^{-1}(D_2+\mu_2^2)^{-1}]_{0,0}.
\]

- **Iteration 377 closes the physical auxiliary-mass kinematic prerequisite for every repeated-cut `Tr U1^2` channel:** `51/51 REGULAR`, `BLOCKED=0`; 36 simple-double + 15 double-double; 17 channels in each q2 coordinate. Minimum analytic uncut separation `0.11857147221810005`; maximum shell error `1.2622654386573035e-16`; minimum Kallen function `0.019594400000000005`.
- **Iteration 378 raw-validates the full physical simple-double pipeline on one prospectively frozen channel only:** class `2`, `q^2=-0.34`, multiplicities `2x1`, `CONVERGED`, `D_s Tr U1^2=-2.5401676390398016e-05`; scaled convergence error `2.3732431469379806e-11`, max shell error `1.726049858596923e-16`, min sampled uncut denominator `0.2609889252677208`, runtime `1312.8183083709998 s`.
- **Iteration 379 is an operational cancellation, not scientific FAIL:** the one-channel double-double scientific step ran for about 45 minutes and was cancelled before sentinel/artifact. No physical value from it is authority.

## Provenance of new validated authorities

- Iteration 380: run `33814113932`, job `100842299850`, artifact `9916838615`, digest `sha256:198d91e9ef7a5a09cdbaca11eb4c02135462fe831f01fbf3c54c7daf7820df63`, raw JSON SHA-256 `217e1fabe4f97967ee82c31101ecce3aeac27826599b516f779a9db84f098ef4`, workflow head `c24850b08f5617868b366d7ec47b68a6cb9cdf40`.
- Iteration 382: run `33816704205`, job `100850328336`, artifact `9916963796`, digest `sha256:e4ce19e00d8b58f78407c68974f9baa326d8777a4cb84af9ec58ac42fc0ee143`, raw JSON SHA-256 `5fddd09cc07224063434e2abeef1c8d0a044cfcf88ee85cb9e825bb69b005648`, workflow head `7fb92f2bd6488ccf7b7a4aaf141bd913ad2aa46a`.
- Iteration 383: successful run `33817475548`, job `100852689209`, artifact `9917045046`, digest `sha256:4de76d7ce811ca34a17b9e21b6408c38a632c2850c41b3008f94292a78504c00`, raw JSON SHA-256 `7c00c0d7e959375d9b8e4614994a16e482dc21c7444e0f589ec8d40c531560f4`, workflow head `72a06217529f4e2f47736542397afdeb4fa65f27`. The prior run `33817415864` failed only an over-literal provenance-string assertion; no scientific input changed in the repair.

## Active computations / resource recovery

- **Iteration 381:** run `33816213900`, workflow head `5ecb485240ffc39f4bd7b8950ec8963e7b06f92f`; full 36-channel simple-double `Tr U1^2` evaluation in 12 prospectively frozen chunks of exactly 3 channels. Full authority requires all 12 raw artifacts and exact 36-index coverage.
- **Iteration 384:** run `33817712381`, workflow head `dcae3ac454fd81f19c6d02d4815f07a741afefc7`; complete 48-channel repeated-cut `Tr U2` recovery in 24 prospectively fixed two-channel chunks `[0,2),[2,4),..., [46,48)`. It uses Iteration-364 `channel_derivative` verbatim with unchanged `h`, `h/2`, angular grids, shifted-phi check, normalization, and thresholds. Full authority requires exact indices `0..47` once each. `BLOCKED_CONVERGENCE` is preserved and never zero-filled.
- **Iteration 385:** code/workflow committed (`bd8f33cd3135966050309711c0a151c445f90f7b`, `dd657f3a1ba115e57fdd0fc5c8b3f2c2fe31615d`) as a resource-only repair of cancelled 379. It preserves the complete Iteration-379 one-channel double-double arithmetic and parallelizes only independent angular points via ordered `fork` map, with a prospectively fixed serial-vs-parallel identity oracle (`2e-13`). At this front update a GitHub Actions run had not yet registered; do not duplicate blindly.

Do not duplicate active computations.

## Exact next gates

1. Consume Iteration 381 only after all 12 raw chunks exist; validate exactly 36 unique simple-double indices with no gaps/overlaps, preserve q2 buckets, and keep any nonconverged channel BLOCKED.
2. Consume Iteration 384 only after raw chunk/sentinel validation; validate exactly 48 unique repeated `Tr U2` indices. Assemble a q2 coordinate only if every required channel in that bucket is scientifically resolved.
3. Recheck Iteration 385 registration. If a raw-valid one-channel result converges, use measured parallel runtime only to prospectively freeze a complete 15-channel double-double architecture with identical arithmetic. If it remains operationally unregistered or fails structurally, repair resource plumbing only; do not alter physics thresholds.
4. Retain the Iteration-383 determinant vector as immutable normalized origin accounting. Iteration-297 finite-DR warning remains separate and binding.
5. Only after complete physical `Tr U2` and complete `Tr U1^2` closure may

\[
D_s\Gamma_{e=2}=+\frac{i}{2}D_s\mathrm{Tr}U_2-\frac{i}{4}D_s\mathrm{Tr}U_1^2
\]

be assembled q2-by-q2.
6. Source/Ward/contact completion and matched `K2` subtraction remain downstream. Source/Born subtraction is forbidden before normalized origin accounting. No candidate residual may be declared before the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient survives.

Repeated-cut normalized signs remain: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through validated Iteration 383 plus active 381/384/385 resource work: `0 pp`. Several hard sub-sectors are now physically closed, including the complete ordinary-simple determinant vector, but complete repeated `Tr U1^2`, complete repeated `Tr U2`, Source/Ward/contact + matched `K2`, and a robust comparator-subtracted residual remain open.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure is not scientific FAIL. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct q2 discontinuity variables are never summed. Same `i0` is mandatory. No effective-action weight is folded before the corresponding operator coordinate is complete. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5.
