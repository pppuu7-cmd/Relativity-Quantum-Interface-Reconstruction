# RQIR Candidate Gravity — Iteration 258

## Physical same-parent second-order orbit-metric coefficient `N2`

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Starting authority

Authoritative front: Iteration 257. Frozen parent remains `D=4`, `Lambda=0`, DeWitt `a=-1/2`, linear covariant-metric split, with no ansatz promotion and no Fisher/resources before a robust nonzero algebraic residual.

Iteration 252 fixed the exact distinction

`Nhat = W N_orb`,

where `N_orb_{alpha beta}=R^i_alpha G_ij R^j_beta` is the symmetric orbit metric and `Nhat` is the minimal mixed-index ghost operator. Iteration 257 then fixed

`Q2 = Q0 N1 Q0 N1 Q0 - Q0 N2 Q0`

for `Q=N_orb^-1`, forbidding any independent `Q2` ansatz.

This iteration constructs the required physical `N2` coefficient from the same parent rather than introducing a new resolvent degree of freedom.

## Exact second-order factorization

Write

`V := W^-1`, so `N_orb = V Nhat`.

For the frozen hard TT background

`g = eta + t epsilon exp(i q.x)`,

with `tr(eta^-1 epsilon)=0`, define `H=eta^-1 epsilon`. Since

`V = g/sqrt(|g|)`,

its coefficient expansion is

`V0 = eta`,

`V1 = epsilon`,

`V2 = (tr(H^2)/4) eta`,

where coefficients are defined without factorials: `V=V0+t V1+t^2 V2+...`.

Therefore, if

`Nhat=Nhat0+t Nhat1+t^2 Nhat2+...`,

then the physical second-order orbit-metric coefficient is exactly

`N2 = V0 Nhat2 + V1 Nhat1 + V2 Nhat0`.

No independent `N2` or `Q2` object is permitted.

## Direct curved-operator validation

The reproducible certificate evaluates the full finite-amplitude minimal vector operator

`Nhat^alpha_beta = delta^alpha_beta Box + R^alpha_beta`

on the same TT plane-wave background, extracts `Nhat0,Nhat1,Nhat2` by symmetric finite differences, constructs `N2` through the exact formula above, and independently extracts `N_orb,2` from the finite-amplitude product `V(t) Nhat(t)`.

For the frozen TT polarization:

- `tr H^2 = 1` to machine precision;
- TT trace is zero;
- transversality residual is `8.16e-18`.

At step `1e-4`:

- `||Nhat2||_F = 1.7777513761962513`;
- `||N2||_F = 1.9494673597527887`;
- `max|N2_direct-N2_assembled| = 1.51e-8`.

The error decreases systematically from `2.93e-5` at step `1e-2` to the `1e-8` level, consistent with the finite-difference extraction plus floating-point floor.

Freeze:

`PASS_SCOPED_PHYSICAL_ORBIT_METRIC_N2_CONSTRUCTION_AND_DIRECT_VALIDATION`.

Guardrail:

`NO_INDEPENDENT_NORB2_OR_Q2_ANSATZ`.

The physical `Q2` must now be generated only as

`Q2=Q0 N1 Q0 N1 Q0-Q0 N2 Q0`.

## Scientific classification

This is a scoped comparator-authority PASS. It is not a C5 physical comparator coordinate, not a Candidate Gravity residual, not an exact comparator identity, not near-degeneracy, not regime-specific non-identifiability, and not a consistency FAIL.

The umbrella status remains

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

with

`BLOCKED_NOT_ZERO`.

The blocker is narrower: the second-order orbit-metric/resolvent sector is now constructively fixed for the frozen TT test channel; the remaining upstream work is completion of physical `A1,A2,A3` and insertion of this `Q2` into the weighted six-term cubic numerator before tensor reduction.

## Reproducibility

- `candidate_gravity/code/iteration258_vd_orbit_metric_n2.py`
- `candidate_gravity/results/iteration258_vd_orbit_metric_n2.json`

## Readiness

MODEL_READINESS: 24%

Change from Iteration 257: **0 percentage points**. A genuine second-order same-parent orbit-metric coefficient has been constructed and the independent-`Q2` ambiguity is eliminated physically, but no complete C5 comparator coordinate or robust nonzero residual closes a readiness-rubric block. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate — Iteration 259

Use the now-fixed physical `N2` to generate `Q2` only through the Iteration-257 recursion. Complete the physical tensor coefficients `A1,A2,A3`, with `A3=K0E3+K1E2+K2E1`, then assemble

`B3=Q0A3Q0+Q1A2Q0+Q0A2Q1+Q2A1Q0+Q0A1Q2+Q1A1Q1`

and apply the weighted pairwise transpose/index/TT certificate before any loop tensor reduction. No ordinary `U1` symmetry test, no independent `Q2`, no heavy integration, no Fisher/resources, and no `ANSATZ-003`.
