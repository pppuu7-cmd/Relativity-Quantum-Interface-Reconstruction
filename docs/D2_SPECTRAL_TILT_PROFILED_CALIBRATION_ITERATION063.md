# RQIR Iteration 063 — Spectral-Tilt-Profiled D2 Calibration Audit

**Date:** 2026-08-30  
**Status:** detector-metric consistency audit; no hardware or new-physics claim.

## 1. Physical detector nuisance inserted into the full Fisher chain

Iteration 062 showed that Toy012's Euclidean four-component detector norm is not the physical two-band D2 Fisher when a relative spectral-shape nuisance is profiled.

For

`s=(Re G2, Im G2, Re G4, Im G4)`

introduce a relative band-tilt nuisance with score

`t=(Re G2, Im G2, -Re G4, -Im G4)`.

With equal whitened noise in the two complex bands,

`F_beta|tilt = s.s - (s.t)^2/(t.t)`

reduces exactly to

`4 |G2|^2 |G4|^2 / (|G2|^2+|G4|^2)`.

Iteration 063 normalizes each candidate by this **profiled physical detector Fisher**, then recomputes the centered NP3 calibration cost while profiling both

- the 22 source nuisances;
- the detector spectral-tilt nuisance.

## 2. Toy009 remains numerically well behaved

For Toy009 the 90%-retention group optimization gives a total normalized calibration cost of order

`2.9e7`,

with representative row weights near

- `gamma_mean ~1.7e6`;
- `gamma_cov ~6.0e5`.

This is close to the mature centered Euclidean-normalized Toy009 budget, which is reassuring: Toy009 already carries substantial information in both harmonics.

## 3. Toy011 locality points remain expensive but finite

Relative total physical calibration costs are approximately

- Toy011 response-oriented: `~21.7x Toy009`;
- Toy011 conditioning-oriented: `~8.8x Toy009`.

These are worse than the Euclidean-metric estimates, but they remain finite and track the fact that the Toy011 search explicitly preserved two-band `S_eff`.

## 4. Toy012 calibration advantage disappears completely

When the same physical spectral-tilt nuisance is included:

- balanced Toy012 calibration cost becomes approximately `4.7e4 x Toy009`;
- high-response Toy012 becomes approximately `5.2e2 x Toy009`.

Thus the earlier `~1.06x Toy009` balanced Toy012 D2 calibration claim was specific to the Euclidean detector-vector normalization. It is not the calibration cost of the physical two-band D2 likelihood.

This reinforces RQIR-NUM-003 and requires a stronger design rule.

### RQIR-CAL-019 — detector nuisance belongs inside calibration co-design

> Source calibration cannot be optimized against a detector metric and later combined with a different profiled detector likelihood. Detector nuisance directions that define the physical discrimination problem must be present when source/calibration Fisher geometry is optimized.

This applies not only to spectral tilt but to any detector nuisance that materially changes the score-space metric.

## 5. What this changes

Toy012 is now firmly demoted from physical D2 baseline status. Its exact locality result remains useful, but both its apparent science-rate advantage and its apparent near-Toy009 calibration efficiency were artifacts of optimizing an incomplete detector metric.

The correct next local source search must score candidates by

1. exact nearest-neighbour locality;
2. exact NP3 null/state positivity;
3. **physical spectral-tilt-profiled D2 source information**;
4. centered calibration cost with the spectral-tilt nuisance already included;
5. source-metrology accessibility.

## 6. Reproducibility

Code:

`analysis/d2_spectral_tilt_profiled_calibration_iteration063.py`

The script reconstructs Toy009, both Toy011 Pareto points and both Toy012 points, verifies that the tilt-only profiled beta Fisher is normalized to one, then recomputes the centered calibration allocation.

## 7. Next gate

Construct Toy013. Use a two-stage search:

- cheap stage: exact local-chain candidates ranked by physical two-band `S_eff` plus conditioning;
- expensive audit: spectral-tilt-profiled centered calibration cost for the Pareto survivors.

The objective should explicitly avoid solutions where either `|G2|` or `|G4|` collapses.
