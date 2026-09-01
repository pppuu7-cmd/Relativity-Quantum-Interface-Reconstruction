# Recovery Delta — RQIR Iteration 219

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New nonlinear source block

Instantiate the full `2 massive scalar + 2 graviton` tree amplitude using the published two-scalar scalar-gluon amplitude and four-point KLT relation from arXiv:1908.09755.

Frozen scalar Compton geometry: `m=0.7`, `sqrt(s)=2`, five fixed scattering angles, four deterministic factorized polarization combinations.

Certificate:

- momentum conservation error `0`;
- max mass-shell error `3.33e-16`;
- max independent KLT-copy gravitational Ward residual `2.25e-15`;
- max graviton-leg exchange asymmetry `4.44e-16`.

This validates the coherent nonlinear source amplitude and confirms that gauge safety cannot be assigned to an isolated `hh phi phi` seagull.

## Important state-projection caveat discovered after the initial certificate

The first implementation used real factorized vector polarizations `e x e`. They are sufficient for the KLT/Ward algebra test, but a real factorized tensor is not by itself a pure helicity-`+/-2` Einstein graviton state; a pure graviton helicity requires matched complex helicity vectors in the two copies (or an explicitly traceless linear combination).

Therefore Iteration 219 is authoritative as a **factorized gauge-algebra/source-completion test**, while the pure-Einstein external-state interpretation must be revalidated prospectively in Iteration 220. Do not delete or rewrite the original result.

## Retained results

- `SRC-NG-003 — FULL_TWO_SCALAR_TWO_GRAVITON_KLT_AMPLITUDE_PASSES_INDEPENDENT_GRAVITATIONAL_WARD_TESTS` (factorized-state algebra scope);
- `SRC-NG-004 — NONLINEAR_SOURCE_GAUGE_SAFETY_BELONGS_TO_THE_COMPLETE_AMPLITUDE_NOT_AN_ISOLATED_SEAGULL_VERTEX`;
- `C5-CUT-018 — GAUGE_INVARIANT_DYNAMICAL_SCALAR_SOURCE_TREE_BLOCK_IS_AVAILABLE_FOR_SOURCE_LEVEL_UNITARITY_CUTS`, pending pure-helicity state validation before a pure-Einstein cut;
- `NG-FUNNEL-076`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Exact restart instruction

Iteration 220: replace the real factorized external states by complex null helicity vectors `e_+/-` satisfying `e.e=0`, `e.k=0`, and use matched left/right helicities for pure graviton `+/-2` states. Repeat independent-copy Ward tests and graviton exchange symmetry before any pure-Einstein source cut is built.
