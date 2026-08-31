# Candidate Gravity Model Registry

**Updated:** 2026-08-31

| Model ID | Version | Status | Parent | Core dynamics authority | Highest passed QG gate | Rejection/supersession authority |
|---|---|---|---|---|---|---|
| `ANSATZ-PQG-EFT-001` | 0.1 | REFERENCE / NOT PROMOTABLE | none | `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | QG-003 | QG-007 FAIL: `REFERENCE_DEGENERACY_C5`; `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md` |
| `ANSATZ-RQIR-CTP-001` | 0.1 | DRAFT / TESTING | `ANSATZ-PQG-EFT-001` boundary at `beta=0` | `candidate_gravity/models/ANSATZ-RQIR-CTP-001/MODEL.md` | QG-002 (scoped CTP dynamics); QG-001 partial | none; QG-007 currently BLOCKED pending comparator/prior-art audit |

## Registry rules

- `ANSATZ-*` entries are pre-candidate constructions.
- `QGxxx` promotion requires QG-001 and QG-002 PASS plus absence of a disqualifying failed novelty/comparator gate.
- Rejected/reference/superseded models stay in the table.
- Do not reuse a retired model ID for unrelated dynamics.
- A material change to dynamics/constraints/causal or renormalization structure increments the version or creates a new model ID according to the recovery guide.

## Current interpretation

`ANSATZ-PQG-EFT-001` validates the gate machinery and supplies the C5 perturbative-QG reference. It must not be relabeled `QG001`: its exact comparator identity is a retained negative result (CG-NG-003).

`ANSATZ-RQIR-CTP-001` is the first RQIR-driven deformation branch. It ties dispersive response and Gaussian quantum noise to one positive spectral kernel and introduces the explicit candidate direction `beta`, with `beta=0` returning to the C5 reference boundary. Iteration 135 established only a scoped Euclidean no-extra-zero/IR-decoupling result. The model is not promotable until Lorentzian consistency, full gauge/relational structure, limits, and comparator distinction are closed.
