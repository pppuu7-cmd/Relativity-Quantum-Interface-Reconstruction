# RQIR Candidate Gravity — Recovery Delta Iteration 532

Date: 2026-09-07

## Authority advanced
Iteration 532 prospectively fixes the complete 12-coordinate successor order for the frozen Iteration-424 quarter-step support before the active rank1 result is known.

Frozen order after exact HALF-overlap removal:
1 `(-2.5e-6,-1.25e-6)`
2 `(-2.5e-6,+1.25e-6)`
3 `(-1.25e-6,-2.5e-6)`
4 `(-1.25e-6,-1.25e-6)`
5 `(-1.25e-6,+1.25e-6)`
6 `(-1.25e-6,+2.5e-6)`
7 `(+1.25e-6,-2.5e-6)`
8 `(+1.25e-6,-1.25e-6)`
9 `(+1.25e-6,+1.25e-6)`
10 `(+1.25e-6,+2.5e-6)`
11 `(+2.5e-6,-1.25e-6)`
12 `(+2.5e-6,+1.25e-6)`.

Classification: `PASS_ITER424_QUARTER_SUCCESSOR_ORDER_PREREGISTERED_EXACT__NON_PROMOTING`.
Machine-readable authority: `candidate_gravity/results/iteration532_iter424_quarter_successor_order_exact_preregistration_audit.json`.

## Transition rule
A raw-consumed PASS permits exactly the next rank; rank12 PASS permits quarter assembly. Scientific block/fail stops rank advancement and requires localization under unchanged thresholds/conventions. Operational failure permits only minimal infrastructure/software repair followed by the same frozen rank. Result-dependent reorder/skip, unsupported u-v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Active computation
Unique active heavy prerequisite remains repaired quarter-rank1 run `34094463024`, job `101654832475`. Last live inspection: stages 1–4 complete, stage 5 full-z MP active, raw audit and artifact upload pending. Stage-level task completion approximately `57.1%`; no reliable within-stage percentage is exposed. No duplicate heavy Action launched.

## Authority ledger
Physical/operator authority: Iteration 411.
Physical blocker: Iteration 421, unresolved set `[2]`.
BASE/HALF support: Iteration 523, `32/32`.
BASE/HALF assembly: Iteration 527.
Quarter support manifest: Iteration 529.
Three-level Gram rank: Iteration 530.
Normalized three-level conditioning: Iteration 531.
Quarter successor-order preregistration: Iteration 532.
Latest authoritative research iteration: Iteration 532.

MODEL_READINESS: 24%
ITERATION_TASK_COMPLETION: 100%

Readiness change: 0 percentage points.

## Exact next gate
Raw-consume run `34094463024` after it becomes terminal. Only raw-valid rank1 PASS permits prospectively fixed rank2 `(-2.5e-6,+1.25e-6)`.
