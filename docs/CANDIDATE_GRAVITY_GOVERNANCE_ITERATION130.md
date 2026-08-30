# RQIR Iteration 130 — Candidate Gravity Gate Governance and Provenance

**Date:** 2026-08-31  
**Scope:** repository infrastructure; no concrete model and no new-physics claim.

## Result

Added four mandatory governance artifacts for every future model:

- machine-readable `GATE_STATUS_TEMPLATE.yaml`;
- `BASELINE_COMPARATORS.md`;
- `ASSUMPTIONS_LEDGER_TEMPLATE.md`;
- `DERIVATION_MAP_TEMPLATE.md`.

Also added `analysis/candidate_gravity_workspace_validator_iteration130.py`, which checks the canonical infrastructure and uniqueness of QG-001…QG-010 labels. The validator checks structure only; it cannot certify physical truth.

## CG-INFRA-002 — evidence-backed gate state

Every QG gate uses one of

`PASS / FAIL / BLOCKED / NOT_TESTED / NOT_APPLICABLE`.

`PASS` requires a repository authority. A prose assertion or chat conclusion is insufficient.

`FAIL` is a retained scientific result. Repairing a failed model requires a new model version rather than silently resetting history.

## CG-INFRA-003 — comparator completeness

A model-specific discriminator must state its status against every applicable comparator class C0–C6. The weakest unresolved comparator bounds the strength of the physics claim.

In particular, distinction from one semiclassical-mean model is not by itself evidence for quantum gravity if stochastic/hybrid/full-QFT alternatives remain degenerate.

## CG-INFRA-004 — assumptions are first-class dependencies

Every non-derived structural, perturbative, renormalization, gauge, detector or numerical assumption that can alter a claim is entered in the assumptions ledger with sensitivity/failure consequence.

## CG-INFRA-005 — derivation provenance

Every model claim is traceable through

`dynamics -> source hierarchy -> RQIR discriminator -> detector Fisher -> resources`

with approximation order, code/test authority and comparator status.

## Readiness snapshot

- Paper III scientific-content readiness: **100%**.
- Paper III submission readiness: **97%**.
- Repository readiness to start Candidate Gravity: **97%**.
- Concrete Candidate Gravity model: **~10%**.

## Remaining infrastructure blockers

1. Candidate-Gravity-specific recovery/front/versioning protocol;
2. stale pre-128 entry/recovery wording must be superseded;
3. final entry-readiness audit must verify that a new model can be created without inventing missing process conventions.
