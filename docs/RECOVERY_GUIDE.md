# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v1.0

This file is the continuity backbone. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

`P_data(o|s) -> [interface class]`.

Rules: observable first; explicit baseline/domain; preserve operator ordering; retain negative results; source response is not detector observability; exact nulls are not statistical identifiability; every numerical result gets reproducibility code; no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

## 2. Ordered source hierarchy

At second order:

`K_T^(2) = (<T>, N, D or chi^R)`

with symmetrized noise `N`, ordered/commutator response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger-Keldysh/CTP generating functional `Z_T[J+,J-]`.

Working channels: Q1 clocks; Q2 superposed sources; Q3 backreaction/source rule; Q4 gravity-mediated quantum information; Q5 geometry fluctuations; Q6 causal/process structure; Q7 low-energy QG EFT. Highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

## 3. Null-pair grades

NP0 global scalar; NP1 selected mean; NP2 selected mean+symmetrized noise; NP3 finite independent multiprobe/multipole mean/noise set; NP4 complete relevant smeared stress-energy mean/noise on declared domain; NP5 NP4 plus apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction remains **Toy 009, finite NP3**, now with improved calibration geometry from Iteration 011. NP grade is not experimental significance.

## 4. Retained result chain

- Toy 001: equal mean can hide different covariance.
- RQIR-NG-001 / Toy 002: static density readout is phase-blind for orthogonal nonoverlapping branches with matching diagonal mass statistics.
- RQIR-NG-002 / Toy 003: minimal ordered-response split has an energy confound.
- Toy 004: balanced five-level witness showing `(<H>,<B>,N_B)` does not determine ordered response `D_B`.
- PE-1 / Toy 005: positive finite-dimensional operator has exact Newtonian one-channel embedding using localized modes at `r_a=L/b_a`; remains NP2.
- RQIR-NG-003 / Toy 006: complete generic local-density history becomes tomography, so exact full-history equality removes the distinct-state null pair.
- Toy 007: first finite NP3, `eta_R~0.457682`, `s_min~1.463e-3`, condition `~3.18e3`.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace; scope exact-null geometry only.
- Toy 008: soft-nullspace scan motivated likelihood/Fisher rather than maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under stated regularity assumptions.

## 5. Statistical identifiability and detector transfer

For parameter of interest beta and nuisances theta:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

After whitening: `F_beta|theta = ||(I-P_J) s_tilde||^2`.

Source ordered response must be propagated through gravity and detector transfer before interpretation. In the Newtonian schematic, `R_G(k)=-4 pi G/k^2`; detector covariance/noise and nuisance profiling are mandatory.

Protocol 002 uses two response bands. For whitened band powers `P2,P4` and an antisymmetric spectral-tilt nuisance:

`S_eff = 4 P2 P4/(P2+P4)`.

If one band is lost, the shape discriminator vanishes. With independent static amplitude calibration information C: `F = S_eff C/(S_eff+C)`.

## 6. Detector branches

D1 matter-wave phase: passive full-period integration cancels chosen AC harmonics, so deliberate lock-in/echo sensitivity is required. Toy 007 eight-switch bounded benchmark gave `m_s m_p ~8.1e-29 kg^2` under idealized assumptions. RQIR-D1-002: cumulative per-switch contrast can dominate finite bandwidth; if each switch multiplies amplitude by c, Fisher scales as `c^(2 N_sw)`.

D2 mechanical force: `Delta F_n = 2 alpha G m_s m_p G_n/L0^2`. RQIR-D2-001: at a true force-noise floor, resonance does not provide free force-domain Fisher gain because susceptibility multiplies both displacement signal and displacement noise. Toy 007 optimistic `1e-21 N/sqrt(Hz)` benchmark required `~2.40e-18 kg^2`.

## 7. Toy 009 — detector-aware source redesign (Iteration 010)

Main file: `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`.

Negative detector-only NP2 candidate: D1 `x5.3625`, D2 `x4.1741`, but inherited NP3 calibration collapses `eta_R` to `~0.0299`, `s_min~2.61e-4`, condition `~1.75e4`. Retain as evidence that upstream response optimization can be projected away.

Accepted Toy 009 source (seed 314159, trial 811), radii approximately `(1.00000,1.60090,1.77911,2.60901,5.90724)`. Inherited calibration stays rank `24/25`, exact selected equality residuals below `6e-16`, states positive. It gives `eta_R~0.568823`, `s_min~1.5122e-3`, condition `~3.03e3`, D1 `S_eff x1.22184`, D2 `S_eff x1.40358` relative Toy 007.

Toy 009 low-switch D1: four-switch design gives `F~1.12746` times Toy007 eight-switch; six-switch gives `~1.23731`. Illustrative mass-product scales become `~7.63e-29 kg^2` and `~7.28e-29 kg^2`. D2 optimistic benchmark rescales to `~2.03e-18 kg^2`.

RQIR-DESIGN-001: optimize `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled Fisher`; do not rank a source before downstream projections.

## 8. Iteration 011 — joint Toy 009 calibration geometry

Main file: `docs/TOY009_JOINT_CALIBRATION_GEOMETRY.md`. Code: `analysis/toy009_joint_calibration_geometry.py`. Log: `research_log/2026-08-29_iteration_011_joint_calibration_geometry.md`.

Inherited settings were `y1=-3.595527...` and Toy007 sampling phases. A joint search over the second-probe position and six nonzero calibration/target phases, while preserving the same 24-row NP3 structure, positivity, and non-degradation guards, found a gain-conditioning Pareto frontier.

Accepted balanced calibration:

`y1=-3.7766873837`

`times=(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`.

Diagnostics:

- rank `24/25`;
- exact selected residual `<1e-15`;
- states positive;
- `eta_R~0.5734264`;
- `s_min~1.999540e-3` (about +32% vs inherited Toy009);
- condition `~2313.05` (about 24% improvement);
- D1 `S_eff x1.7268` vs inherited Toy009;
- D2 `S_eff x1.6838` vs inherited Toy009;
- selected mean/noise remain equal to numerical precision;
- target ordered response remains opposite (`~+/-0.01163`).

Cumulative ideal two-band detector-source gains relative to Toy007 are about D1 `x2.11` and D2 `x2.36`.

An aggressive frontier point reaches about `x1.81` in both D1/D2 relative to inherited Toy009 but leaves `s_min` near the old guard; it is not the operational baseline.

### RQIR-CAL-002 — calibration geometry is an active information resource

At fixed source and fixed NP3 constraint count/type, probe location and sampling phases rotate the surviving exact-null direction relative to detector harmonics and can materially change downstream information. Scope: finite-dimensional numerical design result, not universal theorem.

## 9. Open mandatory consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## 10. Current priority order

P1: replace detector-agnostic/equal-noise `S_eff` objective by an explicit detector covariance and optimize profiled `F_beta|theta` directly. Do not use only eta/s_min as inference proxies.

P2: realistic D2 covariance — thermal force, backaction and displacement-imprecision PSD, including one-mode/dual-mode/tuned strategies.

P3: continuous/phase-modulated D1 control versus four/six hard switches under one bandwidth, contrast, dead-time and timing-jitter budget.

P4: common D1/D2 resource budget at one source mass, gap scale, coherence time, separation and integration time.

P5: propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

P6: after detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation/gauge/renormalization gates.

## 11. Continuation protocol

At each substantive iteration: inspect repository state and latest log; avoid duplication; state one unresolved target; derive before numerical complexity; preserve negative results; save reproducibility code; update this guide and `MASTER_TABLE.md`; never promote toy-model or detector benchmarks to empirical new physics.
