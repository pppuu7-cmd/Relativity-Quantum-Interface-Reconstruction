# RQIR Research Log — Iteration 007

**Date:** 2026-08-29  
**Phase:** exact-nullspace → statistical identifiability → first detector-level profiled protocol

## Objective

Replace the over-strong exact-nullspace experiment-design objective by covariance/Fisher geometry, formalize the exact-null saturation result, and build the first multi-frequency detector-level nuisance-profiled discriminator from the Toy 007 response waveform.

---

## Completed

### ✅ Reproducible soft-nullspace rank/conditioning scan

New code:

- `analysis/rank_conditioning_scan.py`

A deterministic 300-design scan on the Toy 005/007 five-site source found the following best designs under the exploratory score

\[
J_{scan}=\eta_R\sqrt{s_{min}}.
\]

| rank | nullity | eta_R | s_min | condition |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0.696801 | 5.68468e-3 | 750.57 |
| 21 | 4 | 0.677521 | 5.43696e-3 | 803.96 |
| 22 | 3 | 0.638991 | 2.48186e-3 | 1801.88 |
| 23 | 2 | 0.607629 | 1.38924e-3 | 3271.43 |
| 24 | 1 | 0.473850 | 1.56388e-3 | 2965.14 |

Interpretation: inside this scan family, forcing exact nullity one is not automatically best for response survival plus conditioning.

This is numerical design evidence only, not a global optimum theorem.

---

### ✅ RQIR-NG-004 — exact-null saturation theorem

For exact calibration

\[
A\delta\theta=0,
\qquad
\operatorname{rank}A=p-1,
\qquad
\ker A=span\{n\},
\]

one added exact row `a^T` satisfying

\[
a^Tn\neq0
\]

raises the rank to `p` and forces

\[
\delta\theta=0.
\]

Meaning: a one-dimensional exact state-difference null pair is destroyed by any genuinely independent additional exact constraint.

Important scope: this applies to **exact null-pair construction**, not to statistical inference.

Document:

- `docs/STATISTICAL_IDENTIFIABILITY.md`

---

### ✅ Exact-null geometry separated from statistical identifiability

For noisy calibration

\[
y_c=\mu_c+A\theta+\epsilon_c,
\qquad
Cov(\epsilon_c)=\Sigma_c,
\]

define

\[
F_c=A^T\Sigma_c^{-1}A.
\]

The whitened singular spectrum of

\[
\tilde A=\Sigma_c^{-1/2}A
\]

replaces binary rank by strongly/weakly constrained source directions.

For parameter of interest `beta` and nuisances `theta`,

\[
F_{\beta|\theta}
=F_{\beta\beta}
-F_{\beta\theta}F_{\theta\theta}^{-1}F_{\theta\beta}.
\]

Geometrically,

\[
F_{\beta|\theta}=\|(I-P_J)\tilde s\|^2.
\]

Only the whitened detector signal component that cannot be reproduced by nuisance variation is locally identifiable.

---

### ✅ RQIR-CAL-001 — calibration monotonicity theorem

If independent added calibration is `beta`-blind and contributes

\[
C\succeq0
\]

to the nuisance Fisher block, then for positive-definite nuisance information

\[
(F_{\theta\theta}+C)^{-1}\preceq F_{\theta\theta}^{-1}
\]

and therefore

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

This resolves the Toy 006/007 apparent paradox:

- more exact constraints can kill a specially constructed distinct-state null pair;
- more independent noisy calibration can improve actual parameter identifiability.

Code demonstration:

- `analysis/toy007_fisher_calibration_demo.py`

The accepted rank-24 Toy 007 calibration gives zero local profile information for a deliberately scalar target model whose nuisance response has a component along the exact null direction.  Adding a calibration row with nonzero null overlap restores positive information.

---

### ✅ Toy 008 documented

New document:

- `docs/TOY_MODEL_008_SOFT_NULLSPACE_FISHER_TRANSITION.md`

Main methodological conclusion:

\[
\boxed{
\text{maximize detector-level profiled information, not exact nullity.}
}
\]

---

## Protocol 002 — first detector-level profiled harmonic likelihood

### ✅ Two dominant harmonic response retained

From the existing response-spectrum calculation, the selected complex source-response coefficients are

\[
H_2
=-2.718331\times10^{-4}
-i7.661385\times10^{-3},
\]

\[
H_4
=1.209428\times10^{-3}
-i9.061082\times10^{-3}.
\]

Two-harmonic norm:

\[
H_{24}\approx1.19305\times10^{-2}.
\]

Within the selected pair,

\[
p_2\approx0.4129,
\qquad
p_4\approx0.5871.
\]

---

### ✅ Minimal nuisance model

Detector data vector:

\[
(C,ReZ_2,ImZ_2,ReZ_4,ImZ_4).
\]

Parameter of interest:

- `beta`: ordered-response/interface transfer amplitude.

Nuisances:

- common amplitude `g`;
- relative spectral tilt `q` with weights `(-1,+1)`;
- timing/phase offset `tau`.

The response model is

\[
Z_n=g\beta H_n(1+qw_n)e^{in\tau}.
\]

The static calibration constrains `g` but has no direct `beta` dependence.

---

### ✅ Closed-form profiled Fisher result

Define

\[
S=\rho_R^2,
\qquad
C=\rho_C^2,
\]

and

\[
\kappa
=\frac{|H_4|^2-|H_2|^2}{|H_4|^2+|H_2|^2}
\approx0.174201.
\]

Then

\[
1-\kappa^2\approx0.969654.
\]

After profiling common amplitude, spectral tilt and timing under circular quadrature noise,

\[
\boxed{
F_{\beta|g,q,\tau}
=\frac{S(1-\kappa^2)C}
{S(1-\kappa^2)+C}.
}
\]

This is the first closed detector-level RQIR nuisance-profiled discriminator.

Files:

- `docs/PROBE_PROTOCOL_002_TWO_HARMONIC_PROFILED_FISHER.md`
- `analysis/protocol002_profiled_fisher.py`

---

### ✅ Two harmonics break a shape nuisance that one harmonic cannot

With one harmonic and a free relative-amplitude/tilt nuisance,

\[
|\kappa|=1,
\]

so

\[
F_{\beta|\theta}=0.
\]

For the Toy 007 pair,

\[
1-\kappa^2\approx0.969654,
\]

so only about 3% of raw two-harmonic response information is lost to this nuisance in the idealized covariance model.

Interpretation: the second harmonic is not merely extra SNR; it breaks a spectral-shape degeneracy.

---

## Protocol 002B — physical scaling

New files:

- `docs/PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md`
- `analysis/protocol002b_physical_scaling.py`

For pump area `alpha`, source mass `m_s`, probe mass `m_p`, effective interaction time `T_D` and length `L0`,

\[
\Gamma_G
=\frac{Gm_sm_pT_D}{\hbar L_0}.
\]

The selected harmonic phase amplitudes obey

\[
\Delta\varphi_n
=2\alpha\Gamma_GH_n
\]

in the first common-`T_D` matter-wave model.

For equal per-quadrature phase noise `sigma_phi`,

\[
\rho_R
=\frac{2|\alpha|\Gamma_GH_{24}}{\sigma_\varphi}.
\]

Static mean channel at Toy 007 has

\[
\bar B_0\approx0.621539.
\]

If static and harmonic phase noise are comparable and `alpha=0.1`,

\[
\rho_C/\rho_R\approx260.5.
\]

Thus the idealized model is naturally near the strong-calibration regime.

### Five-sigma benchmark

For

\[
Z=5,
\quad
\alpha=0.1,
\quad
\sigma_\varphi=10^{-3}\,rad,
\]

strong calibration requires

\[
\Gamma_G\gtrsim2.128.
\]

At

\[
L_0=10\,\mu m,
\qquad
T_D=1\,s,
\]

this becomes

\[
\boxed{m_sm_p\gtrsim3.36\times10^{-29}\,kg^2.}
\]

For equal masses,

\[
\boxed{m_s=m_p\gtrsim5.80\times10^{-15}\,kg.}
\]

This is only a scaling benchmark, not an experimental-readiness claim.

---

## Protocol 002C — colored detector law

New document:

- `docs/PROBE_PROTOCOL_002C_COLORED_TWO_HARMONIC_DESIGN.md`

After full gravity+detector transfer, define whitened per-band powers

\[
P_n=\frac{|s_n|^2}{\sigma_n^2}.
\]

For the same antisymmetric relative-tilt nuisance,

\[
\kappa_w=\frac{P_4-P_2}{P_4+P_2}
\]

and

\[
\boxed{
S_{eff}
=(P_2+P_4)(1-\kappa_w^2)
=\frac{4P_2P_4}{P_2+P_4}.
}
\]

With static calibration information `C`,

\[
\boxed{
F_{\beta|\theta}
=\frac{S_{eff}C}{S_{eff}+C}.
}
\]

Design implication:

- if either whitened band disappears, `S_eff -> 0`;
- at fixed total two-band information, robustness is maximal for balanced whitened powers.

The detector must therefore preserve both spectral channels after transfer/noise whitening.

---

## External feasibility boundary checked this iteration

Recent literature checked during this iteration:

- 2026 Nature nanoparticle matter-wave interference reports sodium clusters above 170 kDa (~2.8e-22 kg) in widely delocalized matter-wave states.
- 2025/2026 levitated-nanoparticle work demonstrates increasing quantum control/delocalization at larger masses but not the exact RQIR source architecture.
- current QGEM-style design papers target nanodiamond masses around 1e-15 kg with micrometre-scale superpositions; these remain experimental targets rather than completed gravity-mediated-entanglement demonstrations.

Interpretation: the symmetric `5.8e-15 kg` benchmark is many orders above current free nanoparticle matter-wave-interference masses but in the broad mesoscopic mass range targeted by ambitious gravity-superposition proposals.

No feasibility claim is made because Toy 007 additionally requires specific coherent five-level dynamics and controlled source energy gaps.

---

## Strongest new methodological result

The RQIR experiment-design object has changed from

\[
\boxed{\text{exact hidden state direction}}
\]

to

\[
\boxed{
\text{detector-level interface signal orthogonal to the nuisance manifold after whitening}.
}
\]

The operative metric is now

\[
F_{\beta|\theta}
\]

or a full likelihood/Bayes generalization, not exact nullity.

---

## Open items

- ❌ explicit frequency-dependent detector susceptibility for at least two detector classes;
- ❌ colored/correlated full covariance rather than independent harmonic variances;
- ❌ source decoherence and finite-window spectral leakage;
- ❌ apparatus/control stress-energy;
- ❌ full relativistic `T_{mu nu}` embedding and Bianchi/gauge gates;
- ❌ class-by-class detector predictions for semiclassical/stochastic/classical-QFT/perturbative-QG models;
- ❌ likelihood-level validation beyond local Fisher approximation;
- ❌ actual implementation of Toy 007/008 source Hamiltonian in a candidate platform.

---

## Exact next target

Evaluate two concrete detector branches under Protocol 002C:

1. matter-wave phase interferometer;
2. levitated/mechanical force or displacement sensor.

For each branch:

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

Then compare which detector family preserves both whitened harmonics with the best nuisance-profiled information per realistic resource.
