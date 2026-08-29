# RQIR Research Log — Iteration 043

**Date:** 2026-08-29  
**Target:** test whether the mean Fisher needed by Iteration 042 can be treated as free in a shared quantum-source trajectory.

## Proxy model

Use the standard ideal diffusive measurement class

`dy=2 sqrt(eta kappa)<M>dt+dW`,

`dot rho=kappa D[M]rho`.

For a normalized local mean coordinate with `d<M>/du=1`,

`I_u=4 eta kappa T=xi_mu^2`, so `zeta=kappa T=xi_mu^2/(4 eta)`.

The same-time normalized force observables `M0,M1` commute and are applied as parallel dephasing channels.

## Results

Current Toy009 hidden-state purity-loss coefficients:

- `||[M0,rho]||_F^2 ~=0.00433225`;
- `||[M1,rho]||_F^2 ~=0.00130355`.

At the optimistic Iteration-041 shared-cycle mean target `xi_mu=1.245286`, `eta=1`:

- `zeta=0.387685`;
- D2 ordered-response norm retention `~0.856964`;
- signal-direction alignment `~0.998751`.

At the Iteration-042 mean-vs-covariance wall-time crossover `xi_mu=2.772804`, `eta=1`:

- `zeta=1.922111`;
- response-norm retention `~0.493450`;
- alignment `~0.956925`.

At fixed `xi_mu=2.772804`, efficiency penalties are severe:

- `eta=0.8`: response retention `~0.42596`;
- `eta=0.5`: `~0.29954`;
- `eta=0.2`: `~0.15771`.

## New retained rules

**RQIR-NG-020 — direct-monitoring information/backaction obstruction:** in the standard diffusive direct-source measurement class, resource-competitive mean Fisher for the current non-QND force observables entails non-negligible source dephasing; at the `xi~2.77` benchmark the raw ordered-response norm is approximately halved even at ideal efficiency in the simple parallel-force proxy.

**RQIR-RESOURCE-018:** measurement efficiency is also a coherence/backaction resource in a shared quantum-source trajectory because fixed Fisher requires `zeta proportional 1/eta`.

These are protocol-specific bounds, not a no-go for probe-mediated D2 architectures.

## Files

- `analysis/d2_information_backaction_proxy_iteration043.py`
- `docs/D2_INFORMATION_BACKACTION_PROXY.md`
- `recovery/RECOVERY_DELTA_ITERATION_043.md`

## Next gate

Build an explicit source–probe linear-response detector model with imprecision/backaction/cross-noise satisfying a quantum noise inequality; derive detector mean/covariance Fisher and propagate source disturbance through the full profiled `F_beta|theta`.
