# RQIR Recovery Delta — Iteration 134

**Date:** 2026-08-31

## Previous authority

Iteration 132 closed Candidate Gravity infrastructure at 100% readiness with no active model.

## New branch object

Created `candidate_gravity/models/ANSATZ-PQG-EFT-001/` as the first real model object. It is a deliberate low-energy perturbative quantum-GR EFT reference/control, not a novelty claim.

Canonical files:

- `MODEL.md`;
- `GATE_STATUS.yaml`;
- `ASSUMPTIONS_LEDGER.md`;
- `DERIVATION_MAP.md`.

## Gate changes

- QG-001: PASS.
- QG-002: PASS.
- QG-003: PASS after Iteration-134 Newtonian/classical-GR normalization audit.
- QG-007: FAIL with `REFERENCE_DEGENERACY_C5`.
- QG-004/QG-006: NOT_TESTED.
- QG-005: BLOCKED pending relational/gauge-invariant RQIR observable audit.
- QG-008/QG-009/QG-010: BLOCKED because there is no independent C5-distinguishing beta direction.

## New negative result

**CG-NG-003:** standard perturbative quantum-GR EFT is exactly the C5 comparator class for this purpose. It cannot be promoted as a novel Candidate Gravity merely by presenting a quantized metric/graviton mediator. Detector Fisher/resource optimization cannot break an exact theory-class identity.

## Exact normalization regression

For signature `(-,+,+,+)`, `g00=-(1+2Phi)` and `kappa^2=32 pi G`:

`2 nabla^2 Phi = 8 pi G rho -> nabla^2 Phi=4 pi G rho`.

Point source: `Phi=-GM/r`.

Script: `analysis/candidate_gravity_newtonian_limit_iteration134.py`.

## Recovery instruction

On continuation read repository-wide `recovery/CURRENT_FRONT.md`, then `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, then this delta and the four model files.

Do not revert to the old post-Toy010 resource task; Paper III already closed that chain.

## Next priority

Highest-value discovery work is a genuinely distinct `ANSATZ-*` whose dynamics differ from C5/C1/C2/C3 before detector optimization. The PQG-EFT branch remains a reference/control and may be deepened through QG-004/QG-005/QG-006 only for consistency-pipeline validation.
