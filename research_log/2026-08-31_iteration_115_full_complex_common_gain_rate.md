# RQIR Research Log — Iteration 115

**Date:** 2026-08-31

## Goal

Continue from authoritative Iteration 114 without redoing the already-closed physical translation of `C_a` and `gamma`. The active Paper-III gate was to turn the same-state dual-tone transfer likelihood of Iterations 101–103 into the physical scalar common-gain rate `R_c` required by the Toy009/Toy014 architecture quotient.

## Required baseline re-read

Before advancing, re-read:

- `docs/RECOVERY_GUIDE.md`;
- `docs/MASTER_TABLE.md`;
- `recovery/CURRENT_FRONT.md`;
- latest Iteration-114 research log;
- `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`;
- `docs/TOY_MODEL_010_CALIBRATION_GEOMETRY_COOPTIMIZATION.md`;
- `docs/STATISTICAL_IDENTIFIABILITY.md`;
- `docs/STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`;
- Iterations 101–102 same-state transfer likelihood/profile documents.

Confirmed mature guards: detector-level `F_beta|theta`, NG-005 source-amplitude obstruction, independent source-preparation metrology, transfer-gain degeneracy, covariance profiling and no RTK/DSIR mixing.

## Main result

For full local transfer coordinates

`x=(g2,g4,phi2,phi4)`,

one accepted same-state dual-tone block has

`F_blk=J_chi^T Sigma_z^-1 J_chi`.

For independent cycles with acceptance `p_cal` and full cycle time `tau_cyc`, the physical Fisher-rate matrix is

`K_x=(p_cal/tau_cyc) F_blk`

when rejected cycles carry zero usable transfer information.

Transform gains via

`g2=c-d`, `g4=c+d`.

In coordinates `y=(c,d,phi2,phi4)`, write

`K_y=[[k_cc,k_cnu],[k_nuc,K_nunu]]`, `nu=(d,phi2,phi4)`.

### RESOURCE-079

The exact science-relevant common-gain reference rate is

`R_c=k_cc-k_cnu K_nunu^-1 k_nuc`.

Direct profiling of all three nuisance coordinates equals phase-first then differential-gain profiling. A deterministic 1000-matrix regression gives maximum relative discrepancy `<1.6e-15`.

The phase-free two-gain slice exactly recovers Iteration 114:

`R_c=4 det(K_g)/(K22+K44-2K24)`.

## Source-independence gate

If Toy009 and Toy014 have exactly the same same-state transfer Fisher-rate matrix in the same coordinates, then

`c=R_c14/R_c09=1`.

### NG-072

Using the same hardware does not by itself license `c=1`. Equality must include the transfer Jacobian, same-block covariance, window, cycle time, acceptance/reset, feedback/trap/detector state and nuisance priors. Otherwise `c` remains measured/interval-valued.

## Robust matrix-to-scalar certificate

`R_c` is homogeneous and Loewner-monotone. If

`m_i K0 <= K_i <= M_i K0`,

then

`m_i R_c0 <= R_c,i <= M_i R_c0`.

### RESOURCE-080

For Toy014/Toy009,

`c in [m14/M09, M14/m09]`.

This allows a full correlated 4D transfer Fisher uncertainty envelope to enter the architecture decision without independent amplitude/phase tolerances.

## Propagation to detector+transfer ratio

With

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z=R_c09/R_s09`,

Iteration 114 gives

`u_DT=[(1+z^-1/2)/(s^-1/2+(c z)^-1/2)]^2`.

### RESOURCE-081

A rectangular uncertainty box in `(s,c,z)` has no hidden interior extremum; evaluate its eight corners.

Regression-only box

`s=[0.25,0.35]`, `c=[0.8,1.25]`, `z=[0.05,20]`

gives

`u_DT in [0.2957458954,0.9247878849]`.

These numbers test the algebra only and are not apparatus predictions.

## Consistency / identifiability status

- NG-005 remains fully active: transfer references do not calibrate the hidden source-preparation amplitude.
- Free gains still erase beta information; RESOURCE-079 is the independent-reference repair, not an assumption.
- D1 and D2 require their own physical transfer/noise likelihoods.
- No new-physics claim is made.

## Reproducibility

- `analysis/full_complex_common_gain_rate_iteration115.py`
- `docs/PAPER_III_FULL_COMPLEX_COMMON_GAIN_RATE_CERTIFICATE_ITERATION115.md`

## Next gate

Insert the full-complex transfer rate block into the seven-layer campaign scheduler. Determine whether the same physical dual-tone acquisition carries joint Fisher for transfer plus any calibration-layer coordinates; if so, credit that block once through RESOURCE-057/064. Otherwise treat non-overlapping reference blocks through the recertification overhead formalism. The target is a non-double-counted robust interval for the full detector-side Toy014/Toy009 ratio `u`.
