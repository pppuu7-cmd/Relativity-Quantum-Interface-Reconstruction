# RQIR Toy Model 012 — Resource-Aware Local Source Co-Design

**Iteration:** 055  
**Date:** 2026-08-30  
**Status:** exact nearest-neighbour local-source redesign with centered resource-aware scoring; not a global optimum, hardware design, or new-physics claim.

## 1. Why Toy012 was needed

Toy011 proved that the RQIR ordered-response discriminator survives an exactly local nearest-neighbour five-site source Hamiltonian. Iteration 054 then showed that the two original Toy011 Pareto points were badly ranked by the quantities that actually matter experimentally:

- absolute detector signal;
- centered nuisance-calibration cost;
- source-metrology rate.

The old Toy011 search used exact conditioning and raw response proxies as its main objective. That was sufficient for a locality existence proof, but not for resource optimization.

Toy012 repeats the local source/calibration co-design with the resource structure exposed by Iteration 054.

## 2. Search domain

The exact locality construction is unchanged:

- five physical radius sites with Toy009 radii;
- exact spectrum `E=(1,2,3,4,6)`;
- a Jacobi/Lanczos site Hamiltonian that is exactly nearest-neighbour;
- finite NP3 calibration family;
- positive hidden-state pair `rho_±=I/5±0.08 Delta0`.

A two-stage deterministic search was used.

### Stage A — broader local-manifold scan

Seed `20260830` varied

- positive Lanczos spectral weights;
- second probe position;
- six nonzero calibration phases.

Cheap Pareto screening used absolute D2 signal and normalized calibration conditioning. The promising anchors were then passed through the full centered hard-constrained calibration optimizer from Iteration 054.

### Stage B — local refinement

Seed `2026083001` perturbed the strongest global anchors at several scales and re-evaluated the explicit centered D2 calibration cost.

No global-optimum claim is made.

## 3. Balanced Toy012 point

The preferred balanced local point is the refinement of global anchor `1638`, local mutation `182`.

### Source spectral weights

`q0 = (0.182446543760, 0.684368939221, 0.165591352865, 0.679324856717, 0.097209344214)`.

### Calibration geometry

`y1 = -2.94878656991`.

Phases:

`(0, 1.038867458294, 2.985962997881, 4.875819177097, 4.150899563476, 1.623915172581, 5.275220686287)`.

### Exact local Hamiltonian

In the radius/site basis,

```text
H_site ≈
[[2.954897, 1.070515, 0,        0,        0],
 [1.070515, 3.074552, 0.890550, 0,        0],
 [0,        0.890550, 4.268129, 2.121488, 0],
 [0,        0,        2.121488, 2.759606, 0.470961],
 [0,        0,        0,        0.470961, 2.942816]]
```

All entries beyond nearest neighbours vanish to numerical precision; the exact eigenvalues remain `(1,2,3,4,6)`.

### Exact/null properties

- calibration rank `24/25`;
- `s_min ≈ 1.43255e-3`;
- condition `≈3264.22`;
- positive states, minimum eigenvalues `rho_+≈0.1200`, `rho_-≈0.1236`;
- selected equality residual `<6e-17`.

Thus the locality/null/discriminator conditions remain exact.

## 4. Major improvement over Toy011

Relative to the practical Toy009 baseline:

### Absolute detector signal

- D1 raw two-band Fisher proxy: `0.17042`;
- D2 raw two-band Fisher proxy: `0.21617`.

So the D2 science-time penalty at equal detector noise is now about

`1/0.21617 ≈ 4.63x`.

This is still a real penalty, but it is far smaller than the weakest local candidates and comes with much better calibration geometry.

### Centered calibration cost

The 90%-retention normalized cost ratios are

- D1: `1.515x` Toy009;
- D2: `1.058x` Toy009.

The D2 calibration penalty that was `10–35x` for the original Toy011 points has therefore collapsed to only about **6% above Toy009**.

This is the central Toy012 result.

## 5. Source metrology is also healthy

For the fractional hidden amplitude:

`F_Q^(alpha) ≈ 0.0992807`,

which is about `1.169x` Toy009.

Simple energy-population Fisher is

`F_E^(alpha) ≈ 0.00629727`,

about `0.671x` Toy009.

For independent QND Ramsey-ancilla metrology, the rate optimum is

- `phi_rate ≈ 1.57508`;
- `max F_alpha/phi ≈ 0.00213429`.

This retains about

`0.846x`

of the Toy009 Ramsey Fisher-rate coefficient.

Thus the balanced local source does not require exotic source metrology to compensate for locality.

## 6. High-response local Pareto point

A second refinement of the same global anchor, mutation `382`, is retained as an aggressive D2 point.

It gives approximately

- D2 raw signal: `0.30469` of Toy009;
- D2 calibration cost: `1.375x` Toy009;
- D1 raw signal: `0.25276`;
- D1 calibration cost: `5.65x` Toy009;
- `s_min≈5.80e-4`, condition `≈8034`;
- Ramsey source-metrology rate coefficient `≈1.15x` Toy009.

This candidate has substantially more raw D2 response, but poorer conditioning and a much larger D1 calibration burden. It is therefore a Pareto alternative rather than the preferred balanced point.

## 7. RQIR-DESIGN-003 — locality penalty is objective-dependent

> The large resource penalty seen in the first locality-constrained scan is not an unavoidable consequence of nearest-neighbour source dynamics. Once absolute detector signal and centered nuisance-calibration cost are included directly in source/calibration co-design, local candidates can recover near-Toy009 calibration efficiency while retaining a finite fraction of Toy009 detector signal.

This is a numerical design result in the current five-site manifold, not a theorem that arbitrary realistic local sources can achieve the same tradeoff.

## 8. What Toy012 changes

Before Toy012, locality appeared to cost either

- acceptable response with `~35x` D2 calibration burden, or
- acceptable conditioning with `~10x` D2 calibration burden and very weak signal.

Toy012 removes that apparent dichotomy:

`exact locality + rank 24/25 + positive hidden states + nonzero ordered response + ~Toy009 calibration cost`

are simultaneously achievable.

The remaining dominant penalty is now **absolute detector signal**, not nuisance geometry.

That is scientifically important because absolute signal can in principle be attacked by source mass, separation, detector PSD, coherence and source geometry, whereas a catastrophic nuisance degeneracy would have been much harder to repair.

## 9. Baseline decision

Toy012 is promoted to the **leading locality-constrained source candidate**, but not yet to the global RQIR statistical baseline.

Toy009 remains the reference for the mature D1/D2 resource machinery until Toy012 is passed through:

- the complementary relational/force D2 branch;
- centered covariance subset optimization;
- timing/additive systematics;
- physical source-metrology rate boundaries;
- a common SI detector budget.

## 10. Reproducibility

Code:

`analysis/toy012_resource_aware_local_codesign_iteration055.py`

It reconstructs the deterministic global anchors and local mutations, verifies exact nearest-neighbour locality and state positivity, and recomputes centered D1/D2 calibration, QFI, energy-population Fisher and Ramsey Fisher-rate metrics.

## 11. Next gate

Carry the balanced Toy012 source through the **same complementary D2 architecture** that currently makes Toy009 useful:

1. finite-reference relational potential rows;
2. direct force means;
3. centered relational covariance;
4. centered force-covariance subset enumeration;
5. source-amplitude metrology and `F_beta|theta` profiling.

The key question is whether Toy012's near-baseline NP3 calibration cost survives when the physically preferred complementary D2 branch is reconstructed, or whether a new detector-aligned relational null appears.