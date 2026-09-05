# Candidate Gravity Current Front

**Updated:** 2026-09-05  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: Iteration 411.
- Latest validated structural authority: Iteration 410.
- Latest raw-valid physical blocker: Iteration 421 — `BLOCKED_CONVERGENCE`, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: `[2]`.
- Latest completed numerical mass-support authority: Iteration 459 raw-consumes run `33946347229` as PASS at `u=-1e-5, v=+5e-6`; non-promoting.
- Latest authoritative research iteration: Iteration 459.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: `5/32 = 15.625%`, i.e. `400/2560` row occurrences.
- Active numerical gate: run `33951807833` at Iteration-455 distinct rank 3, `u=-1e-5, v=+1e-5`, all five training-z, NPHI16, unchanged radial Richardson, direct MP80/120. This is the sole authorized numerical gate; do not duplicate.

## Retained physical authority
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Numerical precision chain
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic. Iteration 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459 progressively close direct-parent full-training-z mass support. Iteration 454 rejects `u<->v` deduplication. Iteration 455 freezes exact support order. Iteration 457 proves the four exact BASE/HALF coordinate overlaps may share one `F(u,v)` precision certificate but must retain separate derivative weights.

## Iteration 458 assembly-level precision barrier
The authoritative Iteration-407 mixed auxiliary-mass derivative uses tensor-product central4 first derivatives with coefficients `[1/12,-2/3,+2/3,-1/12]/h`. BASE and HALF are formed separately; the frozen physical quantity retains `ds=-d_base`, while BASE/HALF disagreement is a separate mass-step convergence test. There is no BASE/HALF Richardson extrapolation.

The first-derivative coefficient L1 sum is exactly `3/2`, hence the tensor mixed-derivative pre-scaling L1 sum is `9/4`. Therefore error-amplification norms are BASE `9.0e10` and HALF `3.6e11`. Local fixed-mass MP80/120 PASSes are necessary but do not by logic alone certify the assembled derivative.

After all 28 distinct `F(u,v)` coordinates have local certificates, assemble BASE and HALF independently at MP80 and MP120, require all finite, require each assembled scaled MP80↔120 discrepancy `<=2e-6`, retain BASE↔HALF physical mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Only after that PASS may frozen Iteration 424 be reevaluated.

## Iteration 459 raw authority
Run `33946347229`, job `101253020122`, artifact `9964610341`, artifact digest `sha256:8a3f2ec89403a45ad525a4428cc3212b4ee47f632dba306dcb5a530145760a7b`, scientific JSON SHA-256 `0eafc8afad813c42b245ba9f49280b26b241a1b638cdb21fc9f83845d69e03d9`. At `u=-1e-5, v=+5e-6`: `80/80` finite, max scaled MP80↔MP120 `3.26861120435911150741540805708e-80 <= 1e-30`, max radial Richardson scaled error `2.56975832612797362560915878496e-15 <= 5e-4`. Non-promoting PASS.

## Active gate
Run `33951807833`: raw-consume fail-closed at `u=-1e-5, v=+1e-5` (Iteration-455 distinct rank 3). PASS closes only that coordinate and permits only distinct rank 4 `u=-5e-6, v=-1e-5` under unchanged five-z/NPHI16/radial/direct-MP80/120 conventions. BLOCKED requires localization of the first failing sample at exactly the active coordinate. No later coordinate may be launched before raw consumption.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Only exact BASE/HALF coordinate overlaps may share precision certificates, and shared certificates never erase level-specific central4 derivative weights. Local MP sample PASS never substitutes for assembled derivative MP closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
