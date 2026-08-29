# RQIR Toy Model 009 — Detector-Aware Source Optimization

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`  
**Status:** finite-dimensional detector-aware NP3 redesign; not a global optimum or experimental-readiness claim.

## 1. Motivation

Toy 007 was optimized before the detector layer was understood. Iterations 008–009 then showed that real observability depends on:

- the two dominant response bands;
- detector transfer/window functions;
- nuisance-profiled Fisher information;
- calibration conditioning;
- D1 control-switch burden;
- D2 equivalent-force noise.

Therefore source optimization should no longer maximize a source-side commutator residual alone.

The design vector used here is

\[
\boxed{
\mathbf Q=
(S_{eff}^{D1},\;S_{eff}^{D2},\;\eta_R,\;s_{min},\;-N_{sw})
}
\]

subject to state positivity, a fixed five-level energy spectrum, Newtonian embedding and finite geometry constraints.

The preferred design criterion is Pareto improvement rather than an arbitrary single scalar objective.

---

## 2. Fixed physical/algebraic domain

Use the same five-level spectrum as Toy 007,

\[
\boxed{E=(1,2,3,4,6)}.
\]

Candidate source operators are real symmetric matrices. Each is shifted positive, diagonalized and normalized so the nearest Newtonian source site lies at one dimensionless length unit.

Geometry constraints for this scan:

\[
\boxed{r_{max}\le 6,}
\]

and minimum site-spacing

\[
\boxed{\Delta r_{min}\ge0.1.}
\]

These are scan guards, not fundamental physical constants.

For the accepted NP3 scan, the Toy 007 finite calibration pattern is held fixed:

- probe 0 at `y0=0`;
- probe 1 at `y1=-3.5955271928522547`;
- the same seven calibration times;
- the same target-time self-noise and selected auto/cross symmetrized controls.

Thus any improvement is not obtained by silently weakening the old calibration protocol.

---

## 3. Negative result: detector-only NP2 optimization is unsafe

A 5000-trial detector-only scan with seed `20260829` finds a strong NP2 candidate at trial

\[
\boxed{2641}.
\]

Its embedded radii are approximately

\[
\boxed{
(1.0000,\;1.19973,\;1.56485,\;3.27170,\;5.18517).
}
\]

Relative to Toy 007, its ideal two-band source Fisher proxies improve by

\[
\boxed{
S_{eff}^{D1}:\;\times5.3625,
}
\]

\[
\boxed{
S_{eff}^{D2}:\;\times4.1741.
}
\]

However, when the old Toy 007 NP3 calibration is applied to this high-gain source, the response survival collapses to

\[
\boxed{\eta_R\approx0.02990,}
\]

with normalized conditioning

\[
\boxed{s_{min}\approx2.61\times10^{-4},}
\]

\[
\boxed{\kappa_A\approx1.75\times10^4.}
\]

The detector-level two-band response of the resulting NP3 null direction also falls below the Toy 007 baseline.

### Design lesson

> Maximizing detector response before calibration can produce a source that is almost entirely projected away by the calibration/nuisance geometry.

This is a numerical counterexample to detector-only source optimization. It is not a general theorem.

---

## 4. NP3-constrained scan

A second deterministic 5000-trial scan with seed

\[
\boxed{314159}
\]

requires, before ranking detector response,

\[
\eta_R\ge\eta_R^{007}
\]

and

\[
s_{min}\ge s_{min}^{007}.
\]

Only one scanned candidate satisfies both non-degradation conditions.

It occurs at trial

\[
\boxed{811}.
\]

This is therefore an unusually clean scan result, but it must not be called a global optimum.

---

## 5. Accepted Toy 009 geometry

The new dimensionless source radii are

\[
\boxed{
(1.00000,\;1.60090,\;1.77911,\;2.60901,\;5.90724).
}
\]

The minimum site spacing is

\[
\Delta r_{min}\approx0.17821,
\]

slightly larger than Toy 007's approximately `0.16347`.

The maximum radius remains below the scan guard `6`.

---

## 6. Exact NP3 calibration properties

Using the same finite calibration pattern as Toy 007,

\[
\boxed{rank(A)=24/25,}
\]

so one exact Hermitian null direction remains.

With

\[
\rho_\pm=I/5\pm0.08\Delta_0,
\]

the state eigenvalues are approximately

\[
\operatorname{eig}(\rho_+)
=(0.12000,0.17296,0.19541,0.24624,0.26539),
\]

\[
\operatorname{eig}(\rho_-)
=(0.13461,0.15376,0.20459,0.22704,0.28000).
\]

Both states are positive.

Maximum selected equality residual is below

\[
6\times10^{-16}.
\]

At the inherited target time,

\[
\langle B_0\rangle_+=\langle B_0\rangle_-
\approx0.547860,
\]

and centered target self-noise matches,

\[
N_{00,+}=N_{00,-}
\approx0.0132606.
\]

But the ordered response remains opposite:

\[
\boxed{
D_{00,+}\approx-0.0120850,
\qquad
D_{00,-}\approx+0.0120850.
}
\]

---

## 7. Calibration geometry improves

Toy 009 has

\[
\boxed{\eta_R\approx0.568823,}
\]

versus Toy 007

\[
\eta_R^{007}\approx0.457682.
\]

This is approximately a

\[
\boxed{24.3\%}
\]

increase in response-survival fraction.

The normalized smallest singular value becomes

\[
\boxed{s_{min}\approx1.5122\times10^{-3},}
\]

about `3.4%` above Toy 007.

The condition number becomes

\[
\boxed{\kappa_A\approx3.03\times10^3,}
\]

versus approximately `3.18e3` for Toy 007.

Thus the detector improvement is not purchased by worse exact calibration conditioning.

---

## 8. D1 potential-response improvement

Toy 009 NP3 potential-response harmonics are

\[
\boxed{
H_2\approx-0.00167587+i\,0.00792491,
}
\]

\[
\boxed{
H_4\approx+0.00434188+i\,0.00995421.
}
\]

Using the same two-band profiled Fisher definition as Protocol 002C, the ideal-window source information is

\[
\boxed{
S_{eff}^{D1}(009)
\approx1.22184\,
S_{eff}^{D1}(007).
}
\]

So Toy 009 improves the NP3 D1 source information by about

\[
\boxed{22.2\%}.
\]

---

## 9. D2 gradient-response improvement

The corresponding gradient/force harmonics are

\[
\boxed{
G_2\approx-0.00225535+i\,0.0133231,
}
\]

\[
\boxed{
G_4\approx+0.00508697+i\,0.0116624.
}
\]

Their profiled two-band source information is

\[
\boxed{
S_{eff}^{D2}(009)
\approx1.40358\,
S_{eff}^{D2}(007).
}
\]

So D2 improves by approximately

\[
\boxed{40.4\%}.
\]

Under the same deliberately optimistic force-noise benchmark used in Detector Comparison 001, the illustrative five-sigma mass-product requirement would scale from

\[
2.40\times10^{-18}\;kg^2
\]

to approximately

\[
\boxed{2.03\times10^{-18}\;kg^2.}
\]

This remains far from the Toy-source quantum regime; D2 is not suddenly experimental-ready.

---

## 10. D1 low-switch redesign

The new source also allows a lower-control-burden phase window.

### Four-switch sequence

A `pi`-periodic four-switch sequence can be written with one positive interval of length

\[
a\approx0.912594
\]

per half-period, followed by a negative interval of length `pi-a`, repeated.

For even harmonic `n`,

\[
|W_n|=\frac{4|\sin(na/2)|}{n\pi}.
\]

At the accepted `a`,

\[
|W_2|\approx0.50363,
\qquad
|W_4|\approx0.30807.
\]

Despite using half as many switches as the old Toy 007 sequence, the detector-level two-band Fisher proxy is

\[
\boxed{
F_{009,4sw}\approx1.12746\,F_{007,8sw}.
}
\]

### Six-switch sequence

An optimized six-switch interval vector is approximately

\[
(0.26890,0.92358,1.02555,2.11605,1.02554,0.92358),
\]

summing to `2 pi`.

It gives

\[
|W_2|\approx0.45974,
\qquad
|W_4|\approx0.36382,
\]

and

\[
\boxed{
F_{009,6sw}\approx1.23731\,F_{007,8sw}.
}
\]

Thus Toy 009 simultaneously provides more Fisher information and fewer hard sensitivity switches.

If every switch carries the same amplitude-contrast factor `c<=1`, the advantage over the eight-switch Toy 007 design only grows because Fisher carries factors `c^(2N_sw)`.

---

## 11. Revised D1 scaling illustrations

Starting from the previous bounded-window Toy 007 illustration

\[
m_sm_p\approx8.1\times10^{-29}\;kg^2,
\]

Toy 009 gives approximately

### Four switches

\[
\boxed{
m_sm_p\approx7.63\times10^{-29}\;kg^2,
}
\]

with equal-mass illustration

\[
\boxed{m\approx8.73\times10^{-15}\;kg.}
\]

### Six switches

\[
\boxed{
m_sm_p\approx7.28\times10^{-29}\;kg^2,
}
\]

with equal-mass illustration

\[
\boxed{m\approx8.53\times10^{-15}\;kg.}
\]

These remain idealized scaling benchmarks, not implementation forecasts.

---

## 12. Interpretation

Toy 009 is the first RQIR source redesign that Pareto-improves the previous NP3 baseline in the simultaneously relevant directions:

- D1 two-band information;
- D2 two-band information;
- target response survival through exact calibration;
- calibration conditioning;
- D1 switch count.

This is stronger than the detector-only NP2 gain because it survives the same finite NP3 calibration protocol.

However, it is still only a finite nonrelativistic one-particle source model.

---

## 13. New design rule

### RQIR-DESIGN-001 — optimize source and inference geometry jointly

A useful source must be scored only after the calibration and detector maps are included:

\[
\boxed{
\text{source}
\to
\text{calibration/null or Fisher geometry}
\to
\text{gravity transfer}
\to
\text{detector window/noise}
\to
F_{\beta|\theta}.
}
\]

Optimizing an earlier layer in isolation can produce large apparent gains that disappear at a later projection.

---

## 14. External-method boundary

The idea of engineering time-dependent quantum-sensor sensitivity functions is established outside RQIR. Recent continuous phased dynamical-decoupling work demonstrates that AC quantum sensing need not rely exclusively on ideal instantaneous pulses and can use continuous control with discrete phase changes. RQIR therefore does not claim lock-in/control modulation itself as new physics.

The RQIR-specific contribution is the joint source/calibration/detector optimization for the ordered gravity-interface discriminator.

---

## 15. Reproducibility

- `analysis/toy009_detector_aware_source_search.py`
- `analysis/d1_low_switch_toy009.py`

The source scans are deterministic and record their random seeds and trial identities.

---

## 16. Next gate

1. Re-optimize the second probe location and calibration times jointly with the Toy 009 source instead of inheriting Toy 007 settings.
2. Replace exact-rank/conditioning guards by the full detector covariance Fisher objective.
3. Test whether continuous/phase-modulated D1 sensitivity functions can outperform four/six hard switches once bandwidth and contrast are included.
4. Only after detector/calibration optimization stabilizes, attempt a more physical oscillator/atomic realization and full source+apparatus stress-energy embedding.
