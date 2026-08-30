# RQIR Recovery Delta — Iteration 114

**Date:** 2026-08-31  
**Parent front:** Iteration 113.

## New two-band transfer quotient

For current two-real-band D2 science amplitudes `s=(s2,s4)`:

- beta score `(s2,s4)`;
- tilt score `(-s2,s4)`;
- gain scores `(s2,0)` and `(0,s4)`.

With `g2=c-d`, `g4=c+d`, common gain is exactly beta-aligned and differential gain exactly tilt-aligned.

### NG-071

Free per-band fractional gains imply exact `F_beta=0` after nuisance profiling, independent of exposure/source harmonic balance/covariance.

### RESOURCE-077

For reference Fisher `C_g` in `(g2,g4)`, transform to common/differential coordinates and retain

`C_com=C_cc-C_cd^2/C_dd`.

For SPD `C_g=[[C22,C24],[C24,C44]]`,

`C_com=4 det(C_g)/(C22+C44-2C24)`.

For independent band references,

`C_com=4 C2 C4/(C2+C4)`.

### DESIGN-017

At fixed independent `C2+C4`, balanced gain calibration maximizes `C_com`. A direct common-mode reference may be more efficient and should not be artificially split.

### Exact retained Fisher

If `F_s` is the transfer-fixed science Fisher after spectral-tilt profiling,

`F_beta=F_s C_com/(F_s+C_com)`.

At fixed retention q,

`C_com >= q/(1-q) F_s`.

Thus both Toy009 and Toy014 share the same algebraic common-gain retention coefficient; architecture differences enter through physical science/reference rates, not a different formal kappa.

### RESOURCE-078

For separate science/reference rates,

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

For Toy014/Toy009,

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z_c=R_c09/R_s09`,

`u_DT=[(1+z_c^-1/2)/(s^-1/2+(c z_c)^-1/2)]^2`.

The Iteration-074 equal-ASD science ratio `s=0.28301465746` is retained only as a regression slice, not a physical apparatus result.

## Files

- `analysis/two_band_gain_tilt_quotient_iteration114.py`
- `docs/PAPER_III_TWO_BAND_GAIN_TILT_QUOTIENT_ITERATION114.md`
- `research_log/2026-08-31_iteration_114_two_band_gain_tilt_quotient.md`

## Next gate

Obtain/certify a same-state common-gain quotient rate `R_c` interval from the dual-tone reference likelihood of Iterations 101–103. If source-independent transfer reference is defensible, test `c=1`; otherwise keep `c` interval-valued. Insert `R_DT` into the seven-layer/control scheduler and update the robust detector-side ratio `u`.

Do not invent complex phase stability or SI drift, and do not open Toy015 unless residual dominant uncertainty becomes demonstrably source-dependent.
