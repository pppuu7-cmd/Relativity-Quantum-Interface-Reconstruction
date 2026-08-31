# Recovery Delta — RQIR Iteration 153

**Date:** 2026-08-31  
**Authoritative change:** the first concrete finite C3 stochastic comparator block is now instantiated; it replaces the broad C3 capability mask only on the rows it actually derives.

## New comparator
`C3-PQCG-LIN-001`: linearized covariant postquantum-classical stochastic metric block with parameter vector `(D2,D0)`.

Frozen stochastic dynamics:

`box h_s = J_s + xi_s`, `<xi_s xi_s'>=2D_s delta_ss' delta^4`, for `s=2,0`.

The finite `N2` coordinate on the Iteration-149 smearing/probe layer is

`N2=A(5D2+D0)`, `A=258.83104475297773`.

Supported tangent `(N2,chi1R)` x `(D2,D0)` has rank `1/2` and singular values `[1319.7845479190407,0]`.

## Retained scientific distinction
This rank deficiency is `REGIME_SPECIFIC_NON_IDENTIFIABILITY`, not a consistency FAIL. The current single scalar noise coordinate identifies only one diffusion combination.

Retain:
- `C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS`;
- `NG-FUNNEL-011 — PARTIAL_COMPARATOR_ROWS_ARE_NOT_ZERO_ROWS`.

Unsupported C3 rows `C3sym`, `chi2R_even`, `chi2R_odd`, `soft2`, `tensor_geo`, `threshold` are BLOCKED, not zero.

Authorities:
- `candidate_gravity/comparators/C3-PQCG-LIN-001.md`;
- `analysis/c3_pqcg_linear_tangent_iteration153.py`;
- `results/c3_pqcg_linear_tangent_iteration153.json`;
- `candidate_gravity/C3_PQCG_LINEAR_TANGENT_ITERATION153.md`;
- `research_log/2026-08-31_iteration_153_c3_pqcg_linear_tangent.md`.

## Exact restart instruction
Resume at **Iteration 154**:
1. attempt a literature-grounded nonlinear extension from the same covariant CQ path-integral family, with one explicitly frozen nonlinear drift/backreaction or non-Gaussian noise term;
2. derive at least one genuine `chi2R` or `C3sym` coordinate from that same dynamics and test rank gain beyond the linear `N2` direction;
3. if the nonlinear C3 truncation requires unsupported conventions, record `BLOCKED_NONLINEAR_C3_SPECIFICATION` rather than inventing columns and proceed to a fixed nonlinear C4 comparator;
4. keep C5 higher-local/loop sectors BLOCKED and do not start Fisher/resources or `ANSATZ-003`.
