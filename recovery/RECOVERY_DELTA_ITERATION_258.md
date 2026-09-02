# RECOVERY DELTA — Candidate Gravity Iteration 258

**Date:** 2026-09-02  
**Authoritative iteration:** 258  
**MODEL_READINESS: 24%**

## Delta from Iteration 257

Iteration 257 fixed the inverse-orbit recursion and forbade an independent `Q2`. Iteration 258 now constructs the required same-parent second-order orbit metric itself.

With the Iteration-252 exact factorization

`Nhat=W N_orb`,

set `V=W^-1`, so `N_orb=V Nhat`.

For the frozen TT background `g=eta+t epsilon exp(iq.x)` and `H=eta^-1 epsilon`,

`V0=eta`,

`V1=epsilon`,

`V2=(tr(H^2)/4) eta`.

Hence the physical coefficient is exactly

`N2 = V0 Nhat2 + V1 Nhat1 + V2 Nhat0`.

A finite-amplitude curved-operator certificate evaluates `Nhat^alpha_beta=delta^alpha_beta Box+R^alpha_beta`, extracts `Nhat0,Nhat1,Nhat2`, and independently differentiates `N_orb(t)=V(t)Nhat(t)`. At step `1e-4`,

`max|N2_direct-N2_assembled| = 1.51e-8`,

`||N2||_F = 1.9494673597527887`.

Freeze:

`PASS_SCOPED_PHYSICAL_ORBIT_METRIC_N2_CONSTRUCTION_AND_DIRECT_VALIDATION`

and

`NO_INDEPENDENT_NORB2_OR_Q2_ANSATZ`.

Physical `Q2` must be generated only from

`Q2=Q0N1Q0N1Q0-Q0N2Q0`.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This is operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or a novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 257: **0 percentage points**. A real second-order comparator-building block is closed, but no complete C5 comparator coordinate or robust algebraic residual closes a readiness-rubric category. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Generate `Q2` from the now-fixed physical `N2` using only the inverse recursion. Complete physical `A1,A2,A3` with `A3=K0E3+K1E2+K2E1`, assemble all six terms of `B3=[U1W]_3`, and apply weighted pairwise transpose/index/TT checks before tensor reduction. Do not use ordinary `U1` symmetry, do not introduce an independent `Q2`, and do not launch heavy integration, Fisher/resources, or `ANSATZ-003`.
