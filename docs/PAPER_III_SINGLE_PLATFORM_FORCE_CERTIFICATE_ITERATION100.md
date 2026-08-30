# RQIR Iteration 100 — Single-Platform Broadband Force-Certificate Audit

**Date:** 2026-08-30  
**Status:** Paper-III external apparatus partial-closure audit; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 099 formalized the minimum primitive apparatus certificate and required the next step to populate it only with quantities that can share one physical normalization. The goal here is therefore not to combine best-in-class numbers from different experiments, but to ask whether one published levitated force-sensing platform already closes a useful subset of the RQIR detector/science/calibration cuts.

The strongest single-platform detector-normalization anchor found in this pass is:

Z. Fu et al., **“Force detection sensitivity spectrum calibration of levitated nanomechanical sensor using harmonic Coulomb force,”** *Optics and Lasers in Engineering* 152, 106957 (2022), DOI `10.1016/j.optlaseng.2022.106957`, preprint `arXiv:2109.02437`.

This platform is especially relevant because it measures a physical force-to-displacement transfer function using a known harmonic Coulomb force and converts measured displacement PSD into a force detection sensitivity spectrum (FDSS), rather than quoting only one resonant ASD.

## 2. Publication-backed apparatus facts retained

The paper reports, in one apparatus:

- harmonic Coulomb-force injection through ITO electrodes;
- electric field `E0 = 3800 +/- 10 V/m` for the stated calibration geometry;
- measured force-to-displacement transfer `chi(omega)=q_ext/F_ext`;
- lock-in sweep of the transfer function from `1 kHz` to `500 kHz`;
- x-axis displacement calibration `80.7 +/- 0.5 mV/nm`;
- particle radius `80.8 +/- 3.1 nm`;
- measured displacement PSD and conversion to FDSS;
- explicit detector crosstalk modelling, including a residual z-mode feature near `48.5 kHz` with coupling coefficient about `0.008`;
- PSD sampling rate `937 kHz`, sampling duration `270 ms`, with ten averages used for the high-pressure curves;
- an off-resonance measured force sensitivity of order `10^-17 N/sqrt(Hz)` in the reported apparatus;
- a thermal-noise-limit value `(4.39 +/- 0.62)e-20 N/sqrt(Hz)` at `2.4e-6 mbar` under feedback cooling.

References:

- `https://arxiv.org/abs/2109.02437`
- `https://doi.org/10.1016/j.optlaseng.2022.106957`

## 3. RQIR-APP-004 — a broadband force spectrum can satisfy the factor-two frequency-span cut

The RQIR D2 science likelihood requires two retained frequencies `f` and `2f`, but those frequencies do not need to be two mechanical eigenmodes if a single broadband force sensor supplies a calibrated response at both frequencies.

The Fu transfer sweep covers

`1 kHz <= f_meas <= 500 kHz`.

Therefore every fundamental in

`boxed{1 kHz <= f <= 250 kHz}`

has both `f` and `2f` inside the same published transfer-function sweep.

### RQIR-APP-004 — broadband single-axis factor-two support

A single broadband force-referred sensor can satisfy the RQIR `f,2f` frequency-span requirement without requiring an accidental `2:1` ratio between two mechanical resonance frequencies, provided both frequency bins are calibrated in the same operating state and likelihood normalization.

This is a useful correction to an overly narrow “two resonances must be 2:1” interpretation. The detector may instead use two Fourier bands of one calibrated broadband channel.

## 4. What this platform partially closes

### Science spectral amplitude / transfer cut — PARTIAL POSITIVE

The measured `chi(omega)` and FDSS provide exactly the type of force-domain quantities needed to construct marginal band rates

`r_n = kappa_PSD |Delta F_n|^2 / S_F,n^eq`.

For a declared `f` and `2f` inside the calibrated sweep, this platform can in principle supply both marginal equivalent-force noise levels and transfer values from one physical force coordinate.

However, the paper does not publish an RQIR-ready joint two-band covariance coefficient `rho`, nor a complete same-window likelihood from which the RQIR correlated two-band Fisher can be reconstructed directly.

### Calibration transduction cut — PARTIAL POSITIVE

The harmonic Coulomb injection is a real physical calibration actuator. It demonstrates a route to measuring transfer amplitude and phase and therefore is directly relevant to the RQIR requirement that calibration Fisher be derived from injected references rather than abstract normalized coordinates.

But one scalar force transfer calibration is not yet the seven source-specific same-time dual-probe `2x2` Fisher blocks required by Iteration 088/APP-003.

### Absolute detector scale `R0` — NOT ROBUSTLY CLOSED

The paper contains enough information to define an absolute force sensitivity spectrum in calibrated operating regimes. But the most attractive high-vacuum feedback-cooled state is precisely where the authors report difficulty in accurately measuring the transfer function because resonant drift and feedback alter the electrical response.

Therefore the best thermal-limit number cannot simply be inserted as the RQIR absolute `R0`.

## 5. RQIR-NG-053 — frequency span is not a simultaneous two-band covariance certificate

A transfer-function sweep covering both `f` and `2f` does not by itself determine the correlated simultaneous science rate

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`.

The missing object is the same-state joint acquisition likelihood or an experimentally justified independence result for the two band estimators.

In particular, a scalar PSD plus sequential transfer sweep does not certify

`rho = 0`.

Finite windows, drift, feedback, crosstalk, leakage and nonstationarity can generate covariance between band estimators even when the nominal frequencies are distinct.

### RQIR-NG-053 — broadband coverage does not imply cross-band independence

Do not replace the missing `rho`/cross-spectral information by zero merely because both frequencies lie in one measured spectrum.

A future certificate may set `rho≈0` only after the same-state acquisition protocol demonstrates the required stationarity/orthogonality or directly estimates the covariance.

## 6. RQIR-NG-054 — transfer calibration must match the science operating state

The Fu experiment explicitly reports that below roughly the low-pressure calibration regime the resonant peak drifts strongly, and that feedback cooling weakens the electrical response used to calibrate the transfer function. The paper therefore does not show FDSS curves for the lowest-pressure states where the transfer calibration is unreliable.

This matters directly for RQIR.

### RQIR-NG-054 — operating-state transduction mismatch

A force ASD or thermal limit measured or inferred in one dynamical state cannot normalize science data taken in another state if feedback, drift, gain or control changes the force-to-output transfer. The transfer/PSD/cross-PSD certificate must be measured in the same science state or linked by an independently calibrated state-transfer model with uncertainty.

This prevents a tempting but invalid combination of the paper’s most favorable high-vacuum thermal limit with a transfer function calibrated in a different control regime.

## 7. RQIR-RESOURCE-053 — force-ASD to science-harmonic threshold

For balanced independent raw science bands (`r2=r4=r`) the Iteration-084 law gives

`r = Z^2/(2 T_sci)`.

With equivalent-force ASD

`A_F = sqrt(S_F)`,

and the retained convention factor `kappa_PSD`,

`r = kappa_PSD |Delta F|^2/A_F^2`.

Therefore the required per-band force harmonic is

`boxed{|Delta F|_req = A_F Z / sqrt(2 kappa_PSD T_sci)}`.

This is a science-only threshold; calibration, source metrology, controls and duty remain additional costs.

Using only the paper’s reported off-resonance **order-of-magnitude** `A_F ~ 1e-17 N/sqrt(Hz)` and setting `kappa_PSD=1` only as a transparent convention slice gives:

- 1 day: `|Delta F|_req ~ 1.203e-19 N` per balanced band;
- 7 days: `~4.546e-20 N`;
- 30 days: `~2.196e-20 N`.

These are not predictions for the Fu apparatus at selected `f,2f` bins because the paper does not provide exact band-specific FDSS values, cross-band covariance, or the full RQIR nuisance likelihood. They are engineering scale transforms of a published ASD order-of-magnitude.

## 8. Comparison with other single-platform anchors — no concatenation

The earlier RQIR external audit retained:

- Piotrowski et al. (2023): simultaneous multimode readout/cooling and measured heterodyne PSDs, but the reported mode frequencies are not a `2:1` pair and no RQIR input-force cross-PSD certificate is supplied;
- Pontin et al. (2026): full optical spectral covariance of a multimode levitated output, but not a calibrated input-referred force matrix for the RQIR template.

A further 2026 levitated two-mode phonon-laser experiment reports simultaneous x/y correlations, displacement calibration, frequencies around `115` and `130 kHz`, and repeated 200-ms cycles, but again does not supply a broadband force-referred RQIR likelihood.

These papers must **not** be spliced with the Fu force ASD. Their role is comparative only: Fu closes more of the force-normalization cut, while the newer multimode experiments close more of the simultaneous-covariance capability cut.

## 9. Certificate status after Iteration 100

For the Fu single platform:

| APP-003 cut | Status |
|---|---|
| factor-two frequency span | **closed as span** for `1–250 kHz` fundamentals |
| marginal force transfer/PSD at both bands | **partially closed** in calibrated regimes |
| simultaneous band covariance `rho` | **open** |
| seven physical calibration blocks | **open**, injection method only partially relevant |
| common absolute `R0` in target high-vacuum science state | **open** because same-state transfer calibration is not closed |
| source `p_E,Omega_E,t_reset,V` / `R_src` | **open** |
| campaign duty/control uncertainty | **open** |
| characterization Fisher rates/floors | **open** |

The key progress is that the external detector problem is now narrower: the factor-two frequency requirement itself is not the main obstacle for a broadband force sensor. The remaining hard detector cuts are **same-state transduction**, **joint band covariance**, and **source-specific calibration Fisher blocks**.

## 10. Next admissible gate

The next highest-value step is to derive a **same-state two-band acquisition certificate** for a broadband force sensor:

1. define the exact finite-time Fourier/window estimators at `f` and `2f`;
2. derive or measure their covariance `rho` from one scalar time series under stationary/cyclostationary assumptions;
3. include transfer-function uncertainty and drift as nuisance parameters rather than treating `chi(f),chi(2f)` as exact;
4. map one harmonic-force injection campaign into Fisher for gain/phase at both bands;
5. determine the minimum number/duration of calibration injections required before transfer uncertainty ceases to dominate `R_beta`.

This is more useful than Toy015 because the newly exposed bottleneck is still apparatus characterization, not source geometry.

## 11. Reproducibility

Code:

`analysis/single_platform_force_certificate_iteration100.py`

The script verifies the factor-two frequency interval of the published 1–500 kHz transfer sweep, reproduces the mature balanced science-rate targets, and maps a declared force ASD to the corresponding science-only harmonic-force threshold while leaving `kappa_PSD` explicit.
