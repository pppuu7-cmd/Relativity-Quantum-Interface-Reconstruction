# RQIR Readiness Tracker

**Updated:** 2026-09-08

Percentages are project-management readiness estimates, not statistical confidence measures.

## Definitions

- **Paper III scientific:** completeness of the frozen Paper-III scientific/resource claim.
- **Paper III submission:** manuscript/figures/reviewer-style reproduction/journal packaging.
- **Candidate-Gravity repository start readiness:** whether the repository has a fixed, recoverable, evidence-gated process to instantiate and test a concrete model.
- **Concrete Candidate Gravity:** actual progress on a dynamical model; infrastructure alone does not advance the physics solution.

## History

| Iteration | Paper III scientific | Paper III submission | Repository ready to start Candidate Gravity | Concrete Candidate Gravity | Main reason |
|---|---:|---:|---:|---:|---|
| 116 | 89% | 70% | 84% | ~10% | Joint reference quota/no-double-counting theorem. |
| 117 | 90% | 71% | 84% | ~10% | Rank/span no-go. |
| 118 | 91% | 72% | 84% | ~10% | Exact 22D calibration span. |
| 119 | 92% | 73% | 84% | ~10% | Covariance matching-cover optimum. |
| 120 | 93% | 74% | 84% | ~10% | Strong/shared calibration bracket. |
| 121 | 94% | 75% | 84% | ~10% | Physical detector-rate `u` bracket. |
| 122 | 95% | 78% | 84% | ~10% | External apparatus feasibility/evidence audit. |
| 123 | 95% | 81% | 85% | ~10% | Claim/novelty boundary audit. |
| 124 | 96% | 86% | 85% | ~10% | Manuscript scientific skeleton. |
| 125 | 97% | 89% | 86% | ~10% | Canonical notation/dependency audit. |
| 126 | 98% | 93% | 86% | ~10% | Reproducibility manifest. |
| 127 | 99% | 96% | 87% | ~10% | Final priority audit. |
| 128 | **100%** | 97% | 90% | ~10% | Paper III scientific closure. |
| 129 | **100%** | 97% | 94% | ~10% | Candidate Gravity workspace + Model→RQIR contract. |
| 130 | **100%** | 97% | 97% | ~10% | Machine-readable gates, comparators, assumptions and derivation provenance. |
| 131 | **100%** | 97% | 99% | ~10% | Candidate Gravity recovery/versioning/model registry/boot protocol. |
| **132** | **100%** | **97%** | **100%** | **~10% / not instantiated** | **Final Candidate Gravity infrastructure closure before first real ansatz.** |

## Current status

### Paper III

- scientific scope: **CLOSED at Iteration 128 — 100%**;
- submission readiness: **97%**;
- primary submission target for the final hardening pass: **Quantum Science and Technology (QST)**;
- the remaining **3%** is explicitly reserved for QST-oriented submission hardening, not scientific-scope expansion;
- Paper III does **not** wait for Paper IV, Paper V, or Candidate Gravity completion;
- canonical QST completion gate: `docs/PAPER_III_QST_SUBMISSION_GATE.md`.

The 97% -> 100% promotion requires closure of the QST work package: concrete experimental architecture; resource-budget/assumption validation; publication-quality figures/tables; reviewer-style reproducibility binding; QST-specific claims/scope alignment; and the final journal-facing submission package.

Recording the QST strategy alone does **not** raise the submission-readiness value: it remains **97%** until all final gates PASS.

### Candidate Gravity repository infrastructure

**CLOSED/READY at Iteration 132 — 100% readiness to instantiate the first real ansatz.**

Canonical infrastructure includes:

- model specification template;
- single-dynamics Model→RQIR contract;
- QG-001…QG-010 + cross-gate state machine;
- baseline comparator registry;
- assumptions ledger;
- derivation provenance map;
- model registry/versioning;
- new-model boot checklist;
- branch-local recovery/front;
- structural closure audit;
- machine-readable `INFRASTRUCTURE_STATUS.yaml`.

**CG-NG-002:** 100% repository readiness is not 100% quantum-gravity theory readiness.

### Concrete Candidate Gravity

The historical infrastructure table above records the state at Iteration 132. For current model physics readiness, use `candidate_gravity/recovery/CURRENT_QG_FRONT.md` as the live authority rather than extrapolating from that table.

## Scope rules

- Paper III stays frozen under P3-CLOSE-001 absent a real contradiction/failed regression/materially relevant new literature.
- Paper III submission readiness is promoted from 97% to 100% only after all gates in `docs/PAPER_III_QST_SUBMISSION_GATE.md` pass.
- Candidate Gravity evaluation process is frozen under CG-INFRA-009 before the first model; changes require methodological provenance rather than candidate-dependent tuning.
- Failed/rejected model versions remain first-class results.
