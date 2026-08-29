# RQIR Research Log — Iteration 018: Reference-Channel and Wall-Clock Resource Budget

**Date:** 2026-08-29

## Starting point

Iteration 017 showed that timing curvature and gain×timing are subdominant once the first-order control gate is satisfied, while common gain remains a gain×state product resource. The declared next step was to convert the surviving timing, reset/preparation and gain-reference requirements into physical reference-channel and wall-clock quantities.

## Timing/reference translation

Using `tau=2 pi f_gap t` and the corrected Iteration-016 timing priors at `f_gap=100 Hz`:

- D1 `sigma_tau=5.95e-3` -> `sigma_t=9.47 us`;
- D2 `sigma_tau=5.03e-3` -> `sigma_t=8.01 us`.

For white jitter integrated over bandwidth `B`, `J_t<=sigma_t/sqrt(B)`. At `B=1 kHz` this is about `0.299 us/sqrtHz` D1 and `0.253 us/sqrtHz` D2.

If four independent timing edges add in quadrature, the per-edge RMS bounds are about `4.73 us` D1 and `4.00 us` D2. Common-mode edge errors do not receive this square-root benefit.

## Coherence-floor correction to wall-clock examples

The current maximum phase `tau_max=4.99085067` implies `T_coh,min=7.94 ms` at `100 Hz`. Therefore a full-span shot at this gap cannot consistently be assigned an arbitrary 1-ms cycle time.

Recorded as **RQIR-RESOURCE-002**: the required coherent span is a hard lower bound in Fisher-per-second accounting.

## Corrected calibration wall time

At detector SNR 5 and equal standardized mean/covariance single-shot sensitivity `xi=10`, the corrected Iteration-015 allocations correspond to approximately:

- D1 `7.90e6` accepted calibration-shot equivalents;
- D2 `1.031e7`.

Using only the 7.94-ms coherent-span floor gives lower wall times of about `17.4 h` D1 and `22.7 h` D2. Adding `1 ms` dead time and `p_success=0.5` gives about `39.3 h` D1 and `51.2 h` D2.

These remain standardized resource examples, not hardware forecasts.

## Preparation/reset metrology

At detector SNR 5, isolated preparation-amplitude retention targets imply:

- 80%: `C_a=100`, local `sigma_a=0.10`;
- 90%: `C_a=225`, local `sigma_a=0.0667`;
- 95%: `C_a=475`, local `sigma_a=0.0459`.

The hidden amplitude must be independently characterized because it is null to the gravitational NP3 calibration.

## New wall-clock allocation law

For detector Fisher rate `R_D`, preparation-metrology rate `R_P`, and total time split between them, maximizing the two-resource profiled Fisher rate gives

`x_D=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`,

`x_P=sqrt(R_D)/(sqrt(R_D)+sqrt(R_P))`.

The optimal preparation-retention fraction is

`r*=sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`.

Recorded as **RQIR-RESOURCE-003**: wall-clock allocation follows a square-root Fisher-rate law in the two-resource local limit. A fixed 90% preparation-retention target is wall-clock optimal only if `R_P/R_D=81`.

This reclassifies previous 80/90/95% retention tables as benchmark constraints rather than universal optimal schedules.

## Gain-reference translation

Using the Iteration-017 local posterior-scale coefficient `bias/sigma_beta ~=0.325 |delta g|`:

- 0.1-sigma bias budget -> gain-reference SNR about `3.25`;
- 0.01-sigma -> `32.5`;
- 0.001-sigma -> `325`.

This is local only; arbitrary residual source error restores the product dependence `delta g * delta theta`.

## Files

- `analysis/reference_channel_wallclock_iteration018.py`
- `docs/REFERENCE_CHANNEL_WALLCLOCK_RESOURCE_BUDGET.md`
- this log

## Next gate

Construct branch-specific physical Fisher rates: D1 phase-shot/contrast/four-switch/dead-time model and D2 equivalent-force-PSD/integration/duty-cycle model, plus explicit source-metrology rate. Then optimize full `F_beta|theta` per wall-clock second rather than fixed-retention constraints.
