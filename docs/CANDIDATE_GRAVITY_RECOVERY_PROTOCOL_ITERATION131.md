# RQIR Iteration 131 — Candidate Gravity Recovery / Versioning Protocol

**Date:** 2026-08-31  
**Scope:** repository infrastructure only; no concrete model and no new-physics claim.

## Result

Added a Candidate-Gravity-specific continuity layer:

- `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
- `candidate_gravity/recovery/RECOVERY_GUIDE.md`;
- `candidate_gravity/MODEL_REGISTRY.md`;
- `candidate_gravity/NEW_MODEL_CHECKLIST.md`.

The canonical entry criteria were also synchronized with the post-Iteration-128 state: Papers I–III are scientifically closed and are now fixed test stages for future model work.

## CG-INFRA-006 — immutable negative-result provenance

A failed gate, rejected ansatz or model version that underlies retained conclusions is never silently rewritten into a passing model. Material changes to dynamics/constraints/causal or renormalization structure create a new version/model identity.

## CG-INFRA-007 — branch-local recovery

Candidate Gravity has its own recovery pointer and read order, subordinate to repository-wide `recovery/CURRENT_FRONT.md`. A new chat can reconstruct active model state from repository files without using chat history as authority.

## CG-INFRA-008 — ansatz-before-candidate promotion

A new construction begins as `ANSATZ-*`. Promotion to `QGxxx` requires at least QG-001 and QG-002 PASS with repository evidence plus no unresolved foundational contradiction in the declared promotion rules.

## Readiness snapshot

- Paper III scientific-content readiness: **100%**.
- Paper III submission readiness: **97%**.
- Repository readiness to start Candidate Gravity: **99%**.
- Concrete Candidate Gravity model: **~10%**.

## Remaining blocker

Only a final infrastructure closure audit remains: verify canonical file presence/uniqueness, current-status consistency and a complete boot path from empty workspace to first `ANSATZ-*` without adding process conventions after seeing a preferred physical model.
