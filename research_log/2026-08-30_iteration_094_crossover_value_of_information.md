# RQIR Research Log — Iteration 094

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 093. Quantify which uncertainty in the robust Toy009/Toy014 physical comparison should be characterized first by differentiating the two NG-030 crossover boundaries and the NG-043 unresolved-band width with respect to `A_i`, `R_src,i`, and duty `d_i`.

No closed Paper-I/II gate was reopened and no Toy015 search was started.

## Result

For a robust boundary `B=-D/S`,

`dB=-(1/S)dD+(D/S^2)dS`.

All endpoint sensitivities are therefore analytic. To compare unlike physical coordinates, each interval is parameterized by a common contraction coordinate `eta` that scales its current half-width while holding its midpoint fixed. Define

`Lambda_x=(1/W) dW/deta_x` at the current box.

This is **RQIR-RESOURCE-046** and **RQIR-DESIGN-006**: characterize the apparatus parameter that reduces the robust decision dead zone fastest, rather than ranking measurements by raw percent uncertainty.

## Synthetic regression result

The Iteration-093 synthetic box is reproduced exactly:

- lower boundary `0.025237237237237236`;
- upper boundary `0.08006274509803925`;
- unresolved width `0.05482550786080201`.

Local decision leverage ranking:

1. Toy014 `R_src`: `Lambda=0.51911`;
2. Toy009 `R_src`: `0.42737`;
3. Toy014 `A`: `0.18110`;
4. Toy014 duty: `0.15900`;
5. Toy009 duty: `0.10243`;
6. Toy009 `A`: `0.03528`.

A 50% interval contraction gives the same ordering; source-metrology interval contraction reduces the synthetic dead zone most strongly. These are regression numbers only, not apparatus forecasts.

## New negative/guardrail results

**RQIR-NG-045:** largest raw fractional uncertainty need not have largest architecture-decision value. Crossover sensitivity weights detector/calibration, source rate, and duty differently.

**RQIR-NG-046:** the value-of-information ranking is local to the declared uncertainty set and parameterization. Recompute after substantial characterization changes; correlated uncertainties require a joint uncertainty set rather than independent Cartesian boxes.

## Files

- `analysis/crossover_value_of_information_iteration094.py`
- `docs/PAPER_III_CROSSOVER_VALUE_OF_INFORMATION_ITERATION094.md`
- `recovery/RECOVERY_DELTA_ITERATION_094.md`

## Next gate

Apply RESOURCE-046 to source-specific physical uncertainty inputs rather than the synthetic regression box. The highest-value path is to propagate primitive science/calibration uncertainties (`r2,r4,rho` and seven matrix calibration blocks) and source-metrology/reset/visibility uncertainty into `A_i`, `R_src,i`, and `d_i`, then identify which primitive measurement dominates decision leverage. Do not start Toy015 unless that primitive analysis identifies a genuinely source-dependent bottleneck.
