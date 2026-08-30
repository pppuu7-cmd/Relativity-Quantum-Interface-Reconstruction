# RQIR Recovery Delta — Iteration 120

**Date:** 2026-08-31  
**Parent front:** Iteration 119.

## Calibration-cover bracket

Let `xi_mean^2` be the weakest-direction Fisher per accepted same-time dual-probe mean layer.

`M=7 gamma_mean/xi_mean^2`.

Iteration 119 gives covariance burdens

`C4=4 gamma_cov` for the optimal four-matching detector-output cover,

`C8=8 gamma_cov` for separate covariance rows.

### RESOURCE-090

Normalized accepted-cycle branches:

`N_lower=max(M,C4)`

`N_match=M+C4`

`N_strong=M+C8`.

The first is an optimistic perfect-sharing lower bound; the last is the conservative no-sharing branch. Real apparatus scheduling must use RESOURCE-083 with physical rate matrices.

Mean/covariance crossover:

`xi_cross=sqrt[7 gamma_mean/(4 gamma_cov)]`.

- Toy009: `xi_cross~=2.32971677`.
- Toy014: `xi_cross~=1.91172817`.

At `xi_mean=3`, covariance dominates both normalized burdens. Toy014/Toy009 branch ratios are approximately

- lower shared: `4.60693`;
- matching covariance separate from mean: `4.04082`;
- conservative: `4.25830`.

### DESIGN-019

Characterize covariance-complement throughput and backaction before reopening Toy015; Toy014's covariance normalization is relatively more expensive than its mean normalization.

## Readiness after Iteration 120

- Paper III scientific-content readiness: **93%**.
- Paper III submission readiness: **74%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/calibration_cover_bracket_iteration120.py`
- `docs/PAPER_III_CALIBRATION_COVER_BRACKET_ITERATION120.md`
- `research_log/2026-08-31_iteration_120_calibration_cover_bracket.md`

## Next gate

Convert the normalized cover to a symbolic physical rate-matrix bracket with unequal layer durations/acceptance, four covariance matching-block matrices and the common-gain transfer block. Solve RESOURCE-083 for conservative and optimistic campaign libraries and propagate the result toward `u=R_D14/R_D09`.
