# RQIR Second-Order Nonlinear Bias Audit

**Date:** 2026-08-29  
**Iteration:** 017  
**Status:** local Toy009 / Iteration-011 calibration likelihood audit; not an experimental forecast.

## 1. Purpose

Iterations 015-016 established the corrected hard-constrained 22-dimensional source-nuisance basis and showed that first-order timing/geometry/additive systematics require independent control priors. Pure common multiplicative gain is first-order suppressed at the exact null.

The next unresolved question is whether the omitted nonlinear terms can re-enter strongly enough to invalidate the first-order resource budget.

The calibration residual is expanded schematically as

\[
y_C \simeq A\,\delta\theta
+\delta\tau A_\tau\theta_0
+\frac12\delta\tau^2 A_{\tau\tau}\theta_0
+\delta g\,A\,\delta\theta
+\delta g\,\delta\tau A_\tau\theta_0+\cdots .
\]

Here `theta0` is the exact-null source difference, `A theta0=0`.

## 2. Timing curvature

Finite differencing of the current row-normalized calibration map gives

\[
\|A_{\tau\tau}\theta_0\|\approx1.2525\times10^{-1}.
\]

The largest absolute second-derivative components are approximately

\[
\max_{mean}|v_{\tau\tau}|\approx4.77\times10^{-2},
\qquad
\max_{cov}|v_{\tau\tau}|\approx5.23\times10^{-2}.
\]

The quadratic residual is propagated through the full corrected joint Fisher model, including the four first-order systematic columns and the Iteration-016 control priors.

### D1

At the current first-order timing prior

\[
\sigma(\delta\tau)=5.95\times10^{-3},
\]

the unmodeled quadratic timing term biases beta by only

\[
\boxed{|\Delta\beta|\approx3.49\times10^{-5}\,\sigma_\beta}.
\]

A quadratic timing bias of `0.1 sigma_beta` is reached only around

\[
\boxed{|\delta\tau|\approx0.319,}
\]

about `53.5` times larger than the current first-order timing prior. At a 100 Hz gap this corresponds to about `507 us`.

### D2

At

\[
\sigma(\delta\tau)=5.03\times10^{-3},
\]

the quadratic timing bias is

\[
\boxed{|\Delta\beta|\approx8.75\times10^{-6}\,\sigma_\beta}.
\]

The `0.1 sigma_beta` curvature threshold is approximately

\[
\boxed{|\delta\tau|\approx0.538,}
\]

about `107` times the current first-order timing prior, or about `856 us` at 100 Hz.

### RQIR-NL-001 — timing-curvature hierarchy

Within the present local Toy009 likelihood, satisfying the first-order timing-control requirement from Iteration 016 automatically suppresses the second-order timing curvature by many orders below the statistical error budget. Therefore timing curvature is **not** the present calibration bottleneck.

This result is local to the declared phase grid and source model; it is not a theorem for arbitrary pulse sequences.

## 3. Bilinear common-gain × source-state coupling

Because `A theta0=0`, a common multiplicative gain has no standalone first-order column at the exact null. The leading state-dependent term is

\[
\boxed{q_g=\delta g\,A\,\delta\theta.}
\]

Propagating this residual through the same joint Fisher model and taking the 22-dimensional orthogonal source nuisance to have the local linear posterior covariance gives an RMS beta-bias coefficient

\[
\sigma(\Delta\beta)\approx0.325\,|\delta g|
\]

for both D1 and D2 in detector-normalized beta units.

Relative to the current `sigma_beta~1.054`, a `1%` common gain error therefore corresponds to only about `3.1e-3 sigma_beta` RMS under this **posterior-scale local nuisance assumption**. The gain error needed to reach `0.1 sigma_beta` is roughly

\[
\boxed{|\delta g|\sim0.32.}
\]

### Critical scope warning

This is not a global tolerance on gain. The estimate assumes the orthogonal source-state error is itself at the current posterior scale. For an arbitrary uncalibrated source deviation `u`, the bias scales as

\[
\Delta\beta\propto\delta g\,u,
\]

so no finite gain-only bound exists without a bound or prior on `u`.

### RQIR-NL-002 — bilinear-product resource rule

A first-order null in one control parameter does not remove the need to control that parameter globally; it changes the relevant resource from a standalone tolerance to a **product tolerance** with the coupled nuisance amplitude.

For common gain in the current exact-null protocol, the meaningful requirement is on `|delta g|` times the residual orthogonal source-preparation uncertainty, not on `|delta g|` alone.

## 4. Gain × timing cross-term

The cross residual

\[
q_{g\tau}=\delta g\,\delta\tau A_\tau\theta_0
\]

is also small at the current first-order timing priors. For `|delta g|=1%`:

- D1 bias is about `2.3e-5 sigma_beta`;
- D2 bias is about `4.5e-5 sigma_beta`.

Thus it is subdominant to the already-required first-order timing/offset control in the present local model.

## 5. Scientific interpretation

The nonlinear audit does **not** loosen the Iteration-016 control requirements. Instead it establishes a hierarchy:

1. independent first-order timing/additive control is mandatory for identifiability;
2. once those priors are satisfied, finite timing curvature is negligible at the current operating point;
3. common gain remains relevant only through products with residual state/timing errors, so it should be budgeted jointly with source reproducibility rather than promoted to an artificial first-order Fisher column.

No claim about new gravitational physics follows from this result.

## 6. Reproducibility

Code: `analysis/second_order_nonlinear_bias_iteration017.py`.

The script imports the corrected Iterations 015-016 model, computes the timing second derivative by centered finite differences, propagates unmodeled residuals through the joint Fisher inverse, and includes regression guards for the recorded headline numbers.

## 7. Next gate

Translate the first-order timing prior and the newly identified gain×state product budget into explicit D1/D2 reference-channel hardware variables: clock jitter spectrum, shot-to-shot reset/repreparation error, dead time, and common gain/reference monitoring. The next resource objective should be detector-level `F_beta|theta` per wall-clock time rather than dimensionless Fisher weight alone.
