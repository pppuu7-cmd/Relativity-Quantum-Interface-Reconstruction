# Candidate Gravity — Iteration 187: asymptotic-safety joint-relation authority audit

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

Can the fixed asymptotic-safety comparator be inserted into the authoritative source-completed joint observable

`Y=(K2_rows,S_soft2_full_rows)`

without mixing incompatible Euclidean and Lorentzian inputs?

## Literature coverage

The fixed AS comparator has three distinct authority layers:

1. Pawlowski–Tränkle (2024): momentum-dependent Euclidean multi-graviton vertices and reconstructed covariant curvature form factors.
2. Pawlowski–Reichert–Wessely / Lorentzian spectral work: controlled Lorentzian graviton two-point spectral information.
3. Chiesa–Pawlowski–Reichert (2026): scalar scattering with full spacelike scalar–graviton three-point momentum dependence and a reconstructed timelike scalar–graviton vertex.

These results materially strengthen the comparator, but the current RQIR row requires a **three-graviton**, off-shell, source-completed `O(k_soft^2)` relation in the same Lorentzian/in-in parent convention as `K2`.

The available scalar–graviton timelike vertex is not that object. The Euclidean three-graviton effective action cannot simply be combined with a Lorentzian two-point function to manufacture it.

## Classification

- Lorentzian AS `K2`: `SUPPORTED_SCOPED`.
- Timelike scalar–graviton vertex: `SUPPORTED_SCOPED_BUT_WRONG_VERTEX_FOR_CURRENT_PROTOCOL`.
- Three-graviton source-completed Lorentzian soft2: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`.
- Current AS comparator column: `BLOCKED_NOT_ZERO`.

This is neither a consistency failure nor an exact comparator identity.

## Retained results

- `AS-NG-004 — LORENTZIAN_TWO_POINT_OR_SCALAR_GRAVITON_SCATTERING_DATA_DO_NOT_FIX_THE_SOURCE_COMPLETED_THREE_GRAVITON_SOFT2_RELATION`.
- `REL-NG-005 — AS_COLUMN_REMAINS_BLOCKED_UNTIL_K2_AND_THREE_GRAVITON_SOFT2_SHARE_ONE_CONTROLLED_REAL_TIME_PARENT_CONVENTION`.
- `NG-FUNNEL-042 — DO_NOT_MIX_EUCLIDEAN_THREE_GRAVITON_AND_LORENTZIAN_TWO_POINT_INPUTS_INTO_A_SYNTHETIC_COMPARATOR_COLUMN`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. AS coverage improved conceptually, but the exact current comparator coordinate is still unsupported.
