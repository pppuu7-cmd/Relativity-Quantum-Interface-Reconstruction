# RQIR Research Log — Iteration 037

**Date:** 2026-08-29  
**Target:** advance the phase-referenced D2 covariance measurement gate without inventing a detector PSD or arbitrary SNR.

## Result

For one accepted real Gaussian output sample with affine covariance

`Sigma(alpha)=Sigma0+alpha Sigma1`

and the same model required to remain positive for the full source branch interval `alpha in [-1,1]`, the whitened derivative eigenvalues obey `|lambda_k|<1`. Therefore

`I_alpha^(shot)=1/2 sum lambda_k^2 < m/2`

for output dimension `m`.

This yields **RQIR-NG-016**: a finite-dimensional affine covariance-only Gaussian readout has a positivity-limited per-shot Fisher ceiling.

For a bivariate readout, `Ishot<1`. Combined with the coordinate-correct Iteration-035 first-four break-even product `~4.4502e4`, a necessary equal-efficiency condition is

`t_P/t_C > 4.4502e4`.

Examples:

- `t_P=1 s` -> `t_C<22.47 us`;
- `t_P=100 s` -> `t_C<2.247 ms`;
- `t_P=10^4 s` -> `t_C<0.2247 s`.

The fifth-row product `~1.0012e6` is much harsher.

A joint `m=8` output relaxes the necessary first-four cycle ratio to `>1.11255e4`, but then independent row-time summation is invalid because one shot contributes to several covariance directions simultaneously.

This gives **RQIR-RESOURCE-013**: shared-shot covariance acquisition must be costed with the full matrix Fisher, not `sum gamma_i/q_i`, unless rows are genuinely measured in separate campaigns.

## Interpretation

The high-value covariance rows remain useful geometrically, but the simple minimal bivariate covariance-only implementation is resource-competitive only if it is enormously faster than source metrology. The next useful branch is therefore a joint multi-output likelihood or a readout that simultaneously carries mean/response information.

## Files

- `analysis/phase_referenced_gaussian_covariance_bound_iteration037.py`
- `docs/PHASE_REFERENCED_GAUSSIAN_COVARIANCE_BOUND.md`
- `recovery/RECOVERY_DELTA_ITERATION_037.md`

## Next gate

Construct a joint-output D2 phase-referenced likelihood for covariance rows `(0,1,3,7)` with matrix-valued covariance derivatives, centered mean/timing/additive nuisances, and imprecision/backaction. Compare shared-shot profiled Fisher/time directly against `R_P^(alpha)`.
