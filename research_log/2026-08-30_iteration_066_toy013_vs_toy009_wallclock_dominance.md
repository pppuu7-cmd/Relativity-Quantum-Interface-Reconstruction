# RQIR Research Log — Iteration 066

**Date:** 2026-08-30

## What was done

Continued from the executed Toy013 gate without reopening or duplicating closed Toy009–013 searches. Used the Iteration-065 physical spectral-tilt-profiled ratios to derive an architecture-independent total-time crossover between Toy013 trial 29100 and the mature Toy009 D2 baseline.

## Inputs retained from Iteration 065

- `S_eff,013/S_eff,009 = 0.04228407350`;
- calibration cost ratio `=0.1233011369`;
- zero-reset Ramsey rate coefficient ratio `=0.003022`.

## Result

With

- `x=T_cal,009/T_sci,009`;
- `y=T_src,009/T_sci,009`,

Toy013 beats Toy009 only if

`x > 25.83505838 + 376.3055916 y`.

Even if source metrology were free (`y=0`), Toy009 calibration must cost more than `25.835x` its science exposure before Toy013's `~8.11x` calibration saving can offset Toy013's `~23.65x` science-exposure penalty.

At nonzero Ramsey source cost the required calibration dominance rises sharply; at `y=0.1`, the threshold is `x>63.466`, and at `y=1`, `x>402.141`.

## Interpretation

Retain **RQIR-RESOURCE-029**: a calibration-optimal source can be pruned from most of resource space before an SI detector model is chosen. Toy013 remains a local Pareto point, not the baseline.

The result is optimistic for Toy013 because the source-rate ratio holds Ramsey acceptance, coupling normalization, reset regime and visibility equal. Any source-specific degradation must be inserted later.

No new-physics claim. NG-005, NG-006, NG-023, NG-026 and all open consistency gates remain active.

## Reproducibility

`analysis/toy013_vs_toy009_wallclock_dominance_iteration066.py`

`docs/TOY013_VS_TOY009_WALLCLOCK_DOMINANCE_ITERATION066.md`

## Next

Attach a physical detector transduction/ASD model to mature Toy009 D2 science and direct-force mean calibration, then propagate the same apparatus assumptions to Toy013. This converts `x,y` into seconds and tests whether the Toy013-winning region is physically reachable.
