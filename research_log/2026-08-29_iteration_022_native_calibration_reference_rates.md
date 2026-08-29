# RQIR Research Log — Iteration 022

**Date:** 2026-08-29

## Target

Close the resource-model gap left by Iteration 021: derive physical Fisher-information rates for gravitational calibration and independent reference/control channels without inventing apparatus-specific performance.

## Work completed

1. Re-read the current recovery guide, master table, Iteration-021 optimizer, and Iteration-016 explicit-systematics Fisher layer.
2. Replaced standardized mean-calibration sensitivity by explicit D1 phase-readout Fisher at quadrature:
   `R_M = p_acc C^2 k^2 / t_cycle`.
3. Replaced standardized covariance sensitivity by the Gaussian covariance Fisher formula and the broadband limit `R_C ~= duty * B * k_C^2` for a unit log-variance coordinate.
4. Wrote the D2 mean-calibration rate directly in equivalent-force PSD/template form.
5. Derived native timing, additive-offset, and gain-reference Fisher rates.
6. Derived the timing wall-time invariant `T = t_cycle/p * (sigma_event/sigma_target)^2`; explicit `f_gap` cancels when nuisance units are converted consistently.
7. Added transparent numerical unit-coupling benchmarks using the corrected Iteration-015 row weights.

## Numerical checks

With `tau_max=4.99085067`, `f_gap=100 Hz`, `1 ms` extra dead time and `p_acc=0.5`:

- coherence floor is about `7.94 ms`;
- D1-like mean calibration with `C=0.66`, `k=1 rad/unit`, sequential 14 rows costs about `275 h` for D1 corrected weights;
- applying the same readout benchmark to D2 corrected mean weights gives about `386 h`;
- covariance/log-PSD calibration with `B=1 kHz`, unit log-variance sensitivity, sequential 8 rows gives about `2.08 h` D1 and `2.07 h` D2;
- timing reference with `10 us` independent per-event timestamp RMS reaches the current timing-prior benchmark in about `0.020 s` D1 / `0.028 s` D2 under the white independent-event model.

The last result is intentionally interpreted negatively: white timing statistics are not the likely bottleneck. Long-campaign low-frequency/common-mode drift remains the relevant unresolved systematic.

## New rules

**RQIR-RESOURCE-006:** reference-control wall-time cost is governed by event-level precision relative to required prior precision times cycle/acceptance cost; nuisance normalization must not create artificial wall-time scaling.

**RQIR-DRIFT-002:** once white timing-reference information is fast, the limiting timing resource is low-frequency/common-mode stability over the acquisition campaign. A white per-event Fisher rate alone cannot certify the Iteration-016 prior.

## Scientific status

No new-physics claim. No consistency/degeneracy gate is promoted. The advance is strictly in experimental-resource identifiability.

## Files

- `analysis/native_calibration_reference_rates_iteration022.py`
- `docs/NATIVE_CALIBRATION_REFERENCE_FISHER_RATES.md`
- `recovery/RECOVERY_DELTA_ITERATION_022.md`

## Next gate

Build a colored-drift / Allan-variance model for timing and additive references, derive the calibration cadence required over the full D1/D2 campaign, and add that cadence cost to the Iteration-021 wall-clock objective.
