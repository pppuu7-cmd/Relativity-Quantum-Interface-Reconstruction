# Candidate Gravity — Iteration 188: stability of the unique rank-5 complement

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting span

After Iteration 186, the supported six-row conditioned comparator space is

`M=[V4,S_cond]`,

where local zero-K2 C5 has rank 4 and the conditioned exponential nonlocal comparator supplies one independent fifth direction.

Therefore a one-dimensional algebraic left complement exists in `R^6` before AS/C3 completion.

## Certificate

Singular values of the supported rank-5 matrix are

`[10.2208867, 2.16482489, 0.046278608, 0.00404433441, 6.52067013e-05]`.

The smallest nonzero singular value is `12.39` times the inherited absolute soft2 numerical envelope, so the **rank-5 statement itself** is numerically resolved.

The normalized left-null functional is approximately

`w=(-0.0001456, 0.9729630, 0.0157852, 0.0949990, 0.2052566, -0.0440300)`.

Its squared row weights show that row 1 alone carries

`0.9466570713`

of the norm: **94.67%**.

A 5000-sample fixed-seed perturbation test at the inherited entrywise error scale gives left-null rotations

- median `3.13 deg`;
- 95th percentile `9.30 deg`;
- maximum `16.83 deg`.

## Interpretation

A one-dimensional algebraic complement exists, but it is not yet a robust physical witness. It is strongly row-dominated and AS/C3 remain blocked.

The protocol must therefore be expanded prospectively before any candidate is tested against this direction.

## Retained results

- `NUM-NG-004 — CURRENT_RANK5_LEFT_NULL_IS_94P7_PERCENT_DOMINATED_BY_ONE_FROZEN_ROW`.
- `REL-NG-006 — ONE_DIMENSIONAL_ALGEBRAIC_COMPLEMENT_IS_NOT_A_ROBUST_RESIDUAL_CERTIFICATE_BEFORE_ROW_EXTENSION_AND_BLOCKED_COMPARATOR_COMPLETION`.
- `NG-FUNNEL-043 — PREREGISTER_ROW_EXTENSION_BEFORE_TESTING_ANY_MODEL_AGAINST_THE_CURRENT_LEFT_NULL`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. No candidate has been evaluated and no robust residual exists.
