# RQIR Research Log — Iteration 033

**Date:** 2026-08-29  
**Target:** convert the Iteration-032 covariance-complementarity gain into a physical Fisher-rate break-even against independent source-preparation metrology.

## Starting point

Iteration 032 established that, at `y_ref=-4` and `lambda=1`, the relational-potential + force-mean D2 branch requires `C_a*=5.82122` for 90% retention with relational covariance only. The best four added force-covariance rows `(0,1,3,7)` reduce this to `0.5889578885`; all eight reduce it to `0.0670833727`.

Those were Fisher-geometry results only. Their wall-clock value was still unknown.

## Physical rate model

For a stationary Gaussian scalar covariance/log-PSD coordinate, retain the Iteration-022 convention

`q_cov = eta_duty B_eff kappa_eff^2`,

with `kappa_eff=d ln S/du`.

For multi-channel covariance/cross-spectrum data, `q_cov` is the corresponding integrated spectral-matrix Fisher rate. A force PSD alone is insufficient; the derivative of the detector spectral matrix with respect to the source covariance coordinate is required.

## New negative gate

**RQIR-NG-013 — covariance-transduction derivative obstruction:** `S_F(f)` plus bandwidth/duty does not determine the Fisher rate of a source covariance row. One must also provide `dS/d u_cov` (or cross-spectral derivatives) in the physical nuisance coordinate.

## Break-even result

For a covariance subset with row target `gamma_cov=0.929e6`, physical cost is

`T_cov=sum_i gamma_cov/q_i`.

The preparation time it removes is

`Delta T_prep=Delta C_a/R_P`.

Hence covariance is locally wall-clock beneficial only if

`sum_i gamma_cov/q_i < Delta C_a/R_P`.

At equal per-row covariance rate:

- best first four: `Delta C_a=5.2322621115`, requiring `q_cov/R_P > 7.10209e5`;
- remaining four: `Delta C_a=0.5218745158`, requiring `q_cov/R_P > 7.12049e6`;
- all eight vs none: requiring `q_cov/R_P > 1.29159e6`.

Thus the last four covariance rows have about an order-of-magnitude harsher rate threshold than the high-value first four.

## Transparent scaling

Using ideal `F_Q=13.2707`, `p_P eta_P=1`, `B=1 kHz`:

- if `t_P=1 s`, first-four break-even needs `kappa_eff>97.1`;
- if `t_P=100 s`, `kappa_eff>9.71`;
- if `t_P=10^4 s`, `kappa_eff>0.971`.

These are scaling examples only.

## New retained rule

**RQIR-RESOURCE-011 — covariance/preparation substitution criterion:** covariance rows must be selected by physical rate-weighted inequality `sum gamma_i/q_i < Delta C_a/R_P`, not by rank or Fisher gain alone.

## Interpretation

Iteration 032's strong covariance nuisance closure survives, but it is not automatically a wall-clock advantage. Unless covariance Fisher accumulates vastly faster than source-preparation Fisher, independent source metrology may be cheaper than buying millions of row-Fisher units in extra covariance calibration.

This is an experimentally useful screening result and narrows the next gate to stochastic transduction derivatives.

## Files

- `analysis/d2_covariance_rate_break_even_iteration033.py`
- `docs/D2_COVARIANCE_RATE_BREAK_EVEN.md`
- `recovery/RECOVERY_DELTA_ITERATION_033.md`

## Next gate

Derive row-specific `dS_F/du_cov` and cross-spectral derivatives for force covariance and finite-reference relational covariance from one common D2 detector model; then insert those `q_i` together with `R_P` and timing/reference duty into the full `F_beta|theta/T_wall` optimizer.
