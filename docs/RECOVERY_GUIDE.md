# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v0.9

This file is the continuity backbone. A new session should be able to resume from this document plus the referenced files. The repository, not chat history, is authoritative project memory.

## 1. Objective

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

\[
P_{data}(\mathbf o|\mathbf s)\Rightarrow[\mathfrak I].
\]

Core discipline:

- observable first;
- baseline/domain explicit;
- preserve operator ordering;
- retain negative/no-go results;
- compare competing interface classes in one likelihood language;
- source response is not detector observability;
- exact nulls are not statistical identifiability;
- every numerical claim gets reproducibility code;
- no fundamental/new-physics claim until classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

## 2. Ordered source hierarchy

At second order,

\[
\boxed{\mathcal K_T^{(2)}=(\langle T\rangle,N,D\text{ or }\chi^R).}
\]

\[
N_{AB}=\frac12\langle\{\delta T_A,\delta T_B\}\rangle,
\qquad
D_{AB}=\frac1{2i}\langle[\delta T_A,\delta T_B]\rangle,
\]

\[
\chi^R_{AB}=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A,T_B]\rangle.
\]

Parent source object:

\[
Z_T[J_+,J_-]=Tr(U[J_+]\rho_TU[J_-]^\dagger).
\]

Do not merge different operator orderings without an explicit identity/limit.

## 3. Working channels

- `Q1` quantum clocks / proper time;
- `Q2` superposed sources;
- `Q3` backreaction/source rule;
- `Q4` gravity-mediated quantum information;
- `Q5` geometry fluctuations;
- `Q6` causal/process structure;
- `Q7` low-energy quantum-gravity EFT.

Current highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

## 4. Null-pair grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational-readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over a declared domain;
- **NP5:** NP4 plus source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction: **Toy 009 = finite NP3**, improving Toy 007.

NP grade is not experimental significance.

## 5. Result chain to preserve

### Toy 001 — same mean, different variance

Equal mean mass can hide different covariance. Mean-vs-fluctuation discriminator only.

### RQIR-NG-001 / Toy 002 — static density phase blindness

For orthogonal nonoverlapping mass branches with density-diagonal static coupling/readout, relative phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — response split with energy confound

A qubit can have equal density mean/noise and opposite ordered response, but the same state direction changes mean generator energy.

### Toy 004 — balanced five-level witness

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — exact Newtonian one-channel embedding

For positive finite-dimensional `B=V diag(b_a)V^dagger`, choose localized one-particle modes at

\[
r_a=L/b_a,
\]

so

\[
\Phi_p=-\frac{Gm}{L}B.
\]

Toy 005 is NP2 because other density combinations differ.

### RQIR-NG-003 / Toy 006 — complete density-history tomography

Under sufficient generic finite-mode conditions,

\[
span_R\{P_a(t)\}=Herm(d),
\]

so complete local-density history equality implies identical states. Exact full tomography is too strong for a distinct-state response-only null pair.

### Toy 007 — first finite NP3

Two-probe finite calibration gave

\[
r_{obs}=24/25,
\qquad
\eta_R\approx0.457682,
\]

with equal selected potential mean/noise and opposite target response.

Weakness:

\[
s_{min}\approx1.463\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004 — exact-null saturation

If exact calibration has a one-dimensional nullspace, one additional independent exact row removes the nonzero exact state-difference null direction. Scope: exact null-pair geometry only.

### Toy 008 — soft-nullspace / Fisher transition

A reproducible design scan showed that forcing nullity one is not automatically optimal for response survival plus conditioning. This motivated statistical identifiability as the main experiment-design language.

## 6. Statistical identifiability core

File: `docs/STATISTICAL_IDENTIFIABILITY.md`.

For parameter of interest `beta` and nuisances `theta`,

\[
\boxed{
F_{\beta|\theta}
=F_{\beta\beta}
-F_{\beta\theta}F_{\theta\theta}^{-1}F_{\theta\beta}.
}
\]

After whitening,

\[
\boxed{F_{\beta|\theta}=\|(I-P_J)\tilde s\|^2.}
\]

Only detector signal outside the nuisance tangent span is locally identifiable.

### RQIR-CAL-001 — calibration monotonicity

Independent `beta`-blind calibration adds nuisance information and, under the declared regularity assumptions,

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

Thus more exact constraints can kill a constructed null pair while more noisy independent calibration can improve real inference.

## 7. Transfer layer

File: `docs/LINEAR_RESPONSE_TRANSFER.md`.

Bare Newtonian kernel:

\[
R_G(k)=-4\pi G/k^2.
\]

Dressed source-to-potential response:

\[
\mathcal R_{\Phi\rho}^R=[I-R_G\sigma_\chi\chi_\rho^R]^{-1}R_G.
\]

Detector:

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R.
\]

Detector covariance/noise must be propagated before interpreting a source-side `D/chi^R` split.

## 8. Protocol 002 — two-band profiled likelihood

Current discriminator uses two response harmonics. After full detector transfer and whitening,

\[
P_n=|s_n|^2/\sigma_n^2.
\]

For a free antisymmetric spectral-tilt nuisance,

\[
\boxed{S_{eff}=\frac{4P_2P_4}{P_2+P_4}.}
\]

If one band is lost, the shape discriminator vanishes.

With independent static amplitude calibration information `C`,

\[
\boxed{F_{\beta|\theta}=\frac{S_{eff}C}{S_{eff}+C}.}
\]

## 9. Detector branches

### D1 — matter-wave phase

General phase response:

\[
\Delta\varphi_n
=2\alpha\frac{Gm_sm_pT_D}{\hbar L_0}H_nW_n.
\]

`RQIR-D1-001`: uniform integration over an integer number of complete source periods cancels the nonzero harmonics (`W_2=W_4=0`). Deliberate lock-in/echo sensitivity engineering is required.

Toy 007 eight-switch bounded sequence gave the revised five-sigma illustration

\[
m_sm_p\sim8.1\times10^{-29}\,kg^2
\]

or equal mass around `9e-15 kg` under the stated idealized noise/geometry assumptions.

`RQIR-D1-002`: finite switching bandwidth is less severe than repeated contrast loss; if each switch multiplies signal amplitude by `c`, Fisher scales as `c^(2N_sw)`.

### D2 — mechanical force

\[
\Delta F_n=2\alpha\frac{Gm_sm_p}{L_0^2}G_n.
\]

Equivalent force noise:

\[
S_F^{eq}=S_F^{th}+S_x^{imp}/|\chi_m|^2.
\]

`RQIR-D2-001`: at a true force-noise floor, resonance amplifies both signal and displacement noise, so susceptibility does not provide free force-domain Fisher gain.

Toy 007 optimistic `1e-21 N/sqrt(Hz)` benchmark required approximately

\[
2.40\times10^{-18}\,kg^2.
\]

D1 remains the stronger absolute-sensitivity branch for the current micrometre geometry; D2 remains much more technologically mature but far from the required force scale.

## 10. Toy 009 — detector-aware source redesign

Main file: `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`.

### 10.1 Negative detector-only candidate

A deterministic NP2 scan (seed `20260829`, 5000 trials) found trial `2641` with apparent ideal two-band gains

\[
S_{eff}^{D1}:\times5.3625,
\qquad
S_{eff}^{D2}:\times4.1741.
\]

But applying the inherited Toy 007 NP3 calibration gives

\[
\eta_R\approx0.02990,
\]

\[
s_{min}\approx2.61\times10^{-4},
\qquad
\kappa_A\approx1.75\times10^4.
\]

This is retained as a `NEG/NUM` result: detector-only source optimization is unsafe because calibration can project away the gain.

### 10.2 Accepted NP3 candidate

Second deterministic scan: seed `314159`, 5000 trials, fixed Toy 007 calibration pattern. Acceptance required

\[
\eta_R\ge\eta_R^{007},
\qquad
s_{min}\ge s_{min}^{007}.
\]

Only one scanned candidate passes both guards: trial `811`.

Toy 009 radii:

\[
\boxed{(1.00000,1.60090,1.77911,2.60901,5.90724).}
\]

The fixed calibration remains rank `24/25`.

Positive state eigenvalues:

- rho+ approximately `(0.12000,0.17296,0.19541,0.24624,0.26539)`;
- rho- approximately `(0.13461,0.15376,0.20459,0.22704,0.28000)`.

Selected equality residuals are below `6e-16`.

At the inherited target time:

\[
\langle B_0\rangle_+=\langle B_0\rangle_-
\approx0.547860,
\]

\[
N_{00,+}=N_{00,-}\approx0.0132606,
\]

but

\[
\boxed{D_{00,+}\approx-0.0120850,}
\]

\[
\boxed{D_{00,-}\approx+0.0120850.}
\]

Calibration geometry:

\[
\boxed{\eta_R\approx0.568823,}
\]

\[
\boxed{s_{min}\approx1.5122\times10^{-3},}
\]

\[
\boxed{\kappa_A\approx3.03\times10^3.}
\]

Relative detector-source information:

\[
\boxed{S_{eff}^{D1}:\times1.22184,}
\]

\[
\boxed{S_{eff}^{D2}:\times1.40358.}
\]

This is the first simultaneous Pareto improvement over Toy 007 in D1, D2, response survival and conditioning.

## 11. Toy 009 D1 low-switch control

Toy 009 potential harmonics:

\[
H_2\approx-0.00167587+i0.00792491,
\]

\[
H_4\approx0.00434188+i0.00995421.
\]

### Four switches

A pi-periodic four-switch sequence with positive interval

\[
a\approx0.912594
\]

per half-period gives

\[
|W_2|\approx0.50363,
\qquad
|W_4|\approx0.30807,
\]

and

\[
\boxed{F_{009,4sw}\approx1.12746F_{007,8sw}.}
\]

### Six switches

Accepted interval vector:

`(0.26890,0.92358,1.02555,2.11605,1.02554,0.92358)`.

\[
|W_2|\approx0.45974,
\qquad
|W_4|\approx0.36382,
\]

\[
\boxed{F_{009,6sw}\approx1.23731F_{007,8sw}.}
\]

Thus the new source produces more two-band Fisher information with fewer hard switches.

Illustrative D1 mass-product scales under the previous assumptions:

- four switches: `~7.63e-29 kg^2`, equal mass `~8.73e-15 kg`;
- six switches: `~7.28e-29 kg^2`, equal mass `~8.53e-15 kg`.

Toy 009 D2 rescales the same optimistic force benchmark to `~2.03e-18 kg^2`.

These are scaling illustrations, not implementation forecasts.

## 12. New design principle

### RQIR-DESIGN-001 — optimize source and inference geometry jointly

Correct design ordering:

\[
\boxed{
\text{source}
\to
\text{calibration/null or Fisher geometry}
\to
\text{gravity transfer}
\to
\text{detector window/noise}
\to
F_{\beta|\theta}.
}
\]

Large upstream response gain is not accepted until it survives every downstream projection.

## 13. External-method boundary

Time-dependent lock-in/dynamical-decoupling sensitivity engineering is established quantum-sensing methodology. Recent continuous phased dynamical-decoupling work (PRL 134, 120802, 2025) shows that AC quantum sensing can use continuous control with discrete phase changes rather than only ideal instantaneous pulses.

RQIR does not claim this control method as new physics. The RQIR-specific contribution is applying joint source/calibration/gravity/detector optimization to the ordered gravity-interface discriminator.

## 14. Current consistency gates

Still open and mandatory before any fundamental claim:

- `G1` gauge/relational observables;
- `G2` full source+apparatus conservation/Bianchi embedding;
- `G3/G3b` positivity/unitarity/spectral response consistency;
- `G4a` causal retarded support;
- `G8` controlled Newtonian limit;
- `G9` EFT power counting;
- `G10/G10a` stress-energy smearing/renormalization;
- `G12/G12a` classical/stochastic/full-QFT degeneracy audit;
- `G13` detector-level covariance, nuisance profiling and measurability.

## 15. Current core files

- `docs/MASTER_TABLE.md`
- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`
- `docs/D1_FINITE_BANDWIDTH_CONTROL.md`
- `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`
- `analysis/toy009_detector_aware_source_search.py`
- `analysis/d1_low_switch_toy009.py`
- `research_log/2026-08-29_iteration_010_toy009_detector_aware_source.md`

Earlier toy-model and protocol files remain part of the chain and should not be deleted.

## 16. Exact next research target

### P1 — joint Toy 009 calibration-geometry optimization

Vary second-probe location and calibration times together with the source. Replace the inherited Toy 007 settings by an objective based on detector-level profiled Fisher while preserving state positivity and declared geometry guards.

### P2 — continuous D1 sensitivity

Compare four/six hard switches against continuous/phase-modulated sensitivity functions under the same bandwidth, contrast, dead-time and timing-jitter budget.

### P3 — realistic D2 covariance

Add thermal force, backaction and displacement-imprecision PSD; evaluate actual two-band whitened `P2,P4` rather than detector-agnostic force floors.

### P4 — common resource budget

Compare D1/D2 at one declared source mass, gap scale, coherence time, separation and integration time.

### P5 — interface-class fingerprints

Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same detector likelihood.

### P6 — relativistic/full-stress embedding

Only after detector/inference geometry stabilizes, embed a more physical oscillator/atomic source and close source+apparatus stress-energy, conservation, gauge and renormalization gates.

## 17. Continuation protocol

At each substantive iteration:

1. read this guide and the latest research log;
2. inspect repository state before starting work, especially because hourly automation may also advance the project;
3. avoid duplicating active or already-completed work;
4. state one exact unresolved target;
5. derive analytically before adding numerical complexity;
6. preserve negative/correction results;
7. save reproducibility code for every numerical result;
8. update `MASTER_TABLE.md` and this guide when the project state changes;
9. never promote a toy model, detector benchmark or internal consistency result to empirical new physics.
