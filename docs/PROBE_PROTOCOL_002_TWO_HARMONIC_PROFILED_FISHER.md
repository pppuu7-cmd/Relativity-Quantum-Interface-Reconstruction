# RQIR Probe Protocol 002 — Two-Harmonic Profiled Fisher Readout

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`  
**Purpose:** convert the Toy 007 response spectrum into the first explicit detector-data likelihood geometry with nuisance profiling.

## 1. Response channels

Toy 007 produces a periodic ordered-response difference

\[
\Delta D_{00}(\tau,0)
\]

whose Fourier spectrum is dominated by harmonics `n=2` and `n=4`.

The complex Fourier coefficients are

\[
\boxed{
H_2
=-2.718331\times10^{-4}
-i\,7.661385\times10^{-3}
}
\]

and

\[
\boxed{
H_4
=1.209428\times10^{-3}
-i\,9.061082\times10^{-3}.
}
\]

Their magnitudes are approximately

\[
|H_2|\approx7.66621\times10^{-3},
\qquad
|H_4|\approx9.14144\times10^{-3}.
\]

Within the two-harmonic subspace the power fractions are

\[
p_2\approx0.4129,
\qquad
p_4\approx0.5871.
\]

The two-harmonic norm is

\[
\boxed{
H_{24}=\sqrt{|H_2|^2+|H_4|^2}
\approx1.19305\times10^{-2}.
}
\]

---

## 2. Minimal detector data vector

Use one independent static calibration datum plus complex demodulated response at the two harmonics:

\[
\mathbf y=
(C,\Re Z_2,\Im Z_2,\Re Z_4,\Im Z_4).
\]

This is a normalized statistical model.  Physical units and detector transfer factors will be restored through Transfer Layer 001 in a later iteration.

Assume for the first calculation:

- independent Gaussian static-calibration noise;
- circular equal-variance Gaussian noise in the four response quadratures;
- linearized parameter dependence around the fiducial point.

These assumptions are deliberately simple and must later be relaxed.

---

## 3. Parameter of interest and nuisance parameters

Define

- `beta` — dimensionless ordered-response/interface transfer amplitude, parameter of interest;
- `g` — common gravitational/source/detector amplitude normalization;
- `q` — unknown relative spectral tilt between the two harmonics;
- `tau` — timing/phase offset.

Write the complex response model as

\[
Z_n
=g\,\beta\,H_n
(1+q w_n)
\exp(i n\tau),
\]

with

\[
w_2=-1,
\qquad
w_4=+1.
\]

The static calibration is chosen to constrain `g` without direct `beta` dependence.

This is the first explicit realization of the `RQIR-CAL-001` requirement: calibration constrains a nuisance that would otherwise be exactly degenerate with the interface amplitude.

---

## 4. Why static calibration is necessary

In response data alone,

\[
\frac{\partial Z_n}{\partial\beta}
\propto H_n,
\qquad
\frac{\partial Z_n}{\partial\ln g}
\propto H_n.
\]

Therefore `beta` and common amplitude `g` are exactly collinear in the response likelihood.

Without an independent calibration of `g`,

\[
\boxed{F_{\beta|g}=0.}
\]

This is a detector-level degeneracy, not a property of the source commutator itself.

Thus a claimed measurement of an ordered-response amplitude requires an independent calibration of the ordinary gravitational/detector normalization.

---

## 5. Normalized SNR variables

Define

\[
\rho_R^2=S
\]

as the total squared signal-to-noise ratio of the two response harmonics for `g beta = 1` before nuisance profiling.

Define

\[
\rho_C^2=C
\]

as the squared SNR of the independent static amplitude calibration.

The relative two-harmonic power imbalance is

\[
\boxed{
\kappa
=\frac{|H_4|^2-|H_2|^2}
{|H_4|^2+|H_2|^2}
\approx0.174201.
}
\]

Therefore

\[
\boxed{
1-\kappa^2
\approx0.969654.
}
\]

---

## 6. Fisher matrix structure

At the fiducial point `beta=g=1`, `q=tau=0`, circular quadrature noise gives the normalized Fisher block for parameters

\[
(\beta,\ln g,q,\tau).
\]

The amplitude/tilt sector is

\[
F=
\begin{pmatrix}
S&S&\kappa S\\
S&S+C&\kappa S\\
\kappa S&\kappa S&S
\end{pmatrix}
\]

for `(beta, ln g, q)`.

The timing derivative is orthogonal to the amplitude derivatives under the circular-noise assumption because

\[
\Re\sum_n H_n^*(inH_n)=0.
\]

Thus `tau` does not reduce the local amplitude information in this idealized first model.

---

## 7. Closed-form profiled information

Profile over common amplitude `g` and spectral tilt `q`.

Define

\[
S_{eff}=S(1-\kappa^2).
\]

Then the exact Schur complement gives

\[
\boxed{
F_{\beta|g,q,\tau}
=\frac{S_{eff}C}{S_{eff}+C}.
}
\]

Equivalently,

\[
\boxed{
F_{\beta|g,q,\tau}
=
\frac{
\rho_R^2(1-\kappa^2)\rho_C^2
}{
\rho_R^2(1-\kappa^2)+\rho_C^2
}.
}
\]

The local expected significance for a small `beta` displacement is therefore

\[
\boxed{
Z_\beta
\approx
|\delta\beta|\sqrt{F_{\beta|g,q,\tau}}.
}
\]

This is the first RQIR detector-level nuisance-profiled discriminator formula.

---

## 8. Physical interpretation

### Strong calibration

If

\[
\rho_C^2\gg\rho_R^2(1-\kappa^2),
\]

then

\[
F_{\beta|\theta}
\to
\rho_R^2(1-\kappa^2).
\]

The experiment is response-noise limited.

### Weak calibration

If

\[
\rho_C^2\ll\rho_R^2(1-\kappa^2),
\]

then

\[
F_{\beta|\theta}
\to
\rho_C^2.
\]

The experiment is calibration limited.

Thus making the response detector arbitrarily sensitive does not help if ordinary gravitational/detector normalization is poorly calibrated.

---

## 9. Why two harmonics are qualitatively useful

With only one harmonic and an unconstrained relative-amplitude/tilt nuisance, the tilt derivative is collinear with the amplitude derivative.

In the present notation this corresponds to

\[
|\kappa|=1,
\]

so

\[
S_{eff}=0
\]

and therefore

\[
\boxed{F_{\beta|g,q}=0.}
\]

regardless of static amplitude calibration.

For the Toy 007 two-harmonic waveform,

\[
1-\kappa^2\approx0.969654.
\]

Hence the free relative-tilt nuisance costs only about 3.0% of the pre-profile two-harmonic response information in this idealized model.

This is a stronger statement than the earlier matched-filter SNR observation:

> the second harmonic channel is not only additional signal power; it breaks a detector/source spectral-shape degeneracy.

---

## 10. Example normalized significances

For `delta beta = 1`:

- `rho_R=rho_C=1` gives `sqrt(F) ≈ 0.702`;
- `rho_R=rho_C=10` gives `sqrt(F) ≈ 7.02`;
- `rho_R=10, rho_C=100` gives `sqrt(F) ≈ 9.80`;
- `rho_R=100, rho_C=10` gives `sqrt(F) ≈ 9.95`.

The asymmetry of the last two cases reflects the harmonic-tilt penalty and the fact that significance is limited by the weaker effective information channel.

These numbers are normalized and are not experimental forecasts.

---

## 11. What is established

### `DRV`

For the stated Gaussian/circular-noise model,

\[
F_{\beta|g,q,\tau}
=\frac{S(1-\kappa^2)C}{S(1-\kappa^2)+C}.
\]

### `NUM`

For the Toy 007 `n=2,4` harmonics,

\[
\kappa\approx0.174201,
\qquad
1-\kappa^2\approx0.969654.
\]

### Consequence

A single-harmonic response amplitude is not robust to an unconstrained relative spectral-gain nuisance, whereas the two-harmonic waveform remains locally identifiable after profiling in the current model.

---

## 12. What remains open

- physical SI response noise and static calibration noise;
- colored/noncircular covariance between quadratures and harmonics;
- frequency-dependent detector gain;
- source energy-scale uncertainty that changes harmonic frequencies;
- finite observation window and spectral leakage;
- stochastic gravity / alternative-interface changes in both mean and covariance;
- apparatus backaction and control stress-energy;
- nonlinear likelihood away from the local Fisher regime.

---

## 13. Next extension

Protocol 002B should push the same two-harmonic likelihood through the physical transfer law:

\[
H_n^{source}
\xrightarrow{\mathcal R_{\Phi\rho}^R}
H_n^{gravity}
\xrightarrow{R_D^R}
H_n^{detector},
\]

with full covariance

\[
\Sigma_D(\omega)
=
R_D^R N_\Phi R_D^A+N_D.
\]

Then replace the normalized quantities `rho_R`, `rho_C` by values computed from an explicit detector and source geometry.

Reproducibility:

- `analysis/protocol002_response_spectrum.py`
- `analysis/protocol002_profiled_fisher.py`
