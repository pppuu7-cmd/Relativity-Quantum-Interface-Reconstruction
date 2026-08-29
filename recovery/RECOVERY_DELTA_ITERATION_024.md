# RQIR Recovery Delta — Iteration 024

**Date:** 2026-08-29

## Authority

This delta is subordinate to `docs/RECOVERY_GUIDE.md` and records only the new Iteration-024 frontier. Repository state remains authoritative over chat history.

## New gate closed

Iteration 023 left two unresolved metrology ambiguities: which timing-stability statistic corresponds to `delta tau`, and how row-normalized additive priors map to physical readout units.

Iteration 024 closes both at the formal level without inventing apparatus sensitivities.

## Retained formulas

Detector timing nuisance:

`delta tau = omega_gap * delta t_rel`.

`delta t_rel` is the differential source-drive to detector-reference delay, including non-common source path, detector path, trigger, DAC, ADC/aperture and synchronization terms.

Current 100-Hz targets remain:

- D1 `sigma_t,rel ~ 9.47 us`;
- D2 `sigma_t,rel ~ 8.01 us`.

Do not substitute the ADEV of one oscillator for this target. Use measured differential TDEV/phase-delay stability of the complete synchronized chain.

For a raw Toy calibration row `a_i` normalized as `a_i/||a_i||`, a common normalized additive nuisance `b` corresponds to

`delta x_i,raw = ||a_i|| b`.

If physical readout is

`y_i = g_i x_i,raw + o_i`,

then

`sigma(o_i) <= |g_i| ||a_i|| sigma(b_group)`.

This is the required normalization-safe route to SI units.

## Numerical row norms and targets

Mean-row norms:

- probe-0 seven rows: `1.371745109247`;
- probe-1 seven rows: `0.382088538024`.

Covariance-row norm range: `0.0674024429 ... 0.98271945`.

Raw Toy-unit additive requirements:

- D1 mean `2.912e-5 ... 1.045e-4`;
- D1 covariance `6.943e-6 ... 1.012e-4`;
- D2 mean `2.461e-5 ... 8.835e-5`;
- D2 covariance `7.010e-6 ... 1.022e-4`.

These are not SI values.

## New labels

**RQIR-REF-001:** detector timing prior is a differential source-to-detector reference stability requirement; single-clock ADEV is insufficient.

**RQIR-CAL-008:** convert normalized additive priors through raw row norms and then branch-specific readout Jacobians.

**RQIR-NG-008:** unknown/uncontrolled physical transduction prevents a unique SI additive-offset tolerance; repeated normalized calibration alone cannot cure this scale ambiguity.

## External metrology interpretation

NIST distinguishes ADEV from TDEV and demonstrates that distribution topology affects relative timing. Precision interferometric detector literature treats ADC/sampling-clock jitter as an explicit coupling. These are methodological boundaries, not RQIR hardware certification.

## Files to read next

1. `docs/DIFFERENTIAL_REFERENCE_AND_PHYSICAL_OFFSET_MAP.md`
2. `analysis/differential_reference_offset_units_iteration024.py`
3. `research_log/2026-08-29_iteration_024_differential_reference_physical_offsets.md`

## Next unresolved target

Build row-specific branch transductions:

- D1 raw source/calibration coordinate -> phase/contrast estimator;
- D2 raw coordinate -> equivalent-force/PSD estimator.

Then inject differential TDEV and physical additive-reference drift into the hard-constrained detector-level Fisher and the Iteration-021 `F_beta|theta/T_wall` optimization.
