# RQIR Recovery Delta — Iteration 066

**Date:** 2026-08-30

## New retained result

Iteration 066 derives an architecture-independent wall-clock dominance boundary for Toy013 trial 29100 versus Toy009 using only Iteration-065 physical D2 ratios.

Inputs:

- science information ratio `S_eff,013/S_eff,009 = 0.04228407350`;
- calibration cost ratio `C_cal,013/C_cal,009 = 0.1233011369`;
- zero-reset Ramsey Fisher-rate ratio `R_R,013/R_R,009 = 0.003022`.

Normalize to Toy009 science time and define

`x=T_cal,009/T_sci,009`, `y=T_src,009/T_sci,009`.

Then

`T_013/T_sci,009 = 23.64956631 + 0.1233011369 x + 330.9066843 y + z`,

`T_009/T_sci,009 = 1 + x + y + z`,

for common cost `z`. Common costs cancel from the dominance inequality.

Toy013 is faster only if

`x > 25.83505838 + 376.3055916 y`.

### RQIR-RESOURCE-029

Calibration-optimality is insufficient for architecture promotion. Even with zero source-metrology cost, Toy013 requires Toy009 calibration to exceed `25.835 x` Toy009 science exposure before its calibration saving can compensate its science penalty. Nonzero Ramsey source cost makes the Toy013-winning region much narrower.

## Status

Toy013 remains a calibration-optimal local Pareto point, not the overall baseline. Toy009 remains the mature D1/D2 reference. No consistency gate is closed by this resource inequality.

Active: NG-005, NG-006, NG-023, NG-026 and all gauge/conservation/positivity/causality/EFT/renormalization/full-QFT degeneracy gates.

## Reproduce

Run:

`python analysis/toy013_vs_toy009_wallclock_dominance_iteration066.py`

Read:

`docs/TOY013_VS_TOY009_WALLCLOCK_DOMINANCE_ITERATION066.md`

`research_log/2026-08-30_iteration_066_toy013_vs_toy009_wallclock_dominance.md`

## Next front

Convert the dimensionless crossover coordinates `x,y` to SI wall-clock values by attaching one declared detector transduction/ASD model to Toy009 D2 science plus direct-force/relational mean calibration, then apply the same apparatus assumptions to Toy013. Include acceptance, reset, visibility, state-preparation throughput and coherence before architecture promotion.
