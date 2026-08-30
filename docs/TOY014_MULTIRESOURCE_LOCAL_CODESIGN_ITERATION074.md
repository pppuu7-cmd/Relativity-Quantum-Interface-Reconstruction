# RQIR Iteration 074 — Executed Toy014 Physical Multi-Resource Local Co-Design

**Date:** 2026-08-30  
**Status:** executed deterministic local-source search/audit; physical resource Pareto result; no global-optimum, apparatus-feasibility or new-physics claim.

## 1. Why Toy014 was needed

Iteration 073 showed that the corrected nearest-neighbour local-source family had four resource-specialized branches:

- Toy011-response: strongest science axis among the retained older local points;
- Toy011-conditioning: better calibration/source compromise;
- Toy012-high: best Ramsey source-metrology axis but catastrophic science/calibration;
- Toy013: excellent spectral-tilt-profiled calibration but catastrophic Ramsey source metrology.

The correct next question was therefore not “maximize response” or “minimize calibration,” but whether a source can **collapse this Pareto spread** while keeping exact nearest-neighbour locality and the full physical two-band detector likelihood.

## 2. Executed search

The Toy014 search was executed in the same exact-spectrum Jacobi/Lanczos nearest-neighbour manifold.

Search provenance:

- global seed `20260830074`;
- `30,000` global cheap-stage candidates;
- cheap stage protected:
  - NP3 smallest singular value;
  - physical spectral-tilt-profiled D2 `S_eff`;
  - explicit `n=2/n=4` harmonic-balance floor;
  - energy/Ramsey source-metrology accessibility;
- local seed `202608300741`;
- local refinement around global anchors `(7383, 8984, 8503)`;
- `1500` mutations per anchor;
- top 120 local survivors by the declared cheap multi-resource composite were sent to the expensive Iteration-063 spectral-tilt-profiled centered calibration audit.

The retained **minimax-balanced** point is

`anchor 8984 / local mutation 578`.

No claim is made that this is the global optimum of the full local manifold.

## 3. Toy014 geometry

`q0 = (0.276628448462335, 0.692706589526471, 0.133811514954169, 0.242173595051988, 0.605871859928477)`

`y1 = -5.776797810075849`

phases:

`(0, 1.282219941742947, 1.828517907056411, 3.566406614507335, 3.168865574324793, 4.280901503306583, 2.751657214339520)`.

Exact checks:

- nearest-neighbour far-coupling norm `~5.77e-16`;
- NP3 `s_min = 1.4256442476e-3`;
- condition `~3291.873`;
- positive hidden-state minima `0.1214272` and `0.1200000`;
- selected calibration-null residual `5.55e-17`;
- normalized tilt-only profiled beta Fisher `1`;
- physical D2 harmonic power balance `~0.66845`.

Thus Toy014 does **not** reproduce the Toy012 failure mode of hiding almost all response in one harmonic.

## 4. Physical science axis

The equal-ASD spectral-tilt-profiled D2 information is

`S_eff,014 = 1.6356852494e-4`.

Relative to Toy009:

`S_eff,014/S_eff,009 = 0.28301465746`.

Therefore the same-kernel science-time factor is

`boxed{q_s = 3.53338589945}`.

This is a major improvement over all prior retained local physical branches:

- Toy011-response: `~6.42`;
- Toy011-conditioning: `~12.25`;
- Toy012-high: `~8237`;
- Toy013: `23.65`.

Toy014 still does not beat Toy009 on raw science exposure; it reduces the locality penalty to about `3.53x` in the declared physical D2 metric.

## 5. Physical calibration axis

Using the same 900-point spectral-tilt-profiled centered calibration allocation as Iteration 063:

Toy014:

- total cost `1.0123698016e8`;
- `gamma_mean = 5.6776851e6`;
- `gamma_cov = 2.7186736e6`.

Toy009 in the same execution:

- total cost `2.9050780559e7`.

Therefore

`boxed{q_c = 3.48482822888}`.

Toy014 is not as calibration-efficient as Toy009 or Toy013, but it is dramatically better than the older local points:

- Toy011-response `~21.7`;
- Toy011-conditioning `~8.83`;
- Toy012-high `>490` in the conservative Iteration-063 bound.

## 6. Source-metrology axis improves rather than collapses

Toy014 source-side information is healthy:

- full `F_Q^alpha = 0.1015944563`, about `1.196x` Toy009;
- energy-population Fisher `F_E^alpha = 0.01532342451`, about `1.632x` Toy009;
- Ramsey Fisher/sec optimum:
  - `phi ~= 0.92642951`;
  - `max F_alpha/phi = 0.00376329150`;
  - rate ratio to Toy009 `= 1.49133432`.

Hence the independent Ramsey source-metrology time factor is

`boxed{q_p = 0.67054046}`.

Unlike Toy013, Toy014 does **not** buy calibration performance by making the hidden source amplitude difficult to measure. It is actually faster than Toy009 in the current zero-reset Ramsey class.

## 7. Main Pareto result

Toy014 resource vector is approximately

`boxed{(q_s,q_c,q_p) = (3.5334, 3.4848, 0.6705)}`.

It componentwise dominates all three pre-Toy013 local physical branches retained in Iteration 073:

- Toy011-response `(6.418, 21.7, 3.759)`;
- Toy011-conditioning `(12.250, 8.83, 2.384)`;
- Toy012-high `(8237, >490, 0.869)`.

### RQIR-DESIGN-009 — multi-resource co-design can collapse a local Pareto front

> When the physical detector nuisance, absolute science information and source-metrology accessibility are placed inside the source search, a new local source can simultaneously improve several previously conflicting resource axes. The earlier Pareto plurality was therefore not a fundamental locality no-go; it was partly a consequence of optimizing different source designs for different incomplete objectives.

The locality-only physical Pareto front is now reduced substantially. Among the retained candidates, the main specialization pair becomes

- **Toy014:** balanced science + calibration + strong source metrology;
- **Toy013:** calibration-specialized extreme.

Toy013 remains non-dominated because its calibration factor `0.1233` is still much lower than Toy014's `3.485`, while Toy014 is overwhelmingly better in science and source metrology.

## 8. Toy014 vs Toy009

Under the projected shared-kernel wall-clock model,

Toy014 beats Toy009 when

`3.5334 + 3.4848 x + 0.67054 y < 1+x+y`.

Equivalently,

`boxed{y > 7.6895 + 7.5421 x}`.

This is still a conditional architecture region: Toy014 needs the Toy009 baseline to be sufficiently source-metrology dominated because Toy014 is slower on science and calibration but faster on source metrology.

The important improvement is scale. Toy012-high required roughly

`y > 6.3e4 + 3.7e3 x`.

Toy014 reduces that rescue boundary by orders of magnitude.

## 9. Toy014 vs Toy013

Using the retained Iteration-065/066 Toy013 factors, Toy013 wins over Toy014 only when calibration weight is very large:

`boxed{x > 5.9842 + 98.2399 y}`.

At `y=0`, Toy013 needs `x>~5.98` to justify its calibration specialization. As soon as source-metrology time has appreciable weight, its huge Ramsey penalty rapidly shrinks its winning region.

## 10. What is and is not established

Established:

- a new exact nearest-neighbour source exists that preserves both D2 bands;
- it has healthy QFI, energy-population and Ramsey source metrology;
- after the full spectral-tilt-profiled calibration audit it componentwise dominates the older Toy011 and Toy012-high physical local branches;
- the apparent locality tradeoff is substantially smaller than previously found.

Not established:

- global optimality of Toy014;
- apparatus-specific seconds/hours;
- source-specific detector transfer equality required by shared-kernel ratios;
- timing/additive/control priors rebuilt for Toy014;
- relativistic conservation, QFT, stochastic/classical degeneracy, renormalization or experimental feasibility gates;
- any new physics.

## 11. Reproducibility

Code:

`analysis/toy014_multiresource_local_codesign_iteration074.py`

The code reconstructs the final candidate, reruns exact locality/state/null checks, recomputes the Iteration-063 900-point physical calibration allocation, source QFI/energy/Ramsey metrics, Pareto dominance, and Toy014/Toy009/Toy013 crossover formulas.

## 12. Next gate

Toy014 should now replace Toy011/Toy012 as the **leading balanced locality-constrained D2 source candidate**, while Toy013 remains the calibration-specialized comparison branch.

The next admissible calculation is source-specific detector/control closure for Toy014:

1. rebuild timing/geometry/additive systematics with the physical spectral-tilt detector metric;
2. insert Toy014 into the Iteration-071 general `R_beta, R_cal,j, R_src` wall-clock closure;
3. derive the source-specific transfer/PSD rescue surface versus Toy009 and Toy013;
4. only then consider a broader Toy015 search or apparatus instantiation.
