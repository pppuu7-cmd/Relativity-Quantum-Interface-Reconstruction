# RQIR Candidate Gravity research log — Iteration 257

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 256 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_256.md`, the Iteration-256 research log, recent commits, and GitHub Actions. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Kept the frozen weighted object `U1 W = Q A Q` with `Q=N_orb^-1`, never ordinary `U1` symmetry.
2. Expanded `N=N0+tN1+t^2N2+...`, `Q=Q0+tQ1+t^2Q2+...` and solved `NQ=I` order by order:
   - `Q0=N0^-1`;
   - `Q1=-Q0N1Q0`;
   - `Q2=Q0N1Q0N1Q0-Q0N2Q0`.
3. Proved that symmetric `N0,N1,N2` imply symmetric `Q0,Q1,Q2`; hence `Q2` is not an independent ansatz or vertex family.
4. Reorganized the frozen cubic coefficient

`B3=Q0A3Q0+Q1A2Q0+Q0A2Q1+Q2A1Q0+Q0A1Q2+Q1A1Q1`

into two individually symmetric terms and two transpose pairs. If complete same-parent `A1,A2,A3` are symmetric, then `B3=B3^T` follows pairwise; no global fine-tuned six-term cancellation is needed.
5. Added a deterministic reproducible certificate. It gives inverse-series error `5.55e-17`, pairwise transpose residuals `2.17e-19` and `6.78e-20`, and total cubic symmetry residual `8.67e-19`.

Freeze:

`PASS_SCOPED_CUBIC_WEIGHTED_WARD_PAIRWISE_REDUCTION`

and

`NO_INDEPENDENT_Q2_RESOLVENT_ANSATZ`.

This is a scoped exact algebraic PASS and false-branch elimination result. It is not a physical comparator coordinate, not an exact comparator identity, not a Candidate Gravity residual, not near-degeneracy, not regime-specific non-identifiability, and not a consistency FAIL.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 256: **0 percentage points**. The correct inverse recursion and pairwise Ward reduction shrink the upstream library, but no physical C5 comparator coordinate or robust residual closes a rubric block. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct physical same-parent `N2` in the frozen `D=4, Lambda=0, a=-1/2` convention and derive `Q2` only through the exact recursion. Complete `A1,A2,A3`, retaining `A3=K0E3+K1E2+K2E1`, then apply the pairwise weighted-Ward certificate before tensor reduction. No independent `Q2` ansatz, no heavy integration, no Fisher/resources, and no `ANSATZ-003`.
