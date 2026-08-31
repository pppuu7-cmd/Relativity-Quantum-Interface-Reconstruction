# Candidate Gravity Model Registry

**Updated:** 2026-08-31

| Model ID | Version | Status | Parent | Core dynamics authority | Highest meaningful gate state | Rejection/supersession authority |
|---|---|---|---|---|---|---|
| `ANSATZ-PQG-EFT-001` | 0.1 | REFERENCE / NOT PROMOTABLE | none | `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | QG-003 PASS; QG-007 FAIL novelty | `REFERENCE_DEGENERACY_C5` |
| `ANSATZ-RQIR-CTP-001` | 0.1 | REJECTED | C5 boundary at `beta=0` | `candidate_gravity/models/ANSATZ-RQIR-CTP-001/MODEL.md` | QG-004 FAIL consistency | `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE` |
| `ANSATZ-RQIR-KL-002` | 0.1 | REFERENCE / NOT PROMOTABLE | structural branch informed by CG-NG-004 | `candidate_gravity/models/ANSATZ-RQIR-KL-002/MODEL.md` | QG-004 PASS_SCOPED; QG-007 FAIL novelty | `EXACT_GAUSSIAN_C4_KK_DEGENERACY`; `docs/CANDIDATE_GRAVITY_C4_GAUSSIAN_DEGENERACY_ITERATION141.md` |

## Registry rules

- `ANSATZ-*` entries are pre-candidate constructions.
- `QGxxx` promotion requires QG-001 and QG-002 PASS plus absence of disqualifying consistency or comparator failures.
- Rejected/reference/superseded models remain permanently registered.
- Do not reuse a retired model ID for unrelated dynamics.
- Material changes to dynamics/constraints/causal or renormalization structure create a new version/model ID.
- A failed frozen gate is not repaired post hoc inside the same version.
- Exact comparator identity cannot be repaired by detector sensitivity, Fisher profiling or resources.

## Retained lessons

### C5 reference

`CG-NG-003`: standard perturbative quantum GR is viable but cannot be promoted as novel relative to comparator C5.

### First RQIR-driven ansatz

`CG-NG-004`: Euclidean-safe positive-beta spectral inverse-kernel deformation can be Lorentzian-inconsistent because it forces a below-threshold opposite-residue pole.

### Second RQIR-driven ansatz

`CG-NG-005`: a gapped positive continuum is finite-order C5-EFT-degenerate strictly below threshold.

`CG-NG-006`: a positive KL spin-2 continuum with only linear conserved-stress coupling is exactly equivalent at Gaussian RQIR level to an ordinary positive-norm mediator continuum/tower, so it cannot establish gravity-specific novelty.

## Current discovery state

There is **no active promotable ansatz after Iteration 141**. This is intentional: the next model must not be another propagator-only Gaussian modification.

The next architecture must contain a derived nonlinear/non-Gaussian gravitational relation and should be designed only after auditing strong existing nonlinear/nonlocal quantum-gravity comparators.
