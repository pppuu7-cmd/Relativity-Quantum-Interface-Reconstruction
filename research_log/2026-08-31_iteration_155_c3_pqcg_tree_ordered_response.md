# RQIR Research Log — Iteration 155

**Date:** 2026-08-31  
**Comparator:** `C3-PQCG-NL-001`  
**Topic:** ordered nonlinear response from the same PQCG dynamics

## Starting point

Iteration 154 showed that the published nonlinear Onsager–Machlup PQCG action generates a nonzero fully symmetric gravitational third cumulant and lifts the scoped `(D2,D0)` tangent from rank 1 to rank 2. The remaining important C3 question was whether the same realization predicts an ordered/causal nonlinear response without introducing an independent phenomenological kernel.

## Same-dynamics tree response

The covariant CQ gravity construction diffuses around the nonlinear Einstein equation. At tree level, the second functional response to a source is therefore fixed by the nonlinear Einstein drift:

`chi2R_A;BC = - G_R_AA' Gamma3_EH^A'_{B'C'} G_R^B'_B G_R^C'_C`.

This is structurally the same EH retarded response already computed in the frozen six-probe C5 boundary protocol.

The six finite response values are

`[0.30003001285313774,-1.461790494216445,-12.034873790942026,-14.434681522564402,4.867521776975717,-2.7789127642722273]`.

Thus the classical stochastic spacetime comparator has a nonzero causal nonlinear response.

## Tangent result

The C3 stochastic parameters remain `(D2,D0)`.

At tree level the Einstein drift is controlled by the hard-calibrated Newton/GR coupling, not by `D2,D0`. Therefore

`d chi2R_tree / d D2 = d chi2R_tree / d D0 = 0`.

The six-by-two diffusion tangent contributed by this tree response is the zero matrix and adds rank `0`.

This is **not** the statement `chi2R=0`. The physical tree response is nonzero; only its derivative with respect to the chosen stochastic diffusion parameters is zero after fixing the common GR boundary.

## Retained results

### `C3-NG-003 — TREE_ORDERED_RESPONSE_IS_COMMON_GR_BOUNDARY`

The PQCG tree causal response is nonzero but belongs to the common calibrated Einstein boundary and does not add a `D2/D0` comparator direction.

### `NG-FUNNEL-013 — NONZERO_CAUSAL_NONLINEAR_RESPONSE_NOT_QUANTUM_CERTIFICATE`

A nonzero causal nonlinear gravitational response is not sufficient evidence for a quantum metric. A concrete classical stochastic spacetime with nonlinear Einstein drift already generates one.

## Ordered sector still blocked

A diffusion-dependent ordered response would arise only after a same-convention stochastic/MSR-loop or other explicitly derived correction. That calculation is not available in the current frozen finite PQCG implementation.

The Iteration-145 scalar decomposition into `chi2R_even/odd` also requires a fully fixed order-sensitive selector before an odd component can be assigned.

Therefore:

- tree causal response: `PASS_SCOPED_COMMON_GR_BOUNDARY`;
- added tree diffusion rank: `0`;
- diffusion-dependent ordered correction: `BLOCKED_STOCHASTIC_LOOP_RESPONSE`;
- exact `chi2R_odd` selector: `BLOCKED_SELECTOR_COMPLETION`;
- full C3 ordered tangent: `BLOCKED`.

Blocked entries are not zeros.

## Decision

Do not invent a diffusion-dependent C3 ordered column. Per the frozen Iteration-154 restart rule, move the active comparator construction to the first fixed nonlinear C4 realization while retaining the C3 stochastic-loop sector as an explicit blocker.

No Fisher/resources and no `ANSATZ-003` promotion.

## Reproducibility

- `analysis/c3_pqcg_tree_ordered_response_iteration155.py`
- `results/c3_pqcg_tree_ordered_response_iteration155.json`
- `candidate_gravity/C3_PQCG_TREE_ORDERED_RESPONSE_ITERATION155.md`
