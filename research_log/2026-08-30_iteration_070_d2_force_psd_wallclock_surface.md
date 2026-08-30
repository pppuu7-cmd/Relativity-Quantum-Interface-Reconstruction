# RQIR Research Log — Iteration 070

**Date:** 2026-08-30

## Source-of-truth check

Read before advancing:

- `docs/RECOVERY_GUIDE.md`;
- `docs/MASTER_TABLE.md`;
- latest confirmed log, Iteration 069;
- `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`;
- `docs/TOY_MODEL_010_CALIBRATION_GEOMETRY_COOPTIMIZATION.md`;
- `docs/STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`.

No active/closed toy search was duplicated.

## What was done

Closed the next physical resource bridge after the Iteration-069 dual-probe matrix-Fisher gate. A declared white equivalent-force likelihood was used to convert the mean-calibration Fisher into a force-PSD coordinate while keeping the result parametric in the physical science/calibration transduction ratio.

For a rectangular force template,

`I_F = 2 F^2 T/S_F`.

For a symmetric same-time two-probe PSD block with correlation `rho`, the worst calibration eigenmode is

`I_cal,min = 2 F_cal^2 T/[S_F(1+|rho|)]`.

With equal science/calibration scheduling and PSD, define `r_F=F_sci/F_cal`. Then Toy009 gives

`x=T_cal/T_sci = 296.184784604 (1+|rho|) r_F^2`

at `Z=5`.

## New retained result

### RQIR-RESOURCE-032

The old abstract mean-calibration scale can be replaced, under one declared equivalent-force likelihood, by a physical transduction ratio. The Toy009/Toy013 total-time boundary becomes

`296.184784604 (1+|rho|) r_F^2 > 25.8350584 + 376.305592 y`,

with `y=T_src009/T_sci009`.

At `r_F=1`:

- `rho=0`: Toy013-favouring only for `y<0.718431328`;
- `rho=0.5`: `y<1.111974224`;
- `rho=0.9`: `y<1.426808540`.

At `rho=0`, critical `r_F` is about `0.29534`, `0.46298`, `1.16510` for `y=0`, `0.1`, `1`, respectively.

## New negative guardrail

### RQIR-NG-028

Cancellation of an absolute equivalent-force ASD from `T_cal/T_sci` is valid only if science and calibration truly share the declared transfer/noise/acquisition model up to the explicit scale factors. Separate transfer functions, colored PSDs, bandwidths, acceptance or duty factors invalidate the cancellation.

Therefore the numerical `x` surface is a controlled reference likelihood, not an apparatus forecast.

## Gates retained

NG-005, NG-006, NG-023, NG-026, NG-027 and all relativistic/full-QFT/classical/stochastic consistency/degeneracy gates remain active. No new-physics claim.

## Reproducibility

- `analysis/d2_force_psd_wallclock_surface_iteration070.py`
- `docs/D2_FORCE_PSD_WALLCLOCK_SURFACE_ITERATION070.md`

## Next

Generalize from the common-PSD/common-schedule reference likelihood to separate science and calibration matched-filter integrals and explicit acceptance/dead/coherence factors. Then combine those with source-metrology reset/visibility rates into one total wall-clock surface.
