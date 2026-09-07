# RQIR Candidate Gravity — Recovery Delta Iteration 553

Date: 2026-09-07

## Authority advanced
Iteration 553 independently replicates the Iteration-552 u↔v non-equivalence result using the second already raw-closed swapped pair rank2/rank7.

Rank2 `(-2.5e-6,+1.25e-6)` versus rank7 `(+1.25e-6,-2.5e-6)`: all 80 z/phi rows align; MP120 real components differ in 80/80 rows. Absolute differences span approximately `2.42140e-12` to `8.01905e-10`, with maximum local relative difference approximately `3.36547e-4`. Discrepancy/radial-error separation is at least approximately `1.388e4` and reaches approximately `9.437e6`.

The exact alpha-swap gap is three times that of the Iteration-552 rank1/rank3 pair. Corresponding signed raw swap differences scale by nearly the same factor in all 80 rows: ratio range `2.999763206...` to `3.000157660...`, mean `2.999976034...`, same sign 80/80. This supports the source-level alpha-shift mechanism locally; it is not a general linearity theorem.

Classification: `PASS_ITER424_UV_SWAP_NON_EQUIVALENCE_REPLICATION_RANK2_RANK7__DIAGNOSTIC_ONLY_NON_PROMOTING`.
Machine-readable authority: `candidate_gravity/results/iteration553_iter424_uv_swap_replication_rank2_rank7.json`.

## Consequence
`NO_UV_SYMMETRY_SUBSTITUTION` is independently replicated and remains mandatory. Frozen rank order is unchanged.

## Active heavy route
Rank7 raw PASS: Iteration 551. Rank8 canonical run `34153849866`, job `101841466120`, coordinate `(+1.25e-6,-1.25e-6)`, remains the only allowed heavy successor. No duplicate run is authorized.

MODEL_READINESS: 24%
ITERATION_TASK_COMPLETION: 100%
Readiness change: 0 percentage points.

## Exact next gate
Raw-consume rank8 after terminal completion; only raw-valid PASS permits rank9 `(+1.25e-6,+1.25e-6)`.
