# RQIR Operational Master Table

**Version:** 1.2  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, correlations | ordinary relativistic/control effects | profiled likelihood with explicit calibration | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static density phase blindness; full history becomes tomography | finite NP3 multiprobe calibration + detector transfer | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | response can be projected away by calibration/detector geometry; hidden-state amplitude is not self-calibrating | joint source+calibration+detector Fisher optimization with independent source metrology | HIGHEST PRIORITY |
| Q4 Gravity-mediated QI | entanglement/non-Gaussianity/scaling | entanglement alone is not unique to quantized gravity | common detector likelihood across interface classes | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise/response spectra | matter, intrinsic-gravity and technical noise degeneracies | joint N/chi/covariance fit | HIGH PRIORITY |
| Q6 Causal/process | relational timing/process observables | control-system nonclassicality | gravity-dependent scaling with nuisance closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | tiny universal pieces and local-UV degeneracy | cross-process long-range/nonanalytic fingerprints | OPEN |

## Mathematical coordinate

`K_T^(2)=(<T>,N,D or chi^R)` with Schwinger-Keldysh/CTP parent functional. Operator ordering remains explicit.

## Retained closed/negative results

- RQIR-NG-001 / Toy002: static density phase blindness.
- RQIR-NG-002 / Toy003: minimal response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response.
- PE-1 / Toy005: exact Newtonian one-channel embedding; still NP2.
- RQIR-NG-003 / Toy006: generic complete density history becomes state tomography.
- Toy007: first finite NP3.
- RQIR-NG-004: one extra independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivates likelihood/Fisher over maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under stated assumptions.
- RQIR-NG-005: if detector signal is `beta*a*s` and the hidden state direction obeys `A n=0`, gravitational null calibration cannot self-calibrate amplitude `a`; without independent source metrology `F_beta|a=0`.

## Current source/calibration baseline

Toy009 source radii approximately `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Iteration-011 balanced calibration:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- positive states;
- exact selected equality residual `<1e-15`;
- `eta_R~0.573426`;
- `s_min~1.99954e-3`;
- condition `~2313`;
- cumulative ideal detector-source gains vs Toy007 roughly D1 `x2.11`, D2 `x2.36`.

RQIR-DESIGN-001: optimize `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`.

RQIR-CAL-002: calibration geometry is an active information resource.

## Physical resource layer — Iteration 012

The 24 NP3 calibration rows consist of trace 1, energy 1, potential means 14, symmetrized covariance/noise 8.

Scalar gamma is retained only as a diagnostic proxy. Physical calibration must use `F_C=A^T Sigma_C^-1 A` or repeated-setting Fisher sums.

At detector SNR 5, 90% retention of the hidden preparation-amplitude degree requires `C_a=225`, hence `N_prep=225/xi_prep^2` in standardized single-shot units.

RQIR-CAL-004: conditioning alone is not a sufficient physical-resource proxy.

RQIR-RESOURCE-001: per-shot coherence time and total integration time are distinct resources; for current max phase `4.99085`, `T_coh>=0.7943/f_gap`.

## Heterogeneous calibration allocation — Iteration 013

Main file: `docs/HETEROGENEOUS_CALIBRATION_FISHER_ALLOCATION.md`.

Replace scalar gamma by separate potential-mean and covariance information weights:

`F_C=F_trace+energy + gamma_m M_m + gamma_c M_c`.

For per-shot informations `q_m,q_c`, standardized cost is

`14 gamma_m/q_m + 8 gamma_c/q_c`.

At 90% retained detector information and `q_c/q_m=1`:

- D1 uniform weight `~1.54e6`; optimized `gamma_m~1.82e5`, `gamma_c~3.49e5`; cost reduction `~6.3x`.
- D2 uniform weight `~2.14e6`; optimized `gamma_m~1.7e5`, `gamma_c~1.0e6`; cost reduction `~4.6x`.

The optimum changes strongly with covariance-shot efficiency and is different for D1 and D2.

### RQIR-CAL-005

At fixed likelihood and calibration operator set, resource-optimal calibration allocates Fisher information according to downstream nuisance-projection leverage and per-shot information cost. Equal precision on all calibration observables is generally not optimal. Scope: current finite-dimensional model.

### Negative design result

There is no detector-independent optimal calibration schedule for the same source and NP3 observable set. Calibration cannot be finalized before detector branch and covariance are declared.

## Correlated calibration covariance and drift — Iteration 014

Main file: `docs/CORRELATED_CALIBRATION_COVARIANCE_AND_DRIFT.md`.

Class-wise compound-symmetry covariance stress tests show detector-specific sensitivity to correlated calibration noise while holding marginal row variance fixed.

At 90% retained detector information:

- D1 cost ratios relative to uncorrelated are about `0.998`, `0.991`, `0.986` for `rho=0.01,0.05,0.10`.
- D2 ratios are about `1.019`, `1.191`, `2.129` for the same correlations.

### RQIR-CAL-006

Correlation cannot be summarized by one scalar degradation factor. Its effect depends on alignment of calibration-covariance eigendirections with detector-relevant nuisance tangents. Moderate common correlation is nearly harmless for the current D1 design but materially costly for D2.

Slow-drift derivative norms for the exact-null state in row-normalized coordinates:

- second-probe position: `~2.91e-4`;
- common source phase/time: `~2.56e-2`.

With Iteration-013 q=1 allocations and a conservative 10%-of-statistical-sigma drift budget:

- D1 `|delta tau| <~1.63e-2`;
- D2 `|delta tau| <~9.63e-3`.

At `f_gap=100 Hz`, these correspond to about `26 us` and `15 us` respectively.

### RQIR-DRIFT-001

Purely multiplicative common calibration gain is first-order suppressed at the exact null because `A theta0=0`. Geometry/time drift is not protected; additive offsets and second-order gain-state coupling remain open.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## Priority ranking v1.2

1. **Explicit low-rank drift nuisance:** replace fixed covariance stress test by finite-prior drift Fisher; add additive offsets and second-order gain-state coupling; determine prior/control information needed for 90% D1/D2 retention.
2. **D1 timing/control budget:** pulse-clock jitter, finite bandwidth, contrast/dead time, preparation/reset success and independent source metrology.
3. **D2 physical PSD model:** thermal force, backaction, displacement imprecision; compare one-mode, dual-mode and tuned strategies.
4. **Common D1/D2 resource budget:** one source mass, gap, coherence, separation and integration budget.
5. **Interface-class fingerprints:** semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
6. **Relativistic/full-stress embedding:** after detector/inference geometry stabilizes, close conservation, gauge and renormalization gates.
