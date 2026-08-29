# RQIR Research Log — Iteration 008

**Date:** 2026-08-29  
**Theme:** first common-normalization comparison of detector branches D1 and D2.

## Starting point

Framework v0.7 had completed:

- finite NP3 source construction (Toy 007);
- exact-null versus Fisher distinction;
- two-harmonic profiled likelihood;
- physical matter-wave scaling;
- colored-detector two-band design law.

The exact next target was to compare:

- D1 matter-wave phase interferometry;
- D2 levitated/mechanical force or displacement sensing;

using the *same* Toy 007 source waveform and interface parameter.

## Work completed

### 1. D1 detector-window correction

General phase readout written as

\[
\Delta\varphi
=\frac{m_p}{\hbar}\int dt\,g(t)\Delta\Phi(t).
\]

For harmonic `n`, normalized detector window is

\[
\mathcal W_n=T_D^{-1}\int dt\,g(t)e^{i\omega_nt}.
\]

The Protocol 002B expression must therefore be understood as an ideal matched-readout scaling. A passive uniform full-period integration has

\[
\mathcal W_2=\mathcal W_4=0.
\]

Recorded as `RQIR-D1-001`: full-period window cancellation.

### 2. Simple bounded D1 dual-band readout

Tested

\[
g(\tau)=sign[\cos2\tau+\lambda\cos4\tau].
\]

Deterministic scan gives near

\[
\lambda\approx1.046,
\]

\[
|W_2|\approx0.4402,
\qquad
|W_4|\approx0.3851.
\]

This retains about `17.2%` of the ideal two-band Fisher information, or `41.5%` of ideal SNR amplitude.

Revised five-sigma D1 illustration under the previous Protocol 002B assumptions:

\[
m_sm_p\gtrsim8.1\times10^{-29}\,kg^2,
\]

with equal-mass illustration

\[
m_s=m_p\gtrsim9.0\times10^{-15}\,kg.
\]

### 3. D2 force-gradient response

Defined

\[
G_0=\partial_yB(y)|_{y=0}
=\sum_a x_a^{-2}n_a.
\]

Computed the cross-response of `G0(t)` to the same `B0` pump.

Dominant harmonics:

\[
G_2\approx-6.78211\times10^{-4}-i1.14277\times10^{-2},
\]

\[
G_4\approx1.41626\times10^{-3}-i1.06107\times10^{-2}.
\]

Two-band norm:

\[
G_{24}\approx1.56731\times10^{-2},
\]

about `1.314` times the D1 potential norm.

Two-band imbalance:

\[
\kappa_G\approx-0.06701,
\]

so

\[
1-\kappa_G^2\approx0.99551.
\]

Hence only about `0.45%` of equal-noise information is lost to the same antisymmetric relative spectral-tilt nuisance.

### 4. Mechanical equivalent-force transfer

With

\[
\Delta F_n
=2\alpha Gm_sm_pG_n/L_0^2,
\]

and

\[
x_n=\chi_m(\omega_n)\Delta F_n,
\]

define

\[
S_F^{eq}=S_F^{th}+S_x^{imp}/|\chi_m|^2.
\]

Then

\[
P_n\propto|\Delta F_n|^2T/S_F^{eq}.
\]

Derived `RQIR-D2-001`: if force noise dominates, the explicit mechanical susceptibility cancels from whitened force information. Resonance improves readout only insofar as it suppresses equivalent imprecision; it cannot by itself beat a physical force-noise floor.

### 5. D2 benchmark gap

At an optimistic design point

\[
S_F^{1/2}=10^{-21}\,N/\sqrt{Hz},
\quad
T=1s,
\quad
L_0=10\,\mu m,
\quad
\alpha=0.1,
\]

five-sigma two-band detection requires approximately

\[
m_sm_p\gtrsim2.40\times10^{-18}\,kg^2.
\]

Equal-mass illustration:

\[
m\sim1.55\times10^{-9}\,kg.
\]

This is roughly `3e10` times the revised D1 mass-product benchmark.

This is not a universal mechanical-sensor no-go; it is a detector-resource bound for the declared geometry and force floor.

## External boundary check

Current literature anchors checked:

- Pedalino et al., Nature 649, 866–870 (2026), nanoparticle matter-wave interference above 170 kDa.
- Skrabulis et al., PRL 136, 233604 (2026), levitated nanomechanical impulsive-force sensing below zero-point momentum scale.
- Kamba et al., PRL 137, 050801 (2026), levitated nano-accelerometer with approximately two orders sensitivity enhancement by quantum quench.
- Wang et al., PRL 135, 120803 (2025), proposed mesoscopic levitated gravity sensing.
- Ranjit et al., PRA 93, 053801 (2016), zeptonewton-scale levitated force sensing over long integration.

None is treated as an implementation of RQIR.

## Files added

- `docs/DETECTOR_BRANCH_D1_D2_COMPARISON.md`
- `analysis/detector_branch_d1_d2.py`

## Current branch ranking

- **D1:** stronger absolute gravitational-information scaling, but requires deliberate AC sensitivity modulation and extremely ambitious coherent mass.
- **D2:** cleaner two-band shape and technologically mature readout, but present force/acceleration scales leave a very large absolute-sensitivity gap.

## Exact next target

1. Replace idealized D1 bang-bang modulation by finite-pulse sensitivity functions and include visibility/contrast loss.
2. Construct D2 thermal + imprecision equivalent-force PSD and test one-mode versus dual-mode/tunable readout.
3. Jointly optimize source geometry for potential and force response rather than inheriting Toy 007 geometry.
4. Compare branches under the same source coherence-time resource budget.
