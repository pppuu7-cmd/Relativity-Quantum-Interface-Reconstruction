# RQIR Research Log — Iteration 069

**Date:** 2026-08-30

## What was done

Continued from the confirmed Iteration-068 front. Did not reopen active/closed Toy searches. Closed the next acquisition-likelihood gate for D2 mean calibration: the two same-time probe channels in each of the seven compatible layers are now treated with a full `2x2` Gaussian Fisher block / PSD matrix rather than as two independent scalar SNRs.

## Main result

For one layer,

`F_j = 4 Re int J_j(f)^dagger S_j(f)^(-1) J_j(f) df`.

Therefore cross spectra/covariances are part of the calibration likelihood and must be retained when translating `gamma_mean` into shots or seconds.

### RQIR-CAL-016

Same-time dual-probe Fisher cannot in general be obtained by adding two scalar `SNR^2` values. Use the full matrix PSD/covariance likelihood.

### RQIR-RESOURCE-031

For the exact symmetric white benchmark

`C=[[1,rho],[rho,1]]`, `J=xi I`,

Fisher eigenvalues are

`xi^2/(1+|rho|)` and `xi^2/(1-|rho|)`.

If at least `gamma` information is required in every two-row direction, the robust accepted-cycle requirement is

`N_layer >= gamma (1+|rho|)/xi^2`.

Thus the correlation inflation relative to the independent limit is exactly `1+|rho|` in this benchmark.

## Numerical regression

At `xi=3`:

- Toy009, 7 layers, `rho=0`: `1,423,539.213` accepted layer-cycles;
- Toy009, `rho=0.5`: `2,135,308.820`;
- Toy009, `rho=0.9`: `2,704,724.506`;
- Toy012, `rho=0`: `940,089.500` accepted layer-cycles.

At the retained lower-bound schedule (`100 Hz`, `p=0.5`, `1 ms` dead/readout):

- Toy009 `rho=0`: `5.00946094 h`;
- Toy009 `rho=0.5`: `7.51419141 h`;
- Toy009 `rho=0.9`: `9.51797579 h`;
- Toy012 `rho=0`: `2.89133490 h`.

These are not apparatus forecasts; physical transduction, colored PSD, cross spectrum, preparation/reset and drift remain open.

## Gates retained

NG-005, NG-006, NG-023, NG-026, NG-027 and all relativistic/full-QFT/classical/stochastic consistency and degeneracy gates remain active. No new-physics claim.

## Reproducibility

- `analysis/d2_dual_probe_matrix_fisher_iteration069.py`
- `docs/D2_DUAL_PROBE_MATRIX_FISHER_ITERATION069.md`

## Next

Insert one declared physical D2 transduction Jacobian and one-sided `2x2` equivalent-force/output PSD matrix, including cross spectrum, and integrate all seven same-time Fisher blocks. Use their detector-relevant minimum eigenvalues to obtain apparatus-specific `T_cal/T_sci`, then combine with source-metrology `T_src/T_sci` and re-test the Toy009/Toy013 dominance boundary.
