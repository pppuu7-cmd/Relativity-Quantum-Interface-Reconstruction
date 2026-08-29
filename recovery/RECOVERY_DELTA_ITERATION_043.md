# RQIR Recovery Delta — Iteration 043

**Date:** 2026-08-29

## New retained results

A standard direct diffusive source-monitoring proxy was introduced:

`dy=2 sqrt(eta kappa)<M>dt+dW`, `dot rho=kappa D[M]rho`.

For normalized local mean sensitivity, `I=xi_mu^2=4 eta kappa T`, hence measurement/dephasing strength

`zeta=xi_mu^2/(4 eta)`.

For the same-time normalized Toy009 force operators `M0,M1`:

- hidden-state purity-loss coefficients are `0.00433225` and `0.00130355`;
- at Iteration-041 optimistic shared mean target `xi=1.245286`, `eta=1`, response norm retains `~0.856964` with alignment `~0.998751`;
- at Iteration-042 mean/cov wall-time crossover `xi=2.772804`, `eta=1`, response norm retains only `~0.493450`, alignment `~0.956925`;
- at the same required Fisher, lower efficiency worsens disturbance: retention `~0.42596` at `eta=.8`, `~0.29954` at `.5`, `~0.15771` at `.2`.

## New rules

- **RQIR-NG-020 — direct-monitoring information/backaction obstruction:** resource-competitive mean Fisher is not free in the standard non-QND diffusive source-monitoring class; the current `xi~2.77` benchmark approximately halves the raw D2 ordered-response norm even at ideal efficiency in the simple proxy.
- **RQIR-RESOURCE-018:** measurement efficiency is a coherence/backaction resource as well as a time resource because fixed Fisher requires `zeta proportional 1/eta`.

These are protocol-specific and do not rule out probe-mediated or ancilla-assisted D2 measurements.

## Next

Build a source–probe linear-response detector with explicit imprecision/backaction/cross-noise and propagate it through the profiled Fisher and source-response dynamics.
