# RQIR Iteration 065 — Toy013 executed physical D2 gate

**Date:** 2026-08-30

## Status

Iteration 064 defined a deterministic nearest-neighbour Toy013 search but did not execute it. Iteration 065 executes that gate with the same seed and candidate definition, then profiles the relative two-band spectral-tilt nuisance using the Iteration-063 centered calibration Fisher.

No global-optimum or new-physics claim is made.

## Search

- seed `20260830064`;
- 30,000 exact nearest-neighbour Jacobi candidates;
- `s_min >= 7.5e-4`;
- harmonic balance `min(|G2|^2,|G4|^2)/max(...) >= 0.06`;
- 137 candidates survived the hard cheap-stage cuts;
- the best 120 were carried to the physical Fisher audit.

The retained candidate is trial **29100**:

- `q0=(0.11922119,0.26536367,0.70036208,0.09485418,0.64487523)`;
- `y1=-1.4477160194842833`;
- phases `(0,1.56834478,2.71476078,5.80286452,5.44370383,3.68646610,3.20043127)`;
- `s_min=1.3291881226e-3`;
- condition `3527.2295`;
- harmonic balance `0.9047551404`.

Exact checks:

- non-nearest-neighbour Hamiltonian norm `3.42e-16`;
- hidden-state minima `0.1206413852` and `0.1200000000`;
- calibration-null residual `5.55e-17`;
- tilt-only normalized profiled beta Fisher `1.0000000000000002`.

## Physical spectral-tilt-profiled calibration result

Toy013 trial 29100 requires

`cost = 3.5819942712e6`

in the Iteration-063 weighted calibration coordinate, with

- `gamma_mean = 1.2086865290e5`;
- `gamma_cov = 2.3622914132e5`;
- uniform threshold `1.8050247460e5`.

The same executed optimizer gives Toy009

`cost = 2.9050780559e7`.

Therefore

`Toy013/Toy009 calibration cost = 0.1233011369`.

This is a genuine improvement in nuisance-calibration geometry after spectral-tilt profiling.

## Important counter-costs

The absolute physical two-band D2 information is

`S_eff = 2.4438110707e-5`,

only

`S_eff(Toy013)/S_eff(Toy009) = 0.04228407350`.

Thus equal-noise science exposure scales approximately as `1/S_eff`; Toy013 would need about `23.65x` the Toy009 science exposure before other wall-clock terms are included.

Independent source metrology is also poor for this candidate:

- full source `F_Q^alpha = 0.08073047882`, about `0.9505x` Toy009;
- energy-population `F_E^alpha = 4.54142493e-5`, only `0.004835x` Toy009;
- zero-reset Ramsey rate coefficient `F_R/phi = 7.6258e-6`, about `0.003022x` Toy009.

So the calibration improvement is accompanied by a severe energy-diagonal source-metrology penalty.

## Retained result — RQIR-DESIGN-006

A source that is excellent after detector nuisance profiling can still be poor in total experiment time because calibration geometry, absolute detector signal, and independent source-metrology accessibility are distinct resource axes.

Toy013 trial 29100 is therefore retained as a **calibration-optimal local Pareto point**, not as the new overall RQIR baseline.

## Next gate

Put Toy009, Toy011, Toy012 and Toy013 on one common total-time objective containing at minimum:

`T_total = T_science + T_mean/cov calibration + T_source metrology + T_controls + T_reset/dead/coherence`.

For Toy013 the critical question is whether its `~8.11x` calibration saving relative to Toy009 can ever compensate both its `~23.65x` science-exposure penalty and its `~331x` worse Ramsey source-metrology rate coefficient. Until that wall-clock comparison is done, promotion is not justified.
