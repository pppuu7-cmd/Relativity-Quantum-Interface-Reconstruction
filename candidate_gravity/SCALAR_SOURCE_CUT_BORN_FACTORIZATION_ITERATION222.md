# Candidate Gravity — Iteration 222: Born-fixed IR factorization of the source cut

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Iteration 221 established a gauge-safe connected `MSSC-001` scalar+graviton cut with two logarithmic collinear singularities. Iteration 222 determines the local residues **before angular integration**, without fitting cap-regulated integrals.

Define locally

`R = lim_(delta->0) [1-cos(delta)] I_cut`.

The audit uses five frozen external scattering angles and both independent real linear spin-2 external polarizations (plus and cross). The residue/Born ratio is extrapolated from the fixed local samples `delta=0.01,0.005,0.002,0.001,0.0005`.

Result in the stripped normalization used since Iteration 219:

`R_in = R_out = -8 M_Born`.

Across all ten angle/polarization tests:

- worst extrapolated deviation of `R/M_Born` from `-8`: `3.15e-6`;
- worst incoming/outgoing ratio mismatch: `3.54e-6`.

This is a cross-kinematic factorization result, not a cap fit.

## Consequence

The leading collinear subtraction coefficient of the connected source cut is fixed by the **complete gauge-invariant scalar Compton Born amplitude**. It is not an adjustable source/contact parameter and must not be estimated from regulated phase-space growth.

## Retained results

- `SRC-CUT-003 — BOTH_SCALAR_SOURCE_CUT_COLLINEAR_RESIDUES_FACTORIZE_AS_MINUS_EIGHT_TIMES_THE_COMPLETE_COMPTON_BORN_AMPLITUDE_IN_THE_FROZEN_NORMALIZATION`;
- `IR-NG-006 — SOURCE_CUT_IR_RESIDUES_MUST_BE_FIXED_LOCALLY_BY_BORN_FACTORIZATION_NOT_BY_REGULATED_PHASE_SPACE_FITS`;
- `NG-FUNNEL-078 — CONNECTED_SOURCE_HARD_REMAINDERS_REQUIRE_BORN_FIXED_IR_COMPLETION_BEFORE_LINKED_CUT_COMPARISON`.

## Readiness

`MODEL_READINESS: 23%` — unchanged. The IR coefficient is fixed, but the finite/inclusive source cut is not yet an authoritative comparator column.
