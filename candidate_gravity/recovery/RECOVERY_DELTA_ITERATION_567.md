# Recovery Delta — Iteration 567

## New exact diagnostic authority
The frozen QUARTER mixed central4 assembly is a single linear functional `D_uv=<C,F>/(144 h^2)` with `C=w⊗w`, `w=[1,-8,8,-1]`.

Exact geometry:
- `rank(C)=1`;
- 16-dimensional grid-data space kernel dimension = `15`;
- additive row/column nuisance subspace dimension = `7`, entirely inside the kernel;
- therefore there are `8` additional invisible non-additive directions modulo additive nuisance;
- `||C||_F^2=16900`, `||C||_F=130`;
- orthogonal projector onto the sole stencil-visible mode: `P_C(F)=<C,F>/16900 * C`;
- visible-component norm: `||P_C(F)||_F=(72/65) h^2 |D_uv|`.

Classification: `PASS_ITER424_QUARTER_STENCIL_NULLSPACE_PROJECTOR_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is stencil-functional regime-specific non-identifiability only. It is not Candidate-Gravity model-level non-identifiability, near-degeneracy, comparator identity, consistency PASS/FAIL, or novelty evidence.

Reproducible audit: `candidate_gravity/code/iteration567_iter424_quarter_stencil_nullspace_projector_audit.py`. Machine-readable result: `candidate_gravity/results/iteration567_iter424_quarter_stencil_nullspace_projector.json`.

## Heavy state
Rank11 `(+2.5e-6,-1.25e-6)` run `34168897005`, job `101885271903`, remained `in_progress`. No duplicate/reordered heavy run was launched. Only a raw-valid rank11 PASS may authorize frozen rank12 `(+2.5e-6,+1.25e-6)`.

## Guardrails retained
Physical/operator authority remains Iteration411; blocker authority remains Iteration421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Concrete `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change: `0 pp`; no additional stable model-level rubric sector was closed.
