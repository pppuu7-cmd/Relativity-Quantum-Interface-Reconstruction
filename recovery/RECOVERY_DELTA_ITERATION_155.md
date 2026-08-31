# Recovery Delta — RQIR Iteration 155

**Date:** 2026-08-31  
**Authoritative change:** the fixed PQCG comparator is now shown to possess a nonzero tree causal nonlinear response, but this response is a common hard-calibrated GR-boundary contribution and adds zero tangent rank with respect to `(D2,D0)`; diffusion-dependent/order-sensitive C3 response remains BLOCKED.

## Previous front

Iteration 154 derived `C3sym_TT=B D2^2` from the same nonlinear PQCG Onsager–Machlup action and lifted the supported `(N2,C3sym_TT)` tangent to rank `2/2`.

## New tree ordered-response result

The nonlinear Einstein drift gives

`chi2R_A;BC = - G_R_AA' Gamma3_EH^A'_{B'C'} G_R^B'_B G_R^C'_C`.

On the frozen six-probe protocol the finite response is

`[0.30003001285313774,-1.461790494216445,-12.034873790942026,-14.434681522564402,4.867521776975717,-2.7789127642722273]`.

Hence a classical stochastic spacetime has a nonzero causal nonlinear response.

However, after the Newton/GR normalization is treated as a hard calibrated boundary, this tree Einstein response is independent of the PQCG diffusion parameters `(D2,D0)`:

`partial chi2R_tree / partial D2 = 0`,

`partial chi2R_tree / partial D0 = 0`.

Thus the tree ordered-response block adds rank `0` to the diffusion tangent.

## New retained results

### `C3-NG-003 — TREE_ORDERED_RESPONSE_IS_COMMON_GR_BOUNDARY`

The tree PQCG causal response is nonzero, but it does not distinguish diffusion parameters once the common GR coupling is fixed.

### `NG-FUNNEL-013 — NONZERO_CAUSAL_NONLINEAR_RESPONSE_NOT_QUANTUM_CERTIFICATE`

Nonzero causal nonlinear response alone is not a quantum-spacetime witness; a classical spacetime with nonlinear Einstein drift produces it.

## Critical scope distinction

Do **not** interpret the zero diffusion derivative as `chi2R=0`.

Still BLOCKED:

- diffusion-dependent stochastic/MSR-loop ordered corrections;
- the protocol-specific order-sensitive scalar selector needed to assign `chi2R_odd`;
- full C3 ordered tangent.

These rows remain unknown, not zero.

## New files

- `analysis/c3_pqcg_tree_ordered_response_iteration155.py`
- `results/c3_pqcg_tree_ordered_response_iteration155.json`
- `candidate_gravity/C3_PQCG_TREE_ORDERED_RESPONSE_ITERATION155.md`
- `research_log/2026-08-31_iteration_155_c3_pqcg_tree_ordered_response.md`
- `recovery/RECOVERY_DELTA_ITERATION_155.md`

## Exact restart instruction — Iteration 156

Move the active comparator program to the first fixed nonlinear C4 realization because the same-convention diffusion-dependent PQCG ordered correction is not currently derived.

1. freeze one concrete interacting massive-spin-2 / dRGT-style action and finite parameter vector rather than the C4 class label;
2. retain the same physical source/metric convention and six-probe response layer where applicable;
3. derive its tree `Gamma3`, retarded `chi2R`, and supported tensor/threshold directions from the same action;
4. check ghost/constraint assumptions only within the declared model regime;
5. compare its finite nonlinear tangent against the existing C5 `6x2` response span and the supported C3 rows;
6. keep any unavailable nonlinear C4 rows BLOCKED rather than zero;
7. no Fisher/resources and no `ANSATZ-003` until a nonzero residual survives fixed comparator quotienting.
