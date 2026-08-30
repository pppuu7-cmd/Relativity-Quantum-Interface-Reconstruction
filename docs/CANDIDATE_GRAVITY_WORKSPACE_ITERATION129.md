# RQIR Iteration 129 — Candidate Gravity Workspace and Model→RQIR Contract

**Date:** 2026-08-31  
**Scope:** repository infrastructure only; no concrete gravity model and no new-physics claim.

## Result

Created the canonical `candidate_gravity/` workspace and two mandatory model-entry authorities:

- `candidate_gravity/MODEL_SPEC_TEMPLATE.md`;
- `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`.

The model specification requires one coherent physical state space, dynamics, gauge/constraint structure, validity domain, consistency conditions, limits, source hierarchy, discriminator and rejection conditions.

The Model→RQIR contract requires one dynamical model to derive, in one parameter convention, the source hierarchy and the objects needed by closed Papers I–III.

### CG-INFRA-001 — single-dynamics contract

A Candidate Gravity model may not independently tune `J`, `N`, `chi^R`, higher correlators or detector-facing kernels to improve an RQIR discriminator. Claimed model-core observables must descend from the same declared dynamics, with ordering, smearing, causal prescription, gauge status and approximation order stated.

### CG-NG-001 — phenomenological kernel is not yet a gravity model

A useful CTP kernel, modified response function or quantum channel is not by itself a Candidate Gravity model unless the underlying state space/dynamics/constraints and required limits are supplied.

## Readiness snapshot

- Paper III scientific-content readiness: **100%** (frozen/closed).
- Paper III submission readiness: **97%**.
- Repository readiness to start a concrete Candidate Gravity model: **94%**.
- Concrete Candidate Gravity model: **~10%** (no new dynamics constructed in this iteration).

## Next gate

Add machine-readable QG gate state, comparator registry, assumptions ledger and derivation provenance so model promotion cannot occur by prose assertion alone.
