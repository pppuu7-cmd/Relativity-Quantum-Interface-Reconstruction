# RQIR Research Log — Iteration 084

**Date:** 2026-08-30

## Goal

Advance the Paper-III apparatus front after NG-033/NG-034 without inventing an absolute ASD: derive the exact physical science Fisher-rate law for a simultaneous broadband/two-mode detector and identify the irreducible weak-band requirement.

## Result

For simultaneous band information rates `r2,r4` and the retained antisymmetric spectral-tilt nuisance,

`R_2band = 4 r2 r4/(r2+r4)`.

New **RQIR-RESOURCE-038**: the profiled two-band science throughput is twice the harmonic mean of the two band rates.

New **RQIR-NG-035**: at fixed weak-band rate `r_w`, unlimited improvement of the other band cannot raise the profiled science rate above `4 r_w`. A target `R_*` therefore requires both bands individually above `R_*/4`.

The inverse partner requirement is

`r4 >= R_* r2/(4 r2-R_*)`,

valid only for `4 r2>R_*`.

At `Z=5`, science-only profiled-rate targets are `2.8935e-4`, `4.1336e-5`, and `9.6451e-6 s^-1` for 1, 7, and 30 days respectively. These are specifications, not apparatus forecasts.

## External check

Published levitated systems do demonstrate simultaneous multimode readout/control. Piotrowski et al. (*Nature Physics* 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`) report simultaneous two-mode COM cooling and modes near 224, 268 and 80 kHz. However, the literature check did not yield one measured RQIR-ready apparatus with calibrated force PSD/cross-PSD at two simultaneous bands in exact 2:1 ratio plus the required calibration/source/control channels. No absolute wall-clock forecast was therefore inserted.

## Decision

For the next apparatus gate, prioritize the weaker physical science band. Once both measured band rates exist, set `R_beta=R_2band` and propagate the same detector model into the seven calibration layers, source-metrology rate and duty before NG-030 branch comparison.

## Reproduce

`python analysis/simultaneous_dual_band_rate_iteration084.py`

## Document

`docs/PAPER_III_SIMULTANEOUS_DUAL_BAND_RATE_ITERATION084.md`
