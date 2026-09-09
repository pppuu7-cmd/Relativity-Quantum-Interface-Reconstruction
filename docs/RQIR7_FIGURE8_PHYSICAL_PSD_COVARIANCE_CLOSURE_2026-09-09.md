# RQIR7 — Figure-8 physical PSD/covariance closure

**Date:** 2026-09-09  
**Code authority:** `analysis/atom_gravimeter_figure8_psd_covariance_audit.py`

## Objective

Replace the synthetic AR(1) off-diagonal covariance used in the first same-apparatus Paper-III audit with a source-traceable physical colored-noise covariance derived from the published SYRTE atom-gravimeter vibration spectrum.

## Source authority

Primary apparatus/noise source:

J. Le Gouet et al., *Limits to the sensitivity of a low noise compact atomic gravimeter*, Applied Physics B 92, 133-144 (2008), arXiv:0801.1270.

The paper provides all of the following independent constraints used here:

- Fig. 8: measured acceleration amplitude spectral density of the passive isolation platform, active platform and ground;
- Eq. (15): vibration-noise propagation through the atom-interferometer transfer function;
- inferred passive-platform vibration limit `6.5e-8 g at 1 s` and night value `5e-8 g at 1 s`;
- atom/seismometer correlation coefficient up to `0.94` in low-noise conditions;
- vibration-correction rejection efficiency approximately `3`, giving a typical corrected sensitivity `2e-8 g at 1 s`;
- best total phase noise `11 mrad/shot`;
- independently evaluated quadrature sum of other noise sources approximately `4 mrad/shot`;
- broad residual/crosstalk feature around `2 Hz`; horizontal acceleration noise reaches `6e-7 g/Hz^1/2` there and the authors infer few-percent horizontal-to-vertical crosstalk.

The corresponding three-pulse sensitivity-function formalism remains anchored to P. Cheinet et al., IEEE TIM 57, 1141-1148 (2008), arXiv:physics/0510197.

## PSD provenance rule

The code contains a coarse human-readable log-log digitization of the **passive-platform** curve in Fig. 8. It is explicitly labelled an approximate digitization, not raw data. No amplitude fitting to the paper's integrated sensitivity is performed.

The continuous acceleration ASD is propagated through

`R_a(f) = sinc(f T)^2`

and the one-sided phase PSD is converted directly into sampled shot covariance via

`C_l = integral S_phi(f) cos(2 pi f l T_c) df`.

Because the covariance is evaluated at actual shot separations, continuous-frequency aliasing into the sampled sequence is contained in the covariance rather than replaced by an arbitrary AR coefficient.

## Independent source reproduction

The coarse Fig.-8 trace predicts, without normalization,

- **uncorrected vibration sensitivity:** `6.3486e-8 g at 1 s`;
- published inferred value: `6.5e-8 g at 1 s`;
- relative mismatch: **2.33%**.

Applying the paper's factor-3 vibration rejection and adding the paper's independent `4 mrad/shot` non-vibration budget in quadrature/covariance gives

- **predicted typical corrected sensitivity:** `2.1759e-8 g at 1 s`;
- published typical corrected value: `2e-8 g at 1 s`;
- relative mismatch: **8.8%**.

This is the key authority upgrade: the spectrum shape and absolute amplitude reproduce two independent integrated apparatus-level scales without being tuned to either one.

## Fisher / nuisance result

The same RQIR science design used in the first same-apparatus audit is re-run with this physical Toeplitz covariance while simultaneously profiling

- common multiplicative scale/readout gain;
- phase offset;
- linear drift;
- quadratic drift;
- optional reference amplitude.

For a 60-s campaign:

| Case | Result |
|---|---|
| static science + calibrated reference | **FAIL** — science absorbed by free offset |
| modulated science, no calibrated reference | **FAIL** — absolute scale degeneracy |
| modulated science + known reference | **PASS**, full local science rank |
| modulated science + unknown unconstrained reference | **FAIL** |
| modulated science + finite reference prior | **PASS** |

For the nominal physical PSD and a 0.1% reference-prior demonstration:

- `60 s`: `sigma_theta = 5.723 ng`;
- `600 s`: `sigma_theta = 1.845 ng`;
- `3600 s`: `sigma_theta = 0.764 ng`.

These uncertainties are worse than the earlier AR(1) toy-covariance forecast, as they should be: the physical spectrum carries concentrated colored vibration power. The structural PASS nevertheless survives.

## Crosstalk stress

Because the publication identifies an incompletely rejected broad feature near 2 Hz, the audit applies a smooth one-octave stress centered on 2 Hz. For 60 s:

| 2-Hz ASD boost | sigma_theta |
|---:|---:|
| x1 | `5.72 ng` |
| x2 | `6.58 ng` |
| x3 | `7.48 ng` |
| x5 | `9.31 ng` |

Science estimability survives every tested stress. Thus the previous PASS is not an artifact of assuming short-memory AR(1) noise.

## Reference-metrology interpretation

The same paper reports that the two seismometer outputs are in phase at low frequency and that their scale-factor difference is below 1%, and separately shows that the measured seismometer transfer function agrees well with its specified response. This makes percent-level finite reference-transfer uncertainty physically plausible, but it is **not** a certified absolute uncertainty on the proposed injected acceleration amplitude. Therefore the current audit treats reference priors only as sensitivity studies and does not declare the reference-metrology gate fully closed.

## Decision

**SOURCE-TRACEABLE PHYSICAL PSD/COVARIANCE GATE: PASS.**

More specifically:

- physical PSD shape: PASS;
- independent integrated vibration-scale reproduction: PASS;
- published factor-3 correction-scale reproduction with the independent 4-mrad budget: PASS;
- science identifiability under physical colored covariance: PASS;
- robustness to enlarged 2-Hz crosstalk: PASS;
- raw machine-readable campaign PSD/cross-PSD: not available / not closed;
- certified absolute reference-metrology uncertainty: OPEN;
- explicit contrast/readout evolution in the joint likelihood: OPEN;
- final end-to-end campaign certificate: OPEN.

## Readiness consequence

Paper III was `64%` after the first same-apparatus audit. Closing the physical colored-covariance authority is a material step, but the absence of raw cross-spectral data and certified reference/contrast metrology prevents a near-complete score. The strengthened Paper-III readiness is therefore promoted conservatively to **68%**.

The overall RQIR programme/model readiness moves from approximately `70%` to approximately **71%**. Paper IV remains the dominant programme bottleneck, so no larger programme-level promotion is justified.

## Next gate

The strongest next task is to close the **reference/contrast campaign layer** rather than create more generic covariance variants:

1. formulate the observable as transition probability `P = (1 + C cos Phi)/2` rather than phase-only Gaussian data;
2. introduce finite contrast `C`, contrast drift and readout-gain nuisance;
3. use the paper's mid-fringe constraint and measured detection-noise scale;
4. propagate a conservative percent-level reference-transfer uncertainty and determine the statistical-to-calibration transition;
5. test whether `theta` remains estimable in that nonlinear detector-facing likelihood.

If this passes, Paper III can reasonably move into the low/mid-70% strengthened range before a final raw-data/cross-PSD campaign certificate.