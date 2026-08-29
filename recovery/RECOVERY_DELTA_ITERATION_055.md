# RQIR Recovery Delta — Iteration 055 / Toy012

**Date:** 2026-08-30

Apply after Iteration 054.

## New retained source candidate

Toy012 is a resource-aware exact nearest-neighbour refinement of Toy011.

Balanced candidate: global anchor `1638`, local mutation `182` from deterministic seeds `20260830` and `2026083001`.

Geometry:

- `q0=(0.182446543760,0.684368939221,0.165591352865,0.679324856717,0.097209344214)`;
- `y1=-2.94878656991`;
- phases `(0,1.038867458294,2.985962997881,4.875819177097,4.150899563476,1.623915172581,5.275220686287)`.

Exact properties:

- nearest-neighbour/tridiagonal site Hamiltonian with spectrum `(1,2,3,4,6)`;
- rank `24/25`;
- `s_min=1.43254596e-3`;
- condition `~3264.22`;
- positive states;
- equality residual `<6e-17`.

## Resource metrics relative to Toy009

Balanced Toy012:

- D1 raw detector signal Fisher proxy `0.17042`;
- D2 raw detector signal Fisher proxy `0.21617`;
- D1 centered calibration cost `1.515x`;
- D2 centered calibration cost `1.058x`.

Source metrology:

- `F_Q^alpha=0.0992807` (`1.169x` Toy009);
- energy-population Fisher `0.00629727` (`0.671x`);
- Ramsey rate coefficient `max F_alpha/phi=0.00213429` (`0.846x`).

Thus the old Toy011 `10–35x` D2 calibration penalty is **not** intrinsic to nearest-neighbour locality.

## High-response local Pareto alternative

Anchor `1638`, mutation `382`:

- D2 raw signal `0.30469` Toy009;
- D2 calibration cost `1.375x`;
- D1 raw signal `0.25276`;
- D1 calibration cost `5.65x`;
- `s_min~5.80e-4`, condition `~8034`;
- Ramsey rate coefficient `~1.15x` Toy009.

## New rule

**RQIR-DESIGN-003 — locality penalty is objective-dependent.**

Resource-aware co-design can recover near-Toy009 centered calibration efficiency inside the exact nearest-neighbour source manifold. The leading remaining penalty is absolute detector signal, not nuisance identifiability.

## Baseline decision

- Toy009 remains the mature statistical/resource baseline.
- Toy012 balanced becomes the leading locality-constrained source candidate.
- Do not promote Toy012 to global baseline until complementary D2, covariance subsets and systematics are rebuilt.

## Next continuation step

Reconstruct the finite-reference relational + direct-force complementary D2 branch on Toy012 balanced:

1. relational means/covariances at finite `y_ref`;
2. direct force means;
3. centered force-covariance subset enumeration;
4. full `F_beta|theta` and `C_alpha` profiling;
5. compare branch0/best4/best5 structure with Toy009.