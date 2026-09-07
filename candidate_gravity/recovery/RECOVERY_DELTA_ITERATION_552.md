# RQIR Candidate Gravity — Recovery Delta Iteration 552

Date: 2026-09-07

## Authority advanced
Iteration 552 certifies that u↔v-swapped QUARTER coordinates are not equivalent in the current routed parent implementation and therefore cannot be support-substituted.

Raw-comparison sources are already authoritative rank1 and rank3 artifacts. Their 80 z/phi rows align exactly. MP120 real values differ in all 80/80 rows. Absolute differences range from approximately `8.07090e-13` to `2.67304e-10`; maximum local relative difference is approximately `1.12203e-4`. The raw swap discrepancy is at least approximately `4.61e3` times and up to approximately `3.26e6` times the larger corresponding pairwise radial-error estimate.

Exact geometry explains the asymmetry: `lambda` and `rho` are u↔v symmetric, but `alpha=-(s+u-v)/(2s)` is not; `alpha(u,v)-alpha(v,u)=(v-u)/s`. Since the routed point is `p=-a+alpha*q+rho*unit(z,phi)`, a swap changes the physical cut momentum for `u!=v`.

Classification: `PASS_ITER424_UV_SWAP_NON_EQUIVALENCE_RANK1_RANK3__DIAGNOSTIC_ONLY_NON_PROMOTING`.
Machine-readable authority: `candidate_gravity/results/iteration552_iter424_uv_swap_non_equivalence_audit.json`.

## Consequence
Iteration-532 `NO_UV_SYMMETRY_SUBSTITUTION` is now explicitly evidence-backed. No rank may be skipped or replaced by its swapped partner. This is diagnostic/provenance authority only, not a Candidate-Gravity consistency FAIL or physical index2 result.

## Active heavy route
Rank7 raw PASS remains Iteration 551. Canonical rank8 run `34153849866`, coordinate `(+1.25e-6,-1.25e-6)`, was triggered under unchanged frozen conditions. It must be raw-consumed after terminal completion before any rank9 authorization.

MODEL_READINESS: 24%
ITERATION_TASK_COMPLETION: 100%
Readiness change: 0 percentage points.

## Exact next gate
Raw-consume rank8 run `34153849866`; only raw-valid PASS permits rank9 `(+1.25e-6,+1.25e-6)`.
