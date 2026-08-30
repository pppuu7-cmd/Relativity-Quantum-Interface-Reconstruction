# RQIR Research Log — Iteration 117

**Date:** 2026-08-31

## Question

Can one four-real same-state dual-tone reference setting span common transfer gain plus the nuisance directions required by the seven calibration layers, or can repetition/SNR compensate for missing directions?

## Result

For one setting with four-real observation Jacobian `J_b`,

`K_b=J_b^T W_b J_b`,

so `rank(K_b)<=4`.

Repeating the same setting gives `N K_b` and does not change rank. Therefore a required direction outside the score span remains unidentifiable at every finite exposure (NG-074).

For requirement matrix `H_*`, finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`,

or equivalently

`null(K_tot) subseteq null(H_*)` (RESOURCE-085).

With `m` distinct four-real settings,

`rank(K_tot)<=4m`,

so if `r_req=rank(H_*)`, necessarily

`m>=ceil(r_req/4)` (RESOURCE-086).

This dimensional bound is not sufficient: settings must have complementary score orientation. The practical design test is positive smallest singular value of the stacked whitened Jacobian restricted to the required subspace (DESIGN-018).

## Reproducibility

`analysis/reference_span_rank_iteration117.py` verifies the four-real rank ceiling, identical-repetition no-go, support condition, setting-count lower bound and complementary-vs-redundant setting regressions.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **90%**.
- Paper III submission readiness: **71%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

Candidate-Gravity readiness does not increase in this iteration because no QG consistency gate or concrete dynamics was closed; only downstream experimental certification became sharper.

## Next gate

Reconstruct the actual required nuisance subspace for Toy009/Toy014 from the existing hard constraints, spectral-tilt quotient, seven calibration settings and same-state transfer setting. Determine the minimal nonredundant reference-setting cover before solving the Iteration-116 quota SDP.
