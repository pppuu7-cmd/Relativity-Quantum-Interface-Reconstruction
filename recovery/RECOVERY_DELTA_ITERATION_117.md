# RQIR Recovery Delta — Iteration 117

**Date:** 2026-08-31  
**Parent front:** Iteration 116.

## New structural gate

A one-setting same-state dual-tone reference has a four-real observation vector, so for local Jacobian `J_b`,

`K_b=J_b^T W_b J_b`

has

`rank(K_b)<=4`.

Repeating the unchanged setting only multiplies `K_b`; it does not enlarge its Fisher support.

### NG-074

Missing reference directions cannot be repaired by more SNR/exposure if the local Jacobian span is unchanged.

### RESOURCE-085

For required information `H_*>=0` and accumulated reference Fisher `K_tot`, finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`,

or equivalently

`null(K_tot) subseteq null(H_*)`.

### RESOURCE-086

With `m` distinct four-real reference settings and `r_req=rank(H_*)`,

`m>=ceil(r_req/4)`

is a necessary dimensional lower bound. It is not sufficient; settings can be redundant.

### DESIGN-018

Choose new reference settings to increase the missing score span / `sigma_min` of the stacked whitened Jacobian on the required nuisance subspace before increasing SNR in already-covered directions.

Dimensional examples only:

- common gain + seven independent scalar layer directions: `r_req=8`, at least 2 distinct settings;
- common gain + seven independent 2D layer directions: `r_req=15`, at least 4 distinct settings.

Actual RQIR rank must be reconstructed after hard constraints and overlaps.

## Readiness after Iteration 117

- Paper III scientific-content readiness: **90%**.
- Paper III submission readiness: **71%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/reference_span_rank_iteration117.py`
- `docs/PAPER_III_REFERENCE_SPAN_RANK_ITERATION117.md`
- `research_log/2026-08-31_iteration_117_reference_span_rank.md`

## Next gate

Reconstruct the actual required nuisance subspace and the score span of the existing seven-layer calibration settings plus same-state dual-tone transfer setting for Toy009/Toy014. Find the minimal nonredundant setting cover, then solve the Iteration-116 matrix quota problem without double counting.
