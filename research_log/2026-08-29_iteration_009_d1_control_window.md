# RQIR Research Log — Iteration 009

**Date:** 2026-08-29  
**Theme:** D1 finite control bandwidth and contrast accumulation.

## Starting point

Iteration 008 established that D1 requires a deliberately modulated sensitivity function because uniform full-period phase accumulation cancels the selected AC response harmonics.

The simple bounded proof-of-principle sequence was

\[
g(\tau)=sign[\cos2\tau+1.046\cos4\tau].
\]

## Results

### 1. Switch count

The sequence has exactly

\[
N_{sw}=8
\]

sign changes per source period.

### 2. Finite-bandwidth proxy

Non-instantaneous switching was modeled by boxcar smoothing of fractional period width `f`, multiplying harmonic `n` by

\[
Q_n(f)=\sin(\pi nf)/(\pi nf).
\]

Retained two-band Fisher information relative to the instantaneous bounded sequence:

- `f=0.05`: `0.9210`;
- `f=0.10`: `0.6986`;
- `f=0.125`: `0.5481`;
- `f=0.15`: `0.3864`.

Approximate 50%-information point:

\[
f_{50}\approx0.1325.
\]

Thus the idealized dual-band sequence is not singularly sensitive to very small nonzero switching time. The fourth harmonic is attenuated first.

### 3. Contrast accumulation

If each of eight switches multiplies signal amplitude by `c`, then

\[
F/F_0=c^{16}.
\]

Required per-switch amplitude retention:

- 50% total Fisher: `c >= 0.95760`;
- 80% total Fisher: `c >= 0.98615`;
- 90% total Fisher: `c >= 0.99344`.

Recorded as `RQIR-D1-002`: repeated contrast/control loss can be more restrictive than finite switching bandwidth.

## Interpretation

D1 now has three separate gates:

1. source ordered-response exists;
2. detector sensitivity window overlaps both selected harmonics;
3. switching/control preserves sufficient contrast.

The ideal mass-product benchmark alone is therefore not an adequate experimental score.

## Files

- `docs/D1_FINITE_BANDWIDTH_CONTROL.md`
- `analysis/d1_finite_bandwidth_window.py`

## Next target

Use a specific finite-pulse/path-switching sensitivity function with explicit pulse duration, dead time and contrast model, then optimize switching count and harmonic balance jointly.
