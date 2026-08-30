# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** PRE-MODEL READYING  
**Active concrete model:** NONE

## Authority rule

This file is authoritative only for the Candidate Gravity branch. Repository-wide RQIR authority remains `recovery/CURRENT_FRONT.md`.

Chat history is never authority over repository files.

## Current branch state

- Papers I–III are scientifically closed and serve as the fixed reconstruction/identifiability/resource test pipeline.
- No concrete Candidate Gravity model has been admitted yet.
- The next concrete model must begin as `ANSATZ-*` until QG-001 and QG-002 are passed with repository evidence.
- Promotion to `QGxxx` follows `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`.

## Recovery order for Candidate Gravity work

1. `recovery/CURRENT_FRONT.md`;
2. `docs/MASTER_TABLE.md`;
3. `docs/READINESS_TRACKER.md`;
4. this file;
5. `candidate_gravity/README.md`;
6. `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
7. active model `MODEL.md`;
8. active model `GATE_STATUS.yaml`;
9. active model `ASSUMPTIONS_LEDGER.md`;
10. active model `DERIVATION_MAP.md`;
11. latest Candidate Gravity research log/recovery delta.

## Model versioning rule

A model version is immutable as a scientific provenance point once a gate is marked `FAIL` or a published/retained numerical result depends on it.

A material change to dynamics, constraints, state space, coupling structure, causal prescription or renormalization convention creates a new model version.

Parameter scans inside an unchanged declared model may remain the same version if the governing equations and approximation order are unchanged.

## Negative-result rule

- `FAIL` is preserved.
- `BLOCKED` is not treated as provisional PASS.
- a rejected ansatz remains in the model registry with rejection authority;
- a replacement receives a new version/model ID rather than rewriting history.

## Next admissible action

Complete repository infrastructure closure. Only after readiness reaches 100% may the first actual ansatz be instantiated from the templates.
