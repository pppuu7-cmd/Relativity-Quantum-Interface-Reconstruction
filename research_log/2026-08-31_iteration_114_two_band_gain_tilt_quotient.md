# RQIR Research Log — Iteration 114

**Date:** 2026-08-31

## Goal

Use the existing mature two-real-band D2 likelihood to make the Iteration-113 science-coupled transfer mode source-specific without inventing a full complex apparatus Jacobian.

## Exact score quotient

For science amplitudes `s=(s2,s4)`,

- beta score: `(s2,s4)`;
- spectral-tilt score: `(-s2,s4)`;
- fractional gain scores: `(s2,0)` and `(0,s4)`.

With `g2=c-d`, `g4=c+d`,

- common-gain score `v_c=v_beta`;
- differential-gain score `v_d=v_tilt`.

Therefore free per-band gains exactly span the beta+tilt science score space.

### NG-071

With both band gains unconstrained, `F_beta=0` irrespective of exposure/source harmonic balance/detector covariance. Source design cannot remove the common-gain degeneracy in this likelihood.

## Common-gain quotient Fisher

For gain-reference Fisher `C_g` in `(g2,g4)`, transform to common/differential coordinates. After profiling differential gain,

`RESOURCE-077:`

`C_com=C_cc-C_cd^2/C_dd`.

For SPD `C_g=[[C22,C24],[C24,C44]]`,

`C_com=4 det(C_g)/(C22+C44-2C24)`.

For independent references `diag(C2,C4)`,

`C_com=4 C2 C4/(C2+C4)`.

At fixed `C2+C4`, this is maximized by balanced independent allocation.

### DESIGN-017

Balance independent dual-band transfer Fisher unless a direct common-mode reference exists.

## Exact retained beta Fisher

Let `F_s` be the transfer-fixed science Fisher after profiling spectral tilt. Then the full `(beta,g2,g4,tilt)` profile reduces exactly to

`F_beta=F_s C_com/(F_s+C_com)`.

The deterministic script verifies the reduction over 300 random SPD science/reference problems.

At fixed retention q,

`C_com >= q/(1-q) F_s`.

At q=.9, the ratio is 9. For final `F*=25` at q=.9, `F_s=27.7777778` and `C_com=250`.

## Rate closure

For separate science/reference times,

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

For Toy014/Toy009, with

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z_c=R_c09/R_s09`,

`RESOURCE-078:`

`u_DT=[(1+z_c^-1/2)/(s^-1/2+(c z_c)^-1/2)]^2`.

Using only the Iteration-074 equal-ASD science-ratio regression `s=0.28301465746` and illustrative `c=1` gives

- z_c=.01 -> u_DT=.85738;
- .1 -> .68148;
- 1 -> .48234;
- 10 -> .35926;
- 100 -> .30873.

These are not apparatus forecasts. They show that a common slow transfer reference compresses the science-only architecture difference, while a very fast reference restores the science ratio.

## Next gate

Certify the physical/common-coordinate `R_c` interval from the same-state dual-tone reference likelihood. Keep complex phase drift symbolic until a physical stability process exists. Then propagate `R_DT` into the seven-layer/control scheduler and the robust detector ratio `u`.
