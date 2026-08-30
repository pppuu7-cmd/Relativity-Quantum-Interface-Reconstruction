# RQIR Recovery Delta — Iteration 069

**Date:** 2026-08-30  
**Parent front:** Iteration 068 physical Fisher-rate closure

## New retained result

Iteration 069 closes the next D2 mean-calibration acquisition-likelihood gate. The seven compatible same-time dual-probe layers must be treated with full two-output Fisher blocks, not two independent scalar SNRs.

For layer `j`:

`F_j = 4 Re int J_j(f)^dagger S_j(f)^(-1) J_j(f) df`,

with full `2x2` one-sided output/equivalent-force PSD matrix `S_j`, including cross spectrum.

### RQIR-CAL-016

Independent addition of two same-time probe `SNR^2` values is valid only when the declared cross covariance/spectrum is negligible. Otherwise use the matrix likelihood.

### RQIR-RESOURCE-031

For the exact symmetric benchmark

`C=[[1,rho],[rho,1]]`, `J=xi I`,

the Fisher eigenvalues are

`lambda_min=xi^2/(1+|rho|)`,

`lambda_max=xi^2/(1-|rho|)`.

A robust isotropic target `gamma` therefore requires

`N_layer >= gamma (1+|rho|)/xi^2`.

This is an exact benchmark correlation penalty, not an apparatus forecast.

## Regressions

At `xi=3`:

- Toy009 `rho=0`, seven layers: `1,423,539.213` accepted layer-cycles;
- Toy009 `rho=0.5`: `2,135,308.820`;
- Toy009 `rho=0.9`: `2,704,724.506`;
- Toy012 `rho=0`: `940,089.500`.

At `100 Hz`, `p=.5`, `1 ms` dead/readout:

- Toy009 `rho=0`: `5.00946094 h`;
- Toy009 `rho=.5`: `7.51419141 h`;
- Toy009 `rho=.9`: `9.51797579 h`;
- Toy012 `rho=0`: `2.89133490 h`.

The `rho=0` Toy009 count exactly reproduces the earlier independent-channel budget, so this iteration is a strict generalization rather than a changed baseline.

## Do not forget

- `alpha_h` is hidden source-preparation amplitude; `epsilon_drv` is pump/drive amplitude.
- NG-005 remains: gravitational exact-null calibration cannot self-calibrate `alpha_h`.
- Same-time dual probes are the maximal disturbance-free grouping; cross-time force means remain separate campaigns unless one physical likelihood with backaction proves otherwise.
- `gamma_mean` becomes an apparatus-specific time only after a physical transduction Jacobian, PSD/cross-PSD, acceptance, bandwidth/window and cycle duration are specified.
- No new-physics claim.

## Reproducibility

- `analysis/d2_dual_probe_matrix_fisher_iteration069.py`
- `docs/D2_DUAL_PROBE_MATRIX_FISHER_ITERATION069.md`
- `research_log/2026-08-30_iteration_069_d2_dual_probe_matrix_fisher.md`

## Next admissible gate

Choose one declared physical D2 transduction/noise model and compute all seven integrated `2x2` Fisher blocks. From those obtain apparatus-consistent `x=T_cal/T_sci`; combine with source-metrology `y=T_src/T_sci`; only then re-test the Toy009/Toy013 wall-clock dominance boundary.
