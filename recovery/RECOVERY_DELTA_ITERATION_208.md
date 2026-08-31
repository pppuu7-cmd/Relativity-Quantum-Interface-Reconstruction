# Recovery Delta — RQIR Iteration 208

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 207 froze `BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`: no directly reusable finite nonlocal curvature-cubic pure-Einstein Vilkovisky-DeWitt result was found for the off-shell/source-completed RQIR cut.

## New authoritative result

A separate **physical on-shell standard-QG nonanalytic anchor** exists.

Dunbar–Norridge (`hep-th/9408014`) computed the one-loop four-graviton amplitude, including pure gravity, and its unitarity structure. For a declared channel, the branch discontinuity is fixed by a two-particle phase-space integral of products of tree Einstein amplitudes, summed over physical intermediate graviton helicities.

Local analytic counterterms have zero branch discontinuity in their analytic domain, so this provides a clean positive control for the local-tower-null principle behind `T_cut`.

Massless gravitational loops are infrared divergent at the virtual-amplitude level. Donoghue–Torma (`hep-th/9901156`) show that the remaining dimensional pole is infrared and that the physical graviton-graviton cross section is finite and model-independent when soft bremsstrahlung is included. Therefore the operational anchor must be inclusive/IR-safe or use a separately preregistered IR-subtracted hard amplitude.

## Classification

- `C5-SMATRIX-CUT-001`: `PASS_SCOPED` as a gauge-invariant nonanalytic C5 positive control;
- raw virtual amplitude: not an operational observable without IR completion;
- off-shell/source-completed `T_cut`: still `BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`.

## Retained results

- `C5-CUT-006 — PURE_EINSTEIN_ONE_LOOP_FOUR_GRAVITON_UNITARITY_CUT_IS_A_GAUGE_INVARIANT_NONANALYTIC_POSITIVE_CONTROL`;
- `IR-NG-001 — RAW_VIRTUAL_GRAVITON_CUT_IS_NOT_AN_OPERATIONAL_ANCHOR_WITHOUT_IR_COMPLETION_OR_SUBTRACTION`;
- `C5-NG-021 — AT_DECLARED_ONE_LOOP_LOW_ENERGY_ORDER_THE_PHYSICAL_GRAVITON_SCATTERING_RESULT_IS_MODEL_INDEPENDENT_AND_FIXED_BY_NEWTONS_CONSTANT`;
- `NG-FUNNEL-064 — ONSHELL_NONANALYTIC_POSITIVE_CONTROL_DOES_NOT_REPLACE_THE_OFFSHELL_SOURCE_COMPLETED_LINKED_CUT`.

## Readiness

`MODEL_READINESS: 23%`, unchanged. The physical C5 nonanalytic sector has a robust benchmark, but the actual RQIR comparator column is not closed.

## Exact restart instruction

Resume at **Iteration 209 — loop-soft bridge audit**.

Audit loop-corrected leading/subleading/subsubleading soft-graviton relations in four dimensions, including infrared logarithms. Determine whether the frozen RQIR `soft2` coordinate remains a pure Taylor coefficient in the loop/nonanalytic sector or must be extended by explicit `soft^m log(soft)` coordinates. Do not infer the off-shell `T_cut` from the tree soft theorem. If logarithmic soft terms are mandatory, freeze the polyhomogeneous soft basis before any loop comparator implementation.

No `ANSATZ-003`, Fisher or resources.
