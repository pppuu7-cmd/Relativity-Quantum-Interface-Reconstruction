# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Reference model:** `ANSATZ-PQG-EFT-001` v0.1, REFERENCE / NOT PROMOTABLE  
**Active discovery model:** `ANSATZ-RQIR-CTP-001` v0.1, DRAFT / TESTING  
**Authoritative Candidate Gravity front:** **Iteration 135**

## Current branch state

- Papers I–III remain scientifically closed and form the fixed RQIR test pipeline.
- Candidate Gravity process/infrastructure closed at Iteration 132.
- Iteration 133 instantiated the conservative perturbative quantum-GR EFT reference/control.
- Iteration 134 passed that reference model's Newtonian/classical-GR normalization gate.
- Iteration 135 instantiated the first RQIR-driven non-reference ansatz with a linked causal response/noise spectral kernel and recorded the first scoped Euclidean stability result.

## Reference branch retained result

For `ANSATZ-PQG-EFT-001`:

- QG-001/QG-002/QG-003 PASS;
- QG-007 FAIL due exact comparator C5 theory-class identity;
- it remains a permanent reference/control and cannot be promoted without changing the model class.

Retained negative result **CG-NG-003**: quantizing the weak-field metric within standard perturbative quantum-GR EFT does not itself create a new Candidate Gravity discriminator against C5.

## Active discovery ansatz

`ANSATZ-RQIR-CTP-001` v0.1 uses

`rho_hat(s)=exp(1-s)Theta(s-1)`,

`zeta=-(p^2+i0 p^0)/M_*^2`,

`F_R=zeta int_1^infty ds rho_hat(s)/(s+zeta)`,

`K_R^(2)=K_GR,R^(2)[1+beta F_R]`, `beta>=0`.

The same spectral object fixes the dispersive/absorptive response and the v0.1 Gaussian quantum-noise relation. Response and noise may not be tuned independently.

## Iteration 135 scoped result

For spacelike `x=-p^2/M_*^2>=0`,

`F_E=x exp(1+x)E1(1+x)`

and positivity/normalization of the spectral density gives

`0<=F_E<=x/(1+x)<1`.

Therefore

`1+beta F_E>=1`

for `beta>=0`: no additional Euclidean/spacelike zero of the multiplicative spin-2 kernel.

IR coefficient:

`F_E=0.596347362323... x+O(x^2)`.

This is a **PASS_SCOPED**, not a Lorentzian ghost-freedom theorem.

## Active model gate state

For `ANSATZ-RQIR-CTP-001`:

- QG-001 PARTIAL — effective linearized state structure specified; microscopic physical-state/dilation closure open;
- QG-002 PASS scoped — one CTP effective dynamics fixes response and linked noise;
- QG-003 NOT_TESTED — full Newtonian source normalization open;
- QG-004 BLOCKED — Lorentzian unitarity/positivity and microscopic dilation open;
- QG-005 PARTIAL — transverse linear spin-2 Ward structure only;
- QG-006 NOT_TESTED;
- QG-007 BLOCKED — prior-art/comparator distinction unresolved;
- QG-008 NOT_TESTED;
- QG-009/QG-010 BLOCKED until a nondegenerate beta direction survives earlier gates.

## Comparator status that must not be forgotten

The deep-infrared expansion is expected to be degenerate with ordinary higher-dimension gravitational EFT coefficients to finite order. Existing nonlocal/form-factor quantum-gravity constructions also occupy nearby structural territory. Therefore Iteration 135 is a model-construction advance, **not a novelty claim**.

## Canonical authorities

Read in this order:

1. `candidate_gravity/models/ANSATZ-RQIR-CTP-001/MODEL.md`;
2. `candidate_gravity/models/ANSATZ-RQIR-CTP-001/GATE_STATUS.yaml`;
3. `candidate_gravity/models/ANSATZ-RQIR-CTP-001/ASSUMPTIONS_LEDGER.md`;
4. `candidate_gravity/models/ANSATZ-RQIR-CTP-001/DERIVATION_MAP.md`;
5. `candidate_gravity/models/ANSATZ-RQIR-CTP-001/COMPARATOR_STATUS.md`;
6. `analysis/candidate_gravity_rqir_ctp_iteration135.py`;
7. `results/candidate_gravity_rqir_ctp_iteration135.json`;
8. `docs/CANDIDATE_GRAVITY_RQIR_CTP_ITERATION135.md`;
9. `research_log/2026-08-31_iteration_135_rqir_ctp_candidate_start.md`;
10. `recovery/RECOVERY_DELTA_ITERATION_135.md`.

The C5 reference branch remains authoritative for comparator boundary checks.

## Immediate next scientific priority

**Iteration 136: Lorentzian analytic-structure gate.**

Before any detector optimization:

1. analytically continue the frozen `F_R` across the timelike threshold `p^2>=M_*^2`;
2. compute its discontinuity and absorptive sign;
3. search the physical sheet for zeros of `1+beta F_R` over a frozen parameter box;
4. determine whether the dressed propagator admits a positive spectral/causal interpretation;
5. restore the complete conserved-source tensor structure;
6. explicitly compare the result to C5 and known nonlocal/form-factor gravity.

Do not change the spectral shape after inspecting this gate. Failure is recorded and used to design a new version rather than post-hoc tuning.
