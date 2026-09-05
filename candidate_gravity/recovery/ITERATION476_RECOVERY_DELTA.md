# Iteration 476 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 (`BLOCKED_CONVERGENCE`), exact unresolved physical set `[2]`. Iteration 475 remains latest completed numerical mass-support authority. Canonical rank-11 run `33989317870` remains the sole active heavy gate and was not duplicated.

## New exact structural/provenance authority
For frozen central4 `c=(1/12,-2/3,+2/3,-1/12)` and any 4x4 MP discrepancy matrix `DeltaF`,

`DeltaD = c^T DeltaF c = <c c^T, DeltaF>_F`.

Exact rational values:
- `||c||_2^2 = 65/72`;
- for `A=cc^T`, `||A||_F = 65/72` and `||A||_F^2=4225/5184`;
- the derivative-sensitive matrix subspace is one-dimensional;
- the exact full functional nullspace has dimension 15.

The unique Frobenius-sensitive projection is

`DeltaF_sens=(DeltaD/(65/72)^2)cc^T=(5184/4225)DeltaD cc^T`,

and

`||DeltaF_sens||_F=(72/65)|DeltaD|`.

All Frobenius-orthogonal discrepancy modes are exactly invisible to the frozen mixed derivative.

With Iteration-474 double-centering projector `P=I-(1/4)11^T` and Iteration-467 odd projector `Qo=(I-R)/2`, exact identities `Pc=c` and `Qo c=c` give

`DeltaD=<cc^T,DeltaF>_F=<cc^T,P DeltaF P>_F=<cc^T,Qo DeltaF Qo>_F`,

with hierarchy

`|DeltaD| <= (65/72)||Qo DeltaF Qo||_F <= (65/72)||P DeltaF P||_F <= (65/72)||DeltaF||_F`.

Dimension hierarchy: ambient matrix space 16, double-centered sector 9, odd-odd sector 4, derivative-sensitive sector 1. Thus the odd-odd sector itself contains a 3-dimensional exact derivative nullspace.

Classification: `PASS_MIXED_DERIVATIVE_RANK1_PRECISION_SENSITIVE_MODE__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is implementation/provenance/conditioning only. It changes no frozen estimator, threshold, dynamics, support order, coordinate state, or physical promotion rule. Failure of the exact projection identities in future assembly is implementation/provenance BLOCKED, not physics FAIL.

Reproducible code: `candidate_gravity/code/iteration476_mixed_derivative_rank1_precision_mode.py`.
Result: `candidate_gravity/results/iteration476_mixed_derivative_rank1_precision_mode.json`.

`ANSATZ-003` remains uncreated. Comparator-subtracted residual and Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: **0 percentage points**. Precision attribution is strengthened, but no additional stable readiness-rubric component is fully closed.

## Exact next gate
Raw-consume canonical rank-11 run `33989317870` fail-closed. PASS permits only the next UNTESTED frozen Iteration-455 manifest coordinate; BLOCKED requires localization at rank 11 without threshold/dynamics/routing/precision changes.
