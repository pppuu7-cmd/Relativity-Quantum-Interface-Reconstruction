# Candidate Gravity Recovery Delta — Iteration 413

Date: 2026-09-04

MODEL_READINESS: 24%

## Source-of-truth entry state

At run start, `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_412.md`, recent research logs/commits, and current GitHub Actions state were re-read. Iteration-411 run `33851983789` had completed `success`, but workflow colour was not treated as scientific authority. Both per-target artifacts were downloaded and raw-inspected before any promotion.

## Iteration 411 raw authority

### Index 11 / class 16 / q^2=-0.34 — CONVERGED

- run: `33851983789`
- artifact: `9931076355` (`iteration411-physical-index-11`)
- artifact digest: `sha256:8551fba98b0f3f218960820a01369ca183da1234d22754bd5c647fa8909cf6f8`
- scientific JSON SHA-256 from the raw authority audit: `f8aea08be16636dcf5d83afaa29dd3059c734a1a3ad8f778f07ef53b3041abf1`
- status: `CONVERGED`
- `D_s TrU1^2 double-double channel = +0.013050543643260309`
- scaled mass-step convergence error: `5.421327239850046e-06 < 2e-05`
- max direct original-integrand cross-check scaled error: `1.1526331104849685e-12 < 2e-06`
- minimum analytic uncut separation: `0.25855334940036967`

Index 11 is therefore promoted as a physical double-double channel value. No effective-action factor is folded.

### Index 2 / class 3 / q^2=-1 — BLOCKED_CONVERGENCE

- run: `33851983789`
- artifact: `9930938547` (`iteration411-physical-index-2`)
- artifact digest: `sha256:3c34f0110e3dbf97b7abf5dedf7b70bf918d4bb3a9e2b5572c7d1f92df7120c2`
- scientific JSON SHA-256 from the raw authority audit: `53a185ae9825cde0a273161b1ee093ede54103b52d513ea291a3bfc8e1381486`
- status: `BLOCKED_CONVERGENCE`
- diagnostic `D_s` at the coarse member of the failed pair: `+0.003560682203382001`; this is NOT promoted as an authority value
- base/half mixed derivatives: `-0.003560682203382001` and `-0.0036107242774472896`
- scaled mass-step convergence error: `5.0042074065288766e-05 > 2e-05`
- max direct original-integrand cross-check scaled error: `2.0658472996495925e-09 < 2e-06`
- denominator-affine, polynomial held-out, radial extrapolation, positive Kallen, and uncut-separation checks all pass.

Thus the failure is localized to the auxiliary-mass finite-difference convergence check, not to the analytic/spectral angular representation. Unsupported remains BLOCKED; index 2 is not zero-filled and its diagnostic value is not inserted into any q2 sum.

The exact unresolved physical double-double set is now **`[2]`**. Iteration 412 exact15 assembly remains correctly BLOCKED because it requires all 15 records to be scientifically `CONVERGED`.

## Iteration 413 — prospectively frozen mass-step refinement

With no useful nonduplicating RQIR Actions queued/in_progress after Iteration 411 completed, anti-idle required the nearest scientifically allowed gate. Blind angular-grid escalation is forbidden and unnecessary because the original-integrand and structural checks already pass. Therefore Iteration 413 freezes exactly one next auxiliary-mass halving pair for index 2:

- same Iteration-407/411 physical integrand;
- same analytic/spectral angular reduction;
- same central4 x central4 stencil and `D_s=-sphere_mean[d_u d_v G]` normalization;
- same held-out original-integrand cross-checks;
- same physical convergence threshold `2e-5` and all structural thresholds;
- mass-step pair only: `h=2.5e-6`, `h/2=1.25e-6`.

The new coarse step is exactly the prior Iteration-411 half-step scale, making this a deterministic numerical refinement rather than a new fitted prescription. Code commit: `b3a94b2c37ad4ea005127822c304855095cfd0b0`. Workflow/head commit: `a8ecf715f49ca9a45fde149087359924ec856b36`. GitHub Actions run: `33861440653`.

A `CONVERGED` raw result may remove only blocker index 2 and then unlock the already-frozen Iteration-412 exact15 assembly. A repeated `BLOCKED_CONVERGENCE` must remain negative/blocked evidence and moves the next gate to a dedicated auxiliary-mass derivative representation/error analysis; thresholds may not be weakened.

## Downstream guardrails

No complete `Tr U1^2` exists yet. Therefore q2-resolved `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` is still forbidden. Comparator-subtracted residual, `ANSATZ-003`, Fisher/resources and Source/Born subtraction remain forbidden under the retained guards.

MODEL_READINESS: 24%

Change: `0 pp`. One physical blocker was removed (index 11), but no stable readiness-rubric bucket closes until the exact 15/15 `Tr U1^2` coordinate and downstream comparator quotient are closed.
