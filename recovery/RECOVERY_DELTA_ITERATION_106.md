# RQIR Recovery Delta — Iteration 106

**Date:** 2026-08-30  
**Parent front:** Iteration 105.

## What changed

Paper III now has a rigorous way to bound the missing detector-side architecture ratio

`u=R_D,14/R_D,09`

without fabricating an absolute ASD.

### RESOURCE-062 — Fisher-matrix Loewner ratio certificate

For common-coordinate campaign Fisher-rate matrices, if uniformly over campaigns and apparatus uncertainty

`alpha J_09,k <= J_14,k <= beta J_09,k`

and the feasible campaign-fraction set is common, then after full profiled-Fisher schedule optimization

`alpha <= u <= beta`.

For positive-definite reference matrices, obtain tight per-campaign bounds from generalized eigenvalues. Singular supports must be audited explicitly.

### NG-061

Scalar subsystem ratios do not certify `u`. Nuisance orientation, Fisher support and scheduling constraints matter. Use the full common-coordinate matrix schedule or a valid Loewner sandwich.

### NG-062 — detector no-rescue condition

With Iteration-105 variables `(u,v,z,delta)`, the `u -> infinity` final-rate ratio is

`G_inf=delta v (1+sqrt(z))^2`.

If

`delta v (1+sqrt(z))^2 <= 1`,

Toy014 cannot beat Toy009 for any finite positive detector-side ratio `u` in the separable final-significance model.

Otherwise the required detector ratio is

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

### RESOURCE-063 — independent-box final architecture certificate

For independent positive intervals in `(u,v,z,delta)`, exact lower/upper `Q14/Q09` endpoints follow from monotonicity in `u,v,delta` and the sign-controlled `z` monotonicity from Iteration 105. Use NG-030 on these bounds.

Correlated physical uncertainties must use their joint set.

## Regression

Synthetic common-coordinate campaign matrices:

- generalized-eigenvalue envelope `alpha=0.55`, `beta=1.40`;
- direct optimized ratio `u=0.6172845158`, inside the certified envelope.

The script also reproduces the Iteration-105 crossover and checks the box extrema against brute Cartesian corners.

## Files

- `analysis/detector_ratio_certificate_iteration106.py`
- `docs/PAPER_III_DETECTOR_RATIO_CERTIFICATE_ITERATION106.md`
- `research_log/2026-08-30_iteration_106_detector_ratio_certificate.md`

## Next admissible gate

Promote timing/geometry/additive/gain recertification from a scalar duty multiplier to explicit minimum-fraction / periodic schedule constraints. Derive the constrained detector-side optimum and corresponding robust `u` bounds for Toy009/Toy014. Do not open Toy015 yet.
