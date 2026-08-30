# RQIR Recovery Delta — Iteration 074

**Date:** 2026-08-30

## Current front

Iteration 073 established a four-branch locality-only Pareto front. Iteration 074 executes Toy014, a physical multi-resource nearest-neighbour co-design intended to collapse that spread.

## Executed Toy014 candidate

Search provenance:

- global seed `20260830074`, 30,000 exact local candidates;
- local seed `202608300741` around anchors `(7383,8984,8503)`, 1500 mutations each;
- cheap stage protects `s_min`, physical two-band `S_eff`, harmonic balance and source-metrology accessibility;
- top 120 local survivors audited with Iteration-063 spectral-tilt-profiled centered calibration Fisher;
- retained minimax point = anchor `8984`, mutation `578`.

Geometry:

- `q0=(0.276628448462335,0.692706589526471,0.133811514954169,0.242173595051988,0.605871859928477)`;
- `y1=-5.776797810075849`;
- phases `(0,1.282219941742947,1.828517907056411,3.566406614507335,3.168865574324793,4.280901503306583,2.751657214339520)`;
- `s_min=1.4256442476e-3`, condition `~3291.87`;
- harmonic balance `0.6684501`;
- exact locality/state/null checks pass.

## Physical resource vector vs Toy009

- `S_eff ratio = 0.28301465746` -> science-time factor `q_s=3.53338589945`;
- physical spectral-tilt calibration ratio `q_c=3.48482822888`;
- full source QFI ratio `1.19618`;
- energy-population Fisher ratio `1.63156`;
- Ramsey rate ratio `1.49133432` -> source-time factor `q_p=0.67054046`.

Thus

`(q_s,q_c,q_p)=(3.5334,3.4848,0.6705)`.

## New retained rule

**RQIR-DESIGN-009 — multi-resource co-design can collapse a local Pareto front.**

Toy014 componentwise dominates the previously retained physical local branches:

- Toy011-response;
- Toy011-conditioning;
- Toy012-high.

Toy013 remains non-dominated because its calibration factor `0.1233` is much lower, although its science/source-metrology factors are much worse.

The locality-constrained physical front is therefore reduced, among currently executed points, mainly to **Toy014 balanced vs Toy013 calibration-specialized**.

Reference projected boundaries:

- Toy014 vs Toy009: Toy014 wins if `y > 7.6895 + 7.5421 x` under shared kernels;
- Toy013 vs Toy014: Toy013 wins if `x > 5.9842 + 98.2399 y`.

## Reproduce

`python analysis/toy014_multiresource_local_codesign_iteration074.py`

Primary note:

`docs/TOY014_MULTIRESOURCE_LOCAL_CODESIGN_ITERATION074.md`

## Next admissible gate

Rebuild source-specific Toy014 timing/geometry/additive control nuisances with the physical spectral-tilt detector metric, then instantiate the Iteration-071 general `R_beta`, `R_cal,j`, `R_src` wall-clock closure. Do not import Toy009/Toy012 control priors without revalidation.
