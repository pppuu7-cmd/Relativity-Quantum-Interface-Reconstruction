# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v0.7

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
- low-energy accessible channels before Planck-scale speculation;
- every numerical result gets reproducibility code;
- exact algebraic nulls are not confused with statistical identifiability.

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
\chi^R_{AB}=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A,T_B]\rangle
\]

under the current RQIR convention.

Parent source object:

\[
Z_T[J_+,J_-]=Tr(U[J_+]\rho_TU[J_-]^\dagger).
\]

Never collapse different orderings into one `C^(n)` unless an explicit identity/limit justifies it.

## 3. Working channels

- `Q1` quantum clocks / proper time;
- `Q2` superposed sources;
- `Q3` backreaction / source rule;
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
- **NP5:** NP4 plus complete source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction: Toy 007 = finite NP3.

NP grade is not experimental significance.

## 5. Result chain

### Toy 001 — same mean, different variance

`docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`

Equal mean mass can hide different covariance. Mean-vs-fluctuation discriminator only.

### RQIR-NG-001 / Toy 002 — static density phase blindness

`docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`

For orthogonal nonoverlapping mass branches with density-diagonal static coupling/readout, relative phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — same noise, different response, energy confound

`docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`

A qubit can have equal density mean/noise and opposite ordered response, but the same direction changes mean generator energy.

### Toy 004 — balanced five-level algebraic witness

`docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`  
`analysis/search_balanced_ordered_kernel.py`

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — exact Newtonian one-channel embedding

`docs/TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md`  
`analysis/search_real_newtonian_embedding.py`

For positive finite-dimensional `B=V diag(b_a)V^dagger`, choose localized one-particle modes at distances

\[
r_a=L/b_a
\]

from a fixed probe. Then

\[
\boxed{\Phi_p=-\frac{Gm}{L}B.}
\]

Toy 005 gives equal mean energy, equal complete chosen-potential mean history and equal chosen-potential symmetrized noise while ordered response differs. It is NP2 because other density combinations remain unmatched.

### RQIR-NG-003 / Toy 006 — complete density-history tomography

`docs/TOY_MODEL_006_DENSITY_HISTORY_TOMOGRAPHY_NO_GO.md`  
`analysis/check_density_history_tomography.py`

Under sufficient generic finite-mode conditions,

\[
span_R\{P_a(t)\}=Herm(d),
\]

so complete local-density history equality implies

\[
\rho_+=\rho_-.
\]

Complete exact tomography is therefore too strong for a distinct-state response-only null pair.

### Toy 007 — finite multiprobe NP3

`docs/TOY_MODEL_007_FINITE_MULTIPROBE_NULLSPACE_DESIGN.md`  
`analysis/toy007_finite_multiprobe_design.py`

Five-site source positions:

\[
x_a\approx(5.53112,2.21089,1.44295,1.27948,1.00000).
\]

Probe positions:

\[
y_0=0,
\qquad
y_1\approx-3.59552719.
\]

Accepted finite calibration:

\[
\boxed{r_{obs}=24/25},
\qquad
\boxed{\dim\ker A=1},
\qquad
\boxed{\eta_R\approx0.457682}.
\]

At

\[
t_R\approx3.583928899,
\]

\[
\langle B_0\rangle_+=\langle B_0\rangle_-\approx0.62153865,
\]

\[
N_{00,+}=N_{00,-}\approx0.00944118,
\]

but

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

Toy 007 is NP3 proof-of-principle, not experimental-ready.

### RQIR-NG-004 — exact-null saturation

`docs/STATISTICAL_IDENTIFIABILITY.md`

If

\[
rank(A)=p-1,
\qquad
ker(A)=span\{n\},
\]

then one added exact calibration row `a^T` with

\[
a^Tn\neq0
\]

raises the rank to `p` and eliminates all nonzero exact state-difference null pairs.

Scope: exact null-pair construction only.

### Toy 008 — soft-nullspace / Fisher transition

`docs/TOY_MODEL_008_SOFT_NULLSPACE_FISHER_TRANSITION.md`  
`analysis/rank_conditioning_scan.py`

Reproducible 300-design scan:

| rank | nullity | eta_R | s_min | condition |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0.696801 | 5.68468e-3 | 750.57 |
| 21 | 4 | 0.677521 | 5.43696e-3 | 803.96 |
| 22 | 3 | 0.638991 | 2.48186e-3 | 1801.88 |
| 23 | 2 | 0.607629 | 1.38924e-3 | 3271.43 |
| 24 | 1 | 0.473850 | 1.56388e-3 | 2965.14 |

Inside this design family, forcing nullity one is not automatically optimal for response survival plus conditioning.

## 6. Statistical identifiability core

File:

`docs/STATISTICAL_IDENTIFIABILITY.md`

For noisy calibration

\[
y_c=\mu_c+A\theta+\epsilon_c,
\qquad
Cov(\epsilon_c)=\Sigma_c,
\]

\[
\boxed{F_c=A^T\Sigma_c^{-1}A.}
\]

Whitened singular vectors of

\[
\tilde A=\Sigma_c^{-1/2}A
\]

are strongly/weakly constrained source directions.

For parameter of interest `beta` and nuisances `theta`,

\[
\boxed{
F_{\beta|\theta}
=F_{\beta\beta}
-F_{\beta\theta}F_{\theta\theta}^{-1}F_{\theta\beta}.
}
\]

Geometrically,

\[
\boxed{
F_{\beta|\theta}=\|(I-P_J)\tilde s\|^2.
}
\]

Only the whitened detector signal component outside the nuisance derivative span is locally identifiable.

### RQIR-CAL-001 — calibration monotonicity

If added statistically independent calibration is `beta`-blind and contributes `C >= 0` only to the nuisance Fisher block, then under positive-definite nuisance information

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

Thus more exact constraints can kill a constructed null pair while more noisy independent calibration can improve actual inference.

Code:

`analysis/toy007_fisher_calibration_demo.py`.

## 7. Transfer Layer 001 — source → gravity → detector

`docs/LINEAR_RESPONSE_TRANSFER.md`

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

Potential noise:

\[
\boxed{
N_\Phi
=\mathcal R_{\Phi\rho}^R*N_\rho*\mathcal R_{\Phi\rho}^A
+\mathcal D_\Phi^R*N_\Phi^{intr}*\mathcal D_\Phi^A.
}
\]

Detector:

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R,
\]

\[
N_D^{obs}=R_D^R*N_\Phi*R_D^A+N_D.
\]

Source-side `D/chi^R != 0` is not yet an observable gravitational discriminator.

## 8. Protocol 001 — weak pump / phase scaling

`docs/PROBE_PROTOCOL_001_PUMP_PROBE_PHASE.md`

For weak source impulse area

\[
\alpha=\frac{m_s}{\hbar}\int A(t)dt,
\]

Toy 007 target-time response difference gives

\[
|\Delta\delta B_0|\approx0.0422625|\alpha|.
\]

Simple phase scaling:

\[
|\Delta\varphi|
\sim0.0422625|\alpha|\frac{Gm_sm_pT}{\hbar L_0}.
\]

## 9. Protocol 002 — two-harmonic profiled Fisher

Files:

- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`
- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`

Dominant selected response coefficients:

\[
H_2=-2.718331e{-4}-i7.661385e{-3},
\]

\[
H_4=1.209428e{-3}-i9.061082e{-3}.
\]

Two-harmonic norm:

\[
H_{24}\approx1.19305\times10^{-2}.
\]

Relative power imbalance:

\[
\kappa
=\frac{|H_4|^2-|H_2|^2}{|H_4|^2+|H_2|^2}
\approx0.174201,
\]

so

\[
1-\kappa^2\approx0.969654.
\]

Minimal detector model:

\[
Z_n=g\beta H_n(1+q w_n)e^{in\tau},
\qquad
w_2=-1,
w_4=+1.
\]

For response SNR squared `S=rho_R^2` and independent static common-amplitude calibration `C=rho_C^2`, profiling common gain, relative spectral tilt and timing gives

\[
\boxed{
F_{\beta|g,q,\tau}
=\frac{S(1-\kappa^2)C}{S(1-\kappa^2)+C}.
}
\]

One harmonic with the same free relative-tilt nuisance has `|kappa|=1` and zero identifiable common-amplitude information. The second harmonic therefore breaks a shape degeneracy, not merely adds SNR.

## 10. Protocol 002B — physical scaling

Files:

- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `analysis/protocol002b_physical_scaling.py`

Define

\[
\Gamma_G=\frac{Gm_sm_pT_D}{\hbar L_0}.
\]

Simple matter-wave response:

\[
\Delta\varphi_n=2\alpha\Gamma_GH_n.
\]

Equal-quadrature phase-noise response SNR:

\[
\rho_R=\frac{2|\alpha|\Gamma_GH_{24}}{\sigma_\varphi}.
\]

Static Toy 007 mean:

\[
\bar B_0\approx0.621539.
\]

For `alpha=0.1` and comparable static/harmonic phase noise,

\[
\rho_C/\rho_R\approx260.5,
\]

so the idealized model is close to response-limited once static calibration is clean.

Five-sigma benchmark for

\[
\alpha=0.1,
\quad
\sigma_\varphi=1\,mrad,
\quad
L_0=10\,\mu m,
\quad
T_D=1s:
\]

\[
\Gamma_G\gtrsim2.128,
\]

\[
\boxed{m_sm_p\gtrsim3.36\times10^{-29}\,kg^2.}
\]

Equal-mass illustration:

\[
\boxed{m_s=m_p\gtrsim5.80\times10^{-15}\,kg.}
\]

This is not an experimental-readiness claim.

Source gap scale:

\[
\omega_n=nE_*/\hbar,
\qquad
T_*=2\pi\hbar/E_*.
\]

For one-period interaction,

\[
\Gamma_G\sim2\pi Gm_sm_p/(E_*L_0).
\]

Mass, gap scale and coherence time must therefore be optimized together.

## 11. Protocol 002C — colored detector law

`docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`

After full detector transfer and whitening, define

\[
P_n=|s_n|^2/\sigma_n^2.
\]

For the free antisymmetric spectral-tilt nuisance,

\[
\kappa_w=(P_4-P_2)/(P_4+P_2)
\]

and

\[
\boxed{
S_{eff}
=\frac{4P_2P_4}{P_2+P_4}.
}
\]

With static calibration information `C`,

\[
\boxed{
F_{\beta|\theta}=\frac{S_{eff}C}{S_{eff}+C}.
}
\]

At fixed total two-band information, robustness is maximal for balanced **whitened** powers. If either band is lost after colored detector transfer/noise, `S_eff -> 0`.

## 12. Current empirical boundary

Recent literature checked on 2026-08-29:

- 2026 Nature: nanoparticle matter-wave interference for sodium clusters above 170 kDa (~2.8e-22 kg), with large spatial delocalization relative to particle size.
- 2025 levitated-nanoparticle experiments demonstrate increased quantum delocalization/control but not the RQIR five-level gravity protocol.
- 2025/2026 QGEM-style design work targets nanodiamond masses around `1e-15 kg` with micrometre-scale superpositions; these are target designs, not completed gravity-mediated-entanglement observations.

Thus the current symmetric Protocol 002B benchmark is many orders above present free nanoparticle-interference masses but lies in the broad mesoscopic mass range of ambitious gravity-superposition proposals.

Do not confuse mass-range overlap with implementability of the required Toy 007 Hamiltonian/coherence.

## 13. Critical external boundaries

- stochastic gravity already contains matter-induced noise and dissipation/response; nonzero `N` or `chi^R` does not prove quantum geometry;
- classical gravity + full QFT matter can generate entanglement in suitable constructions; entanglement alone is not a unique quantum-gravity witness;
- low-energy quantum-GR EFT remains a compulsory consistency anchor.

## 14. Current consistency gates

Especially important:

- `G1` gauge/relational observables;
- `G2` conservation/Bianchi embedding;
- `G3/G3b` positivity/unitarity/spectral identities;
- `G4a` retarded causal support;
- `G8` controlled Newtonian limit;
- `G9` EFT power counting;
- `G10/G10a` stress-tensor smearing/renormalization;
- `G12/G12a` classical/stochastic/full-QFT degeneracy audit;
- `G13` detector-level likelihood and covariance.

## 15. Current repository core additions

In addition to Toys 001–007 and foundations, the current continuation-critical files are:

- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `docs/TOY_MODEL_008_SOFT_NULLSPACE_FISHER_TRANSITION.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/PROBE_PROTOCOL_001_PUMP_PROBE_PHASE.md`
- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`
- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`
- `analysis/rank_conditioning_scan.py`
- `analysis/toy007_fisher_calibration_demo.py`
- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`
- `analysis/protocol002b_physical_scaling.py`
- `research_log/2026-08-29_iteration_007_fisher_and_protocol002.md`

## 16. Exact next research target

Evaluate **two concrete detector branches** rather than optimizing a generic detector forever:

### Branch D1 — matter-wave phase interferometer

Derive or adopt a realistic frequency response and phase covariance for the two harmonics, including finite interrogation window and phase noise.

### Branch D2 — levitated/mechanical force or displacement sensor

Use a mechanical susceptibility

\[
\chi_m(\omega)
\]

and force/displacement noise PSD to compute whitened `P2,P4`.

For each branch perform

\[
H_n^{source}
\to
\mathcal R_{\Phi\rho}^R(\omega_n)
\to
R_D^R(\omega_n)
\to
P_n
\to
F_{\beta|\theta}.
\]

Then compare which detector class retains both harmonics with the highest nuisance-profiled information under realistic resource constraints.

After that, compare at least semiclassical/stochastic and one alternative interface class in the same detector likelihood.

## 17. Continuation protocol

At each substantive iteration:

1. read this guide and the latest research log;
2. state one exact unresolved target;
3. derive analytically before adding numerical complexity;
4. run applicable consistency gates;
5. retain positive and negative results;
6. record reproducibility code;
7. update `MASTER_TABLE.md` and this guide when the project state changes;
8. never promote a toy result or normalized Fisher calculation to empirical evidence.
