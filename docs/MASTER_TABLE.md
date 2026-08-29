# RQIR Operational Master Table

**Version:** 0.9  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main degeneracy / current obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, clock correlations | ordinary relativistic/control effects can mimic interface residuals | profiled likelihood with explicit source/control calibration | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static density is phase-blind; complete density history becomes tomography | finite multiprobe calibration + detector transfer + multi-band inference | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | equal selected mean+noise need not determine response; source response can be projected away by calibration/detector geometry | joint source+calibration+detector Fisher optimization | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, non-Gaussianity, scaling | entanglement alone not unique to quantized gravity | common likelihood over force/noise/response/entanglement scaling | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise and response spectra | matter-induced, intrinsic-gravity and technical noise can be degenerate | joint `N`, `chi^R`, intrinsic-gravity and detector covariance fit | HIGH PRIORITY |
| Q6 Causal/process | relational timing/process observables | control-system nonclassicality can mimic gravity structure | gravity-dependent scaling with nuisance closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | universal pieces tiny, local UV terms degenerate | cross-process nonanalytic/long-range fingerprint | OPEN |

---

## 1. Current source coordinate

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

The formal parent object remains the Schwinger–Keldysh / CTP generating functional.

---

## 2. Closed/retained result chain

### RQIR-NG-001 / Toy 002 — static density phase blindness

For orthogonal nonoverlapping mass branches with density-diagonal static coupling/readout, relative phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — minimal response split has an energy confound

A qubit can have equal density mean/noise and opposite ordered response, but the same state direction changes mean generator energy.

### Toy 004 — balanced algebraic witness

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — exact Newtonian one-channel embedding

For positive `B=V diag(b_a)V^dagger`, localized modes at `r_a=L/b_a` give

\[
\Phi_p=-\frac{Gm}{L}B.
\]

### RQIR-NG-003 / Toy 006 — complete density-history tomography

Under sufficient generic finite-mode conditions,

\[
span_R\{P_a(t)\}=Herm(d),
\]

so complete local-density history equality implies identical states.

### Toy 007 — first finite NP3

Fixed two-probe calibration gave

\[
r_{obs}=24/25,
\qquad
\eta_R\approx0.457682,
\]

with equal selected mean/noise and opposite target response. Conditioning was weak:

\[
s_{min}\approx1.463\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004 — exact-null saturation

With a one-dimensional exact nullspace, one additional independent exact row removes the nonzero exact state-difference null direction. Scope: exact null-pair construction only.

### Toy 008 — soft-nullspace / Fisher transition

A reproducible design scan showed that maximal exact rank is not automatically best for response survival plus conditioning. This motivated the likelihood/Fisher formulation.

---

## 3. Statistical identifiability

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

Independent `beta`-blind calibration can only add nuisance information under the declared regularity assumptions:

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

---

## 4. Transfer layer

A source-side ordered-response split is not yet an observable gravitational discriminator.

Newtonian schematic:

\[
R_G(k)=-4\pi G/k^2,
\]

\[
\mathcal R_{\Phi\rho}^R
=[I-R_G\sigma_\chi\chi_\rho^R]^{-1}R_G,
\]

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R.
\]

Detector-level noise/covariance and nuisance profiling must be included before interpretation.

---

## 5. Protocol 002 — two-band shape discriminator

For whitened information powers

\[
P_n=|s_n|^2/\sigma_n^2,
\]

the antisymmetric relative-tilt nuisance leaves

\[
\boxed{S_{eff}=\frac{4P_2P_4}{P_2+P_4}.}
\]

If one band is lost, the shape discriminator vanishes.

With independent static common-amplitude calibration `C`,

\[
\boxed{F_{\beta|\theta}=\frac{S_{eff}C}{S_{eff}+C}.}
\]

---

## 6. Detector comparison D1 vs D2

### D1 — matter-wave phase

A passive full-period phase integral cancels the chosen nonzero harmonics:

\[
W_2=W_4=0.
\]

A deliberately modulated lock-in/echo sensitivity is required.

Toy 007 eight-switch bounded sequence gave the revised five-sigma illustration

\[
m_sm_p\sim8.1\times10^{-29}\,kg^2,
\]

or equal-mass illustration near

\[
9.0\times10^{-15}\,kg.
\]

### D2 — mechanical force

Force response is

\[
\Delta F_n=2\alpha\frac{Gm_sm_p}{L_0^2}G_n.
\]

At a true force-noise floor, mechanical resonance does not provide free Fisher gain because susceptibility multiplies both signal and displacement noise.

Under the deliberately optimistic `1e-21 N/sqrt(Hz)` benchmark, Toy 007 required about

\[
2.40\times10^{-18}\,kg^2.
\]

D1 remains the stronger absolute-sensitivity branch for the present micrometre geometry; D2 remains technologically mature but far from the required force scale.

---

## 7. D1 control layer

Toy 007's eight-switch sequence showed that finite switching bandwidth is less severe than cumulative contrast loss. If each switch multiplies amplitude by `c`, Fisher scales as

\[
F\propto c^{2N_{sw}}.
\]

This makes switch count an explicit experimental resource.

Recent continuous-control quantum-sensing methods show that AC sensing need not be restricted to ideal instantaneous pulses; RQIR does not claim lock-in/dynamical-decoupling control itself as new physics.

---

## 8. Toy 009 — detector-aware source redesign

Main file: `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`.

### 8.1 Negative detector-only candidate

A 5000-trial NP2 scan found a source with apparent gains

\[
S_{eff}^{D1}:\times5.3625,
\qquad
S_{eff}^{D2}:\times4.1741.
\]

But after the inherited NP3 calibration,

\[
\eta_R\approx0.0299,
\qquad
s_{min}\approx2.61\times10^{-4},
\qquad
\kappa_A\approx1.75\times10^4.
\]

Thus detector-only optimization can create large gains that disappear after calibration projection.

### 8.2 Accepted NP3 candidate

A second deterministic 5000-trial scan fixed the Toy 007 calibration pattern and required

\[
\eta_R\ge\eta_R^{007},
\qquad
s_{min}\ge s_{min}^{007}.
\]

Only one scanned candidate passed both guards: seed `314159`, trial `811`.

Toy 009 radii:

\[
\boxed{(1.00000,1.60090,1.77911,2.60901,5.90724).}
\]

The fixed calibration still gives

\[
rank(A)=24/25.
\]

Selected mean/noise equality residuals are below `6e-16`; states remain positive.

Target response:

\[
D_{00,+}\approx-0.0120850,
\qquad
D_{00,-}\approx+0.0120850.
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

Relative to Toy 007:

\[
\boxed{S_{eff}^{D1}:\times1.22184,}
\]

\[
\boxed{S_{eff}^{D2}:\times1.40358.}
\]

This is the first simultaneous Pareto improvement of D1, D2, response survival and conditioning over the finite NP3 baseline.

---

## 9. Toy 009 low-switch D1

Four-switch sequence:

\[
|W_2|\approx0.50363,
\qquad
|W_4|\approx0.30807,
\]

\[
\boxed{F_{009,4sw}\approx1.12746F_{007,8sw}.}
\]

Six-switch sequence:

\[
|W_2|\approx0.45974,
\qquad
|W_4|\approx0.36382,
\]

\[
\boxed{F_{009,6sw}\approx1.23731F_{007,8sw}.}
\]

Thus the new source produces more two-band information with fewer hard switches.

Illustrative D1 mass-product scales become approximately

\[
7.63\times10^{-29}\,kg^2
\]

for four switches and

\[
7.28\times10^{-29}\,kg^2
\]

for six switches under the same earlier assumptions.

The D2 optimistic benchmark rescales to approximately

\[
2.03\times10^{-18}\,kg^2.
\]

---

## 10. New design principle

### RQIR-DESIGN-001 — optimize source and inference geometry jointly

The correct ordering is

\[
\boxed{
\text{source}
\to
\text{calibration/Fisher geometry}
\to
\text{gravity transfer}
\to
\text{detector window/noise}
\to
F_{\beta|\theta}.
}
\]

A source is not considered improved merely because an upstream response norm increases.

---

## 11. Current priority ranking v0.9

### P1 — jointly re-optimize Toy 009 calibration geometry

Vary second-probe location and calibration times with the source, rather than inheriting Toy 007 settings. Optimize detector-level profiled Fisher while keeping state positivity and geometry guards.

### P2 — continuous/phase-modulated D1 control

Compare four/six hard switches with continuous phased control under one bandwidth, contrast and timing-jitter budget.

### P3 — realistic D2 covariance

Add thermal force, backaction and displacement-imprecision PSD and evaluate two-band `P2,P4` rather than detector-agnostic force floors.

### P4 — common resource budget

Compare D1/D2 at one declared source mass, gap scale, coherence time, separation and integration time.

### P5 — interface-class fingerprints

Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same detector likelihood.

### P6 — full relativistic stress-energy embedding

Close source+apparatus conservation, gauge/relational and stress-tensor renormalization gates before any fundamental claim.

---

## 12. Key files

- `docs/RECOVERY_GUIDE.md`
- `docs/STATISTICAL_IDENTIFIABILITY.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`
- `docs/D1_FINITE_BANDWIDTH_CONTROL.md`
- `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`
- `analysis/toy009_detector_aware_source_search.py`
- `analysis/d1_low_switch_toy009.py`
- `research_log/2026-08-29_iteration_010_toy009_detector_aware_source.md`
