# RQIR Recovery Delta — Iteration 048

**Date:** 2026-08-29

## New branch-selection rule

Use explicit energy-basis source-metrology Fisher

`F_E^alpha=0.0093918844`

per accepted plus-branch copy.

At centered `y_ref=-4`, `lambda=1`:

- no extra force-cov rows: `C_alpha*=4.55511` -> `~485.00` energy copies;
- best4: `N4=1.180254e6` covariance trajectories + `~5.33` energy copies;
- best5: `N5=2.135100e6`, `C_alpha*=0`.

Define

`x_E=(p_C eta_C)/(p_E eta_E) * t_E/t_C`.

**RQIR-RESOURCE-021 — explicit source-metrology branch phase diagram**

- `x_E<2460.53`: no-extra-force-cov + energy metrology is cheapest;
- `2460.53<x_E<1.79136e5`: best4 + tiny energy metrology is cheapest;
- `x_E>1.79136e5`: best5 is cheapest.

At equal efficiency, 100 Hz, `1 ms` covariance readout overhead:

- branch0/best4 boundary: `t_E~22.0 s`;
- best4/best5 boundary: `t_E~26.7 min`.

Therefore a physical estimate of energy/population source-metrology cycle time is now higher priority than adding more covariance rows.

## Scope

This phase diagram compares source-amplitude closure strategies only. Mean calibration, controls and science integration common to branches are omitted.

## Next

Build a physical or at least device-class-specific energy/population metrology model and determine whether realistic `t_E,p_E,eta_E` place the current source below or above the ~20-second branch boundary.