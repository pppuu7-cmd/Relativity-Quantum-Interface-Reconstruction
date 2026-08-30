# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 132**.

> Repository state, not chat history, is authoritative. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication / branch status

- **Paper I scientific scope:** CLOSED at Iteration 078 — 100% scientific.
- **Paper II scientific scope:** CLOSED at Iteration 079 — 100% scientific.
- **Paper III scientific scope:** CLOSED at Iteration 128 — 100% scientific; submission readiness 97%.
- **Candidate Gravity repository infrastructure:** **CLOSED/READY at Iteration 132 — 100% ready to instantiate the first real ansatz.**
- **Concrete Candidate Gravity model:** not yet instantiated; approximately 10% project bookkeeping only because the testing architecture exists but the dynamics do not.

## Mandatory recovery order

Read:

1. `docs/RECOVERY_GUIDE.md`;
2. `docs/MASTER_TABLE.md`;
3. this file;
4. `docs/READINESS_TRACKER.md`;
5. latest relevant recovery delta.

For Candidate Gravity additionally read:

- `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
- `candidate_gravity/recovery/RECOVERY_GUIDE.md`;
- `candidate_gravity/INFRASTRUCTURE_STATUS.yaml`;
- `candidate_gravity/NEW_MODEL_CHECKLIST.md`;
- `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`.

## Closed RQIR test pipeline

Future models are propagated through the frozen chain

`model dynamics -> J,N,chi^R,higher correlators -> Paper-I finite discriminator -> Paper-II F_beta|theta -> Paper-III physical resources`.

Detector inference uses exact hard-constraint reduction and

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Final-significance bookkeeping uses

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

Historical `A_raw=25, C_src=225` is only a raw-5-sigma/90%-retention regression; it gives final `Z=4.74341649`. For final `Z=5` at fixed 90% retention use `A_raw=27.77777778, C_src=250`, while joint science/source-metrology optimization is preferred.

Paper-III closure remains a framework/resource certificate, not a measured apparatus winner (NG-084).

## Candidate Gravity infrastructure — Iterations 129–132

### Iteration 129 — workspace and Model→RQIR contract

Created the canonical workspace and model specification/contract.

**CG-INFRA-001:** one model version must derive its RQIR-facing hierarchy from one declared dynamics/convention.

**CG-NG-001:** a phenomenological kernel/channel alone is not yet a gravity model.

Readiness: Candidate Gravity start 94%.

### Iteration 130 — gate governance and provenance

Added:

- machine-readable QG-001…QG-010 and cross-gate state;
- comparator registry;
- assumptions ledger;
- derivation provenance;
- structural workspace validator.

**CG-INFRA-002…005:** PASS requires evidence; comparator completeness bounds claim strength; assumptions and derivation provenance are first-class.

Readiness: 97%.

### Iteration 131 — recovery/versioning

Added:

- Candidate Gravity branch-local recovery/front;
- model registry;
- new-model boot checklist;
- synchronized entry criteria.

**CG-INFRA-006…008:** preserve negative results; recover from repo, not chat; start as `ANSATZ-*` before promotion to `QGxxx`.

Readiness: 99%.

### Iteration 132 — infrastructure closure

Canonical authorities:

- `analysis/candidate_gravity_readiness_closure_iteration132.py`;
- `candidate_gravity/INFRASTRUCTURE_STATUS.yaml`;
- `docs/CANDIDATE_GRAVITY_INFRASTRUCTURE_CLOSURE_ITERATION132.md`;
- `research_log/2026-08-31_iteration_132_candidate_gravity_infrastructure_closure.md`;
- `recovery/RECOVERY_DELTA_ITERATION_132.md`.

**CG-INFRA-009:** freeze the evaluation process before the first real model; changes require methodological provenance.

**CG-NG-002:** 100% repository readiness is not 100% theory readiness.

## Candidate Gravity promotion discipline

A new construction begins as `ANSATZ-*`.

Promotion to `QGxxx` requires at least QG-001 and QG-002 PASS with repository authorities and no unresolved foundational contradiction under the promotion rules.

A model is not called RQIR-discriminating until the model-specific discriminator, Paper-I survival and positive Paper-II profiled Fisher gates pass. It is not experimentally closed until QG-010 passes.

Comparator classes include classical GR/Newtonian, semiclassical, stochastic, classical-channel/hybrid/postquantum, conventional quantum/technical mediator, perturbative-QG and full-QFT-source/classical-interface alternatives as applicable.

## Immediate next scientific action

**The repository preparation task is complete.**

The next scientific step is to instantiate the first real construction as `ANSATZ-*` using `candidate_gravity/NEW_MODEL_CHECKLIST.md`.

Start with:

1. **QG-001 — physical state space**;
2. **QG-002 — matter–gravity dynamics**.

Do not optimize a detector discriminator before the model foundations, constraints and parameter domain are frozen.
