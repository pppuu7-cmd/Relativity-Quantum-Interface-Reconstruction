# RQIR Operational Master Table

**Version:** 0.7  
**Date:** 2026-08-29

This table is deliberately conservative. `OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy/no-go | Current discriminant strategy | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase can mimic interface effects unless source/control nuisances are constrained | profiled multi-clock likelihood + source/control calibration | OPEN |
| Q2 Superposed sources | probe phase/force/potential spectra | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch/hybrid, quantum mediator | static density is phase-blind; complete density history can become tomography | finite multiprobe calibration + source→gravity→detector transfer + profiled likelihood | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | semiclassical Einstein / Einstein–Langevin | stochastic gravity, classical gravity + full QFT matter, hybrid/collapse, quantized metric | equal selected mean+noise need not fix response; exact null geometry differs from statistical identifiability | multi-frequency detector `F_{beta|theta}` with calibrated source/detector nuisances | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, non-Gaussianity, visibility, scaling | common low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement alone is not unique to quantized gravity | common likelihood over scaling/order + force/noise/response channels | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise and response spectra | detector/environment noise + matter-induced metric fluctuations | stochastic induced fluctuations, intrinsic quantum geometry, technical noise | nonzero noise is not diagnostic | joint source `N`, source `chi^R`, intrinsic-gravity noise and detector covariance fit | HIGH PRIORITY |
| Q6 Causal/process structure | causal-order/process and relational timing observables | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | control-system nonclassicality can masquerade as gravity structure | gravity-dependent scaling + profiled control-system nuisances | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | classical GR + SM/QFT | perturbative QG EFT, local higher-curvature terms, classical systematics | universal nonanalytic pieces tiny; local terms absorb UV dependence | cross-process nonanalytic/long-range fingerprint | OPEN |

---

## 1. Current mathematical source coordinate

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

The parent source object is the Schwinger–Keldysh / CTP generating functional `Z_T[J_+,J_-]`.

---

## 2. Closed result chain

### RQIR-NG-001 / Toy 002 — static density phase blindness

Relative phase between orthogonal nonoverlapping mass branches is invisible to density-diagonal static gravitational readout when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — minimal response split has energy confound

Equal density mean/noise plus opposite response is possible in a qubit, but the same state direction changes mean generator energy.

### Toy 004 — balanced algebraic witness

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — Newtonian single-channel physical embedding

For positive `B=V diag(b_a)V^dagger`, choose one-particle localized modes at distances `r_a=L/b_a`, giving

\[
\Phi_p=-\frac{Gm}{L}B.
\]

Thus equal selected potential mean/noise need not determine its ordered response.

### RQIR-NG-003 / Toy 006 — complete density-history tomography

Under sufficient generic finite-mode conditions,

\[
span_R\{P_a(t)\}=Herm(d),
\]

so complete density-history equality implies identical states.

### Toy 007 — finite NP3 multiprobe nullspace

\[
r_{obs}=24/25,
\qquad
\eta_R\approx0.457682.
\]

At the target time:

\[
\langle B_0\rangle_+=\langle B_0\rangle_-,
\qquad
N_{00,+}=N_{00,-},
\]

but

\[
D_{00,+}\approx-0.0105656,
\qquad
D_{00,-}\approx+0.0105656.
\]

Conditioning:

\[
s_{min}\approx1.46\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004 — exact-null saturation

If exact calibration has rank `p-1` and null vector `n`, one additional exact row with nonzero overlap with `n` raises the rank to `p` and eliminates every nonzero exact state-difference null pair.

This does **not** mean additional noisy calibration worsens inference.

### Toy 008 — soft-nullspace scan

Reproducible 300-design scan:

| rank | nullity | eta_R | s_min | condition |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0.696801 | 5.68468e-3 | 750.57 |
| 21 | 4 | 0.677521 | 5.43696e-3 | 803.96 |
| 22 | 3 | 0.638991 | 2.48186e-3 | 1801.88 |
| 23 | 2 | 0.607629 | 1.38924e-3 | 3271.43 |
| 24 | 1 | 0.473850 | 1.56388e-3 | 2965.14 |

Inside this scan family, maximal exact rank is not automatically optimal for response survival plus conditioning.

---

## 3. Statistical identifiability core

For noisy calibration

\[
y_c=\mu_c+A\theta+\epsilon_c,
\qquad
Cov(\epsilon_c)=\Sigma_c,
\]

\[
F_c=A^T\Sigma_c^{-1}A.
\]

For parameter of interest `beta` and nuisance coordinates `theta`,

\[
\boxed{
F_{\beta|\theta}
=F_{\beta\beta}
-F_{\beta\theta}F_{\theta\theta}^{-1}F_{\theta\beta}.
}
\]

After whitening,

\[
\boxed{
F_{\beta|\theta}=\|(I-P_J)\tilde s\|^2.
}
\]

Only the detector signal component outside the nuisance derivative span is identifiable.

### RQIR-CAL-001 — calibration monotonicity

Independent `beta`-blind calibration contributes `C>=0` to the nuisance block and, under the declared positive-definite Fisher assumptions,

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

Files:

- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `analysis/toy007_fisher_calibration_demo.py`

---

## 4. Transfer Layer 001

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

Detector response/noise:

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R,
\]

\[
N_D^{obs}=R_D^R*N_\Phi*R_D^A+N_D.
\]

A source-side response split is not an observable gravity discriminator until it survives this transfer and nuisance profiling.

---

## 5. Protocol 002 — two-harmonic detector likelihood

Dominant selected source-response harmonics:

\[
H_2=-2.718331\times10^{-4}-i7.661385\times10^{-3},
\]

\[
H_4=1.209428\times10^{-3}-i9.061082\times10^{-3}.
\]

\[
H_{24}=\sqrt{|H_2|^2+|H_4|^2}
\approx1.19305\times10^{-2}.
\]

Power imbalance:

\[
\kappa
=\frac{|H_4|^2-|H_2|^2}{|H_4|^2+|H_2|^2}
\approx0.174201,
\]

\[
1-\kappa^2\approx0.969654.
\]

Minimal model:

\[
Z_n=g\beta H_n(1+qw_n)e^{in\tau},
\qquad
w_2=-1,
w_4=+1.
\]

With response information `S=rho_R^2` and independent static amplitude calibration `C=rho_C^2`, profiling common amplitude, relative spectral tilt and timing gives

\[
\boxed{
F_{\beta|g,q,\tau}
=\frac{S(1-\kappa^2)C}{S(1-\kappa^2)+C}.
}
\]

A single harmonic with the same unconstrained relative-tilt nuisance has zero identifiable common-amplitude information; the second harmonic therefore breaks a spectral-shape degeneracy.

Files:

- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`
- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`

---

## 6. Protocol 002B — physical scaling

Define

\[
\Gamma_G=\frac{Gm_sm_pT_D}{\hbar L_0}.
\]

Simple matter-wave response:

\[
\Delta\varphi_n=2\alpha\Gamma_GH_n.
\]

Response SNR for equal quadrature noise:

\[
\rho_R=\frac{2|\alpha|\Gamma_GH_{24}}{\sigma_\varphi}.
\]

Toy 007 static mean is

\[
\bar B_0\approx0.621539.
\]

For `alpha=0.1` and comparable static/harmonic phase noise,

\[
\rho_C/\rho_R\approx260.5.
\]

Five-sigma benchmark for `alpha=0.1`, `sigma_phi=1 mrad`, `L0=10 um`, `T_D=1 s`:

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

This is a scaling benchmark, not an experimental-readiness claim.

Files:

- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `analysis/protocol002b_physical_scaling.py`

---

## 7. Protocol 002C — colored detector design law

After full gravity+detector transfer and whitening, define

\[
P_n=|s_n|^2/\sigma_n^2.
\]

For the antisymmetric relative spectral-tilt nuisance,

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

Consequences:

- if one whitened band is lost, `S_eff -> 0`;
- at fixed total two-band information, robustness is maximal for balanced whitened powers;
- detector transfer/noise must therefore be evaluated before calling the source waveform discriminating.

File:

- `docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`

---

## 8. Current empirical boundary

Recent literature checked in this iteration places current free nanoparticle matter-wave interference around `170 kDa ~ 2.8e-22 kg`, while ambitious QGEM-style nanodiamond designs target masses around `1e-15 kg` and micrometre-scale superpositions. The Protocol 002B symmetric benchmark is therefore far above present free-particle interference masses but in the broad mesoscopic mass neighborhood of proposed gravity-superposition platforms.

No implementation claim is made: Toy 007 additionally requires controlled five-level coherent dynamics and a suitable source gap scale.

---

## 9. Current priority ranking v0.7

### P1 — Detector Branch D1: matter-wave interferometer

Derive frequency response, finite interrogation-window effects and realistic phase covariance at `2 omega_*` and `4 omega_*`; compute `P2,P4,F_{beta|theta}`.

### P2 — Detector Branch D2: levitated/mechanical sensor

Use mechanical susceptibility `chi_m(omega)` and force/displacement noise PSD to compute the same whitened two-harmonic information.

### P3 — compare D1 vs D2

Choose neither a priori. Compare profiled information per physical resource, coherence requirement and nuisance burden.

### P4 — class-by-class interface prediction

Run at least semiclassical/stochastic and one alternative interface class through the same detector likelihood.

### P5 — relativistic/full-stress embedding

Close conservation/Bianchi/gauge and apparatus stress-energy gates before any fundamental claim.

---

## 10. Continuation-critical files

- `docs/RECOVERY_GUIDE.md`
- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `docs/TOY_MODEL_008_SOFT_NULLSPACE_FISHER_TRANSITION.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`
- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`
- `analysis/rank_conditioning_scan.py`
- `analysis/toy007_fisher_calibration_demo.py`
- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`
- `analysis/protocol002b_physical_scaling.py`
- `research_log/2026-08-29_iteration_007_fisher_and_protocol002.md`

---

## 11. Exact next iteration

Evaluate detector branches D1 and D2 under the same pipeline:

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

The first branch comparison must use the same source waveform and the same interface parameter definition so that detector preference is based on observable information rather than inconsistent normalizations.
