# Recovery Delta — RQIR Iteration 135

**Date:** 2026-08-31  
**Authoritative scientific change:** first RQIR-driven Candidate Gravity ansatz instantiated.

## Previous front

Iteration 134 ended with:

- Candidate Gravity infrastructure READY;
- `ANSATZ-PQG-EFT-001` retained as the perturbative-QG C5 reference;
- QG-007 permanently failed for that reference due exact theory-class degeneracy;
- next priority: create a genuinely distinct `ANSATZ-*` before detector optimization.

## New front

Created:

`candidate_gravity/models/ANSATZ-RQIR-CTP-001/`

with:

- `MODEL.md`;
- `GATE_STATUS.yaml`;
- `ASSUMPTIONS_LEDGER.md`;
- `DERIVATION_MAP.md`;
- `COMPARATOR_STATUS.md`.

## Core v0.1 equations

`rho_hat(s)=exp(1-s)Theta(s-1)`,

`zeta=-(p^2+i0 p^0)/M_*^2`,

`F_R=zeta int_1^infty ds rho_hat(s)/(s+zeta)`,

`K_R^(2)=K_GR,R^(2)[1+beta F_R]`,

with `beta>=0`, `M_*>0`.

Response and Gaussian noise are tied to the same spectral object; they are not independent RQIR fit functions.

## New scoped result

For spacelike `x=-p^2/M_*^2>=0`,

`F_E=x exp(1+x)E1(1+x)`

and

`0<=F_E<=x/(1+x)<1`.

Hence `1+beta F_E>=1` for `beta>=0`, so no extra Euclidean/spacelike zero exists in the frozen v0.1 multiplicative spin-2 kernel.

IR slope:

`e E1(1)=0.596347362323...`.

This does not prove Lorentzian ghost freedom.

## Reproducibility

Run:

`python analysis/candidate_gravity_rqir_ctp_iteration135.py`

Expected output file:

`results/candidate_gravity_rqir_ctp_iteration135.json`

Expected `overall`:

`PASS_SCOPED`.

## Current gate state

- QG-001 PARTIAL;
- QG-002 PASS scoped;
- QG-003 NOT_TESTED;
- QG-004 BLOCKED;
- QG-005 PARTIAL;
- QG-006 NOT_TESTED;
- QG-007 BLOCKED;
- QG-008 NOT_TESTED;
- QG-009/QG-010 BLOCKED.

## Critical nonclaims

Do not infer from Iteration 135 that:

- the model is a UV completion;
- the model is novel relative to known nonlocal/form-factor gravity;
- positive input spectral density alone proves dressed-propagator unitarity;
- the Newtonian limit has passed;
- beta is experimentally identifiable;
- quantum gravity has been detected or derived.

## Exact restart instruction

Resume with **Iteration 136 Lorentzian analytic-structure gate**. Do not change `rho_hat` or the sign domain after inspecting the result. First test the frozen model as written; if it fails, record the failure and create a new version/ansatz.
