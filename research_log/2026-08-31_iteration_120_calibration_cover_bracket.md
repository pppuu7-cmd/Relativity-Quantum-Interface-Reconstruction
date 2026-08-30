# RQIR Research Log — Iteration 120

**Date:** 2026-08-31

## Question

How should the current mean-plus-covariance calibration cost be bracketed between a conservative strong-measurement schedule and an optimistic shared-output schedule without inventing apparatus rates?

## Result

Using the stored row-normalized calibration weights and a weakest-direction mean Fisher `xi_mean^2` per accepted same-time dual-probe layer:

`M=7 gamma_mean/xi_mean^2`.

From Iteration 119:

`C4=4 gamma_cov` for the optimal four-matching covariance detector-output cover,

`C8=8 gamma_cov` for separate covariance rows.

The normalized accepted-cycle branches are

- optimistic shared lower bound: `N_lower=max(M,C4)`;
- matching covariance separate from mean: `N_match=M+C4`;
- conservative no-sharing branch: `N_strong=M+C8`.

The mean/covariance crossover is

`xi_cross=sqrt[7 gamma_mean/(4 gamma_cov)]`,

which is `~2.32972` for Toy009 and `~1.91173` for Toy014.

At the historical regression `xi_mean=3`, covariance dominates both architectures. Toy014/Toy009 normalized calibration-burden ratios are

- lower shared: `~4.60693`;
- matching separate from mean: `~4.04082`;
- conservative: `~4.25830`.

This identifies physical covariance-complement throughput/backaction as a higher-value characterization target than reopening source search.

## Labels

- **RESOURCE-090:** explicit calibration-cover lower/intermediate/conservative bracket.
- **DESIGN-019:** characterize covariance throughput before Toy015.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **93%**.
- Paper III submission readiness: **74%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Promote the cycle-count bracket to a full symbolic rate-matrix bracket with seven `R_mean,j`, four covariance matching-block matrices, common-gain transfer `K_x`, unequal duration/acceptance and RESOURCE-083 scheduling. Derive a symbolic detector-ratio interval before adding apparatus ASD.
