# RQIR Operational Master Table

**Version:** 1.7  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, correlations | ordinary relativistic/control effects; long-run clock drift | profiled likelihood + Allan/PSD control model | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static-density blindness; full history becomes tomography | finite NP3 calibration + detector transfer | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded/ordered response | hidden-amplitude non-identifiability; calibration nuisance; low-frequency drift | joint source+calibration+detector Fisher with independent source/control metrology and wall-clock budget | HIGHEST PRIORITY |
| Q4 Gravity-mediated QI | entanglement/non-Gaussianity/scaling | entanglement alone is not unique to quantized gravity | common detector likelihood across interface classes | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise/response spectra | matter, intrinsic-gravity and technical-noise degeneracies | joint N/chi/covariance fit | HIGH PRIORITY |
| Q6 Causal/process | relational timing/process observables | control-system nonclassicality | gravity-dependent scaling with nuisance closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | tiny universal pieces and local-UV degeneracy | cross-process long-range/nonanalytic fingerprints | OPEN |

## Current mathematical coordinate

`K_T^(2)=(<T>,N,D or chi^R)` with Schwinger-Keldysh/CTP parent functional. Operator ordering remains explicit.

## Retained closed/negative results

- RQIR-NG-001: static density phase blindness.
- RQIR-NG-002: minimal response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response.
- PE-1 / Toy005: exact Newtonian one-channel embedding; NP2 only.
- RQIR-NG-003: generic complete density history becomes tomography.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace.
- RQIR-NG-005: gravitational exact-null calibration cannot self-calibrate the amplitude of the hidden source direction; without independent source metrology `F_beta|a=0`.
- RQIR-NG-006: uncontrolled low-rank timing/geometry/additive systematics can remain structurally degenerate with detector-relevant nuisance; more gravitational exposure alone does not cure this.
- RQIR-NG-007: if the Allan/flicker floor plus immediate reference variance exhausts the detector-required nuisance prior, repeated fast sampling and finite recalibration cadence cannot satisfy the requirement.

## Current source/calibration baseline

Toy009 source radii approximately `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Iteration-011 balanced calibration remains the practical geometry baseline:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- positive states;
- selected equality residual `<1e-15`;
- `eta_R~0.573426`;
- `s_min~1.99954e-3`;
- condition `~2313`.

RQIR-DESIGN-001: optimize `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`.

RQIR-CAL-002: calibration geometry is an active information/design resource.

## Mandatory numerical correction

RQIR-NUM-001: exact constraints must be eliminated analytically through a nullspace/reduced basis rather than approximated by huge Fisher penalties before pseudoinversion.

Corrected 90%-retention row weights:

- D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`;
- D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`.

Old Iteration-013/014 headline gains based on the penalty+pseudoinverse implementation are withdrawn.

## Detector-level/systematics requirements

Current first-order timing priors from the corrected low-rank Fisher:

- D1 `sigma_t~9.47 us` at 100 Hz;
- D2 `sigma_t~8.01 us`.

Additive row-normalized controls:

- D1 `sigma(b_mean)~7.62e-5`, `sigma(b_cov)~1.03e-4`;
- D2 `sigma(b_mean)~6.44e-5`, `sigma(b_cov)~1.04e-4`.

RQIR-CAL-007: exposure and independent control-prior information are non-interchangeable resources.

RQIR-DRIFT-001: pure common multiplicative gain is first-order suppressed at exact null; leading gain contamination is product-like.

RQIR-NL-001: timing curvature is negligible after current first-order timing control.

RQIR-NL-002: leading gain contamination scales with `delta_g * delta_theta`; no global gain-only tolerance exists.

## Physical resource stack

RQIR-RESOURCE-001: coherence time and total integration time are distinct.

RQIR-RESOURCE-002: required coherent evolution is a hard lower bound on shot duration.

RQIR-RESOURCE-003: in the two-resource detector/preparation limit, wall-clock allocation follows the square-root Fisher-rate law; fixed 90% retention is not universal.

RQIR-RESOURCE-004: D1 vs D2 cannot be globally ranked without native Fisher rates and explicit noise models.

RQIR-RESOURCE-005: dimensionless calibration Fisher weights cannot be converted to hours without measurement-level Fisher rates.

RQIR-RESOURCE-006: nuisance normalization cannot create physical wall-time cost; use event precision, transduction, acceptance/cycle, PSD/bandwidth and physical priors.

## Branch-specific detector/preparation rates

D1: binary phase/interference readout with contrast/control-window/coherence/dead-time model. Detector acquisition can require millions of accepted events for mrad-scale final phase precision; do not confuse final phase error with single-event noise.

D2: equivalent-force PSD/live-integration model with `R_D2=eta_duty*4 r2 r4/(r2+r4)`, `r_n=|Delta F_n|^2/S_F,n`.

Source preparation: for `rho(a)=I/5+a Delta0` with `[rho,Delta0]=0`, `F_Q(a~0.08)~13.2707` per ideal accepted copy. At detector SNR 5, 90%-retention `C_a=225` is only about 17 ideal accepted copies at the QFI bound.

RQIR-PREP-001: RQIR-NG-005 is channel-specific, not absence of source-state information in principle.

## Native calibration/reference rates

D1 mean row: `R_M,i=p_acc C_i^2 k_i^2/t_cycle`.

Gaussian covariance/log-PSD row: `R_C~duty*B*k_C^2`.

D2 mean row: one-sided force-template Fisher `I_i=4 int |dh_i/du_i|^2/S_F df`.

Timing reference: `T_tau=t_cycle/p_acc*(sigma_event/sigma_target)^2` after consistent unit conversion.

RQIR-DRIFT-002: high-rate white timing statistics do not certify long-campaign stability.

## Iteration 023 — colored drift / Allan cadence

For immediate reference variance `sigma_ref^2`, random-walk diffusion `D` and Allan/flicker floor `sigma_floor`, the interval-averaged residual is

`<sigma^2>=sigma_floor^2+sigma_ref^2+D Delta/2`.

Hence

`Delta_max=2(sigma_target^2-sigma_floor^2-sigma_ref^2)/D`,

if the numerator is positive.

RQIR-DRIFT-003: long-campaign control is governed by low-frequency stability `(D,sigma_floor)` or the measured Allan-deviation curve plus recalibration duty, not per-event precision alone.

Transparent timing benchmark with `sigma_event=10 us`, `sigma_ref=sigma_target/3`:

- reference blocks: `~0.1795 s` D1, `~0.2509 s` D2;
- `D=100 us^2/h`: cadence `~1.594 h` D1, `~1.141 h` D2;
- `D=1000 us^2/h`: `~9.57 min` D1, `~6.84 min` D2;
- equal-diffusion cadence ratio D2/D1 `~0.715`.

These are parametric benchmarks, not hardware predictions.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## Priority ranking v1.7

1. **Measured/justified stability models:** obtain D1 clock/control and D2 sampling/reference Allan/PSD parameters; convert additive-offset nuisance coordinates to physical detector units.
2. **Full wall-clock objective:** insert drift cadence and reference-control duty into the corrected Iteration-021 `F_beta|theta/T_wall` optimizer.
3. **Common D1/D2 resource budget:** one source mass, gap, coherence, separation and campaign duration.
4. **Interface-class fingerprints:** propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
5. **Relativistic/full-stress embedding:** close conservation, gauge and renormalization gates after detector/inference geometry stabilizes.
