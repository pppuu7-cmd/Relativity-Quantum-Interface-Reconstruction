# RQIR Recovery Delta — Iteration 049

**Date:** 2026-08-29

## New current result

Ideal projective energy-basis source metrology is no longer the only physical model. For finite-resolution QND energy readout use

`y|E_i ~ N(r E_i,1)`, `p_i(alpha)=1/5+0.08 alpha d_i`.

Toy009 hidden direction satisfies exact trace and mean-energy matching:

`sum d_i=0`, `sum E_i d_i=0`.

Therefore weak pointer Fisher begins quartically:

`F_alpha(r) ~= 0.0158603616 r^4`.

**RQIR-NG-024:** exact conserved-moment matching suppresses arbitrarily weak linear energy readout.

Projective plus-branch Fisher remains

`F_E^(alpha)=0.00939188436`.

Finite pointer fractions:

- `r=1`: 21.69%;
- `r=2`: 57.61%;
- `r=3`: 81.39%;
- `r=4`: 93.52%;
- `r=6`: 99.61%.

For `r=2 sqrt(eta_E kappa_E T_E)` and negligible reset overhead,

`R_E=4 p_E eta_E kappa_E F(r)/r^2`.

Maximum rate occurs at

`r*=0.8677465`,

with

`F(r*)=0.0015568125`,

`R_E,max=0.0082700957 p_E eta_E kappa_E`.

**RQIR-RESOURCE-022:** throughput-optimal source metrology can be deliberately nonprojective.

Transparent 100-Hz branch-rate thresholds:

- Branch0 vs best4: `R_E > 2.13404e-4 s^-1` favors Branch0;
- best4 vs best5: `R_E > 2.9312e-6 s^-1` favors best4.

At zero reset overhead the first becomes

`p_E eta_E kappa_E > 0.025804 s^-1`.

## Files

- `analysis/qnd_energy_pointer_fisher_iteration049.py`
- `docs/QND_ENERGY_POINTER_FINITE_STRENGTH.md`
- `research_log/2026-08-29_iteration_049_qnd_energy_pointer_fisher.md`

## Next

Optimize the same pointer with explicit source preparation/reset overhead. Do not use the zero-reset optimum as a hardware forecast.
