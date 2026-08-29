# RQIR Iteration 022 — Native Calibration and Reference Fisher Rates

**Date:** 2026-08-29  
**Status:** physical measurement-model layer closed parametrically; hardware-specific transduction/PSD values remain open.

## 1. Target

Iteration 021 established that a unique wall-clock optimum is undefined until every independent resource channel has a physical Fisher-information rate. Detector and source-preparation rates already have native forms, but gravitational mean/covariance calibration and timing/additive/gain references still used dimensionless information requirements.

This iteration derives those rates from explicit measurement models without inventing hardware performance.

## 2. D1 mean-calibration rate

For a binary matter-wave readout

\[
p_+(\phi)=\frac{1+C\cos\phi}{2},
\]

operated at quadrature, the accepted-event Fisher information in phase is

\[
I_\phi=C^2.
\]

If a row-normalized calibration coordinate `u_i` produces phase response

\[
\partial\phi/\partial u_i=k_i,
\]

then the physical row Fisher rate is

\[
\boxed{R_{M,i}^{D1}=\frac{p_i C_i^2 k_i^2}{t_{\rm cyc,i}}}.
\]

This removes the old hidden `xi_mean`: the remaining quantity `k_i` is an explicit, measurable transduction in rad per row unit.

## 3. Gaussian covariance/noise calibration

For a zero-mean Gaussian observation with covariance `Sigma(lambda)`, the Fisher matrix is

\[
I_{ab}=\frac12\mathrm{Tr}\left(\Sigma^{-1}\Sigma_{,a}\Sigma^{-1}\Sigma_{,b}\right).
\]

For a scalar log-variance parameter, one statistically independent Gaussian sample gives

\[
I_{\ln V}=\frac12.
\]

With approximately `2 B T` independent real modes in bandwidth `B`, the unit-log-variance Fisher rate is therefore

\[
\boxed{R_C\simeq \eta_{\rm duty} B k_C^2},
\]

where `k_C=d ln V / d u_C` is the explicit covariance-row transduction.

This gives a concrete interpretation of the large corrected `gamma_cov~10^6`: it is not necessarily millions of slow shots if a broadband stationary readout supplies many statistically independent modes per second.

## 4. D2 mean-calibration rate

For a stationary Gaussian force readout and known force template `h_i(f)` for row coordinate `u_i`, the native Fisher information is

\[
I_i=4\int_0^\infty df\,\frac{|\partial h_i(f)/\partial u_i|^2}{S_F(f)}
\]

for the standard one-sided PSD convention. For repeated or duty-cycled measurements,

\[
\boxed{R_{M,i}^{D2}=\eta_i\,4\int df\,\frac{|\partial h_i(f)/\partial u_i|^2}{S_F(f)}}
\]

per wall second when the template is normalized per unit live time. Any alternative PSD convention must carry its prefactor explicitly; it must not be hidden inside a standardized `xi`.

## 5. Timing-reference Fisher rate

Let the physical timing error be `delta t` and the dimensionless timing nuisance be

\[
\delta\tau=\omega_{\rm gap}\delta t,
\qquad \omega_{\rm gap}=2\pi f_{\rm gap}.
\]

If one accepted timing-reference event estimates `delta t` with Gaussian RMS `sigma_t,event`, then

\[
I_{\tau,\rm event}=\frac{1}{(\omega_{\rm gap}\sigma_{t,\rm event})^2},
\]

and

\[
\boxed{R_\tau=\frac{p_{\rm acc}}{t_{\rm cyc}(\omega_{\rm gap}\sigma_{t,\rm event})^2}}.
\]

To reach a target physical timing prior `sigma_t,target`, the required wall time is

\[
\boxed{T_\tau=\frac{t_{\rm cyc}}{p_{\rm acc}}
\left(\frac{\sigma_{t,\rm event}}{\sigma_{t,\rm target}}\right)^2}.
\]

The explicit `f_gap` cancels when the target and event uncertainties are converted consistently. This is a useful new resource invariant.

**RQIR-RESOURCE-006:** reference-control cost is determined by event-level metrology precision relative to the required prior, multiplied by cycle/acceptance cost; the dimensionless nuisance normalization must not create artificial wall-time dependence.

## 6. Additive-offset and gain-reference rates

For a row-normalized additive reference with per-event Gaussian uncertainty `sigma_b,event`,

\[
\boxed{R_b=\frac{p_{\rm acc}}{t_{\rm cyc}\sigma_{b,\rm event}^2}}.
\]

For a known-amplitude fractional gain reference with per-event reference SNR `rho_g`, the local Fisher rate is

\[
\boxed{R_g=\frac{p_{\rm acc}\rho_g^2}{t_{\rm cyc}}}.
\]

The Iteration-017 nonlinear gain×state product budget still applies: a large `R_g` is useful only relative to the residual source-state uncertainty.

## 7. Transparent numerical benchmarks

The following numbers are deliberately **unit-coupling benchmarks**, not hardware forecasts. They use the current corrected 90%-retention row weights and make all remaining assumptions explicit.

Current values:

- D1 `gamma_mean=1.7219876e6`, `gamma_cov=9.3814709e5`;
- D2 `gamma_mean=2.4144544e6`, `gamma_cov=9.2943956e5`;
- `f_gap=100 Hz`;
- `tau_max=4.99085067`, hence `T_coh=7.94 ms`;
- additional dead time `1 ms`;
- acceptance `0.5`.

### D1-like phase calibration benchmark

Take `C=0.66` and explicit unit transduction `k_i=1 rad/unit` for every mean row. Sequential calibration of all 14 mean rows then costs approximately:

- D1 weights: **275 h**;
- D2 weights under the same phase-readout assumption: **386 h**.

These large numbers are not predictions. They show that if each normalized row unit produces only O(1 rad) and settings are measured sequentially, mean calibration can dominate the wall-clock budget. A physical apparatus with larger `k_i`, parallel settings, higher contrast, or higher acceptance can reduce this quadratically/linearly according to the formula above.

### Broadband covariance benchmark

Take `B=1 kHz`, unit log-variance sensitivity, duty 1. Sequentially accumulating all 8 covariance rows gives only about:

- D1: **2.08 h**;
- D2: **2.07 h**.

Thus the apparently similar dimensionless `gamma_mean` and `gamma_cov` can correspond to radically different wall times because covariance/PSD estimation can harvest many independent modes per second.

This is the main practical consequence of replacing `xi` by native Fisher rates.

## 8. Timing reference benchmark

Using the current target priors `sigma_t,target~9.47 us` (D1) and `8.01 us` (D2), the required reference time depends only on the event-level timestamp precision relative to those targets.

At the current `8.94 ms` cycle and 50% acceptance:

- if event timestamp RMS is `10 us`, the ideal independent-reference time is only about `0.020 s` D1 and `0.028 s` D2;
- if it is `50 us`, about `0.50 s` D1 and `0.70 s` D2.

These tiny ideal statistical times expose the actual issue: slow correlated clock drift is not a white-shot-statistics problem. It requires a drift spectrum/stability model. Iteration 016's structural degeneracy therefore survives; the independent reference must track the relevant low-frequency modes, not merely accumulate high-rate timestamp samples.

**RQIR-DRIFT-002:** once white timing-reference statistics are fast enough, the limiting resource moves to low-frequency/common-mode stability; a white per-event Fisher rate alone is insufficient to certify the timing prior over a long campaign.

## 9. Consequence for Iteration 021

The complete optimizer can now accept physically interpretable rates:

\[
R_D,\ R_P,\ R_{M,i},\ R_{C,i},\ R_\tau,\ R_{b_M},\ R_{b_C},\ R_g.
\]

However, a unique SI-time optimum still requires apparatus-specific values of the transductions `k_i`, force/reference PSDs, bandwidths, duty cycles, and low-frequency drift spectra.

The important advance is that there is no longer a conceptual need for standardized `xi_mean`, `xi_cov`, or a dimensionless seconds conversion. Every remaining unknown is a measurable hardware quantity.

## 10. Next gate

The highest-value next iteration is a **low-frequency stability / Allan-variance gate** for timing and additive references. It should replace independent white-event priors by colored drift PSDs, determine the calibration cadence required to keep the Iteration-016 priors valid over the full D1/D2 acquisition campaign, and then feed that cadence cost into the Iteration-021 wall-clock optimizer.

## Reproducibility

Code: `analysis/native_calibration_reference_rates_iteration022.py`.
