# RQIR Operational Master Table

**Version:** 0.6  
**Date:** 2026-08-29

This table is deliberately conservative. `OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy/no-go | Current discriminant strategy | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase can mimic interface effects unless source/control nuisances are constrained | profiled multi-clock likelihood + source/clock calibration | OPEN |
| Q2 Superposed sources | probe phase/force/potential statistics | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch/hybrid, quantum mediator | static density coupling is phase-blind; complete density history can become state tomography | finite multiprobe calibration + source→gravity→detector transfer + nuisance profiling | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | semiclassical Einstein equation / Einstein–Langevin | stochastic gravity, classical gravity + full QFT matter, hybrid/collapse, quantized metric | equal selected mean+noise need not fix response; exact near-tomographic null-pairs can be poorly conditioned | maximize detector-level profiled Fisher information for response/interface parameters | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, non-Gaussianity, visibility, scaling/correlations | common low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement alone is not unique to quantized gravity | common likelihood over scaling/order + force/noise/response observables | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise and response spectra | detector/environment noise + matter-induced metric-fluctuation prediction | stochastic induced metric fluctuations, intrinsic quantum geometry, technical noise | nonzero noise is not diagnostic | joint transfer fit of source `N`, source `chi^R`, intrinsic-gravity sector and detector covariance | HIGH PRIORITY |
| Q6 Causal/process structure | process correlations, causal-order and relational timing observables | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | control-system nonclassicality can masquerade as gravity-specific structure | gravity-dependent scaling + profiled control-system nuisance model | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections in EFT-valid regime | classical GR + Standard Model/QFT | perturbative QG EFT, local higher-curvature terms, classical systematics | universal nonanalytic pieces are tiny; local terms absorb UV dependence | cross-process nonanalytic/long-range fingerprint | OPEN |

---

## 1. Current source-side coordinate

RQIR preserves operator ordering at second order:

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

under the current sign convention.

The parent source object is the Schwinger–Keldysh / closed-time-path generating functional `Z_T[J_+,J_-]`.

---

## 2. Null-pair grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational-readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over a declared domain;
- **NP5:** NP4 plus full source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction: **Toy 007 reaches finite NP3**.

NP grades are algebraic construction grades, not experimental significance measures.

---

## 3. Exact observability geometry

For calibration operators/settings `M_alpha`,

\[
\mathcal S_M=\operatorname{span}_{\mathbb R}\{M_\alpha\},
\qquad
\boxed{r_{obs}=\dim\mathcal S_M},
\]

and

\[
\mathcal N_{obs}=\mathcal S_M^\perp.
\]

For target response vector/operator `r`,

\[
\boxed{\eta_R=\frac{\|P_{\mathcal N}r\|}{\|r\|}.}
\]

This remains useful for existence/no-go proofs, but exact rank is no longer the final experiment-design objective.

---

## 4. Result chain

### RQIR-NG-001 / Toy 002 — static density phase blindness (`DRV/NEG`)

For orthogonal nonoverlapping mass branches and density-diagonal static coupling/readout, relative branch phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 / Toy 003 — minimal qubit energy obstruction (`DRV/NEG`)

A qubit can have equal density mean/noise and opposite ordered response, but the same state direction changes mean generator energy.

### Toy 004 — balanced algebraic ordered-kernel witness (`NUM/DRV`)

A five-level model demonstrates

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — exact Newtonian single-channel embedding (`DRV/NUM`)

Any positive finite-dimensional `B` can be represented as one Newtonian potential channel of a one-particle finite-site source:

\[
B=\sum_a b_an_a,
\qquad
r_a=L/b_a,
\qquad
\Phi_p=-\frac{Gm}{L}B.
\]

Toy 005 reaches NP2 but does not match all spatial density combinations.

### RQIR-NG-003 / Toy 006 — complete density-history tomography (`DRV/NEG`)

Under sufficient generic finite-mode conditions, complete time-evolved local-density information can span `Herm(d)`, giving

\[
\langle n_a(t)\rangle_+=\langle n_a(t)\rangle_-\;\forall a,t
\Rightarrow
\rho_+=\rho_-.
\]

Thus complete exact source tomography is incompatible with a distinct-state response-only null pair.

### Toy 007 — finite NP3 multiprobe nullspace (`NUM/DRV`)

Accepted design:

\[
\boxed{r_{obs}=24/25},
\qquad
\boxed{\eta_R\approx0.457682}.
\]

At the target time,

\[
\langle B_0\rangle_+=\langle B_0\rangle_-,
\qquad
N_{00,+}=N_{00,-}\approx0.00944118,
\]

but

\[
D_{00,+}\approx-0.0105656,
\qquad
D_{00,-}\approx+0.0105656.
\]

Conditioning is weak:

\[
s_{min}\approx1.46\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

### RQIR-NG-004 — exact-null saturation (`DRV`)

If exact calibration `A` has rank `p-1` with null vector `n`, then one additional exact calibration row `a^T` satisfying

\[
a^Tn\neq0
\]

raises the rank to `p` and eliminates every nonzero exact state-difference null pair.

**Scope:** this is a theorem about exact null-pair construction only. It is not a theorem that more experimental calibration reduces statistical sensitivity.

### Toy 008 — soft-nullspace scan (`NUM/DRV`)

A reproducible 300-design scan using the same five-site source found:

| rank | nullity | eta_R | s_min | condition |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0.696801 | 5.68468e-3 | 750.57 |
| 21 | 4 | 0.677521 | 5.43696e-3 | 803.96 |
| 22 | 3 | 0.638991 | 2.48186e-3 | 1801.88 |
| 23 | 2 | 0.607629 | 1.38924e-3 | 3271.43 |
| 24 | 1 | 0.473850 | 1.56388e-3 | 2965.14 |

This is not a global optimum. It proves only that, inside the scanned design family and exploratory score `eta_R sqrt(s_min)`, forcing nullity one is not automatically optimal.

Files:

- `docs/TOY_MODEL_008_SOFT_NULLSPACE_FISHER_TRANSITION.md`
- `analysis/rank_conditioning_scan.py`

---

## 5. Statistical identifiability layer

For local calibration model

\[
y_c=\mu_c+A\theta+\epsilon_c,
\qquad
\operatorname{Cov}\epsilon_c=\Sigma_c,
\]

define

\[
\boxed{F_c=A^T\Sigma_c^{-1}A.}
\]

The singular vectors of the whitened matrix

\[
\widetilde A=\Sigma_c^{-1/2}A
\]

replace binary exact-null thinking by a spectrum of strongly and weakly constrained source directions.

For parameter of interest `beta` and nuisance coordinates `theta`,

\[
\mu(\beta,\theta)=\mu_0+s\,\delta\beta+J\,\delta\theta.
\]

The nuisance-profiled Fisher information is

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

Only the component of the interface signal that cannot be reproduced by nuisance variation is statistically identifiable.

File: `docs/STATISTICAL_IDENTIFIABILITY.md`.

### RQIR-CAL-001 — calibration monotonicity (`DRV`)

If statistically independent added calibration is `beta`-blind and contributes `C\succeq0` only to the nuisance Fisher block, with a positive-definite nuisance block in the domain used, then

\[
\boxed{F'_{\beta|\theta}\ge F_{\beta|\theta}.}
\]

Thus extra calibration may destroy an exact constructed null pair while improving the actual identifiability of the physical interface parameter.

This resolves the apparent Toy 006/007 calibration paradox.

---

## 6. Transfer Layer 001 — source → gravity → detector

With bare Newtonian density-to-potential kernel

\[
R_G(\mathbf k)=-\frac{4\pi G}{k^2}
\]

and source linear response, the dressed source-to-potential response is

\[
\boxed{
\mathcal R_{\Phi\rho}^R
=\left[I-R_G\sigma_\chi\chi_\rho^R\right]^{-1}R_G.
}
\]

For independent source and intrinsic-gravity noise sectors,

\[
\boxed{
N_\Phi
=\mathcal R_{\Phi\rho}^R*N_\rho*\mathcal R_{\Phi\rho}^A
+\mathcal D_\Phi^R*N_\Phi^{intr}*\mathcal D_\Phi^A.
}
\]

A linear detector obeys

\[
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R,
\]

\[
N_D^{obs}=R_D^R*N_\Phi*R_D^A+N_D
\]

under the declared independence assumptions.

A source-side response split must survive gravitational dressing, model degeneracies, detector susceptibility, covariance and nuisance profiling before it is an observable RQIR discriminator.

---

## 7. Pump–probe / spectral result

For a weak source impulse with dimensionless area

\[
\alpha=\frac{m_s}{\hbar}\int A(t)dt,
\]

Toy 007 gives at its original target time

\[
|\Delta\delta B_0|\simeq0.0422625|\alpha|.
\]

The corresponding simple interferometric scaling is

\[
|\Delta\varphi|
\sim0.0422625|\alpha|\frac{Gm_sm_pT_{eff}}{\hbar L_0}.
\]

The full response waveform is dominated by two harmonics: approximately 89.4% of its power lies in the `2 omega_*` and `4 omega_*` components in the current dimensionless model.

This motivates a multi-frequency profiled-likelihood protocol rather than a single-time exact null test.

---

## 8. Current priority ranking v0.6

### P1 — Protocol 002: multi-frequency profiled likelihood

Use the `2 omega_*` and `4 omega_*` response channels plus calibration data in one likelihood. Include nuisance parameters for source state, energy scale, probe geometry, detector gain/phase and noise amplitudes.

Primary objective:

\[
\boxed{F_{\beta|\theta}}
\]

or a likelihood-level generalization.

### P2 — push Fisher geometry through Transfer Layer 001

The signal derivative and nuisance Jacobian must be evaluated at the detector output, not only source operator space.

### P3 — covariance model

Build correlated source, detector and environmental covariance; test Gaussian/Fisher validity against likelihood calculations.

### P4 — physical scales and apparatus stress-energy

Restore SI scales only after the dimensionless inference model is stable; include control energy and source apparatus.

### P5 — cross-class gravity comparison

Require semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG baselines to predict the same detector observables and nuisance structure.

---

## 9. Cross-channel matrix v0.6

| Pair | Why it matters | Current strategy |
|---|---|---|
| Q1 ↔ Q2 | source preparation affects clock phase | profile source/control nuisances jointly with clock signal |
| Q2 ↔ Q3 | tests source rule directly | NP3 constructions → transfer law → profiled detector likelihood |
| Q3 ↔ Q5 | separates response/noise transfer | joint source `N`, source `chi^R`, intrinsic-gravity noise and detector covariance |
| Q3 ↔ Q4 | source rule constrains information flow | one likelihood must fit force/potential, response and quantum-information channels |
| Q4 ↔ Q5 | candidate mechanisms imply accompanying noise/response structure | compare perturbative order and scaling relations |
| Q1 ↔ Q6 | clocks operationalize causal/reference-frame structure | relational timing with explicit control-system nuisances |
| Q7 ↔ all | EFT is a low-energy consistency boundary | reject inconsistent interface maps |

---

## 10. Seed references

1. J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
2. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity 11, 3 (2008), arXiv:0802.0658.
3. N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001).
4. R. Howl et al., *Non-Gaussianity as a Signature of a Quantum Theory of Gravity*, PRX Quantum 2, 010325 (2021).
5. A. Czerwinski, *Quantum state tomography with informationally complete POVMs generated in the time domain*, arXiv:2010.13777.
6. A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
7. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.
8. J. Yant & M. Blencowe, *Operational quantum field theoretic model for gravitationally induced entanglement*, Phys. Rev. D 114, 026006 (2026).

---

## 11. Exact next iteration

1. Build Protocol 002 with a two-harmonic detector data vector.
2. Define a minimal but explicit nuisance vector.
3. Compute the first detector-level `F_{beta|theta}` and identify exact/near degeneracies.
4. Add calibration channels only according to their improvement in profiled information per experimental cost.
5. Replace Fisher results by direct likelihood checks where nonlinearity/non-Gaussianity matters.
6. Begin the same detector-level fit under at least semiclassical/stochastic and one alternative interface class.
