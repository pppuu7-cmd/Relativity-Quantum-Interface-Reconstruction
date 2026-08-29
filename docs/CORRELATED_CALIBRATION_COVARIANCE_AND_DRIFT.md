# RQIR Correlated Calibration Covariance and Drift — Iteration 014

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`  
**Scope:** finite-dimensional Toy009 / Iteration-011 calibration stress test; not a hardware forecast.

## 1. Question

Iteration 013 showed that resource-optimal calibration is heterogeneous across the 14 potential-mean and 8 covariance rows. The next gate is whether that advantage survives non-diagonal calibration covariance and slow calibration drift.

The current source, NP3 observable set, detector definitions and exact-null state are unchanged.

## 2. Correlated covariance model

Within each physical row class use a compound-symmetry covariance

\[
C_n(\rho)=(1-\rho)I+\rho\mathbf 1\mathbf 1^T.
\]

The calibration Fisher becomes

\[
F_C=F_{trace+energy}
+\gamma_m A_m^T C_{14}(\rho_m)^{-1}A_m
+\gamma_c A_c^T C_8(\rho_c)^{-1}A_c.
\]

The cost function remains

\[
N_{eq}=14\gamma_m+8\gamma_c
\]

for equal standardized single-shot information. This model holds marginal row variance fixed while introducing common-mode correlation. It is therefore a covariance stress test, not yet an irreducible systematic-floor model.

## 3. D1 result

At 90% retained profiled detector information:

| common correlation `rho_m=rho_c` | optimized standardized cost | ratio to uncorrelated |
|---:|---:|---:|
| 0 | `5.346e6` | 1.000 |
| 0.01 | `5.335e6` | 0.998 |
| 0.05 | `5.298e6` | 0.991 |
| 0.10 | `5.274e6` | 0.986 |

Moderate positive equicorrelation does **not** damage D1 in this model and can slightly reduce the required cost because the D1 nuisance-breaking information is substantially contrast-like across calibration settings. Common-mode noise leaves those contrasts relatively well determined when marginal variance is held fixed.

This is a useful negative correction to the naive rule that any positive correlation must reduce useful Fisher information.

## 4. D2 result

For D2 under the same stress test:

| common correlation `rho_m=rho_c` | optimized standardized cost | ratio to uncorrelated |
|---:|---:|---:|
| 0 | `1.041e7` | 1.000 |
| 0.01 | `1.061e7` | 1.019 |
| 0.05 | `1.239e7` | 1.191 |
| 0.10 | `2.216e7` | 2.129 |

D2 is therefore materially more sensitive to modest common-mode correlation. At `rho=0.10` the calibration resource rises by about a factor `2.1`.

### RQIR-CAL-006 — correlation orientation principle

Calibration correlation cannot be summarized by a scalar degradation factor. Its effect depends on the orientation of the correlated-noise eigenspaces relative to the detector-relevant nuisance tangents. The same non-diagonal covariance can be nearly harmless for D1 and costly for D2.

Scope: current finite-dimensional stress test.

## 5. First-order slow-drift couplings

The exact-null state difference is `theta0`, satisfying

\[
A\theta_0=0.
\]

For a calibration-geometry parameter `z`, a slow error produces the first-order residual

\[
\delta\mu_C\simeq (\partial_z A)\theta_0\,\delta z.
\]

Finite-difference derivatives were evaluated for:

- second-probe position `y1`;
- a common source-phase/time offset `delta tau` applied to all time-labelled calibration settings.

Their row-normalized residual-vector norms are approximately

\[
\|v_y\|\approx2.91\times10^{-4},
\qquad
\|v_\tau\|\approx2.56\times10^{-2}.
\]

Thus the current design is roughly two orders of magnitude more sensitive to common phase/timing drift than to second-probe position drift in these normalized coordinates.

## 6. Conservative drift budgets

Using the Iteration-013 `q_m=q_c=1` optimized information allocations, require the largest drift-induced row residual to remain below 10% of the corresponding statistical calibration standard deviation.

### D1

With approximately

\[
\gamma_m=1.82\times10^5,\qquad
\gamma_c=3.49\times10^5,
\]

one obtains

\[
|\delta y_1|\lesssim1.22
\]

in the current dimensionless distance coordinate and

\[
\boxed{|\delta\tau|\lesssim1.63\times10^{-2}}.
\]

The timing form is

\[
|\delta t|\lesssim\frac{0.0163}{2\pi f_{gap}},
\]

or approximately:

- `2.60 ms` at `1 Hz`;
- `26 us` at `100 Hz`;
- `2.6 us` at `1 kHz`.

### D2

Using

\[
\gamma_m=1.70\times10^5,\qquad
\gamma_c=1.00\times10^6,
\]

one obtains

\[
|\delta y_1|\lesssim0.72,
\]

and

\[
\boxed{|\delta\tau|\lesssim9.63\times10^{-3}}.
\]

Equivalent timing bounds are approximately:

- `1.53 ms` at `1 Hz`;
- `15.3 us` at `100 Hz`;
- `1.53 us` at `1 kHz`.

These are standardized design bounds, not laboratory tolerances until the dimensionless distance and gap scale are fixed physically.

## 7. Multiplicative gain drift has a protected first-order null

For a multiplicative calibration gain `g`,

\[
\mu_C=gA\theta.
\]

At the exact-null state,

\[
\left.\frac{\partial\mu_C}{\partial g}\right|_{\theta_0}
=A\theta_0=0.
\]

Therefore a purely multiplicative common gain error does not mimic the hidden state direction at first order in the exact-null difference channel.

### RQIR-DRIFT-001 — exact-null gain protection

Exact-null calibration suppresses purely multiplicative calibration-gain drift to first order. This protection does **not** apply to geometry/time drift because those perturb the calibration operator itself and generate `(partial A) theta0`.

Scope: local first-order statement. Second-order gain-state products and additive offsets remain open.

## 8. Interpretation

Iteration 013's heterogeneous allocation gain survives modest non-diagonal covariance for D1 but is not automatically robust for D2. The important experimental-control nuisance emerging here is common source phase/timing, not simple multiplicative gain.

This sharpens G13: a realistic covariance model must track eigenvectors and drift derivatives, not just marginal variances.

## 9. Next gate

1. Replace fixed equicorrelation by an irreducible low-rank drift floor / explicit drift-nuisance Fisher model with priors.
2. Convert the dimensionless timing bound to a declared D1 pulse-clock and D2 sampling-clock stability budget including dead time and timing jitter.
3. Add additive offset drift and second-order gain-state terms; verify whether exact-null gain protection remains useful beyond local first order.
4. Only then convert the surviving standardized calibration costs to branch-specific wall-clock seconds.

Reproducibility code: `analysis/correlated_calibration_drift_iteration014.py`.
