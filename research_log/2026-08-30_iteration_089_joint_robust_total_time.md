# RQIR Research Log — Iteration 089

**Date:** 2026-08-30

## Goal

Combine the robust science-rate bound (Iteration 087), seven-layer calibration bounds (Iteration 088), independent source-metrology rate and control/reference duty into one exact NG-030 wall-clock interval.

## Result

For

`T_total=[Z^2/R_beta + gamma sum_j 1/R_cal,j + C_src/R_src]/(1-d)`,

with independent bounded intervals, monotonicity gives exact box extrema:

`T_upper=[Z^2/R_beta^- + gamma sum 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`,

`T_lower=[Z^2/R_beta^+ + gamma sum 1/R_cal,j^+ + C_src/R_src^+]/(1-d^-)`.

New **RQIR-RESOURCE-042**: the interval `[T_lower,T_upper]` is the exact joint Cartesian-box wall-clock certificate for the current independent uncertainty model.

For architecture comparison define

`M_{i<k}=T_k^lower-T_i^upper`.

Positive margin certifies robust dominance; otherwise NG-030 keeps the decision unresolved.

## Source-metrology correction

New **RQIR-NG-039**: if a source-metrology design setting must be fixed before uncertain apparatus parameters are known, the guaranteed rate is

`max_design min_uncertainty R`,

not the generally larger

`min_uncertainty max_design R`.

The deterministic counterexample `R(q,u)=exp[-(q-u)^2]`, `u={-1,+1}`, gives

`max min = exp(-1)=0.36787944117`,

but

`min max = 1`.

Thus post-hoc reoptimization can understate source-preparation wall time unless an adaptive retuning protocol and its duty/calibration cost are explicitly included.

## Regression

Synthetic architecture intervals overlap:

- A: `[45.8754208754,70.2319587629] s`;
- B: `[50.5281059792,68.9506673882] s`.

Neither robust dominance margin is positive. These are regression-only values, not apparatus predictions.

## Reproduce

`python analysis/joint_robust_total_time_iteration089.py`

## Document

`docs/PAPER_III_JOINT_ROBUST_TOTAL_TIME_ITERATION089.md`

## Next gate

Build one declared physical D1/D2 apparatus envelope from externally sourced/measured or explicitly design-level transfer, PSD/cross-PSD, calibration, source-metrology and duty parameters. Feed its intervals through RESOURCE-042; if data are incomplete, report the exact missing coordinates rather than inventing ASD values.
