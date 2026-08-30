# RQIR Recovery Delta — Iteration 115

**Date:** 2026-08-31  
**Parent front:** Iteration 114.

## New detector/transfer result

The full same-state dual-tone complex transfer likelihood can now be reduced exactly to the single scalar common-gain Fisher rate needed by the two-band science architecture.

For local transfer coordinates

`x=(g2,g4,phi2,phi4)`,

one accepted block has

`F_blk=J_chi^T Sigma_z^-1 J_chi`.

With independent-cycle acceptance `p_cal` and full cycle time `tau_cyc`, use

`K_x=(p_cal/tau_cyc) F_blk`

when rejected cycles carry no usable transfer Fisher.

Transform gains by

`g2=c-d`, `g4=c+d`.

In `y=(c,d,phi2,phi4)`, let nuisance `nu=(d,phi2,phi4)`.

### RESOURCE-079

`R_c = k_cc - k_cnu K_nunu^-1 k_nuc`.

This is the exact full-complex common-gain reference rate. Direct 4D profiling equals phase-first then differential-gain profiling; regression error is `<1.6e-15`.

The phase-free slice recovers Iteration 114:

`R_c=4 det(K_g)/(K22+K44-2K24)`.

## New negative gate

### NG-072 — same hardware != same reference rate

Do not set

`c=R_c14/R_c09=1`

merely because Toy009 and Toy014 are assigned to the same detector hardware.

`c=1` is exact only when their same-state transfer Fisher-rate matrices are equal in the same coordinates, including transfer Jacobian, covariance, acquisition window, cycle duration, acceptance/reset/readout, feedback/trap/detector state and included nuisance priors.

## Robust matrix certificate

RESOURCE-079 is homogeneous and Loewner-monotone.

If

`m_i K0 <= K_i <= M_i K0`,

then

`m_i R_c0 <= R_c,i <= M_i R_c0`.

### RESOURCE-080

For Toy014/Toy009,

`c in [m14/M09, M14/m09]`.

This propagates correlated full-complex calibration uncertainty without arbitrary independent amplitude/phase error bars.

## Detector+transfer propagation

With

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z=R_c09/R_s09`,

`u_DT=[(1+z^-1/2)/(s^-1/2+(c z)^-1/2)]^2`.

### RESOURCE-081

For interval-valued `(s,c,z)`, the robust enclosure is attained at box corners; there is no hidden interior extremum.

Stored dimensionless regression box:

`s=[0.25,0.35]`, `c=[0.8,1.25]`, `z=[0.05,20]`

produces

`u_DT in [0.2957458954,0.9247878849]`.

Not an apparatus forecast.

## Identifiability guards retained

- detector inference remains `F_beta|theta`;
- NG-005 source-preparation self-calibration obstruction remains active;
- transfer calibration does not replace independent source metrology;
- free gains still erase common-amplitude science;
- D1/D2 transfer/noise likelihoods are not interchangeable;
- no new-physics claim.

## Files

- `analysis/full_complex_common_gain_rate_iteration115.py`
- `docs/PAPER_III_FULL_COMPLEX_COMMON_GAIN_RATE_CERTIFICATE_ITERATION115.md`
- `research_log/2026-08-31_iteration_115_full_complex_common_gain_rate.md`
- `recovery/RECOVERY_DELTA_ITERATION_115.md`

## Next gate

Insert RESOURCE-079/080 into the seven-layer physical campaign scheduler without double-counting shared calibration blocks. If dual-tone blocks carry Fisher jointly for transfer and calibration-layer nuisances, credit the full joint matrix once through RESOURCE-057/064. If blocks are non-overlapping pure-dead references, use Iterations 107–112 recertification overhead. Then produce the first full robust Toy014/Toy009 detector-side `u` interval including common-gain transfer.
