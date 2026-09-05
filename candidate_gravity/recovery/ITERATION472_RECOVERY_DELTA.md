# Iteration 472 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421. Exact unresolved physical set remains `[2]`. Latest completed numerical mass-support authority remains Iteration 470 while rank-8 run `33980045356` is in progress.

## New exact precision-provenance closure
For a linear assembled BASE or HALF operator `D=sum_i w_i F_i`, define `delta_i=F80_i-F120_i`, `s_i=max(1,|F80_i|,|F120_i|)`, local scaled precision discrepancy `e_i=|delta_i|/s_i`, and weighted magnitude envelope `E=sum_i |w_i|s_i`.

If all local samples obey `e_i<=eps_local`, then

`|DeltaD| <= B_sample_delta <= eps_local E`,

with `DeltaD=D80-D120` and `B_sample_delta=sum_i |w_i||delta_i|`.

Hence a sufficient condition for the frozen assembled MP threshold `tau=2e-6` is

`eps_local E / max(1,|D80|,|D120|) <= tau`.

Local scaled PASS alone cannot imply this because the amplification envelope is not bounded by the local certificate. Exact counterexample using actual equal-and-opposite central4 sample weights `+4/9,-4/9`: `F120=(10^30,10^30)`, `F80=(10^30+1,10^30-1)`. Both local scaled discrepancies are `<=1e-30`; nevertheless `D120=0`, `D80=8/9`, so assembled scaled discrepancy is `8/9 >> 2e-6`.

Classification: `PASS_LOCAL_TO_ASSEMBLED_MP_SUFFICIENCY_CONTRACT__NON_PROMOTING`.

This strengthens the rationale for the already-frozen Iterations 458/460 assembled MP gate. Failure of the assembled condition is precision/provenance `BLOCKED` or unproven, never Candidate-Gravity consistency FAIL. No threshold, estimator, dynamics, support order, or ansatz rule changes.

## Exact next gate
Do not duplicate rank 8. Raw-consume run `33980045356` fail-closed when complete. PASS permits only Iteration-455 distinct rank 9 `u=+5e-6, v=-5e-6`, multiplicity 2. BLOCKED requires localization at rank 8 under unchanged frozen conventions.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; no stable readiness-rubric component closed.
