# Recovery Delta — Iteration 546

Date: 2026-09-07

## Exact level-error correlation contract for frozen BASE/HALF/QUARTER diagnostic
Authoritative start: Iteration 545. Canonical QUARTER rank5 run `34136802871`, job `101789577462`, remained `in_progress`; no duplicate heavy Action was launched.

For `d1=BASE-HALF`, `d2=HALF-QUARTER`, `P=64d2-d1`, `Q=d1-16d2`, exact propagation of assembled level errors gives:

- `deltaP = -e_BASE + 65 e_HALF - 64 e_QUARTER`
- `deltaQ = +e_BASE - 17 e_HALF + 16 e_QUARTER`.

For bounded level errors `|e_i|<=eps_i`:
- `rho_P = eps_BASE + 65 eps_HALF + 64 eps_QUARTER`
- `rho_Q = eps_BASE + 17 eps_HALF + 16 eps_QUARTER`.

Fail-closed rule: a P/Q sign certificate is allowed only when the corresponding interval excludes zero.

For independent equal-variance level errors, exactly

`Cov(P,Q)/sigma^2 = [[8322,-2130],[-2130,546]]`,

with determinant `6912>0`, correlation `-0.9992391156789705`, covariance condition number `11375.520745421576`, and standard-deviation-map condition number `106.65608630275901`. The strong anti-correlation is caused by the shared HALF level and is diagnostic conditioning only, not Candidate-Gravity model-level near-degeneracy.

Classification: `PASS_ITER424_LEVEL_ERROR_CORRELATION_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

No frozen Iteration-424 threshold, parent dynamics, parameter convention, mass node, precision setting, or Iteration-532 successor order changed. Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Robust comparator-subtracted residual remains absent; `ANSATZ-003`, Fisher/resources remain BLOCKED.

Machine authority: `candidate_gravity/results/iteration546_iter424_level_error_correlation_contract.json`.
Reproducible audit: `candidate_gravity/code/iteration546_iter424_level_error_correlation_contract.py`.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; an exact error-propagation subgate closed, but no stable readiness rubric sector closed.

Exact next gate: after rank5 terminal completion, fail-closed raw-consume run `34136802871`. Only raw-valid PASS authorizes frozen rank6 `(-1.25e-6,+2.5e-6)`; scientific FAIL/BLOCKED stops advancement and operational failure permits only minimal rank5 repair.
