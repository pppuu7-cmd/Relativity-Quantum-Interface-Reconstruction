# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v1.7

This file is the continuity backbone. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem: `P_data(o|s) -> [interface class]`.

Rules: observable first; explicit baseline/domain; preserve operator ordering; retain negative/correction results; source response is not detector observability; exact nulls are not statistical identifiability; every numerical result gets reproducibility code; no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

## 2. Ordered source hierarchy and null grades

At second order `K_T^(2)=(<T>,N,D or chi^R)`, with symmetrized noise `N`, ordered/commutator response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger-Keldysh/CTP generating functional.

Working channels: Q1 clocks; Q2 superposed sources; Q3 backreaction/source rule; Q4 gravity-mediated quantum information; Q5 geometry fluctuations; Q6 causal/process structure; Q7 low-energy QG EFT. Highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

NP0 global scalar; NP1 selected mean; NP2 selected mean+symmetrized noise; NP3 finite independent multiprobe/multipole mean/noise set; NP4 complete relevant smeared stress-energy mean/noise on declared domain; NP5 NP4 plus apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction remains finite NP3 Toy009/Toy010 family. NP grade is not experimental significance.

## 3. Retained result chain

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

## 4. Statistical identifiability and detector transfer

For parameter of interest beta and nuisances theta,

`F_beta|theta=F_bb-F_btheta F_thetatheta^-1 F_thetab`.

After whitening: `F_beta|theta=||(I-P_J)s_tilde||^2`.

Protocol 002 uses two response bands. For whitened powers `P2,P4` and a relative spectral-tilt nuisance,

`S_eff=4 P2 P4/(P2+P4)`.

Losing one band kills the shape discriminator.

D1 matter-wave phase: passive full-period integration cancels selected AC bands; deliberate lock-in/echo sensitivity is required. D2 force: at a true force-noise floor, mechanical susceptibility does not provide free force-domain Fisher gain.

## 5. Toy009/Toy010 calibration baseline

Toy009 source radii: `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Toy009 established RQIR-DESIGN-001: optimize the whole chain `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`; detector-only high-gain candidates can be projected away by NP3 calibration.

Toy010 showed calibration geometry is itself an active design variable. The exact-null direction can rotate strongly when probe position/times change even for a fixed source.

The later Iteration-011 balanced calibration is the current practical geometry baseline:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- positive states and selected equality residual `<1e-15`;
- `eta_R~0.5734264`;
- `s_min~1.999540e-3`;
- condition `~2313.05`.

RQIR-CAL-002: finite calibration geometry steers the hidden direction and must be co-designed with detector observability.

## 6. RQIR-NG-005 — hidden-amplitude self-calibration obstruction

If hidden source direction `n` obeys `A n=0` and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration contains no information on amplitude `a`. Without independent source-preparation metrology, beta and a are locally non-identifiable and `F_beta|a=0`.

Independent preparation Fisher `C_a` is logically required. In the one-nuisance ideal limit, retaining fraction `r` of detector information requires `C_a/S_D=r/(1-r)`.

## 7. Physical resource layer and mandatory numerical correction

The NP3 calibration rows are trace 1; energy 1; potential means 14; symmetrized covariance/noise 8.

RQIR-RESOURCE-001: per-shot coherence and total integration time are distinct. Current largest dimensionless phase `4.99085067` requires `T_coh>=0.7943/f_gap`.

Critical Iteration-015 correction: trace+energy had been approximated by a `1e12` Fisher penalty followed by thresholded pseudoinverse, which truncated real weak nuisance directions and inflated `F_beta`.

RQIR-NUM-001: exact constraints must be eliminated analytically through a nullspace/reduced basis, not emulated by enormous penalties before pseudoinversion.

Corrected 22D hard-constrained 90%-retention row weights:

- D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`;
- D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`.

Old large heterogeneous-allocation gains are withdrawn; corrected gains are only about `x1.07` D1 and `x1.14` D2.

## 8. Explicit low-rank systematics

Iteration 016 includes second-probe drift `delta y`, common timing/phase drift `delta tau`, common mean offset and common covariance offset.

With no independent priors, profiled `F_beta` collapses to numerical zero for both D1 and D2 even when gravitational calibration exposure increases by up to `100x`.

RQIR-NG-006: uncontrolled low-rank systematics can be structurally degenerate with detector-relevant source nuisance; exposure alone cannot restore identifiability.

A control bundle restoring about 90% information requires approximately:

- D1 `sigma(delta tau)=5.95e-3` -> `sigma_t~9.47 us` at 100 Hz; `sigma(b_mean)=7.62e-5`; `sigma(b_cov)=1.03e-4`.
- D2 `sigma(delta tau)=5.03e-3` -> `sigma_t~8.01 us`; `sigma(b_mean)=6.44e-5`; `sigma(b_cov)=1.04e-4`.

RQIR-CAL-007: calibration exposure and independent control-prior information are distinct resources.

RQIR-DRIFT-001: pure common multiplicative gain is first-order suppressed at exact null because `A theta0=0`; leading gain contamination is nonlinear/product-like.

## 9. Nonlinear bias audit

At the current timing priors, quadratic timing bias is only `~3.49e-5 sigma_beta` D1 and `~8.75e-6 sigma_beta` D2.

RQIR-NL-001: once first-order timing control is satisfied, timing curvature is not the current bottleneck.

For common gain × residual source nuisance, local posterior-scale RMS beta-bias is about `0.325 |delta g|`; no global gain-only tolerance exists because the bias scales as `delta g * delta theta`.

RQIR-NL-002: first-order nulling can convert a standalone control requirement into a product-resource requirement.

## 10. Reference channels and branch-specific Fisher rates

Iteration 018 mapped the timing priors to physical timing scales and established the coherence floor. RQIR-RESOURCE-002: coherent evolution is a hard lower bound on physical shot duration.

Iteration 019 replaced standardized detector sensitivity by native branch models:

- D1 phase/interference Fisher rate scales as `p_acc C^2 M^2 T^2/(T+t_dead)` with control-window factors; acquisition throughput is a separate resource from source mass/coherence.
- D2 is naturally a force-PSD/live-time problem with `R_D2 = eta_duty * 4 r2 r4/(r2+r4)`, `r_n=|Delta F_n|^2/S_F,n`.

RQIR-RESOURCE-004: D1 and D2 cannot be globally ranked without native Fisher rates and explicit noise assumptions.

## 11. Source-preparation QFI

Iteration 020 treats `rho(a)=I/5+a Delta0`. Because `[rho(a),Delta0]=0`, the amplitude QFI is

`F_Q(a)=sum_i d_i^2/(1/5+a d_i)`.

At `a=0.08`, `F_Q~13.2707` per ideal accepted copy. At detector SNR 5, a 90%-retention target `C_a=225` corresponds to only about 17 ideal accepted copies at the QFI bound.

RQIR-PREP-001: RQIR-NG-005 is an obstruction of the gravitational null channel, not absence of source-state information in principle.

Physical preparation-metrology rate: `R_P=p_P eta_P F_Q/t_P`.

## 12. Full wall-clock optimizer

Iteration 021 builds a hard-constrained optimizer over detector, preparation, mean-calibration and covariance-calibration time fractions. A unique SI-time optimum remains underdetermined until physical calibration/reference rates are supplied.

RQIR-RESOURCE-005: do not convert dimensionless row weights to hours without a measurement-level Fisher-rate model.

The optimizer recovers the two-resource square-root law when calibration becomes effectively free.

## 13. Native calibration/reference Fisher rates

Iteration 022 replaces remaining standardized calibration/reference sensitivities by explicit rates.

D1 mean calibration at phase quadrature:

`R_M,i = p_acc C_i^2 k_i^2/t_cycle`.

Gaussian covariance/log-PSD channel:

`R_C ~= duty * B * k_C^2`.

D2 mean calibration uses the one-sided force-template Fisher `I_i=4 int |dh_i/du_i|^2/S_F df`.

Timing reference:

`R_tau=p_acc/[t_cycle (omega_gap sigma_t,event)^2]`.

Equivalent time to a physical timing target:

`T_tau=t_cycle/p_acc * (sigma_t,event/sigma_t,target)^2`.

RQIR-RESOURCE-006: nuisance-coordinate normalization cannot create a physical wall-time cost; cost is set by physical event precision, acceptance/cycle and required physical prior.

RQIR-DRIFT-002: white per-event timing Fisher does not certify long-run stability; low-frequency/common-mode drift is the relevant gate once white statistics are cheap.

## 14. Colored drift / Allan cadence — Iteration 023

Main file: `docs/COLORED_DRIFT_ALLAN_CADENCE.md`. Code: `analysis/colored_drift_allan_cadence_iteration023.py`.

For immediate reference variance `sigma_ref^2`, random-walk diffusion `D`, and irreducible Allan/flicker floor `sigma_floor`, the interval-averaged residual variance is

`<sigma^2> = sigma_floor^2 + sigma_ref^2 + D Delta/2`.

Therefore

`Delta_max = 2 (sigma_target^2-sigma_floor^2-sigma_ref^2)/D`,

provided the numerator is positive.

RQIR-NG-007 — stability-floor obstruction: if `sigma_floor^2+sigma_ref^2 >= sigma_target^2`, no finite recalibration cadence or repeated white-noise averaging can satisfy the required nuisance prior.

RQIR-DRIFT-003: long-campaign control must be budgeted by low-frequency stability `(D,sigma_floor)` or a measured Allan-deviation curve plus recalibration duty, not by per-event precision alone.

Transparent timing benchmark with `sigma_event=10 us`, `sigma_ref=sigma_target/3`, current 100-Hz coherence/dead-time/acceptance assumptions:

- reference block `~0.1795 s` D1, `~0.2509 s` D2;
- at `D=100 us^2/h`, cadence `~1.594 h` D1 and `~1.141 h` D2;
- at `D=1000 us^2/h`, cadence `~9.57 min` D1 and `~6.84 min` D2;
- equal-diffusion cadence ratio `Delta_D2/Delta_D1~0.715`.

These are parametric stability benchmarks, not hardware forecasts.

## 15. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## 16. Current priority order

P1: obtain branch-specific physically justified Allan/PSD models for D1 clock/control and D2 sampling/reference channels; map additive offsets into physical detector units.

P2: insert actual drift cadence and reference-control duty into the Iteration-021 full `F_beta|theta/T_wall` optimizer.

P3: build a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.

P4: propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

P5: after detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation/gauge/renormalization gates.

## 17. Continuation protocol

At each substantive iteration: inspect repository state and latest log; avoid duplication; state one unresolved target; derive before numerical complexity; preserve negative/correction results; save reproducibility code; update this guide and `MASTER_TABLE.md` or an explicit recovery delta; never promote toy-model or detector benchmarks to empirical new physics.
