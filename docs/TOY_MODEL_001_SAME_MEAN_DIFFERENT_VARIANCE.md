# RQIR Toy Model 001 — Same Mean Mass, Different Source Fluctuations

**Date:** 2026-08-29  
**Labels:** `DEF`, `DRV`, `OPEN`  
**Purpose:** construct the first explicit cross-channel null test for Q2/Q3/Q5.

## 1. Question

Can two source states have the same mean mass distribution — and therefore the same leading semiclassical mean-field geometry — while having different stress/mass-density fluctuations that a fluctuation-sensitive gravitational interface could distinguish?

Yes, in a simple two-mode model.

This does **not** yet demonstrate new physics. It constructs a controlled discriminator.

## 2. Two localized source modes

Take two well-separated localized modes `L` and `R` with occupation operators

\[
\hat n_L,\qquad \hat n_R.
\]

Each quantum has rest mass \(m\). In the pointlike weak-field approximation define discrete mass operators

\[
\hat\mu_L=m\hat n_L,\qquad
\hat\mu_R=m\hat n_R.
\]

We compare two states with total occupation number 2.

### State A — number-fluctuating state

\[
|A\rangle=\frac{|2,0\rangle+|0,2\rangle}{\sqrt2}.
\]

### State B — number-balanced state

\[
|B\rangle=|1,1\rangle.
\]

The mode wavefunctions are assumed sufficiently separated that overlap corrections can initially be neglected.

## 3. Equal one-point mass distributions

For state A,

\[
\langle \hat n_L\rangle_A
=\langle \hat n_R\rangle_A=1.
\]

For state B,

\[
\langle \hat n_L\rangle_B
=\langle \hat n_R\rangle_B=1.
\]

Therefore

\[
\boxed{
\langle\hat\mu_i\rangle_A
=\langle\hat\mu_i\rangle_B=m,
\qquad i=L,R.
}
\]

A gravitational law depending only on the one-point mean mass density predicts the same leading static field for A and B.

## 4. Different second moments

For A,

\[
\langle \hat n_L^2\rangle_A
=\langle \hat n_R^2\rangle_A=2,
\]

so

\[
\operatorname{Var}_A(n_L)=
\operatorname{Var}_A(n_R)=1.
\]

Also

\[
\langle \hat n_L\hat n_R\rangle_A=0,
\]

hence

\[
\operatorname{Cov}_A(n_L,n_R)=-1.
\]

Thus the occupation covariance matrix is

\[
\boxed{
\Sigma_A^{(n)}=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
}
\]

For B,

\[
\hat n_L|B\rangle=|B\rangle,
\qquad
\hat n_R|B\rangle=|B\rangle,
\]

and therefore

\[
\boxed{
\Sigma_B^{(n)}=0.
}
\]

For the mass variables,

\[
\Sigma_A^{(\mu)}=m^2\Sigma_A^{(n)},
\qquad
\Sigma_B^{(\mu)}=0.
\]

So A and B have identical one-point mass density but distinct second-order source statistics.

## 5. Newtonian weak-field probe

Place a probe at position \(\mathbf x\), with distances

\[
r_L=|\mathbf x-\mathbf x_L|,
\qquad
r_R=|\mathbf x-\mathbf x_R|.
\]

Promote the source-dependent Newtonian potential formally to

\[
\hat\Phi(\mathbf x)
=-Gm\left(\frac{\hat n_L}{r_L}+\frac{\hat n_R}{r_R}\right).
\]

This operator is used here only to compute source moments. It does **not** assume that the gravitational field itself is quantum.

The mean is identical:

\[
\boxed{
\langle\hat\Phi\rangle_A
=\langle\hat\Phi\rangle_B
=-Gm\left(\frac1{r_L}+\frac1{r_R}\right).
}
\]

But for A,

\[
\operatorname{Var}_A(\Phi)
=G^2m^2
\left(\frac1{r_L}-\frac1{r_R}\right)^2,
\]

whereas for B,

\[
\boxed{
\operatorname{Var}_B(\Phi)=0
}
\]

within this idealized source-statistics model.

Therefore

\[
\boxed{
\Delta\operatorname{Var}(\Phi)
=G^2m^2
\left(\frac1{r_L}-\frac1{r_R}\right)^2.
}
\]

The difference vanishes at geometrically symmetric probe locations where \(r_L=r_R\), giving an immediate experimental-design constraint.

## 6. Interferometric phase proxy

For a nonrelativistic probe of mass \(M\) interacting for time \(\tau\), a potential contribution to phase scales as

\[
\phi\sim -\frac{M\tau}{\hbar}\Phi.
\]

Hence a fluctuation-sensitive realization would inherit the schematic source-induced phase variance

\[
\boxed{
\operatorname{Var}_A(\phi)
\sim
\left(\frac{GMm\tau}{\hbar}\right)^2
\left(\frac1{r_L}-\frac1{r_R}\right)^2,
}
\]

while the idealized B source contribution from occupation fluctuations is zero.

This expression is **not yet an experimental prediction**. A detector model, time-dependent Green function, quantum backreaction prescription, environmental noise and proper operator ordering must be specified before it becomes one.

## 7. What different interface classes do with this construction

### Pure expectation-value semiclassical mean field

If the weak-field gravitational potential is sourced only by

\[
\langle\hat\mu\rangle,
\]

then A and B generate the same leading static mean field:

\[
\Phi_A^{\rm mean}=\Phi_B^{\rm mean}.
\]

No distinction follows **solely from the different second moments** unless extra stochastic or state-update structure is added.

### Stochastic/fluctuation-sensitive interface

If source fluctuations feed into gravitational fluctuations through a noise kernel or analogous covariance-transfer law, A and B can differ despite identical one-point mass density.

### Quantized/hybrid interfaces

They may also distinguish A and B, but the form, magnitude and ordering of the effect must be derived model by model. RQIR will compare these predictions in a common observable basis rather than assuming that any nonzero difference proves metric quantization.

## 8. Critical caveat: this is not yet a coherence witness

The pure superposition

\[
\frac{|2,0\rangle+|0,2\rangle}{\sqrt2}
\]

and the incoherent mixture

\[
\rho_{\rm mix}=\frac12|2,0\rangle\langle2,0|
+\frac12|0,2\rangle\langle0,2|
\]

have the same statistics for observables built only from the diagonal occupation operators \(n_L,n_R\) in the zero-overlap approximation.

Therefore Toy Model 001 tests **sensitivity beyond the mean**, but by itself does not establish sensitivity to quantum coherence.

This distinction is essential and is deliberately preserved rather than hidden.

## 9. Next null test

Construct `Toy Model 002` with two preparations that match not only the one-point mass density but also the relevant classical stochastic density moments, while differing in an explicitly coherence-sensitive quantity. The goal is to isolate interface sensitivity to off-diagonal quantum information rather than merely classical source variance.

Candidate routes:

1. finite-overlap localized modes with coherence-dependent stress-density matrix elements;
2. controlled recombination/interference before gravitational readout;
3. ancilla-assisted relational correlators;
4. time-separated unequal-time correlators that retain phase information;
5. joint source–probe observables inaccessible to a classical mixture with the same density statistics.

## 10. Consistency gates for Toy Model 001

- `G0 dimensional consistency`: PASS for the displayed weak-field scalings.
- `G5 ħ→0`: phase expression requires care because interferometric phase itself scales as \(1/\hbar\); the observable classical limit must be formulated at probability level. OPEN.
- `G6 G→0`: PASS, all gravitational differences vanish.
- `G7 flat/gravity-off`: PASS in the same sense.
- `G8 Newtonian limit`: construction is explicitly Newtonian/weak-field.
- `G10 smearing`: point-source approximation must be replaced by finite wavefunctions before precision work. OPEN.
- `G12 degeneracy audit`: classical statistical mass fluctuations can mimic second-moment effects; this toy model therefore cannot identify quantum coherence. IDENTIFIED.
- `G13 measurability`: OPEN.

## 11. Result

The first RQIR discriminator exists already at the level of source moments:

\[
\boxed{
\langle\mu\rangle_A=\langle\mu\rangle_B,
\qquad
\operatorname{Cov}_A(\mu)\neq\operatorname{Cov}_B(\mu).
}
\]

This makes Q2–Q3–Q5 a concrete inverse problem: determine whether gravitational observables depend only on source means or also on higher source statistics, and if so, through what transfer law.