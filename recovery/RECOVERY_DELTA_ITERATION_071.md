# RQIR Recovery Delta — Iteration 071

**Date:** 2026-08-30

## Current front

Iteration 071 generalizes the Iteration-070 force-PSD reference likelihood into a source/calibration/science Fisher-rate wall-clock closure. This is the current confirmed resource front.

## New retained formulas

For profiled science Fisher rate `R_beta`, independent calibration-layer rates `R_cal,j`, source-metrology rate `R_src`, target significance `Z`, mean-calibration weight `gamma_mean` and source-prior target `C_prep`:

`T_sci = Z^2/R_beta`

`T_cal = gamma_mean sum_j 1/R_cal,j`

`T_src = C_prep/R_src`

`x = T_cal/T_sci = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`

`y = T_src/T_sci = C_prep R_beta/(Z^2 R_src)`

For a multiplicative beta-alpha nuisance retaining fraction `r` of raw science Fisher at `F_bb^raw=Z^2`:

`C_prep=[r/(1-r)]Z^2`

and therefore

`y=[r/(1-r)]R_beta/R_src`.

At `r=0.90`:

`C_prep=225` for `Z=5`, and `y=9 R_beta/R_src`.

Useful boundaries:

- `T_src < T_sci` requires `R_src > 9 R_beta`;
- `T_src < 0.1 T_sci` requires `R_src > 90 R_beta`.

## Retained labels

- **RQIR-RESOURCE-033:** general Fisher-rate wall-clock closure.
- **RQIR-NG-029:** architecture ratios are not invariant if different source designs induce different detector transfer/PSD/coherence/acceptance/scheduling kernels.

## Regression

Under the Iteration-070 special common-PSD/common-schedule assumptions, the general closure reproduces

`x = 296.184784604 (1+|rho|) r_F^2`

for Toy009 at `Z=5`.

## Physical interpretation discipline

`R_beta` must be detector-level and profiled over nuisance parameters. `R_cal,j` must use the full same-time dual-probe matrix PSD. `R_src` must include fresh-source acceptance, reset/readout time and protocol visibility/coherence. Do not replace these by normalized SNR placeholders after this iteration.

NG-005 remains active: gravitational null calibration does not identify the hidden source amplitude. NG-006/023/026/027/028 and all relativistic/full-QFT/classical/stochastic consistency gates remain open. No new-physics claim.

## Reproduce

Run:

`python analysis/d2_general_fisher_rate_wallclock_iteration071.py`

Primary note:

`docs/D2_GENERAL_FISHER_RATE_WALLCLOCK_ITERATION071.md`

Research log:

`research_log/2026-08-30_iteration_071_d2_general_fisher_rate_wallclock.md`

## Next admissible step

Instantiate this closure for Toy012 with its own D2 profiled response and source-metrology rates. Use the 100 Hz timing/coherence benchmark only when compatible with the declared likelihood. Keep detector PSD/transduction parametric unless an explicit repository-backed apparatus model exists.
