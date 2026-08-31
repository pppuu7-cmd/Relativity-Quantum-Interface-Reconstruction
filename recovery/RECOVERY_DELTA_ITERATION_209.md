# Recovery Delta — RQIR Iteration 209

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 208 established a gauge-invariant on-shell C5 nonanalytic positive control but preserved the distinction between that physical S-matrix anchor and the blocked off-shell/source-completed RQIR `T_cut`.

## New authoritative result

Four-dimensional loop soft behavior is not generically a pure Taylor series.

- `arXiv:1405.1015`: leading soft-graviton behavior is not loop-corrected, while subleading behavior is anomalous/loop-modified and higher orders receive loop corrections.
- `arXiv:1706.00759`: generic sub-subleading soft behavior contains a universal term plus a non-universal contribution depending on two- and three-point functions; the loop statement avoids 4D because of IR divergence.
- `arXiv:1804.09193`: in four dimensions the usual soft factor becomes ambiguous beyond leading order and logarithms of the soft energy appear at subleading order.

Therefore the existing local/tree `soft2` coordinate remains valid only in its analytic tree scope. The loop/nonanalytic comparator must use a polyhomogeneous basis

`epsilon^n [a_n + b_n log(epsilon/mu_soft)]`

at one loop, with a declared remainder and a common IR convention.

Freeze the operation order: take the hard-channel discontinuity at finite nonzero soft momentum first, then perform the regular+log soft extraction. Do not assume a naive Taylor soft limit commutes with the cut.

## Retained results

- `SOFT-NG-006 — FOUR_DIMENSIONAL_LOOP_SOFT_EXPANSION_IS_POLYHOMOGENEOUS_NOT_PURE_TAYLOR`;
- `C5-CUT-007 — LOOP_C5_T_cut_REQUIRES_EXPLICIT_LOG_SOFT_COORDINATES_AND_IR_CONVENTION`;
- `REL-NG-018 — GENERIC_SUBSUBLEADING_SOFT_STRUCTURE_CONTAINS_NONUNIVERSAL_TWO_AND_THREE_POINT_INFORMATION`;
- `NG-FUNNEL-065 — DO_NOT_IDENTIFY_TREE_SOFT2_WITH_THE_LOOP_NONANALYTIC_SOFT_COEFFICIENT_WITHOUT_LOG_BASIS_EXTENSION`;
- `NG-FUNNEL-066 — TAKE_HARD_CHANNEL_DISCONTINUITY_AT_FINITE_SOFT_MOMENTUM_BEFORE_POLYHOMOGENEOUS_SOFT_EXTRACTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged. No residual and no re-closed comparator block.

## Exact restart instruction

Resume at **Iteration 210 — executable polyhomogeneous soft extractor**.

Use a target-independent finite-epsilon grid with at least six points for the one-loop basis through `n=2`: `[1, L, z, zL, z^2, z^2L]` after dimensionless rescaling. Quantify rank/condition number. Demonstrate exact recovery on a synthetic regular+log control, deterministic noise amplification, and a nonzero failure residual for a pure-Taylor fit to the same logarithmic data. Store code/results. This is protocol conditioning only, not Fisher/resources.

Do not create `ANSATZ-003`.
