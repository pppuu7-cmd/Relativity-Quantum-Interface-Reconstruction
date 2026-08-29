# RQIR D1 Control Layer 001 — Finite Bandwidth and Contrast Budget

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`

## 1. Purpose

Detector Comparison 001 showed that D1 must use a deliberately modulated sensitivity function; uniform full-period phase integration cancels the desired `2 omega_*` and `4 omega_*` response.

This note asks whether the simple bounded dual-band lock-in survives finite control bandwidth and repeated switching loss.

It is a control-resource model, not a specific interferometer hardware design.

---

## 2. Ideal bounded sequence

Use

\[
g_0(\tau)=sign[\cos(2\tau)+\lambda\cos(4\tau)],
\]

with the previously optimized

\[
\lambda\approx1.04604.
\]

Over one source period this sequence has

\[
\boxed{N_{sw}=8}
\]

sign changes.

Its normalized harmonic transfer magnitudes are

\[
|W_2|\approx0.4402,
\qquad
|W_4|\approx0.3851.
\]

---

## 3. Finite-bandwidth proxy

Model non-instantaneous switching by convolving the ideal sensitivity function with a normalized boxcar of width

\[
\delta t=fT_*.
\]

This is a simple low-pass proxy. In Fourier space harmonic `n` is multiplied by

\[
Q_n(f)=\frac{\sin(\pi nf)}{\pi nf}.
\]

Thus

\[
W_n(f)=W_n(0)Q_n(f).
\]

The profiled two-band information remains

\[
S_{eff}(f)
=\frac{4P_2(f)P_4(f)}{P_2(f)+P_4(f)},
\]

with

\[
P_n(f)\propto|H_nW_n(f)|^2.
\]

---

## 4. Numerical bandwidth budget

Relative to the instantaneous bounded sequence:

| smoothing width `f = delta t/T*` | retained Fisher | retained SNR amplitude |
|---:|---:|---:|
| 0.01 | 0.9968 | 0.9984 |
| 0.025 | 0.9800 | 0.9900 |
| 0.05 | 0.9210 | 0.9597 |
| 0.075 | 0.8255 | 0.9086 |
| 0.10 | 0.6986 | 0.8358 |
| 0.125 | 0.5481 | 0.7403 |
| 0.15 | 0.3864 | 0.6216 |
| 0.20 | 0.1035 | 0.3217 |

The approximately 50%-information point is

\[
\boxed{f_{50}\approx0.1325.}
\]

Therefore the simple two-band protocol is not singularly sensitive to infinitesimal switching time: in this proxy, switching/smoothing occupying `5%` of the source period costs only about `8%` of Fisher information.

The fourth harmonic is the first band to be strongly attenuated as control becomes slow.

---

## 5. Contrast accumulation

A different limitation is repeated control loss.

Let each of the eight switches multiply the signal amplitude by a common factor `c`.

Then total amplitude becomes

\[
A=A_0c^8,
\]

and Fisher information scales as

\[
F=F_0c^{16}.
\]

Required per-switch amplitude factors are therefore:

| desired total Fisher retention | required per-switch `c` |
|---:|---:|
| 50% | 0.9576 |
| 80% | 0.98615 |
| 90% | 0.99344 |

Thus the eight-switch strategy trades detector-window recovery for a potentially severe cumulative contrast requirement.

### RQIR-D1-002 — control-fidelity accumulation

> For a multi-switch harmonic lock-in, finite switching bandwidth can be relatively benign while small repeated contrast losses accumulate exponentially in Fisher information.

This is not a fundamental no-go because more efficient continuous modulation or fewer-switch sequences may exist.

---

## 6. Interpretation

The D1 problem is now separated into three distinct layers:

1. **source response exists:** Toy 007 / Protocol 002;
2. **detector window must overlap both bands:** RQIR-D1-001;
3. **control must preserve sufficient contrast:** RQIR-D1-002.

It is therefore incorrect to characterize D1 only by the ideal mass-product number.

A realistic experimental score must include

\[
F_{D1}
\propto
V^2
\frac{4P_2P_4}{P_2+P_4},
\]

where `V` includes contrast/control loss and each `P_n` includes the actual sensitivity-window transfer and phase noise.

---

## 7. Next D1 step

Replace the boxcar low-pass proxy by a specific finite-pulse sensitivity function, for example a piecewise pulse/hold sequence with declared maximum pulse rate and dead time. Optimize the number and locations of switches jointly with contrast loss rather than maximizing ideal harmonic transfer alone.

Reproducibility: `analysis/d1_finite_bandwidth_window.py`.
