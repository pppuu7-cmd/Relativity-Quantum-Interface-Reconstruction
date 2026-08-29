# RQIR Recovery Delta — Iteration 044

**Date:** 2026-08-29

## New retained gate

**RQIR-NG-021 — reciprocal linear probe shared-copy information/backaction bound**

For reciprocal linear source→probe→detector readout

`x_p=chi_p(g u+F_BA)`, `y=x_p+x_imp`,

and detector noise satisfying

`S_xx S_FF-S_xF^2 >= hbar^2/(4 eta)`,

the source-referred imprecision and reciprocal source backaction satisfy

`S_u S_BA,src >= hbar^2/(4 eta)`.

The coupling `g` and probe susceptibility `chi_p` cancel from this input-referred product. Optimal imprecision/backaction correlation can saturate but not beat the bound.

In the Iteration-043 white-noise convention:

`zeta >= I_mu/(4 eta)`.

Thus ideal reciprocal probe mediation cannot improve the minimum same-copy source dephasing at fixed mean Fisher relative to the direct diffusive-monitor reference. It can still improve technical detector noise or hardware feasibility.

## Current numerical consequence

Using the exact Toy009 dephasing proxy:

- to retain 90% of unperturbed **raw detector signal Fisher**, require response norm `>=sqrt(0.9)`;
- at ideal efficiency this gives `xi_mu<=0.7239817`, `I_mu<=0.5241495` per shared copy;
- current optimistic shared target is `xi_mu=1.245286`, giving raw detector Fisher retention `~0.734388`;
- current mean/covariance wall-time crossover is `xi_mu=2.772804`, giving raw detector Fisher retention `~0.243493`.

Therefore the current same-copy shared mean+covariance strategy cannot preserve a 90% raw detector-Fisher ceiling in the reciprocal linear quantum-limited class.

## Scope

Not a D2 no-go. Independent calibration preparations, QND/backaction-evading or nonreciprocal architectures, ancilla methods or other detector classes remain open.

## Next

Use `I_mu<=0.5241495` as a science-copy mean-information cap and compute the mixed shared+independent calibration schedule. Then propagate the dephasing channel through the full profiled D2 Fisher.