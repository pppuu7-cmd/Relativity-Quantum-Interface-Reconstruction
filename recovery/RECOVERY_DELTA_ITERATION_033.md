# RQIR Recovery Delta — Iteration 033

**Date:** 2026-08-29

## New confirmed result

Iteration 032's covariance-complementarity gain was converted into a physical Fisher-rate break-even against independent source-preparation metrology.

For stationary scalar covariance/log-PSD calibration use the Iteration-022 convention

`q_cov = eta_duty * B_eff * kappa_eff^2`,

with `kappa_eff=d ln S/du`. For a multichannel spectrum use the corresponding integrated spectral-matrix Fisher rate.

## New negative gate

**RQIR-NG-013 — covariance-transduction derivative obstruction:** an equivalent-force PSD and bandwidth do not determine the Fisher rate of a source covariance row. The physical derivative `dS_detector/du_cov` or cross-spectral derivative is also required.

Do not assign SI covariance times from `S_F` alone.

## New resource rule

**RQIR-RESOURCE-011 — covariance/preparation substitution criterion:** for a covariance subset to replace independent preparation metrology beneficially in wall-clock time,

`sum_i gamma_i/q_i < Delta C_a/R_P`.

At the Iteration-032 `y_ref=-4`, `lambda=1` benchmark with `gamma_cov=0.929e6`:

- best four force-covariance rows `(0,1,3,7)` save `Delta C_a=5.2322621115`; equal-row break-even `q_cov/R_P > 7.10209e5`;
- remaining four save only `Delta C_a=0.5218745158`; break-even `q_cov/R_P > 7.12049e6`;
- all eight vs none: `q_cov/R_P > 1.29159e6`.

Therefore the geometric gain of all eight covariance rows does not imply a wall-clock advantage. The final four have severe diminishing resource return.

## Reproducibility

- `analysis/d2_covariance_rate_break_even_iteration033.py`
- `docs/D2_COVARIANCE_RATE_BREAK_EVEN.md`
- `research_log/2026-08-29_iteration_033_d2_covariance_rate_break_even.md`

## Next action

Derive row-specific force-covariance and finite-reference relational-covariance spectral derivatives from one common D2 detector model. Insert the resulting `q_i` into the full wall-clock optimizer together with source-preparation rate `R_P` and timing/reference recertification duty.
