# RQIR7 — detector-facing transition-probability likelihood closure

**Date:** 2026-09-09  
**Code authority:** `analysis/atom_gravimeter_detector_facing_probability_likelihood_audit.py`

## Objective

Advance strengthened Paper III from a phase-Gaussian Fisher model to the actual atom-interferometer detector observable

`P = (1 + C cos Phi)/2`

and determine whether the RQIR science amplitude remains estimable after simultaneous profiling of phase, contrast and readout nuisances under the source-traceable physical colored covariance established in the preceding Figure-8 audit.

## Source anchors

The detector model is tied to J. Le Gouet et al., *Limits to the sensitivity of a low noise compact atomic gravimeter*, Applied Physics B 92, 133-144 (2008), arXiv:0801.1270.

The publication states that:

- transition probability is characterized at mid-fringe `P=0.5`;
- for atom number above about `5e6`, technical detection noise limits the probability standard deviation to approximately `sigma_P = 3e-4`;
- probability noise converts to phase noise as `sigma_phi = 2 sigma_P / C`;
- sensitivity close to `1 mrad/shot` can be achieved from the detection system;
- post-correction on transition probability requires operation near mid-fringe, peak-to-peak phase fluctuations below a few tens of degrees and stable contrast.

Combining `sigma_P ~ 3e-4` with the stated near-`1 mrad` detector phase sensitivity implies an effective working contrast near

`C ~ 2 sigma_P / sigma_phi ~ 0.6`.

This is used as an approximate source-derived working anchor, not claimed as an independently quoted contrast measurement.

## Detector-facing likelihood

For each shot,

`P_i = 1/2 + b + G_i [ (1/2)(1 + C_i cos Phi_i) - 1/2 ]`,

where the centered readout definition prevents the fixed population baseline from trivially calibrating gain.

The nuisance set is deliberately larger than in the phase-only audit:

- RQIR science acceleration amplitude `theta`;
- common acceleration/phase scale `gamma`;
- phase offset;
- linear phase drift;
- quadratic phase drift;
- absolute contrast;
- linear contrast drift;
- quadratic contrast drift;
- centered probability readout gain;
- linear readout-gain drift;
- probability readout offset;
- injected reference amplitude `alpha` when it is not externally fixed.

The probability covariance is not approximated by a white Gaussian phase error. The already validated physical phase covariance `C_phi` is propagated through the local nonlinear fringe slope:

`C_P = D C_phi D + sigma_P^2 I`,

with

`D_ii = dP_i/dPhi_i`.

Because the reference phase varies shot-to-shot, `D` is not constant and the resulting probability covariance is not Toeplitz. The code therefore applies it as a linear operator and solves `C_P^-1 J` iteratively, while the underlying phase covariance remains the source-traceable Toeplitz covariance from the published vibration spectrum.

To stay conservative, the Fisher calculation freezes the covariance at the nominal/stress point and uses **mean information only**. It does not gain science information from parameter-dependence of the noise amplitude.

## Structural gate

For a 60-s campaign:

| Case | Result |
|---|---|
| static science + finite reference prior | **FAIL** — science remains absorbed by free phase offset |
| modulated science, no acceleration reference | **FAIL** — absolute scale degeneracy |
| modulated science + unknown uncalibrated reference | **FAIL** |
| modulated science + finite reference calibration | **PASS** |

With finite reference calibration, the normalized Fisher matrix remains rank deficient because contrast and centered readout gain contain apparatus-only degeneracies. Crucially, every surviving null direction is orthogonal to `theta`: full apparatus identifiability is therefore not required for science estimability.

For the nominal detector state at `theta=1 ng`:

- `60 s`: `sigma_theta ~ 5.728 ng`;
- `600 s`: `sigma_theta ~ 1.829 ng`.

At this small science/reference ratio, changing the reference prior from 10% to 0.1% barely changes the statistical uncertainty because the multiplicative calibration floor scales with the true science amplitude.

## Detector nuisance stress

The same 60-s gate was evaluated at nonzero detector nuisance truth values, including:

- 20% reduction in contrast (`C=0.48`);
- 10% linear contrast drift;
- 10% quadratic contrast drift;
- 5% linear readout-gain drift;
- phase offset/drift at the `0.1-0.2 rad` scale, within the source-described few-tens-of-degrees post-correction regime;
- a combined stress containing lower contrast, contrast drift, gain drift and phase offset/linear/quadratic drift simultaneously.

`theta` remains estimable in every tested case. The combined stress gives approximately `sigma_theta = 5.732 ng` at 60 s, compared with `5.728 ng` nominal.

The weak dependence is physically sensible rather than suspicious: in this regime the dominant correlated phase noise and the phase science signal are multiplied by nearly the same local fringe slope, whereas the independent detector floor `sigma_P=3e-4` corresponds to only about `1 mrad` at `C~0.6`, below the several-mrad non-vibration plus residual-vibration phase scale already present in the physical covariance.

## Detector-facing calibration floor

The finite reference uncertainty reproduces the expected multiplicative calibration law in the full probability likelihood. At `theta=100 ng`, the near-statistical baseline is `sigma_stat ~ 5.755 ng`, and the calculation follows

`sigma_theta^2 ~= sigma_stat^2 + (theta f_ref)^2`,

where `f_ref` is the fractional reference-amplitude uncertainty.

Examples for 60 s:

| reference uncertainty | Fisher sigma_theta | quadrature law |
|---:|---:|---:|
| 10% | `11.538 ng` | `11.538 ng` |
| 3% | `6.490 ng` | `6.490 ng` |
| 1% | `5.841 ng` | `5.841 ng` |
| 0.3% | `5.763 ng` | `5.763 ng` |
| 0.1% | `5.756 ng` | `5.756 ng` |

The numerical agreement is essentially machine precision. This is useful because it exposes the calibration/statistics crossover directly in the detector-facing model rather than relying on the earlier abstract resource law.

At 60 s the crossover science amplitude is approximately

`theta_cross ~= sigma_stat / f_ref`.

Thus a 10% reference uncertainty becomes calibration-dominant around `~58 ng`, a 1% uncertainty around `~0.58 micro-g`, and a 0.1% uncertainty around `~5.8 micro-g` for this particular resource point.

## Decision

**NONLINEAR DETECTOR-FACING TRANSITION-PROBABILITY GATE: PASS.**

More specifically:

- source-grounded probability detection noise: PASS;
- source-derived working contrast scale: PASS as an approximate anchor;
- physical colored phase covariance propagated into probability space: PASS;
- contrast and contrast-drift profiling: PASS;
- readout-gain/gain-drift/offset profiling: PASS;
- finite-reference calibration law: PASS;
- apparatus-only null modes correctly separated from science estimability: PASS;
- uncalibrated absolute reference: FAIL by construction, as required;
- certified real injected-reference metrology: OPEN;
- raw shot-level population/contrast time series: OPEN;
- source/modulation implementation and final campaign certificate: OPEN.

## Readiness consequence

This closes the principal detector-facing nuisance layer identified at the previous 68% Paper-III state. It does not close the final experiment because the proposed acceleration reference still lacks a certified measured absolute transfer uncertainty and the calculation does not possess raw shot-level atom populations / contrast or cross-spectral campaign data.

A conservative strengthened Paper-III readiness after this gate is therefore **74%**.

The whole RQIR programme/model readiness moves only from approximately `71%` to approximately **72%**, because Paper IV remains blocked upstream of the terminal comparator decision and continues to dominate programme-level completion.

## Next gate

The strongest remaining Paper-III task is now an **end-to-end campaign certificate**, not another generic nuisance variant. Its required ingredients are:

1. choose/freeze an experimentally realizable reference-injection protocol;
2. assign a source-grounded absolute uncertainty to its acceleration amplitude / transfer;
3. include modulation/reference shots in the duty-cycle/resource ledger;
4. if obtainable, replace the coarse Fig.-8 trace with raw or digitized campaign cross-spectral information and raw contrast/population evolution;
5. produce one joint certificate containing science estimability, calibration floor, exposure time, failure domains and provenance.

Passing that layer would justify moving strengthened Paper III from the mid-70% range toward final scientific closure.