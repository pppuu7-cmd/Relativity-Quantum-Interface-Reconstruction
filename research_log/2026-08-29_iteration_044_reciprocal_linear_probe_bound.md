# RQIR Research Log — Iteration 044

**Date:** 2026-08-29  
**Target:** replace the direct-source-monitor proxy with a minimal reciprocal source→probe→detector linear-response class and determine whether probe gain/susceptibility can evade the information/backaction cost.

## Result

For

`x_p=chi_p(g u+F_BA)`, `y=x_p+x_imp`,

with detector quantum noise

`S_xx S_FF-S_xF^2 >= hbar^2/(4 eta)`,

the source-referred measurement noise and source backaction obey

`S_u S_BA,src >= hbar^2/(4 eta)`.

The source-probe gain `g` and susceptibility `chi_p` cancel from the input-referred product. Optimal imprecision/backaction correlation can saturate but not beat it.

In the Iteration-043 white-noise convention this becomes

`zeta >= I_u/(4 eta)`.

This is **RQIR-NG-021**: reciprocal linear probe mediation does not provide a free same-copy information/backaction advantage over the ideal direct diffusive monitor. It may improve technical noise, but not the quantum-limited reciprocal product.

## Toy009 consequence

Using the exact Iteration-043 dephasing map, retaining 90% of unperturbed raw detector signal Fisher requires response-norm retention `sqrt(0.9)` and hence, at `eta=1`,

`xi_mu <= 0.7239817`, i.e. `I_mu <= 0.5241495` per shared source copy.

Current resource targets are larger:

- optimistic best4-covariance shared target `xi_mu=1.245286` -> response norm `0.856964`, raw detector signal Fisher retention `~0.734388`;
- mean/covariance wall-time crossover `xi_mu=2.772804` -> response norm `0.493450`, raw detector signal Fisher retention `~0.243493`.

Thus the current same-copy shared-trajectory idea cannot simultaneously supply its target mean Fisher and preserve a 90% raw detector-Fisher ceiling within the reciprocal linear quantum-limited class.

## Important scope

This does not rule out D2. Independent/sacrificial calibration copies, QND/backaction-evading variables, nonreciprocity, coherent noise cancellation, ancilla protocols or another detector class can alter the conclusion. Such a proposal must explicitly identify which assumption of RQIR-NG-021 it changes.

## Files

- `analysis/d2_reciprocal_linear_probe_bound_iteration044.py`
- `docs/D2_RECIPROCAL_LINEAR_PROBE_BOUND.md`
- `recovery/RECOVERY_DELTA_ITERATION_044.md`

## Next gate

Convert the 90%-Fisher-compatible per-copy cap `I_mu<=0.5241495` into a mixed campaign: credit only that much mean Fisher to each best4 covariance/science trajectory and compute the remaining independent time-layer calibration burden. Then propagate the backaction map through the full hard-constrained profiled D2 Fisher rather than using only raw signal attenuation.