# Candidate Gravity — Iteration 194: local zero-K2 C5 span on withheld v2

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Scope

Evaluate the frozen local zero-K2 curvature-cubic C5 comparator on `RQIR-WITHHELD-NULLSOFT-12-v2`. No candidate is evaluated.

For cyclic `Riemann^3`, the linearized soft Riemann is exactly proportional to `k_soft^2`. Therefore the leading soft2 coefficient can be evaluated directly at `(k0,q,-q)` without numerical soft extrapolation.

Using the exact Iteration-178 null-soft identities, the local dimension-12 span is

`V4 = Riemann3_soft2 * {1,-q^2,q^4,-q^6}`.

## Result

On twelve withheld rows:

- rank `4/12`;
- singular values `[1.1350290414,0.1259090262,0.0173586351,0.0011354930]`;
- condition number `999.5914`.

Thus the local zero-K2 soft2 algebraic complement has dimension `8` before unsupported AS/C3 completion.

Iteration 191 separately established that the fixed nonlocal lambda direction has no exact K2-preserving null combination with the six local quadratic Wilson directions on these same q-points. Therefore that old six-row conditioned nonlocal nuisance direction is not carried into the exact zero-delta-K2 withheld quotient.

## Interpretation

The withheld protocol is substantially less saturated than the original six-row protocol. This is encouraging for future identifiability, but the eight-dimensional complement is **not** Candidate Gravity novelty: AS and C3 are still unsupported, and no candidate has been tested.

## Retained results

- `C5-NG-014 — WITHHELD_V2_ZERO_K2_LOCAL_DIM12_CURVATURE_CUBIC_SOFT2_SPAN_REMAINS_RANK4`.
- `NUM-NG-008 — EXACT_RIEMANN_SOFT2_COEFFICIENT_REMOVES_SOFT_EXTRAPOLATION_ERROR_FOR_THE_CURVATURE_CUBIC_BASE`.
- `REL-NG-009 — WITHHELD_V2_LEAVES_EIGHT_SOFT2_RELATION_DIMENSIONS_BEFORE_BLOCKED_AS_C3_COMPLETION`.

## Readiness

`MODEL_READINESS: 24%` — unchanged.
