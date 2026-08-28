# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)

This file is the continuity backbone of the project. A new session should be able to resume RQIR by reading this file plus the documents it references.

## 1. Project objective

RQIR reconstructs the operational interface between relativity/gravity and quantum physics **without assuming in advance** that gravity is classical, stochastic, quantized, emergent, hybrid, or described by a particular UV theory.

Central inverse problem:

\[
P_{\rm data}(\mathbf o|\mathbf s)
\Rightarrow
[\mathfrak I].
\]

`[I]` is the equivalence class of interface maps compatible with observations and consistency requirements.

## 2. Core discipline

- observable first;
- baseline declared explicitly;
- residuals only relative to controlled baselines;
- common observable language for competing interface classes;
- degeneracies/no-go results retained as primary results;
- no “quantum gravity detected” claim until classical/stochastic/hybrid/full-QFT-matter explanations are excluded in the same regime;
- low-energy and experimentally accessible channels before Planck-scale speculation;
- repository is authoritative project memory.

## 3. Baseline benchmark

Semiclassical gravity:

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}+H_{\mu\nu}^{\rm EFT}
=8\pi G\langle\hat T_{\mu\nu}\rangle_{\rm ren}.
\]

This is a benchmark, not the assumed true theory.

## 4. Residual object

For operational observable `O_A` and baseline `B`,

\[
\Delta_A^{(B)}=O_A^{\rm obs}-O_A^{(B)}.
\]

Always record regime, uncertainty/covariance and nuisance assumptions.

## 5. Ordered source hierarchy — current mathematical core

The original single `C^(2)` hierarchy has been superseded because operator ordering matters.

Define

\[
\delta\hat T_A(x)=\hat T_A(x)-\langle\hat T_A(x)\rangle.
\]

Current second-order coordinate:

\[
\boxed{
\mathcal K_T^{(2)}
=\left(\langle T\rangle,N,D\;\text{or}\;\chi^R\right)
}
\]

with

\[
N_{AB}(x,y)=\frac12\langle\{\delta T_A(x),\delta T_B(y)\}\rangle,
\]

\[
D_{AB}(x,y)=\frac1{2i}\langle[\delta T_A(x),\delta T_B(y)]\rangle,
\]

and one convention for retarded response

\[
\chi^R_{AB}(x,y)=\frac{i}{\hbar}\theta(x^0-y^0)
\langle[T_A(x),T_B(y)]\rangle.
\]

A Schwinger–Keldysh / closed-time-path generating functional is the formal parent object for all higher operator orderings:

\[
Z_T[J_+,J_-]=Tr(U[J_+]\rho_TU[J_-]^\dagger).
\]

See `docs/ORDERED_KERNEL_HIERARCHY.md` and `docs/FOUNDATIONS.md`.

## 6. Operational sensitivity levels

- `L1`: mean-sensitive — only `<T>`;
- `L2`: noise-sensitive — `N` also matters;
- `L3`: ordered-response-sensitive — `D/chi^R` also matters;
- `L4`: higher ordered cumulants/nested responses;
- `L5`: quantum-information/process constraints.

These are sensitivity classes, **not** declarations that the metric is quantum.

## 7. Working channels

- `Q1` Quantum clocks / proper time.
- `Q2` Superposed sources.
- `Q3` Backreaction / source rule.
- `Q4` Gravity-mediated quantum information.
- `Q5` Geometry fluctuations.
- `Q6` Causal/process structure.
- `Q7` Low-energy quantum-gravity EFT.

## 8. Critical external boundary adopted

Gravity-mediated entanglement alone is **not** treated as an unambiguous proof of quantized gravity.

Aziz & Howl, Nature 646, 813–817 (2025), show that when matter is treated in full QFT, local classical-gravity constructions can generate quantum communication and entanglement through matter processes, with different parametric behavior from perturbative quantum gravity.

Therefore RQIR uses multi-observable/scaling fingerprints.

## 9. Toy Model 001 — same mean, different variance

File: `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`.

States

\[
|A\rangle=(|2,0\rangle+|0,2\rangle)/\sqrt2,
\qquad
|B\rangle=|1,1\rangle
\]

have the same mean mass distribution but different covariance. This establishes a mean-vs-fluctuation discriminator but **not** a coherence witness.

## 10. RQIR-NG-001 — static density phase blindness

File: `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.

For

\[
|\psi_\pm\rangle=(|2,0\rangle\pm|0,2\rangle)/\sqrt2
\]

and the corresponding incoherent mixture, all observables diagonal in the occupation/mass-configuration basis have identical statistics.

For a density-diagonal controlled source–probe interaction, the reduced probe state depends only on source diagonal probabilities, so source phase is invisible to probe-only measurements in this idealized domain.

**Meaning:** static superposition-vs-mixture is not automatically a gravitational coherence witness.

## 11. Toy Model 003 / RQIR-NG-002 — same noise, different response, but energy confound

File: `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.

For

\[
H=(\hbar\Omega/2)\sigma_x,
\qquad
n_L=(I+\sigma_z)/2,
\]

states `|+x>` and `|-x>` satisfy

\[
\langle n_L(t)\rangle_+=\langle n_L(t)\rangle_-=1/2,
\]

\[
N_+=N_-=\frac14\cos\Omega t,
\]

but

\[
D_\pm=\pm\frac14\sin\Omega t.
\]

However

\[
\langle H\rangle_\pm=\pm\hbar\Omega/2,
\]

so the minimal qubit is not a clean equal-full-stress-energy gravitational null pair.

## 12. Toy Model 004 — balanced five-level ordered-kernel witness

File: `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`.

A finite-dimensional numerical search found a positive five-level Hamiltonian, positive Hermitian source observable `B`, and positive density matrices `rho±` satisfying

\[
\boxed{
\langle H\rangle_+=\langle H\rangle_-,
\quad
\langle B(t)\rangle_+=\langle B(t)\rangle_-\;\forall t,
\quad
N_+(t,0)=N_-(t,0)\;\forall t,
\quad
D_+(t,0)\neq D_-(t,0).
}
\]

Common mean energy in the chosen units: `3.4`.

At one checked time near `t=3.26726`:

\[
N_+=N_-\approx0.803678,
\]

\[
D_+\approx+0.535468,
\qquad
D_-\approx-0.535468.
\]

Reproducibility code: `analysis/search_balanced_ordered_kernel.py`.

### Interpretation

The Toy 003 mean-energy obstruction is **not universal**. Even matching mean energy, the entire one-point history of a source observable, and its reference-time symmetrized noise does not mathematically determine the commutator/retarded sector.

Thus

\[
(\langle H\rangle,\langle B\rangle,N)\not\Rightarrow D.
\]

### Critical limitation

`B` is not yet embedded as a covariantly conserved local/smeared stress-energy observable of a full relativistic source + control apparatus.

Equality of global mean energy does not establish

\[
\langle T_{\mu\nu}(x)\rangle_+=\langle T_{\mu\nu}(x)\rangle_-.
\]

This is now the main physical gate.

## 13. Dimension-search observation

Recorded numerical search:

- `d=2`: no witness in 500 random trials;
- `d=3`: no witness in 1500 random trials;
- `d=4`: no witness in 5000 random trials;
- `d=5`: witness found quickly for the recorded seed.

Do **not** call five the minimal dimension. This is numerical evidence only.

Working conjecture `CONJ-RQIR-001`: under generic conditions used by the search, an independent ordered-response direction may require dimension at least five. Must be proved or falsified.

## 14. Consistency gates

Current gates are in `docs/FOUNDATIONS.md`. Especially important now:

- `G2` full conservation/Bianchi embedding;
- `G3b` valid quantum spectral/commutator structure;
- `G4a` causal retarded support;
- `G10/G10a` smearing and renormalized stress-tensor kernels;
- `G12/G12a` classical/stochastic response degeneracy audit;
- `G13` operational measurability.

## 15. Epistemic labels

- `DEF` definition/convention
- `EST` established external result
- `DRV` RQIR analytic derivation
- `NUM` numerical result
- `EMP` empirical constraint
- `CONJ` conjecture
- `OPEN` unresolved
- `NEG` failed/excluded branch or negative result

Never promote `CONJ`, `OPEN`, `NUM` toy behavior, or a conditional no-go beyond its stated domain.

## 16. Current repository structure

- `README.md` — project charter.
- `docs/FOUNDATIONS.md` — current mathematical foundations v0.2.
- `docs/MASTER_TABLE.md` — current operational channel/degeneracy table v0.2.
- `docs/ORDERED_KERNEL_HIERARCHY.md` — ordered/CTP hierarchy.
- `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`.
- `docs/TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.
- `docs/TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.
- `docs/TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`.
- `analysis/search_balanced_ordered_kernel.py` — reproducibility search code.
- `docs/RECOVERY_GUIDE.md` — this document.
- `research_log/` — dated chronology.

## 17. Exact next research target

The next iteration must move from arbitrary finite-dimensional operator algebra toward **physical stress-energy structure**.

Priority:

1. Search structured oscillator/atomic/molecular realizations for the Toy 004 ordered-kernel split.
2. Require equality of the full relevant smeared mean stress-energy, not only global energy.
3. Extend matching from `N(t,0)` to the required two-time domain `N(t,t')`.
4. Derive a common probe transfer law

\[
(\langle T\rangle,N,\chi^R)
\to
(\text{probe mean phase},\text{noise},\text{phase lag/response}).
\]

5. Fit this structure across semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG interface classes.
6. Attempt proof/counterexample for the apparent low-dimensional obstruction.
7. Begin Q4 perturbative-order/scaling comparison using Aziz–Howl versus perturbative quantum gravity.

## 18. Continuation protocol

At each substantive iteration:

1. read this recovery guide;
2. inspect the latest research log;
3. state one exact unresolved target;
4. perform analytic work before numerical complexity where possible;
5. run all applicable consistency gates;
6. preserve positive, negative and null results;
7. update `MASTER_TABLE.md` when discriminants/degeneracies change;
8. update this guide whenever project state or next target changes;
9. add dated research log and reproducibility code for numerical claims.

The repository, not chat history, is the authoritative project memory.