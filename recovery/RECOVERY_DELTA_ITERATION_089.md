# RQIR Recovery Delta — Iteration 089

**Date:** 2026-08-30

## New retained result

Iteration 089 combines the robust science, calibration, source-metrology and control/reference resources into one exact wall-clock interval for independent bounded uncertainties.

Use

`T_total=[Z^2/R_beta + gamma sum_j 1/R_cal,j + C_src/R_src]/(1-d)`.

### RQIR-RESOURCE-042

For independent intervals:

`T_upper=[Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`,

`T_lower=[Z^2/R_beta^+ + gamma sum_j 1/R_cal,j^+ + C_src/R_src^+]/(1-d^-)`.

These are exact endpoint bounds for the Cartesian uncertainty model because wall time is monotone in every rate and in duty loss.

NG-030 robust dominance is equivalent to positive margin

`M_{i<k}=T_k^lower-T_i^upper>0`.

### RQIR-NG-039

When a source-metrology control/design setting is chosen before uncertain apparatus parameters are known, use the guaranteed rate

`max_design min_uncertainty R`.

Do not use the generally optimistic `min_uncertainty max_design R` unless adaptive retuning is physically implemented and its calibration/duty cost is included.

A deterministic positive-rate counterexample gives `max min=e^-1` versus `min max=1`.

## Reproducibility

- `analysis/joint_robust_total_time_iteration089.py`
- `docs/PAPER_III_JOINT_ROBUST_TOTAL_TIME_ITERATION089.md`
- `research_log/2026-08-30_iteration_089_joint_robust_total_time.md`

## Current next gate

The rate algebra is ready for apparatus insertion. Construct one declared physical reference apparatus envelope with:

- two-band science transfer plus full PSD/cross-PSD intervals;
- seven same-time dual-probe calibration Fisher-block intervals;
- robust independent source-metrology rate with correct max/min order;
- control/reference duty/stability interval.

Then apply RESOURCE-042 and NG-030 to Toy009/Toy014. If published/apparatus data do not close all coordinates, retain a parameterized feasibility envelope and record the missing measurements explicitly rather than inventing them.
