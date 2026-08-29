# RQIR Statistical Identifiability 002 — Noisy Preparation and Calibration

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## 1. Question

Toy 010 improved exact NP3 geometry, but a real experiment does not know the prepared source state exactly. This note asks:

> If the amplitude of the prepared state difference along the exact NP3 null direction is uncertain, can gravitational calibration alone identify an interface-response amplitude `beta`?

The answer is no.

This exposes a new distinction between:

1. calibrating ordinary gravitational observables;
2. independently characterizing the quantum source preparation.

---

## 2. Local model

Let `n` be the unit exact-null direction of the Toy 010 gravitational calibration matrix:

\[
A n=0.
\]

Let `a` be the actual amplitude of the prepared state difference along that direction.

Let `beta` multiply the interface-response law being tested.

For the selected detector response, the leading signal is proportional to

\[
\boxed{\mu_D\propto\beta a\,s.}
\]

Therefore at the nominal point `beta=a=1`,

\[
\partial_\beta\mu_D=s,
\qquad
\partial_a\mu_D=s.
\]

The detector derivatives are exactly collinear.

Meanwhile the gravitational NP3 calibration has

\[
\partial_a\mu_C=A n=0.
\]

So the very state direction that carries the desired response is invisible to the declared exact gravitational calibration.

---

## 3. RQIR-NG-005 — null-amplitude self-calibration obstruction

### Statement

Suppose:

- `A n=0` for the source difference direction `n`;
- detector signal is locally `mu_D=beta a s`;
- no independent measurement constrains `a`.

Then `beta` and `a` are locally non-identifiable from detector plus `A`-calibration data.

The Fisher block for `(beta,a)` from the detector is proportional to

\[
S
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\]

which has rank one.

Because the gravitational null calibration contributes zero information on `a`, profiling `a` gives

\[
\boxed{F_{\beta|a}=0.}
\]

independently of how precise the orthogonal gravitational calibration becomes.

### Meaning

> An exact gravitational null protocol cannot use the same null observables to calibrate the amplitude of the hidden source direction whose response it wants to exploit.

Independent nongravitational source characterization is therefore logically required.

Examples could include preparation-control metrology or quantum-state tomography in observables not belonging to the gravitational null set.

This is an identifiability statement, not a claim that a particular laboratory tomography scheme is available.

---

## 4. Independent source-preparation information

Let an independent source-preparation measurement contribute Fisher information

\[
C_a
\]

on the amplitude `a`.

Normalize detector-only beta information to

\[
S=1.
\]

If all other source nuisance directions were known perfectly, profiling `a` gives

\[
\boxed{
F_{\beta|a}=\frac{C_a}{1+C_a}.
}
\]

Equivalently, to retain a fraction `r` of detector-limited information,

\[
\boxed{
\frac{C_a}{S}=\frac{r}{1-r}.
}
\]

In SNR language:

\[
\boxed{
\frac{\rho_{prep}}{\rho_D}
=\sqrt{\frac{r}{1-r}}.
}
\]

Examples:

| retained detector information | `C_a/S` | `rho_prep/rho_D` |
|---:|---:|---:|
| 50% | 1 | 1 |
| 80% | 4 | 2 |
| 90% | 9 | 3 |
| 95% | 19 | 4.36 |
| 99% | 99 | 9.95 |

Thus source-state amplitude characterization does not need infinite precision, but it must be stronger than the target detector measurement if one wants near detector-limited inference.

---

## 5. Add the remaining 24 source-state nuisance directions

Write the Hermitian state-difference perturbation as

\[
\delta\theta=a\,n+Q u,
\]

where columns of `Q` span the 24-dimensional orthogonal complement of `n`.

Toy 010 detector data use the real/imaginary quadratures of the `n=2` and `n=4` D1 response harmonics.

The local detector model is

\[
\mu_D
=\beta a s+B_u u.
\]

Row-normalized gravitational calibration contributes

\[
F_C=\gamma\,(A_{norm}Q)^T(A_{norm}Q),
\]

where `gamma` is the dimensionless calibration information strength relative to the normalized detector information scale.

Independent source preparation adds `C_a` on `a`.

The full Fisher matrix is then profiled over `a` and all 24 components of `u`.

---

## 6. Toy 010 numerical result

Toy 010 has normalized calibration smallest singular value

\[
\boxed{s_{min}\approx2.21101\times10^{-3}.}
\]

The associated crude conditioning-information scale is

\[
\boxed{
1/s_{min}^2\approx2.05\times10^5.
}
\]

This is not by itself the required calibration strength because the weakest calibration direction need not align perfectly with the detector nuisance tangent. The full Fisher calculation nevertheless finds the same order-of-magnitude problem.

With effectively perfect source-amplitude preparation calibration (`C_a -> infinity`), approximate gravitational calibration strengths required for retained detector information are:

| target retained `F_beta` | required `gamma` |
|---:|---:|
| 50% | `~1.2e5` |
| 80% | `~5.0e5` |
| 90% | `~1.2e6` |
| 95% | `~2.5e6` |

These values are dimensionless in the declared row-normalized toy Fisher model. They are **not** direct experimental SNR requirements until each calibration observable receives a physical covariance model.

With `C_a=9`, the asymptotic maximum retained information is 90%, and about 80% requires gravitational calibration strength of order

\[
\boxed{\gamma\sim9\times10^5.}
\]

---

## 7. Why conditioning now has a direct statistical meaning

The earlier exact-null analysis treated small `s_min` mainly as numerical fragility.

In the noisy Fisher model, it becomes a physical resource issue:

- weak singular directions of `A` correspond to source perturbations that large calibration noise can hide;
- those perturbations can mimic part of the detector response;
- suppressing them requires calibration information scaling roughly with the inverse squared weak singular scale when detector coupling is appreciable.

For comparison:

Toy 009 inherited calibration had

\[
s_{min}\approx1.5122\times10^{-3},
\]

so

\[
1/s_{min}^2\approx4.37\times10^5.
\]

Toy 010 improves this proxy to

\[
2.05\times10^5,
\]

a factor of about

\[
\boxed{2.14}
\]

less severe.

Thus the Toy 010 conditioning improvement is not merely aesthetic; it directly reduces the scale of finite-noise calibration burden.

---

## 8. New operational requirement

### RQIR-CAL-003 — dual source characterization

A viable response experiment needs two logically distinct calibration layers:

1. **gravitational/null calibration** — constrains ordinary mean/noise nuisance directions;
2. **nongravitational preparation calibration** — constrains the amplitude and relevant quantum coordinates intentionally left invisible by the gravitational null test.

Without layer 2, the interface amplitude is locally non-identifiable.

Without sufficiently strong layer 1, orthogonal state perturbations can still mimic the detector response.

---

## 9. Consequence for experimental design

The design object expands again:

\[
\boxed{
(\text{source preparation},
\text{nongravitational source metrology},
\text{gravitational calibration},
\text{detector},
\text{covariance})
\to
F_{\beta|\theta}.
}
\]

This means an RQIR experiment cannot be specified only by source mass, separation and detector sensitivity. It also needs a quantitative source-state verification budget.

---

## 10. Limits

- `gamma` is currently a row-normalized abstract information strength, not a physical instrument SNR.
- Calibration covariance is taken independent and isotropic after row normalization.
- State nuisance coordinates are local Hermitian perturbations; positivity boundaries are not imposed in the infinitesimal Fisher calculation.
- Detector noise is whitened and the D1 two-band quadratures are used as the data vector.
- Full apparatus stress-energy and relativistic consistency gates remain open.

---

## 11. Reproducibility

See

`analysis/toy010_noisy_calibration_fisher.py`.

The script verifies:

- `F_beta=0` for `C_a=0` at all tested gravitational calibration strengths;
- the asymptotic law `F_beta=C_a/(1+C_a)` when orthogonal calibration is extremely strong;
- finite-`gamma` Toy 010 retention curves.

---

## 12. Next target

Convert abstract `gamma` and `C_a` into physical measurement budgets:

1. assign shot/noise covariance to each potential mean calibration;
2. assign covariance to each symmetrized-noise estimate;
3. specify a concrete nongravitational source-state measurement protocol;
4. compute the number of repetitions / integration time required to reach the Fisher strengths above;
5. compare that resource cost against D1 detector integration and source coherence time.
