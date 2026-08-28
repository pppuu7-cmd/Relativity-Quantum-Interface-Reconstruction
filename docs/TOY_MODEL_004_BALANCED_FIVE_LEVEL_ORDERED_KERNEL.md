# RQIR Toy Model 004 — Balanced Five-Level Ordered-Kernel Null Construction

**Date:** 2026-08-29  
**Labels:** `NUM`, `DRV`, `OPEN`  
**Purpose:** search for a source algebra in which mean energy, the full one-point history of a chosen positive source observable, and its symmetrized two-point kernel are identical, while the commutator/response kernel differs.

## 1. Why this model was needed

Toy Model 003 produced the desired algebraic split

\[
\langle B(t)\rangle_+=\langle B(t)\rangle_-,\qquad
N_+(t,0)=N_-(t,0),\qquad
D_+(t,0)\neq D_-(t,0),
\]

but the two qubit states also had different mean generator energy. That contaminates a gravitational null test because gravity couples to the full stress-energy tensor.

Toy Model 004 asks whether the mean-energy obstruction is fundamental or only a feature of the minimal qubit realization.

The answer is: **it is not a general algebraic obstruction.** A five-level construction exists.

This does not yet provide a covariant stress-energy realization; it is an existence proof in finite-dimensional source algebra.

---

## 2. Search problem

Let `H` be a finite-dimensional Hamiltonian and `B` a Hermitian source observable. For two states

\[
\rho_+=\rho_0+\epsilon\Delta,
\qquad
\rho_-=\rho_0-\epsilon\Delta,
\]

we impose

\[
\operatorname{Tr}\Delta=0,
\]

\[
\operatorname{Tr}(\Delta H)=0,
\]

\[
\operatorname{Tr}[\Delta B(t)]=0
\qquad \forall t,
\]

and

\[
\operatorname{Tr}\left[
\Delta\,\frac{\{B(t),B(0)\}}2
\right]=0
\qquad \forall t.
\]

Because the one-point means are equal, the last condition is equivalent to equality of the centered symmetrized kernels

\[
N_+(t,0)=N_-(t,0).
\]

We then ask whether

\[
\operatorname{Tr}\left[
\Delta\,\frac{[B(t),B(0)]}{2i}
\right]
\neq0
\]

for some `t`.

This is a linear-algebra problem in the real vector space of Hermitian operators.

---

## 3. Exact finite-frequency treatment

Choose `H` diagonal with integer-spaced eigenvalues. Then

\[
B(t)=e^{iHt}Be^{-iHt}
\]

contains only a finite set of Fourier frequencies

\[
\omega=E_i-E_j.
\]

Therefore the conditions “for all `t`” can be enforced by requiring `Delta` to be Hilbert–Schmidt orthogonal to every independent sine/cosine Fourier coefficient of

\[
B(t)
\]

and

\[
S(t)=\frac12\{B(t),B(0)\}.
\]

The commutator sector is

\[
C(t)=\frac1{2i}[B(t),B(0)].
\]

A solution exists when at least one Fourier component of `C(t)` has a nonzero projection onto the nullspace of all equality constraints.

---

## 4. Five-level witness

A reproducible numerical search found a witness for `d=5`.

After harmless identity shifts that make both operators positive, use

\[
\boxed{
H=\operatorname{diag}(1,2,3,5,6)
}
\]

in arbitrary energy units.

A positive Hermitian observable `B` is

\[
B=\begin{pmatrix}
6.07786 & -0.36396+0.66835i & 0.30512-0.75309i & 0.83925-0.19901i & 0.56714-1.08355i\\
-0.36396-0.66835i & 3.93927 & -0.60051+0.41504i & -0.12986-0.77610i & 0.28682-0.21720i\\
0.30512+0.75309i & -0.60051-0.41504i & 6.74874 & 0.83720-0.42462i & 0.57021+0.42211i\\
0.83925+0.19901i & -0.12986+0.77610i & 0.83720+0.42462i & 2.79450 & -0.83878-1.31103i\\
0.56714+1.08355i & 0.28682+0.21720i & 0.57021-0.42211i & -0.83878+1.31103i & 3.85258
\end{pmatrix}.
\]

Its numerical eigenvalues are approximately

\[
(1.00000,\;3.77571,\;4.35311,\;6.25704,\;8.02708),
\]

so `B` is positive definite.

The traceless Hermitian null direction, normalized to operator norm 1, is

\[
\Delta=\begin{pmatrix}
-0.39925 & 0.38669+0.10561i & -0.27742-0.17049i & 0.01915+0.20133i & 0\\
0.38669-0.10561i & 0.20218 & 0.05500-0.09611i & 0.25586-0.27706i & -0.23675-0.42310i\\
-0.27742+0.17049i & 0.05500+0.09611i & 0.35046 & 0.08418+0.26899i & -0.00925-0.41819i\\
0.01915-0.20133i & 0.25586+0.27706i & 0.08418-0.26899i & 0.13616 & 0.09225-0.16815i\\
0 & -0.23675+0.42310i & -0.00925+0.41819i & 0.09225+0.16815i & -0.28955
\end{pmatrix}.
\]

Take

\[
\rho_0=I/5,
\qquad
\epsilon=0.1,
\]

and define

\[
\boxed{
\rho_\pm=I/5\pm0.1\Delta.
}
\]

The numerical eigenvalues are

\[
\operatorname{eig}(\rho_+)
\approx(0.11383,0.13398,0.20514,0.24704,0.30000),
\]

\[
\operatorname{eig}(\rho_-)
\approx(0.10000,0.15296,0.19486,0.26602,0.28617),
\]

so both density matrices are positive.

---

## 5. Equal mean energy

The construction satisfies

\[
\operatorname{Tr}(\Delta H)=0
\]

to numerical precision. Therefore

\[
\boxed{
\langle H\rangle_+=\langle H\rangle_-=3.4
}
\]

in the chosen units.

This removes the specific mean-generator-energy obstruction of Toy Model 003.

---

## 6. Equal full one-point history of `B`

For

\[
B(t)=e^{iHt}Be^{-iHt},
\]

the Fourier-constraint construction enforces

\[
\boxed{
\langle B(t)\rangle_+=\langle B(t)\rangle_-
\qquad\forall t.
}
\]

At `t=0`,

\[
\langle B\rangle_+=\langle B\rangle_-
\approx4.682588.
\]

A dense independent numerical check over one full `2pi` period gave a maximum absolute mean difference below approximately

\[
3\times10^{-15}.
\]

---

## 7. Equal symmetrized kernel

Define centered operators separately for each state,

\[
\delta B_\pm(t)=B(t)-\langle B(t)\rangle_\pm I.
\]

Then

\[
N_\pm(t,0)
=\frac12\operatorname{Tr}
\left[
\rho_\pm\{\delta B_\pm(t),\delta B_\pm(0)\}
\right].
\]

The construction enforces

\[
\boxed{
N_+(t,0)=N_-(t,0)
\qquad\forall t.
}
\]

A dense numerical check over one period gave a maximum absolute difference below approximately

\[
5\times10^{-15}.
\]

---

## 8. Different commutator kernel

Define

\[
D_\pm(t,0)
=\frac{1}{2i}
\operatorname{Tr}
\left[
\rho_\pm[\delta B_\pm(t),\delta B_\pm(0)]
\right].
\]

The two states have a nonzero response split. In the dense check, near

\[
t\approx3.26726,
\]

we find

\[
D_+\approx+0.535468,
\qquad
D_-\approx-0.535468,
\]

while at the same time

\[
N_+\approx N_-\approx0.803678.
\]

Thus

\[
\boxed{
\langle H\rangle_+=\langle H\rangle_-,
\quad
\langle B(t)\rangle_+=\langle B(t)\rangle_-,
\quad
N_+(t,0)=N_-(t,0),
\quad
D_+(t,0)\neq D_-(t,0).
}
\]

This is the first balanced ordered-kernel split found in RQIR.

---

## 9. What this does and does not prove

### What is established in the finite-dimensional algebra

The Toy Model 003 energy obstruction is not universal. Equal mean energy plus equal source mean history plus equal symmetrized two-point kernel **does not mathematically determine** the antisymmetric/retarded sector.

Therefore

\[
\boxed{
(\langle H\rangle,\langle B\rangle,N)
\not\Rightarrow D.
}
\]

This strengthens the need for the ordered-kernel hierarchy.

### What is not established

`B` has not yet been embedded as a covariantly conserved local/smeared stress-energy observable of a complete relativistic matter + apparatus system.

Equality of one global mean Hamiltonian does not imply

\[
\langle T_{\mu\nu}(x)\rangle_+
=\langle T_{\mu\nu}(x)\rangle_-
\]

pointwise or relationally.

Therefore Toy Model 004 is **not yet a gravitational experimental proposal** and not a proof of quantum geometry.

---

## 10. Dimension-search observation

In the numerical search performed during this iteration:

- `d=2`: no witness found in 500 random trials;
- `d=3`: no witness found in 1500 random trials;
- `d=4`: no witness found in 5000 random trials;
- `d=5`: a witness appeared within the first few trials for one tested seed.

For the random `d<=4` cases the equality-constraint operators numerically spanned the full Hermitian operator space, leaving no null direction for an independent commutator component.

### Important status

This is a **numerical observation only**.

RQIR does **not** yet claim that dimension five is minimal. A proof would require characterizing the rank of the operator-span constraints for all admissible `H,B`, including degeneracies and structured/sparse cases.

Working conjecture:

> `CONJ-RQIR-001`: under generic finite-dimensional conditions with equality of energy, full one-point `B(t)` history and reference-time symmetrized kernel `N(t,0)`, an independent response direction may require Hilbert-space dimension at least five.

This conjecture is deliberately weak and is a target for proof or counterexample.

---

## 11. Why positivity shifts are legitimate here

Adding identity pieces

\[
H\to H+c_HI,
\qquad
B\to B+c_BI
\]

does not change Heisenberg dynamics generated by energy gaps, centered fluctuations, or commutators. It changes only common offsets.

Therefore the search witness can be shifted so that both `H` and `B` are positive without altering the ordered-kernel split.

This does not by itself make `B` a physical mass density; it only removes an unnecessary algebraic objection.

---

## 12. Consistency gates

- `G0 dimensions`: PASS after assigning units to `H`, `B`, and time.
- `G1 gauge/relational`: OPEN; no spacetime embedding yet.
- `G2 conservation/Bianchi`: OPEN; this is the main remaining obstacle.
- `G3 positivity/unitarity`: PASS for `rho_±`, positive `H/B`, and unitary evolution.
- `G3a covariance positivity`: compatible numerically; full smeared-kernel analysis remains OPEN.
- `G3b spectral identities`: PASS within the finite-dimensional quantum model.
- `G4 causality`: not yet a spacetime model.
- `G5 classical limit`: OPEN.
- `G6 gravity-off`: not yet coupled to gravity.
- `G8 Newtonian limit`: not yet assigned.
- `G9 EFT`: OPEN.
- `G10 smearing/renormalization`: OPEN.
- `G11 known precision tests`: not applicable yet.
- `G12 degeneracy audit`: IMPORTANT — `D` difference alone still does not imply quantum gravitational degrees of freedom.
- `G13 measurability`: OPEN.

---

## 13. Next target

The next step is no longer to search blindly for algebraic examples. It is to **embed this structure into a physically admissible source**.

Priority questions:

1. Can a five-level atom/molecule/oscillator truncation realize analogous operator spans for a smeared component of `T_{mu nu}`?
2. Can the two states be chosen so that the **full relevant mean stress-energy**, not only global energy, is matched?
3. Can the equality be extended from `N(t,0)` to the experimentally required two-time region `N(t,t')`?
4. What probe observable isolates `chi^R` after `N` and the mean are calibrated?
5. Can a classical/stochastic gravitational interface reproduce the same joint `(N,chi^R)` relation?

The first successful covariant/smeared embedding would become the first genuinely strong RQIR coherence-sensitive null construction.