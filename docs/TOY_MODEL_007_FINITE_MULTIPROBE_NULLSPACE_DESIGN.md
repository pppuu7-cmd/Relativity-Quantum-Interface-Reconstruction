# RQIR Toy Model 007 — Finite Multiprobe Nullspace Design

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`  
**Purpose:** replace impossible complete-density matching by a declared finite gravitational calibration and test whether an ordered/retarded response direction survives after mean and noise controls.

## 1. Main result

Using the physical five-site Newtonian source of Toy 005, two probe locations and a finite set of calibration times can constrain the Hermitian state-difference space to **one dimension** while leaving a nonzero self-response direction of probe 0.

For the recorded design:

\[
\boxed{r_{obs}=24\quad\text{in}\quad d^2=25,}
\]

so

\[
\boxed{\dim\mathcal N_{obs}=1.}
\]

The normalized surviving response fraction is

\[
\boxed{\eta_R\approx0.458.}
\]

At the response time the two states have identical calibrated mean potential and identical calibrated symmetrized self-noise, while their commutator response is opposite:

\[
\boxed{
\langle B_0(t_R)\rangle_+=\langle B_0(t_R)\rangle_-,
}
\]

\[
\boxed{
N_{00,+}(t_R,0)=N_{00,-}(t_R,0),
}
\]

but

\[
\boxed{
D_{00,+}(t_R,0)\neq D_{00,-}(t_R,0).
}
\]

This upgrades the project from NP2 to a finite **NP3 proof-of-principle** under the explicitly declared calibration set.

It is not yet robust enough for phenomenology because the constraint matrix is poorly conditioned.

---

## 2. Source inherited from Toy 005

Use the same one-particle five-site source. In units where the nearest site to probe 0 is at one length unit, place the sites on a line at

\[
\boxed{
x_a\approx(5.53112,\;2.21089,\;1.44295,\;1.27948,\;1.00000).
}
\]

The site-basis Hamiltonian is

\[
H_{site}\approx
\begin{pmatrix}
3.32831&1.31670&0.98110&0.61320&1.18889\\
1.31670&1.86853&0.10773&0.49490&1.05759\\
0.98110&0.10773&3.61765&0.18506&-0.25465\\
0.61320&0.49490&0.18506&3.28024&0.45425\\
1.18889&1.05759&-0.25465&0.45425&3.90527
\end{pmatrix},
\]

with energy eigenvalues

\[
(1,2,3,4,6).
\]

This is a real coupled-mode / tight-binding source Hamiltonian.

---

## 3. Two Newtonian probes

Place probe 0 at

\[
y_0=0,
\]

and probe 1 at

\[
\boxed{y_1\approx-3.59553}
\]

in the same dimensionless length units.

For probe `k`, define the dimensionless Newtonian channel operator

\[
B_k=\sum_{a=1}^5\frac{1}{|x_a-y_k|}\,n_a.
\]

The physical potential is

\[
\Phi_k=-\frac{Gm}{L_0}B_k
\]

if `L0` is the physical length represented by one dimensionless unit.

Thus all source-side kernels below acquire the appropriate powers of `Gm/L0` when translated into physical potential units.

---

## 4. Declared calibration times

Use the dimensionless time set

\[
\boxed{
\mathcal T=
\{0,
3.07093,
3.58393,
3.73521,
4.18983,
4.89703,
5.65727\}.
}
\]

The target response time is included explicitly:

\[
\boxed{t_R=3.58393.}
\]

Including `t_R` in the mean calibration is essential: otherwise a response difference could be trivially contaminated by an uncalibrated mean-potential difference at the same time.

---

## 5. Equality-constraint set

Let

\[
\Delta=\rho_+-\rho_-.
\]

The calibration requires:

### Global controls

\[
\operatorname{Tr}\Delta=0,
\qquad
\operatorname{Tr}(\Delta H)=0.
\]

### Mean-potential controls

For both probes and all seven calibration times,

\[
\boxed{
\operatorname{Tr}[\Delta B_k(t)]=0,
\qquad k=0,1,
\quad t\in\mathcal T.
}
\]

This contributes 14 mean constraints before linear dependencies are removed.

### Mandatory target self-noise control

At the response time, require equality of the uncentered symmetrized self-product

\[
\operatorname{Tr}\left[
\Delta\frac{\{B_0(t_R),B_0(0)\}}2
\right]=0.
\]

Because the mean values at `t_R` and `0` are separately matched, this is equivalent to equality of the centered self-noise

\[
N_{00,+}(t_R,0)=N_{00,-}(t_R,0).
\]

### Additional greedy-selected symmetrized controls

The deterministic search selects seven additional independent symmetrized constraints:

\[
S_{01}(3.07093,0),
\]

\[
S_{11}(4.89703,0),
\]

\[
S_{10}(t_R,0),
\qquad
S_{01}(t_R,0),
\]

\[
S_{10}(3.73521,0),
\]

\[
S_{00}(5.65727,0),
\qquad
S_{01}(5.65727,0),
\]

where

\[
S_{kl}(t,0)=\frac12\{B_k(t),B_l(0)\}.
\]

Again, all associated means at `t` and `0` are separately calibrated, so equality of these uncentered symmetrized products implies equality of the corresponding centered auto/cross-noise entries.

---

## 6. Constraint rank

Vectorize Hermitian operators with the Hilbert–Schmidt inner product and form the equality matrix `A` whose rows are the calibration operators.

The recorded design gives

\[
\boxed{\operatorname{rank}A=24.}
\]

Since

\[
\dim\operatorname{Herm}(5)=25,
\]

the exact equality nullspace is one-dimensional:

\[
\boxed{\dim\ker A=1.}
\]

Thus ordinary state ambiguity has been reduced from a large subspace to one controlled Hermitian direction.

---

## 7. Surviving response fraction

Let the target response operator be

\[
C_R=
\frac{1}{2i}
[B_0(t_R),B_0(0)].
\]

Let `P_N` be the Hilbert–Schmidt projector onto the equality nullspace. Define

\[
\boxed{
\eta_R=\frac{\|P_N C_R\|_{HS}}{\|C_R\|_{HS}}.
}
\]

For this design,

\[
\boxed{\eta_R\approx0.45768.}
\]

Therefore nearly half of the operator-norm direction relevant to this chosen response remains independent of the 24-dimensional calibrated equality span.

This does **not** mean a 46% experimental signal. It is a dimensionless operator-space geometry measure only.

---

## 8. Explicit positive state pair

Normalize the one-dimensional null operator `Delta0` to unit operator norm and choose

\[
\rho_\pm=I/5\pm0.08\Delta_0.
\]

The resulting eigenvalues are approximately

\[
\operatorname{eig}(\rho_+)
\approx
(0.12000,0.17274,0.18974,0.24227,0.27524),
\]

\[
\operatorname{eig}(\rho_-)
\approx
(0.12476,0.15773,0.21026,0.22726,0.28000),
\]

so both are positive density matrices.

Direct numerical evaluation gives equality residuals below approximately

\[
3\times10^{-16}
\]

for all selected linear calibration constraints.

---

## 9. Target-time null and response split

At

\[
t_R\approx3.58393,
\]

probe 0 has exactly matched calibrated mean:

\[
\boxed{
\langle B_0(t_R)\rangle_+
=
\langle B_0(t_R)\rangle_-
\approx0.621539.
}
\]

The reference-time mean is also equal:

\[
\langle B_0(0)\rangle_+
=
\langle B_0(0)\rangle_-
\approx0.621539.
\]

The centered symmetrized self-noise matches:

\[
\boxed{
N_{00,+}(t_R,0)
=N_{00,-}(t_R,0)
\approx0.00944118.
}
\]

But the commutator response is opposite:

\[
\boxed{
D_{00,+}(t_R,0)
\approx-0.0105656,
\qquad
D_{00,-}(t_R,0)
\approx+0.0105656.
}
\]

Thus

\[
\boxed{
\Delta D_{00}(t_R,0)
\approx-0.0211313.
}
\]

Under the current RQIR retarded-response sign convention and `hbar=1`, this corresponds to an opposite retarded-response contribution proportional to `D`.

---

## 10. Why this is stronger than Toy 005

Toy 005 matched one complete single-probe mean history and one reference-time self-noise history.

Toy 007 instead calibrates:

- two independent Newtonian probe kernels;
- both probe means at seven explicit times;
- target self-noise at the response time;
- selected additional auto/cross-noise entries;
- total mean energy;
- trace/normalization.

The equality span reaches rank 24 of 25 rather than leaving a broad uncharacterized state space.

Therefore this is a finite NP3 construction rather than NP2.

---

## 11. Critical weakness: conditioning

Normalize every equality row to unit Hilbert–Schmidt norm and examine the nonzero singular values of the calibration matrix.

For the recorded design,

\[
\boxed{s_{min}\approx1.46\times10^{-3},}
\]

with condition number approximately

\[
\boxed{\kappa_A\approx3.18\times10^3.}
\]

This is poor conditioning.

Meaning: although the equality rank is mathematically 24, finite experimental errors can strongly inflate the apparent one-dimensional null direction into a larger practical uncertainty region.

Therefore Toy 007 is a **proof of principle, not yet a robust experimental discriminator**.

The next optimizer must maximize response survival and calibration conditioning jointly.

---

## 12. New experiment-design objective

A minimal deterministic design score should include at least:

\[
\eta_R
=
\frac{\|P_NC_R\|}{\|C_R\|},
\]

remaining nullity

\[
q=d^2-r_{obs},
\]

and normalized calibration conditioning

\[
s_{min}(A_{norm}).
\]

A schematic objective is

\[
\boxed{
J=\eta_R\,f(s_{min})
}
\]

subject to

\[
q\le q_{max}
\]

and physical constraints on probe placement, timing and measurement count.

For real experiments this operator-space score must eventually be replaced or supplemented by a Fisher-information / likelihood-level objective including measurement covariance.

---

## 13. What this still does not prove

- The source is nonrelativistic and finite-mode.
- The calibration is finite; unmeasured source observables can still differ.
- A matter commutator response does not prove quantum geometry.
- The probe/detector transfer function has not yet been included.
- The signal size in SI units has not been estimated.
- Apparatus/control stress-energy is not yet included.
- Relativistic conservation/Bianchi/gauge gates remain open.

---

## 14. Reproducibility

See

`analysis/toy007_finite_multiprobe_design.py`.

The search uses a fixed source inherited from Toy 005, a deterministic random seed for candidate probe/time designs, a greedy rank-increasing symmetrized-constraint selector, and records the best design under a response-survival/conditioning score.

This is not a proof of global optimality.

---

## 15. Next target

1. Improve conditioning by optimizing geometry/time samples and allowing more than two probes.
2. Replace exact row-rank objectives by covariance-weighted Fisher/likelihood metrics.
3. Derive the source-to-gravity-to-detector linear transfer law for `mean`, `N`, and `chi^R`.
4. Translate the dimensionless response split into physical units for realistic `m`, `L0`, source energy scale and detector susceptibility.
5. Compare the resulting observable against semiclassical/stochastic/classical-QFT/perturbative-QG baselines.

Toy 007 establishes that the operational middle ground identified by Toy 006 is nonempty: a finite calibration can be highly constraining without becoming fully tomographically complete, while an ordered-response direction still survives.
