# RQIR Research Log — Iteration 119

**Date:** 2026-08-31

## Question

What is the endpoint-congestion cost of measuring all eight indispensable centered-covariance calibration rows, and is one giant shared covariance trajectory optimal?

## Result

The full eight-row endpoint graph has eight vertices and eight edges. Its nonzero adjacency eigenvalues are `+-sqrt(6)` and `+-sqrt(2)`, so `rho(A)^2=6`.

In the affine whitened cross-covariance-only Gaussian model, full-hypercube positivity therefore gives per-edge Fisher `<1/6`, implying

`N_all8 > 6 gamma_cov`.

Exhaustive enumeration of all 4140 edge partitions gives an exact optimum

`min sum_k rho(G_k)^2 = 4`,

attained by four endpoint-disjoint two-edge matchings. Thus

`N_cov,partition > 4 gamma_cov`.

For stored normalizations:

- Toy009: all-eight joint `>3.540763755e6`, optimal four-matchings `>2.36050917e6`, separate edges `>4.72101834e6` accepted trajectories;
- Toy014: all-eight joint `>1.63120416e7`, optimal four-matchings `>1.08746944e7`, separate edges `>2.17493888e7`.

The value 4 is exact: `rho(G_k)^2>=Delta(G_k)`, while a degree-four hub forces the partition sum to be at least four; a four-matching edge coloring attains it.

## Labels

- **NG-077:** all-eight covariance congestion, `lambda_min<1/6` in the declared cross-covariance encoding.
- **RESOURCE-089:** exact four-matching detector-output partition optimum, `N>4 gamma_cov`.
- **NG-078:** endpoint-disjoint does not imply source-measurement compatible; noncommutation/backaction remains active.

## Reproducibility

`analysis/full_covariance_endpoint_partition_iteration119.py` verifies the graph spectrum, exhaustive partition optimum and normalized trajectory counts.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **92%**.
- Paper III submission readiness: **73%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Construct two calibration-cover branches: conservative strong-measurement independent-preparation scheduling and optimistic weak/shared-output scheduling using the four matching blocks. Use them to bracket calibration time and propagate the bracket into the non-double-counted Toy014/Toy009 detector ratio.
