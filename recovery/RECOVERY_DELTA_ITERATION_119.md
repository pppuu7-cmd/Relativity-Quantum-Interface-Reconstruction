# RQIR Recovery Delta — Iteration 119

**Date:** 2026-08-31  
**Parent front:** Iteration 118.

## Full eight-row covariance graph

All eight indispensable centered-covariance rows form an eight-vertex/eight-edge endpoint graph with adjacency spectrum containing

`+-sqrt(6)`, `+-sqrt(2)`.

Thus `rho(A)^2=6`.

In the affine whitened cross-covariance-only Gaussian encoding, full-hypercube positivity gives

`lambda_min(K)<1/6`,

so one all-eight joint trajectory class needs

`N_all8 > 6 gamma_cov` (NG-077).

## Exact partition optimum

Exhaustive enumeration of all 4140 edge partitions gives

`min sum_k rho(G_k)^2 = 4`.

The optimum is attained by four endpoint-disjoint two-edge matching blocks, giving

`N_cov,partition > 4 gamma_cov` (RESOURCE-089).

The optimum is exact because `rho(G_k)^2>=Delta(G_k)` and the original graph contains a degree-four hub; four matchings attain the lower bound.

Stored normalized trajectory lower bounds:

- Toy009: all-eight `>3.540763755e6`; optimal partition `>2.36050917e6`; separate edges `>4.72101834e6`;
- Toy014: all-eight `>1.63120416e7`; optimal partition `>1.08746944e7`; separate edges `>2.17493888e7`.

NG-078: endpoint-disjoint detector estimators are not automatically compatible source measurements. Iteration-041 noncommutation/backaction remains active.

## Readiness after Iteration 119

- Paper III scientific-content readiness: **92%**.
- Paper III submission readiness: **73%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/full_covariance_endpoint_partition_iteration119.py`
- `docs/PAPER_III_FULL_COVARIANCE_ENDPOINT_PARTITION_ITERATION119.md`
- `research_log/2026-08-31_iteration_119_full_covariance_endpoint_partition.md`

## Next gate

Build conservative strong-measurement and optimistic weak/shared-output calibration covers, bracket the calibration wall time, then propagate that bracket through RESOURCE-083 toward the Toy014/Toy009 detector-side ratio `u`.
