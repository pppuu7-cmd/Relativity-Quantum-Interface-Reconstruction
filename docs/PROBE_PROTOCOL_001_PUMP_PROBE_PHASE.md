# RQIR Probe Protocol 001 — Pump–Probe Ordered-Response Phase Readout

**Date:** 2026-08-29  
**Version:** 0.1  
**Labels:** `DRV`, `EST`, `OPEN`  
**Purpose:** convert the Toy 007 source-side ordered-response split into a first explicit weak-field detector-level phase scaling.

## 1. Scope

Toy 007 proves that a finite NP3 calibration can leave a one-dimensional source-state direction invisible to the selected mean/noise controls while the source commutator response differs.

The next question is operational:

> If the source is weakly driven, what gravitational signal does that response split produce, and how could a matter-wave phase detector read it?

This document gives the first controlled scaling law. It is not yet an experimental proposal.

---

## 2. Toy 007 source channel

For source mass `m_s`, physical length scale `L0`, and dimensionless Toy 007 channel operator

\[
B_0=\sum_a w_{0a}n_a,
\]

the source-generated Newtonian potential at probe 0 is

\[
\boxed{
\hat\Phi_0=-\frac{Gm_s}{L_0}B_0.
}
\]

At the accepted target time

\[
t_R\approx3.583928899
\]

in the source's dimensionless time coordinate,

\[
D_{00,+}(t_R,0)
\approx-0.010565632,
\]

\[
D_{00,-}(t_R,0)
\approx+0.010565632.
\]

Thus

\[
\boxed{
\Delta D_{00}
\equiv D_{00,+}-D_{00,-}
\approx-0.021131264.
}
\]

The selected mean and symmetrized self-noise are equal at this same time.

---

## 3. Weak source drive

Apply a small external potential profile to the source sites,

\[
\delta\Phi_{drv}(x_a,t)
=A(t)w_{0a},
\]

so the perturbing source Hamiltonian is

\[
\boxed{
\delta H_{drv}(t)
=m_s A(t)B_0.
}
\]

This drive may conceptually be produced either by a calibrated gravitational actuator or by a nongravitational control used only to characterize the source susceptibility. Those two experimental interpretations must not be conflated later.

With current RQIR convention

\[
\chi_{00}^R(t,t')
=\frac{i}{\hbar}\theta(t-t')
\langle[B_0(t),B_0(t')]\rangle,
\]

Kubo response for `delta H=+m_s A B0` gives

\[
\delta\langle B_0(t)\rangle
=-m_s\int dt'\,\chi_{00}^R(t,t')A(t').
\]

Since

\[
\chi_{00}^R(t,t')
=-\frac{2}{\hbar}\theta(t-t')D_{00}(t,t'),
\]

we obtain

\[
\boxed{
\delta\langle B_0(t)\rangle
=
\frac{2m_s}{\hbar}
\int_{-\infty}^t dt'\,
D_{00}(t,t')A(t').
}
\]

for the declared sign convention.

---

## 4. Impulse-area coordinate

For a drive pulse narrow compared with the source response timescale, define the dimensionless pulse area

\[
\boxed{
\alpha
\equiv
\frac{m_s}{\hbar}
\int dt\,A(t).
}
\]

Linear response requires `|alpha|` and the resulting state displacement to remain sufficiently small; `alpha << 1` is a useful conservative perturbative target, not a universal bound.

For a pulse centered near `t=0`,

\[
\delta\langle B_0(t)\rangle_\pm
\approx2\alpha D_{00,\pm}(t,0).
\]

Hence at the Toy 007 target time,

\[
\boxed{
\Delta\delta\langle B_0(t_R)\rangle
=2\alpha\Delta D_{00}
\approx-0.04226253\,\alpha.
}
\]

This coefficient is a direct dimensionless output of Toy 007.

---

## 5. Gravitational response signal

The corresponding difference in source-generated potential response is

\[
\Delta\delta\Phi_0(t)
=-\frac{Gm_s}{L_0}
\Delta\delta\langle B_0(t)\rangle.
\]

Therefore near the target time,

\[
\boxed{
|\Delta\delta\Phi_0(t_R)|
\approx
0.04226253\,|\alpha|
\frac{Gm_s}{L_0}.
}
\]

This is the first RQIR scaling that converts the Toy 007 ordered-response split into physical gravitational-potential units.

It remains a **matter-response-induced gravitational signal**. It is not a signature of quantum geometry by itself.

---

## 6. Matter-wave phase detector

For a nonrelativistic probe particle of mass `m_p`, a weak perturbing potential contributes propagation phase through the action. In the simplest differential-potential approximation,

\[
\delta\varphi
=-\frac{m_p}{\hbar}
\int dt\,g_D(t)\,\delta\Phi(t),
\]

where `g_D(t)` is the interferometer sensitivity/arm-difference function.

A proper atom-interferometer calculation also includes laser phases, path motion and relativistic corrections. Here the expression is used only as a controlled weak-potential phase-transfer proxy.

Substituting the pump–probe response gives

\[
\boxed{
\Delta\varphi
=
2\alpha
\frac{Gm_sm_p}{\hbar L_0}
\int dt\,g_D(t)\,\Delta D_{00}(t,0).
}
\]

This is the main detector-level relation of Protocol 001.

---

## 7. Effective-duration approximation

If the detector is arranged so that its sensitivity samples a region where `Delta D` has approximately fixed sign and magnitude near the Toy 007 maximum, define an effective integration time `T_eff`.

Then

\[
\boxed{
|\Delta\varphi|
\approx
C_{007}|\alpha|
\frac{Gm_sm_pT_{eff}}{\hbar L_0},
}
\]

with

\[
\boxed{
C_{007}
=2|\Delta D_{00}(t_R,0)|
\approx0.04226253.
}
\]

The familiar gravitational interferometric scale

\[
\Gamma_G
\equiv
\frac{Gm_sm_pT_{eff}}{\hbar L_0}
\]

therefore appears multiplied by the null-pair response coefficient and the weak-drive area:

\[
\boxed{|\Delta\varphi|\approx C_{007}|\alpha|\Gamma_G.}
\]

---

## 8. Pure scaling examples — not feasibility claims

Take only for dimensional orientation

\[
|\alpha|=0.1,
\qquad
L_0=10\,\mu\mathrm m,
\qquad
T_{eff}=1\,\mathrm s.
\]

Then the approximate phase scaling is:

| Source mass `m_s` | Probe mass `m_p` | `|Delta phi|` |
|---:|---:|---:|
| `1e-18 kg` | `1e-18 kg` | `2.67e-10 rad` |
| `1e-14 kg` | `1e-17 kg` | `2.67e-5 rad` |
| `1e-14 kg` | `1e-14 kg` | `2.67e-2 rad` |

Conversely, a nominal target

\[
|\Delta\varphi|=10^{-3}\,\mathrm{rad}
\]

under the same `alpha`, `L0`, and `T_eff` would require the mass product

\[
\boxed{
m_sm_p\approx3.74\times10^{-30}\,\mathrm{kg}^2.
}
\]

If the masses were equal, this corresponds algebraically to

\[
\boxed{m_s=m_p\approx1.93\times10^{-15}\,\mathrm{kg}.}
\]

These numbers say **nothing** about whether the required quantum source state, five-mode coherent dynamics, actuator, isolation or detector can actually be realized at those masses. They are scaling coordinates only.

---

## 9. Hidden source-timescale constraint

Toy 007 uses a dimensionless Hamiltonian spectrum

\[
E/E_*=\{1,2,3,4,6\}.
\]

If

\[
\tau=E_*t_{phys}/\hbar,
\]

then the physical target response time is

\[
\boxed{
t_R^{phys}=3.58393\,\frac{\hbar}{E_*}.}
\]

Therefore source mass, mode spacing, tunneling/coupling scale and usable interrogation time are **not independent knobs**.

Increasing `m_s` in the phase formula without demonstrating that the required coherent five-mode Hamiltonian can still be prepared and maintained is invalid.

### Rule P1 — no free mass amplification

Any future feasibility estimate must couple the gravitational mass scaling to a concrete state-preparation/control Hamiltonian and decoherence model.

---

## 10. Drive provenance matters

There are two distinct protocols:

### A. Nongravitational susceptibility calibration

Use electromagnetic/trap control to implement a Hamiltonian proportional to `B0`, independently measure source `chi^R`, then use gravity only in the readout/transfer test.

Advantage: stronger source calibration.

Limitation: it does not by itself test whether gravity is the perturbing mediator.

### B. Gravity-only pump–probe test

Generate `A(t)w_0a` with a calibrated moving/controlled external mass distribution and read the source-generated gravitational response.

Advantage: directly tests a gravitational source-to-source response channel.

Limitation: the actuator's own gravitational field and mechanical/environmental correlations become major nuisance channels.

RQIR must keep these likelihoods separate.

---

## 11. Detector covariance

Let the measured phase be

\[
\varphi_{obs}=\varphi_{sig}+n_\varphi.
\]

For repeated shots with phase variance `sigma_phi^2`, a minimal local distinguishability proxy is

\[
\mathrm{SNR}^2
\approx
N_{shots}
\frac{(\Delta\varphi)^2}{\sigma_\varphi^2}
\]

only when shots are independent and the variance is parameter-independent.

The full RQIR treatment should instead use the covariance/Fisher expression in `LINEAR_RESPONSE_TRANSFER.md`, because source noise, actuator noise and detector noise can be correlated and parameter dependent.

---

## 12. New experimental gates exposed by Protocol 001

A credible implementation must close at least:

- source coherence over `t_R^phys`;
- realization/calibration of the five-mode Hamiltonian;
- preparation fidelity of the two NP3 states;
- weak-drive linearity in `alpha`;
- actuator-field profile fidelity;
- actuator mechanical/gravitational nuisance subtraction;
- mean/noise calibration conditioning from Toy 007;
- detector sensitivity function and reference-arm systematics;
- source-apparatus stress-energy accounting;
- environmental decoherence and technical force noise.

These are not secondary engineering details: each can reopen a classical explanation for the intended response residual.

---

## 13. What is established versus open

### Established/derived within the declared toy model

- Toy 007 response coefficient:
  \[
  C_{007}\approx0.04226253.
  \]
- weak impulse response:
  \[
  \Delta\delta B_0\approx2\alpha\Delta D_{00}.
  \]
- physical potential scaling:
  \[
  |\Delta\delta\Phi_0|
  \approx C_{007}|\alpha|Gm_s/L_0.
  \]
- interferometric phase scaling:
  \[
  |\Delta\varphi|
  \approx C_{007}|\alpha|Gm_sm_pT_{eff}/(\hbar L_0)
  \]
  under the effective-duration approximation.

### Still open

- physically realizable source masses and Hamiltonian scales;
- decoherence and preparation fidelity;
- actual detector architecture and noise spectrum;
- gravity-only actuator geometry;
- covariance/Fisher optimization;
- covariant/full-stress-energy embedding;
- discrimination among gravity-interface classes.

---

## 14. External formal boundary

Matter-wave/atom interferometer phase shifts in weak gravitational fields are standard and require careful inclusion of propagation, light/laser and relativistic contributions in precision work. Protocol 001 therefore treats the simple action-phase formula as a first transfer proxy, not the final atom-interferometer model.

Seed references:

- S. Dimopoulos et al., *General Relativistic Effects in Atom Interferometry*, Phys. Rev. D 78, 042003 (2008).
- L. Badurina et al., *Signatures of linearized gravity in atom interferometers: A simplified computational framework*, Phys. Rev. D 111, 042002 (2025).

---

## 15. Exact next computation

**Protocol 002 — response-waveform matched filtering and Fisher design.**

1. Compute the full Toy 007 `Delta D_00(t,0)` waveform over one source period.
2. Derive the optimal linear detector sensitivity function `g_D(t)` for white and colored phase noise.
3. Replace the local `T_eff` approximation by the exact matched-filter integral.
4. Propagate Toy 007 calibration uncertainty/conditioning into the predicted phase.
5. Determine how the optimal response signal scales with `E_*`, `m_s`, `m_p`, `L0`, decoherence rate and detector bandwidth.
6. Only then compare against actual experimental sensitivity classes.
