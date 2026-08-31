# Iteration 163 — Expanded C5 quotient saturates the six-probe dRGT C4 protocol

## Scope

This iteration obeys the Iteration 162 restart instruction. It recomputes the fixed dRGT nonlinear C4 quotient after adding the explicit source-completed local C5 columns from Iteration 162. The observable layer is unchanged: the same six frozen TT ordered-response probes are used.

Comparator matrix:

`M=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`.

Targets:

`b=(alpha3,alpha4)` from the already frozen `C4-DRGT-001` point and parameter convention.

## Certificate

The expanded fixed comparator matrix is `6 x 6` and has rank `6/6` under every predeclared conditioning audit.

Raw singular values:

`(24.1048587,4.70111456,1.52500764,0.252707745,0.184809884,0.0103548959)`

with `s_min/s_max = 4.2957925700833976e-4`.

The most favorable conditioning audit (`base_row_l2`) gives

`(2.21141475,0.889290047,0.237231335,0.0807399767,0.0618913401,0.0121638094)`

and `s_min/s_max = 5.500461215995698e-3`.

Both frozen dRGT nonlinear target directions are absorbed to numerical precision. Across raw and all three row-conditioning audits, maximum absolute projection residual stays below `3.71e-14` and relative residual norms stay below `1.42e-13`.

## Scientific classification

**C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES.**

This is **regime-specific non-identifiability / finite-protocol saturation**. It is not:

- a consistency FAIL of dRGT;
- an exact theory identity between dRGT and local EFT;
- proof that the nonlinear sectors coincide outside these six observables;
- a novelty certificate.

The Iteration 157 `alpha3` residual was valid only relative to the smaller then-implemented C5 basis. It is now superseded for promotion decisions: the residual is not stable under the expanded fixed comparator quotient required by the frozen funnel.

## New funnel guardrail

**NG-FUNNEL-020 — SIX_ROW_TT_PROTOCOL_SATURATED_BY_FIXED_C5_PLUS_SHARED_BOUNDARY.**

Once a fixed comparator matrix has rank six on six frozen observable rows, adding more comparator columns cannot recover an orthogonal algebraic residual inside those same six coordinates. The next scientific move must therefore enrich the observable/protocol dimension rather than keep adding nuisance columns to a saturated six-row space.

## Consequences

1. `ANSATZ-003` remains forbidden.
2. Fisher/resources remain forbidden because no nonzero algebraic residual survives this quotient.
3. The current dRGT C4 target is not promotable on the six-TT protocol.
4. The next gate is protocol enrichment with independently frozen observables before evaluating any new candidate residual. Preferred first extension: non-TT/helicity-sensitive and/or additional off-shell triplets derived from the same source-completed dynamics, then recompute fixed C3/C4/C5/nonlocal/AS ranks without changing already frozen comparator definitions.

## Provenance

Numerical input is taken only from existing certified repository results:

- `results/c5_cubic_response_iteration150.json`;
- `results/c5_curvature_squared_retarded_tangent_iteration162.json`;
- `results/c4_drgt_nonlinear_tangent_iteration156.json`.

Reproducible audit:

- `analysis/c4_c5_protocol_saturation_iteration163.py`;
- `results/c4_c5_protocol_saturation_iteration163.json`.
