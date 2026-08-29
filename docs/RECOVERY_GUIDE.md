# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v1.6

This file is the continuity backbone. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem: `P_data(o|s) -> [interface class]`.

Rules: observable first; explicit baseline/domain; preserve operator ordering; retain negative/correction results; source response is not detector observability; exact nulls are not statistical identifiability; every numerical result gets reproducibility code; no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

## 2. Ordered source hierarchy

At second order `K_T^(2)=(<T>,N,D or chi^R)`, with symmetrized noise `N`, ordered/commutator response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger-Keldysh/CTP generating functional.

Working channels: Q1 clocks; Q2 superposed sources; Q3 backreaction/source rule; Q4 gravity-mediated quantum information; Q5 geometry fluctuations; Q6 causal/process structure; Q7 low-energy QG EFT. Highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

## 3. Null-pair grades

NP0 global scalar; NP1 selected mean; NP2 selected mean+symmetrized noise; NP3 finite independent multiprobe/multipole mean/noise set; NP4 complete relevant smeared stress-energy mean/noise on declared domain; NP5 NP4 plus apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction remains finite NP3 Toy009 with the Iteration-011 balanced calibration geometry. NP grade is not experimental significance.

## 4. Retained result chain

- Toy001: equal mean can hide different covariance.
- RQIR-NG-001 / Toy002: static density phase blindness.
- RQIR-NG-002 / Toy003: minimal ordered-response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response `D_B`.
- PE-1 / Toy005: exact Newtonian one-channel embedding; remains NP2.
- RQIR-NG-003 / Toy006: complete generic local-density history becomes tomography.
- Toy007: first finite NP3, `eta_R~0.457682`, `s_min~1.463e-3`, condition `~3.18e3`.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivated likelihood/Fisher rather than maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under stated regularity assumptions.

## 5. Statistical identifiability and detector transfer

For parameter of interest beta and nuisances theta, `F_beta|theta=F_bb-F_btheta F_thetatheta^-1 F_thetab`; after whitening `F_beta|theta=||(I-P_J)s_tilde||^2`.

Protocol 002 uses two response bands. For whitened powers `P2,P4` and a relative spectral-tilt nuisance, `S_eff=4 P2 P4/(P2+P4)`. Losing one band kills the shape discriminator.

D1 matter-wave phase: passive full-period integration cancels selected AC bands; deliberate lock-in/echo sensitivity is required. D2 force: at a true force-noise floor, mechanical susceptibility does not provide free force-domain Fisher gain.

## 6. Toy009 and balanced calibration baseline

Toy009 source radii: `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Detector-aware source redesign improved the Toy007 ideal two-band source information by about `x1.22184` D1 and `x1.40358` D2 while improving response survival/conditioning. A detector-only high-gain source gave much larger raw signal but was projected away by NP3 calibration; retain this negative counterexample.

RQIR-DESIGN-001: optimize the whole chain `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`.

Iteration-011 balanced calibration is the current geometry baseline:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- positive states and selected equality residual `<1e-15`;
- `eta_R~0.5734264`;
- `s_min~1.999540e-3`;
- condition `~2313.05`;
- cumulative ideal gains vs Toy007 roughly D1 `x2.11`, D2 `x2.36`.

RQIR-CAL-002: calibration geometry is an active information resource.

## 7. RQIR-NG-005 — hidden-amplitude self-calibration obstruction

If hidden source direction `n` obeys `A n=0` and detector signal is locally `mu_D=beta*a*s`, the gravitational null calibration contains no information on amplitude `a`. Without independent source-preparation metrology, beta and a are locally non-identifiable and `F_beta|a=0`.

Independent preparation Fisher `C_a` is logically required. In the one-nuisance ideal limit, retaining fraction `r` of detector information requires `C_a/S_D=r/(1-r)`.

## 8. Physical Fisher resource layer — Iteration 012

Main file: `docs/PHYSICAL_FISHER_RESOURCE_BUDGET.md`. Code: `analysis/physical_resource_budget_iteration012.py`.

Current NP3 row classes: trace 1; energy 1; potential means 14; symmetrized covariance/noise 8.

At detector SNR 5, 90% retention of the preparation-amplitude degree requires `C_a=225`, hence `N_prep=225/xi_prep^2` for standardized single-shot sensitivity `xi_prep`.

RQIR-CAL-004: `s_min`/condition number alone are insufficient physical-resource proxies because detector-nuisance alignment matters.

RQIR-RESOURCE-001: per-shot coherence and total integration time are distinct. Current largest phase `4.99085` requires `T_coh>=0.7943/f_gap`.

Scalar gamma is diagnostic only. Physical calibration must use `F_C=A^T Sigma_C^-1 A` or equivalent row-specific repeated-setting Fisher sums.

## 9. Iterations 013-015 — heterogeneous allocation and mandatory numerical correction

Iteration 013 introduced separate mean/covariance Fisher weights and the principle that detector-level leverage plus per-shot information should determine resource allocation. Iteration 014 added correlated covariance and slow-drift diagnostics.

**Critical correction from Iteration 015:** trace+energy were approximated by a `1e12` Fisher penalty and then passed through a thresholded pseudoinverse. For heterogeneous weights this truncated genuine weak directions and artificially inflated `F_beta`.

RQIR-NUM-001: exact constraints must be eliminated analytically through a nullspace/reduced basis, not emulated by enormous penalties before pseudoinversion.

Corrected 22D hard-constrained consequences:

- old Iteration-013 D1 point retains about `0.572`, not 90%; D2 about `0.481`;
- corrected heterogeneous-allocation cost gains at 90% are only about `x1.07` D1 and `x1.14` D2, not the old `x6.3/x4.6`;
- corrected q=1 allocations: D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`; D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`;
- the old Iteration-014 claim that `rho=0.10` common correlation makes D2 about `2.13x` costlier is withdrawn; corrected stress-test cost ratios are about `0.90` D1 and `0.91` D2;
- corrected conservative first-order timing scales are about `9.5 us` D1 and `8.0 us` D2 at `100 Hz`.

The conceptual orientation/resource-allocation lessons survive; the old headline numerical gains do not.

## 10. Iteration 016 — explicit low-rank systematics Fisher

Main file: `docs/LOW_RANK_CALIBRATION_SYSTEMATICS_FISHER.md`. Code: `analysis/low_rank_systematics_fisher_iteration016.py`.

Four first-order calibration nuisances are explicit: second-probe drift `delta y`, common timing/phase drift `delta tau`, common mean offset and common covariance offset.

With no independent priors on these four amplitudes, profiled `F_beta` collapses to numerical zero for both D1 and D2. Increasing gravitational calibration exposure by up to `100x` does not cure the structural degeneracy.

RQIR-NG-006: uncontrolled low-rank calibration systematics can be structurally degenerate with detector-relevant source nuisance, so exposure alone cannot restore identifiability.

A control bundle restoring about 90% information requires approximately:

D1: `sigma(delta tau)=5.95e-3` (`~9.5 us` at 100 Hz), `sigma(b_mean)=7.62e-5`, `sigma(b_cov)=1.03e-4`.

D2: `sigma(delta tau)=5.03e-3` (`~8.0 us` at 100 Hz), `sigma(b_mean)=6.44e-5`, `sigma(b_cov)=1.04e-4`.

RQIR-CAL-007: calibration exposure and independent control-prior information are distinct, non-interchangeable resources.

RQIR-DRIFT-001: pure common multiplicative gain is first-order suppressed at exact null because `A theta0=0`. Leading gain contamination is nonlinear/product-like.

## 11. Iteration 017 — second-order nonlinear bias

Main file: `docs/SECOND_ORDER_NONLINEAR_BIAS_AUDIT.md`. Code: `analysis/second_order_nonlinear_bias_iteration017.py`.

At the Iteration-016 timing priors, quadratic timing bias is only `~3.49e-5 sigma_beta` D1 and `~8.75e-6 sigma_beta` D2. A `0.1 sigma_beta` curvature bias occurs only near `delta_tau~0.319` D1 and `~0.538` D2.

RQIR-NL-001: satisfying the current first-order timing-control requirement automatically suppresses timing curvature far below the statistical budget in this local Toy009 likelihood.

For common gain × residual source nuisance, local posterior-scale RMS beta-bias coefficient is about `0.325 |delta_g|`. A 1% common gain error is only about `3.1e-3 sigma_beta` under that local assumption. No global gain-only tolerance exists because bias scales as `delta_g * delta_theta`.

RQIR-NL-002: first-order nulling converts a standalone control requirement into a product-resource requirement with the coupled nuisance amplitude.

## 12. Iteration 018 — reference channels and wall-clock Fisher

Main file: `docs/REFERENCE_CHANNEL_WALLCLOCK_RESOURCE_BUDGET.md`. Code: `analysis/reference_channel_wallclock_iteration018.py`. Log: `research_log/2026-08-29_iteration_018_reference_channel_wallclock.md`.

Timing mapping at `f_gap=100 Hz`:

- D1 `sigma_tau=5.95e-3` -> `sigma_t~9.47 us`;
- D2 `sigma_tau=5.03e-3` -> `sigma_t~8.01 us`.

For white one-sided clock jitter integrated over bandwidth `B`, `J_t<=sigma_t/sqrt(B)`. At 1 kHz this is about `0.299 us/sqrtHz` D1 and `0.253 us/sqrtHz` D2. If four independent edge errors add in quadrature, per-edge RMS is about `4.73 us` D1 and `4.00 us` D2; correlated/common timing errors do not receive this reduction.

The maximum phase `tau_max=4.99085067` implies a hard coherent-shot floor `T_coh,min~7.94 ms` at 100 Hz.

**RQIR-RESOURCE-002:** coherence-span requirements must enter Fisher-per-second accounting; do not convert repetitions to wall time using a nominal shot duration shorter than the required coherent evolution.

At detector SNR 5 and standardized `xi_mean=xi_cov=10`, the corrected Iteration-015 calibration allocations correspond to about `7.90e6` accepted calibration-shot equivalents D1 and `1.031e7` D2. With only the 7.94-ms coherence floor this is at least `17.4 h` D1 and `22.7 h` D2. With `1 ms` extra dead time and `p_success=0.5`, about `39.3 h` and `51.2 h`. These are scaling examples, not hardware forecasts.

Preparation benchmarks at detector SNR 5: 80% -> `C_a=100`, `sigma_a=0.10`; 90% -> `225`, `0.0667`; 95% -> `475`, `0.0459`.

For a two-resource wall-clock split between detector Fisher rate `R_D` and independent preparation-metrology rate `R_P`, maximizing `F/T` for `F=SC/(S+C)` gives

- `x_D=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`;
- `x_P=sqrt(R_D)/(sqrt(R_D)+sqrt(R_P))`;
- optimal preparation-retention fraction `r*=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`.

**RQIR-RESOURCE-003:** wall-clock allocation follows a square-root Fisher-rate law in the two-resource local limit. A fixed 90% preparation-retention target is wall-clock optimal only when `R_P/R_D=81`; previous 80/90/95% tables are benchmark constraints, not universal optimal schedules.

Gain-reference mapping from Iteration 017: local bias budgets of `0.1`, `0.01`, `0.001 sigma_beta` correspond to gain-reference SNR about `3.25`, `32.5`, `325`, respectively, under the local posterior-scale source-error assumption.

## 13. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## 14. Current priority order

P1: build branch-specific physical Fisher rates rather than standardized `xi`: D1 phase-shot variance/contrast/four-switch timing/dead time; D2 equivalent-force PSD/integration/sampling/duty cycle; explicit source-preparation metrology rate.

P2: optimize the full detector + preparation + gravitational calibration + reference-control `F_beta|theta/T_wall`; use Iteration-018 square-root law only as a two-resource analytic check.

P3: common D1/D2 resource budget at one source mass, gap, coherence, separation and integration time.

P4: propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

P5: after detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation/gauge/renormalization gates.

## 15. Continuation protocol

At each substantive iteration: inspect repository state and latest log; avoid duplication; state one unresolved target; derive before numerical complexity; preserve negative/correction results; save reproducibility code; update this guide and `MASTER_TABLE.md`; never promote toy-model or detector benchmarks to empirical new physics.
