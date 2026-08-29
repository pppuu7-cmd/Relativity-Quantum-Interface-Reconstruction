# RQIR Recovery Delta — Iteration 023

**Date:** 2026-08-29

## Entering state

Iteration 022 converted white calibration/reference observables into native Fisher rates and showed that white timing-reference statistics are cheap compared with the long campaign. The open gate was low-frequency/common-mode drift.

## New model

For a reference coordinate with immediate post-calibration variance `sigma_ref^2`, random-walk diffusion `D`, and irreducible Allan/flicker floor `sigma_floor`, the interval-averaged residual variance is

`<sigma^2> = sigma_floor^2 + sigma_ref^2 + D Delta/2`.

Hence

`Delta_max = 2 (sigma_target^2 - sigma_floor^2 - sigma_ref^2)/D`,

provided the numerator is positive.

Reference duty cost is approximately

`epsilon_ref = T_ref/Delta_max`,

where `T_ref = t_cycle/p_acc * (sigma_event/sigma_ref)^2` from Iteration 022.

## New retained rules

- **RQIR-NG-007 — stability-floor obstruction:** if `sigma_floor^2 + sigma_ref^2 >= sigma_target^2`, repeated fast reference measurements and arbitrarily frequent finite cadence cannot satisfy the target nuisance prior.
- **RQIR-DRIFT-003:** once white reference Fisher is cheap, long-run control is governed by low-frequency stability (`D`, Allan floor, or full Allan/PSD curve) plus recalibration duty, not by per-event precision alone.

## Timing benchmark

At the current 100-Hz baseline, with `sigma_event=10 us`, `sigma_ref=sigma_target/3`, `1 ms` dead time and `p_acc=0.5`:

- D1 target `9.47 us`: reference block `~0.1795 s`;
- D2 target `8.01 us`: reference block `~0.2509 s`.

At timing diffusion `100 us^2/h`:

- D1 cadence `~1.594 h`;
- D2 cadence `~1.141 h`.

At `1000 us^2/h`:

- D1 `~9.57 min`;
- D2 `~6.84 min`.

For equal fractional reference allocation and equal diffusion, `Delta_D2/Delta_D1~0.715`.

These are parametric stability benchmarks, not hardware forecasts.

## Reproducibility

- `analysis/colored_drift_allan_cadence_iteration023.py`
- `docs/COLORED_DRIFT_ALLAN_CADENCE.md`
- `research_log/2026-08-29_iteration_023_colored_drift_allan_cadence.md`

## Current frontier

Next, obtain branch-specific Allan/PSD parameters for D1 clock/control and D2 sampling/reference channels, map additive-offset nuisance coordinates to physical readout units, and insert real drift-control duty fractions into the full wall-clock optimizer. Do not promote any detector hierarchy or new-physics claim until those physical stability inputs and the remaining consistency/degeneracy gates are closed.
