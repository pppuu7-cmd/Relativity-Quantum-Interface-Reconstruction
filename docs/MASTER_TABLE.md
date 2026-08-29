# RQIR Operational Master Table

**Version:** 1.6  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, correlations | ordinary relativistic/control effects | profiled likelihood with explicit calibration | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static density phase blindness; full history becomes tomography | finite NP3 multiprobe calibration + detector transfer | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | response can be projected away; hidden-state amplitude is not self-calibrating; low-rank systematics can destroy identifiability | joint source+calibration+detector Fisher with independent source/control metrology and wall-clock resource accounting | HIGHEST PRIORITY |
| Q4 Gravity-mediated QI | entanglement/non-Gaussianity/scaling | entanglement alone is not unique to quantized gravity | common detector likelihood across interface classes | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise/response spectra | matter, intrinsic-gravity and technical-noise degeneracies | joint N/chi/covariance fit | HIGH PRIORITY |
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
- RQIR-NG-005: if detector signal is `beta*a*s` and hidden state direction obeys `A n=0`, null calibration cannot self-calibrate amplitude `a`; without independent source metrology `F_beta|a=0`.
- RQIR-NG-006: uncontrolled low-rank timing/geometry/additive calibration systematics can remain structurally degenerate with detector-relevant source nuisance, so more gravitational calibration exposure alone does not restore identifiability.

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

The 24 NP3 calibration rows are trace 1, energy 1, potential means 14, symmetrized covariance/noise 8.

Scalar gamma is retained only as a diagnostic proxy. Physical calibration must use `F_C=A^T Sigma_C^-1 A` or repeated-setting Fisher sums.

At detector SNR 5, 90% retention of the hidden preparation-amplitude degree requires `C_a=225`, hence `N_prep=225/xi_prep^2` in standardized single-shot units.

RQIR-CAL-004: conditioning alone is not a sufficient physical-resource proxy.

RQIR-RESOURCE-001: per-shot coherence time and total integration time are distinct resources; for current max phase `4.99085`, `T_coh>=0.7943/f_gap`.

## Critical numerical correction — Iteration 015

Earlier Iterations 013-014 implemented exact trace+energy constraints with a huge Fisher penalty followed by a thresholded pseudoinverse. This created scale separation that truncated genuine weak nuisance directions and artificially inflated profiled `F_beta`.

RQIR-NUM-001: exact constraints must be eliminated analytically through a nullspace/reduced basis rather than approximated by an enormous penalty before pseudoinversion.

Corrected 22D hard-constrained results:

- old Iteration-013 D1 allocation retains only about `0.572`, not 90%; old D2 allocation about `0.481`;
- corrected heterogeneous-allocation cost improvement at 90% is modest: about `x1.07` D1 and `x1.14` D2, not `x6.3/x4.6`;
- corrected q=1 allocation: D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`; D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`;
- the previous Iteration-014 statement that `rho=0.10` common-mode covariance made D2 about `2.13x` more expensive is withdrawn; corrected ratios are about `0.90` D1 and `0.91` D2 for that stress test;
- corrected conservative first-order timing scales are about `9.5 us` D1 and `8.0 us` D2 at `f_gap=100 Hz`.

The conceptual rules RQIR-CAL-005/006 survive, but the old headline numerical gains do not.

## Explicit low-rank systematics — Iteration 016

Four first-order calibration systematics are included explicitly: second-probe drift `delta y`, common timing/phase drift `delta tau`, common mean offset and common covariance offset.

With no independent priors on these amplitudes, `F_beta` collapses to numerical zero for both D1 and D2 even when gravitational calibration exposure is increased by up to `100x`.

A control bundle that restores approximately 90% information is:

D1:
- `sigma(delta tau)~5.95e-3` (`~9.5 us` at 100 Hz);
- `sigma(b_mean)~7.62e-5`;
- `sigma(b_cov)~1.03e-4`.

D2:
- `sigma(delta tau)~5.03e-3` (`~8.0 us` at 100 Hz);
- `sigma(b_mean)~6.44e-5`;
- `sigma(b_cov)~1.04e-4`.

RQIR-CAL-007: calibration exposure and independent control-prior information are distinct, non-interchangeable resources.

RQIR-DRIFT-001: purely multiplicative common gain is first-order suppressed at exact null because `A theta0=0`; this does not protect timing/geometry/additive systematics or nonlinear gain-state products.

## Second-order nonlinear audit — Iteration 017

Timing curvature is subdominant once first-order timing control is satisfied: current-prior quadratic timing bias is only `~3.49e-5 sigma_beta` D1 and `~8.75e-6 sigma_beta` D2.

RQIR-NL-001: current timing curvature is not the bottleneck.

Bilinear common-gain × source-state coupling has local posterior-scale RMS beta-bias coefficient about `0.325 |delta g|`. No global gain-only tolerance exists because contamination scales as `delta g * delta theta`.

RQIR-NL-002: first-order nulling converts standalone control requirements into product-resource requirements when nonlinear coupling is leading.

## Reference-channel and wall-clock layer — Iteration 018

Main file: `docs/REFERENCE_CHANNEL_WALLCLOCK_RESOURCE_BUDGET.md`.

At `f_gap=100 Hz`, the corrected timing priors map to:

- D1 `sigma_t~9.47 us`;
- D2 `sigma_t~8.01 us`.

For white time-jitter ASD integrated over bandwidth `B`, `J_t<=sigma_t/sqrt(B)`. At `1 kHz`, the bookkeeping limits are approximately `0.299 us/sqrtHz` D1 and `0.253 us/sqrtHz` D2. With four independent timing edges, per-edge RMS is approximately `4.73 us` D1 and `4.00 us` D2; correlated timing errors must remain explicit common-mode nuisances.

The current `tau_max=4.99085067` imposes `T_coh,min~7.94 ms` at 100 Hz.

**RQIR-RESOURCE-002:** required coherent evolution is a hard lower bound on physical shot duration for Fisher-per-second accounting.

At detector SNR 5 with standardized `xi_mean=xi_cov=10`, corrected 90%-retention calibration resources correspond to about:

- D1 `7.90e6` accepted-shot equivalents, lower wall-time bound `~17.4 h` at 100 Hz;
- D2 `1.031e7`, lower bound `~22.7 h`.

With `1 ms` extra dead time and `p_success=0.5`, these become approximately `39.3 h` and `51.2 h`. These remain scaling examples, not hardware forecasts.

Preparation-amplitude benchmarks at SNR 5: 80% -> `C_a=100`, `sigma_a=0.10`; 90% -> `225`, `0.0667`; 95% -> `475`, `0.0459`.

For the two-resource limit with detector Fisher rate `R_D` and independent preparation-metrology rate `R_P`, maximizing profiled `F/T` gives

`x_D=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`,

`x_P=sqrt(R_D)/(sqrt(R_D)+sqrt(R_P))`,

and optimal preparation-retention fraction

`r*=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`.

**RQIR-RESOURCE-003:** wall-clock resource allocation follows a square-root Fisher-rate law in this two-resource limit. A fixed 90% preparation-retention constraint is wall-clock optimal only for `R_P/R_D=81`; fixed 80/90/95% tables are benchmark constraints, not universal optimal schedules.

Iteration-017 gain mapping gives local reference SNR about `3.25`, `32.5`, `325` for gain×state bias budgets `0.1`, `0.01`, `0.001 sigma_beta`, respectively, under the local posterior-scale source-error assumption.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## Priority ranking v1.6

1. **Branch-specific Fisher rates:** replace standardized `xi` by D1 phase-shot/contrast/four-switch/dead-time and D2 force-PSD/integration/duty-cycle models; assign explicit source-metrology rate.
2. **Full wall-clock objective:** optimize detector + preparation + gravitational calibration + reference-control `F_beta|theta/T_wall`; use RQIR-RESOURCE-003 as the two-resource regression limit.
3. **Common D1/D2 resource budget:** one source mass, gap, coherence, separation and integration budget.
4. **Interface-class fingerprints:** semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
5. **Relativistic/full-stress embedding:** after detector/inference geometry stabilizes, close conservation, gauge and renormalization gates.
