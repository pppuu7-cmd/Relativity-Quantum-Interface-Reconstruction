# RQIR Research Log — Iteration 068

**Date:** 2026-08-30

## What was done

Continued from Iteration 067 without reopening closed Toy searches. Converted the source-preparation Fisher target and row-normalized mean-calibration strength into explicit accepted-copy, detector-PSD and wall-clock Fisher-rate language.

Before doing so, resolved a notation collision: current source Fisher uses fractional hidden amplitude `alpha_h` (`a=0.08 alpha_h`), while older Protocol 002B used `alpha` for the pump impulse area. The drive variable is now denoted `epsilon_drv`.

## Main results

### RQIR-NUM-004

Separate hidden-source preparation amplitude from pump/drive amplitude. The science-cycle leverage is

`q_drv = 2 |epsilon_drv| Gamma_G/sigma_phi`,

while `alpha_h` remains the nuisance preparation coordinate constrained by independent source metrology. The local model is `mu_D ~ beta alpha_h epsilon_drv s`, so NG-005 remains unchanged.

### Absolute preparation Fisher

For raw detector Fisher `S`, retaining fraction `r` against only the beta/source-amplitude degeneracy requires

`C_prep = r/(1-r) S`.

At `Z=5`, `Delta beta=1`, `S=25`, and `r=0.90`:

`C_prep = 225`.

Toy009 then needs at least

- `23956.85364` accepted energy-population metrology copies using `F_E^alpha=0.0093918844`;
- `2649.165951` accepted copies even at the ideal full-QFI ceiling `F_Q^alpha=0.0849323916`.

At `p=0.5`, attempts double to `47913.71` and `5298.33`, before reset/readout/systematics.

### RQIR-RESOURCE-030

For calibration layer `j`,

`I_mu,j = 4 int |d htilde_j/du_j|^2/S_out,j df`,

`R_mu,j = p_j I_mu,j/tau_j`.

For independently scheduled layers,

`T_cal = gamma sum_j 1/R_mu,j`.

Combined with science Fisher rate `R_beta`,

`x=T_cal/T_sci = gamma R_beta/Z^2 sum_j 1/R_mu,j`.

This is the physical rate closure of abstract `gamma`. A detector PSD, transduction template and acquisition cycle are mandatory before `gamma` can be quoted as shots or hours.

The homogeneous limit exactly reproduces Iteration 042: Toy009 seven-layer mean calibration at `xi_mu=3` requires `1,423,539.213` accepted layer-cycles before acceptance/time overhead.

## Regression

The Toy013/Toy009 physical D2 science-time ratio remains

`23.64956630775`.

It is unaffected by the notation correction because the common detector leverage cancels.

## Gates retained

NG-005, NG-006, NG-023, NG-026, NG-027 and all relativistic/full-QFT/classical/stochastic consistency/degeneracy gates remain active. No new-physics claim.

## Reproducibility

- `analysis/physical_fisher_rate_closure_iteration068.py`
- `docs/PHYSICAL_FISHER_RATE_CLOSURE_ITERATION068.md`

## Next

Construct one explicit D2 same-time dual-probe calibration likelihood with physical transduction and output/equivalent-force PSD. Compute each `2x2` per-layer Fisher block, all seven layers, and the apparatus-consistent `x=T_cal/T_sci`; then combine with a chosen source-metrology `y=T_src/T_sci` and re-test the Iteration-066 dominance boundary.
