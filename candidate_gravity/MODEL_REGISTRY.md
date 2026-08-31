# Candidate Gravity Model Registry

**Updated:** 2026-08-31

| Model ID | Version | Status | Parent | Core dynamics authority | Highest passed QG gate | Rejection/supersession authority |
|---|---|---|---|---|---|---|
| `ANSATZ-PQG-EFT-001` | 0.1 | REFERENCE / NOT PROMOTABLE | none | `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | QG-003 | QG-007 FAIL: `REFERENCE_DEGENERACY_C5`; `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md` |
| `ANSATZ-RQIR-CTP-001` | 0.1 | REJECTED | C5 boundary at `beta=0` | `candidate_gravity/models/ANSATZ-RQIR-CTP-001/MODEL.md` | QG-002; Euclidean scoped checks | QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`; `docs/CANDIDATE_GRAVITY_LORENTZIAN_ITERATION136.md` |
| `ANSATZ-RQIR-KL-002` | 0.1 | DRAFT / TESTING | new structural branch informed by CG-NG-004 | `candidate_gravity/models/ANSATZ-RQIR-KL-002/MODEL.md` | QG-002; QG-004 PASS_SCOPED; QG-003 PARTIAL | none; QG-005/QG-007 currently blocking promotion |

## Registry rules

- `ANSATZ-*` entries are pre-candidate constructions.
- `QGxxx` promotion requires QG-001 and QG-002 PASS plus absence of a disqualifying failed consistency/novelty gate.
- Rejected/reference/superseded models stay in the table permanently.
- Do not reuse a retired model ID for unrelated dynamics.
- A material change to dynamics/constraints/causal or renormalization structure increments the version or creates a new model ID according to the recovery guide.
- A failed frozen gate is not repaired by changing the tested parameter sign or functional form inside the same version after the result is known.

## Current interpretation

`ANSATZ-PQG-EFT-001` supplies the permanent C5 low-energy perturbative-QG control and cannot be relabeled as a novel candidate.

`ANSATZ-RQIR-CTP-001` v0.1 is the first rejected RQIR-driven model. Its Euclidean kernel was positive, but the Lorentzian continuation analytically forces exactly one additional below-threshold timelike zero for every `beta>0`, with opposite residue sign in the frozen spin-2 convention. This retained failure is `CG-NG-004`.

`ANSATZ-RQIR-KL-002` is the active discovery model. It moves the new physics from a multiplicative inverse-kernel deformation to a directly nonnegative Källén–Lehmann spectral continuum. This structurally removes the specific Iteration-136 isolated-pole failure at Gaussian two-point level. Its next high-value risks are complete tensor/helicity consistency (QG-005) and exact degeneracy with C4/C5/nonlocal/KK continuum models (QG-007).
