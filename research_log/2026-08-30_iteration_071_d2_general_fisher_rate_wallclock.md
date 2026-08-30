# RQIR Research Log — Iteration 071

**Date:** 2026-08-30

## Source-of-truth check

Read before advancing: `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, latest confirmed Iteration 070 log, and the retained Toy009/Toy010/statistical-identifiability baseline referenced by Iteration 070. No active or closed toy search was duplicated.

## What was done

Generalized the Iteration-070 common-PSD/common-schedule force-likelihood bridge to separate science, calibration and source-metrology Fisher rates.

Define

`R_beta=(p_sci/tau_sci) K_sci,profiled`,

`R_cal,j=(p_j/tau_j) lambda_min[K_cal,j]`,

with `K_cal,j=4 Re int J_j^dag S_j^-1 J_j df`, and independent source-metrology rate `R_src` from the declared pointer/Ramsey likelihood including reset/readout/visibility.

Then

`T_sci=Z^2/R_beta`,

`T_cal=gamma_mean sum_j 1/R_cal,j`,

`T_src=C_prep/R_src`.

Therefore

`x=gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y=C_prep R_beta/(Z^2 R_src)`.

## New retained result

### RQIR-RESOURCE-033

The physical resource closure no longer needs a common ASD or common cycle schedule. Shot noise and colored noise live in the PSD; coherence/visibility in the signal kernel; acceptance and dead/reset time in the rates; cross-channel noise in the matrix PSD; nuisance degeneracies in profiled science Fisher.

For the multiplicative beta-alpha source nuisance, if one retains fraction `r` of raw Fisher and the raw target is `F_bb=Z^2`,

`C_prep=[r/(1-r)]Z^2`,

so

`y=[r/(1-r)] R_beta/R_src`.

At `r=0.90`, `y=9 R_beta/R_src`. Hence source metrology below 10% of science time requires `R_src>90 R_beta`; source metrology below science time requires `R_src>9 R_beta`.

## Regression

The general formula exactly reduces to Iteration 070 under its special assumptions:

`x=296.184784604 (1+|rho|) r_F^2` for Toy009 at `Z=5`.

The new script asserts the prior prefactor and the stored `rho=0,0.5,0.9` values.

## New negative guardrail

### RQIR-NG-029

Toy009/Toy013 normalized time ratios are not automatically apparatus-invariant. If source geometry changes detector transfer, PSD weighting, bandwidth, coherence, acceptance or scheduling, the science/calibration/source ratios must be recomputed from physical rates for each source rather than importing Iteration-066 ratios.

## Gates retained

NG-005, NG-006, NG-023, NG-026, NG-027, NG-028 and all relativistic/full-QFT/classical/stochastic consistency/degeneracy gates remain active. No new-physics claim.

## Reproducibility

- `analysis/d2_general_fisher_rate_wallclock_iteration071.py`
- `docs/D2_GENERAL_FISHER_RATE_WALLCLOCK_ITERATION071.md`

## Next

Instantiate the general rate closure for Toy012 using its own D2 profiled response, seven mean-calibration layers and pointer/Ramsey source-metrology rates, retaining the 100 Hz timing/coherence benchmark only where its likelihood assumptions apply. Keep the result as a physical parameter surface unless a repository-backed detector PSD/transduction model exists.
