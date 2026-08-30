# RQIR Recovery Delta — Iteration 084

**Date:** 2026-08-30  
**Authoritative predecessor:** Iteration 083.

## New retained results

**RQIR-RESOURCE-038 — simultaneous two-band throughput**

For simultaneous science-band Fisher rates `r2,r4` under the mature relative spectral-tilt nuisance,

`R_beta = R_2band = 4 r2 r4/(r2+r4)`.

This is twice the ordinary harmonic mean of the two band rates. Use it as the science-rate input to Iterations 077/080 only after the actual detector transfer/noise nuisance profile has been applied.

**RQIR-NG-035 — weak-band ceiling**

For fixed weak-band rate `r_w`, even an arbitrarily good partner band gives only

`R_2band -> 4 r_w`.

Hence any target `R_*` requires each band individually to satisfy `r_n > R_*/4`. One excellent band cannot rescue an unusable second band.

Inverse partner requirement:

`r4 >= R_* r2/(4 r2-R_*)`,

with no finite solution when `4 r2 <= R_*`.

## Physical normalization rule

For D2 force readout, use measured/declared physical quantities in one fixed PSD convention:

`r_n = kappa_PSD |Delta F_n|^2/S_F,n^eq`.

Keep `kappa_PSD` explicit until validated against the chosen time-domain/complex-quadrature likelihood. Include full cross-PSD if the simultaneous modes share output noise.

## Science-only target examples at Z=5

- 1 day: `R_beta >= 2.8935185e-4 s^-1`;
- 7 days: `R_beta >= 4.1335979e-5 s^-1`;
- 30 days: `R_beta >= 9.6450617e-6 s^-1`.

For balanced bands, each rate is half the corresponding `R_beta` target.

These are not total experiment rates and not apparatus forecasts.

## External platform boundary

Simultaneous multimode levitated readout/control exists experimentally (e.g. Piotrowski et al., Nature Physics 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`), but no searched source supplied a complete RQIR apparatus with two calibrated force bands in exact 2:1 ratio plus cross-PSD, seven calibration layers, source metrology and control duty. Do not fabricate those missing inputs.

## Files

- `analysis/simultaneous_dual_band_rate_iteration084.py`
- `docs/PAPER_III_SIMULTANEOUS_DUAL_BAND_RATE_ITERATION084.md`
- `research_log/2026-08-30_iteration_084_simultaneous_dual_band_rate.md`

## Next gate

Construct a two-band physical detector specification in terms of measured/declared `S_F,2`, `S_F,4`, transfer functions/windows and cross-PSD. Then propagate the same apparatus model into the seven calibration layers and source/control rates before Toy009/Toy014 NG-030 comparison.
