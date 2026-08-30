# RQIR Recovery Delta — Iteration 068

**Date:** 2026-08-30  
**Continue from:** Iteration 067 detector-cycle/SNR bridge.

## New retained results

1. **RQIR-NUM-004 — notation/coordinate separation.**
   - `alpha_h`: fractional hidden-source preparation amplitude, with `a=0.08 alpha_h`.
   - `epsilon_drv`: pump/drive impulse area formerly also denoted `alpha` in Protocol 002B.
   - D2 cycle leverage: `q_drv=2|epsilon_drv|Gamma_G/sigma_phi`.
   - Local science model: `mu_D ~ beta alpha_h epsilon_drv s`.
   - NG-005 remains unchanged because beta and alpha_h are still locally collinear in the science signal.

2. **Absolute source-preparation Fisher target.**
   For isolated beta/alpha_h degeneracy,
   `C_prep=[r/(1-r)] S`, where `S` is raw detector Fisher in the same physical coordinate.
   At `Delta beta=1`, `Z=5`, `r=0.90`: `S=25`, `C_prep=225`.

   Toy009 accepted-copy lower bounds:
   - energy-population readout (`F_E^alpha=0.0093918844`): `23956.85364` copies;
   - full ideal QFI ceiling (`F_Q^alpha=0.0849323916`): `2649.165951` copies.
   At acceptance 0.5, attempts are `47913.71` and `5298.33` respectively, before reset/readout/systematics.

3. **RQIR-RESOURCE-030 — physical Fisher-rate closure of gamma.**
   For row-normalized calibration coordinate `u_j`, physical template `h_j` and one-sided output PSD `S_out,j`:

   `I_mu,j = 4 int_0^infty |d htilde_j/du_j|^2 / S_out,j df`,

   `R_mu,j = p_j I_mu,j/tau_j`,

   and for independently scheduled layers

   `T_cal = gamma sum_j 1/R_mu,j`.

   With science rate `R_beta`, target `Z`:

   `x=T_cal/T_sci = gamma R_beta/Z^2 sum_j 1/R_mu,j`.

   For a same-time dual-probe pair acquired jointly, use the full `2x2` Fisher block including cross-Fisher; do not sum two scalar row SNRs unless the likelihood factorizes.

4. **Regression checks.**
   - Toy013/Toy009 physical D2 science-time penalty remains `23.64956630775`.
   - Toy009 seven-layer mean calibration at homogeneous `xi_mu=3` remains `1,423,539.213` accepted layer-cycles before acceptance/time overhead.

## What remains open

- Physical transduction Jacobian and output/equivalent-force PSD for the D2 calibration detector.
- Full seven-layer multichannel Fisher including detector correlations.
- Apparatus-consistent `x=T_cal/T_sci` and `y=T_src/T_sci` for Toy009/Toy013.
- Timing/additive/control nuisances on the same likelihood.
- D1/D2 common apparatus budget.
- Gauge/conservation/positivity/causality/Newtonian/EFT/renormalization/full-QFT-vs-classical/stochastic degeneracy gates.

## Do not regress

- Do not identify `alpha_h` with `epsilon_drv`.
- Do not convert a demodulated, already-averaged sigma into single-shot noise (NG-027).
- Do not treat normalized `gamma` or `C_a/S` as a physical shot count without a declared Fisher rate.
- Do not reuse noncommuting cross-time calibration layers as one disturbance-free source copy.
- Do not rank sources by Euclidean detector norm instead of the nuisance-profiled physical detector likelihood.
- No new-physics claim.

## Reproducible files

- `analysis/physical_fisher_rate_closure_iteration068.py`
- `docs/PHYSICAL_FISHER_RATE_CLOSURE_ITERATION068.md`
- `research_log/2026-08-30_iteration_068_physical_fisher_rate_closure.md`

## Next gate

Build a physical D2 same-time dual-probe calibration likelihood. Declare the transduction Jacobian, one-sided PSD, acquisition window, acceptance and dead/reset time. Compute the seven `2x2` per-layer Fisher blocks and the resulting `x=T_cal/T_sci`, then combine with source-metrology `y` and apply the Iteration-066 architecture-dominance inequality.
