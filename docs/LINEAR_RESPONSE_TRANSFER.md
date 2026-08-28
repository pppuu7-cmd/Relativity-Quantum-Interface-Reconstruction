# RQIR Transfer Layer 001 — Source → Gravity → Detector

**Date:** 2026-08-29  
**Version:** 0.1  
**Labels:** `DEF`, `EST`, `DRV`, `OPEN`  
**Purpose:** derive the first convention-explicit transfer map carrying source mean, symmetrized noise and retarded response into gravitational and detector observables.

## 1. Epistemic status

This document does **not** propose a new law of gravity.

Established ingredients used here include:

- semiclassical mean-field sourcing;
- linear response / Kubo theory;
- Schwinger–Keldysh / CTP influence-functionals;
- stochastic-gravity separation of noise and dissipation/response;
- Einstein–Langevin propagation of stress-energy fluctuations into metric fluctuations.

The RQIR-specific contribution is organizational and inverse-problem oriented: put the source kernels, gravitational transfer and detector transfer into one declared chain so that competing interface classes can be compared in a common observable basis.

---

## 2. Source-side coordinates

For a nonrelativistic weak-field source, use mass density

\[
\hat\rho(\mathbf x,t)
=\bar\rho(\mathbf x,t)+\delta\hat\rho(\mathbf x,t).
\]

The source coordinates retained at second order are

\[
J_\rho(1)=\langle\hat\rho(1)\rangle,
\]

\[
N_\rho(1,2)
=\frac12
\left\langle
\{\delta\hat\rho(1),\delta\hat\rho(2)\}
\right\rangle,
\]

and, using the current RQIR convention,

\[
\boxed{
\chi_\rho^R(1,2)
=\frac{i}{\hbar}\theta(t_1-t_2)
\left\langle
[\hat\rho(1),\hat\rho(2)]
\right\rangle.
}
\]

Here `1=(x_1,t_1)` and repeated spacetime labels imply integration/convolution where appropriate.

---

## 3. Sign convention audit

Suppose a weak classical potential perturbation enters the matter Hamiltonian as

\[
\delta H(t)
=\int d^3x\,\hat\rho(\mathbf x,t)\,\delta\Phi(\mathbf x,t).
\]

With the RQIR definition above, first-order Kubo response gives

\[
\boxed{
\delta\langle\rho\rangle
=-\chi_\rho^R*\delta\Phi.
}
\]

To keep later formulas portable across alternative sign conventions, define

\[
\delta\langle\rho\rangle
=\sigma_\chi\chi_\rho^R*\delta\Phi,
\]

where for the convention and coupling declared above

\[
\boxed{\sigma_\chi=-1.}
\]

### Rule T1 — never hide response-sign conventions

Every implementation must record both the definition of `chi^R` and the sign of the perturbing Hamiltonian. A response sign cannot be compared across papers/models until these conventions are aligned.

---

## 4. Bare Newtonian gravitational transfer

Define the spatial Green kernel `K_N` by

\[
\nabla^2 K_N(\mathbf x,\mathbf x')
=\delta^{(3)}(\mathbf x-\mathbf x'),
\]

so in free space

\[
K_N(\mathbf x,\mathbf x')
=-\frac{1}{4\pi|\mathbf x-\mathbf x'|}.
\]

Define the bare density-to-potential transfer operator

\[
\boxed{
R_G\equiv4\pi G K_N,
}
\]

so that

\[
\Phi=R_G*\rho
=-G\int d^3x'\frac{\rho(\mathbf x')}{|\mathbf x-\mathbf x'|}.
\]

In spatial Fourier variables,

\[
\boxed{
R_G(\mathbf k)=-\frac{4\pi G}{k^2}.
}
\]

The Newtonian potential is a constraint field rather than an independent propagating relativistic degree of freedom. Time dependence in this first transfer layer therefore comes from the source and detector dynamics. A fully relativistic retarded metric propagator is treated separately below.

---

## 5. Linearized self-consistent source–gravity equation

Linearize about a declared self-consistent mean configuration.

Write the source-density fluctuation as three conceptually distinct pieces:

\[
\delta\rho
=\delta\rho_{ext}
+\delta\langle\rho\rangle
+\xi_\rho,
\]

where

- `delta rho_ext` is a controlled external source perturbation;
- `delta<rho>` is induced matter response to the gravitational potential;
- `xi_rho` represents the source fluctuation channel with symmetrized covariance `N_rho`.

The weak gravitational potential fluctuation is

\[
\delta\Phi
=R_G*
\left(
\delta\rho_{ext}
+\sigma_\chi\chi_\rho^R*\delta\Phi
+\xi_\rho
\right)
+\phi_{intr}.
\]

Here `phi_intr` is a model-class placeholder for an independent/intrinsic gravitational fluctuation sector. It is zero in a strictly classical deterministic Newtonian baseline, but RQIR keeps it explicit rather than silently excluding intrinsic gravity fluctuations.

Rearranging,

\[
\boxed{
\left[I-R_G*\sigma_\chi\chi_\rho^R\right]
*\delta\Phi
=R_G*(\delta\rho_{ext}+\xi_\rho)+\phi_{intr}.
}
\]

---

## 6. Dressed gravitational transfer

Define

\[
\boxed{
\mathcal D_\Phi^R
\equiv
\left[I-R_G*\sigma_\chi\chi_\rho^R\right]^{-1}
}
\]

and the dressed source-density to potential response

\[
\boxed{
\mathcal R_{\Phi\rho}^R
\equiv
\mathcal D_\Phi^R*R_G.
}
\]

Then

\[
\boxed{
\delta\Phi
=
\mathcal R_{\Phi\rho}^R*\delta\rho_{ext}
+
\mathcal R_{\Phi\rho}^R*\xi_\rho
+
\mathcal D_\Phi^R*\phi_{intr}.
}
\]

This separates three questions cleanly:

1. how the source responds (`chi_rho^R`);
2. how gravity transfers that source information (`R_G` and model-dependent intrinsic sector);
3. what the detector subsequently measures.

### Weak-backreaction expansion

If

\[
\|R_G\chi_\rho^R\|\ll1,
\]

then

\[
\mathcal R_{\Phi\rho}^R
=R_G
+R_G*\sigma_\chi\chi_\rho^R*R_G
+O(G^3\chi^2)
\]

when `R_G=O(G)`.

This explicitly shows where the source retarded response enters beyond the bare mean-field transfer.

---

## 7. Stationary Fourier-domain form

For a stationary translation-invariant approximation,

\[
\boxed{
\mathcal R_{\Phi\rho}^R(\mathbf k,\omega)
=
\frac{R_G(\mathbf k)}
{1-\sigma_\chi R_G(\mathbf k)\chi_\rho^R(\mathbf k,\omega)}.
}
\]

Using

\[
R_G(\mathbf k)=-\frac{4\pi G}{k^2}
\]

and the present convention `sigma_chi=-1`,

\[
\boxed{
\mathcal R_{\Phi\rho}^R(\mathbf k,\omega)
=
-\frac{4\pi G}
{k^2-4\pi G\chi_\rho^R(\mathbf k,\omega)}.
}
\]

This form makes poles/collective instabilities visible. Any apparent pole must be checked against the validity of the linear-response approximation, source stability and the Newtonian regime before physical interpretation.

---

## 8. Potential-noise transfer

Assume initially that source fluctuation `xi_rho` and intrinsic-gravity fluctuation `phi_intr` are statistically independent.

Let

\[
N_\rho
=\frac12\langle\{\xi_\rho,\xi_\rho\}\rangle
\]

and

\[
N_\Phi^{intr}
=\frac12\langle\{\phi_{intr},\phi_{intr}\}\rangle
\]

in the appropriate classical stochastic or operator/symmetrized representation of the chosen model.

Then

\[
\boxed{
N_\Phi
=
\mathcal R_{\Phi\rho}^R
*N_\rho*
\mathcal R_{\Phi\rho}^A
+
\mathcal D_\Phi^R
*N_\Phi^{intr}*
\mathcal D_\Phi^A.
}
\]

If the sectors are correlated, cross-covariance terms must be added explicitly.

In a stationary scalar channel,

\[
\boxed{
N_\Phi(\mathbf k,\omega)
=
|\mathcal R_{\Phi\rho}^R|^2N_\rho
+
|\mathcal D_\Phi^R|^2N_\Phi^{intr}
}
\]

for independent sectors.

### Important interpretation

A nonzero measured gravitational noise spectrum does not determine whether the noise is:

- detector/environmental;
- classical source noise;
- quantum-matter-induced;
- intrinsic gravitational;
- or a mixture.

The transfer decomposition is designed precisely to keep these alternatives separate.

---

## 9. Noise and response are not generally redundant

RQIR must **not** assume a universal fluctuation-dissipation relation relating `N_rho` and `chi_rho^R`.

Such relations arise under additional conditions such as stationarity and thermal/KMS equilibrium. Away from those conditions, the symmetrized noise kernel and retarded response are independent coordinates of the source state/dynamics and must be reconstructed separately.

This point is essential for the Toy 003–007 programme, which deliberately constructs preparations with matched selected noise information but different ordered response.

---

## 10. Detector transfer

Let a detector output `O_D` respond linearly to the potential:

\[
\delta O_D
=R_D^R*\delta\Phi+n_D,
\]

where

- `R_D^R` is the detector susceptibility/response kernel;
- `n_D` is detector/environmental noise.

Then the source-density to detector response is

\[
\boxed{
\mathcal R_{D\rho}^R
=R_D^R*\mathcal R_{\Phi\rho}^R.
}
\]

For independent detector noise,

\[
\boxed{
N_D^{obs}
=R_D^R*N_\Phi*R_D^A+N_D.
}
\]

For multiple detectors `i,j`,

\[
\boxed{
N_{O_iO_j}
=R_i^R*N_\Phi*R_j^A+N_{D,ij},
}
\]

where the last term includes known/unknown detector cross-noise.

This is the natural transfer language for Toy 007 multiprobe covariance calibration.

---

## 11. Mean transfer

The mean configuration must be solved separately from fluctuations.

At the simplest Newtonian baseline,

\[
\bar\Phi=R_G*\bar\rho.
\]

If the equilibrium source density itself depends on the self-consistent mean potential, solve

\[
\boxed{
\bar\Phi=R_G*\bar\rho[\bar\Phi]
}
\]

before applying the linearized transfer above.

The detector mean is then

\[
\boxed{
\bar O_D=O_{D,0}+R_D^R*\bar\Phi
}
\]

within the declared linear detector model.

Mean, noise and response must therefore be fitted jointly but not conflated.

---

## 12. Compact RQIR transfer chain

The current weak-field second-order chain is

\[
\boxed{
(J_\rho,N_\rho,\chi_\rho^R)
\xrightarrow{\;\mathfrak T_G\;}
(J_\Phi,N_\Phi,\mathcal R_\Phi^R)
\xrightarrow{\;\mathfrak T_D\;}
(J_O,N_O,\mathcal R_O^R).
}
\]

More explicitly,

\[
\boxed{
\mathfrak T_{RQIR}^{(2)}
=\mathfrak T_D\circ\mathfrak T_G.
}
\]

This transfer object is a candidate central coordinate for cross-model comparison.

Different gravity-interface classes are represented by different choices of:

- bare gravitational kernel/propagator;
- matter backreaction kernel;
- intrinsic gravity fluctuation sector;
- nonlinear/higher-order corrections;
- causal/gauge constraints;
- detector coupling.

---

## 13. Covariant linearized analogue

The relativistic analogue around a declared semiclassical background has the schematic form

\[
\mathcal E^{(1)}_{ab}{}^{cd}h_{cd}
=
8\pi G
\left(
\delta\langle T_{ab}\rangle
+\xi_{ab}
+T_{ab}^{ext}
\right),
\]

with linear matter response

\[
\delta\langle T_{ab}(x)\rangle
=
\sigma_\chi
\int d^4y\,
\Pi^R_{ab}{}^{cd}(x,y)h_{cd}(y)
+\text{local/contact terms}.
\]

Thus schematically

\[
\boxed{
\left[\mathcal E^{(1)}-8\pi G\sigma_\chi\Pi^R\right]h
=8\pi G(\xi+T^{ext}).
}
\]

If the gauge-fixed/relational inverse exists,

\[
\boxed{
h=8\pi G\,G_h^R*(\xi+T^{ext})+h_{intr}.
}
\]

The induced metric-noise contribution then has the schematic structure

\[
\boxed{
N_h^{ind}
=(8\pi G)^2G_h^R*N_T*G_h^A.
}
\]

This matches the established stochastic-gravity architecture at linear order.

### Critical relativistic caveats

A full implementation must handle:

- gauge fixing or relational observables;
- Bianchi/conservation identities;
- renormalized stress-tensor response kernels;
- local counterterms/contact terms;
- initial-state/intrinsic metric fluctuations;
- causal retarded support;
- EFT power counting.

The Newtonian equations above should therefore not simply be promoted component-by-component to a covariant theory.

---

## 14. Model-class fingerprints in the transfer language

### B0 — deterministic semiclassical mean field

At the simplest level:

\[
N_\Phi^{intr}=0
\]

and only the mean source is used for the background. Matter linear response may still affect driven backreaction if included self-consistently.

### B1 — stochastic semiclassical gravity

Matter noise `N_T` drives induced geometry fluctuations through an Einstein–Langevin transfer; dissipation/response enters the dressed retarded kernel.

### B2 — classical gravity + full QFT matter

Quantum matter can carry response, correlations and quantum information even when the gravitational field is classical. RQIR must compute the same detector-level transfer before interpreting a nonclassical matter observable as quantum gravity.

### B3 — perturbative quantum gravity EFT

In addition to matter-induced effects, quantum gravitational degrees of freedom can contribute controlled low-energy response/noise/scattering structures. The exact decomposition depends on state, gauge/observable definition and EFT order.

### B4 — phenomenological hybrid/collapse/emergent interfaces

These may modify one or several transfer blocks. They must be represented by explicit changes in `T_G`, `T_D` or higher-order kernels rather than verbal labels.

---

## 15. Connection to Toy 007

Toy 007 constrains a finite set of source potential means and symmetrized auto/cross-noise entries while leaving a one-dimensional source response direction.

Transfer Layer 001 now clarifies the next question:

> Does the surviving source-side `chi^R` direction actually produce a detector-level observable after gravitational dressing and detector susceptibility are included, and how large is it relative to propagated source/noise uncertainty?

The relevant target is no longer simply

\[
\eta_R>0,
\]

but a covariance-weighted detector-level distinguishability.

---

## 16. Next statistical object

For model parameters or a local state-direction coordinate `theta`, let the detector mean/covariance be

\[
\mu(\theta),\qquad\Sigma(\theta).
\]

A first Gaussian/Fisher approximation should use

\[
F_{ij}
=\partial_i\mu^T\Sigma^{-1}\partial_j\mu
+\frac12
\operatorname{Tr}
\left[
\Sigma^{-1}(\partial_i\Sigma)
\Sigma^{-1}(\partial_j\Sigma)
\right].
\]

RQIR should project/profile nuisance directions and measure whether the ordered-response direction remains identifiable after realistic covariance propagation.

This will replace exact rank and `eta_R` as the primary experimental-design metric while retaining them as useful algebraic diagnostics.

---

## 17. Consistency gates

- `G0` dimensions: PASS for the declared Newtonian transfer.
- `G1` gauge/relational: Newtonian channel declared; covariant implementation OPEN.
- `G2` conservation/Bianchi: OPEN in the full relativistic transfer.
- `G3` positivity: source/detector covariance matrices must remain positive semidefinite.
- `G3b` spectral/response identities: must be enforced per matter model.
- `G4a` retarded support: required for `chi^R`, detector response and relativistic gravity propagator.
- `G5` classical limit: model dependent; OPEN beyond the deterministic baseline.
- `G6` gravity-off: PASS; `R_G -> 0` removes source-to-gravity transfer.
- `G8` Newtonian limit: PASS by construction for sections 2–12.
- `G9` EFT power counting: OPEN for B3.
- `G10` renormalization/smearing: essential for covariant stress-tensor kernels.
- `G12` degeneracy: central; intrinsic gravity, matter noise, detector noise and classical response must be separated.
- `G13` measurability: OPEN until SI-scale/Fisher analysis is performed.

---

## 18. Seed references

- B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), arXiv:0802.0658 — CTP/influence functional, noise kernel, dissipation/response, Einstein–Langevin framework.
- Standard Kubo linear-response theory — response of an observable to a weak perturbing Hamiltonian through a retarded commutator kernel; sign depends on the declared perturbation convention.
- RQIR `docs/ORDERED_KERNEL_HIERARCHY.md` — project definitions of `N`, `D`, `chi^R`.
- RQIR `docs/TOY_MODEL_007_FINITE_MULTIPROBE_NULLSPACE_DESIGN.md` — finite NP3 calibration to which this transfer layer will be applied.

## 19. Exact next computation

**Transfer Layer 002 — covariance-weighted detector design.**

1. Choose a concrete detector susceptibility `R_D^R` (first: harmonic/mechanical or atom-interferometric phase proxy).
2. Propagate Toy 007 source `N` and surviving response through `T_G` and `T_D`.
3. Assign physical source mass `m`, length `L0`, energy/time scale and detector noise.
4. Compute detector-level response difference and covariance.
5. Build Fisher/profile-likelihood distinguishability for the surviving response direction.
6. Optimize geometry/times against the detector-level metric rather than exact operator rank.
