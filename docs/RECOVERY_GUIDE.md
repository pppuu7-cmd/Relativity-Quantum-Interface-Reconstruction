# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v0.8

This file is the continuity backbone. A new session should be able to resume the project from this document plus the referenced files. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

\[
P_{data}(\mathbf o|\mathbf s)\Rightarrow[\mathfrak I].
\]

Rules:

- observable first;
- explicit baseline and domain;
- preserve operator ordering;
- compare competing interface classes in one observable language;
- retain negative/no-go results;
- no “quantum gravity detected” claim until classical/stochastic/hybrid/full-QFT-matter alternatives are tested in the same regime;
- every numerical claim gets reproducibility code;
- exact algebraic nulls are not confused with statistical identifiability;
- source-side response is not confused with detector-level observability.

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

## 3. Working channels

- `Q1` quantum clocks / proper time;
- `Q2` superposed sources;
- `Q3` backreaction/source rule;
- `Q4` gravity-mediated quantum information;
- `Q5` geometry fluctuations;
- `Q6` causal/process structure;
- `Q7` low-energy quantum-gravity EFT.

## 4. Null-pair grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational-readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over a declared domain;
- **NP5:** NP4 plus source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction: **Toy 007 = finite NP3**.

NP grade is not experimental significance.

## 5. Result chain

### Toy 001 — same mean, different variance

Equal mean mass can hide different covariance. Mean-vs-fluctuation discriminator only.

### RQIR-NG-001 / Toy 002 — static density phase blindness

For orthogonal nonoverlapping mass branches with density-diagonal static coupling/readout, relative phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — response split with energy confound

A qubit can have equal density mean/noise and opposite ordered response, but the same state direction changes mean generator energy.

### Toy 004 — balanced five-level algebraic witness

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

File: `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`.

### PE-1 / Toy 005 — exact Newtonian one-channel embedding

For positive finite-dimensional

\[
B=V\,diag(b_a)V^\dagger,
\]

choose localized one-particle modes at

\[
r_a=L/b_a.
\]

Then

\[
\boxed{\Phi_p=-\frac{Gm}{L}B.}
\]

Toy 005 therefore embeds the ordered-kernel split into a physical weak-field potential channel. It remains NP2 because other spatial density combinations differ.

### RQIR-NG-003 / Toy 006 — complete density-history tomography

Under sufficient generic finite-mode conditions,

\[
span_R\{P_a(t)\}=Herm(d),
\]

so complete local-density history equality implies

\[
\rho_+=\rho_-.
\]

Exact full tomography is too strong for a distinct-state response-only null pair.

### Toy 007 — finite multiprobe NP3

Source positions:

\[
x_a\approx(5.53112,2.21089,1.44295,1.27948,1.00000).
\]

Two-probe finite calibration gives

\[
\boxed{r_{obs}=24/25},
\qquad
\boxed{\eta_R\approx0.457682}.
\]

At target time

\[
t_R\approx3.583928899,
\]

selected potential mean and symmetrized noise are equal while

\[
D_{00,+}\approx-0.01056563,
\qquad
D_{00,-}\approx+0.01056563.
\]

Critical weakness:

\[
s_{min}\approx1.463\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004 — exact-null saturation

If exact calibration has rank `p-1` and one-dimensional nullspace, one additional exact independent row removes the nonzero exact state-difference null direction.

Scope: exact null-pair construction only.

### Toy 008 — soft-nullspace transition

Reproducible 300-design scan showed, within the tested design family, that nullity `3–5` can give larger response survival and better conditioning than forcing nullity `1`.

This motivated moving from exact null geometry to likelihood/Fisher geometry.

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

Only the whitened detector signal component outside the nuisance tangent span is locally identifiable.

### RQIR-CAL-001 — calibration monotonicity

Independent `beta`-blind calibration adds positive semidefinite nuisance information and, under the declared regularity assumptions,

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

Thus additional exact constraints can kill a constructed null pair while additional noisy independent calibration can improve real inference.

## 7. Transfer Layer 001 — source → gravity → detector

File: `docs/LINEAR_RESPONSE_TRANSFER.md`.

Bare Newtonian density-to-potential kernel:

\[
R_G(k)=-4\pi G/k^2.
\]

Dressed source-to-potential response:

\[
\boxed{
\mathcal R_{\Phi\rho}^R
=[I-R_G\sigma_\chi\chi_\rho^R]^{-1}R_G.
}
\]

Detector response/noise:

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R,
\]

\[
N_D^{obs}=R_D^R*N_\Phi*R_D^A+N_D.
\]

Source-side `D/chi^R != 0` is not yet an observable gravitational discriminator.

## 8. Protocol 002 — two-harmonic profiled detector likelihood

Dominant potential-response harmonics:

\[
H_2\approx-2.71833\times10^{-4}-i7.66139\times10^{-3},
\]

\[
H_4\approx1.20943\times10^{-3}-i9.06108\times10^{-3}.
\]

\[
H_{24}\approx1.19305\times10^{-2},
\qquad
\kappa_B\approx0.174201,
\]

\[
1-\kappa_B^2\approx0.969654.
\]

With response information `S`, static common-amplitude calibration `C`, and free relative spectral-tilt nuisance,

\[
\boxed{
F_{\beta|\theta}
=\frac{S(1-\kappa_B^2)C}{S(1-\kappa_B^2)+C}.
}
\]

One harmonic alone is degenerate with the free tilt nuisance; two harmonics break that degeneracy.

Colored detector law:

\[
\boxed{S_{eff}=\frac{4P_2P_4}{P_2+P_4}.}
\]

If one whitened band is lost, the two-band shape discriminator vanishes.

## 9. Protocol 002B — original physical phase scale

Original ideal-window scaling:

\[
\Gamma_G=\frac{Gm_sm_pT_D}{\hbar L_0},
\]

\[
\Delta\varphi_n=2\alpha\Gamma_GH_n.
\]

Under `alpha=0.1`, `sigma_phi=1 mrad`, `L0=10 um`, `T=1 s`, the ideal matched-readout five-sigma illustration was

\[
m_sm_p\gtrsim3.36\times10^{-29}\,kg^2
\]

or equal mass

\[
m\gtrsim5.8\times10^{-15}\,kg.
\]

**Important correction from Iteration 008:** this is an ideal harmonic-transfer benchmark, not the result of passive uniform phase integration.

## 10. Detector Branch Comparison 001 — D1 vs D2

Main file: `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`.  
Code: `analysis/detector_branch_d1_d2.py`.  
Log: `research_log/2026-08-29_iteration_008_detector_branches.md`.

### 10.1 D1 — matter-wave phase

General sensitivity-window response:

\[
\boxed{
\Delta\varphi_n
=2\alpha\frac{Gm_sm_pT_D}{\hbar L_0}
H_n\mathcal W_n.
}
\]

#### RQIR-D1-001 — full-period window cancellation

For uniform phase accumulation over exactly one complete source period,

\[
\mathcal W_2=\mathcal W_4=0.
\]

So a passive full-period interferometer cancels both chosen AC harmonics.

A simple bounded proof-of-principle lock-in

\[
g(\tau)=sign[\cos2\tau+\lambda\cos4\tau]
\]

with

\[
\lambda\approx1.046
\]

gives

\[
|\mathcal W_2|\approx0.4402,
\qquad
|\mathcal W_4|\approx0.3851.
\]

It retains about

\[
17.2\%
\]

of ideal two-band Fisher information, or

\[
41.5\%
\]

of ideal SNR amplitude.

Revised five-sigma illustration under the same assumptions:

\[
\boxed{m_sm_p\gtrsim8.1\times10^{-29}\,kg^2,}
\]

with equal-mass illustration

\[
\boxed{m\gtrsim9.0\times10^{-15}\,kg.}
\]

This is still far above the current free-particle matter-wave mass record.

### 10.2 D2 — mechanical force/acceleration

Gradient readout operator:

\[
G_0=\left.\partial_yB(y)\right|_{0}
=\sum_a x_a^{-2}n_a.
\]

Same-source cross-response harmonics:

\[
\boxed{
G_2\approx-6.78211\times10^{-4}-i1.14277\times10^{-2},
}
\]

\[
\boxed{
G_4\approx1.41626\times10^{-3}-i1.06107\times10^{-2}.
}
\]

Two-band norm:

\[
\boxed{G_{24}\approx1.56731\times10^{-2},}
\]

which is about `1.314` times the D1 source norm.

Spectral balance:

\[
\boxed{\kappa_G\approx-0.06701,}
\]

\[
\boxed{1-\kappa_G^2\approx0.99551.}
\]

Thus the D2 gradient response is intrinsically very robust against the same relative spectral-tilt nuisance.

Physical force harmonics:

\[
\boxed{
\Delta F_n=2\alpha\frac{Gm_sm_p}{L_0^2}G_n.
}
\]

For mechanical susceptibility `chi_m`, define equivalent-force noise

\[
\boxed{
S_F^{eq}=S_F^{th}+S_x^{imp}/|\chi_m|^2.
}
\]

Then

\[
P_n^{D2}\propto|\Delta F_n|^2T/S_{F,n}^{eq}.
\]

#### RQIR-D2-001 — resonance-gain cancellation at force-noise floor

If physical force noise dominates, mechanical susceptibility multiplies both displacement signal and displacement noise and cancels from force-domain Fisher information. Resonance helps mainly against displacement imprecision, not against a true force-noise floor.

At an optimistic detector-agnostic

\[
S_F^{1/2}=10^{-21}\,N/\sqrt{Hz}
\]

benchmark with `alpha=0.1`, `L0=10 um`, `T=1 s`, five sigma requires

\[
\boxed{m_sm_p\gtrsim2.40\times10^{-18}\,kg^2.}
\]

This is about

\[
\boxed{3\times10^{10}}
\]

times the revised D1 mass-product benchmark.

Not a universal no-go: D2 can use a much larger detector mass and different geometry, and better force PSD/integration can change the balance.

## 11. Current empirical boundary

Latest external anchors checked in Iteration 008:

- Pedalino et al., *Nature* 649, 866–870 (2026), DOI `10.1038/s41586-025-09917-9`: matter-wave interference of sodium nanoparticles above 170 kDa.
- Skrabulis et al., *PRL* 136, 233604 (2026), DOI `10.1103/9wzm-3qyb`: optically levitated impulse sensing below the zero-point momentum scale.
- Kamba et al., *PRL* 137, 050801 (2026), DOI `10.1103/js43-kq48`: levitated nano-accelerometer with approximately two orders sensitivity enhancement from trap quench.
- Wang et al., *PRL* 135, 120803 (2025), DOI `10.1103/z8b4-sm79`: proposed levitated mesoscopic gravity sensing.
- Ranjit et al., *PRA* 93, 053801 (2016), DOI `10.1103/PhysRevA.93.053801`: zeptonewton-scale levitated force sensing over long integration.

None implements RQIR.

## 12. Current detector ranking v0.8

### D1 matter-wave phase

**Pros**

- much stronger absolute gravitational-information scaling for the present micrometre source;
- directly senses potential;
- two-band nuisance breaking survives with designed modulation.

**Cons**

- passive full-period integration cancels the desired AC signal;
- needs finite-pulse lock-in/echo style sensitivity engineering;
- coherent source/probe mass requirement remains enormously beyond current free-particle interference masses.

### D2 mechanical force/acceleration

**Pros**

- current Toy 007 gradient response norm is 31% larger than the potential norm;
- two main bands are nearly ideally balanced;
- detector need not itself be a massive matter-wave superposition;
- mature mechanical sensing tools exist.

**Cons**

- absolute gravitational force/acceleration is extremely small;
- even an optimistic zN/sqrtHz force floor leaves a huge mass-product gap;
- a single narrow resonance can lose one of the two crucial bands.

### Conditional conclusion

For the **present** Toy 007 source and micrometre geometry, D1 is the stronger theoretical sensitivity route. D2 is more technologically mature but much farther away in absolute force sensitivity.

This ranking is conditional, not universal.

## 13. Current consistency gates

Still especially important:

- `G1` gauge/relational observables;
- `G2` conservation/Bianchi embedding;
- `G3/G3b` positivity/unitarity/spectral response;
- `G4a` causal retarded support;
- `G8` controlled Newtonian limit;
- `G9` EFT validity;
- `G10/G10a` stress-energy smearing/renormalization;
- `G12/G12a` classical/stochastic/full-QFT degeneracy audit;
- `G13` detector-level measurability, covariance and nuisance profiling.

## 14. Continuation-critical files

- `docs/MASTER_TABLE.md`
- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`
- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`
- `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`
- `analysis/toy007_finite_multiprobe_design.py`
- `analysis/rank_conditioning_scan.py`
- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`
- `analysis/protocol002b_physical_scaling.py`
- `analysis/detector_branch_d1_d2.py`
- `research_log/2026-08-29_iteration_008_detector_branches.md`

## 15. Exact next research target

### P1 — realizable D1 finite-pulse sequence

Replace instantaneous bang-bang switching with finite pulses/path switching; include contrast loss, dead time, phase cycling and timing jitter. Optimize two-band `P2,P4` rather than ideal source amplitudes.

### P2 — realistic D2 noise model

Build thermal force, backaction and displacement-imprecision PSD. Compare one-mode, dual-mode and sequentially tuned two-band sensing.

### P3 — source geometry co-optimization

Toy 007 geometry was inherited from potential calibration and was not optimized jointly for D1/D2 detector Fisher information. Re-optimize site/probe geometry for actual detector-level `F_beta|theta`.

### P4 — common coherence/resource budget

Compare D1 and D2 using one declared source mass, energy-gap scale, coherence time, separation and integration budget.

### P5 — interface-class fingerprints

After detector models stabilize, propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

### P6 — full relativistic stress-energy embedding

Before any fundamental claim, close source+apparatus conservation, gauge/relational and stress-tensor renormalization gates.

## 16. Continuation protocol

At each substantive iteration:

1. read this guide and the latest research log;
2. state the exact open target;
3. derive analytically before adding numerical complexity;
4. preserve negative/correction results rather than hiding them;
5. save reproducibility code for every numerical claim;
6. update `MASTER_TABLE.md` and this file when the project state changes;
7. never promote a toy-model or detector benchmark to empirical new physics.
