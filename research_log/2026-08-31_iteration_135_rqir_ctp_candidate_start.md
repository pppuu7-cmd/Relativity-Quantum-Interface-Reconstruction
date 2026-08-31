# RQIR Research Log — Iteration 135

**Date:** 2026-08-31  
**Branch:** Candidate Gravity  
**Model:** `ANSATZ-RQIR-CTP-001` v0.1

## Trigger

After cross-checking the RQIR 1/2/3 development and the frozen Candidate Gravity front, the next required scientific step was to instantiate a dynamics that differs from the exact C5 perturbative-QG reference before spending any detector-optimization resources.

## Retained RQIR constraints

The new model must preserve the conclusions already frozen by RQIR:

- mean `J`, symmetrized noise `N`, and ordered/retarded response `D/chi^R` are distinct operational layers;
- a claimed model must derive them from one dynamics rather than tune them independently;
- exact hard calibration constraints are eliminated before Fisher profiling;
- a raw nonzero signal is not identified if nuisance directions remove it;
- a model-specific detector/resource calculation is premature until a nondegenerate theory direction exists;
- comparator class identity cannot be repaired by better statistics.

## New model choice

Created `ANSATZ-RQIR-CTP-001`, a weak-field Gaussian CTP ansatz with a single positive spectral form factor in the conserved-source spin-2 sector.

Frozen spectral shape:

`rho_hat(s)=exp(1-s)Theta(s-1)`.

Causal form factor:

`zeta=-(p^2+i0 p^0)/M_*^2`,

`F_R=zeta int_1^infty ds rho_hat(s)/(s+zeta)`.

Retarded kernel:

`K_R^(2)=K_GR,R^(2)[1+beta F_R]`, `beta>=0`.

The absorptive/noise sector is tied to the same spectral kernel under the v0.1 vacuum spectral relation. There is no independent noise-amplitude parameter.

## Scoped analytic result

On the spacelike axis, `x=-p^2/M_*^2>=0`,

`F_E=x exp(1+x)E1(1+x)`.

Positivity/normalization of `rho_hat` implies

`0<=F_E<=x/(1+x)<1`.

Hence

`1+beta F_E>=1`

for `beta>=0`: no additional Euclidean zero of the multiplicative spin-2 kernel.

Infrared coefficient:

`F_E=0.596347362323... x+O(x^2)`.

Therefore the deformation vanishes at the GR pole.

## Reproducible numerical audit

Added:

- `analysis/candidate_gravity_rqir_ctp_iteration135.py`;
- `results/candidate_gravity_rqir_ctp_iteration135.json`.

Recorded result: `PASS_SCOPED`.

## Scientific interpretation

This is **not** a quantum-gravity discovery claim. It is the first explicit RQIR-driven candidate family with a nontrivial beta direction and a linked response/noise fingerprint.

The deep-IR expansion is expected to be degenerate with ordinary gravitational EFT Wilson coefficients at finite order. Known nonlocal/form-factor gravity also occupies nearby structural territory. QG-007 therefore remains BLOCKED pending explicit prior-art/comparator mapping.

## Gates after Iteration 135

- QG-001: PARTIAL;
- QG-002: PASS, scoped to the declared linearized Gaussian CTP effective dynamics;
- QG-003: NOT_TESTED;
- QG-004: BLOCKED;
- QG-005: PARTIAL;
- QG-006: NOT_TESTED;
- QG-007: BLOCKED;
- QG-008: NOT_TESTED;
- QG-009/QG-010: BLOCKED.

## Frozen next iteration

Iteration 136 must audit the Lorentzian continuation before any detector work:

1. compute the branch-cut discontinuity for `p^2>=M_*^2`;
2. search for physical-sheet zeros of `1+beta F_R` on a frozen `(beta,p^2/M_*^2)` domain;
3. determine whether the positive input spectral density yields a valid dressed-propagator positivity statement;
4. restore the complete tensor structure needed for the conserved-source Ward test;
5. compare explicitly to known nonlocal/form-factor and C5 structures.

If this gate fails, reject/supersede the ansatz rather than tuning the spectral shape after seeing the result.
