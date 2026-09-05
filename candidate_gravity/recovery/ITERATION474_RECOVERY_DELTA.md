# Iteration 474 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421. Exact unresolved physical set remains `[2]`. Latest completed numerical mass-support authority remains Iteration 473 while canonical rank-9 run `33983416847` is in progress.

## New exact provenance closure
For frozen central4 `c=(1/12,-2/3,+2/3,-1/12)`, exactly `sum(c)=0` and `||c||_2^2=65/72`.

For the 4x4 MP80↔MP120 discrepancy matrix `DeltaF`, define `DeltaD=c^T DeltaF c` and `P=I-(1/4)11^T`. Then

`DeltaD = c^T P DeltaF P c` exactly.

Hence all row/column-separable discrepancy modes `a1^T+1b^T+gamma11^T` lie in the exact nullspace of the assembled mixed derivative. Only `DeltaF_int=P DeltaF P` can contribute. Exact correlation-aware bound:

`|DeltaD| <= (65/72)||DeltaF_int||_F`.

Exact counterexample: `DeltaF=a1^T`, `a=(1,2,3,4)`, has max local absolute discrepancy 4 but `DeltaD=0` exactly. Together with Iteration 472, local MP sample status is neither sufficient nor necessary for assembled mixed-derivative MP status.

Classification: `PASS_MIXED_DERIVATIVE_PRECISION_NULLSPACE__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Future assembled audit must report `||P DeltaF P||_F` and verify raw versus double-centered `DeltaD` equality. Failure of that identity is implementation/provenance `BLOCKED`, not physics FAIL. Frozen assembled threshold `2e-6`, BASE↔HALF threshold `2e-5`, estimator `ds=-d_base`, dynamics, support order and promotion rules are unchanged.

## Exact next gate
Raw-consume canonical rank-9 run `33983416847` fail-closed. Only PASS permits Iteration-455 distinct rank 10. No duplicate heavy run was launched.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; no stable readiness-rubric component closed.
