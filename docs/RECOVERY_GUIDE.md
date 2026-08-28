# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)

This file is the continuity backbone. A new session should be able to resume the project from this document plus the files it references.

## 1. Objective

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

\[
P_{\rm data}(\mathbf o|\mathbf s)\Rightarrow[\mathfrak I].
\]

The project is observable-first, baseline-explicit, degeneracy-aware, and retains negative/no-go results.

## 2. Current mathematical core

At second order, operator ordering must be preserved:

\[
\boxed{
\mathcal K_T^{(2)}
=(\langle T\rangle,N,D\text{ or }\chi^R).
}
\]

\[
N_{AB}(x,y)=\frac12\langle\{\delta T_A(x),\delta T_B(y)\}\rangle,
\]

\[
D_{AB}(x,y)=\frac1{2i}\langle[\delta T_A(x),\delta T_B(y)]\rangle,
\]

\[
\chi^R_{AB}(x,y)=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A(x),T_B(y)]\rangle.
\]

The parent source object is the Schwinger–Keldysh / closed-time-path generating functional

\[
Z_T[J_+,J_-]=\operatorname{Tr}(U[J_+]\rho_TU[J_-]^\dagger).
\]

Important non-implication: nonzero `N`, nonzero `D/chi^R`, entanglement, or other nonclassical-looking matter observables do not by themselves prove quantum geometry.

## 3. Working channels

- `Q1` quantum clocks / proper time;
- `Q2` superposed sources;
- `Q3` backreaction/source rule;
- `Q4` gravity-mediated quantum information;
- `Q5` geometry fluctuations;
- `Q6` causal/process structure;
- `Q7` low-energy quantum-gravity EFT.

## 4. Null-pair strength grades

To prevent overclaiming:

- **NP0** equal global scalar only;
- **NP1** equal chosen gravitational readout mean;
- **NP2** equal chosen readout mean + symmetrized noise;
- **NP3** equal finite independent multiprobe/multipole mean/noise set;
- **NP4** equal complete relevant smeared stress-energy mean/noise in a declared domain;
- **NP5** NP4 plus complete source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Toy 005 reaches NP2 only.

## 5. Result chain

### Toy 001 — same mean, different variance

File: `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`.

Equal mean mass distribution can hide different source covariance. This gives a mean-vs-fluctuation discriminator but is not a coherence witness.

### RQIR-NG-001 / Toy 002 — static density phase blindness

File: `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.

For nonoverlapping orthogonal mass configurations and density-diagonal static coupling/readout, relative source phase is invisible when diagonal mass statistics match.

Conclusion: “superposition versus mixture” is not automatically a gravitational coherence witness.

### RQIR-NG-002 / Toy 003 — same noise, different response, but energy confound

File: `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.

A qubit can have equal density mean history and equal symmetrized density noise but opposite commutator/retarded response. However the same state direction changes mean generator energy, so it fails as a clean gravity null pair.

### Toy 004 — balanced five-level algebraic witness

File: `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`.

A five-level finite-dimensional model satisfies

\[
\langle H\rangle_+=\langle H\rangle_-,
\quad
\langle B(t)\rangle_+=\langle B(t)\rangle_-\;\forall t,
\quad
N_+(t,0)=N_-(t,0)\;\forall t,
\quad
D_+(t,0)\neq D_-(t,0).
\]

Thus

\[
(\langle H\rangle,\langle B\rangle,N)\not\Rightarrow D.
\]

But `B` was initially only an abstract positive source observable.

### PE-1 / Toy 005 — exact Newtonian density-channel embedding

Files:

- `docs/TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md`
- `analysis/search_real_newtonian_embedding.py`

Analytic embedding lemma:

If

\[
B=V\operatorname{diag}(b_a)V^\dagger,
\qquad b_a>0,
\]

use the eigenvectors as localized one-particle modes and choose their distances from a fixed Newtonian probe as

\[
r_a=L/b_a.
\]

Then

\[
\boxed{\Phi_p=-\frac{Gm}{L}B.}
\]

A cleaner real five-level witness was found with

\[
H=\operatorname{diag}(1,2,3,4,6)
\]

and positive real-symmetric `B`, such that

\[
\langle H\rangle_+=\langle H\rangle_-=3.2,
\]

\[
\langle\Phi_p(t)\rangle_+=\langle\Phi_p(t)\rangle_-\;\forall t,
\]

\[
N_{\Phi,+}(t,0)=N_{\Phi,-}(t,0)\;\forall t,
\]

while

\[
D_{\Phi,+}(t,0)\neq D_{\Phi,-}(t,0).
\]

Near `t≈3.58393` in dimensionless units,

\[
N_+=N_-\approx0.288837,
\]

\[
D_+\approx+0.114476,
\qquad
D_-\approx-0.114476.
\]

This is the first exact physical **single-channel Newtonian** ordered-response split in RQIR.

Critical limitation: local mode populations differ, so an independent second probe can generally distinguish the states at the mean-field level. Therefore Toy 005 is NP2, not NP4/NP5.

### RQIR-NG-003 / Toy 006 — complete density-history tomography obstruction

Files:

- `docs/TOY_MODEL_006_DENSITY_HISTORY_TOMOGRAPHY_NO_GO.md`
- `analysis/check_density_history_tomography.py`

For a finite one-particle source with local projectors

\[
P_a(t)=e^{iHt}|a\rangle\langle a|e^{-iHt},
\]

assume:

1. all positive Bohr gaps are distinct;
2. every energy pair appears with nonzero amplitude in at least one local mode;
3. `W_ai=|V_ia|^2` has rank `d`.

Then

\[
\boxed{
\operatorname{span}_{\mathbb R}\{P_a(t):a,t\}=\operatorname{Herm}(d).
}
\]

Therefore

\[
\langle n_a(t)\rangle_+=\langle n_a(t)\rangle_-\;\forall a,t
\Rightarrow
\rho_+=\rho_-.
\]

So a distinct state pair with identical **complete** local-density history and different response is impossible in this generic regime.

This is a conditional no-go, not a universal field-theory statement.

## 6. New observability-rank principle

The correct experimental null problem is finite-resolution, not infinite exact tomography.

For calibrated observables/settings

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

The invisible Hermitian subspace is

\[
\mathcal N_{obs}=\mathcal S_M^\perp,
\qquad
\boxed{\dim\mathcal N_{obs}=d^2-r_{obs}.}
\]

Add the symmetrized-noise equality operators to the constraint span. A response witness exists exactly when at least one commutator/retarded operator has a nonzero projection into the remaining nullspace.

This is now the central finite-mode experiment-design formulation.

## 7. Why Toy 006 matters

RQIR should match all source information actually calibrated by the declared experiment, but must not demand an idealized complete source history that already reconstructs the entire quantum state.

The practical target lies between:

- under-calibrated NP2, where classical mean-field confounds remain;
- full informational completeness, where no distinct null-pair state remains at all.

The design problem is to close nuisance directions while retaining a target ordered-response direction.

## 8. Current external boundaries

- Hu & Verdaguer: stochastic gravity contains both noise and dissipation/response through influence-functional/CTP structure, so matter response does not imply quantum geometry.
- Howl et al. 2021: nonrelativistic quantized matter density takes the standard `m Psi† Psi` / fixed-particle delta-density form used by PE-1.
- Aziz & Howl 2025: full-QFT matter can generate entanglement with classical gravity in suitable local models, so entanglement alone is not a unique quantum-gravity witness.
- Yant & Blencowe 2026: current gravitational-entanglement modelling can be formulated directly in QFT with operational field observables, reinforcing RQIR's field/observable-first direction.
- Czerwinski 2020: known dynamics plus repeated-time measurements can generate informationally complete quantum tomography, providing external context for RQIR-NG-003.

## 9. Consistency gates to keep active

Especially important now:

- `G1` gauge/relational formulation;
- `G2` full conservation/Bianchi embedding;
- `G3/G3b` positivity/unitarity/spectral identities;
- `G4a` retarded causal support;
- `G8` weak-field/Newtonian control;
- `G10/G10a` smearing/renormalization for field stress tensor;
- `G12/G12a` classical/stochastic/full-QFT degeneracy audit;
- `G13` measurable detector transfer and sensitivity.

## 10. Epistemic labels

- `DEF` definition/convention
- `EST` established external result
- `DRV` RQIR analytic derivation
- `NUM` numerical result
- `EMP` empirical constraint
- `CONJ` conjecture
- `OPEN` unresolved
- `NEG` failed/excluded branch or conditional no-go

Never promote a toy result or conditional no-go beyond its stated assumptions.

## 11. Current repository core

- `README.md`
- `docs/FOUNDATIONS.md`
- `docs/MASTER_TABLE.md`
- `docs/ORDERED_KERNEL_HIERARCHY.md`
- `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`
- `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`
- `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`
- `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`
- `docs/TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md`
- `docs/TOY_MODEL_006_DENSITY_HISTORY_TOMOGRAPHY_NO_GO.md`
- `analysis/search_balanced_ordered_kernel.py`
- `analysis/search_real_newtonian_embedding.py`
- `analysis/check_density_history_tomography.py`
- `research_log/` dated chronology

## 12. Exact next target — Toy 007

**Finite multiprobe optimal nullspace design.**

1. Choose a physically realistic finite set of Newtonian probe locations and times.
2. Build the equality-constraint operator span for calibrated means and symmetrized auto/cross-noise.
3. Compute its rank and nullspace.
4. Project candidate commutator/retarded operators onto that nullspace.
5. Optimize probe geometry/timing to constrain ordinary mean/noise nuisance directions while retaining the largest measurable response direction.
6. Derive the source-to-detector transfer law

\[
(\langle T\rangle,N_T,\chi_T^R)
\rightarrow
(\langle O_p\rangle,N_p,\chi_p^R).
\]

7. Only after this, estimate laboratory signal size and compare competing semiclassical/stochastic/classical-QFT/perturbative-QG fingerprints.

## 13. Continuation protocol

At each substantive iteration:

1. read this guide and latest log;
2. state one exact unresolved target;
3. derive analytically before adding numerical complexity;
4. run applicable consistency gates;
5. preserve positive and negative results;
6. record reproducibility code for numerical claims;
7. update `MASTER_TABLE.md` and this guide when the project state changes;
8. keep the repository, not chat history, as authoritative memory.
