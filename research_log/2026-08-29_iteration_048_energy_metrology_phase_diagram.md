# RQIR Research Log — Iteration 048

**Date:** 2026-08-29  
**Target:** replace abstract source-metrology rate in the D2 branch comparison with the concrete energy-basis Fisher from Iteration 047.

## Result

Using `F_E^alpha=0.0093918844` per accepted plus-branch energy-population copy and the centered `y_ref=-4, lambda=1` requirements:

- no extra force-cov rows: `C_alpha*=4.55511` -> `~485.00` energy copies;
- best4 `(0,1,3,7)`: `N4=1.180254e6` covariance trajectories plus `~5.33` energy copies;
- best5 `(0,1,3,6,7)`: `N5=2.135100e6`, no source prior.

Define

`x_E=(p_C eta_C)/(p_E eta_E) * t_E/t_C`.

The lower-envelope branch sequence is:

- `x_E<2460.53`: no-extra-force-cov + energy metrology wins;
- `2460.53<x_E<1.79136e5`: best4 + tiny energy metrology wins;
- `x_E>1.79136e5`: best5 wins.

This is **RQIR-RESOURCE-021 — explicit source-metrology branch phase diagram**.

At equal efficiency, 100 Hz and `1 ms` detector overhead:

- no-extra-cov ↔ best4 crossover: `t_E~22.0 s`;
- best4 ↔ best5 crossover: `t_E~1602 s~26.7 min`.

So if an accepted energy/population metrology cycle is faster than about 22 seconds, even the best-four covariance bundle is not wall-clock optimal for source-amplitude closure in this transparent benchmark.

## Interpretation

The next experiment-design priority is now the physical energy/population metrology rate (`t_E,p_E,eta_E`), not additional covariance geometry. Covariance complementarity remains valuable only when independent source verification is sufficiently slow.

## Files

- `analysis/d2_energy_metrology_phase_diagram_iteration048.py`
- `docs/D2_ENERGY_METROLOGY_PHASE_DIAGRAM.md`
- `recovery/RECOVERY_DELTA_ITERATION_048.md`

## Next gate

Construct a minimally physical energy/population readout model for the five-mode source and estimate its acceptance, efficiency and cycle/reset time relative to the ~20-second branch boundary.