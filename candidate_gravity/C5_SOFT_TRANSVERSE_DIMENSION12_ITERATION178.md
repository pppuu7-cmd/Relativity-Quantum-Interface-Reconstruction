# RQIR Candidate Gravity — Iteration 178

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

What is the target-independent local-C5 occupancy of the six frozen Ward-subtracted null-soft TT coordinates after completing the already-authorized cubic EFT subset through dimension 12?

## Frozen protocol

No kinematic row is changed from Iteration 177:

`k1=eps*(1,0,0,1)`, `k2=q_i`, `k3=-q_i-k1`,

with the same six hard `q_i`, the same physical null plus-TT soft polarization, the same hard TT polarization seeds, and the same `eps` sequence.

All operators below begin at `O(h^3)` about Minkowski, so their operator-specific quadratic kernel is zero and their Ward subtraction is exactly `W[K2]=0`.

The frozen local cubic subset is

- `Tr(Ricci^3)`;
- cyclic `Riemann^3`;
- mixed `Ricci Ricci Riemann`;
- `RicciChain Box^n Ricci`, `n=1,2,3`;
- `RiemannChain Box^n Riemann`, `n=1,2,3`.

This is the same target-independent cubic subset authorized in Iteration 165 through the dimension-12 cutoff, now recalculated in the Iteration-175/177 soft-transverse protocol.

## Soft-TT reduction

For the physical null TT soft leg,

`R_mn^(1)(k_soft)=0`,

while `R_mnrs^(1)(k_soft)` is nonzero and scales as `eps^2`.

Therefore every cubic invariant in which the soft leg must appear as a Ricci tensor vanishes. In particular,

`B_T[Tr(Ricci^3)] = 0`,

and

`B_T[RicciChain Box^n] = 0`, `n=1,2,3`.

For the surviving Riemann structures the soft limit collapses further. On the frozen hard TT pair, the mixed invariant obeys

`B_T[Ricci Ricci Riemann] = B_T[Riemann^3]/12`.

For the derivative descendants, the `Box^n` factor vanishes whenever it acts on the null soft leg because `k_soft^2=0`; the four hard-leg permutations survive. The result is

`B_T[RiemannChain Box^n] = (2/3)(-q_i^2)^n B_T[Riemann^3]`, `n=1,2,3`.

The numerical checks agree with these identities at relative levels `1.3e-8` to `6.6e-8`.

## Rank certificate

A blind floating-point SVD of the extrapolated nine-column matrix gives singular values approximately

`[2.0254128085, 0.0753112512, 0.0037578441, 4.7032466e-5, 1.2254429e-8, 1.98e-18]`.

A naive tolerance `1e-10` would incorrectly call this rank 5.

However the largest independent soft-extrapolation discrepancy is

`5.2625580e-6`,

which is more than two orders of magnitude above the fifth singular value. More importantly, the exact soft identities remove that direction analytically.

After enforcing the exact kinematic relations, the physical basis is

`Riemann3 * {1, (-q^2), (q^2)^2, (-q^2)^3}`

(up to the fixed `2/3` descendant normalization), with

`rank = 4`,

singular values

`[2.0192478812, 0.0752839640, 0.0037576657, 4.7032262e-5]`,

and `s_min/s_max = 2.3292e-5`.

Pure-gauge replacement of the soft leg leaves maximum absolute cubic residue `9.51e-23`.

## Scientific classification

### `C5-NG-009 — DIMENSION12_LOCAL_C5_NULL_SOFT_TT_BASIS_COMPRESSES_TO_RIEMANN_CHAIN_POLYNOMIAL_RANK_FOUR`

The frozen local dimension-12 cubic subset occupies four independent directions in the six-row null-soft TT `B_T` space.

### `SOFT-NG-005 — NULL_SOFT_TT_KINEMATICS_KILLS_RICCI_CHAIN_AND_REDUCES_DERIVATIVE_RIEMANN_DESCENDANTS_TO_HARD_Q2_MOMENTS`

The new soft-transverse protocol is highly selective: Ricci-based directions vanish, while derivative Riemann descendants reduce to controlled hard-momentum moments of the same underlying Riemann-cubic carrier.

### `NUM-NG-001 — SUB_ERROR_SINGULAR_VALUE_MUST_NOT_BE_PROMOTED_WHEN_EXACT_KINEMATIC_IDENTITIES_REMOVE_IT`

Numerical rank must be compared with the extrapolation/model error and exact identities before scientific interpretation.

## What this does not establish

This does not produce Candidate Gravity novelty. The remaining two-dimensional complement of the six-row space is not a residual certificate while fixed C4, nonlocal, asymptotic-safety and C3 ordered/transverse comparator columns are incomplete.

`ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%`, unchanged.

The local C5 transverse comparator is substantially sharper, but the frozen readiness rubric does not award a point until the remaining comparator-family foundation needed for the actual full quotient is closed.

## Next gate

Iteration 179 should project the first fixed C4 parent realization into the same six `B_T` rows. Before calculation, verify that the chosen C4 realization actually has a massless/null soft spin-2 leg compatible with the frozen protocol; if dRGT's massive graviton makes the null-soft map physically inapplicable, record `BLOCKED_C4_DRGТ_NULL_SOFT_INCOMPATIBLE` and instantiate a fixed massless ordinary-quantum-mediator C4 control instead of forcing dRGT into an invalid kinematic regime.
