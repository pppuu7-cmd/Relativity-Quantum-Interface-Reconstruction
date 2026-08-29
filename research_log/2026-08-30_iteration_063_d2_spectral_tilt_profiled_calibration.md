# RQIR Research Log — Iteration 063

**Date:** 2026-08-30

## Result

The relative spectral-tilt nuisance was inserted directly into the full D2 detector/source Fisher. With detector score `s=(G2,G4)` and tilt score `t=(G2,-G4)`, profiling tilt exactly reproduces the physical two-band metric used in Iteration 019.

After normalizing each source to unit beta Fisher **after tilt profiling**, centered NP3 calibration was re-optimized.

Approximate total calibration-cost ratios:

- Toy009: 1;
- Toy011 response-oriented: `~21.7`;
- Toy011 conditioning-oriented: `~8.8`;
- Toy012 balanced: `~4.7e4`;
- Toy012 high-response: `~5.2e2`.

Thus Toy012's previous `~1.06x` calibration result was not physical for the intended two-band D2 likelihood; it was specific to Euclidean detector normalization.

New retained rule **RQIR-CAL-019**: detector nuisance directions that define the physical discrimination metric must be included inside source/calibration co-design, not profiled only after source optimization.

Toy009 remains well conditioned under the physical metric, while Toy011 remains costly but finite because its original search already preserved both bands.

## Next

Build Toy013 in the exact nearest-neighbour manifold. Cheap search uses physical two-band D2 `S_eff` and conditioning; expensive survivor audit uses the spectral-tilt-profiled centered calibration cost from this iteration.
