# Recovery Delta — RQIR Candidate Gravity Iteration 180

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Previous authoritative front:** Iteration 179

## Source-of-truth files

- `analysis/c4_massless_spin2_boundary_iteration180.py`
- `results/c4_massless_spin2_boundary_iteration180.json`
- `candidate_gravity/C4_MASSLESS_SPIN2_BOUNDARY_ITERATION180.md`
- `research_log/2026-08-31_iteration_180_c4_massless_spin2_boundary.md`

## New result

The strongest finite local/unitary C4 control compatible with the physical null-soft spin-2 carrier is frozen as a single massless spin-2 field with conserved/universal stress coupling, self-consistent nonlinear completion, and local EFT freedom through the same dimension-12 order as C5.

Under this scoped boundary, its `B_T` span is exactly the same four-dimensional local massless-spin-2 EFT span as C5:

`rank(V_C5)=4`, `rank(V_C4_massless)=4`, `rank([V_C5,V_C4_massless])=4`.

Classification:

`SCOPED_EXACT_BOUNDARY_MERGER_WITH_C5_LOCAL_MASSLESS_SPIN2_EFT`.

The existing nonzero-mass dRGT control remains `BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH` from Iteration 179.

## Retained results

- `C4-NG-011 — CONSISTENT_LOCAL_MASSLESS_SPIN2_MEDIATOR_CONTROL_MERGES_WITH_C5_SOFT_BOUNDARY_AT_FROZEN_ORDER`.
- `SOFT-NG-007 — SEMANTIC_GRAVITY_VS_MEDIATOR_LABEL_IS_NOT_AN_OPERATIONAL_DISCRIMINATOR_WHEN_PARENT_DYNAMICS_AND_SOURCE_MAP_COINCIDE`.
- `NG-FUNNEL-038 — C4_NULL_SOFT_CONTROL_SPLITS_INTO_PROTOCOL_INCOMPATIBLE_MASSIVE_CASE_OR_C5_BOUNDARY_MASSLESS_CASE_UNDER_SCOPED_ASSUMPTIONS`.

## Guardrail

Do not generalize the merger beyond the declared local/unitary single-massless-spin-2 assumptions. Other mediator spins, nonlocality, extra fields, Lorentz violation, different source maps or nonunitary dynamics require separate comparators.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Exact next gate

Iteration 181: compute the `B_T` projection of the fixed covariant nonlocal comparator `QG-NL-EXP-001` from its full parent action, including the Frechet operator insertion, on the exact same six rows. Test whether it enlarges the current local rank-4 span.
