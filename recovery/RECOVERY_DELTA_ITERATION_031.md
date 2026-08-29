# RQIR Recovery Delta — Iteration 031

**Date:** 2026-08-29

## New confirmed result

Finite-reference D2 relational-potential calibration was propagated through the corrected hard-constrained profiled Fisher while keeping the original Toy009 hidden source fixed.

The calibration obtains nonzero Fisher information on the old hidden amplitude, but beta remains effectively non-identifiable at `C_a=0` because the one-dimensional exact calibration null rotates into a nearby detector-aligned source direction.

Representative corrected results:

- `y_ref=-5`: `F_beta|theta~8.1742e-5`, old-amplitude calibration Fisher `~3.18167`, new-null detector alignment `~0.9999573`;
- `y_ref=-10`: `F_beta|theta~1.2329e-5`, amplitude Fisher `~0.671908`, alignment `~0.9999936`;
- `y_ref=-100`: `F_beta|theta~1.2490e-8`, amplitude Fisher `~2.8486e-4`, alignment `~0.999999993`.

## New negative gate

**RQIR-NG-012 — relational-null substitution obstruction:** calibration information on one formerly hidden amplitude is not sufficient for identifiability of beta if the full nuisance space contains another exact null whose detector response is aligned with the beta signal.

Do not use `I_cal(old amplitude)>0` as a surrogate for profiled `F_beta|theta`.

## Resource consequence

At current corrected D2 calibration scale `lambda=1`, 90%-retention preparation requirements are approximately:

`C_a*=15.48,16.65,19.36,21.92,31.59,59.67,106.20`

for `y_ref=-4,-5,-7.5,-10,-20,-50,-100` respectively.

Moving `y_ref` outward therefore has a double penalty:

1. finite-reference potential transduction slows through Iteration-030 `q_pot` suppression;
2. the profiled Fisher geometry approaches the original NP3-null geometry, increasing independent source-metrology demand.

## Reproducibility

- `analysis/d2_finite_reference_profiled_fisher_iteration031.py`
- `docs/D2_FINITE_REFERENCE_PROFILED_FISHER.md`
- `research_log/2026-08-29_iteration_031_d2_finite_reference_profiled_fisher.md`

## Next action

Optimize the relational branch jointly over `y_ref`, calibration exposure `lambda`, and source Fisher `C_a` using heterogeneous per-row native potential rates from Iteration 030. Compare the optimized wall-clock frontier against native-force replacement and augmented potential+force calibration. Keep timing/reference duty separate until physical Allan/PSD parameters are supplied.
