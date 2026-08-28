# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current framework version:** operational core v0.5

This file is the continuity backbone. A new session should be able to resume the project from this document plus the files it references. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

\[
P_{data}(\mathbf o|\mathbf s)\Rightarrow[\mathfrak I].
\]

Rules:

- observable first;
- baseline explicit;
- residuals only relative to controlled baselines;
- preserve operator ordering;
- compare competing interface classes in one observable language;
- retain no-go/negative results;
- no “quantum gravity detected” claim until classical/stochastic/hybrid/full-QFT-matter alternatives are tested in the same regime;
- low-energy accessible channels before Planck-scale speculation;
- every numerical claim gets reproducibility code.

## 2. Ordered source hierarchy

At second order,

\[
\boxed{
\mathcal K_T^{(2)}=(\langle T\rangle,N,D\text{ or }\chi^R).
}
\]

\[
N_{AB}(x,y)=\frac12\langle\{\delta T_A(x),\delta T_B(y)\}\rangle,
\]

\[
D_{AB}(x,y)=\frac1{2i}\langle[\delta T_A(x),\delta T_B(y)]\rangle,
\]

\[
\chi^R_{AB}(x,y)=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A(x),T_B(y)]\rangle
\]

under the current RQIR convention.

The parent source object is

\[
Z_T[J_+,J_-]=\operatorname{Tr}(U[J_+]\rho_TU[J_-]^\dagger),
\]

the Schwinger–Keldysh / closed-time-path generating functional.

Never collapse different orderings into one `C^(n)` without an explicit identity/limit that makes them equivalent.

## 3. Working channels

- `Q1` quantum clocks / proper time;
- `Q2` superposed sources;
- `Q3` backreaction/source rule;
- `Q4` gravity-mediated quantum information;
- `Q5` geometry fluctuations;
- `Q6` causal/process structure;
- `Q7` low-energy quantum-gravity EFT.

## 4. Null-pair strength grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over a declared spacetime domain;
- **NP5:** NP4 plus complete source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest positive construction: Toy 007 = finite NP3 proof of principle.

## 5. Result chain

### Toy 001 — same mean, different variance

File: `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`.

Equal mean mass distribution can hide different source covariance. This is a mean-vs-fluctuation discriminator, not a coherence witness.

### RQIR-NG-001 / Toy 002 — static density phase blindness

File: `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.

For orthogonal nonoverlapping mass branches and density-diagonal static gravitational coupling/readout, relative branch phase is invisible when diagonal mass statistics match.

Conclusion: a bare coherent superposition versus incoherent mixture is not automatically a gravitational coherence witness.

### RQIR-NG-002 / Toy 003 — same noise, different response, energy confound

File: `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.

A qubit can have equal density mean history and equal symmetrized density noise but opposite commutator response. The same state direction changes mean generator energy, so it is not a clean gravity null pair.

### Toy 004 — balanced five-level algebraic witness

Files:

- `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`
- `analysis/search_balanced_ordered_kernel.py`

A five-level model satisfies equal mean energy, equal chosen-source mean history and equal reference-time symmetrized kernel, while the commutator response differs.

Therefore

\[
(\langle H\rangle,\langle B\rangle,N_B)\not\Rightarrow D_B.
\]

### PE-1 / Toy 005 — exact Newtonian density-channel embedding

Files:

- `docs/TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md`
- `analysis/search_real_newtonian_embedding.py`

Analytic lemma:

If

\[
B=V\operatorname{diag}(b_a)V^\dagger,
\qquad b_a>0,
\]

use the eigenvectors as localized one-particle modes and choose their distances from one fixed Newtonian probe as

\[
r_a=L/b_a.
\]

Then

\[
\boxed{\Phi_p=-\frac{Gm}{L}B.}
\]

A real five-level witness gives equal mean energy, equal complete chosen-potential mean history and equal chosen-potential symmetrized noise, while `D/chi^R` differs.

Critical limitation: other spatial density combinations differ. Toy 005 is NP2.

### RQIR-NG-003 / Toy 006 — complete density-history tomography obstruction

Files:

- `docs/TOY_MODEL_006_DENSITY_HISTORY_TOMOGRAPHY_NO_GO.md`
- `analysis/check_density_history_tomography.py`

For a finite one-particle source, if positive Bohr gaps are nondegenerate, every energy pair is visible in local modes, and `W_ai=|V_ia|^2` has full rank, then

\[
\operatorname{span}_{\mathbb R}\{P_a(t):a,t\}=\operatorname{Herm}(d).
\]

Hence

\[
\langle n_a(t)\rangle_+=\langle n_a(t)\rangle_-\;\forall a,t
\Rightarrow
\rho_+=\rho_-.
\]

Conclusion: complete infinite-resolution density matching can already be full quantum tomography and therefore destroys all nontrivial distinct-state response pairs.

### Toy 007 — finite multiprobe NP3 nullspace design

Files:

- `docs/TOY_MODEL_007_FINITE_MULTIPROBE_NULLSPACE_DESIGN.md`
- `analysis/toy007_finite_multiprobe_design.py`
- `research_log/2026-08-29_iteration_006_toy007.md`

Toy 005 source positions, in units where the nearest site to probe 0 is at one length unit:

\[
x_a\approx(5.53112,2.21089,1.44295,1.27948,1.00000).
\]

Probe positions:

\[
y_0=0,
\qquad
y_1\approx-3.59552719.
\]

A finite calibration of both probe means plus selected auto/cross symmetrized-noise entries gives

\[
\boxed{r_{obs}=24/25},
\qquad
\boxed{\dim\mathcal N_{obs}=1}.
\]

For target

\[
C_R=\frac1{2i}[B_0(t_R),B_0(0)],
\qquad
t_R\approx3.583928899,
\]

response survival is

\[
\boxed{\eta_R\approx0.457682}.
\]

At `t_R`,

\[
\langle B_0\rangle_+=\langle B_0\rangle_-\approx0.6215386505,
\]

\[
N_{00,+}=N_{00,-}\approx0.0094411777,
\]

but

\[
D_{00,+}\approx-0.010565632,
\qquad
D_{00,-}\approx+0.010565632.
\]

Thus

\[
\Delta D_{00}\approx-0.021131264.
\]

Independent verification reconstructing Toy 005 from seed `105` gives selected equality residuals below `3e-16`.

Critical weakness:

\[
\boxed{s_{min}\approx1.463\times10^{-3}},
\qquad
\boxed{\kappa_A\approx3.18\times10^3}.
\]

Therefore exact rank 24 is poorly conditioned. Toy 007 is a mathematical NP3 proof of principle, not experimental-ready.

## 6. Observability-rank principle

For calibrated operators/settings

\[
\mathcal M=\{M_\alpha\},
\]

define

\[
\mathcal S_M=\operatorname{span}_{\mathbb R}\{M_\alpha\},
\]

\[
\boxed{r_{obs}=\dim\mathcal S_M},
\qquad
\boxed{\mathcal N_{obs}=\mathcal S_M^\perp}.
\]

A response-only direction exists only if the target commutator/retarded operator has nonzero projection into the equality-nullspace remaining after mean and noise controls.

For target `C_R`,

\[
\eta_R=\frac{\|P_NC_R\|}{\|C_R\|}.
\]

Rank and `eta_R` are algebraic diagnostics; realistic inference must use measurement covariance/Fisher information.

## 7. Transfer Layer 001 — source → gravity → detector

File: `docs/LINEAR_RESPONSE_TRANSFER.md`.

This layer is essential because a source-side response difference is not automatically a detector-level gravitational residual.

For Newtonian mass density, define bare transfer

\[
R_G(\mathbf k)=-\frac{4\pi G}{k^2}.
\]

With source response

\[
\delta\langle\rho\rangle
=\sigma_\chi\chi_\rho^R*\delta\Phi,
\]

the dressed density-to-potential transfer is

\[
\boxed{
\mathcal R_{\Phi\rho}^R
=\left[I-R_G\sigma_\chi\chi_\rho^R\right]^{-1}R_G.
}
\]

For the current RQIR definition of `chi^R` and perturbation Hamiltonian `delta H=+int rho deltaPhi`,

\[
\sigma_\chi=-1.
\]

Potential noise, assuming independent source and intrinsic-gravity sectors:

\[
\boxed{
N_\Phi
=\mathcal R_{\Phi\rho}^R*N_\rho*\mathcal R_{\Phi\rho}^A
+\mathcal D_\Phi^R*N_\Phi^{intr}*\mathcal D_\Phi^A.
}
\]

For linear detector response `R_D^R`,

\[
\boxed{
\mathcal R_{D\rho}^R=R_D^R*\mathcal R_{\Phi\rho}^R,
}
\]

\[
\boxed{
N_D^{obs}=R_D^R*N_\Phi*R_D^A+N_D
}
\]

for independent detector noise.

The covariant analogue has schematic form

\[
[\mathcal E^{(1)}-8\pi G\sigma_\chi\Pi^R]h
=8\pi G(\xi+T^{ext}),
\]

with induced metric noise

\[
N_h^{ind}\sim(8\pi G)^2G_h^R*N_T*G_h^A.
\]

Do not promote the Newtonian formula componentwise into GR without gauge, Bianchi/conservation, renormalization/contact-term and causal checks.

## 8. External boundaries that must remain active

- Hu & Verdaguer stochastic gravity: CTP/influence-functional structure contains both matter-induced noise and dissipation/response; Einstein–Langevin dynamics propagates stress-energy fluctuations into geometry. Therefore matter `N` or `chi^R` does not imply quantum geometry.
- Howl et al. 2021: standard nonrelativistic quantum mass-density operator supports the Toy 005 Newtonian embedding structure.
- Aziz & Howl 2025: full-QFT matter can generate entanglement in suitable local classical-gravity constructions; entanglement alone is not a unique quantum-gravity witness.
- Czerwinski 2020: time-domain measurements can become informationally complete, providing context for RQIR-NG-003.
- Yant & Blencowe 2026: gravitational-entanglement calculations can be formulated directly with operational QFT observables, supporting RQIR's observable-first direction.

## 9. Current consistency gates

Especially important now:

- `G1` gauge/relational observables;
- `G2` conservation/Bianchi embedding;
- `G3/G3b` positivity, unitarity and spectral/response identities;
- `G4a` retarded causal support;
- `G8` controlled Newtonian limit;
- `G9` EFT power counting for perturbative QG;
- `G10/G10a` stress-tensor smearing/renormalization;
- `G12/G12a` classical/stochastic/full-QFT degeneracy audit;
- `G13` detector-level measurability and covariance-weighted inference.

## 10. Current repository core

- `README.md`
- `docs/FOUNDATIONS.md`
- `docs/MASTER_TABLE.md`
- `docs/ORDERED_KERNEL_HIERARCHY.md`
- `docs/LINEAR_RESPONSE_TRANSFER.md`
- `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`
- `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`
- `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`
- `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`
- `docs/TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md`
- `docs/TOY_MODEL_006_DENSITY_HISTORY_TOMOGRAPHY_NO_GO.md`
- `docs/TOY_MODEL_007_FINITE_MULTIPROBE_NULLSPACE_DESIGN.md`
- `analysis/search_balanced_ordered_kernel.py`
- `analysis/search_real_newtonian_embedding.py`
- `analysis/check_density_history_tomography.py`
- `analysis/toy007_finite_multiprobe_design.py`
- `research_log/` — dated chronology

## 11. Exact next research target

### Transfer Layer 002 — concrete detector and covariance/Fisher inference

1. Choose a concrete detector model, preferably first an interferometric phase readout or linear mechanical susceptibility.
2. Propagate Toy 007 source response/noise through `T_G` and `T_D`.
3. Replace exact-rank optimization by covariance-weighted Fisher/profile-likelihood distinguishability:

\[
F_{ij}
=\partial_i\mu^T\Sigma^{-1}\partial_j\mu
+\frac12\operatorname{Tr}
[\Sigma^{-1}(\partial_i\Sigma)\Sigma^{-1}(\partial_j\Sigma)].
\]

4. Profile/marginalize all source and detector nuisance directions.
5. Jointly optimize probe positions/times for response survival and conditioning.
6. Restore SI mass/length/time scales only after the dimensionless inference structure is stable.
7. Compare detector-level fingerprints for semiclassical/stochastic/classical-gravity+full-QFT/perturbative-QG classes.

## 12. Epistemic labels

- `DEF` definition/convention
- `EST` established external result
- `DRV` RQIR analytic derivation
- `NUM` numerical result
- `EMP` empirical constraint
- `CONJ` conjecture
- `OPEN` unresolved
- `NEG` failed/excluded branch or conditional no-go

Never promote a toy result, numerical search or conditional no-go beyond its declared assumptions.

## 13. Continuation protocol

At each substantive iteration:

1. read this guide and latest research log;
2. state one exact unresolved target;
3. derive analytically before adding numerical complexity;
4. run applicable consistency gates;
5. preserve positive and negative results;
6. record reproducibility code for numerical claims;
7. update `MASTER_TABLE.md` and this guide when the project state changes;
8. keep the repository as authoritative memory.
