# Recovery Delta — Iteration 564

## New exact authority
Iteration 564 freezes the final frozen rank11/rank12 QUARTER pair into common and differential modes before their heavy values are known.

Classification:
`PASS_ITER424_FINAL_PAIR_COMMON_DIFFERENTIAL_MODE_DECOMPOSITION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`

Files:
- code: `candidate_gravity/code/iteration564_iter424_final_pair_mode_decomposition_exact.py`
- result: `candidate_gravity/results/iteration564_iter424_final_pair_mode_decomposition_exact.json`
- log: `candidate_gravity/research_log/2026-09-08_iteration_564.md`

## Exact result
For rank11 `(+2h,-h)` and rank12 `(+2h,+h)`, the frozen central4 tensor coefficient vector is `[+8,-8]`.

Using orthonormal modes
- `q_common=(F11+F12)/sqrt(2)`
- `q_diff=(F11-F12)/sqrt(2)`

the coefficient vector is exactly `[0,8*sqrt(2)]`.

Thus the final unknown contribution after rank10 is entirely differential:

`T_tail=(F11-F12)/(18 h^2)`.

The common mode cancels exactly. The mode transform has condition number 1.

For equal marginal variance `sigma^2` and coordinate correlation `rho`, the mode covariance is

`diag(sigma^2(1+rho), sigma^2(1-rho))`,

and

`Var(T_tail)=sigma^2(1-rho)/(162 h^4)`.

## Guardrail
This exact common-mode null is not a physical `u<->v` symmetry and never authorizes support substitution. Both final coordinates remain mandatory because the routed integrand is not exchange-equivalent (Iterations 552–555).

No rank skipping/reordering, no zero fill, no threshold relaxation, no smaller `h`, no precision changes, no `ANSATZ-003`, no Fisher/resources.

## Heavy state
At the Iteration564 freeze, rank10 run `34165534613`, job `101875710349` was still inside the full-z MP80/MP120 stage. Do not duplicate. Only raw-valid rank10 PASS authorizes rank11.

## Readiness
MODEL_READINESS remains **24%**.
