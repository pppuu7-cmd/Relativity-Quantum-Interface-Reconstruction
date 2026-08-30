# RQIR Recovery Delta — Iteration 103

**Date:** 2026-08-30  
**Parent front:** Iteration 102.

## What changed

The balanced scalar science/transfer split has been generalized to the full four-real-component temporal `f,2f` likelihood and an arbitrary set of science/calibration campaigns.

For campaign Fisher-rate matrices `J_k` and times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`F_beta=a-b^T N^-1 b`.

### New labels

- **RQIR-RESOURCE-057 — campaign-simplex theorem:** `F_beta(t)` is concave and positively homogeneous on an identifiable branch. The minimum-time target problem is convex. With campaign fractions `x`,

  `R_*=max_{x>=0,sum x=1} F_beta(sum x_k J_k)`,

  `T_min=Z^2/R_*`.

- **RQIR-RESOURCE-058 — equal marginal profiled-Fisher rule:** with `q=N^-1b`, `w=(1,-q)`,

  `dF_beta/dt_k=w^T J_k w`.

  Every active campaign at an interior optimum has this marginal rate equal to `R_*`; inactive campaigns have no larger marginal value.

- **RQIR-NG-058 — phase calibration is Fisher-metric dependent:** Euclidean quadrature orthogonality does not justify dropping transfer phase. Require `s_beta^T W p_n=0` after the declared whitening/nuisance projection; otherwise phase calibration can affect `F_beta|theta`.

## Full-complex checks

The deterministic four-real regression preserves NG-056: free independent complex transfer gains erase common-amplitude science Fisher. Same-state transfer Fisher restores positive information.

A non-isotropic positive-definite precision matrix produces nonzero beta/phase couplings despite exact unweighted amplitude/phase orthogonality.

## Scheduling regression

A symmetric `m=8`, `c=8` calibration model has exact optimal fractions

- science `0.5`;
- each of eight calibrations `0.0625`;
- optimized profiled Fisher rate `2`;
- `Z=5` regression total time `12.5` arbitrary units.

All nine active campaign marginal profile-Fisher rates equal `2`.

## Files

- `analysis/full_complex_campaign_allocation_iteration103.py`
- `docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md`
- `research_log/2026-08-30_iteration_103_full_complex_campaign_allocation.md`

## Next admissible gate

Construct the robust max-min campaign allocation over temporal PSD/cross-PSD, transfer and calibration-rate uncertainty. Then add the already physical source-metrology rate and control/reference duty, and apply the same robust scheduler to Toy009/Toy014. Do not open Toy015 unless the resulting dominant marginal resource is source-dependent.
