# RQIR Research Log — Iteration 103

**Date:** 2026-08-30

## Goal

Continue Paper III from authoritative Iteration 102 without reopening Paper I/II and without starting Toy015. Remove the balanced scalar transfer simplification and solve the full complex `f,2f` science/transfer/seven-calibration scheduling problem at the Fisher-matrix level.

## Main result

For campaign Fisher-rate matrices `J_k>=0` and times `t_k>=0`, let

`J(t)=sum_k t_k J_k = [[a,b^T],[b,N]]`.

The retained detector-level information is

`F_beta=a-b^T N^-1 b`.

This function is concave and positively homogeneous in campaign time. Therefore

`min sum t_k  subject to F_beta>=Z^2`

is convex.

Equivalently maximize `F_beta` over campaign fractions `x_k` on the simplex. If

`R_*=max_x F_beta(sum x_k J_k)`,

then

`T_min=Z^2/R_*`.

Registered as **RQIR-RESOURCE-057**.

## Exact marginal certificate

With

`q=N^-1 b`, `w=(1,-q)`,

an additional second of campaign `k` changes retained Fisher at rate

`partial F_beta/partial t_k = w^T J_k w`.

At an interior optimum all active campaigns have the same marginal retained science Fisher rate, equal to `R_*`; inactive campaigns have no larger marginal value.

Registered as **RQIR-RESOURCE-058**.

This unifies Iteration-102 science/transfer allocation and Iteration-097 water-filling at the full Fisher-matrix level.

## Full complex `f,2f` regression

The science data are represented by four real quadratures `(Re z_f, Im z_f, Re z_2f, Im z_2f)`. Local transfer nuisance includes amplitude and phase for both bands plus spectral tilt.

The regression confirms:

- free independent complex transfer gains erase common-amplitude `beta` Fisher (`~0`), reproducing NG-056 in the four-real representation;
- positive same-state transfer-injection Fisher restores positive `beta` information;
- Euclidean amplitude/phase orthogonality is insufficient under a general precision matrix.

A positive-definite non-isotropic regression metric gives phase couplings approximately `0.104` and `-0.0312` despite exact unweighted quadrature orthogonality.

Registered as **RQIR-NG-058**: transfer phase can be omitted only after Fisher-metric orthogonality is explicitly certified.

## Symmetric multi-calibration regression

For `m=8` nuisance gains and calibration rate `c=8`, the exact optimal unit-time fractions are

- science `x_s=0.5`;
- each calibration `x_c=0.0625`;
- optimized retained Fisher rate `R_*=2`.

All nine active campaigns have marginal profiled rate exactly `2`. For the regression target `Z=5`, total time is `12.5` arbitrary units.

This is an algebra check, not an apparatus forecast.

## Files

- `analysis/full_complex_campaign_allocation_iteration103.py`
- `docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md`
- `recovery/RECOVERY_DELTA_ITERATION_103.md`

## Next gate

Build the robust max-min version with temporal PSD/cross-PSD uncertainty and physical rate intervals; then add independent source-metrology throughput and control/reference duty. Apply the same robust scheduler to Toy009 and Toy014 before any Toy015 search.
