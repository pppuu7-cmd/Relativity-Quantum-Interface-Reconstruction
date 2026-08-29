# RQIR Iteration 040 — D2 Covariance Graph Congestion and Subset Resource Dominance

**Date:** 2026-08-29  
**Scope:** centered D2 covariance subset selection at `y_ref=-4`, `lambda=1`.  
**Status:** detector-architecture/resource result; no new-physics claim.

## 1. Question

Iteration 039 showed that shared detector endpoints reduce the per-shot covariance Fisher of the best four rows. The next resource question is whether adding more covariance rows is always beneficial once they are measured in one joint trajectory.

The centered Fisher geometry from Iteration 034 gives:

- best four `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best five `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all eight: `F_beta~0.905293`, `C_alpha*=0`.

At rank/Fisher level, adding the fifth row looks attractive because it removes the remaining source prior. But in a shared cross-covariance detector, an added edge can increase the spectral radius of the entire endpoint graph, reducing the maximum admissible covariance modulation for **all** simultaneously acquired rows.

## 2. Full eight-row endpoint graph

Use the eight unique covariance endpoints

- `G0@0`, `G1@0`,
- `G0@TR`, `G0@T1`, `G1@T5`, `G1@TR`, `G1@T3`, `G0@T6`.

The eight covariance rows correspond to graph edges

`0:(0,2), 1:(1,3), 2:(1,4), 3:(0,5), 4:(1,2), 5:(0,6), 6:(0,7), 7:(1,7)`.

For a natural uniform cross-covariance encoding

`H_e=a(E_uv+E_vu)`,

full-hypercube positivity requires

`a rho(A_G)<1`,

where `rho(A_G)` is the spectral radius of the endpoint graph adjacency matrix.

Thus the maximum per-edge covariance Fisher is

`K_ee < 1/rho(A_G)^2`.

## 3. Graph congestion for the retained subsets

### Best four `(0,1,3,7)`

`rho^2=2`, hence

`K_edge<1/2`.

Accepted shared-cycle lower bound:

`N4>1.180254e6`.

### Best five `(0,1,3,6,7)`

The fifth edge connects the previously simpler shared-endpoint structure and raises

`rho^2=(5+sqrt(5))/2 ~= 3.61803399`.

Hence

`K_edge<0.2763932`

and

`N5>2.135100e6`.

### All eight rows

The full graph has

`rho=sqrt(6)`,

so

`K_edge<1/6`

and

`N8>3.540762e6`.

## 4. RQIR-RESOURCE-015 — covariance graph congestion

> In a shared cross-covariance detector, adding a calibration row can increase the spectral radius of the endpoint graph and thereby reduce the admissible per-shot Fisher of every simultaneously acquired covariance edge. Row count is therefore not a monotone resource improvement even when profiled Fisher increases.

The relevant subset objective is not only

`Delta F_beta` or `Delta C_alpha`,

but the gain divided by the **graph-congestion cost** of the joint detector likelihood.

This is an experimental-design/resource result, not a fundamental statement about all possible quantum measurements.

## 5. Best four versus best five

The fifth row removes only the residual

`C_alpha=0.0500614`

left after the best four.

With corrected

`F_Q^(alpha)=0.0849323916`,

that residual prior corresponds to only

`~0.58943`

accepted single-branch source-metrology copy equivalents.

But because the fifth edge increases graph congestion, the ideal accepted covariance-cycle lower bound rises from

`1.180254e6`

to

`2.135100e6`,

an increase of about

`9.54846e5`

shared detector trajectories.

Therefore best five can beat best four + minimal source metrology only if

`boxed:
(p_C eta_C)/(p_P eta_P) * t_P/t_C > ~1.61996e6`.

At equal efficiencies and the 100-Hz coherence floor `t_C>=7.94319 ms`, this requires

`boxed: t_P > ~1.2868e4 s ~= 3.57 h`.

With a transparent `1 ms` detector dead/readout time:

`boxed: t_P > ~1.4488e4 s ~= 4.02 h`.

So for the fixed 90% target, the fifth covariance row is resource-competitive only if independent source verification is extraordinarily slow relative to the covariance trajectory.

## 6. Best five versus all eight

Both best five and all eight already have

`C_alpha*=0`

at `lambda=1` and both exceed the 90% target.

Yet the cross-covariance graph lower bounds are

- best five: `N>2.1351e6`;
- all eight: `N>3.5408e6`.

Therefore, for a **fixed 90% target and covariance-only replacement objective**, all eight rows are resource-dominated by the best five under this joint cross-covariance architecture.

The additional three rows can still be justified by:

- a higher target than 90%;
- robustness against model error/drift;
- other nuisance directions;
- simultaneous acquisition at negligible additional detector complexity;
- a non-cross-covariance measurement architecture with different Fisher geometry.

Those benefits must be demonstrated explicitly rather than inferred from larger raw Fisher.

## 7. Comparison of whole-subset break-even ratios

Relative to the relational-covariance-only baseline `C_alpha=4.55511`:

- best four saves `~53.04` source-copy equivalents and needs ideal `t_P/t_C > ~2.2251e4`;
- best five saves `~53.63` copy equivalents and needs `>~3.9810e4`;
- all eight save the same `~53.63` copy equivalents but need `>~6.6019e4`.

Thus beyond the high-value core rows, covariance graph congestion grows much faster than the source-metrology saving.

## 8. Scientific interpretation

The current D2 calibration architecture now has a clearer resource structure:

1. covariance rows are valuable because of their nuisance-space orientation;
2. shared acquisition is necessary to avoid naive row-time summation;
3. shared endpoints create their own positivity/information bottleneck;
4. adding rows can make the joint covariance readout **less** efficient per cycle;
5. a small independent source prior can be dramatically cheaper than geometrically completing the covariance bundle.

This strongly favors a hybrid resource strategy around the 90% target: retain the high-value covariance core and use a small amount of independent source metrology, unless hardware proves source verification extremely slow.

## 9. Reproducibility

Code:

`analysis/d2_covariance_graph_congestion_iteration040.py`

The script reconstructs the endpoint graph, verifies spectral radii for best4/best5/all8, converts them to per-edge Fisher ceilings and accepted-cycle lower bounds, and derives the best5-vs-best4+prep wall-clock crossover.

## 10. Next gate

Build the joint **mean + covariance** phase-referenced detector likelihood on the same endpoint record. The covariance-only analysis now strongly suggests that the only plausible way for the complementary detector branch to beat source metrology is for the same long coherent trajectory to earn substantial force-mean and control Fisher at no comparable extra cycle cost.
