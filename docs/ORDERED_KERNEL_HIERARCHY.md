# RQIR Ordered-Kernel Hierarchy v0.1

**Date:** 2026-08-29  
**Labels:** `DEF`, `EST`, `DRV`, `OPEN`  
**Motivation:** Toy Model 002 shows that diagonal equal-time moments can be exactly blind to quantum phase. RQIR therefore needs an operator-order-sensitive source description rather than a hierarchy of unordered moments alone.

---

## 1. Why the original `C^(n)` hierarchy is insufficient

The provisional RQIR foundations used

\[
C^{(2)}_{AB}(x,y)=\langle\delta\hat T_A(x)\delta\hat T_B(y)\rangle.
\]

For noncommuting operators this notation hides physically inequivalent objects because

\[
\langle\delta\hat T_A(x)\delta\hat T_B(y)\rangle
\neq
\langle\delta\hat T_B(y)\delta\hat T_A(x)\rangle.
\]

A reconstruction programme must therefore preserve operator ordering.

Indices `A,B` are composite tensor/component labels; spacetime arguments are shown explicitly.

---

## 2. Two-point ordered basis

Define

\[
\delta\hat T_A(x)=\hat T_A(x)-\langle\hat T_A(x)\rangle.
\]

### 2.1 Greater and lesser correlators

\[
G^>_{AB}(x,y)
\equiv
\langle\delta\hat T_A(x)\delta\hat T_B(y)\rangle,
\]

\[
G^<_{AB}(x,y)
\equiv
\langle\delta\hat T_B(y)\delta\hat T_A(x)\rangle.
\]

### 2.2 Symmetrized / noise kernel

\[
\boxed{
N_{AB}(x,y)
\equiv
\frac12\langle
\{\delta\hat T_A(x),\delta\hat T_B(y)\}
\rangle
}
\]

so

\[
N=\frac12(G^>+G^<).
\]

This is the sector used as the stochastic source covariance in the Einstein–Langevin formulation of stochastic gravity, after the required regularization/renormalization/smearing treatment.

### 2.3 Antisymmetric / commutator kernel

Define

\[
\boxed{
D_{AB}(x,y)
\equiv
\frac{1}{2i}
\langle[\delta\hat T_A(x),\delta\hat T_B(y)]\rangle
}
\]

so

\[
G^>-G^<=2iD.
\]

`D` is Hermitian-valued in the sense appropriate to smeared Hermitian observables and captures information that is absent from a classical commuting random-variable description.

### 2.4 Retarded response

With one common sign convention,

\[
\boxed{
\chi^R_{AB}(x,y)
\equiv
\frac{i}{\hbar}\theta(x^0-y^0)
\langle[\hat T_A(x),\hat T_B(y)]\rangle
}
\]

and therefore

\[
\chi^R_{AB}(x,y)
=-\frac{2}{\hbar}\theta(x^0-y^0)D_{AB}(x,y).
\]

Other literature conventions differ by an overall sign; RQIR must record the convention in every calculation.

The stochastic-gravity influence-functional literature contains both a symmetric noise kernel and an antisymmetric dissipation kernel. This established structure is the main external precedent for the RQIR decomposition.

---

## 3. Two-point information vector

At second order the source descriptor should therefore be written as

\[
\boxed{
\mathcal K_T^{(2)}
=
\left(
\langle T\rangle,
N,
D\;\text{or}\;\chi^R
\right)
}
\]

rather than a single `C^(2)`.

This immediately defines three nested interface sensitivities:

- `L1 mean-sensitive`: gravity responds only to \(\langle T\rangle\);
- `L2 noise-sensitive`: gravity also transmits/reflects information in \(N\);
- `L3 response/order-sensitive`: gravitational observables depend on the commutator/retarded sector as well.

These levels are **operational sensitivity classes**, not claims about whether the metric is fundamentally quantum.

---

## 4. Critical non-implication

A nonzero matter commutator is quantum information about the **matter source**. It does not follow that a measured response depending on that commutator proves a quantized gravitational field.

Why:

1. semiclassical/stochastic gravity is formulated with classical geometry but quantum matter and already contains dissipation/response structures inherited from quantum matter;
2. a classical causal mediator can possess a nonzero classical response kernel even though classical random variables commute;
3. full-QFT matter can generate quantum communication/entanglement even in local classical-gravity constructions, as shown by Aziz & Howl (2025).

Therefore RQIR must separate

\[
\text{quantum source structure}
\]

from

\[
\text{quantum gravitational degrees of freedom}.
\]

This is a central `G12` rule.

---

## 5. Closed-time-path generating object

A natural compact descriptor of all operator orderings is a Schwinger–Keldysh / closed-time-path generating functional.

For a source coupled to external tensor-valued probes \(J_+^A,J_-^A\) on the forward/backward branches, define schematically

\[
\boxed{
Z_T[J_+,J_-]
=
\operatorname{Tr}
\left(
U[J_+]\,\rho_T\,U[J_-]^\dagger
\right)
}
\]

and

\[
W_T[J_+,J_-]
=-i\hbar\ln Z_T[J_+,J_-].
\]

Functional derivatives generate time-ordered, anti-time-ordered, Wightman, response and higher nested-commutator structures.

### RQIR proposal

Use the equivalence class of the smeared, renormalized source CTP functional

\[
[Z_T]
\]

as the **source-side information object**, and reconstruct which projections of it survive through the gravity interface into operational data.

The interface problem becomes schematically

\[
[Z_T]
\xrightarrow{\;\mathfrak I_G\;}
[Z_{\rm obs}]
\xrightarrow{\;\text{detector}\;}
P(\mathbf o|\mathbf s).
\]

This does not assume that gravity itself has a Hilbert space.

---

## 6. Higher-order hierarchy

For `n >= 3`, a single connected cumulant is again insufficient. Relevant independent structures include:

- fully symmetrized cumulants;
- nested commutators;
- mixed commutator–anticommutator objects;
- retarded multi-point response functions;
- out-of-time-order structures where operationally justified;
- branch-indexed CTP correlators.

Rather than enumerate an exponentially large basis prematurely, RQIR will use the CTP generating functional as the formal parent object and extract only the ordered components required by a proposed discriminator.

### Rule K1 — ordering preservation

No two correlators with different operator ordering may be merged into one `C^(n)` unless commutativity, spacelike separation, a classical limit, or another explicit identity proves them equivalent in the domain used.

---

## 7. Classical stochastic comparison

For a classical stochastic source `T_cl(x)`, multiplication commutes:

\[
[T_{\rm cl}(x),T_{\rm cl}(y)]=0.
\]

Its stochastic covariance can reproduce a symmetrized kernel

\[
N^{\rm cl}(x,y)
=\mathbb E[\delta T_{\rm cl}(x)\delta T_{\rm cl}(y)].
\]

But a classical dynamical model may still have a causal susceptibility

\[
\chi_{\rm cl}^R(x,y)\neq0
\]

defined from equations of motion or Poisson-bracket response rather than an operator commutator.

Hence the experimentally relevant discriminator is not simply

\[
D\neq0,
\]

but whether the **joint set**

\[
(N,\chi^R,\text{higher responses},\text{cross-channel observables})
\]

obeys relations that cannot be reproduced by the competing classical/stochastic interface class.

---

## 8. Candidate cross-channel consistency relation

At or near equilibrium, fluctuation–dissipation relations link the noise and dissipative/retarded sectors. Stochastic-gravity literature provides explicit examples.

RQIR should therefore search for ratios or spectral relations of the schematic form

\[
\boxed{
\mathcal R_{ND}(\omega)
=\frac{N(\omega)}{\operatorname{Im}\chi^R(\omega)}
}
\]

with all state, temperature, smearing and convention dependence kept explicit.

The discriminating power may lie not in either kernel separately but in the relation between them across independently prepared states.

This is a research target, not yet an RQIR prediction.

---

## 9. Measurement reconstruction problem

The practical inverse problem is now layered:

\[
P_{\rm data}
\Rightarrow
\{\text{probe transfer kernels}\}
\Rightarrow
\{N_T,\chi_T^R,\ldots\}
\Rightarrow
[\mathfrak I_G].
\]

This resembles noise spectroscopy and linear-response tomography, but the gravity channel introduces severe weakness, environmental degeneracy and relativistic consistency requirements.

### Immediate observables to search for

1. source-conditioned probe dephasing / phase-noise spectrum → primarily `N`-sensitive;
2. driven source → probe phase lag / susceptibility → response-sensitive;
3. cross-spectrum between independently monitored source fluctuations and probe readout;
4. state swaps that preserve `N` but change `chi^R` if physically realizable;
5. joint fit of response and noise under one interface law.

---

## 10. Consistency gates specific to ordered kernels

Add the following sub-gates:

- `G3a`: positivity of smeared symmetrized covariance where applicable;
- `G3b`: spectral/commutator identities consistent with a valid quantum state or stated classical model;
- `G4a`: retarded support compatible with the assumed causal structure;
- `G10a`: all local stress-tensor kernels must be defined with an explicit regulator/smearing/renormalization prescription;
- `G12a`: compare quantum commutator-derived response against classical causal-response models before interpreting it as quantum gravity.

---

## 11. External anchors

1. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), arXiv:0802.0658. The review formulates stochastic gravity using the noise kernel and, in the influence-functional description, dissipation and fluctuation structures.
2. N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001), arXiv:gr-qc/0010019.
3. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.

---

## 12. Result

RQIR v0.1's moment hierarchy is upgraded to an ordered hierarchy:

\[
\boxed{
\langle T\rangle
\rightarrow
(N,D/\chi^R)
\rightarrow
\text{higher CTP-ordered kernels}
\rightarrow
P(\mathbf o|\mathbf s).
}
\]

This is a structural advance because it identifies **operator ordering itself** as a reconstruction coordinate.

The next calculation should search for a physically consistent null pair with

\[
\langle T\rangle_A=\langle T\rangle_B,
\qquad
N_A=N_B,
\qquad
D_A\neq D_B,
\]

or prove which additional conservation/energy constraints prevent such a pair in simple systems.