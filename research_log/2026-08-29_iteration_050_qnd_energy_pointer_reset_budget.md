# RQIR Research Log — Iteration 050

**Date:** 2026-08-29  
**Target:** include fresh-source preparation/reset overhead in the finite-strength QND energy-metrology channel and close the D2 branch phase diagram in Fisher/sec.

## Result

With pointer separation

`r=2 sqrt(eta_E kappa_E T_E)`

and reset overhead `t_reset`, define

`delta=4 eta_E kappa_E t_reset`.

The accepted source-metrology Fisher rate is

`R_E(r)=4 p_E eta_E kappa_E F_alpha(r)/(r^2+delta)`.

The optimal pointer strength increases with reset cost:

- `delta=0`: `r*=0.868`, 16.6% projective Fisher/copy;
- `delta=1`: `r*=1.471`, 39.8%;
- `delta=5`: `r*=2.170`, 62.5%;
- `delta=10`: `r*=2.587`, 73.1%;
- `delta=50`: `r*=3.656`, 90.4%.

This gives **RQIR-RESOURCE-023 — source-reset/measurement-strength tradeoff**.

At the transparent 100-Hz D2 benchmark the branch decision is now expressible directly in physical energy-metrology Fisher rate:

- Branch0 wins for `R_E > 2.13404e-4 s^-1`;
- best4 wins for `2.93122e-6 < R_E < 2.13404e-4 s^-1`;
- best5 wins only for `R_E < 2.93122e-6 s^-1`.

At zero reset this first boundary corresponds to

`p_E eta_E kappa_E > 0.025804 s^-1`.

Reset overhead reduces the dimensionless rate coefficient and raises the required measurement rate.

## Files

- `analysis/qnd_energy_pointer_reset_budget_iteration050.py`
- `docs/QND_ENERGY_POINTER_RESET_BUDGET.md`
- `recovery/RECOVERY_DELTA_ITERATION_050.md`

## Next gate

Move from the abstract five-level source to a minimal physical source-realization class and determine achievable `(kappa_E, eta_E, p_E, t_reset)` / `R_E^(alpha)`. Until then Branch0 and best4 both remain active.
