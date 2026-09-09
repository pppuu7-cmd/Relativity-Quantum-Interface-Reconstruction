# RQIR7 — same-apparatus atom-gravimeter closure

**Date:** 2026-09-09  
**Branch:** `main`  
**Code authority:** `analysis/atom_gravimeter_same_apparatus_resource_closure_audit.py`

## Purpose

Close the next strengthened Paper-III gate with one real physical atom interferometer rather than dimensionless surrogate units. The question is whether a modulated acceleration-like RQIR science amplitude remains estimable after simultaneous profiling of scale, offset, drift and correlated noise, once the model is tied to a published apparatus and a physically realizable acceleration-reference path.

## Physical apparatus anchor

The audit uses the SYRTE compact 87Rb Raman gravimeter reported by J. Le Gouet et al., *Applied Physics B* 92, 133-144 (2008), arXiv:0801.1270, together with the measured/theoretical sensitivity-function formalism of P. Cheinet et al., *IEEE Transactions on Instrumentation and Measurement* 57, 1141-1148 (2008), arXiv:physics/0510197.

Published anchors used in the code:

- wavelength approximately 780 nm;
- three-pulse acceleration scale `phi = k_eff a T^2` at low frequency;
- total interferometer time `2T = 100 ms`, hence `T = 50 ms`;
- repetition rate `f_c = 4 Hz`, so `T_c = 0.25 s`;
- Raman pulse duration approximately `10 us` for the low-noise gravimeter;
- best measured short-term phase noise `11 mrad/shot`;
- best measured short-term acceleration sensitivity `1.4e-8 g at 1 s`;
- vibration correction via a low-noise seismometer placed with the retroreflection mirror;
- the same apparatus was deliberately driven at selected frequencies while atomic and seismometer signals were recorded, providing a physical route to an injected acceleration-reference calibration rather than an abstract nuisance prior.

The Cheinet sensitivity-function result supplies the low-frequency transfer geometry. For a sinusoidal acceleration, the normalized three-pulse acceleration response used here is

`R_a(f) = [sin(pi f T)/(pi f T)]^2 = sinc(f T)^2`.

At the audit design frequencies, `R_a(0.5 Hz) = 0.9979455` and `R_a(1 Hz) = 0.9918023`, so the chosen modulation bands remain essentially in the DC acceleration-response regime.

## Internal reproduction check

Using `lambda = 780 nm`, counter-propagating `k_eff = 4 pi/lambda`, `T = 50 ms`, and `g0 = 9.80665 m/s^2`, the audit obtains

- `k_eff = 1.61107316e7 1/m`;
- `k_eff T^2 = 4.02768289e4 rad/(m/s^2)`;
- `k_eff T^2 g0 = 3.94980764e5 rad/g`;
- duty fraction `2T/Tc = 0.4`;
- `11 mrad/shot -> 1.39247e-8 g at 1 s` for a 4-Hz cycle.

Thus the numerical scale independently reproduces the paper's quoted `1.4e-8 g at 1 s` to rounding accuracy. It also gives `1 mrad/shot -> 1.266e-9 g at 1 s`, consistent with the published approximate `1.2e-9 g at 1 s` conversion.

## Same-apparatus nuisance model

The phase model profiles simultaneously:

- science acceleration amplitude `theta`;
- common multiplicative acceleration-scale/readout nuisance `gamma`;
- phase offset;
- linear drift;
- quadratic drift;
- optional unknown reference amplitude `alpha`;
- correlated shot noise.

The covariance diagonal is fixed to the actually measured `11 mrad/shot`. Because the publication does not provide a machine-readable full covariance matrix, off-diagonal covariance is stress-tested with an AR(1) family `rho = 0, 0.3, 0.6, 0.9`. These off-diagonal models are deliberately labelled stress models, not measured covariance claims.

A design reference of `1 micro-g` at 1 Hz is used only as a calculational calibration injection. It produces about `0.392 rad`, deliberately below the order-one-radian excursion scale discussed for the apparatus. The amplitude is a design choice, not a value claimed to have been used in the 2008 experiment.

## Gate results

For a 60-s campaign (`240` shots) with `rho=0.3`:

| Case | Fisher result | Science sigma |
|---|---|---:|
| static science + known reference | `FAIL`, rank 4/5 | infinite |
| modulated science, no calibrated reference | `FAIL`, rank 4/5 | infinite |
| modulated science + known reference | `PASS`, rank 5/5 | `2.980 ng` |
| modulated science + unknown unconstrained reference | `FAIL`, rank 5/6 | infinite |
| modulated science + 0.1% reference prior | `PASS`, rank 6/6 | `2.980 ng` |

The failures are scientifically useful:

1. a static acceleration-like science signal is absorbed by the free phase offset;
2. modulation by itself does not repair an absolute common-scale degeneracy;
3. an unconstrained reference amplitude simply moves the scale degeneracy into the science/reference ratio;
4. a finite calibrated reference restores nonzero information on `theta`.

## Physical resource forecast

With the measured 11-mrad shot RMS and a 0.1% finite reference-amplitude prior, the profiled science uncertainty is:

| AR(1) rho | 60 s | 600 s | 3600 s |
|---:|---:|---:|---:|
| 0.0 | 2.548 ng | 0.806 ng | 0.329 ng |
| 0.3 | 2.980 ng | 0.942 ng | 0.385 ng |
| 0.6 | 2.855 ng | 0.901 ng | 0.368 ng |
| 0.9 | 1.520 ng | 0.479 ng | 0.196 ng |

The non-monotonic dependence on positive `rho` is expected for a fixed marginal variance because the chosen science modulation sits away from DC; an AR(1) process redistributes spectral power rather than simply multiplying all frequencies by one penalty. The important structural result is that the effective science information remains strictly nonzero throughout the stress family.

## Decision

**SAME-APPARATUS ACCELERATION INFORMATION AFTER SIMULTANEOUS NUISANCE PROFILING: PASS.**

This materially advances the strengthened Paper-III branch because the Fisher geometry is now tied to a real `T`, `Tc`, pulse scale, acceleration transfer function, measured phase-noise amplitude, dead time/duty cycle and a physically realizable same-apparatus reference-injection path.

It does **not** yet justify full Paper-III apparatus closure. The remaining decisive authorities are:

- measured or defensibly digitized PSD/cross-PSD for the actual campaign rather than an AR(1) stress family;
- explicit contrast/readout-gain evolution in the joint likelihood;
- a measured finite uncertainty for the injected acceleration-reference metrology rather than a design prior;
- source preparation / modulation implementation and its duty-cycle cost;
- one final joint campaign likelihood/certificate using those quantities.

## Readiness consequence

The previous strict Paper-III score of `58%` was set before any same-apparatus pulse/transfer/dead-time/noise-amplitude forecast existed. This iteration closes enough of that missing layer to justify a conservative promotion to **64% strengthened apparatus-specific readiness**.

The whole RQIR programme/model score should move only slightly, from approximately `69%` to approximately **70%**, because Papers I-II were already closed and Paper IV remains blocked at the physical comparator-residual prerequisite. Candidate-Gravity groundwork remains `24%` and Paper V remains unauthorized until Paper IV returns `NEW_REQUIRED`.

## Next gate

The highest-value next action is no longer another abstract Fisher variant. It is to replace the synthetic off-diagonal covariance family with a source-traceable physical noise budget / PSD representation from the chosen apparatus (or a later compatible apparatus with machine-readable spectral data), include contrast/reference-metrology uncertainty explicitly, and re-run the same profiled science-information test as a single campaign closure.
