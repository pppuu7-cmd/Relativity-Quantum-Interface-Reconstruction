# RQIR Research Log — Iteration 074

**Date:** 2026-08-30

## Question

Can a nearest-neighbour local source simultaneously reduce the science, physical calibration and independent source-metrology penalties that were split across the four local branches in Iteration 073?

## Executed search

Global cheap scan: 30,000 exact Jacobi/Lanczos candidates, seed `20260830074`. Local refinement used seed `202608300741` around global anchors `(7383,8984,8503)`, 1500 mutations per anchor. Cheap screening protected physical D2 `S_eff`, harmonic balance, `s_min`, and Ramsey/source accessibility. The top 120 local survivors were passed through the Iteration-063 spectral-tilt-profiled centered calibration audit.

The retained minimax-balanced point is anchor `8984`, mutation `578`.

Geometry:

- `q0=(0.276628448462335,0.692706589526471,0.133811514954169,0.242173595051988,0.605871859928477)`;
- `y1=-5.776797810075849`;
- phases `(0,1.282219941742947,1.828517907056411,3.566406614507335,3.168865574324793,4.280901503306583,2.751657214339520)`;
- `s_min=1.4256442476e-3`, condition `~3291.87`;
- harmonic balance `0.6684501`;
- exact far-coupling norm `~5.77e-16`, null residual `5.55e-17`, positive states.

## Physical resource vector

Relative to Toy009:

- `S_eff ratio = 0.28301465746`, hence science-time factor `q_s=3.53338589945`;
- spectral-tilt-profiled 900-point calibration cost ratio `q_c=3.48482822888`;
- full QFI `1.196x` Toy009;
- energy-population Fisher `1.632x` Toy009;
- zero-reset Ramsey rate coefficient `1.49133432x` Toy009, hence source-time factor `q_p=0.67054046`.

Thus

`(q_s,q_c,q_p)=(3.5334,3.4848,0.6705)`.

This componentwise dominates Toy011-response, Toy011-conditioning and Toy012-high in the corrected physical resource space.

New retained rule **RQIR-DESIGN-009 — multi-resource co-design can collapse a local Pareto front**. The previous spread of local specialized sources was not a fundamental locality no-go; a source search using the same physical detector and source-metrology objectives can improve several axes simultaneously.

The remaining local specialization is primarily Toy014 vs Toy013. Toy013 is still much cheaper to calibrate (`q_c=0.1233`), but Toy014 is far better in science and source metrology.

Reference boundaries:

- Toy014 beats Toy009 under the shared-kernel projected model when `y > 7.6895 + 7.5421 x`;
- Toy013 beats Toy014 when `x > 5.9842 + 98.2399 y`.

## Next

Rebuild Toy014 timing/geometry/additive control nuisance priors using the physical spectral-tilt detector metric, then insert Toy014 into the Iteration-071 general Fisher-rate wall-clock closure. Do not reuse Toy009/Toy012 control tolerances without revalidation.
