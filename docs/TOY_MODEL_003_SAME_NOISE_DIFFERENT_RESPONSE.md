# RQIR Toy Model 003 — Same Mean and Noise, Different Ordered Response

**Date:** 2026-08-29  
**Labels:** `DRV`, `NEG`, `OPEN`  
**Purpose:** determine whether operator ordering can distinguish source preparations even when their one-point signal and symmetrized two-point noise are identical.

## 1. Executive result

A minimal two-level source provides an exact algebraic construction with

\[
\boxed{
\langle B(t)\rangle_+=\langle B(t)\rangle_-,
\qquad
N_+(t,0)=N_-(t,0),
\qquad
D_+(t,0)=-D_-(t,0)\neq0.
}
\]

However, the two states have different expectation values of the Hamiltonian that generates the required dynamics. Therefore the construction is **not yet a clean full-stress-energy null pair** for gravity.

This gives both a positive structural result and a negative consistency result:

- `DRV`: equal mean + equal symmetrized noise does not mathematically force equal commutator response;
- `NEG`: the simplest qubit implementation fails the exact `same full T_{mu nu}` requirement because its mean energy differs.

---

## 2. Two-mode qubit

Use one quantum in two localized modes:

\[
|L\rangle,\qquad |R\rangle.
\]

Define Pauli operators in this basis with

\[
\sigma_z=|L\rangle\langle L|-|R\rangle\langle R|,
\]

and occupation

\[
\hat n_L=\frac{I+\sigma_z}{2},
\qquad
\hat n_R=\frac{I-\sigma_z}{2}.
\]

Choose the tunnelling Hamiltonian

\[
\boxed{
H=\frac{\hbar\Omega}{2}\sigma_x.
}
\]

The two coherent energy eigenstates are

\[
|+x\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2},
\qquad
|-x\rangle=\frac{|L\rangle-|R\rangle}{\sqrt2}.
\]

For compactness let

\[
\rho_s=\frac12(I+s\sigma_x),
\qquad s=+1,-1,
\]

and optionally `s=0` denote the maximally incoherent mixture in this two-state sector.

---

## 3. Heisenberg evolution of density

Under `H`,

\[
\sigma_z(t)
=e^{iHt/\hbar}\sigma_z e^{-iHt/\hbar}
=\sigma_z\cos\Omega t+\sigma_y\sin\Omega t.
\]

Therefore

\[
\hat n_L(t)
=\frac12\left[I+\sigma_z\cos\Omega t+\sigma_y\sin\Omega t\right].
\]

Because

\[
\langle\sigma_z\rangle_s
=\langle\sigma_y\rangle_s=0,
\]

we obtain

\[
\boxed{
\langle n_L(t)\rangle_s=\frac12
}
\]

for `s=+1,-1,0` at every time.

Thus the complete one-point density history is identical in this reduced observable.

---

## 4. Symmetrized noise is also identical

Define

\[
\delta n_L(t)=n_L(t)-\frac12=\frac12\sigma_z(t).
\]

The symmetrized kernel is

\[
N_s(t,0)
\equiv
\frac12\langle
\{\delta n_L(t),\delta n_L(0)\}
\rangle_s.
\]

Using

\[
\{\sigma_z(t),\sigma_z\}=2I\cos\Omega t,
\]

we get

\[
\boxed{
N_s(t,0)=\frac14\cos\Omega t
}
\]

independent of `s`.

Hence

\[
N_+=N_-=N_{\rm mix}.
\]

This is exactly the desired equality in the second-order symmetrized sector.

---

## 5. Antisymmetric response differs

The commutator is

\[
[\sigma_z(t),\sigma_z]
=2i\sigma_x\sin\Omega t.
\]

Therefore

\[
[\delta n_L(t),\delta n_L(0)]
=\frac{i}{2}\sigma_x\sin\Omega t.
\]

Define

\[
D_s(t,0)
=\frac{1}{2i}
\langle[\delta n_L(t),\delta n_L(0)]\rangle_s.
\]

Since

\[
\langle\sigma_x\rangle_s=s,
\]

we obtain

\[
\boxed{
D_s(t,0)=\frac{s}{4}\sin\Omega t.
}
\]

Thus

\[
\boxed{
D_+(t,0)=-D_-(t,0),
\qquad
D_{\rm mix}(t,0)=0.
}
\]

With the convention

\[
\chi_s^R(t,0)
=\frac{i}{\hbar}\theta(t)
\langle[n_L(t),n_L(0)]\rangle_s,
\]

we find

\[
\boxed{
\chi_s^R(t,0)
=-\frac{s}{2\hbar}\theta(t)\sin\Omega t.
}
\]

The overall sign changes if the opposite Kubo convention is used; the physical state dependence does not.

---

## 6. Weak-field potential proxy

At a fixed probe point define

\[
\hat\Phi(t)
=-Gm\left(
\frac{n_L(t)}{r_L}
+\frac{n_R(t)}{r_R}
\right).
\]

Let

\[
\Delta u\equiv\frac1{r_L}-\frac1{r_R}.
\]

The fluctuating part is

\[
\delta\Phi(t)
=-Gm\,\Delta u\,\delta n_L(t).
\]

Therefore

\[
\boxed{
N_{\Phi,s}(t,0)
=\frac{G^2m^2(\Delta u)^2}{4}\cos\Omega t
}
\]

for every `s`, while

\[
\boxed{
D_{\Phi,s}(t,0)
=\frac{s\,G^2m^2(\Delta u)^2}{4}\sin\Omega t.
}
\]

Again, `Phi` here is a source-dependent Newtonian proxy. This calculation does **not** assume that the gravitational field itself is an operator.

---

## 7. Why this is structurally important

The source preparations satisfy, in the reduced density algebra,

\[
\boxed{
\langle n(t)\rangle_+=\langle n(t)\rangle_-,
\qquad
N_+=N_-,
\qquad
D_+\neq D_-.
}
\]

Therefore the ordered-kernel coordinate `D` contains information that cannot be reconstructed from the one-point signal plus the symmetrized noise alone.

This proves the mathematical usefulness of the RQIR hierarchy

\[
\langle T\rangle\rightarrow(N,D)\rightarrow\cdots.
\]

---

## 8. Full-energy obstruction

The same Hamiltonian gives

\[
\langle H\rangle_s
=\frac{\hbar\Omega}{2}\langle\sigma_x\rangle_s
=\boxed{\frac{s\hbar\Omega}{2}}.
\]

Thus

\[
\langle H\rangle_+\neq\langle H\rangle_-.
\]

Gravity couples to the full stress-energy tensor, not only to the rest-mass occupation operator. In a consistent relativistic embedding, the energy associated with the tunnelling/internal dynamics must be included in `T_00` together with the apparatus that generates or confines the modes.

Consequently the pair is **not** an exact null pair satisfying

\[
\langle T_{\mu\nu}\rangle_+
=\langle T_{\mu\nu}\rangle_-
\]

unless an explicit compensating construction is supplied and checked pointwise/relationally.

### RQIR-NG-002 — Minimal response-split energy obstruction

> In the minimal qubit realization with `H proportional sigma_x` and density contrast `B proportional sigma_z`, the same coherence component `sigma_x` that controls the commutator-response difference also controls the mean generator energy. Hence a response split is accompanied by a mean-energy split.

This is a theorem only for this specified minimal construction, not a universal no-go.

---

## 9. Why “the energy difference is tiny” is not enough

For a macroscopic mass one may have

\[
\hbar\Omega\ll mc^2.
\]

That makes the contamination parametrically small, but RQIR's strongest null tests aim for equality of the controlled baseline quantities, not merely numerical smallness.

A claimed coherence-sensitive gravitational residual could otherwise be attributed to the ordinary gravitational effect of the differing energy.

Hence an approximate experiment may use a small parameter, but the theory document must keep the contamination term explicit.

---

## 10. Candidate escape routes

### A. Larger Hilbert space with energy compensation

Add auxiliary degrees of freedom arranged so that the complete source preparations have the same total and local mean stress-energy while retaining a different ordered kernel in the target density sector.

Requirement:

\[
\Delta\langle T_{\mu\nu}(x)\rangle=0
\]

for the full source + control apparatus to the accuracy claimed.

### B. Degenerate dynamical subspaces

Search for systems in which distinct coherent states have equal energy but nontrivial ordered stress-tensor response. Exact degeneracy alone freezes dynamics inside the subspace, so additional operator structure is needed.

### C. Multi-frequency/multi-level systems

Use several transitions so equal-energy and equal-noise constraints can be satisfied while antisymmetric spectral weights differ.

### D. Driven protocol with explicit work accounting

Use an external drive to generate the noncommuting dynamics, but include the drive and exchanged work in the stress-energy bookkeeping. The correct null pair is then defined for the entire closed preparation + source + drive system.

---

## 11. Interface interpretation

Even if a clean pair with `same mean, same N, different D` is constructed, observing a response difference would still not automatically prove quantum geometry.

- quantum matter already has nonzero commutators;
- stochastic semiclassical gravity contains dissipation/response structures inherited from quantum matter;
- classical dynamical mediators can have causal response functions;
- classical gravity + full QFT matter can produce effects previously thought to require quantum gravitational communication.

Therefore the required discriminator is a **cross-kernel relation or multi-channel fingerprint**, not `D != 0` alone.

---

## 12. Consistency gates

- `G0 dimensions`: PASS.
- `G1 gauge/relational`: OPEN; reduced Newtonian model only.
- `G2 conservation/Bianchi`: FAIL/OPEN for use as a full gravity null pair because full stress-energy of the mode Hamiltonian/control system is omitted.
- `G3 unitarity`: PASS for the qubit dynamics.
- `G4 causality`: OPEN for any proposed gravitational readout; source algebra itself is ordinary unitary dynamics.
- `G5 classical limit`: OPEN.
- `G6 G→0`: potential-proxy differences vanish from gravitational observables; PASS.
- `G8 Newtonian`: explicit weak-field source proxy only.
- `G9 EFT`: OPEN.
- `G10 smearing`: finite wavefunctions required.
- `G12 degeneracy audit`: IMPORTANT NEGATIVE RESULT — mean energy differs.
- `G13 measurability`: OPEN.

---

## 13. Result and next step

The ordered-kernel split is algebraically real:

\[
\boxed{
\text{same mean}+\text{same symmetrized noise}
\centernot\Rightarrow
\text{same quantum response}.
}
\]

But the minimal gravitational implementation is not yet clean because

\[
\boxed{
\Delta D\neq0
\quad\text{comes with}\quad
\Delta\langle H\rangle\neq0.
}
\]

The next target is therefore precise:

> Construct or rule out a **balanced multi-level source** satisfying equal full mean stress-energy and equal relevant noise kernel while retaining a different ordered/retarded kernel, with the control apparatus included in the accounting.

That is the first candidate `strong RQIR coherence null pair`.