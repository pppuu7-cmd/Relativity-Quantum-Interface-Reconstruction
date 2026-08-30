# Candidate Gravity Model Registry

**Updated:** 2026-08-31

| Model ID | Version | Status | Parent | Core dynamics authority | Highest passed QG gate | Rejection/supersession authority |
|---|---|---|---|---|---|---|
| `ANSATZ-PQG-EFT-001` | 0.1 | REFERENCE / NOT PROMOTABLE | none | `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | QG-003 | QG-007 FAIL: `REFERENCE_DEGENERACY_C5`; `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md` |

## Registry rules

- `ANSATZ-*` entries are pre-candidate constructions.
- `QGxxx` promotion requires QG-001 and QG-002 PASS plus absence of a disqualifying failed novelty/comparator gate.
- Rejected/reference/superseded models stay in the table.
- Do not reuse a retired model ID for unrelated dynamics.
- A material change to dynamics/constraints/causal or renormalization structure increments the version or creates a new model ID according to the recovery guide.

## Current interpretation

`ANSATZ-PQG-EFT-001` validates the gate machinery and supplies the C5 perturbative-QG reference. It must not be relabeled `QG001`: its exact comparator identity is a retained negative result (CG-NG-003).
