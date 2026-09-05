# Iteration 471 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421. Exact unresolved physical set remains `[2]`. Latest completed numerical mass-support authority remains Iteration 470 while rank-8 run `33980045356` is in progress.

## New exact provenance closure
For assembled MP80↔MP120 differences, let `DeltaF=F80-F120` and form the four exact signed parity quartets `DeltaQ_ab` using the frozen central4 tensor coefficients. Then

`DeltaD = sum alpha_ab DeltaQ_ab`,

`B_quartet_delta = sum |alpha_ab||DeltaQ_ab|`,

`B_sample_delta = sum |alpha_ab| sum_signs |DeltaF|`.

Exact triangle inequalities give

`|DeltaD| <= B_quartet_delta <= B_sample_delta`.

This refines, but never replaces or weakens, the Iteration-460 weighted MP discrepancy bound. Future BASE/HALF assembly must report `B_quartet_delta` in addition to the existing sample-level bound, plus diagnostic ratios `rho_precision_parity=B_quartet_delta/B_sample_delta` and `rho_precision_shell=|DeltaD|/B_quartet_delta` when denominators are nonzero.

Classification: `PASS_MP_DISCREPANCY_QUARTET_BOUND__DIAGNOSTIC_ONLY_NON_PROMOTING`.

A bound violation is implementation/provenance `BLOCKED`, never physics FAIL. Cancellation ratios are diagnostic only and cannot promote novelty, non-identifiability, consistency, or physical residual claims.

## Exact next gate
Do not duplicate rank 8. Raw-consume run `33980045356` fail-closed when complete. PASS permits only Iteration-455 distinct rank 9 `u=+5e-6, v=-5e-6`, multiplicity 2. BLOCKED requires localization at rank 8 under unchanged frozen conventions.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; no stable readiness-rubric component closed.
