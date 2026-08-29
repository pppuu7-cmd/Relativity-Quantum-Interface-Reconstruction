# RQIR Research Log — Iteration 055 / Toy012

**Date:** 2026-08-30  
**Target:** determine whether the large Toy011 resource penalty was intrinsic to nearest-neighbour locality or an artifact of the old optimization objective.

## Two-stage search

A deterministic broader local-manifold scan (`seed=20260830`) varied Lanczos source weights, probe location and six calibration phases. Promising cheap Pareto anchors were then refined with `seed=2026083001` and evaluated by the full centered hard-constrained D2 calibration optimizer.

## Balanced Toy012 candidate

Global anchor `1638`, local mutation `182`:

- exact nearest-neighbour Hamiltonian in radius basis;
- exact spectrum `(1,2,3,4,6)`;
- rank `24/25`;
- `s_min~1.43255e-3`, condition `~3264`;
- positive hidden states and equality residual `<6e-17`.

Relative to Toy009:

- D1 raw signal `~0.17042`;
- D2 raw signal `~0.21617`;
- D1 normalized calibration cost `~1.515x`;
- D2 normalized calibration cost `~1.058x`.

Source metrology:

- `F_Q^alpha~0.0992807` (`1.169x` Toy009);
- energy-population Fisher `~0.00629727` (`0.671x`);
- Ramsey rate coefficient `max F_alpha/phi~0.00213429` (`0.846x`).

This eliminates the old `10–35x` D2 calibration penalty while keeping exact locality.

## High-response local Pareto point

Anchor `1638`, mutation `382`:

- D2 raw signal `~0.30469` Toy009;
- D2 calibration cost `~1.375x`;
- D1 raw signal `~0.25276`;
- D1 calibration cost `~5.65x`;
- `s_min~5.80e-4`, condition `~8034`;
- Ramsey rate coefficient `~1.15x` Toy009.

Retain as a D2-aggressive alternative, not the balanced baseline.

## New design rule

**RQIR-DESIGN-003 — locality penalty is objective-dependent.**

The first Toy011 scan made locality look much more expensive than it is. When centered nuisance-calibration cost and absolute detector signal are included directly in co-design, nearest-neighbour sources can approach Toy009 calibration efficiency. The remaining major penalty is absolute detector signal rather than a catastrophic nuisance geometry.

## Decision

Promote Toy012 balanced point to the leading locality-constrained source candidate. Do not replace Toy009 as mature resource baseline until the full complementary D2 branch, covariance subsets and systematics are rebuilt on Toy012.

## Files

- `analysis/toy012_resource_aware_local_codesign_iteration055.py`
- `docs/TOY_MODEL_012_RESOURCE_AWARE_LOCAL_CODESIGN.md`
- `recovery/RECOVERY_DELTA_ITERATION_055.md`

## Next gate

Reconstruct Toy012's finite-reference relational + direct-force complementary D2 Fisher branch, enumerate centered force-covariance subsets, and test whether a new detector-aligned null appears.