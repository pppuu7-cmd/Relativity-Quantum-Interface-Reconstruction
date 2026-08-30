# RQIR Iteration 119 — Full Eight-Row Covariance Endpoint Graph and Optimal Partition

**Date:** 2026-08-31  
**Status:** Paper-III detector-output covariance/resource bound. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 118 established that all eight centered-covariance rows are linearly indispensable in the current 22D source-nuisance calibration span. Earlier Iterations 039–041 studied only the best four covariance rows in detail.

This iteration builds the endpoint graph for **all eight** current centered-covariance rows and asks how they should be grouped in the same affine Gaussian cross-covariance output model used for the earlier graph bound.

The existing noncommutation/backaction gate remains active throughout: this is a detector-output information bound, not permission to measure arbitrary multitime source observables disturbance-free.

## 2. Exact eight-row endpoint graph

The eight centered-covariance rows correspond to edges

1. `G0(TR) -- G0(0)`;
2. `G0(T1) -- G1(0)`;
3. `G1(T5) -- G1(0)`;
4. `G1(TR) -- G0(0)`;
5. `G0(TR) -- G1(0)`;
6. `G1(T3) -- G0(0)`;
7. `G0(T6) -- G0(0)`;
8. `G0(T6) -- G1(0)`.

There are eight unique endpoint vertices:

`G0(0), G1(0), G0(TR), G0(T1), G1(T5), G1(TR), G1(T3), G0(T6)`.

The two zero-time endpoints are degree-four hubs. `G0(TR)` and `G0(T6)` each connect to both hubs; the remaining four endpoints have degree one.

## 3. Spectral congestion of one all-eight trajectory

Let the nominal whitened detector covariance be `Sigma0=I_8`. Encode each covariance coordinate as an off-diagonal edge perturbation with common amplitude `a`.

At the nominal point, distinct edge derivatives are Frobenius-orthogonal, so the covariance-coordinate Fisher is

`K=a^2 I_8`.

However full-hypercube positivity is controlled by the largest spectral radius over signed endpoint adjacency matrices. The unsigned graph already attains the worst aligned-sign case.

Its nonzero adjacency eigenvalues are

`+-sqrt(6)`, `+-sqrt(2)`.

Therefore

`rho(A)=sqrt(6)`

and full-hypercube positivity requires

`a < 1/sqrt(6)`.

Hence

`boxed{lambda_min(K)<1/6}`.

### RQIR-NG-077 — all-eight covariance congestion

> In the current eight-endpoint, cross-covariance-only affine Gaussian encoding, trying to measure all eight centered-covariance coordinates in one shared trajectory reduces the per-coordinate Fisher ceiling below `1/6` under the full normalized hypercube positivity requirement.

This is substantially more congested than the earlier best-four graph ceiling `<1/2`.

## 4. Accepted-trajectory lower bound

With normalized target `gamma_cov`, one all-eight joint trajectory class therefore needs

`N_all8 > 6 gamma_cov`.

Using the currently stored calibration normalizations:

- Toy009, `gamma_cov=5.901272925e5`:
  `N_all8 > 3.540763755e6` accepted trajectories;
- Toy014, `gamma_cov=2.7186736e6`:
  `N_all8 > 1.63120416e7` accepted trajectories.

These are normalized detector-output lower bounds, not physical hours.

## 5. Is one giant joint graph optimal?

No.

Suppose the eight edges are partitioned into independently scheduled Gaussian cross-covariance blocks. For block graph `G_k`, the same uniform-edge positivity argument gives a trajectory multiplier

`rho(G_k)^2`.

The total normalized accepted-trajectory burden is therefore proportional to

`sum_k rho(G_k)^2`.

An exhaustive enumeration of all `4140` set partitions of the eight edges gives

`boxed{min_partition sum_k rho(G_k)^2 = 4}`.

One exact optimum is four endpoint-disjoint two-edge matchings:

- rows `(4,5)` in one-based numbering;
- rows `(3,6)`;
- rows `(2,7)`;
- rows `(1,8)`.

In zero-based code indexing this is

`([3,4],[2,5],[1,6],[0,7])`.

Every block contains two edges with no shared endpoint, so each block has `rho^2=1`.

### RQIR-RESOURCE-089 — optimal covariance graph partition in the affine cross-covariance class

`boxed{N_cov,partition > 4 gamma_cov}`.

Thus, within this restricted detector-output model:

- eight separate edge campaigns: `8 gamma_cov`;
- one giant all-eight graph: `6 gamma_cov`;
- optimal four matching blocks: `4 gamma_cov`.

The optimal graph partition halves the separate-edge count and improves the all-eight joint graph by one third.

For the stored normalizations:

- Toy009 optimal partition: `>2.36050917e6` accepted trajectories;
- Toy014 optimal partition: `>1.08746944e7` accepted trajectories.

## 6. Why four is the exact optimum

The full graph has a degree-four hub. For any partition into subgraphs,

`rho(G_k)^2 >= Delta(G_k)`

because the largest eigenvalue of `A_k^2` is at least its largest diagonal entry, the maximum degree.

Summing over blocks, the degree contributions of the original degree-four hub sum to four, so

`sum_k rho(G_k)^2 >=4`.

A four-matching edge coloring attains this bound exactly. Since the graph is bipartite with maximum degree four, four matchings are sufficient.

Therefore the value `4` is not merely a numerical partition search result; it is an exact optimum for this graph/objective.

## 7. Backaction / measurement-compatibility guard

The matching partition is **not automatically a realizable strong-measurement source protocol**.

Iteration 041 established that force observables at distinct phase settings are generally noncommuting and not QND. Two covariance edges can be endpoint-disjoint yet still involve different source times and incompatible observables on one quantum trajectory.

Hence:

### RQIR-NG-078 — graph-disjoint does not imply source-measurement compatible

> Endpoint-disjoint covariance estimators may share a classical detector-output block only if one declared physical measurement likelihood, including backaction, generates them jointly. Graph matching removes Gaussian endpoint congestion; it does not remove quantum noncommutation.

The `4 gamma_cov` result is therefore an optimistic detector-output lower bound for a future weak/continuous/ancilla implementation, not the conservative independent-preparation schedule.

## 8. Consequence for the non-double-counted scheduler

Iteration 116 says one physical record receives one wall-clock charge. Iteration 119 now supplies a sharper covariance-side campaign library:

- do not automatically create one all-eight covariance campaign;
- the best affine Gaussian grouping is four matching blocks before backaction constraints;
- if a physical measurement model cannot jointly realize a matching block, split it further;
- if a richer multi-output likelihood beats the cross-covariance-only positivity bound, use its actual Fisher matrix instead.

These blocks can then enter RESOURCE-083 as separate physical campaign matrices.

## 9. Readiness snapshot after Iteration 119

Project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **92%**.
- **Paper III submission-ready state:** **73%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Paper III increases because the previously unresolved all-eight covariance sharing problem now has an exact detector-output optimum and an explicit backaction boundary. Candidate-Gravity readiness is unchanged because no QG dynamics/consistency gate was closed.

## 10. Next admissible gate

Combine the exact rank result of Iteration 118 with the covariance grouping of Iteration 119 and the noncommutation result of Iteration 041:

1. construct a conservative strong-measurement acquisition cover with independent source preparations across incompatible time layers;
2. construct an optimistic weak/shared-output lower-bound cover using the four covariance matchings;
3. bracket the physically allowed calibration wall time between these two branches;
4. propagate this interval through RESOURCE-083 and into the detector-side Toy014/Toy009 ratio `u`.

Geometry/additive SI reference rates and transfer drift remain symbolic unless physically supplied.

## 11. Reproducibility

Run

`python analysis/full_covariance_endpoint_partition_iteration119.py`.

The script reconstructs the eight-edge graph, verifies `rho^2=6`, exhaustively checks all 4140 edge partitions, confirms the exact four-matching optimum and evaluates Toy009/Toy014 normalized accepted-trajectory lower bounds.
