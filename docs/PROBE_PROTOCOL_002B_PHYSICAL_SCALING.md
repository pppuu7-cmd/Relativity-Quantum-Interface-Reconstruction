# RQIR Probe Protocol 002B — Physical Scaling of the Two-Harmonic Readout

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`  
**Purpose:** restore physical units for Protocol 002 and identify the mass/length/time/phase-noise combinations required before any experimental feasibility claim.

## 1. Source response after the pump

Protocol 001 uses a weak source drive with dimensionless impulse area

\[
\alpha=\frac{m_s}{\hbar}\int A(t)dt.
\]

For the Toy 007 null-pair response,

\[
\Delta B(\tau)=2\alpha\,\Delta D(\tau).
\]

Therefore the Fourier components at `n=2,4` are

\[
\boxed{
\Delta B_n=2\alpha H_n.
}
\]

The two-harmonic source-response norm is

\[
\boxed{
2|\alpha|H_{24}
}
\]

with

\[
H_{24}=\sqrt{|H_2|^2+|H_4|^2}
\approx1.19305\times10^{-2}.
\]

---

## 2. Newtonian potential scaling

For source mass `m_s` and physical length unit `L_0`,

\[
\Phi=-\frac{Gm_s}{L_0}B.
\]

Thus

\[
\boxed{
\Delta\Phi_n
=-2\alpha\frac{Gm_s}{L_0}H_n.
}
\]

This is still source-to-potential level.  Frequency-dependent gravitational dressing can modify it in more general interface classes; this expression is the weak-field Newtonian reference channel.

---

## 3. Simple matter-wave phase detector

For a probe of mass `m_p`, approximate the phase response to each selected harmonic by a common effective interaction time `T_D`:

\[
\Delta\varphi_n
\approx
-\frac{m_pT_D}{\hbar}\Delta\Phi_n.
\]

Define

\[
\boxed{
\Gamma_G
=\frac{Gm_sm_pT_D}{\hbar L_0}.
}
\]

Then

\[
\boxed{
\Delta\varphi_n
=2\alpha\Gamma_G H_n.
}
\]

The assumption of a common `T_D` for `n=2` and `n=4` is only the first detector model.  Protocol 002C must replace it by the complex frequency response `R_D^R(\omega_n)`.

---

## 4. Response SNR

Let the demodulated real/imaginary quadratures at both harmonics have equal phase-noise standard deviation

\[
\sigma_\varphi.
\]

Then the pre-profile two-harmonic response SNR is

\[
\boxed{
\rho_R
=\frac{2|\alpha|\Gamma_GH_{24}}{\sigma_\varphi}.
}
\]

Protocol 002 found the tilt-survival factor

\[
1-\kappa^2\approx0.969654.
\]

So in the strong static-calibration limit the profiled significance for `delta beta = 1` is approximately

\[
\boxed{
Z\approx
\rho_R\sqrt{1-\kappa^2}.
}
\]

---

## 5. Static calibration is intrinsically much larger in the toy geometry

At the Toy 007 target/reference point,

\[
\bar B_0\approx0.621539.
\]

If the static mean-potential calibration uses the same gravitational phase scale,

\[
\varphi_C\approx\Gamma_G\bar B_0.
\]

Hence

\[
\rho_C=\frac{\Gamma_G\bar B_0}{\sigma_C}.
\]

The ratio is

\[
\boxed{
\frac{\rho_C}{\rho_R}
=\frac{\bar B_0}{2|\alpha|H_{24}}
\frac{\sigma_\varphi}{\sigma_C}.
}
\]

For

\[
\alpha=0.1,
\qquad
\sigma_C=\sigma_\varphi,
\]

this gives

\[
\boxed{
\rho_C/\rho_R\approx260.5.
}
\]

Therefore, **inside this idealized detector model**, common amplitude calibration can in principle be far stronger than the small ordered-response signal.  This is why Protocol 002 is close to the response-limited regime once a clean static calibration is available.

This does not mean calibration is easy experimentally: backgrounds, ordinary gravitational gradients, detector gain and apparatus fields must be included later.

---

## 6. Five-sigma benchmark

In the strong-calibration limit, require

\[
Z=5.
\]

Then

\[
\Gamma_G
\gtrsim
\frac{5\sigma_\varphi}
{2|\alpha|H_{24}\sqrt{1-\kappa^2}}.
\]

For

\[
\alpha=0.1,
\qquad
\sigma_\varphi=10^{-3}\ {m rad},
\]

we obtain

\[
\boxed{
\Gamma_G\gtrsim2.128.
}
\]

With

\[
L_0=10\,\mu{\rm m},
\qquad
T_D=1\,{\rm s},
\]

this implies

\[
\boxed{
m_sm_p
\gtrsim
3.36\times10^{-29}\ {\rm kg}^2.
}
\]

If source and probe masses are equal,

\[
\boxed{
m_s=m_p\gtrsim5.80\times10^{-15}\ {\rm kg}.}
\]

This is a **benchmark scaling**, not a claim that such a coherent five-level source/probe currently exists.

---

## 7. Phase-noise scaling table

Keeping

\[
Z=5,
\quad
\alpha=0.1,
\quad
L_0=10\,\mu{\rm m},
\quad
T_D=1\,{\rm s},
\]

and assuming equal source/probe masses:

| demodulated phase noise | required `Gamma_G` | required equal mass |
|---:|---:|---:|
| `1e-3 rad` | 2.128 | `5.80e-15 kg` |
| `1e-4 rad` | 0.2128 | `1.83e-15 kg` |
| `1e-5 rad` | 0.02128 | `5.80e-16 kg` |
| `1e-6 rad` | 0.002128 | `1.83e-16 kg` |

The square-root mass scaling follows because the signal depends on the product `m_s m_p`.

---

## 8. Source-dynamics timescale gate

Toy 007 uses dimensionless Hamiltonian gaps measured in units of an energy scale `E_*`.

Physical time is

\[
\tau=\frac{E_*t}{\hbar}.
\]

The response frequencies are therefore

\[
\boxed{
\omega_n=n\frac{E_*}{\hbar}.
}
\]

One dimensionless `2pi` response period corresponds to

\[
\boxed{
T_*=\frac{2\pi\hbar}{E_*}.
}
\]

If the detector integrates for approximately one source period,

\[
T_D\sim T_*.
\]

Then

\[
\boxed{
\Gamma_G^{(1\,period)}
\sim
\frac{2\pi Gm_sm_p}{E_*L_0}.
}
\]

The explicit `hbar` cancels, but this is not a classical limit: the source must still maintain the quantum coherent dynamics that produced the ordered-response waveform.

This exposes an important design tradeoff:

- lower `E_*` gives a longer interaction period and larger gravitational phase;
- but source control, coherence time, thermal noise and environmental drift become more demanding.

Therefore mass cannot be optimized independently from the source gap scale.

---

## 9. Current experimental boundary — preliminary literature comparison

The physical benchmark above is in a mesoscopic mass regime rather than the mass regime of present free-particle matter-wave interference.

A 2026 Nature experiment reports nanoparticle matter-wave interference for sodium clusters above 170 kDa, corresponding to roughly

\[
2.8\times10^{-22}\ {\rm kg},
\]

with spatial delocalization larger than the particle size.

By contrast, current gravity-mediated-entanglement proposals commonly target nanodiamond masses around

\[
10^{-15}\ {\rm kg}
\]

with micrometre-scale superpositions, but these are proposal/design targets rather than completed QGEM demonstrations.

Thus the `5.8e-15 kg` symmetric benchmark at 1 mrad lies:

- many orders of magnitude above current free nanoparticle matter-wave-interference masses;
- in the broad mass neighborhood of ambitious mesoscopic gravity-superposition proposals.

This comparison is only a feasibility boundary.  RQIR does not yet claim that the Toy 007 five-level Hamiltonian can be implemented in those platforms.

---

## 10. Important asymmetry: source and probe need not have equal mass

The fundamental requirement is on

\[
\boxed{m_sm_p,}
\]

not on either mass separately.

Therefore the equal-mass numbers above are only illustrative.

A physically realistic design may use:

- a heavier coherent source and a lighter high-coherence probe;
- a lighter source with an enhanced mechanical/optomechanical phase sensor;
- repeated cycles that improve effective quadrature SNR without increasing single-object mass.

Every such trade must be propagated through source coherence and detector covariance rather than inferred from mass alone.

---

## 11. What this protocol still omits

- frequency-dependent `R_D^R(\omega)`;
- colored/correlated phase noise;
- finite-window spectral leakage;
- source decoherence during the response period;
- electromagnetic/Casimir backgrounds;
- mechanical trap/control stress-energy;
- gravity-induced backaction on the source dynamics;
- relativistic stress-energy conservation/gauge embedding;
- actual preparation/readout fidelity for the five-level state family.

These omissions prevent an experimental-readiness claim.

---

## 12. Next target — Protocol 002C

Replace the scalar `T_D` detector approximation by an explicit frequency-domain transfer:

\[
\Delta\varphi_n
=
R_D^R(\omega_n)
\mathcal R_{\Phi\rho}^R(\omega_n)
\Delta\rho_n,
\]

with detector covariance

\[
\Sigma_D(\omega_n).
\]

Then compute

\[
F_{\beta|\theta}
\]

using realistic colored noise and frequency-dependent gain.

Reproducibility: `analysis/protocol002b_physical_scaling.py`.
