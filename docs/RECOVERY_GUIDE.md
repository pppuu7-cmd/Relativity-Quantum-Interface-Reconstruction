# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v1.1

This file is the continuity backbone. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem: `P_data(o|s) -> [interface class]`.

Rules: observable first; explicit baseline/domain; preserve operator ordering; retain negative results; source response is not detector observability; exact nulls are not statistical identifiability; every numerical result gets reproducibility code; no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

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

D1 matter-wave phase: passive full-period integration cancels the selected AC bands; deliberate lock-in/echo sensitivity is required. D2 force: at a true force-noise floor, mechanical susceptibility does not yield free force-domain Fisher gain.

## 6. Toy009 source redesign — Iteration 010

Main file: `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`.

Accepted radii `(1.00000,1.60090,1.77911,2.60901,5.90724)`. Inherited NP3 calibration remains rank `24/25`, states positive, selected equality residual `<6e-16`, `eta_R~0.568823`, `s_min~1.5122e-3`, condition `~3.03e3`. Relative Toy007 ideal two-band gains: D1 `x1.22184`, D2 `x1.40358`.

Negative detector-only source reached D1 `x5.36`, D2 `x4.17` but was projected away by NP3 calibration (`eta_R~0.03`, condition `~1.75e4`). Retain this counterexample.

RQIR-DESIGN-001: optimize `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`.

## 7. Iteration 011 — balanced joint calibration geometry

Main file: `docs/TOY009_JOINT_CALIBRATION_GEOMETRY.md`.

Operational baseline:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- exact equality residual `<1e-15`;
- positive states;
- `eta_R~0.5734264`;
- `s_min~1.999540e-3`;
- condition `~2313.05`;
- D1 `S_eff x1.7268` vs inherited Toy009;
- D2 `S_eff x1.6838` vs inherited Toy009.

Cumulative ideal detector-source gains vs Toy007: D1 about `x2.11`, D2 about `x2.36`.

RQIR-CAL-002: calibration geometry is an active information resource; fixed-row-count probe/time choices rotate the surviving null direction relative to detector harmonics.

## 8. RQIR-NG-005 — null-amplitude self-calibration obstruction

Main file: `docs/STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`.

If the hidden source direction satisfies `A n=0` and detector signal is locally `mu_D=beta a s`, gravitational null calibration contains no information on amplitude `a`. Without independent source-preparation metrology, beta and a are locally non-identifiable and `F_beta|a=0`.

Independent preparation information `C_a` is therefore logically required. In the ideal one-nuisance limit, retaining fraction `r` of detector information requires `C_a/S_D=r/(1-r)`.

## 9. Iteration 012 — physical Fisher resource budget

Main file: `docs/PHYSICAL_FISHER_RESOURCE_BUDGET.md`. Code: `analysis/physical_resource_budget_iteration012.py`.

The scalar-gamma model was translated into repetition/time/coherence bookkeeping and explicitly demoted to a diagnostic proxy.

Current NP3 row classes: trace 1; energy 1; potential means 14; symmetrized covariance/noise 8.

For D1 on the Iteration-011 geometry, effectively perfect source-amplitude characterization gave scalar-gamma thresholds approximately `2.83e4` (50%), `6.85e5` (80%), `1.58e6` (90%), `3.38e6` (95%).

At detector SNR 5, 90% retention of the preparation-amplitude degree requires `C_a=225`, so `N_prep=225/xi_prep^2` for standardized single-shot sensitivity `xi_prep`.

RQIR-CAL-004: `s_min`/condition number alone are not sufficient physical-resource proxies because alignment with detector nuisance tangents matters.

RQIR-RESOURCE-001: per-shot coherence time and total integration time are distinct resources. For the largest current phase `4.99085`, `T_coh >=0.7943/f_gap`.

Critical correction: scalar gamma cannot be interpreted as one physical shot count. Physical calibration must use `F_C=A^T Sigma_C^-1 A` or an equivalent repeated-setting sum with row-specific Fisher information.

## 10. Iteration 013 — heterogeneous calibration Fisher allocation

Main file: `docs/HETEROGENEOUS_CALIBRATION_FISHER_ALLOCATION.md`. Code: `analysis/heterogeneous_calibration_allocation_iteration013.py`. Log: `research_log/2026-08-29_iteration_013_heterogeneous_calibration_allocation.md`.

Replace scalar gamma by separate weights for 14 potential-mean rows and 8 covariance rows:

`F_C=F_trace+energy + gamma_m M_m + gamma_c M_c`.

For per-shot informations `q_m,q_c`, standardized cost is `14 gamma_m/q_m + 8 gamma_c/q_c`.

At 90% retained detector information and `q_c/q_m=1`:

- D1: uniform weight `~1.54e6`; optimized `gamma_m~1.82e5`, `gamma_c~3.49e5`; standardized cost reduction `~6.3x`.
- D2: uniform weight `~2.14e6`; optimized `gamma_m~1.7e5`, `gamma_c~1.0e6`; cost reduction `~4.6x`.

The optimum changes strongly with `q_c/q_m` and differs between D1 and D2. Therefore there is no detector-independent optimal calibration schedule for the same source/operator set.

RQIR-CAL-005: resource-optimal calibration allocates information according to downstream nuisance-projection leverage and per-shot information cost; equal precision on all calibration observables is generally not resource-optimal. Scope: finite-dimensional numerical design result.

## 11. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## 12. Current priority order

P1: add correlated/common-mode calibration drift and slow source/detector gain/position nuisance. Test whether Iteration-013 allocation gains survive non-diagonal `Sigma_C`.

P2: convert standardized `q_m,q_c` to D1 seconds using phase-shot variance, control contrast/dead time/timing jitter and source-preparation/reset probability.

P3: convert D2 calibration/detection to force/displacement PSD with thermal force, backaction and imprecision, including multi-band strategy.

P4: common D1/D2 resource budget at one source mass, gap, coherence, separation and integration time.

P5: propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

P6: after detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation/gauge/renormalization gates.

## 13. Continuation protocol

At each substantive iteration: inspect repository state and latest log; avoid duplication; state one unresolved target; derive before numerical complexity; preserve negative results; save reproducibility code; update this guide and `MASTER_TABLE.md`; never promote toy-model or detector benchmarks to empirical new physics.
