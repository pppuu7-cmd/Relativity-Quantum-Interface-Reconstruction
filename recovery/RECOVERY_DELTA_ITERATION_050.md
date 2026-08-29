# RQIR Recovery Delta — Iteration 050

**Date:** 2026-08-29

## New current source-metrology rate model

Iteration 049 finite QND energy pointer:

`y|E_i ~ N(r E_i,1)`, `r=2 sqrt(eta_E kappa_E T_E)`.

Iteration 050 adds fresh-copy preparation/reset overhead `t_reset` through

`delta=4 eta_E kappa_E t_reset`.

The accepted Fisher rate is

`R_E(r)=4 p_E eta_E kappa_E F_alpha(r)/(r^2+delta)`.

Optimize `F_alpha(r)/(r^2+delta)`.

**RQIR-RESOURCE-023:** source reset and measurement strength are coupled resources. Cheap reset favors sub-projective readout; expensive reset shifts the optimum toward projective energy discrimination.

Representative optima:

- `delta=0`: `r*=0.868`, 16.6% projective Fisher/copy;
- `delta=1`: `r*=1.471`, 39.8%;
- `delta=5`: `r*=2.170`, 62.5%;
- `delta=10`: `r*=2.587`, 73.1%;
- `delta=50`: `r*=3.656`, 90.4%.

## Current D2 source-amplitude closure phase diagram

Transparent 100-Hz benchmark (`p_C=.5`, `1 ms` covariance-cycle overhead):

- Branch0 vs best4 boundary:
  `R_E^(alpha)=2.13404e-4 s^-1`;
- best4 vs best5 boundary:
  `R_E^(alpha)=2.93122e-6 s^-1`.

Thus:

- `R_E > 2.134e-4 /s`: Branch0 (no added force-covariance rows) is cheapest;
- `2.93e-6 < R_E < 2.134e-4 /s`: best4 + residual source metrology is cheapest;
- `R_E < 2.93e-6 /s`: best5 becomes cheapest.

At zero reset the Branch0/best4 boundary maps to

`p_E eta_E kappa_E > 0.025804 s^-1`.

## New priority

Abstract `R_P` / projective-copy counting is no longer the dominant uncertainty for source amplitude. Build a minimally physical source realization and estimate actual

`(kappa_E, eta_E, p_E, t_reset)`

or directly `R_E^(alpha)`.

Keep Branch0 and best4 active until this physical source-metrology rate is supplied.

## Files

- `analysis/qnd_energy_pointer_reset_budget_iteration050.py`
- `docs/QND_ENERGY_POINTER_RESET_BUDGET.md`
- `research_log/2026-08-29_iteration_050_qnd_energy_pointer_reset_budget.md`
