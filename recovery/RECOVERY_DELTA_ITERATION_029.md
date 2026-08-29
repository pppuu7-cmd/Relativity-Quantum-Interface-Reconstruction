# RQIR Recovery Delta — Iteration 029

**Date:** 2026-08-29

## New retained result

Iteration 029 closes the abstract D2 resource coordinates of Iteration 028 in terms of native apparatus Fisher rates.

With corrected D2 weights `GM=2.414e6`, `GC=0.929e6`, 14 mean rows and 8 covariance rows, define per-second normalized Fisher rates `q_pot`, `q_force`, `q_cov` and source-preparation Fisher rate `R_P`.

Then

`K_pot=14 GM/q_pot`,

`K_force=14 GM/q_force`,

`K_cov=8 GC/q_cov`,

and therefore

`x=q_pot/q_force`,

`y=0.219907681382 q_pot/q_cov`,

`z=3.3796e7 R_P/q_pot`.

### RQIR-RESOURCE-009 — native-rate closure

The D2 branch phase diagram should now be fed by native measurement Fisher-rate ratios rather than arbitrary normalized calibration times.

Useful exact scales:

- `z=1` at `R_P/q_pot ~=2.95893e-8`;
- `y=1` at `q_cov/q_pot ~=0.2199077`;
- `x=1` exactly when `q_force=q_pot`.

Interpretation: because the corrected 14-row potential bundle requires `3.3796e7` Fisher units at `lambda=1`, independent preparation metrology can be much slower per second than one potential row and still matter strongly in total wall-clock optimization.

## Do not overclaim

This is not an SI-time apparatus forecast. A unique D2 branch winner remains open until one common transduction/noise model supplies `q_pot`, `q_force`, and `q_cov` and the source cycle supplies `R_P`.

Potential and force rows must remain physically distinct; do not assume equal native rates merely because both are gravitational calibration channels.

## Continuation

Next gate: construct one D2 equivalent-force-PSD/source-drive transduction model, including a declared protocol for potential calibration, covariance effective bandwidth/duty, preparation QFI efficiency/cycle, and Iteration-023 timing/reference recertification duty. Propagate uncertainty in those native rates through the Iteration-028 branch boundaries before reporting SI hours.
