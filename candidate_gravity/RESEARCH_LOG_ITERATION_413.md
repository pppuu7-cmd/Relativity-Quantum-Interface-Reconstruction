# Candidate Gravity Research Log — Iteration 413

Date: 2026-09-04

Repository source of truth was re-read first: `CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_412.md`, recent logs/commits, and Actions. Iteration-411 run `33851983789` had completed, so both artifacts were downloaded and raw-validated rather than trusting the green workflow.

Index 11 / class 16 / `q^2=-0.34` is physically `CONVERGED`: artifact `9931076355`, digest `sha256:8551fba98b0f3f218960820a01369ca183da1234d22754bd5c647fa8909cf6f8`, raw scientific JSON SHA-256 `f8aea08be16636dcf5d83afaa29dd3059c734a1a3ad8f778f07ef53b3041abf1`, `D_s TrU1^2=+0.013050543643260309`, mass-step error `5.421327239850046e-06 < 2e-05`, direct original-integrand cross-check `1.1526331104849685e-12 < 2e-06`.

Index 2 / class 3 / `q^2=-1` remains `BLOCKED_CONVERGENCE`: artifact `9930938547`, digest `sha256:3c34f0110e3dbf97b7abf5dedf7b70bf918d4bb3a9e2b5572c7d1f92df7120c2`, raw SHA-256 `53a185ae9825cde0a273161b1ee093ede54103b52d513ea291a3bfc8e1381486`. Its diagnostic coarse value is `+0.003560682203382001`, but it is not authority because the mass-step discrepancy is `5.0042074065288766e-05 > 2e-05`. Structural and direct-integrand checks pass, so the remaining issue is localized to auxiliary-mass finite-difference convergence.

The exact unresolved physical double-double set is therefore `[2]`. The prospective Iteration-412 exact15 assembly remains fail-closed and cannot run yet.

To satisfy anti-idle without blind angular escalation, Iteration 413 freezes one deterministic next mass-step halving pair for index 2: `h=2.5e-6`, `h/2=1.25e-6`, with the same physical integrand, analytic/spectral representation, central4 x central4 stencil, normalization, held-out checks, and unchanged `2e-5` threshold. Code commit `b3a94b2c37ad4ea005127822c304855095cfd0b0`; workflow commit `a8ecf715f49ca9a45fde149087359924ec856b36`; run `33861440653` launched.

MODEL_READINESS: 24%

Change: 0 pp. Index 11 is closed, but no readiness-rubric bucket is complete until index 2 closes, exact15 `Tr U1^2` is assembled, and the downstream comparator-subtracted residual is established.
