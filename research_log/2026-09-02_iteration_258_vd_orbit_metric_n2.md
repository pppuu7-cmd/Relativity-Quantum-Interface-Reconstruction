# RQIR Candidate Gravity research log — Iteration 258

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 257 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_257.md`, the Iteration-257 research log, recent commits, and GitHub Actions. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Preserved the Iteration-252 exact factorization `Nhat=W N_orb` and Iteration-257 inverse recursion; no independent `N2` or `Q2` ansatz was introduced.
2. Set `V=W^-1`, so `N_orb=V Nhat`.
3. For the frozen TT background `g=eta+t epsilon exp(i q.x)`, derived the weight-inverse coefficients
   - `V0=eta`,
   - `V1=epsilon`,
   - `V2=(tr(H^2)/4) eta`, `H=eta^-1 epsilon`.
4. Derived the exact second-order physical orbit-metric coefficient

`N2 = V0 Nhat2 + V1 Nhat1 + V2 Nhat0`.

5. Extended the finite-amplitude curved-operator calculation of the minimal vector operator `Nhat^alpha_beta=delta^alpha_beta Box+R^alpha_beta` to second order and independently extracted the second coefficient of the product `V(t)Nhat(t)`.
6. On the frozen TT channel, the direct and assembled `N2` agree to `1.51e-8` at step `1e-4`, with `||N2||_F=1.9494673597527887`; TT transversality residual is `8.16e-18` and `tr H^2=1` to machine precision.

Freeze:

`PASS_SCOPED_PHYSICAL_ORBIT_METRIC_N2_CONSTRUCTION_AND_DIRECT_VALIDATION`

and guardrail

`NO_INDEPENDENT_NORB2_OR_Q2_ANSATZ`.

The physical inverse coefficient must be generated only by

`Q2=Q0N1Q0N1Q0-Q0N2Q0`.

This is a scoped comparator-authority PASS, not a C5 physical comparator coordinate, not a Candidate Gravity residual, not an exact comparator identity, not near-degeneracy, not regime-specific non-identifiability, and not a consistency FAIL.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 257: **0 percentage points**. The physical second-order orbit-metric/resolvent sector is now constructively fixed in the frozen TT test channel, but the full C5 comparator coordinate and robust residual remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Generate physical `Q2` from the fixed `N2` using only the exact inverse recursion. Complete physical `A1,A2,A3`, retaining `A3=K0E3+K1E2+K2E1`, assemble the six-term weighted cubic `B3=[U1W]_3`, and apply the pairwise weighted transpose/index/TT certificate before tensor reduction. No ordinary `U1` symmetry test, no independent resolvent ansatz, no heavy integration, no Fisher/resources, and no `ANSATZ-003`.
