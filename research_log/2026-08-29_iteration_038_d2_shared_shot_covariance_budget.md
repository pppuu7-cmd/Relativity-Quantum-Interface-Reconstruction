# RQIR Research Log — Iteration 038

**Date:** 2026-08-29  
**Target:** quantify the maximum useful shared-shot covariance Fisher for the four high-value centered D2 rows `(0,1,3,7)` and combine it with the Toy009 coherence floor and corrected source-preparation QFI.

## Starting point

Iteration 037 bounded one full-range affine Gaussian covariance amplitude by `I_shot<m/2`, and showed that an `m=8` joint output could in principle reduce the separate-row cycle-rate burden. The missing step was a **multi-parameter** bound for four covariance coordinates measured simultaneously.

## New theorem / negative gate

For

`Sigma(u)=Sigma0+sum_i u_i Sigma_i`, `u_i in [-1,1]`,

let `H_i=Sigma0^-1/2 Sigma_i Sigma0^-1/2` and require positivity at all hypercube vertices. Then for every sign vector `s`, `||sum_i s_i H_i||_op<1`.

Averaging the squared signed sums gives

`sum_i Tr(H_i^2)<m`.

Therefore the covariance Fisher matrix

`K_ij=1/2 Tr(H_i H_j)`

obeys

`Tr K<m/2`, `lambda_min(K)<m/(2q)`.

This is **RQIR-NG-017 — multi-parameter covariance information budget**.

For `q=4,m=8`, the weakest one of the four simultaneously measured covariance directions has per-shot Fisher `<1`.

## Near-saturating construction

Four disjoint traceless two-dimensional detector blocks with amplitude `a=0.999` give

`K=0.998001 I_4`,

while the full calibration hypercube remains positive. Thus the `lambda_min->1` limit can be approached.

At the centered Iteration-034 D2 benchmark `gamma_cov~0.590127e6`, an ideal joint output therefore needs more than `5.90127e5` accepted cycles at `lambda=1`; the explicit `a=0.999` example needs `~5.91309e5`.

This yields **RQIR-RESOURCE-014 — shared-shot speedup is dimension-limited**: for the present four-row/minimal-eight-output architecture the best possible cycle-count advantage over four separate bivariate campaigns approaches a factor of four, not an arbitrary gain.

## Covariance nuisance orientation

In the covariance Fisher metric, the traceless block signals are exactly orthogonal to a common variance/imprecision-scale nuisance at `Sigma0=I`, so profiling that common scale leaves the four-row Fisher unchanged.

An unknown covariance nuisance aligned with one source derivative removes that direction exactly after profiling, making the profiled covariance Fisher singular.

This is **RQIR-CAL-014 — covariance Fisher-orthogonality design rule**: shared output directions must be engineered to be Fisher-orthogonal to dominant imprecision/backaction/cross-noise nuisance derivatives.

## Physical resource closure with source QFI

At `y_ref=-4`, the best four centered force-covariance rows reduce the required source prior from `4.55511` to `0.0500614`, saving

`Delta C_alpha~4.5050486`.

Using coordinate-correct `F_Q^(alpha)=0.0849323916`, this is only `~53.04` accepted single-branch source-metrology copy equivalents.

The ideal shared covariance detector needs `>5.90e5` accepted cycles, so at equal acceptance/efficiency:

`t_P/t_C > ~1.11255e4`

is necessary for covariance to beat source metrology in wall clock.

## Coherence coupling

The joint high-value set reaches phase `tau_max=4.99085067`. Hence

`T_C>=tau_max/(2 pi f_gap)`.

At `100 Hz`, `T_C>=7.94319 ms` before overhead. Combining with the ideal shared-shot bound gives a necessary source-metrology cycle

`t_P>~88.37 s`

at equal efficiencies; with a transparent `1 ms` detector dead/readout time this becomes `~99.50 s`.

Thus if physical source verification is substantially faster than roughly a minute-scale cycle at 100 Hz, the covariance-only complementary route cannot win purely by replacing the hidden-amplitude prior, even under an ideal near-saturating shared Gaussian detector.

## Files

- `analysis/d2_shared_shot_covariance_budget_iteration038.py`
- `docs/D2_SHARED_SHOT_COVARIANCE_BUDGET.md`
- `recovery/RECOVERY_DELTA_ITERATION_038.md`

## Next gate

Build a joint **mean + covariance** D2 output likelihood so that each accepted cycle can contribute direct force-mean information, the four high-value covariance directions, and timing/additive control information simultaneously. Profile explicit imprecision/backaction nuisance derivatives and compare total `F_beta|theta/T_wall` against independent source metrology.
