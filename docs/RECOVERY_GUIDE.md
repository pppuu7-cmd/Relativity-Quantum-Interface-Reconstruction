# RQIR Recovery Guide

**Last updated:** 2026-08-31  
**Current operational framework:** v3.1 / authoritative front Iteration 132

This is the repository continuity backbone. Repository state, not chat history, is authoritative. RQIR remains separate from RTK/DSIR. No toy/resource/detector result is itself an empirical new-physics claim.

## 1. Mandatory recovery order

For any RQIR continuation read:

1. `docs/MASTER_TABLE.md`;
2. `recovery/CURRENT_FRONT.md`;
3. `docs/READINESS_TRACKER.md`;
4. latest `recovery/RECOVERY_DELTA_ITERATION_*.md` relevant to the active branch;
5. the canonical documents/scripts named by that front.

For Candidate Gravity additionally read:

1. `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
2. `candidate_gravity/recovery/RECOVERY_GUIDE.md`;
3. `candidate_gravity/INFRASTRUCTURE_STATUS.yaml`;
4. `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
5. active model files if a model exists.

## 2. Publication/scientific state

- Paper I scientific scope: **CLOSED**, Iteration 078.
- Paper II scientific scope: **CLOSED**, Iteration 079.
- Paper III scientific scope: **CLOSED**, Iteration 128.
- Candidate Gravity repository infrastructure: **READY at 100%**, Iteration 132.
- Concrete Candidate Gravity model: not yet instantiated; no model-specific QG-001…QG-010 gate is passed.

Paper III closure is a resource/design/certificate closure, not an experimental detection or measured Toy009/Toy014 winner.

## 3. Mandatory inference backbone

Use exact hard-constraint reduction and detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain centered covariance derivatives, source-amplitude metrology, detector transfer/noise, controls, backaction, wall-clock rates and comparator/model degeneracy in one consistent parameter coordinate.

Canonical final-significance convention:

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

Historical `A_raw=25, C_src=225` is only a raw-5-sigma / 90%-retention regression. It gives `F_final=22.5`, not final 5 sigma. For final `Z=5` at fixed 90% retention use `A_raw=27.77777778`, `C_src=250`; preferred design jointly optimizes science and source-metrology time.

## 4. Mature Paper-I/II/III authority

Do not restart closed tasks merely because an old chat or historical document predates their closure.

Key authorities:

- `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`;
- `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`;
- `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`;
- `docs/PAPER_III_REPRODUCIBILITY_MANIFEST_ITERATION126.md`;
- `docs/PAPER_III_FINAL_PRIORITY_AUDIT_ITERATION127.md`.

Retain all named NUM/NG/CAL/RESOURCE/DESIGN corrections referenced by `recovery/CURRENT_FRONT.md` and the closure documents.

## 5. Candidate Gravity entry discipline

A future construction starts as `ANSATZ-*`, not `QGxxx`.

Use:

- `candidate_gravity/MODEL_SPEC_TEMPLATE.md`;
- `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`;
- `candidate_gravity/BASELINE_COMPARATORS.md`;
- `candidate_gravity/ASSUMPTIONS_LEDGER_TEMPLATE.md`;
- `candidate_gravity/DERIVATION_MAP_TEMPLATE.md`;
- `candidate_gravity/NEW_MODEL_CHECKLIST.md`.

The same declared model dynamics must derive the source hierarchy and RQIR-facing response. Do not independently tune `J`, `N`, `chi^R`, higher correlators or detector-facing kernels to create a desired discriminator.

## 6. Candidate Gravity mandatory gates

QG-001…QG-010 cover:

1. physical state space;
2. matter-gravity dynamics;
3. controlled Newtonian/GR limit;
4. unitarity/positivity/CP;
5. gauge/constraint consistency;
6. ordinary-QM/semiclassical limits;
7. first model-specific discriminator;
8. Paper-I finite discriminator;
9. Paper-II nuisance-profiled identifiability;
10. Paper-III physical-resource/measurability closure.

Cross-gates include conservation/Bianchi/Ward, causality, positivity/spectral structure, flat-QFT limit, EFT power counting, stress-energy renormalization, comparator degeneracy and detector measurability.

Allowed states are `PASS`, `FAIL`, `BLOCKED`, `NOT_TESTED`, `NOT_APPLICABLE`. PASS requires repository evidence. FAIL is preserved.

## 7. Comparator discipline

A future model is tested against all applicable classes in `candidate_gravity/BASELINE_COMPARATORS.md`, including classical GR/Newtonian, semiclassical, stochastic, classical-channel/hybrid/postquantum, conventional quantum/technical mediators, perturbative quantum gravity and full-QFT-source/classical-interface alternatives.

The weakest unresolved comparator bounds claim strength.

## 8. Recovery/versioning discipline

Material changes to state space, dynamics, constraints, coupling, causal prescription, EFT/UV content or renormalization scheme create a new model version.

Negative results are first-class:

- failed consistency gates;
- exact comparator degeneracies;
- zero profiled Fisher;
- unavailable/divergent resource requirements;
- rejected ansätze.

Do not silently overwrite them.

## 9. Cross-project guard

RTK and DSIR results do not enter RQIR/Candidate Gravity merely because terminology overlaps. They require independent derivation under the RQIR model contract.

## 10. Immediate next action

Repository process readiness for Candidate Gravity is complete. The next scientific action is to instantiate the first real `ANSATZ-*` and work on QG-001/QG-002 before optimizing detector discriminants.
