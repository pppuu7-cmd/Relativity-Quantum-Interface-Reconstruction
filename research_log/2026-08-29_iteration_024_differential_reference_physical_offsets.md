# RQIR Research Log — Iteration 024

**Date:** 2026-08-29

## Target

Advance the Iteration-023 gate without inventing hardware sensitivity: determine which timing-stability observable corresponds to the detector nuisance and convert the row-normalized additive offset priors into a normalization-safe physical-resource map.

## Source-of-truth review

Re-read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, latest Iteration-023 research log, Toy009/Toy010 continuity and Statistical Identifiability 002. Retained constraints: RQIR-NG-005, hard-constraint RQIR-NUM-001, corrected D1/D2 90%-retention weights, RQIR-NG-006/007, current timing/additive priors, and no SI conversion without an explicit measurement transfer function.

## Work completed

1. Identified the detector timing nuisance as a *differential source-drive to detector-reference time error*, not the instability of a single oscillator.
2. Connected the correct experimental certification to TDEV/relative phase-delay stability of the complete synchronized chain; ADEV alone is insufficient.
3. Reconstructed all unnormalized Toy009 calibration-row norms from the authoritative Iteration-012 source construction.
4. Derived the exact normalization inverse `delta x_raw = ||a_i|| b`.
5. Derived the physical readout map `sigma(o_i) <= |g_i| ||a_i|| sigma(b_group)` for `y_i=g_i x_i+o_i`.
6. Added a reproducible script with numerical regression checks.
7. Preserved the remaining missing information explicitly: row-specific D1 phase/contrast and D2 force/PSD transduction Jacobians.

## Numerical checks

Current raw row norms:

- first 7 mean rows: `1.371745109247...`;
- second 7 mean rows: `0.382088538024...`;
- covariance rows: `0.0674024429 ... 0.98271945`.

Applying the corrected Iteration-016 normalized priors:

- D1 mean raw-offset range: `2.912e-5 ... 1.045e-4`;
- D1 covariance raw-offset range: `6.943e-6 ... 1.012e-4`;
- D2 mean raw-offset range: `2.461e-5 ... 8.835e-5`;
- D2 covariance raw-offset range: `7.010e-6 ... 1.022e-4`.

Timing targets remain D1 `9.47 us`, D2 `8.01 us`, but must now be interpreted as differential path TDEV/relative-delay RMS at the relevant averaging/cadence scale.

## External metrology check

NIST distinguishes ADEV (fractional-frequency stability) from TDEV (time-offset stability). NIST dual-clock timing work shows clock-distribution topology changes timing offset/noise. Precision interferometric literature also treats sampling-clock/aperture jitter as an explicit measurement coupling. These establish the correct metrology language and show that sub-microsecond timing is not intrinsically exotic, but they do not certify an RQIR apparatus.

## New retained results

**RQIR-REF-001:** the timing prior entering detector-level `F_{beta|theta}` applies to differential source-drive-to-detector-reference time error; a single clock's ADEV is insufficient.

**RQIR-CAL-008:** normalization-safe SI conversion is `normalized prior -> raw row norm -> physical readout Jacobian`.

**RQIR-NG-008:** if the row-specific physical transduction `g_i` is unknown/uncontrolled, no unique SI additive-offset tolerance follows from the normalized Toy Fisher prior. Repeating the same normalized calibration does not cure this scale ambiguity.

## Scientific status

No new-physics claim. This iteration closes a G13 normalization/metrology ambiguity only. Gauge, conservation, positivity/unitarity, causal, EFT, renormalization and interface-class degeneracy gates remain open.

## Files

- `analysis/differential_reference_offset_units_iteration024.py`
- `docs/DIFFERENTIAL_REFERENCE_AND_PHYSICAL_OFFSET_MAP.md`
- `recovery/RECOVERY_DELTA_ITERATION_024.md`

## Next gate

Build explicit D1 and D2 transduction Jacobians for each calibration row, then combine measured/bounded differential TDEV and physical additive-reference drift with the corrected detector-level Fisher and Iteration-021 wall-clock objective.
