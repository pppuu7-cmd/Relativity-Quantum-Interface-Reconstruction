# RQIR Recovery Delta — Iteration 087

**Date:** 2026-08-30  
**Authority:** read after Iteration 086.

## New retained result

For the correlated two-band likelihood

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`,

with independent uncertainty intervals

`r2 in [r2_lo,r2_hi]`,

`r4 in [r4_lo,r4_hi]`,

`rho in [rho_lo,rho_hi]`,

the exact conservative lower bound is obtained at `rho=rho_hi` and one of the four rate corners.

### RQIR-RESOURCE-040

`R_beta^lower = min_{r2 endpoints, r4 endpoints} R_beta(r2,r4,rho_hi)`.

No Monte Carlo is required for this box-uncertainty model.

### RQIR-NG-037

Nominal negative cross-correlation is not robust resource credit unless the **upper** uncertainty bound on correlation remains sufficiently negative. If the allowed interval crosses zero, the conservative science rate can lose much of the nominal anti-correlation enhancement.

For NG-030 use

`T_sci^upper = Z^2/R_beta^lower`.

Then combine with lower bounds on all seven calibration rates, lower source-metrology rate, and upper control/reference duty.

## Reproduce

- `analysis/correlated_box_uncertainty_iteration087.py`
- `docs/PAPER_III_CORRELATED_BOX_UNCERTAINTY_ITERATION087.md`
- `research_log/2026-08-30_iteration_087_correlated_box_uncertainty.md`

## Next admissible gate

Propagate the same uncertainty-safe construction through the seven same-time dual-probe calibration layers to obtain conservative `R_cal,j^lower`, `H_cal^lower`, and calibration wall-clock upper bounds before evaluating Toy009/Toy014 NG-030 dominance.
