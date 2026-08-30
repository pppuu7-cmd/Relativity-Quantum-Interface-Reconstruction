# RQIR Recovery Delta — Iteration 065

**Date:** 2026-08-30

Apply this delta after the current Recovery Guide v2.8.

## New executed result

Iteration 064's Toy013 search has now been executed. Do not rerun it unless intentionally changing the search objective, seed, cuts, or survivor audit.

Retained calibration-Pareto candidate: **Toy013 trial 29100**.

Geometry:

- `q0=(0.11922119,0.26536367,0.70036208,0.09485418,0.64487523)`;
- `y1=-1.4477160194842833`;
- phases `(0,1.56834478,2.71476078,5.80286452,5.44370383,3.68646610,3.20043127)`.

Checks:

- exact nearest-neighbour Jacobi source;
- `s_min=1.3291881226e-3`, condition `3527.2295`;
- positivity minima `0.1206413852`, `0.1200000000`;
- NP3 null residual `5.55e-17`;
- harmonic balance `0.9047551404`;
- normalized spectral-tilt-profiled beta Fisher = 1.

Physical D2 calibration audit:

- weighted cost `3.5819942712e6`;
- `gamma_mean=1.2086865290e5`;
- `gamma_cov=2.3622914132e5`;
- cost ratio vs Toy009 `0.1233011369`.

But absolute D2 `S_eff` ratio is only `0.04228407350`, implying ~`23.65x` Toy009 science exposure at equal detector noise, and Ramsey source-metrology rate coefficient ratio is only `0.003022` (~331x slower in the same normalized coupling coordinate).

## New rule

**RQIR-DESIGN-006:** never promote a source from calibration cost alone. The minimum physical comparison is the joint tuple

`(absolute science Fisher rate, nuisance-calibration rate, independent source-metrology rate, reset/dead/coherence/control cost)`.

Toy013 trial 29100 is retained only as a calibration-optimal local Pareto point.

## Active front

Next non-duplicative gate: common wall-clock comparison Toy009/Toy011/Toy012/Toy013. Preserve NG-005, NG-006, NG-023, NG-026 and all G-series consistency gates. Do not claim new physics.

Reproducible execution: `analysis/toy013_execution_iteration065.py`.
