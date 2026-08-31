# RQIR Candidate Gravity — Iteration 209

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Audit whether the loop/nonanalytic soft sector can use the same pure-Taylor `soft2` extraction that is valid for the previously implemented local tree comparators.

## Literature result

Bern, Davies and Nohle (`arXiv:1405.1015`) show that the leading soft-graviton behavior is protected from loop corrections, while the first subleading behavior is anomalous/loop-modified under the standard dimensional-regularization soft limit. Higher soft orders receive additional loop corrections.

Laddha and Sen (`arXiv:1706.00759`) show that at sub-subleading order a generic quantum-gravity amplitude contains a universal contribution plus a non-universal part depending on the two- and three-point functions of the theory. Their loop proof is restricted away from four dimensions because of infrared divergences.

Laddha and Sen (`arXiv:1804.09193`) show explicitly that in four dimensions the usual soft-factor definition becomes ambiguous beyond leading order because of IR divergence, and logarithms of the soft graviton energy appear at subleading order.

## Consequence for RQIR

The local/tree `soft2` coefficients already computed remain valid **within their analytic tree scope**.

They may not be reused as the general coordinate system for the one-loop nonanalytic comparator.

At one loop the soft basis must allow a polyhomogeneous expansion. After the observable-specific leading pole has been factored or subtracted, freeze schematically

\[
F(\epsilon)=\sum_{n=0}^{N}\epsilon^n
\left[a_n+b_n\log\left(\frac{\epsilon}{\mu_{\rm soft}}\right)\right]
+R_N(\epsilon),
\]

with a declared remainder. Additional powers of the logarithm are introduced only when the perturbative order requires them.

Thus each soft order has at least two distinct coordinates:

- `soft_n_regular`;
- `soft_n_log`.

A future candidate and every loop comparator must generate both from the same parent dynamics and the same IR convention.

## Order of operations for the linked cut

The hard-channel cut and the soft limit are not to be interchanged by assumption.

Freeze the implementation order:

1. hold the soft momentum `epsilon` finite and nonzero;
2. compute the hard-channel retarded discontinuity `D_s`;
3. perform the Ward/source completion in the same finite-epsilon convention;
4. only then extract the preregistered regular and logarithmic soft coefficients.

A naive polynomial `epsilon -> 0` fit before taking the hard cut is forbidden for loop/nonanalytic columns.

## Scientific classification

- `SOFT-NG-006 — FOUR_DIMENSIONAL_LOOP_SOFT_EXPANSION_IS_POLYHOMOGENEOUS_NOT_PURE_TAYLOR`;
- `C5-CUT-007 — LOOP_C5_T_cut_REQUIRES_EXPLICIT_LOG_SOFT_COORDINATES_AND_IR_CONVENTION`;
- `REL-NG-018 — GENERIC_SUBSUBLEADING_SOFT_STRUCTURE_CONTAINS_NONUNIVERSAL_TWO_AND_THREE_POINT_INFORMATION`;
- `NG-FUNNEL-065 — DO_NOT_IDENTIFY_TREE_SOFT2_WITH_THE_LOOP_NONANALYTIC_SOFT_COEFFICIENT_WITHOUT_LOG_BASIS_EXTENSION`;
- `NG-FUNNEL-066 — TAKE_HARD_CHANNEL_DISCONTINUITY_AT_FINITE_SOFT_MOMENTUM_BEFORE_POLYHOMOGENEOUS_SOFT_EXTRACTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

This closes a protocol loophole before implementation but does not close a comparator block or produce a residual.

## Next gate

Build an executable finite-`epsilon` extraction test with at least six independent samples for the one-loop basis through `n=2`, validate exact recovery on synthetic regular+log controls, quantify conditioning/noise amplification, and demonstrate failure of a pure-Taylor fit on the same logarithmic control. This is a numerical protocol gate, not Fisher/resource analysis.
