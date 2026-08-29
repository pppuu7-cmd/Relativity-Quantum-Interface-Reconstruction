# RQIR Detector Branch Comparison 001 — D1 Matter-Wave Phase vs D2 Mechanical Force

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `EMP`, `OPEN`  
**Status:** first common-normalization detector comparison; not an experimental-readiness claim.

## 1. Question

Use the *same* Toy 007 source pair, pump definition and interface-response amplitude for two detector classes:

- **D1:** matter-wave / phase interferometric readout of gravitational potential;
- **D2:** levitated or mechanical readout of gravitational force/acceleration.

The comparison is required to use the same source waveform before detector transfer.

---

## 2. Common source and pump

The accepted Toy 007 source has dimensionless site coordinates

\[
x_a\approx(5.53112,2.21089,1.44295,1.27948,1.00000),
\]

and probe/readout point `y0=0`.

The dimensionless potential operator is

\[
B(y)=\sum_a \frac{n_a}{|x_a-y|}.
\]

Physical potential:

\[
\Phi(y)=-\frac{Gm_s}{L_0}B(y).
\]

Use the same weak pump area as Protocol 001/002,

\[
\alpha=\frac{m_s}{\hbar}\int A(t)dt.
\]

For any source readout operator `R`, the linear response to the `B_0=B(0)` pump is controlled by

\[
\Delta D_{R B_0}(t,0)
=\frac{1}{2i}\operatorname{Tr}
[(\rho_+-\rho_-)[R(t),B_0]].
\]

---

## 3. D1 — potential/phase branch

The accepted potential-response harmonics remain

\[
H_2\approx-2.71833\times10^{-4}-i\,7.66139\times10^{-3},
\]

\[
H_4\approx+1.20943\times10^{-3}-i\,9.06108\times10^{-3}.
\]

Their two-band norm is

\[
H_{24}=\sqrt{|H_2|^2+|H_4|^2}
\approx1.19305\times10^{-2},
\]

and equal-noise spectral imbalance is

\[
\kappa_B\approx0.174201,
\qquad
1-\kappa_B^2\approx0.969654.
\]

### 3.1 New correction: a passive full-period phase integral can null the signal

A realistic phase observable has a detector sensitivity function `g(t)`,

\[
\Delta\varphi
=\frac{m_p}{\hbar}\int dt\,g(t)\Delta\Phi(t).
\]

For a source harmonic `n`, define normalized window transfer

\[
\mathcal W_n
=\frac{1}{T_D}\int_0^{T_D}dt\,g(t)e^{i\omega_n t}.
\]

The physical harmonic becomes

\[
\boxed{
\Delta\varphi_n
=2\alpha\frac{Gm_sm_pT_D}{\hbar L_0}
H_n\mathcal W_n.
}
\]

Protocol 002B implicitly used an ideal matched-readout scale `|W_n|=1`. It must **not** be interpreted as a passive uniform phase integral.

For `g(t)=1` over exactly one complete source period,

\[
\mathcal W_2=\mathcal W_4=0.
\]

Hence a plain full-period integration exactly cancels both selected AC harmonics in the ideal periodic model.

### RQIR-D1-001 — full-period window cancellation

> A detector that only integrates the oscillatory potential uniformly over an integer number of complete source periods is blind to all nonzero integer source harmonics.

This is a detector-window obstruction, not a failure of the source response.

---

## 4. A simple dual-harmonic D1 lock-in sequence

As a proof of principle, impose a bounded periodic sensitivity function

\[
g(\tau)=\operatorname{sign}
[\cos(2\tau)+\lambda\cos(4\tau)],
\qquad |g|=1.
\]

A deterministic one-parameter scan gives near

\[
\boxed{\lambda\approx1.046}
\]

the window magnitudes

\[
|\mathcal W_2|\approx0.4402,
\qquad
|\mathcal W_4|\approx0.3851.
\]

After the same free relative-tilt nuisance used in Protocol 002C, this simple bounded sequence retains approximately

\[
\boxed{17.2\%}
\]

of the ideal two-band Fisher information, or

\[
\boxed{41.5\%}
\]

of the ideal SNR amplitude.

This sequence is not claimed to be experimentally optimal. Finite pulse time, path geometry, contrast loss and phase-cycling have not yet been included.

### 4.1 Revised D1 scaling illustration

Protocol 002B gave the ideal-window five-sigma illustration

\[
m_sm_p\gtrsim3.36\times10^{-29}\;{\rm kg}^2
\]

for `alpha=0.1`, `L0=10 um`, `T=1 s`, `sigma_phi=1 mrad`.

Applying the simple bounded dual-band window above gives approximately

\[
\boxed{
m_sm_p\gtrsim8.1\times10^{-29}\;{\rm kg}^2
}
\]

and, for equal masses only as an illustration,

\[
\boxed{
m_s=m_p\gtrsim9.0\times10^{-15}\;{\rm kg}.
}
\]

This remains a scaling benchmark, not a realizability claim.

---

## 5. D2 — force/acceleration branch

Differentiate the Newtonian readout with respect to the probe coordinate:

\[
G_0\equiv\left.\frac{\partial B(y)}{\partial y}\right|_{y=0}
=\sum_a\frac{1}{x_a^2}n_a
\]

because all recorded Toy 007 sites lie at `x_a>0`.

Physical acceleration at the detector is

\[
a_0=\frac{Gm_s}{L_0^2}G_0,
\]

up to the declared axis sign.

The force on a mechanical probe of mass `m_p` is

\[
F_0=m_p a_0.
\]

The cross-response to the same `B_0` pump has dominant harmonics

\[
\boxed{
G_2\approx-6.78211\times10^{-4}
-i\,1.14277\times10^{-2},
}
\]

\[
\boxed{
G_4\approx+1.41626\times10^{-3}
-i\,1.06107\times10^{-2}.
}
\]

The two-band gradient-response norm is

\[
\boxed{
G_{24}\approx1.56731\times10^{-2},
}
\]

about

\[
\boxed{1.314}
\]

times the D1 potential-response norm in the same dimensionless source model.

More importantly, the two gradient bands are very well balanced:

\[
\boxed{
\kappa_G\approx-0.06701,
\qquad
1-\kappa_G^2\approx0.99551.
}
\]

Thus only about `0.45%` of equal-noise two-band information is lost to the same antisymmetric relative-tilt nuisance.

**Result:** D2 has a cleaner intrinsic two-band *shape* than D1 for the current Toy 007 geometry.

---

## 6. D2 physical transfer

The force harmonics are

\[
\boxed{
\Delta F_n
=2\alpha\frac{Gm_sm_p}{L_0^2}G_n.
}
\]

For a mechanical susceptibility

\[
\chi_m(\omega)
=\frac{1}{m_p(\Omega_m^2-\omega^2-i\gamma_m\omega)},
\]

the displacement signal is

\[
x_n=\chi_m(\omega_n)\Delta F_n.
\]

If the measured displacement PSD contains force noise plus readout imprecision,

\[
S_x^{obs}
=|\chi_m|^2 S_F^{th}+S_x^{imp},
\]

define the equivalent-force PSD

\[
\boxed{
S_F^{eq}
=S_F^{th}+\frac{S_x^{imp}}{|\chi_m|^2}.
}
\]

Then the whitened information power is simply

\[
\boxed{
P_n^{D2}
\propto
\frac{|\Delta F_n|^2T_{int}}{S_{F,n}^{eq}}.
}
\]

### RQIR-D2-001 — resonance-gain cancellation at the force-noise floor

If thermal/environmental force noise dominates,

\[
S_F^{eq}\approx S_F^{th},
\]

and the explicit mechanical susceptibility cancels between displacement signal and displacement noise.

Therefore a larger resonant displacement or larger `Q` does **not by itself** improve force-domain Fisher information once the sensor is already force-noise limited.

Resonance can still help when readout imprecision is important because it reduces the equivalent imprecision term `S_x^imp/|chi_m|^2`.

---

## 7. D2 benchmark gap

For a deliberately optimistic, detector-agnostic design point

\[
S_F^{1/2}=10^{-21}\;{\rm N}/\sqrt{\rm Hz},
\qquad
T_{int}=1\;{\rm s},
\]

with the same

\[
\alpha=0.1,
\qquad
L_0=10\;\mu{\rm m},
\]

and strong common-amplitude calibration, five-sigma two-band detection would require approximately

\[
\boxed{
m_sm_p\gtrsim2.40\times10^{-18}\;{\rm kg}^2.
}
\]

Equal masses would correspond to

\[
\boxed{
m_s=m_p\sim1.55\times10^{-9}\;{\rm kg},
}
\]

which is not compatible with the present Toy 007 quantum-source assumptions.

Relative to the simple bounded D1 phase benchmark above, this optimistic D2 force benchmark requires roughly

\[
\boxed{3\times10^{10}}
\]

times larger mass product.

This is **not a universal no-go for mechanical sensing**. It is a transparent benchmark showing that current zN-class force scales are far from the gravitational response of a `~10^-15 kg` source at `~10 um` in this protocol.

D2 can compensate partly by using a much larger *detector* mass because the detector itself need not be placed in a matter-wave superposition. However geometry, surface forces, detector acceleration noise and the source's quantum coherence remain separate constraints.

---

## 8. Current experimental boundary

Current external anchors checked for this iteration:

1. Pedalino et al., *Nature* **649**, 866–870 (2026), DOI `10.1038/s41586-025-09917-9`: matter-wave interference of sodium nanoparticles above `170 kDa`.
2. Skrabulis et al., *Phys. Rev. Lett.* **136**, 233604 (2026), DOI `10.1103/9wzm-3qyb`: optically levitated nanomechanical impulse sensing below the zero-point momentum scale.
3. Kamba et al., *Phys. Rev. Lett.* **137**, 050801 (2026), DOI `10.1103/js43-kq48`: levitated nano-accelerometer with approximately two orders of magnitude sensitivity enhancement from trap quenching.
4. Wang et al., *Phys. Rev. Lett.* **135**, 120803 (2025), DOI `10.1103/z8b4-sm79`: proposed levitated-nanodiamond gravity sensor, with quoted projected acceleration sensitivities in the microGal/sqrtHz range.
5. Ranjit et al., *Phys. Rev. A* **93**, 053801 (2016), DOI `10.1103/PhysRevA.93.053801`: established zeptonewton-scale levitated-nanosphere force sensing over long integration.

These external results establish platform capability boundaries; none implements the RQIR protocol.

---

## 9. Branch decision after Comparison 001

### D1 matter-wave phase

**Advantages**

- vastly stronger information scaling for the same small source/probe mass product;
- directly senses potential rather than its spatial derivative;
- two-band nuisance breaking remains available.

**New obstacle**

- passive full-period integration cancels the AC response;
- requires deliberately modulated/echo/lock-in sensitivity;
- required coherent mass remains roughly seven orders above the 2026 free-particle matter-wave mass record.

### D2 mechanical force

**Advantages**

- current Toy 007 gradient response is 31% larger in dimensionless two-band norm;
- two main bands are almost ideally balanced against spectral-tilt nuisance;
- detector need not itself be a massive matter-wave superposition;
- mature force/acceleration readout techniques exist.

**Obstacle**

- absolute gravitational force/acceleration is extremely small;
- even an optimistic `1 zN/sqrtHz` equivalent-force floor leaves a very large mass-product gap;
- a single narrow resonance can also destroy the two-band nuisance-breaking advantage if one harmonic is effectively lost.

### Current ranking

For the *present RQIR source model and micrometre geometry*, D1 is the stronger theoretical sensitivity route, while D2 is the more mature readout technology but is presently much farther away in absolute force sensitivity.

This ranking is conditional and must be revisited if source mass, separation, detector mass, integration time or detector PSD changes substantially.

---

## 10. Next target

1. Replace the ideal D1 bang-bang sequence by a realizable finite-pulse interferometer sensitivity function and optimize `P2,P4` under pulse/contrast constraints.
2. Build a D2 equivalent-force PSD model with thermal force noise, readout imprecision and two-band mechanical transfer; test one-mode versus two-mode/tunable readout.
3. Optimize the source geometry jointly for potential and gradient responses rather than inheriting Toy 007 geometry.
4. Compare both branches after a common resource constraint, especially source coherence time and source mass.
5. Only then begin class-by-class semiclassical/stochastic/alternative-interface likelihood comparison.

Reproducibility: `analysis/detector_branch_d1_d2.py`.
