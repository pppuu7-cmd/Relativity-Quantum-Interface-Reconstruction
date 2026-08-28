# RQIR Toy Model 002 — Phase-Blindness No-Go for Static Density Coupling

**Date:** 2026-08-29  
**Labels:** `DEF`, `DRV`, `NEG`, `OPEN`  
**Purpose:** test whether a static gravitational observable can distinguish quantum coherence when all diagonal mass-density statistics are identical.

## 1. Target

Toy Model 001 showed that two source states can share the same mean mass density while differing in source variance. That construction does **not** isolate quantum coherence, because a classical mixture can reproduce the same diagonal number statistics.

Toy Model 002 asks a stricter question:

> Can two source states with exactly the same complete diagonal mass-density statistics but different relative quantum phase be distinguished by a static gravitational coupling that is itself diagonal in the mass-density basis?

For the idealized two-mode model below, the answer is **no**.

This is a useful no-go result, not a failure of the programme.

---

## 2. Exact phase pair

Take two orthogonal localized modes `L` and `R`, with fixed total occupation number 2. Define

\[
|\psi_+\rangle=\frac{|2,0\rangle+|0,2\rangle}{\sqrt2},
\qquad
|\psi_-\rangle=\frac{|2,0\rangle-|0,2\rangle}{\sqrt2}.
\]

Also define the incoherent mixture

\[
\rho_{\rm mix}=\frac12|2,0\rangle\langle2,0|
+\frac12|0,2\rangle\langle0,2|.
\]

The states \(|\psi_+\rangle\) and \(|\psi_-\rangle\) differ only by an off-diagonal relative phase in the localized occupation basis.

Their density matrices are

\[
\rho_\pm=\frac12\Big(
|20\rangle\langle20|+|02\rangle\langle02|
\pm |20\rangle\langle02|
\pm |02\rangle\langle20|
\Big).
\]

Hence

\[
\rho_\pm-\rho_{\rm mix}
=\pm\frac12\Big(|20\rangle\langle02|+|02\rangle\langle20|\Big).
\]

---

## 3. Complete diagonal-statistics equality

Let

\[
F=F(\hat n_L,\hat n_R)
\]

be any operator that is diagonal in the joint occupation basis. Since

\[
\langle20|F|02\rangle=\langle02|F|20\rangle=0,
\]

we have the exact identity

\[
\boxed{
\operatorname{Tr}(\rho_+F)
=\operatorname{Tr}(\rho_-F)
=\operatorname{Tr}(\rho_{\rm mix}F)
}
\]

for **every** such diagonal function `F`.

Therefore the three preparations share not only the same mean density and variance but the entire joint probability distribution of the diagonal occupation variables:

\[
P(n_L,n_R)
=\frac12\,\delta_{(n_L,n_R),(2,0)}
+\frac12\,\delta_{(n_L,n_R),(0,2)}.
\]

Equivalently, all diagonal moments coincide:

\[
\boxed{
\langle n_L^a n_R^b\rangle_+
=\langle n_L^a n_R^b\rangle_-
=\langle n_L^a n_R^b\rangle_{\rm mix}
}
\]

for all non-negative integers \(a,b\).

This is stronger than Toy Model 001.

---

## 4. Static Newtonian field is exactly phase-blind

For non-overlapping localized modes, write the mass-density operator schematically as

\[
\hat\mu(\mathbf x)
=m\left[
|u_L(\mathbf x)|^2\hat n_L
+|u_R(\mathbf x)|^2\hat n_R
\right],
\]

neglecting mode-overlap terms.

A static Newtonian potential operator proxy at a probe point is then

\[
\hat\Phi(\mathbf x)
=-Gm\left(
\frac{\hat n_L}{r_L}
+\frac{\hat n_R}{r_R}
\right),
\]

which is diagonal in the same occupation basis.

Therefore every moment of this static density-derived potential is identical for the three source preparations:

\[
\boxed{
\langle \Phi^k\rangle_+
=\langle \Phi^k\rangle_-
=\langle \Phi^k\rangle_{\rm mix}
}
\]

for all positive integers \(k\), within the idealized model.

Thus neither the mean field, its diagonal-source variance, nor any higher static moment can reveal the relative phase.

---

## 5. General phase-blindness theorem in the toy domain

Let the source Hilbert space have a preferred orthogonal mass-configuration basis \(\{|\alpha\rangle\}\), and let an interface observable or source coupling have the form

\[
\hat O=\sum_\alpha O_\alpha |\alpha\rangle\langle\alpha|.
\]

If two source states \(\rho_1,\rho_2\) have identical diagonals in that basis,

\[
\langle\alpha|\rho_1|\alpha\rangle
=\langle\alpha|\rho_2|\alpha\rangle
\quad\forall\alpha,
\]

then

\[
\boxed{
\operatorname{Tr}(\rho_1\hat O)
=\operatorname{Tr}(\rho_2\hat O)
}
\]

regardless of their off-diagonal coherences.

The same statement extends to any collection of mutually commuting observables diagonal in that basis and therefore to their complete classical probability distribution.

### RQIR-NG-001 — Static density phase blindness

> **Within a non-overlap model whose gravitational source rule and readout depend only on mutually commuting operators diagonal in the mass-configuration basis, relative quantum phase between orthogonal mass branches is operationally invisible to static gravitational observables.**

This result is conditional on the stated domain. It is not a theorem about all possible gravity–quantum interfaces.

---

## 6. Probe-only extension

Suppose a probe couples through a density-diagonal controlled interaction

\[
\hat U
=\sum_\alpha |\alpha\rangle\langle\alpha|\otimes \hat U_\alpha.
\]

For a source state

\[
\rho_S=\sum_{\alpha\beta}\rho_{\alpha\beta}|\alpha\rangle\langle\beta|
\]

and initial probe state \(\rho_P\), the reduced probe state after the interaction is

\[
\rho'_P
=\operatorname{Tr}_S\left[
\hat U(\rho_S\otimes\rho_P)\hat U^\dagger
\right]
=\sum_\alpha \rho_{\alpha\alpha}
\hat U_\alpha\rho_P\hat U_\alpha^\dagger.
\]

All source off-diagonal terms disappear under the source trace because \(\langle\beta|\alpha\rangle=\delta_{\alpha\beta}\).

Hence

\[
\boxed{
\rho'_{P,+}=\rho'_{P,-}=\rho'_{P,\rm mix}
}
\]

for the phase pair above.

This is stronger than equality of the mean force: **no probe-only measurement after such an ideal controlled interaction can distinguish the source phase.**

---

## 7. What can evade the no-go?

At least one assumption must be broken.

### Route A — finite spatial overlap

If the localized mode functions overlap, local stress/mass-density operators acquire cross terms such as

\[
u_L^*(\mathbf x)u_R(\mathbf x)\,
\hat a_L^\dagger\hat a_R+\text{h.c.},
\]

which are phase-sensitive.

But then the ordinary local matter density may already differ between coherent and incoherent preparations. A gravitational difference would not by itself show that gravity accesses uniquely quantum information.

### Route B — noncommuting/unequal-time source observables

A time-dependent source can have

\[
[\hat T(x),\hat T(y)]\neq0.
\]

Then ordered correlators carry information absent from a classical joint probability distribution of commuting density variables.

This is the preferred next route.

### Route C — joint source–probe measurement

The joint state can retain source coherence even when the reduced probe state is phase-blind. Recombining or measuring the source in a non-density basis may reveal phase-dependent source–probe correlations.

However, the gravity-off control must be subtracted because the source coherence is directly measurable even without gravity.

### Route D — genuinely non-diagonal gravitational coupling

A candidate interface may couple to operators not diagonal in the mass-configuration basis. Such a proposal must be derived consistently from stress-energy, covariance, conservation and the low-energy limit rather than inserted ad hoc.

---

## 8. Why recombination alone is not a gravity coherence witness

A tempting procedure is:

1. prepare \(|\psi_+\rangle\) or \(|\psi_-\rangle\);
2. recombine the branches nongravitationally;
3. observe different output populations;
4. let gravity read the resulting density difference.

This certainly converts phase into population, but it does **not** demonstrate that gravity itself was sensitive to off-diagonal coherence. The nongravitational recombiner performed the coherence-to-density conversion first.

RQIR therefore distinguishes:

\[
\text{gravity reads a coherence-converted classical variable}
\]

from

\[
\text{gravity directly accesses a noncommuting/coherence-sensitive source structure}.
\]

This distinction is mandatory under gate `G12`.

---

## 9. Connection to stochastic-gravity structure

Stochastic gravity already distinguishes different operator orderings at the level of stress-energy two-point functions. In particular, the standard noise kernel is built from the anticommutator of stress-energy fluctuations, while the influence-functional formulation also contains a dissipation/response kernel associated with the antisymmetric/commutator sector.

This motivates replacing the provisional single `C^(2)` object in RQIR by an **ordered-kernel decomposition**:

\[
N_{AB}(x,y)
\equiv \frac12\langle\{\delta\hat T_A(x),\delta\hat T_B(y)\}\rangle,
\]

\[
D_{AB}(x,y)
\equiv \frac{1}{2i}\langle[\delta\hat T_A(x),\delta\hat T_B(y)]\rangle,
\]

plus retarded response

\[
\chi^R_{AB}(x,y)
\equiv \frac{i}{\hbar}\theta(x^0-y^0)
\langle[\hat T_A(x),\hat T_B(y)]\rangle
\]

(up to sign convention).

`N` captures the symmetrized fluctuation sector; `D`/`chi^R` contains noncommuting response information. They must not be conflated.

---

## 10. Consistency gates

- `G0 dimensional consistency`: PASS for the discrete and Newtonian expressions.
- `G1 gauge/relational`: NOT APPLICABLE at the discrete Newtonian toy level; must be restored in relativistic extension.
- `G2 conservation/Bianchi`: OPEN; full stress-energy embedding is not yet supplied.
- `G3 positivity/unitarity`: PASS for the controlled-unitary derivation.
- `G4 no-signalling/causal`: OPEN beyond the static effective interaction approximation.
- `G5 hbar→0`: phase information becomes operational only through a quantum preparation/readout; classical-limit formulation remains OPEN.
- `G6 G→0`: the gravity-dependent probe interaction vanishes; PASS.
- `G7 flat/gravity-off`: PASS in the intended effective sense.
- `G8 Newtonian limit`: construction is explicitly Newtonian/weak-field.
- `G9 EFT power counting`: OPEN.
- `G10 smearing/renormalization`: ideal localized modes require finite wavepacket extension; OPEN.
- `G11 precision tests`: not yet a phenomenological prediction.
- `G12 degeneracy audit`: PASS for the central no-go; recombination loophole explicitly identified.
- `G13 measurability`: the no-go concerns measurability; evading routes remain OPEN.

---

## 11. Result

Toy Model 002 closes one tempting but invalid route:

\[
\boxed{
\text{same diagonal mass statistics}
+\text{different phase}
\not\Rightarrow
\text{different static gravitational observable}
}
\]

when the gravitational interface is diagonal in the same mass basis.

The correct next target is therefore not another static moment but the **ordered unequal-time sector**:

\[
\boxed{
\langle T\rangle,
\quad N=\tfrac12\langle\{\delta T,\delta T\}\rangle,
\quad D=\tfrac1{2i}\langle[\delta T,\delta T]\rangle,
\quad \text{higher ordered cumulants}.
}
\]

The next toy model should attempt to match the mean and `N` while changing `D`, and then determine which gravitational-interface classes can transmit that distinction to an operational probe without violating the full stress-energy and conservation constraints.