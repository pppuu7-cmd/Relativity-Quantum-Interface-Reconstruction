# Candidate Gravity Model Registry

**Updated:** 2026-08-31

| Model ID | Version | Status | Parent | Core dynamics authority | Highest meaningful gate state | Rejection/supersession authority |
|---|---|---|---|---|---|---|
| `ANSATZ-PQG-EFT-001` | 0.1 | REFERENCE / NOT PROMOTABLE | none | `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | QG-003 PASS; QG-007 FAIL novelty | `REFERENCE_DEGENERACY_C5`; `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md` |
| `ANSATZ-RQIR-CTP-001` | 0.1 | REJECTED | C5 boundary at `beta=0` | `candidate_gravity/models/ANSATZ-RQIR-CTP-001/MODEL.md` | QG-004 FAIL consistency | `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`; `docs/CANDIDATE_GRAVITY_LORENTZIAN_ITERATION136.md` |
| `ANSATZ-RQIR-KL-002` | 0.1 | DRAFT / TESTING | new structural branch informed by CG-NG-004 | `candidate_gravity/models/ANSATZ-RQIR-KL-002/MODEL.md` | QG-004 PASS_SCOPED; QG-005 PARTIAL; QG-007 PARTIAL_NEGATIVE | none; deep-IR distinctness is excluded by CG-NG-005 |

## Registry rules

- `ANSATZ-*` entries are pre-candidate constructions.
- `QGxxx` promotion requires QG-001 and QG-002 PASS plus absence of a disqualifying failed consistency/novelty gate.
- Rejected/reference/superseded models stay in the table permanently.
- Do not reuse a retired model ID for unrelated dynamics.
- A material change to dynamics/constraints/causal or renormalization structure increments the version or creates a new model ID.
- A failed frozen gate is not repaired by changing the tested parameter sign or functional form inside the same version after the result is known.
- Comparator degeneracy may remove only a regime rather than reject the whole model; the allowed discovery domain must then be narrowed explicitly.

## Current interpretation

### `ANSATZ-PQG-EFT-001`

Permanent C5 control. It demonstrates that a perfectly viable low-energy quantum-gravity model can fail **promotion as novel** because theory-class identity is exact.

### `ANSATZ-RQIR-CTP-001` v0.1

Permanent rejected negative-control. Its Euclidean kernel passed a scoped no-zero test, but Lorentzian continuation analytically forces one below-threshold timelike zero for every frozen `beta>0`, with opposite residue sign in the declared convention. This is retained result `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1

Active discovery model. It uses a nonnegative massless-plus-continuum spectral measure and now has an explicit linear conserved-source tensor completion. Scoped results include positive spectral weight, retarded support, no isolated added pole, the standard massive-spin-2 `4/3` NR tensor factor, and a linked `3/4` traceless-vs-NR calibration relation.

Iteration 140 removes the strictly below-threshold finite-order EFT regime from the discovery domain: the gapped continuum has a convergent analytic derivative expansion there and is absorbed into C5 Wilson-coefficient freedom at any fixed finite order. Retained result `CG-NG-005`.

The active discovery domain is therefore **threshold-resolved and/or cross-channel**, not deep IR.

## Next promotion requirement

Before any `QG001` label, the active branch must:

1. freeze an explicit C5 loop/nonanalytic baseline so `beta=0` is the declared perturbative-QG reference at the same order;
2. survive comparison with C4 hidden/KK/continuum spin-2 mediators and nonlocal/form-factor gravity;
3. supply a nonlinear or otherwise complete constraint/gauge interpretation adequate for the claimed regime;
4. exhibit a finite Paper-I direction outside the exact calibration/comparator span;
5. retain nonzero profiled Fisher and finite physical resources.
