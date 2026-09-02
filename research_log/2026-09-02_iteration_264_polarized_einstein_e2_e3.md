# RQIR Candidate Gravity research log — Iteration 264

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 263 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_263.md`, the Iteration-263 research log, recent commits, and GitHub Actions. Recent commits confirmed Iteration 263 as the actual front. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Took the exact next gate from Iteration 263: construct physical polarized Einstein EOM coefficients before any tensor reduction.
2. Reused the same exact nonlinear Einstein-tensor implementation previously used for the mixed soft-hard existence certificate, generalized to three distinct external TT Fourier modes.
3. Defined multilinear coefficients directly by amplitude derivatives of `G_mu_nu[eta + sum t_i h_i]` with no factorial convention.
4. Chose one null-soft TT leg `s` and two distinct spacelike hard TT legs `a,b`; verified `k_s^2=0` and `E1[s]=0` numerically.
5. Extracted nonzero `E2[s,a]`, `E2[s,b]`, `E2[a,b]`, and genuinely three-leg `E3[s,a,b]` with stable centered-difference convergence.
6. At step `3e-4` obtained `||E2[s,a]||_F=0.7456115521460782`, `||E2[s,b]||_F=0.7140951693123437`, `||E2[a,b]||_F=0.6270097790259529`, and `||E3[s,a,b]||_F=0.5815260517855062`; max `E3` component `0.4644883431881889`.
7. Verified all-six-leg permutation symmetry of `E3` to `4.39e-10` maximum mismatch and output tensor symmetry to `1.57e-10` at the same step.
8. Added reproducible code, JSON result, scientific note, recovery delta, article/negative-results update and authoritative front update.

Freeze:

`PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC`

Guardrail:

`DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO`

The result shows that the Iteration-263 projected `A3[s,a,b]` target is genuinely nontrivial: the `K0E3` and surviving `K1E2` sectors are not killed by the linear null-soft equation.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

No robust Candidate Gravity residual exists. `ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 263: **0 percentage points**. The physical nonlinear Einstein EOM vertices are now demonstrated nonzero and permutation-consistent on a distinct-leg test family, but the complete projected `K/A` numerator, orbit-metric `Q` dressing, tensor reduction and final C5 comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct physical `K0/K1/K2` on the same polarized three-leg family from frozen `R0/R1`, `P=partial R`, and `Gamma0/Gamma1/Gamma2`; combine with `E1/E2/E3` to assemble `A1/A2/A3`. In parallel derive physical `N1/N2` and obtain `Q1/Q2` only by exact inverse recursion. Assemble the 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical numerator exists; Fisher/resources, blind heavy integration and `ANSATZ-003` remain forbidden.
