# RQIR Operational Master Table

**Version:** 0.8  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main degeneracy / current obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, clock correlations | ordinary relativistic/control effects can mimic interface residuals | profiled likelihood with explicit source/control calibration | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static density is phase-blind; complete density history becomes tomography | finite multiprobe calibration + detector transfer + multi-band inference | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | equal selected mean+noise need not determine response; source response may vanish after detector transfer | common source→gravity→detector Fisher pipeline | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, non-Gaussianity, scaling | entanglement alone not unique to quantized gravity | common likelihood over force/noise/response/entanglement scaling | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise and response spectra | matter-induced, intrinsic-gravity and technical noise can be degenerate | joint `N`, `chi^R`, intrinsic-gravity and detector covariance fit | HIGH PRIORITY |
| Q6 Causal/process | relational timing/process observables | control-system nonclassicality can mimic gravity structure | gravity-dependent scaling with nuisance closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | universal pieces tiny, local UV terms degenerate | cross-process nonanalytic/long-range fingerprint | OPEN |

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

The parent source object remains the Schwinger–Keldysh / CTP generating functional.

---

## 2. Closed result chain

### RQIR-NG-001 / Toy 002

Static density-diagonal gravity is blind to relative phase between orthogonal nonoverlapping mass branches when diagonal statistics match.

### RQIR-NG-002 / Toy 003

A qubit can have equal density mean/noise and opposite response, but the same state direction changes mean generator energy.

### Toy 004

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005

Any positive finite-dimensional `B` admits an exact one-channel Newtonian embedding

\[
\Phi_p=-\frac{Gm}{L}B.
\]

### RQIR-NG-003 / Toy 006

Under sufficient generic finite-mode conditions, complete time-resolved local-density matching is informationally complete and forces identical states.

### Toy 007

Finite NP3 source design:

\[
r_{obs}=24/25,
\qquad
\eta_R\approx0.457682,
\]

with equal selected mean/noise but opposite target commutator response. Exact conditioning remains poor:

\[
s_{min}\approx1.46\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004

A one-dimensional *exact* nullspace is destroyed by one additional exact calibration row with nonzero overlap with its null vector. This is an exact-null statement, not an inference statement.

### Toy 008

Soft-null scan shows that, within the tested design family, forcing nullity one is not automatically optimal for response survival and conditioning.

---

## 3. Statistical identifiability core

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
\boxed{F_{\beta|\theta}=\|(I-P_J)\tilde s\|^2.}
\]

Only the detector signal component outside the nuisance tangent span is identifiable.

### RQIR-CAL-001

Independent `beta`-blind calibration contributes positive semidefinite nuisance information and cannot reduce profiled Fisher information under the declared regularity assumptions.

---

## 4. Transfer Layer 001

Bare Newtonian density-to-potential kernel:

\[
R_G(k)=-4\pi G/k^2.
\]

Dressed response:

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

A source-side response split is not yet an observable gravity discriminator.

---

## 5. Protocol 002 — two-harmonic likelihood

Potential-response harmonics:

\[
H_2\approx-2.71833\times10^{-4}-i7.66139\times10^{-3},
\]

\[
H_4\approx1.20943\times10^{-3}-i9.06108\times10^{-3}.
\]

\[
H_{24}\approx1.19305\times10^{-2},
\qquad
\kappa_B\approx0.174201.
\]

With free antisymmetric relative spectral tilt and static common-amplitude calibration,

\[
F_{\beta|\theta}
=\frac{S(1-\kappa_B^2)C}{S(1-\kappa_B^2)+C}.
\]

One harmonic alone is degenerate with the free tilt nuisance; two harmonics break that degeneracy.

Colored detector law:

\[
\boxed{S_{eff}=\frac{4P_2P_4}{P_2+P_4}.}
\]

If one whitened band is lost, identifiable two-band information vanishes.

---

## 6. Detector Branch Comparison 001 — D1 vs D2

File: `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`  
Code: `analysis/detector_branch_d1_d2.py`

### D1 — matter-wave phase

General windowed phase response:

\[
\Delta\varphi_n
=2\alpha\frac{Gm_sm_pT_D}{\hbar L_0}
H_n\mathcal W_n.
\]

#### RQIR-D1-001 — full-period window cancellation

Uniform phase accumulation over exactly one complete source period has

\[
\mathcal W_2=\mathcal W_4=0.
\]

Thus Protocol 002B is an ideal matched-readout scale, not a passive full-period interferometer.

A simple bounded dual-band lock-in

\[
g(\tau)=sign[\cos2\tau+1.046\cos4\tau]
\]

gives approximately

\[
|W_2|\approx0.440,
\qquad
|W_4|\approx0.385.
\]

It retains about `17.2%` of ideal two-band Fisher information (`41.5%` SNR amplitude).

Revised five-sigma illustration under the same `alpha=0.1`, `L0=10 um`, `T=1 s`, `sigma_phi=1 mrad` assumptions:

\[
\boxed{m_sm_p\gtrsim8.1\times10^{-29}\,kg^2}
\]

or equal-mass illustration

\[
\boxed{m\gtrsim9.0\times10^{-15}\,kg.}
\]

This is not experimental readiness.

### D2 — mechanical force/acceleration

Gradient operator:

\[
G_0=\partial_yB|_{0}=\sum_a x_a^{-2}n_a.
\]

Dominant cross-response harmonics to the same `B0` pump:

\[
G_2\approx-6.78211\times10^{-4}-i1.14277\times10^{-2},
\]

\[
G_4\approx1.41626\times10^{-3}-i1.06107\times10^{-2}.
\]

\[
\boxed{G_{24}\approx1.56731\times10^{-2}}
\]

which is about `1.314` times the D1 dimensionless norm.

Spectral balance is excellent:

\[
\boxed{\kappa_G\approx-0.06701,}
\qquad
\boxed{1-\kappa_G^2\approx0.99551.}
\]

Force harmonics:

\[
\Delta F_n=2\alpha\frac{Gm_sm_p}{L_0^2}G_n.
\]

Equivalent-force noise:

\[
S_F^{eq}=S_F^{th}+S_x^{imp}/|\chi_m|^2.
\]

#### RQIR-D2-001 — resonance-gain cancellation at the force-noise floor

When physical force noise dominates, mechanical susceptibility amplifies both displacement signal and displacement noise, so `chi_m` cancels from whitened force information. Resonance helps mainly against readout imprecision, not against a true force-noise floor.

At an optimistic detector-agnostic `1 zN/sqrtHz` equivalent-force benchmark with `alpha=0.1`, `L0=10 um`, `T=1 s`, five-sigma requires

\[
\boxed{m_sm_p\gtrsim2.40\times10^{-18}\,kg^2.}
\]

This is about `3e10` times the revised D1 mass-product benchmark.

### Conditional branch ranking v0.8

- **D1:** much stronger absolute gravitational-information scaling, but needs deliberately modulated AC sensitivity and coherent masses far beyond the current free-particle matter-wave record.
- **D2:** cleaner two-band shape and mature force/acceleration technology, but current force scales are vastly too weak for the present micrometre Toy 007 source.

No universal detector no-go is claimed.

---

## 7. Current empirical boundary

External anchors retained:

- Pedalino et al., Nature 649, 866–870 (2026): matter-wave interference above 170 kDa.
- Skrabulis et al., PRL 136, 233604 (2026): levitated nanomechanical impulse sensing below the zero-point momentum scale.
- Kamba et al., PRL 137, 050801 (2026): levitated nano-accelerometer with about two orders sensitivity enhancement from quench dynamics.
- Wang et al., PRL 135, 120803 (2025): proposed levitated nanodiamond gravity sensing.
- Ranjit et al., PRA 93, 053801 (2016): zeptonewton-scale levitated force sensing over long integration.

None implements RQIR.

---

## 8. Priority ranking v0.8

### P1 — realizable D1 sensitivity function

Replace ideal bang-bang switching by finite pulses / path switching, include contrast loss, dead time and phase-cycling, then recompute `P2,P4,F_beta|theta`.

### P2 — realistic D2 equivalent-force PSD

Build thermal-force + backaction + imprecision model. Compare one-mode, dual-mode and sequentially tuned two-band readout.

### P3 — source-geometry co-optimization

Toy 007 geometry was optimized for a finite potential calibration, not jointly for D1 and D2 detector information. Re-optimize site/probe geometry for detector-level Fisher information.

### P4 — common source coherence budget

Compare D1 and D2 under one declared source mass, gap scale, coherence time and geometry budget.

### P5 — interface-class comparison

Only after detector transfer is stable, compare semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG fingerprints in the same likelihood.

### P6 — relativistic/full-stress embedding

Conservation/Bianchi/gauge/apparatus stress-energy gates remain mandatory before any fundamental claim.
