# RQIR Research Log — Iteration 046

**Date:** 2026-08-29  
**Target:** propagate the reciprocal-linear/dephasing backaction proxy through the full hard-constrained D2 detector/nuisance Jacobian and solve the actual profiled 90% condition.

## Baseline reproduced

Centered D2 weights:

- `gamma_mean=1.830264703e6`;
- `gamma_cov=5.901272925e5`.

Complementary `y_ref=-4` best4 branch:

- `F_beta|theta(C_alpha=0)=0.899476769`;
- minimal unperturbed `C_alpha90=0.05006144`.

## New result

After propagating the exact two-force dephasing superoperator through beta signal and all 22 source-nuisance detector derivatives, the current `lambda=1` branch cannot maintain `F_beta|theta>=0.90` for

`xi_shared > 0.7001013`

even with asymptotically perfect independent source-amplitude metrology.

Thus the maximum profile-compatible same-copy information is

`I_shared<~0.4901418`

per normalized mean row, stricter than the raw-signal cap `0.5241495` from Iteration 044.

This is **RQIR-NG-022 — profiled backaction tightening**.

Across the `1.180254e6` best4 science trajectories, this can cover at most `~31.61%` of the centered mean target at current calibration exposure, even with perfect amplitude metrology.

## Backaction compensation frontier

At fixed `lambda=1`, required `C_alpha90` rises rapidly:

- xi .1 -> .211
- .2 -> .736
- .3 -> 1.787
- .4 -> 3.793
- .5 -> 8.091
- .6 -> 21.421
- .65 -> 48.31
- .68 -> 128.85

Alternatively keep `C_alpha=0.05006144` and increase calibration scale:

- xi .1 -> lambda 1.019
- .2 -> 1.079
- .3 -> 1.199
- .4 -> 1.422
- .5 -> 1.875
- .6 -> 3.106
- .65 -> 4.992
- .68 -> 8.192
- .70 -> 14.783

This is **RQIR-RESOURCE-020 — backaction compensation frontier**.

The previous optimistic shared target `xi=1.245286` and mean/cov crossover `xi=2.772804` are absolutely incompatible with a 90% target in this proxy because their detector-only beta Fisher is already only `~0.7344` and `~0.2435` respectively.

## Files

- `analysis/d2_profiled_backaction_frontier_iteration046.py`
- `docs/D2_PROFILED_BACKACTION_FRONTIER.md`
- `recovery/RECOVERY_DELTA_ITERATION_046.md`

## Next gate

Test candidate escape architectures rather than generic reciprocal gain. First audit whether an exact QND/backaction-evading calibration observable can span enough of the current hard source nuisance space to be useful; if not, move to nonreciprocal/coherent-noise-cancellation or ancilla-assisted measurement classes.