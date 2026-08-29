# RQIR Research Log — Iteration 023

**Date:** 2026-08-29

## Target

Advance the Iteration-022 frontier: replace static white timing/additive reference priors by a colored-drift/Allan-variance cadence model and determine what repeated calibration can and cannot cure.

## Source-of-truth review

Re-read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, the latest Iteration-022 research log/recovery delta, Toy009, Toy010 and Statistical Identifiability 002. Retained mandatory constraints include RQIR-NG-005, the Iteration-015 hard-constraint correction, RQIR-NG-006, and the D1/D2 first-order timing targets.

## Work completed

1. Added a minimal physical drift model with white reference-estimation variance, Brownian/random-walk drift diffusion `D`, and an optional irreducible Allan/flicker floor.
2. Derived the time-averaged residual variance over a recalibration interval:
   `sigma_avg^2 = sigma_floor^2 + sigma_ref^2 + D Delta/2`.
3. Derived the maximum feasible cadence:
   `Delta_max = 2 (sigma_target^2-sigma_floor^2-sigma_ref^2)/D`.
4. Combined this with the Iteration-022 native reference-block cost to obtain the control-duty penalty `epsilon ~= T_ref/Delta_max`.
5. Added an explicit infeasibility test when the Allan/reference floor exhausts the target prior.
6. Repeated the calculation for both current D1 and D2 timing requirements.

## Numerical checks

Using the existing `f_gap=100 Hz`, `tau_max=4.99085067`, `1 ms` dead time, `p_acc=0.5`, `sigma_event=10 us`, and choosing `sigma_ref=sigma_target/3`:

- D1 reference block: `~0.1795 s`;
- D2 reference block: `~0.2509 s`.

For random-walk timing diffusion `D=100 us^2/h`:

- D1 maximum average-variance cadence: `~1.594 h`;
- D2: `~1.141 h`.

For `D=1000 us^2/h`:

- D1: `~9.57 min`;
- D2: `~6.84 min`.

Despite the shorter cadence, white-reference duty overhead remains very small in this benchmark because the reference blocks themselves are short.

At equal fractional reference allocation and equal physical diffusion,
`Delta_D2/Delta_D1=(8.01/9.47)^2~0.715`.

## New retained results

**RQIR-NG-007 — stability-floor obstruction:** if an Allan/flicker floor plus immediate reference-estimation variance already meets or exceeds the detector-required nuisance variance, no amount of fast repeated reference sampling or finite recalibration cadence can restore the target prior.

**RQIR-DRIFT-003:** once white-event reference Fisher is cheap, long-campaign control must be budgeted by low-frequency stability parameters `(D, sigma_floor)` or a measured Allan-deviation curve, plus recalibration duty fraction, not by event timestamp precision alone.

## Scientific status

No new-physics claim. No relativistic/QFT/gauge/conservation gate is closed. This iteration sharpens the experimental/systematics part of G13 only.

## Files

- `analysis/colored_drift_allan_cadence_iteration023.py`
- `docs/COLORED_DRIFT_ALLAN_CADENCE.md`
- `recovery/RECOVERY_DELTA_ITERATION_023.md`

## Next gate

Use branch-specific measured or literature-justified Allan/PSD models for D1 clock/control and D2 sampling/reference channels; convert additive-offset nuisance coordinates to physical readout units; then insert actual drift cadence and reference duty cost into the full Iteration-021 `F_beta|theta/T_wall` optimizer.
