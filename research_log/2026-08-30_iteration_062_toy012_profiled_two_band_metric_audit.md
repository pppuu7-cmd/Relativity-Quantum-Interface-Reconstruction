# RQIR Research Log — Iteration 062

**Date:** 2026-08-30

## Critical correction

Before attaching an SI science time to Toy012, the detector metric was audited against the physical D1/D2 resource model.

Iteration 055's balanced Toy012 `D2raw_ratio~0.21617` is the Euclidean power ratio of the four real `(Re G2, Im G2, Re G4, Im G4)` components. It is not the spectral-tilt-profiled two-band Fisher used by Iteration 019.

Balanced Toy012 has

- `G2~0.00893149+0.00678180i`;
- `G4~-1.17e-6+1.22e-6i`.

Thus the physical equal-ASD two-band `S_eff` ratio is only `~1.96963e-8` of Toy009, not `0.21617`. The old `~4.63x` science-time interpretation is withdrawn; equal-noise physical science time would instead scale by `~5.08e7` in this detector model.

The high-response Toy012 point is also spectrally imbalanced: physical D2 ratio `~1.214e-4`, science-time factor `~8.24e3`.

D1 shows the same failure after source-specific four-switch optimization: balanced `~5.81e-8`, high-response `~2.94e-6` of Toy009.

New correction **RQIR-NUM-003**: detector-vector norm is not a profiled detector Fisher metric.

New design rule **RQIR-DESIGN-005**: source co-design must optimize the same physical profiled detector likelihood/metric that will later be used for wall-clock conversion.

Toy012 exact locality/null/state-positivity results remain valid; its physical source-baseline promotion is withdrawn until a two-band-aware local redesign is found.

## Next

Build Toy013 inside the exact nearest-neighbour source manifold, but rank candidates by physical two-band D2 `S_eff` together with centered calibration cost. Do not optimize Euclidean detector norm.
