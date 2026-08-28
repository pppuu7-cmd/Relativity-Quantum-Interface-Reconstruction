# RQIR Foundations v0.2

**Date:** 2026-08-29  
**Status:** operational reconstruction framework; not a physical theory.

## 1. Scope

RQIR studies the interface between relativistic spacetime physics and quantum theory without assuming in advance whether gravity is fundamentally classical, stochastic, quantum, emergent, hybrid, or an effective description of deeper degrees of freedom.

The programme is explicitly **operational**, **model-comparative**, and **degeneracy-aware**.

## 2. Baseline layers

### 2.1 Classical GR

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
\]

### 2.2 QFT on a prescribed curved spacetime

Matter is quantized on a classical background `g_{mu nu}`. Predictions are built from renormalized local, smeared or relational observables and correlation functions.

### 2.3 Semiclassical gravity

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}+H_{\mu\nu}^{\rm EFT}
=8\pi G\,\langle \hat T_{\mu\nu}\rangle_{\rm ren}.
\]

This is a benchmark, not the assumed true theory.

### 2.4 Stochastic gravity

A schematic Einstein–Langevin form is

\[
G_{\mu\nu}[g+h]+\Lambda(g_{\mu\nu}+h_{\mu\nu})+\cdots
=8\pi G\left(\langle \hat T_{\mu\nu}\rangle+\xi_{\mu\nu}\right),
\]

with stochastic source covariance linked to the symmetrized stress-energy noise kernel.

The influence-functional formulation also contains dissipation/response structure. This established fact is important because it proves that `mean` and `noise` are not the only second-order objects relevant to a gravity–quantum interface.

### 2.5 Low-energy quantum-gravity EFT

Write schematically

\[
g_{\mu\nu}=\bar g_{\mu\nu}+\kappa h_{\mu\nu}
\]

and quantize perturbations in the regime where the EFT expansion is controlled. RQIR uses this as a low-energy benchmark, not a UV completion.

## 3. Operational observable space

Let

\[
\mathcal O=\{O_A\}
\]

be operationally meaningful observables, including:

- clock readouts and proper-time differences;
- interferometric phases and visibilities;
- transition probabilities;
- connected correlation functions;
- noise and response spectra;
- entanglement witnesses/measures;
- decoherence/dephasing rates;
- force/acceleration spectra;
- scattering observables in controlled EFT regimes;
- relational curvature/metric-noise proxies;
- causal-order/process observables.

The index `A` includes experimental settings, state preparation, smearing/coarse graining, detector response and the renormalization prescription required to make the observable meaningful.

## 4. Baseline-residual map

For observable `O_A`, domain `D`, and explicit baseline `B`,

\[
\Delta_A^{(B)}(D)
\equiv O_A^{\rm obs}(D)-O_A^{(B)}(D).
\]

A complete residual record is

\[
R_A=\left(
\Delta_A,
B,
D,
\Sigma_A^{\rm exp},
\Sigma_A^{\rm th},
\mathcal N_A
\right),
\]

where the covariance structures and nuisance assumptions are explicit.

### Rule R1 — baseline discipline

Residuals defined relative to different baselines must not be combined or compared before an explicit baseline transformation is provided.

## 5. Ordered stress-energy hierarchy

Define

\[
\delta\hat T_A(x)=\hat T_A(x)-\langle\hat T_A(x)\rangle.
\]

The v0.1 notation `C^(2)` is insufficient whenever operators do not commute. RQIR v0.2 therefore preserves operator ordering.

### 5.1 One-point sector

\[
J_A(x)=\langle\hat T_A(x)\rangle.
\]

### 5.2 Greater/lesser correlators

\[
G^>_{AB}(x,y)
=\langle\delta\hat T_A(x)\delta\hat T_B(y)\rangle,
\]

\[
G^<_{AB}(x,y)
=\langle\delta\hat T_B(y)\delta\hat T_A(x)\rangle.
\]

### 5.3 Symmetrized/noise kernel

\[
\boxed{
N_{AB}(x,y)
=\frac12\langle\{\delta\hat T_A(x),\delta\hat T_B(y)\}\rangle
}
\]

with

\[
N=\frac12(G^>+G^<).
\]

### 5.4 Antisymmetric/commutator kernel

\[
\boxed{
D_{AB}(x,y)
=\frac{1}{2i}\langle[\delta\hat T_A(x),\delta\hat T_B(y)]\rangle
}
\]

with

\[
G^>-G^<=2iD.
\]

### 5.5 Retarded response

Using one declared sign convention,

\[
\boxed{
\chi^R_{AB}(x,y)
=\frac{i}{\hbar}\theta(x^0-y^0)
\langle[\hat T_A(x),\hat T_B(y)]\rangle.
}
\]

Therefore, up to convention,

\[
\chi^R\propto\theta D.
\]

### Rule K1 — ordering preservation

Different operator orderings may not be collapsed into one `C^(n)` unless an explicit identity, commutativity condition, spacelike-separation statement or classical limit proves them equivalent in the domain used.

## 6. CTP generating object

A compact parent object for all ordered source correlators is the Schwinger–Keldysh / closed-time-path generating functional

\[
Z_T[J_+,J_-]
=\operatorname{Tr}
\left(
U[J_+]\rho_T U[J_-]^\dagger
\right),
\]

with

\[
W_T=-i\hbar\ln Z_T.
\]

Functional derivatives generate branch-ordered correlators, including Wightman, time-ordered, retarded and higher nested-commutator structures.

### RQIR source-side object

RQIR treats the smeared/renormalized equivalence class

\[
[Z_T]
\]

as a candidate source-side information object and asks which projections survive through the gravity interface.

Schematically,

\[
[Z_T]
\xrightarrow{\mathfrak I_G}
[Z_{\rm obs}]
\xrightarrow{\rm detector}
P(\mathbf o|\mathbf s).
\]

This formulation does **not** assume an operator-valued metric.

## 7. Operational sensitivity levels

At second order define the working hierarchy:

- `L1 mean-sensitive`: only `J=<T>` matters;
- `L2 noise-sensitive`: `N` also affects observables;
- `L3 order/response-sensitive`: `D` or `chi^R` also matters;
- `L4 higher-order-sensitive`: genuinely higher CTP cumulants/nested responses are required;
- `L5 quantum-information-sensitive`: entanglement/process observables add independent constraints.

These levels classify **what information is operationally transmitted**, not whether gravity is fundamentally quantum.

## 8. Critical non-implications

### 8.1 Entanglement is not by itself proof of a quantized gravitational field

Full-QFT matter can generate entanglement in local classical-gravity constructions. Therefore Q4 requires scaling/multi-observable discrimination.

### 8.2 Nonzero matter commutator is not proof of quantum geometry

Quantum matter naturally has nonzero commutators, and semiclassical/stochastic formulations with classical geometry already contain matter-induced response/dissipation structures.

### 8.3 Nonzero noise is not proof of intrinsic quantum geometry

Noise can arise from classical source statistics, detector/environmental noise, matter-induced metric fluctuations or intrinsic gravitational fluctuations.

### Rule G12-core

No single nonclassical-looking observable may be interpreted as evidence for quantum gravitational degrees of freedom until the corresponding classical, stochastic, hybrid and full-QFT-matter degeneracies have been tested in the same operational regime.

## 9. Abstract interface map

\[
\mathfrak I:
(\rho_{\rm matter},\mathcal G,\mathcal C,\lambda)
\longrightarrow
P(\mathbf o|\mathbf s).
\]

The inverse problem is

\[
P_{\rm data}(\mathbf o|\mathbf s)
\Rightarrow
[\mathfrak I],
\]

where `[I]` is an experimentally indistinguishable equivalence class.

## 10. Fingerprints and minimal discriminants

For interface/model class `M`,

\[
\mathbf F_M(D)=
(\Delta_{Q1},\ldots,\Delta_{Q7},N,\chi^R,\ldots)_M.
\]

Two models are operationally degenerate in domain `D` if their predicted probability distributions are indistinguishable at the justified resolution after nuisance profiling/marginalization.

The optimization target is the smallest feasible observable subset `S` satisfying

\[
P(O_S|M_i)\not\simeq P(O_S|M_j)
\]

for the important competing classes.

## 11. Consistency gates

Every derived prediction must pass, where applicable:

- `G0` dimensional consistency;
- `G1` gauge/coordinate or relational consistency;
- `G2` conservation/Bianchi consistency;
- `G3` positivity/unitarity/complete positivity;
- `G3a` positivity of smeared symmetrized covariance where applicable;
- `G3b` valid spectral/commutator identities for the stated quantum/classical model;
- `G4` no-signalling/causal consistency;
- `G4a` retarded support compatible with assumed causal structure;
- `G5` classical limit `hbar -> 0`;
- `G6` gravity-off `G -> 0`;
- `G7` flat-spacetime limit;
- `G8` Newtonian/weak-field limit;
- `G9` EFT power-counting validity;
- `G10` renormalization/smearing consistency;
- `G10a` local stress-tensor kernels require explicit regulator/smearing/renormalization;
- `G11` known precision-test consistency;
- `G12` degeneracy audit;
- `G12a` quantum commutator-derived response must be compared against classical causal-response models;
- `G13` operational measurability.

Passing the gates is necessary, not sufficient.

## 12. Initial channels

### Q1 — Quantum clocks / proper time

Operational clock phases, visibilities, conditional timing and clock-clock correlations when paths, velocities, potentials or frames are quantum-controlled.

### Q2 — Superposed sources

Gravitational response to spatially separated or internal-state-dependent quantum source preparations.

### Q3 — Backreaction/source rule

Which source information controls gravity: expectation value, stochastic realization/noise, retarded response, conditional state, local classical field coupled to QFT, operator-valued geometry or another relational structure?

### Q4 — Gravity-mediated quantum information

What quantum information can be generated or transmitted when gravity is the intended coupling? Entanglement alone is not sufficient; parametric scaling and cross-channel observables are required.

### Q5 — Geometry fluctuations

Can observed gravitational fluctuations be explained by detector/environmental noise and matter-induced fluctuations, or is an independent gravitational fluctuation sector required?

### Q6 — Causal/process structure

Can operational causal relations/reference-frame relations display gravity-specific nonclassical structure?

### Q7 — Low-energy QG EFT

Which predictions are controlled below the Planck scale independently of UV completion?

## 13. Closed toy-model results

### RQIR-NG-001 — Static density phase blindness

For non-overlapping orthogonal mass configurations and a gravitational source/readout diagonal in the mass-configuration basis, states with identical diagonal mass statistics but different relative phase are indistinguishable by static diagonal gravitational observables and probe-only controlled-density interactions.

See `TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.

### RQIR-NG-002 — Minimal response-split energy obstruction

In the minimal qubit realization

\[
H=(\hbar\Omega/2)\sigma_x,
\qquad
n_L=(I+\sigma_z)/2,
\]

`|+x>` and `|-x>` have equal one-point density histories and equal symmetrized density noise, but opposite commutator/retarded response. The same state component produces opposite mean generator energy, so the pair fails as an exact equal-full-`T_{mu nu}` gravity null pair.

See `TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.

## 14. Epistemic labels

- `DEF` definition/convention
- `EST` established external result
- `DRV` RQIR analytic derivation
- `NUM` numerical result
- `EMP` empirical constraint
- `CONJ` conjecture
- `OPEN` unresolved
- `NEG` failed/excluded branch or negative result

No `CONJ`, `OPEN` or toy-model result may be promoted to empirical fact.

## 15. Immediate tasks

1. Find or rule out a balanced multi-level source satisfying equal full mean stress-energy and equal relevant `N` but different `D/chi^R`.
2. Derive a common probe transfer law mapping source `J,N,chi^R` into phase/noise/lag observables.
3. Make residual inference likelihood-level and statistically rigorous.
4. Formalize relational/gauge-invariant observables for Q1/Q5/Q6.
5. Derive Q4 scaling fingerprints for perturbative QG versus classical-gravity + full-QFT matter.
6. Identify cross-channel no-go combinations.
7. Build structured literature and experimental-bound tables.

## 16. Seed literature

- J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
- B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), arXiv:0802.0658.
- N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001), arXiv:gr-qc/0010019.
- A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
- J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.

These references define useful boundaries and established formalisms; they do not determine the RQIR solution.