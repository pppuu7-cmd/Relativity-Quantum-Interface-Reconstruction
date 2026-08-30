# RQIR Research Log — Iteration 095

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 094 without reopening Paper I/II or starting Toy015. Expand the aggregate crossover value-of-information variables `A_i` and `R_src,i` to experimentally measurable primitive inputs.

## Result

Derived the exact local primitive decision Jacobian.

For two-band science,

`A_sci = Z^2[1/(4a2)+1/(4a4)+rho/(2 sqrt(a2 a4))]`,

with analytic derivatives in `a2,a4,rho`.

For each same-time dual-probe calibration block `F_j=[[u,w],[w,v]]`, derived the exact `lambda_min` matrix-entry gradient and propagated it through

`A_cal=gamma sum_j 1/k_j`.

This yields **RQIR-DESIGN-007**: for equal fractional rate improvements, the slowest calibration layer (`min k_j`, largest `gamma/k_j`) has the largest first-order reduction of calibration wall time.

For source metrology, wrote

`R_src=p_E Omega_E q(V,Omega_E t_reset)`

and derived the smooth-branch derivatives with respect to preparation success, coupling, reset time and visibility. These compose directly with RESOURCE-046's outer crossover derivative.

## New guardrails

- **RQIR-NG-047:** under negative cross-correlation, increasing one raw band rate is not globally monotone useful after nuisance profiling. The derivative changes sign at `a2/a4=1/rho^2`, reproducing CORR-001 locally.
- **RQIR-NG-048:** primitive local VOI is invalid at repeated calibration eigenvalues, PSD-boundary contact, worst-case corner changes or robust-boundary active-set changes; exact finite contractions/subgradient/robust optimization must then replace the ordinary derivative.

## Numerical regression

The new deterministic script compares all analytic derivatives against central finite differences.

At synthetic `(a2,a4,rho)=(1.2,0.8,-0.3)`:

- `dA/da2=-2.74555789315`;
- `dA/da4=-7.37354517306`;
- `dA/drho=12.7577590770`.

For synthetic calibration block `(u,v,w)=(1.5,2.2,0.3)`:

- `dlambda/du=0.879628301183`;
- `dlambda/dv=0.120371698817`;
- `dlambda/dw=-0.650791373456`.

The outer crossover chain rule and source-rate primitive derivatives also agree with finite differences. The anti-correlation sign-flip threshold is reproduced exactly for `rho=-0.5`, `a4=1`: `a2=4`.

These numbers are regression checks only, not apparatus forecasts.

## Files

- `analysis/primitive_decision_jacobian_iteration095.py`
- `docs/PAPER_III_PRIMITIVE_DECISION_JACOBIAN_ITERATION095.md`
- `recovery/RECOVERY_DELTA_ITERATION_095.md`

## Next gate

Construct one declared primitive uncertainty envelope for Toy009 and Toy014: `a2,a4,rho`, all seven `2x2` calibration blocks, Ramsey preparation/coupling/reset/visibility, and duty. Propagate it through the Iteration-095 Jacobian and exact nonsmooth guards, then identify the actual highest-value characterization measurement by contraction of the NG-043 unresolved band. Do not start Toy015 unless the resulting bottleneck is demonstrably source-dependent.
