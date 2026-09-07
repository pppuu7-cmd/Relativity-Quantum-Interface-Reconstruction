# Recovery Delta — Iteration 566

## New exact diagnostic authority
The frozen QUARTER 4x4 central4 mixed-derivative coefficient matrix is now pre-registered exactly as `C=w⊗w`, `w=[1,-8,+8,-1]`, normalization `1/(144 h^2)`.

Exact properties:
- `rank(C)=1`;
- all row sums and column sums vanish;
- every additive grid nuisance `F_ij=a_i+b_j+c` is annihilated exactly;
- additive row/column nuisance subspace dimension is `7` within the 16-coordinate grid;
- bounded common coordinate error gain is `9/(4 h^2)`;
- independent equal-variance error standard-deviation gain is `65/(72 h^2)`;
- corresponding variance gain is `4225/(5184 h^4)`.

Classification: `PASS_ITER424_QUARTER_FULL_STENCIL_GEOMETRY_ERROR_NORM_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Reproducible audit: `candidate_gravity/code/iteration566_iter424_quarter_full_stencil_geometry_audit.py`. Machine-readable result: `candidate_gravity/results/iteration566_iter424_quarter_full_stencil_geometry.json`.

## Interpretation
This is exact stencil/assembly geometry and error propagation only. It is not Candidate-Gravity model-level non-identifiability, near-degeneracy, comparator identity, consistency PASS/FAIL, or novelty evidence. It does not alter the frozen Iteration424/532 support order or thresholds.

## Heavy state
Rank11 `(+2.5e-6,-1.25e-6)` run `34168897005`, job `101885271903`, was still `in_progress` at freeze. No duplicate heavy run was launched. Only a raw-valid rank11 PASS may authorize rank12 `(+2.5e-6,+1.25e-6)`.

## Guardrails retained
Physical/operator authority remains Iteration411; blocker authority remains Iteration421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Upstream concrete `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. `ANSATZ-003` is not created. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change: `0 pp`; no additional stable model-level rubric sector was closed.
