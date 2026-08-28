# RQIR Probe Protocol 002C — Colored Two-Harmonic Detector Design Law

**Date:** 2026-08-29  
**Labels:** `DRV`, `OPEN`  
**Purpose:** generalize Protocol 002 from equal white quadrature noise to frequency-dependent detector gain/noise and derive a direct spectral design criterion.

## 1. Detector-level harmonic amplitudes

After source dynamics, gravitational transfer and detector response, write the two selected complex detector amplitudes as

\[
s_n
=R_D^R(\omega_n)\,
\mathcal R_{\Phi\rho}^R(\omega_n)\,
H_n,
\qquad n\in\{2,4\}.
\]

All physical normalization factors such as pump amplitude and masses can be absorbed into a common amplitude parameter for the local Fisher calculation.

Let the effective circular quadrature-noise variances be

\[
\sigma_2^2,
\qquad
\sigma_4^2.
\]

Define the whitened information powers

\[
\boxed{
P_n=\frac{|s_n|^2}{\sigma_n^2}.
}
\]

These are detector-level quantities.  Raw source Fourier power is not the correct experiment-design variable once transfer and colored noise are included.

---

## 2. Relative spectral-tilt nuisance

Retain the same nuisance model as Protocol 002:

\[
s_n\to s_n(1+q w_n),
\]

with

\[
w_2=-1,
\qquad
w_4=+1.
\]

This represents an unknown first-order relative gain/shape distortion between the two selected bands.

The total pre-profile response information is

\[
S=P_2+P_4.
\]

The weighted imbalance is

\[
\boxed{
\kappa_w
=\frac{P_4-P_2}{P_4+P_2}.
}
\]

---

## 3. Closed-form shape-surviving information

Profiling the relative spectral tilt removes the component of common response amplitude parallel to the tilt direction.

Therefore

\[
S_{eff}=S(1-\kappa_w^2).
\]

Substituting the two-channel expression gives

\[
\boxed{
S_{eff}
=\frac{4P_2P_4}{P_2+P_4}.
}
\]

This is the key Protocol 002C design law.

---

## 4. Consequences

### 4.1 One useful band is not enough

If

\[
P_2\to0
\quad\text{or}\quad
P_4\to0,
\]

then

\[
\boxed{S_{eff}\to0.}
\]

Thus arbitrarily high SNR in only one of the two bands cannot distinguish a common interface amplitude from a free relative spectral-gain nuisance.

### 4.2 Balanced whitened powers are maximally robust at fixed total information

For fixed

\[
S=P_2+P_4,
\]

the product `P2 P4` is maximal at

\[
P_2=P_4=S/2.
\]

Hence

\[
\boxed{
S_{eff}^{max}=S
\quad\text{when}\quad
P_2=P_4.
}
\]

In this balanced limit, profiling the antisymmetric tilt nuisance costs no common-amplitude information locally.

The design target is therefore **balanced whitened response power**, not necessarily balanced source power.

### 4.3 Colored detector noise can destroy an otherwise good source waveform

Even though Toy 007 has reasonably balanced raw two-harmonic source power, a detector with

\[
|R_D(\omega_2)|^2/\sigma_2^2
\ll
|R_D(\omega_4)|^2/\sigma_4^2
\]

or the reverse can drive

\[
|\kappa_w|\to1
\]

and erase robustness to spectral tilt.

Therefore detector transfer and noise must enter before declaring the multi-harmonic discriminator viable.

---

## 5. Add static amplitude calibration

Let the independent static/common-amplitude calibration have information

\[
C=\rho_C^2.
\]

Then the Protocol 002 profiled result generalizes immediately to

\[
\boxed{
F_{\beta|\theta}
=
\frac{S_{eff}C}{S_{eff}+C}
=
\frac{
\frac{4P_2P_4}{P_2+P_4}C
}{
\frac{4P_2P_4}{P_2+P_4}+C
}.
}
\]

This equation combines:

1. frequency-dependent gravity+detector transfer;
2. colored per-band noise;
3. relative spectral-tilt profiling;
4. common amplitude calibration.

It is the current minimal detector-level RQIR design metric.

---

## 6. Timing/phase nuisance

For circular quadrature covariance, a small timing offset has derivative

\[
\partial_\tau s_n=i n s_n.
\]

The real Fisher inner product with the common amplitude derivative is

\[
\Re\sum_n s_n^*(in s_n)/\sigma_n^2=0.
\]

Thus timing offset remains locally orthogonal to common amplitude under this specific covariance model.

With noncircular quadrature covariance, correlated phase/amplitude noise or finite-window leakage, this orthogonality can fail.  Protocol 002D must use the full covariance matrix rather than independent `sigma_n`.

---

## 7. Current Toy 007 source balance

Before detector coloring, Protocol 002 found within the selected two-harmonic subspace

\[
p_2\approx0.4129,
\qquad
p_4\approx0.5871.
\]

Therefore

\[
\kappa\approx0.1742,
\]

and

\[
S_{eff}/S\approx0.96965.
\]

So the raw source waveform is already close to the balanced-information regime.

This favorable property can be lost or improved after multiplication by actual transfer functions and noise spectra.

---

## 8. Experimental design prescription

For each candidate source energy scale and detector:

1. compute physical harmonic frequencies
   \[
   \omega_n=nE_*/\hbar;
   \]
2. compute source harmonic amplitudes `H_n`;
3. propagate through `R_{Phi rho}^R(omega_n)`;
4. propagate through detector response `R_D^R(omega_n)`;
5. evaluate the complex noise covariance;
6. whiten the two harmonic channels;
7. calculate `P2`, `P4`, `S_eff`;
8. include common amplitude calibration `C`;
9. maximize profiled `F_{beta|theta}` over source gap scale, detector tuning and observing protocol.

This is more objective than maximizing raw phase amplitude alone.

---

## 9. Next target

The next physically decisive input is an explicit detector transfer/noise model.  Candidate branches:

- matter-wave phase interferometer;
- levitated mechanical force/phase sensor;
- clock/interferometric hybrid;
- resonant mechanical detector tuned near `2 omega_*` and `4 omega_*`.

RQIR should evaluate at least two detector classes before choosing a preferred experimental route.
