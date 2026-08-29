# RQIR Iteration 024 — Differential Reference and Physical Offset Map

**Date:** 2026-08-29  
**Scope:** G13 detector/control metrology only. No new-physics claim.

## 1. Why this gate was necessary

Iteration 023 reduced long-run timing control to a colored-drift/Allan problem, but two ambiguities remained:

1. Which clock-stability statistic actually corresponds to the RQIR timing nuisance `delta tau`?
2. How should the row-normalized additive offsets `b_mean` and `b_cov` be converted to physical readout units without inventing a hidden sensitivity scale?

The answer to both is that the *complete differential measurement chain* must be modeled explicitly.

## 2. Timing nuisance is differential time error

The detector prior from Iteration 016 is

`delta tau = omega_gap * delta t_rel`,

with current 100-Hz targets

- D1: `sigma_t,rel ~ 9.47 us`;
- D2: `sigma_t,rel ~ 8.01 us`.

Here `delta t_rel` is not the error of one clock in isolation. It is the relative delay between the source modulation phase actually delivered to the source and the detector/reference phase used in inference.

A useful decomposition is

`delta t_rel = delta t_source-path - delta t_detector-path + delta t_DAC + delta t_ADC + delta t_trigger + ...`.

If source drive and detector reference are coherently synthesized from one master timebase, the common oscillator phase can cancel to first order. Cable/fiber delay drift, trigger latency, DAC/ADC aperture jitter, asynchronous buffering, PLL transfer noise and differential electronics do not cancel automatically.

NIST explicitly distinguishes ADEV, which characterizes fractional-frequency instability, from TDEV, which characterizes variation of time offset. NIST dual-clock work also shows that clock distribution topology changes the observed timing offset/noise. Therefore the RQIR acceptance test must be placed on a measured differential TDEV/phase-error curve of the full source-to-detector path, not on the datasheet ADEV of one oscillator.

Relevant external metrology boundaries:

- NIST, *How UTC(NIST) Works*: ADEV estimates frequency stability; TDEV estimates time stability/holdover.
- Kast et al., NIST/IEEE 2021, *Timing Offset and Timing Stability for Dual-Clock Systems*: untethered, tethered and single-clock configurations exhibit distinct timing behavior.
- Yamamoto et al., Phys. Rev. D 105, 042009 (2022): independent detector clocks and phasemeter sampling require explicit synchronization and noise-coupling treatment.
- Xu et al., Phys. Rev. Applied 24, 014014 (2025): ADC aperture jitter and sampling-clock jitter are explicit measurement couplings in precision interferometric detection.

These references demonstrate feasibility of timing metrology far below the current microsecond RQIR toy target, but they do **not** certify an RQIR apparatus. The relevant path must be measured in situ.

## 3. RQIR-REF-001 — differential-reference rule

> The timing prior entering detector-level `F_{beta|theta}` applies to differential source-drive-to-detector-reference time error. ADEV of a single clock is insufficient; use TDEV/phase-error/relative-delay stability for the complete synchronized chain.

This sharpens RQIR-DRIFT-003 rather than replacing it.

## 4. Undoing row normalization for additive offsets

Toy009/Iteration-011 forms each raw calibration row `a_i` and then uses

`a_i,norm = a_i / ||a_i||`.

Iteration 016 adds a common normalized additive nuisance `b`, so a normalized observable is

`x_i,norm -> x_i,norm + b`.

Therefore the corresponding additive offset in the *raw Toy009 observable* is exactly

`delta x_i,raw = ||a_i|| b`.

For the current source and calibration geometry the raw row norms are:

- 7 mean rows for probe 0: `||a_i|| = 1.37174510925`;
- 7 mean rows for probe 1: `||a_i|| = 0.382088538024`;
- 8 covariance rows: norms from `0.0674024429` to `0.98271945`.

Using the corrected Iteration-016 control priors gives raw-Toy-unit one-sigma offset requirements:

### D1

- mean: `2.912e-5` to `1.045e-4` raw units;
- covariance: `6.943e-6` to `1.012e-4` raw units.

### D2

- mean: `2.461e-5` to `8.835e-5` raw units;
- covariance: `7.010e-6` to `1.022e-4` raw units.

These are exact conversions inside Toy009, not SI values.

## 5. Physical readout Jacobian

Let a physical calibration readout be

`y_i = g_i x_i,raw + o_i`,

where `g_i = d y_i / d x_i,raw` is the branch- and row-specific transduction.

Then the physical additive-offset requirement is

`boxed: sigma(o_i) <= |g_i| ||a_i|| sigma(b_group)`.

For D1, `y_i` might be a phase or population-derived phase estimate; for D2 it might be an equivalent-force estimator or a calibrated spectral amplitude. The same formula applies, but the `g_i` are different physical objects.

For covariance/PSD channels, if the fitted observable is a nonlinear statistic such as `ln S_F`, the appropriate Jacobian is the derivative of that statistic with respect to the raw Toy covariance coordinate. One must not reuse a mean-channel gain.

## 6. RQIR-CAL-008 — normalization-safe SI conversion

> Row normalization can be undone exactly, but SI conversion requires the physical readout Jacobian for each calibration row. The correct resource map is `normalized prior -> raw row norm -> physical transduction`.

This is the missing link between Iteration 016 additive priors and Iteration 022 native Fisher rates.

## 7. RQIR-NG-008 — unknown-transduction obstruction

If `g_i` is unknown or drifts without an independent calibration, a numerical row-normalized additive prior cannot be assigned a unique SI tolerance. Repeating the same normalized calibration shots does not determine the SI offset scale by itself.

This is not a new physics obstruction. It is an experimental identifiability requirement: the transfer function/readout gain must itself be calibrated or jointly inferred with an independent reference.

## 8. Consequence for wall-clock optimization

The full control pool should now be represented by measured functions/parameters:

- timing: differential `sigma_x,rel(tau)` or a fitted TDEV/PSD model;
- mean offsets: physical reference noise/drift divided by `|g_i| ||a_i||`;
- covariance offsets: physical PSD/statistic reference noise/drift divided by the corresponding covariance Jacobian;
- gain: independent reference constrained jointly with residual source-state uncertainty, per RQIR-NL-002.

Only after these are supplied can the Iteration-021 optimizer attach SI wall-clock cost to the control pools.

## 9. Current scientific conclusion

The timing requirement itself is not obviously severe relative to modern timing-transfer demonstrations; the unresolved issue is differential path stability across the actual source/control/detector chain. Additive-offset requirements are now converted out of arbitrary row normalization, but remain intentionally expressed in raw Toy units until D1/D2 transduction coefficients are specified.

This closes a normalization ambiguity and prevents another hidden `xi`-type sensitivity assumption.

## 10. Next gate

Construct branch-specific transduction models:

1. D1: raw mean/covariance coordinate -> controlled phase/contrast estimator, including finite contrast and lock-in window;
2. D2: raw mean/covariance coordinate -> equivalent-force/PSD estimator;
3. insert measured or literature-bounded differential TDEV plus additive-reference drift into the Iteration-021 wall-clock optimizer;
4. test whether D1/D2 `F_{beta|theta}` remains above the selected retention target after profiling these physical control nuisances.
