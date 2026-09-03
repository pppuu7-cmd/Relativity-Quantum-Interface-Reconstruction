# Recovery Delta — Candidate Gravity Iteration 345

Date: 2026-09-03

## Scope

Route-only validation of the functional transpose needed for physical `Tr U2` after the same-parent physical `A1/A2` authority (Iteration 341), `N/Y` bridge (Iteration 342), primary `A.T/A` orientation and `Hinv_VD=-K^-1` convention (Iteration 340), and shifted graviton inverse routing (Iteration 339).

## Raw Actions authority

- run: `33769608279`
- job: `100696159016`
- artifact: `9899021604` (`iteration345-result`)
- artifact digest: `sha256:adaf0d811580d697791f7f33ef8922fcb487c82362c3ed714591a5ac6e0e8cb7`
- scientific JSON SHA-256: `41edecce8d1a8ac4e90d8f513ac4367b5237db0d9db614f0e9119cb4ce06988a`
- workflow head: `755599b4027668c0cd7b5a766a13d8a4b2ab912d`

The artifact is schema-valid and independently inspected; workflow green status alone was not used as scientific authority.

## Result

Frozen Fourier-routing rule:

- right insertion: `A_R(Q;p)=A(Q;p)`, routing `p -> p+Q`;
- functional transpose: `A_T(Q;k)=A(Q;-k-Q)^T`, routing `k -> k+Q`;
- the external background momentum remains the same `+Q` under transpose;
- closed-loop condition `sum_i Q_i=0` is unchanged.

Validation over six fixtures gives max kernel error `3.47e-18`, max bilinear pairing error `1.73e-17`, max phase-closure error `5.55e-17`, and exact closed-triad loop error `0`. The deliberately wrong same-`k` transpose is separated by at least `1.22e-2`, well above the frozen `1e-5` discrimination threshold.

Authority:

`PASS_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_FROM_FROZEN_ITERATION341_A1_AUTHORITY__TRU2_CUBIC_ROUTE_ASSEMBLY_AUTHORIZED_NEXT`.

Iterations 343 and 344 remain preserved implementation/gate-design FAILs. Their hand-coded Eq.55 oracle mismatch is not reclassified and no threshold was weakened. Component correctness remains sourced from independently validated Iteration 341; Iteration 345 isolates routing only.

## Status

- frozen: physical `A1/A2` from Iteration 341;
- frozen: `N/Y` bridge from Iteration 342;
- frozen: `A.T/A` orientation and `Hinv_VD=-K^-1` sign from Iteration 340;
- frozen: shifted graviton inverse routing from Iteration 339;
- frozen: functional-transpose Fourier routing from Iteration 345;
- authorized next: assemble and independently validate the 12 surviving cubic-background `Tr U2` routes from Iteration 308 before any cut integration;
- still forbidden: Source/Born subtraction, `ANSATZ-003`, Fisher/resources, blind full-C5.

The independent determinant Iteration 335 replacement run `33759144658` remains in progress and must not be duplicated.

MODEL_READINESS: 24%

Change from Iteration 340: `0 pp`; a real U2 routing prerequisite closed, but no readiness-rubric bucket and no robust comparator-subtracted residual closed.
