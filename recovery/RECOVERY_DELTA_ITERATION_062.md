# RQIR Recovery Delta — Iteration 062

**Date:** 2026-08-30

## Mandatory correction

**RQIR-NUM-003 — detector-vector norm is not a profiled detector Fisher metric.**

Iteration 055's balanced Toy012 value `D2raw_ratio~0.2161694` is the Euclidean four-component detector-vector power ratio. Do not use it as the physical D2 science Fisher ratio when the Iteration-019 relative spectral-tilt nuisance is active.

Physical equal-ASD D2 two-band metric:

`S_eff=4|G2|^2|G4|^2/(|G2|^2+|G4|^2)`.

Balanced Toy012:

- `G2~0.00893149+0.00678180 i`;
- `G4~-1.168e-6+1.217e-6 i`;
- physical D2 ratio to Toy009 `~1.96963e-8`;
- equal-noise science-time factor `~5.077e7`;
- balancing the two detector bands by noise alone would require `ASD4/ASD2~1.504e-4` (~6600x lower ASD in n=4).

High-response Toy012:

- physical D2 ratio `~1.214e-4`;
- science-time factor `~8.24e3`;
- needed ASD4/ASD2 for band balance `~0.00995`.

D1 source-optimized four-switch profiled ratios are likewise tiny: balanced `~5.81e-8`, high-response `~2.94e-6`.

Withdraw the statement `Toy012 science penalty~4.63x`.

**RQIR-DESIGN-005:** source/calibration co-design must optimize the same profiled physical detector metric used for the intended wall-clock model. Euclidean detector normalization may remain an abstract nuisance-geometry convention but cannot be promoted to physical rate without a matching detector covariance/nuisance model.

## What survives

Toy012 exact nearest-neighbour locality, exact spectrum, rank/null construction, positive states, selected ordered-response split, source QFI/metrology, and normalized auxiliary Fisher calculations remain valid as declared mathematical/resource diagnostics. Toy012 is not currently the physical D2 source baseline.

## Reproduction

Run `analysis/toy012_profiled_two_band_metric_audit_iteration062.py`.

## Next gate

Build Toy013: exact-nearest-neighbour source co-design scored by physical two-band D2 `S_eff` plus centered calibration cost. Preserve both n=2 and n=4 science bands; then re-run source metrology and complementary D2 profiling.
