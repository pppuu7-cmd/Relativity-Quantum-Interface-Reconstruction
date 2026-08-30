# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 134**.

> Repository state, not chat history, is authoritative. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication / branch status

- **Paper I scientific scope:** CLOSED at Iteration 078 — 100% scientific.
- **Paper II scientific scope:** CLOSED at Iteration 079 — 100% scientific.
- **Paper III scientific scope:** CLOSED at Iteration 128 — 100% scientific; submission readiness 97%.
- **Candidate Gravity infrastructure:** CLOSED/READY at Iteration 132 — 100% repository readiness.
- **Candidate Gravity reference model:** `ANSATZ-PQG-EFT-001` v0.1 instantiated at Iteration 133; QG-001/QG-002 PASS, QG-007 FAIL by exact C5 comparator identity.
- **Iteration 134:** QG-003 PASS for the reference branch via explicit Newtonian/classical-GR normalization audit.

## Mandatory inference/resource backbone

Detector inference remains

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Paper III already closed the old post-Toy010 task of converting abstract source/calibration Fisher parameters into accepted repetitions, shot/Fisher rates, calibration time, source preparation/metrology, coherence/reset, detector PSD/SNR, controls/backaction and wall-clock resources. Do not restart that task unless a contradiction is found.

## Candidate Gravity Iterations 133–134

### Iteration 133 — first real reference ansatz

Created `candidate_gravity/models/ANSATZ-PQG-EFT-001/`, a standard low-energy perturbative quantum-GR EFT with minimally coupled scalar matter.

One dynamics supplies the RQIR source hierarchy: `J=<T>`, centered `N`, retarded `chi^R`, and higher CTP/SK stress correlators.

Gate state:

- QG-001 PASS;
- QG-002 PASS;
- QG-007 FAIL.

**CG-NG-003:** the standard perturbative quantum-GR EFT branch is exactly comparator C5 at theory-class level. A quantized metric/graviton mediator is not, by itself, a novel Candidate Gravity. No detector optimization can create a C5-distinguishing beta direction when the model classes are identical.

### Iteration 134 — Newtonian/classical-GR gate

With `kappa^2=32 pi G`, signature `(-,+,+,+)` and `g00=-(1+2Phi)`, the static weak-field 00 Einstein equation gives

`2 nabla^2 Phi = 8 pi G rho`, hence `nabla^2 Phi=4 pi G rho` and `Phi=-GM/r` for a point source.

QG-003 = PASS for the declared low-energy reference domain. This validates convention/normalization only and does not repair QG-007.

Canonical files:

- `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md`;
- `docs/CANDIDATE_GRAVITY_NEWTONIAN_LIMIT_ITERATION134.md`;
- `analysis/candidate_gravity_reference_ansatz_iteration133.py`;
- `analysis/candidate_gravity_newtonian_limit_iteration134.py`;
- `research_log/2026-08-31_iteration_134_reference_ansatz_newtonian_gate.md`;
- `recovery/RECOVERY_DELTA_ITERATION_134.md`.

## Immediate next scientific priority

The highest-value next step is a genuinely distinct `ANSATZ-*` whose dynamics differ from the admitted C1/C2/C3/C5 comparator classes **before** any detector/Fisher optimization. The perturbative-QG reference may separately be deepened through QG-004/QG-005/QG-006 as a validation control, but it cannot be promoted to `QGxxx` while CG-NG-003 holds.
