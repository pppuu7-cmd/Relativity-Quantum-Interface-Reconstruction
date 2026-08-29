# RQIR Research Log — Iteration 017: Second-Order Nonlinear Bias Audit

**Date:** 2026-08-29

## Starting point

Iteration 016 established that first-order timing/geometry/additive calibration systematics require independent control priors and that pure common multiplicative gain is first-order suppressed at exact null. The next declared gate was the omitted second-order nonlinear bias.

## Terms audited

The calibration residual was expanded through the leading nonlinear terms:

- `0.5 * delta_tau^2 * A_tautau theta0`;
- `delta_g * A * delta_theta`;
- `delta_g * delta_tau * A_tau theta0`.

All propagation uses the corrected hard-constrained 22D source-nuisance basis from Iteration 015 and the explicit low-rank systematics/prior bundle from Iteration 016.

## Timing curvature result

Current row-normalized timing second-derivative norm:

- `||v_tautau|| ~ 0.12525`;
- max mean component `~0.0477`;
- max covariance component `~0.0523`.

At the current first-order timing priors:

D1:
- `sigma(delta_tau)=5.95e-3`;
- quadratic timing bias `~3.49e-5 sigma_beta`;
- `0.1 sigma_beta` threshold only near `delta_tau~0.319`, about `53.5x` the current prior;
- equivalent `~507 us` at 100 Hz.

D2:
- `sigma(delta_tau)=5.03e-3`;
- quadratic timing bias `~8.75e-6 sigma_beta`;
- `0.1 sigma_beta` threshold near `delta_tau~0.538`, about `107x` the current prior;
- equivalent `~856 us` at 100 Hz.

Recorded as **RQIR-NL-001**: once the current first-order timing-control gate is satisfied, timing curvature is not the limiting systematic in the present local Toy009 likelihood.

## Bilinear gain-state result

Because `A theta0=0`, common gain enters first through `delta_g A delta_theta`.

Using the local linear posterior covariance for the 22 orthogonal source nuisance coordinates, the RMS beta-bias coefficient is `~0.325 |delta_g|` for both D1 and D2. A 1% common gain error is therefore only about `3.1e-3 sigma_beta` RMS under that local posterior-scale assumption; roughly 32% gain error would be needed for `0.1 sigma_beta`.

Important scope restriction: this is not a global gain tolerance. For arbitrary unbounded source deviation the product `delta_g * delta_theta` is unbounded. Recorded as **RQIR-NL-002**: first-order nulling converts a standalone control requirement into a product-resource requirement with the coupled nuisance amplitude.

## Gain-timing cross-term

At 1% common gain and the current first-order timing priors:

- D1: `~2.3e-5 sigma_beta`;
- D2: `~4.5e-5 sigma_beta`.

Subdominant to the first-order control gate.

## Files

- `analysis/second_order_nonlinear_bias_iteration017.py`
- `docs/SECOND_ORDER_NONLINEAR_BIAS_AUDIT.md`
- this log

## Next gate

Translate the first-order timing prior and gain×state product requirement into explicit D1/D2 reference-channel resources: clock jitter spectrum, reset/repreparation error, dead time and gain/reference monitoring, then optimize detector-level profiled Fisher per wall-clock time.
