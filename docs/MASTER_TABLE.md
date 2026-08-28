# RQIR Operational Master Table

**Version:** 0.5  
**Date:** 2026-08-29

This table is deliberately conservative. `OPEN` means that the required comparison has not yet been demonstrated at RQIR precision; it does not mean the literature is absent.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy/no-go | Current discriminant strategy | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase can mimic interface-specific effects unless the source/control state is independently constrained | multi-clock correlations + explicit source observability rank + cross-channel consistency | OPEN |
| Q2 Superposed sources | probe phase/force/potential statistics | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch/hybrid, quantum mediator | static density coupling is phase-blind; one potential can hide local density differences; complete density history can become full state tomography | finite multiprobe calibration with declared rank/nullspace and detector-level response transfer | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | semiclassical Einstein equation / Einstein–Langevin | stochastic gravity, classical gravity + full QFT matter, hybrid/collapse, quantized metric | equal selected mean+noise need not fix response, but over-complete calibration removes all distinct-state freedom | optimize finite calibration + propagate surviving `chi^R` through gravity and detector | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, non-Gaussianity, visibility, scaling/correlations | common low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement alone is not unique to quantized gravity | perturbative order + mass/time/distance scaling + force/noise/response fingerprint | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise and response spectra | detector/environment noise + matter-induced metric-fluctuation prediction | stochastic induced metric fluctuations, intrinsic quantum geometry, technical noise | nonzero noise is not diagnostic; source response/noise and intrinsic gravity can be degenerate | joint transfer fit of source `N`, source `chi^R`, intrinsic-gravity sector and detector covariance | HIGH PRIORITY |
| Q6 Causal/process structure | process correlations, causal-order and relational timing observables | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | control-system nonclassicality can masquerade as gravity-specific process structure | gravity-dependent scaling + nongravitational-control closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections in EFT-valid regime | classical GR + Standard Model/QFT | perturbative QG EFT, local higher-curvature terms, classical systematics | universal nonanalytic pieces are tiny; local terms absorb UV dependence | cross-process nonanalytic/long-range fingerprint | OPEN |

---

## 1. Current source-side coordinate

RQIR preserves operator ordering at second order:

\[
\boxed{
\mathcal K_T^{(2)}
=(\langle T\rangle,N,D\text{ or }\chi^R).
}
\]

\[
N_{AB}=\frac12\langle\{\delta T_A,\delta T_B\}\rangle,
\]

\[
D_{AB}=\frac1{2i}\langle[\delta T_A,\delta T_B]\rangle,
\]

\[
\chi^R_{AB}
=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A,T_B]\rangle
\]

under the current RQIR sign convention.

The parent source object is the Schwinger–Keldysh / closed-time-path generating functional `Z_T[J_+,J_-]`.

---

## 2. Null-pair strength grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over a declared spacetime domain;
- **NP5:** NP4 plus full source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest positive construction: **Toy 007 reaches finite NP3**.

---

## 3. Observability rank and response survival

For finite calibration operators/settings

\[
\mathcal M=\{M_\alpha\},
\]

define

\[
\mathcal S_M=\operatorname{span}_{\mathbb R}\{M_\alpha\},
\]

\[
\boxed{r_{obs}=\dim\mathcal S_M.}
\]

The equality-nullspace is

\[
\mathcal N_{obs}=\mathcal S_M^\perp.
\]

For a target response operator `C_R`, define

\[
\boxed{
\eta_R=\frac{\|P_NC_R\|_{HS}}{\|C_R\|_{HS}}.
}
\]

Exact rank and `eta_R` are algebraic diagnostics only. Experimental design must also track conditioning and ultimately covariance/Fisher information.

---

## 4. Result chain

### RQIR-NG-001 / Toy 002 — static density phase blindness (`DRV/NEG`)

For orthogonal nonoverlapping mass branches and density-diagonal static coupling/readout, relative branch phase is invisible when diagonal mass statistics match.

**Consequence:** bare “superposition versus mixture” is not a gravitational coherence witness.

### RQIR-NG-002 / Toy 003 — minimal qubit energy obstruction (`DRV/NEG`)

A qubit can have equal density mean/noise and opposite ordered response, but the same state direction changes the mean generator energy.

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

A real five-level witness yields

\[
(\langle H\rangle,\langle\Phi_p\rangle,N_{\Phi_p})
\not\Rightarrow D_{\Phi_p}.
\]

Toy 005 is NP2 because other spatial density combinations remain unmatched.

### RQIR-NG-003 / Toy 006 — complete density-history tomography obstruction (`DRV/NEG`)

Under sufficient generic finite-mode conditions — distinct positive Bohr gaps, visibility of every energy pair and full-rank `W_ai=|V_ia|^2` — the complete time-evolved local-density projectors span `Herm(d)`.

Therefore

\[
\langle n_a(t)\rangle_+=\langle n_a(t)\rangle_-\;\forall a,t
\Rightarrow
\rho_+=\rho_-.
\]

**Consequence:** exact complete source tomography is too strong for a nontrivial response-only null pair.

### Toy 007 — finite NP3 multiprobe nullspace design (`NUM/DRV`)

Two Newtonian probes and a finite time/noise calibration give

\[
\boxed{r_{obs}=24\text{ of }25},
\qquad
\boxed{\dim\mathcal N_{obs}=1}.
\]

For the selected probe-0 response,

\[
\boxed{\eta_R\approx0.457682}.
\]

At the target time,

\[
\langle B_0\rangle_+=\langle B_0\rangle_-,
\]

\[
N_{00,+}=N_{00,-}\approx0.00944118,
\]

while

\[
D_{00,+}\approx-0.0105656,
\qquad
D_{00,-}\approx+0.0105656.
\]

However the normalized calibration matrix has

\[
s_{min}\approx1.46\times10^{-3},
\qquad
\kappa_A\approx3.18\times10^3.
\]

Thus Toy 007 proves that the finite operational middle ground is nonempty, but the design is poorly conditioned and not experimental-ready.

Files:

- `docs/TOY_MODEL_007_FINITE_MULTIPROBE_NULLSPACE_DESIGN.md`
- `analysis/toy007_finite_multiprobe_design.py`

---

## 5. Transfer Layer 001 — source → gravity → detector

The weak-field transfer is now explicit.

With bare Newtonian density-to-potential kernel

\[
R_G(\mathbf k)=-\frac{4\pi G}{k^2}
\]

and source response convention

\[
\delta\langle\rho\rangle
=\sigma_\chi\chi_\rho^R*\delta\Phi,
\]

the dressed source-to-potential response is

\[
\boxed{
\mathcal R_{\Phi\rho}^R
=
\left[I-R_G\sigma_\chi\chi_\rho^R\right]^{-1}R_G.
}
\]

For the present RQIR `chi^R` convention and perturbation Hamiltonian `delta H=+int rho deltaPhi`,

\[
\sigma_\chi=-1.
\]

For independent source and intrinsic-gravity noise sectors,

\[
\boxed{
N_\Phi
=
\mathcal R_{\Phi\rho}^R*N_\rho*\mathcal R_{\Phi\rho}^A
+
\mathcal D_\Phi^R*N_\Phi^{intr}*\mathcal D_\Phi^A.
}
\]

A linear detector with susceptibility `R_D^R` obeys

\[
\boxed{
\mathcal R_{D\rho}^R
=R_D^R*\mathcal R_{\Phi\rho}^R,
}
\]

\[
\boxed{
N_D^{obs}
=R_D^R*N_\Phi*R_D^A+N_D
}
\]

for independent detector noise.

File: `docs/LINEAR_RESPONSE_TRANSFER.md`.

### Critical implication

A source-side ordered-response split is not yet an observable gravitational discriminator. It must survive:

1. gravitational dressing;
2. intrinsic-gravity/model degeneracies;
3. detector susceptibility;
4. detector/environmental covariance;
5. nuisance profiling.

---

## 6. Current priority ranking v0.5

### P1 — Transfer Layer 002: detector-level Fisher distinguishability

Replace exact-rank optimization by covariance-weighted inference.

For detector mean/covariance `mu(theta), Sigma(theta)`, start with Gaussian Fisher information

\[
F_{ij}
=\partial_i\mu^T\Sigma^{-1}\partial_j\mu
+\frac12\operatorname{Tr}
\left[
\Sigma^{-1}(\partial_i\Sigma)
\Sigma^{-1}(\partial_j\Sigma)
\right].
\]

Profile/marginalize nuisance source directions and ask whether the Toy 007 ordered-response direction remains identifiable.

### P2 — improve NP3 conditioning

Optimize probe positions, times and covariance measurements jointly for:

- small nullity;
- large detector-level response separation;
- large smallest information singular value;
- realistic measurement count and geometry.

### P3 — restore physical scales

Assign source mass, site separation, energy/time scale and detector susceptibility. Compute SI-level response/noise and compare with known detector limits.

### P4 — Q4 common scaling/order comparison

Compare classical-gravity + full-QFT and perturbative-QG mechanisms in the same observables, not via a binary entanglement witness.

### P5 — Q7 EFT anchor

Reject interface laws inconsistent with controlled low-energy quantum-GR EFT.

---

## 7. Cross-channel matrix v0.5

| Pair | Why it matters | Current strategy |
|---|---|---|
| Q1 ↔ Q2 | source preparation affects clock phase | include source calibration/Fisher rank before assigning clock residual to interface physics |
| Q2 ↔ Q3 | directly tests source rule | finite NP3 Toy 007 + transfer-layer propagation |
| Q3 ↔ Q5 | separates mean/noise/response transfer | jointly infer source `N`, source `chi^R`, intrinsic-gravity noise and detector covariance |
| Q3 ↔ Q4 | source rule constrains information flow | one model must fit force/potential, response and quantum-information observables together |
| Q4 ↔ Q5 | entanglement/non-Gaussianity mechanisms imply accompanying noise/response structure | search for class-specific perturbative-order and scaling relations |
| Q1 ↔ Q6 | clocks operationalize causal/reference-frame structure | relational timing with explicit control-system nulls |
| Q7 ↔ all | EFT is a low-energy boundary | reject inconsistent interface maps |

---

## 8. Seed references

1. J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
2. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity 11, 3 (2008), arXiv:0802.0658.
3. N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001).
4. R. Howl et al., *Non-Gaussianity as a Signature of a Quantum Theory of Gravity*, PRX Quantum 2, 010325 (2021).
5. A. Czerwinski, *Quantum state tomography with informationally complete POVMs generated in the time domain*, arXiv:2010.13777.
6. A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
7. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.
8. J. Yant & M. Blencowe, *Operational quantum field theoretic model for gravitationally induced entanglement*, Phys. Rev. D 114, 026006 (2026).

## 9. Exact next iteration

1. Select a concrete first detector model.
2. Propagate Toy 007 `N` and surviving response through Transfer Layer 001.
3. Build covariance/Fisher distinguishability including detector noise.
4. Optimize probe geometry/times at detector level.
5. Restore SI scales only after the dimensionless inference structure is stable.
