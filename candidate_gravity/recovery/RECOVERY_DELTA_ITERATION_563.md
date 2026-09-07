# Recovery Delta — Iteration 563

## Authority added
Iteration 563 freezes a prospective exact assembly/error contract for the final two QUARTER support coordinates after a future raw-valid PASS of rank10.

Classification:
`PASS_ITER424_POST_RANK10_TWO_POINT_TAIL_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`

Files:
- `candidate_gravity/code/iteration563_iter424_post_rank10_two_point_tail_contract_exact.py`
- `candidate_gravity/results/iteration563_iter424_post_rank10_two_point_tail_contract_exact.json`
- `candidate_gravity/research_log/2026-09-08_iteration_563.md`

## Exact retained relation
Frozen central4 nodes are `[-2,-1,+1,+2]`, weights are `[1,-8,+8,-1]`, and the mixed normalization is `1/(144 h^2)`.

After raw-valid rank10, only ranks11 and12 remain unknown:
- rank11 `(+2h,-h)` coefficient `+8`;
- rank12 `(+2h,+h)` coefficient `-8`.

Hence

`T_tail=[F(+2h,-h)-F(+2h,+h)]/(18 h^2)`.

With common/differential coordinates `m=(F11+F12)/2`, `d=(F11-F12)/2`, the common mode cancels exactly and

`T_tail=d/(9 h^2)`.

This is a one-dimensional remaining assembly mode, but two physical support coordinates are still required. No rank skipping or support substitution follows.

## Fail-closed uncertainty contract
For bounded coordinate errors,

`|delta T_tail| <= (eps11+eps12)/(18 h^2)`.

For independent equal-variance coordinate errors,

`Var(T_tail)=sigma^2/(162 h^4)` and `Std(T_tail)=sigma/(9 sqrt(2) h^2)`.

## Current repository authority
Iteration562 raw-consumed rank9 PASS, closing `9/12=75%` new QUARTER support and `13/16=81.25%` total QUARTER coordinates including HALF-overlap corners.

Canonical rank10 `(+1.25e-6,+2.5e-6)` run `34165534613`, job `101875710349`, is the sole active heavy successor. Workflow status is not scientific authority. Only raw-valid PASS authorizes rank11 `(+2.5e-6,-1.25e-6)`.

## Retained blockers
Physical/operator authority remains Iteration411. Physical blocker remains Iteration421 `BLOCKED_CONVERGENCE` with unresolved set `[2]`. Concrete robust comparator-subtracted residual remains absent. `ANSATZ-003`, Fisher, and resources remain BLOCKED.

## Readiness
MODEL_READINESS: 24%

Readiness change: 0 percentage points. Iteration563 closes an exact diagnostic/assembly subgate only; no additional stable model-level readiness sector is complete.
