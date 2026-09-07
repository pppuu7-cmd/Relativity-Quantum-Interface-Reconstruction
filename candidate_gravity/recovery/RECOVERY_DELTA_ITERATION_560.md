# RECOVERY DELTA — ITERATION 560

Date: 2026-09-08

## New exact remaining-orbit tail authority
For the frozen QUARTER central4 stencil, after a future raw-valid rank9 PASS the only incomplete exchange orbits are ranks6/11 and ranks10/12. Their integer coefficient sums are `+16` and `-16`, respectively, so the combined remaining sector has exact zero total coefficient.

With exchange-orbit averages

`E_A=[F(-1,+2)+F(+2,-1)]/2`,

`E_B=[F(+1,+2)+F(+2,+1)]/2`,

the full remaining normalized stencil contribution is exactly

`T_rem=(E_A-E_B)/(9 h^2)`.

Hence a common constant offset across the four remaining coordinates cancels exactly.

Fail-closed bounded-error propagation:

`|delta T_rem| <= (eps1+eps2+eps3+eps4)/(18 h^2)`

for four coordinate-wise absolute error bounds, or equivalently

`|delta T_rem| <= (eps_A+eps_B)/(9 h^2)`

for the two orbit-average error bounds.

Classification:
`PASS_ITER424_REMAINING_ORBIT_TAIL_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is assembly/numerical conditioning only. It does not authorize rank reordering/skipping, u<->v substitution, zero fill, or physical promotion.

Machine-readable authority: `candidate_gravity/results/iteration560_iter424_remaining_orbit_tail_contract_exact.json`.
Reproducible audit: `candidate_gravity/code/iteration560_iter424_remaining_orbit_tail_contract_exact.py`.

## Active heavy process
Rank9 run `34160111095` was still `in_progress` at the start of Iteration 560 and was not duplicated. On terminal completion, raw-consume fail-closed. Only raw-valid PASS authorizes rank10 `(+1.25e-6,+2.5e-6)`.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; a genuine assembly-control subgate closed, but no new model-level readiness sector completed.
