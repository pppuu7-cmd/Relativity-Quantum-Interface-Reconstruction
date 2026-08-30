# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** **READY — 100% repository readiness to instantiate first ansatz**  
**Active concrete model:** NONE

## Authority rule

This file is authoritative for Candidate Gravity branch state; repository-wide authority remains `recovery/CURRENT_FRONT.md`. Chat history is never authority over repository state.

## Current branch state

- Papers I–III are scientifically closed and form the fixed RQIR test pipeline.
- Candidate Gravity process/infrastructure is closed at Iteration 132.
- No concrete Candidate Gravity model has yet been created or passed any QG gate.
- The next construction must begin as `ANSATZ-*` using `candidate_gravity/NEW_MODEL_CHECKLIST.md`.
- Promotion to `QGxxx` follows `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`.

## Canonical infrastructure

Read:

1. `candidate_gravity/README.md`;
2. `candidate_gravity/MODEL_SPEC_TEMPLATE.md`;
3. `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
4. `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`;
5. `candidate_gravity/BASELINE_COMPARATORS.md`;
6. `candidate_gravity/ASSUMPTIONS_LEDGER_TEMPLATE.md`;
7. `candidate_gravity/DERIVATION_MAP_TEMPLATE.md`;
8. `candidate_gravity/MODEL_REGISTRY.md`;
9. `candidate_gravity/NEW_MODEL_CHECKLIST.md`;
10. `candidate_gravity/recovery/RECOVERY_GUIDE.md`;
11. `candidate_gravity/INFRASTRUCTURE_STATUS.yaml`.

## Recovery order once a model exists

After the repository-wide front and the files above, read the active model in this order:

`MODEL.md -> GATE_STATUS.yaml -> ASSUMPTIONS_LEDGER.md -> DERIVATION_MAP.md -> COMPARATOR_STATUS.md -> latest model log/delta -> referenced tests`.

## Immutable provenance rules

- `FAIL` is retained.
- `BLOCKED` is not provisional PASS.
- material changes to dynamics/constraints/causal/renormalization structure create a new model version;
- rejected/superseded models remain in `MODEL_REGISTRY.md`;
- RTK/DSIR material does not transfer without independent RQIR rederivation.

## Next admissible action

Instantiate the first real construction as `ANSATZ-*`. The first scientific target is QG-001/QG-002: freeze a coherent physical state space and dynamics before optimizing any RQIR discriminator.
