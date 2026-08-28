# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)

This file is the continuity backbone of the project. A new session should be able to resume RQIR by reading this file plus the documents it references.

## 1. Project objective

RQIR aims to reconstruct the operational interface between general relativity and quantum physics **without assuming in advance** that the gravitational field is classical, stochastic, quantized, emergent, or described by any specific UV theory.

The central inverse problem is:

\[
P_{\rm data}(\mathbf o\mid\mathbf s)
\quad\Rightarrow\quad
[\mathfrak I],
\]

where \([\mathfrak I]\) is the equivalence class of interface maps compatible with observations and consistency requirements.

## 2. Core philosophy

The project follows the same methodological discipline as a model-independent reconstruction programme:

- observable first;
- baseline declared explicitly;
- residuals defined only relative to controlled baselines;
- competing theory classes represented in a common observable language;
- degeneracies treated as central results, not nuisances;
- no claim of “quantum gravity detected” unless alternative classical/stochastic/hybrid mechanisms are excluded in the same regime;
- low-energy and experimentally accessible channels are prioritized before Planck-scale speculation;
- failed branches and no-go results remain in the repository.

## 3. Primary mathematical objects

### 3.1 Semiclassical benchmark

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}+H_{\mu\nu}^{\rm EFT}
=8\pi G\langle\hat T_{\mu\nu}\rangle_{\rm ren}.
\]

This is a benchmark, not the assumed true theory.

### 3.2 Residual

For operational observable \(O_A\) and baseline \(B\),

\[
\Delta_A^{(B)}
=O_A^{\rm obs}-O_A^{(B)}.
\]

Always record baseline, regime, theory uncertainty, experimental covariance and nuisance assumptions.

### 3.3 Stress-energy fluctuation hierarchy

\[
\delta\hat T_{\mu\nu}
=\hat T_{\mu\nu}-\langle\hat T_{\mu\nu}\rangle,
\]

\[
N_{\mu\nu\rho\sigma}(x,y)
=\frac12\langle\{\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)\}\rangle_{\rm ren}.
\]

Higher connected cumulants must be tracked when relevant.

### 3.4 Abstract interface map

\[
\mathfrak I:
(\rho_{\rm matter},\mathcal G,\mathcal C,\lambda)
\rightarrow
P(\mathbf o\mid\mathbf s).
\]

This deliberately does not assume an operator-valued metric.

### 3.5 Model fingerprint

\[
\mathbf F_M
=(\Delta_{Q1},\Delta_{Q2},\ldots,\Delta_{Q7},\ldots)_M.
\]

The project seeks minimal observable subsets that distinguish important model/interface classes.

## 4. Initial channels

- `Q1` Quantum clocks / proper time.
- `Q2` Superposed sources.
- `Q3` Backreaction / source rule.
- `Q4` Gravity-mediated quantum information.
- `Q5` Geometry fluctuations.
- `Q6` Causal/process structure.
- `Q7` Low-energy quantum gravity EFT.

These are working channels, not immutable categories.

## 5. Critical established boundary already adopted

The project must **not** treat gravity-mediated entanglement alone as an unambiguous proof that the gravitational field itself is quantized.

Reason: Aziz & Howl, Nature 646, 813–817 (2025), show that once matter is treated using full QFT, local classical-gravity models can generate entanglement through quantum matter processes, with distinguishable scaling. This makes multi-observable/scaling discrimination mandatory.

Reference: https://www.nature.com/articles/s41586-025-09595-7

## 6. First RQIR derivation completed

See `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md`.

Two two-mode source states are defined:

\[
|A\rangle=\frac{|2,0\rangle+|0,2\rangle}{\sqrt2},
\qquad
|B\rangle=|1,1\rangle.
\]

They have equal mean occupations,

\[
\langle n_L\rangle_A=\langle n_R\rangle_A
=\langle n_L\rangle_B=\langle n_R\rangle_B=1,
\]

but different covariance matrices,

\[
\Sigma_A^{(n)}=
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
\Sigma_B^{(n)}=0.
\]

For a weak-field probe,

\[
\langle\Phi\rangle_A=\langle\Phi\rangle_B
=-Gm\left(\frac1{r_L}+\frac1{r_R}\right),
\]

while the source-statistics potential variance differs:

\[
\operatorname{Var}_A(\Phi)
=G^2m^2\left(\frac1{r_L}-\frac1{r_R}\right)^2,
\qquad
\operatorname{Var}_B(\Phi)=0.
\]

Interpretation: a pure expectation-value mean-field law cannot distinguish the states through their equal one-point mass density, whereas a fluctuation-sensitive interface can in principle respond differently.

### Important limitation

Toy Model 001 is **not a coherence witness**. In the zero-overlap density basis, the NOON pure state and the corresponding incoherent mixture have the same diagonal occupation statistics. Therefore classical statistical variance remains a degeneracy.

This limitation is an explicit result, not a defect to hide.

## 7. Exact next research target

### Toy Model 002 — Same classical density statistics, different quantum coherence

Construct two source preparations that agree in the relevant classical/diagonal source statistics but differ in off-diagonal coherence, then derive an operational observable that responds differently under at least one interface class.

Priority candidate approaches:

1. finite-overlap localized modes, where local stress/mass-density matrix elements acquire coherence-sensitive cross terms;
2. time-dependent recombination, creating unequal-time correlators sensitive to phase coherence;
3. ancilla-assisted joint source–probe correlations;
4. relational observables that compare source coherence before and after gravitational interaction;
5. common influence-functional formulation allowing semiclassical/stochastic/quantized comparison.

The next derivation should answer:

> Can RQIR construct a null pair with the same one-point density and the same relevant classical stochastic density moments, but a different gravitationally accessible coherence-sensitive observable?

If not, that itself becomes a no-go/degeneracy result.

## 8. Consistency gates

Use the gates in `docs/FOUNDATIONS.md` for every derived prediction:

`G0` dimensions; `G1` gauge/relational; `G2` conservation/Bianchi; `G3` positivity/unitarity/CP; `G4` causal/no-signalling; `G5` classical limit; `G6` gravity-off; `G7` flat limit; `G8` Newtonian/weak field; `G9` EFT power counting; `G10` renormalization/smearing; `G11` known tests; `G12` degeneracy audit; `G13` measurability.

## 9. Epistemic labels

- `DEF`: definition/convention
- `EST`: established external result
- `DRV`: RQIR analytic derivation
- `NUM`: numerical result
- `EMP`: empirical constraint
- `CONJ`: conjecture
- `OPEN`: unresolved
- `NEG`: failed/excluded branch

Never promote `CONJ`, `OPEN`, or toy-model behavior to an empirical fact.

## 10. Current repository structure

- `README.md` — project charter and rules.
- `docs/FOUNDATIONS.md` — mathematical foundations v0.1.
- `docs/MASTER_TABLE.md` — observable channels and degeneracies.
- `docs/TOY_MODEL_001_SAME_MEAN_DIFFERENT_VARIANCE.md` — first explicit null construction.
- `docs/RECOVERY_GUIDE.md` — this recovery document.
- `research_log/` — dated iteration chronology.

## 11. Seed literature

- Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
- Hu & Verdaguer, *Stochastic Gravity: Theory and Applications*, arXiv:0802.0658.
- Smith & Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
- Aziz & Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025).

Literature expansion remains a major pending task. The bibliography must eventually distinguish reviews, formal results, experimental proposals, actual measurements, and contested interpretations.

## 12. Continuation protocol

At each substantive iteration:

1. read this recovery guide;
2. inspect the latest dated research log;
3. state the exact unresolved target;
4. perform analytic work before adding numerical complexity where possible;
5. run all applicable gates;
6. record both positive and negative results;
7. update `MASTER_TABLE.md` when a degeneracy or discriminator changes;
8. update this recovery guide if the project state or next target changes;
9. append a dated research-log entry with commit/result chronology.

The repository, not chat history, is intended to be the authoritative project memory.