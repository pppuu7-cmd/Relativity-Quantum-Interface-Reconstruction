# RQIR Candidate Gravity — Recovery Delta Iteration 533

Date: 2026-09-07

## Authority advanced
Iteration 533 preregisters exact truncation/convergence diagnostics for the frozen BASE/HALF/QUARTER central4 levels without changing any physical acceptance rule.

For the frozen central4 first-derivative stencil,
`D_h f = f' - h^4 f^(5)/30 - h^6 f^(7)/252 - h^8 f^(9)/4320 + O(h^10)`.
Thus the mixed tensor-product derivative has a common formal `O(h^4)` leading error under sufficient smoothness. Across BASE=`h`, HALF=`h/2`, QUARTER=`h/4`, the common h4 error scales `1:1/16:1/256` and the next h6 error scales `1:1/64:1/4096`.

Prospectively frozen diagnostics:
- leading-h4 difference ratio: `(BASE-HALF)/(HALF-QUARTER) -> 16` when the common h4 term dominates and denominator is nonzero;
- `R_BH=(16*HALF-BASE)/15` cancels formal h4;
- `R_HQ=(16*QUARTER-HALF)/15` cancels formal h4;
- `R_3=(BASE-80*HALF+1024*QUARTER)/945` cancels formal h4 and h6.

Classification: `PASS_ITER424_CENTRAL4_THREE_LEVEL_TRUNCATION_GEOMETRY_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.
Machine-readable authority: `candidate_gravity/results/iteration533_iter424_three_level_truncation_geometry_exact_audit.json`.

## Guardrail
These formulas are diagnostic only. They do not alter the frozen five-clause Iteration-424 acceptance, cannot replace physical D_s by a Richardson/extrapolated value, cannot rescue a failed mass-step clause, and do not authorize smaller h, threshold weakening, index2 promotion, ANSATZ-003, Fisher, or resources.

## Active computation
Unique active heavy prerequisite remains repaired quarter-rank1 run `34094463024`, job `101654832475`. Last live inspection: stages 1–4 complete, stage5 full-z MP active; stage-level completion approximately `57.1%`. No duplicate heavy Action launched.

## Authority ledger
Physical/operator authority: Iteration 411.
Physical blocker: Iteration 421, unresolved set `[2]`.
BASE/HALF support: Iteration 523 (`32/32`).
BASE/HALF assembly: Iteration 527.
Quarter support manifest: Iteration 529.
Three-level Gram: Iteration 530.
Normalized conditioning: Iteration 531.
Quarter successor-order preregistration: Iteration 532.
Three-level truncation diagnostic: Iteration 533.
Latest authoritative research iteration: Iteration 533.

MODEL_READINESS: 24%
ITERATION_TASK_COMPLETION: 100%
Readiness change: 0 percentage points.

## Exact next gate
Raw-consume rank1 only after terminal completion. Raw-valid PASS -> preregistered rank2 `(-2.5e-6,+1.25e-6)`; otherwise follow Iteration-532 fail-closed transition rule.
