# Iteration 155 — PQCG tree ordered nonlinear response

**Date:** 2026-08-31  
**Comparator:** `C3-PQCG-NL-001`  
**Status:** `PASS_SCOPED_COMMON_GR_BOUNDARY / DIFFUSION_ORDERED_BLOCKED`

## Question

Does the same fixed postquantum-classical gravity realization that produced the Iteration-154 symmetric bispectrum also predict a nonzero causal second-order response, and does that response add a new `(D2,D0)` comparator direction?

## Same parent dynamics

The covariant PQCG construction diffuses around the nonlinear Einstein equation. At tree level, differentiating the nonlinear drift with respect to two external sources gives the classical retarded response

`chi2R_A;BC = - G_R_AA' Gamma3_EH^A'_{B'C'} G_R^B'_B G_R^C'_C`.

This is the same structural Einstein-Hilbert response already evaluated on the frozen six-probe protocol in the C5 boundary calculation. No new phenomenological response kernel is added.

## Six-probe result

The finite tree response fingerprint is

`[0.30003001285313774, -1.461790494216445, -12.034873790942026, -14.434681522564402, 4.867521776975717, -2.7789127642722273]`.

Therefore a classical stochastic spacetime realization has a **nonzero causal nonlinear response**.

## Parameter tangent

The stochastic comparator parameters remain

`theta_C3=(D2,D0)`.

The tree Einstein drift is fixed by the already calibrated Newton/GR normalization `G_N`; it does not vary with the diffusion constants at this order. Hence

`partial chi2R_tree / partial D2 = 0`,

`partial chi2R_tree / partial D0 = 0`.

The six-probe tree response therefore adds rank **0** to the `(D2,D0)` tangent.

This zero derivative must not be confused with zero physical response: the response is nonzero but common to the GR boundary.

## New retained results

### `C3-NG-003 — TREE_ORDERED_RESPONSE_IS_COMMON_GR_BOUNDARY`

The fixed PQCG realization has a nonzero tree causal nonlinear response, but after the Newton/GR coupling is hard-calibrated it supplies no new diffusion-parameter direction. It is a common GR-boundary contribution rather than a distinguishing `D2/D0` signal.

### `NG-FUNNEL-013 — NONZERO_CAUSAL_NONLINEAR_RESPONSE_NOT_QUANTUM_CERTIFICATE`

A nonzero causal nonlinear gravitational response is not, by itself, evidence for a quantum metric. A classical spacetime with nonlinear Einstein drift already produces one.

A useful RQIR discriminator must instead depend on an ordered structure or parameter-linked correction that survives subtraction of the common GR boundary and all fixed comparators.

## What remains blocked

The tree result does **not** derive the full Iteration-145 `chi2R_even/odd` comparator rows.

- diffusion-dependent stochastic/MSR-loop ordered corrections: `BLOCKED_STOCHASTIC_LOOP_RESPONSE`;
- the exact order-sensitive scalar selector defining `chi2R_odd`: `BLOCKED_SELECTOR_COMPLETION`;
- full ordered C3 tangent: `BLOCKED`.

These entries must not be set to zero merely because the tree diffusion tangent vanishes.

## Literature / formalism guardrail

The Martin–Siggia–Rose/Janssen–De Dominicis representation of the stochastic dynamics supports causal response functions. In the same CQ literature, discretization/Jacobian contributions cancel against closed response loops when treated consistently. Thus the tree causal response can be stated without inventing a new stochastic prescription, while diffusion-dependent loop corrections still require an explicit same-convention calculation.

## Decision

Iteration 155 closes the tree-level C3 ordered-response question but does **not** complete the C3 comparator.

Per the frozen funnel rule, do not invent missing diffusion-dependent ordered columns. The next productive comparator target is a fixed nonlinear C4 realization, while the C3 stochastic-loop ordered sector remains explicitly BLOCKED.

## Reproducibility

- `analysis/c3_pqcg_tree_ordered_response_iteration155.py`
- `results/c3_pqcg_tree_ordered_response_iteration155.json`
- Iteration-150 EH response authority: `results/c5_cubic_response_iteration150.json`
