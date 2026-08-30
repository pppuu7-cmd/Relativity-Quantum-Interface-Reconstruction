# RQIR Recovery Delta — Iteration 076

**Date:** 2026-08-30

## Current front

Iteration 075 rebuilt Toy014 source-specific physical controls. Iteration 076 converts the timing-reference/drift model into an explicit fractional recertification duty and folds it into the projected wall clock.

## New retained result

**RQIR-RESOURCE-035 — timing recertification has a fourth-power tolerance penalty.**

Under the declared white-event reference + Brownian timing-diffusion model, with `sigma_ref=sigma_target/3` and zero floor,

`d_tau proportional to D_tau * sigma_event^2 * t_cycle / sigma_target^4`.

Thus stricter timing tolerance can increase reference duty very rapidly even if a single reference block is short.

## Toy014 vs Toy009 benchmark

Common assumptions: event jitter `10 us`, acceptance `.5`, 1-ms dead/read.

At `D_tau=100 us^2/h`:

- Toy014 duty `8.7829e-4` (`0.0878%`);
- Toy009 duty `3.5263e-5`;
- ratio `~24.91`.

At `D_tau=1000 us^2/h`:

- Toy014 duty `8.7829e-3` (`0.878%`);
- Toy009 duty `3.5263e-4`;
- ratio `~24.91`.

Control-aware Toy014-vs-Toy009 projected boundary becomes

- `D=100`: `y > 7.7118 + 7.5640 x`;
- `D=1000`: `y > 7.9178 + 7.7665 x`.

The no-control reference was `y > 7.6895 + 7.5421 x`.

Thus the stricter Toy014 timing control does not dominate the wall clock for these transparent low/moderate diffusion examples, although its relative duty penalty is large.

Toy014 reaches ~10% timing-reference duty around `D_tau=1.14e4 us^2/h` in this zero-floor model. A nonzero stability floor can close the gate earlier (NG-007).

## Reproduce

`python analysis/timing_recertification_wallclock_iteration076.py`

Primary note:

`docs/TIMING_RECERTIFICATION_WALLCLOCK_ITERATION076.md`

## Next admissible gate

Build a compact apparatus-requirement map for the surviving physical architectures Toy009, Toy014 and Toy013 using the Iteration-071 quantities:

- profiled `R_beta`;
- seven same-time matrix `R_cal,j`;
- independent `R_src`;
- control duty `d_ctrl` including timing drift/floor.

Derive which measurable rate ratios decide the architecture without inventing absolute detector ASD values.
