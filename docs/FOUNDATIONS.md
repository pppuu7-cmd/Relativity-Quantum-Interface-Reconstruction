# RQIR Foundations v0.1

**Date:** 2026-08-29  
**Status:** bootstrap definitions; not yet a physical theory.

## 1. Scope

RQIR studies the interface between relativistic spacetime physics and quantum theory without assuming in advance whether gravity is fundamentally classical, stochastic, quantum, emergent, or only an effective description of deeper degrees of freedom.

The programme is explicitly **operational** and **model-comparative**.

## 2. Baseline layers

### 2.1 Classical GR

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
\]

### 2.2 QFT on a prescribed curved spacetime

Matter is quantized on a classical background \(g_{\mu\nu}\). Operational predictions are built from renormalized local or relational observables and correlation functions.

### 2.3 Semiclassical gravity

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}+H_{\mu\nu}^{\rm EFT}
=8\pi G\,\langle \hat T_{\mu\nu}\rangle_{\rm ren}.
\]

Here \(H_{\mu\nu}^{\rm EFT}\) denotes allowed higher-curvature/effective terms required by the chosen low-energy truncation and renormalization prescription. This equation is a benchmark only.

### 2.4 Stochastic extension

A schematic Einstein–Langevin form is

\[
G_{\mu\nu}[g+h]+\Lambda(g_{\mu\nu}+h_{\mu\nu})+\cdots
=8\pi G\left(\langle \hat T_{\mu\nu}\rangle+\xi_{\mu\nu}\right),
\]

with stochastic source correlations linked to the stress-energy noise kernel,

\[
N_{\mu\nu\rho\sigma}(x,y)
\equiv \frac12\left\langle
\left\{\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)\right\}
\right\rangle_{\rm ren}.
\]

This provides a controlled example showing why the first moment of \(T_{\mu\nu}\) is insufficient to characterize the interface.

### 2.5 Low-energy quantum gravity EFT

The metric can be decomposed schematically as

\[
g_{\mu\nu}=\bar g_{\mu\nu}+\kappa h_{\mu\nu},
\]

with perturbative quantum fluctuations treated in the regime where the effective expansion is controlled. RQIR uses EFT predictions as a low-energy benchmark, not as a claim of UV completeness.

## 3. Operational observable space

Let \(\mathcal O=\{O_A\}\) denote a set of operationally meaningful observables. Examples include:

- clock readouts and proper-time differences;
- relative interferometric phases;
- transition probabilities;
- connected correlation functions;
- entanglement witnesses and entanglement measures;
- decoherence/dephasing rates;
- force/acceleration spectra;
- scattering amplitudes or cross sections in controlled EFT regimes;
- curvature or metric-noise proxies defined relationally;
- causal-order/process observables.

The label \(A\) includes all experimental settings, spacetime locations only when operationally defined, state preparation, coarse graining, detector response, and renormalization prescription needed to make the observable meaningful.

## 4. Baseline-residual map

For each observable and domain \(D\), choose an explicit controlled baseline \(B\):

\[
\Delta_A^{(B)}(D)
\equiv O_A^{\rm obs}(D)-O_A^{(B)}(D).
\]

A residual is incomplete unless the following tuple is recorded:

\[
R_A=\left(\Delta_A, B, D, \Sigma_A^{\rm exp}, \Sigma_A^{\rm th}, \mathcal N_A\right),
\]

where \(\Sigma^{\rm exp}\) and \(\Sigma^{\rm th}\) are experimental and theoretical uncertainty/covariance structures and \(\mathcal N_A\) records nuisance assumptions.

### Rule R1

Residuals defined relative to different baselines must not be added, compared, or jointly interpreted before an explicit baseline transformation is given.

## 5. Correlation hierarchy

Define fluctuations

\[
\delta \hat T_{\mu\nu}(x)=\hat T_{\mu\nu}(x)-\langle\hat T_{\mu\nu}(x)\rangle.
\]

The interface hierarchy includes

\[
C^{(1)}_{\mu\nu}(x)=\langle\hat T_{\mu\nu}(x)\rangle,
\]

\[
C^{(2)}_{\mu\nu\rho\sigma}(x,y)
=\langle\delta \hat T_{\mu\nu}(x)\delta \hat T_{\rho\sigma}(y)\rangle,
\]

and higher connected cumulants \(C^{(n)}\).

RQIR does **not** assume that the full hierarchy sources independent gravitational degrees of freedom. Instead it asks which members of this hierarchy are operationally visible through gravity and with what transfer law.

## 6. Interface map

Introduce an abstract interface map

\[
\mathfrak I:\quad
(\rho_{\rm matter},\mathcal G,\mathcal C,\lambda)
\longrightarrow
P(\mathbf o\mid\mathbf s),
\]

where:

- \(\rho_{\rm matter}\) represents quantum matter preparation;
- \(\mathcal G\) is the spacetime/gravitational state or effective structure;
- \(\mathcal C\) encodes causal/reference-frame data;
- \(\lambda\) denotes model and nuisance parameters;
- \(P(\mathbf o\mid\mathbf s)\) is the operational prediction for outcomes \(\mathbf o\) given settings \(\mathbf s\).

The central inverse problem is:

\[
P_{\rm data}(\mathbf o\mid\mathbf s)
\quad\Rightarrow\quad
[\mathfrak I],
\]

where \([\mathfrak I]\) is an experimentally indistinguishable equivalence class of interface maps.

This formulation is deliberately more general than quantizing \(g_{\mu\nu}\).

## 7. Fingerprints and degeneracy

For a model or interface class \(M\), define a fingerprint

\[
\mathbf F_M(D)=
(\Delta_{Q1},\Delta_{Q2},\ldots,\Delta_{Q7},\ldots)_M.
\]

Two classes \(M_1,M_2\) are operationally degenerate over \(D\) if

\[
\|\mathbf F_{M_1}(D)-\mathbf F_{M_2}(D)\|_{\Sigma^{-1}}
<\epsilon
\]

for the experimentally and theoretically justified covariance metric and resolution \(\epsilon\).

This definition is provisional because a universal metric over heterogeneous observables may not exist. In practice, likelihood ratios, Bayes factors, profile likelihoods, or channel-specific test statistics may replace the schematic norm.

## 8. Minimal discriminant problem

Given candidate classes \(\{M_i\}\), find the smallest observable subset \(S\subset\mathcal O\) such that

\[
\forall i\neq j:\quad
P(O_S\mid M_i)\not\simeq P(O_S\mid M_j)
\]

within a specified domain and resolution.

This is a central RQIR optimization target: **not the largest number of observables, but the smallest experimentally feasible set that breaks the important degeneracies.**

## 9. Consistency gates

Every derived model-dependent prediction must pass, when applicable:

- **G0 Dimensional consistency**
- **G1 Coordinate/gauge or relational-observable consistency**
- **G2 Conservation/Bianchi consistency**
- **G3 Positivity/unitarity/complete-positivity check appropriate to the formulation**
- **G4 No-signalling / causal consistency appropriate to the assumed causal framework**
- **G5 Classical limit \(\hbar\to0\)**
- **G6 Gravity-off limit \(G\to0\)**
- **G7 Flat-spacetime limit**
- **G8 Newtonian/weak-field limit**
- **G9 EFT power-counting validity**
- **G10 Renormalization/smearing consistency**
- **G11 Known precision-test consistency**
- **G12 Degeneracy audit against non-quantum-gravity explanations**
- **G13 Operational measurability**

Passing these gates is necessary, not sufficient, for physical viability.

## 10. Initial channel definitions

### Q1 — Quantum clocks / proper time

Question: how are clock phases/readouts predicted when path, velocity, gravitational potential, or reference frame is in a quantum superposition?

Primary observables: conditional clock probabilities, visibility, relative phase, clock-clock correlations.

### Q2 — Superposed gravitational sources

Question: what gravitational response corresponds to a massive quantum state with spatially separated branches or internal-state-dependent mass-energy?

Primary observables: probe phase, force/acceleration statistics, branch-conditioned correlations.

### Q3 — Backreaction/source rule

Question: what object determines gravitational response — expectation value, stochastic realization, conditional state, local classical field coupled to QFT, operator-valued metric, or other relational structure?

Primary observables: nonlinear response, noise, branch dependence, state-update sensitivity.

### Q4 — Gravity-mediated quantum information

Question: what quantum information can be generated, transmitted, or witnessed when gravity is the only intended coupling?

Primary observables: entanglement witnesses, negativity/concurrence where appropriate, phase structure, scaling with mass/time/separation, higher-order correlations.

Important caution: entanglement alone must not automatically be labeled a proof that the gravitational field itself is quantized. Recent full-QFT analyses exhibit classical-gravity mechanisms capable of generating entanglement with different scaling.

### Q5 — Geometry fluctuations

Question: are observed metric/curvature fluctuations fully explainable as induced fluctuations from quantum matter and detector noise, or is an independent gravitational fluctuation sector required?

### Q6 — Causal/process structure

Question: can operational causal relations or reference-frame relations display nonclassical structure attributable specifically to gravity/spacetime?

### Q7 — Low-energy quantum gravity EFT

Question: what predictions are fixed or parametrically controlled at energies well below the Planck scale independently of a UV completion?

## 11. Epistemic labels

Each result must carry one label:

- `DEF` — definition/convention
- `EST` — established external result
- `DRV` — analytic derivation made in RQIR
- `NUM` — numerical result
- `EMP` — empirical/experimental constraint
- `CONJ` — conjecture
- `OPEN` — unresolved question
- `NEG` — excluded/failed branch or negative result

A statement may carry multiple labels only if its components are explicitly separated.

## 12. Immediate mathematical tasks

1. Replace the schematic residual vector by a statistically rigorous likelihood-level construction.
2. Determine which channel observables can be formulated diffeomorphism-invariantly or relationally.
3. Separate matter-induced metric fluctuations from intrinsic gravitational fluctuations.
4. Derive scaling fingerprints for Q4 under at least semiclassical, stochastic, local classical-QFT, and perturbative quantum-gravity baselines.
5. Establish cross-channel consistency relations, especially Q1↔Q2↔Q3 and Q3↔Q4↔Q5.
6. Identify no-go combinations: observable patterns impossible for whole classes of interface maps.

## 13. Seed literature status

The following are starting references, not an exhaustive review:

- Donoghue 2022, arXiv:2211.09902 — low-energy quantum GR as EFT.
- Hu & Verdaguer 2008, arXiv:0802.0658 — stochastic gravity and the noise kernel.
- Smith & Ahmadi 2020, Nature Communications 11, 5360 — quantum clocks and relativistic time dilation framework.
- Aziz & Howl 2025, Nature 646, 813–817 — demonstration that full-QFT matter can permit entanglement generation even with a classical gravitational field, motivating stronger discriminants than entanglement alone.

These references establish useful boundaries of the reconstruction problem but do not determine its solution.