# RQIR Recovery Delta — Iteration 046

**Date:** 2026-08-29

## New retained gate

**RQIR-NG-022 — profiled backaction tightening**

The same-copy reciprocal-linear/dephasing channel must be propagated through the complete detector/nuisance Jacobian, not judged by signal attenuation alone.

For the centered complementary best4 D2 branch at `y_ref=-4`, current calibration scale `lambda=1` and exact hard trace+energy constraints:

- baseline `F_beta|theta(C_alpha=0)=0.899476769`;
- baseline `C_alpha90=0.05006144`;
- even with effectively perfect source-amplitude metrology, 90% profiled information is impossible once `xi_shared>~0.7001013`;
- this corresponds to `I_shared~0.4901418` per normalized mean row;
- maximum optimistic shared fraction of centered `gamma_mean` across best4 trajectories is only `~31.61%`.

The earlier raw-signal cap `xi<=0.723982` / `~33.8%` is therefore an optimistic upper bound.

## New resource rule

**RQIR-RESOURCE-020 — backaction compensation frontier**

Same-copy measurement strength, independent source metrology and gravitational calibration exposure form a three-way frontier.

At fixed `lambda=1`, required `C_alpha90` rises from `~0.211` at `xi=.1` to `~21.42` at `.6`, `~128.85` at `.68`, then diverges near `xi~.7001`.

Keeping the old tiny `C_alpha=0.05006144` instead requires calibration scale approximately:

- xi .1 -> 1.019
- .2 -> 1.079
- .3 -> 1.199
- .4 -> 1.422
- .5 -> 1.875
- .6 -> 3.106
- .65 -> 4.992
- .68 -> 8.192
- .70 -> 14.783

Current optimistic shared target `xi=1.245286` and mean/cov crossover `xi=2.772804` cannot reach 90% irrespective of preparation/calibration in this proxy because detector-only beta Fisher is already below 0.9.

## Next

Audit exact QND/backaction-evading calibration capacity in the Toy009 hard source space before pursuing more elaborate nonreciprocal or ancilla measurement models.