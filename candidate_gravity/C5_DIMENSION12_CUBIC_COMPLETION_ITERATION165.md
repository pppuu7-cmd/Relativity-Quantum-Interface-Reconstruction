# RQIR Candidate Gravity — Iteration 165

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

Does the scoped dRGT `dalpha3` residual from Iteration 164 survive target-independent completion of the already-authorized local C5 cubic TT sector through the pre-existing dimension-12 cutoff?

## Frozen scope

The 12 TT rows of Iteration 164 are unchanged. No row, polarization, acceptance criterion, target parameter, or conditioning rule is retuned.

The pure local-C5 base is

`[EH, Ricci^3, Riemann^3, Ricci^2_full, Ricci Box Ricci_full]`.

The target-independent completion adds:

- mixed `Ricci Ricci Riemann` at cubic curvature order;
- `Box^n` descendants, `n=1,2,3`, of the already-declared Ricci-chain and Riemann-chain cubic invariants;
- the cutoff remains dimension 12, inherited from the frozen C5 convention.

These new operators start at `O(h^3)` about Minkowski, so their cubic TT vertices are products of linearized curvatures with flat `Box` factors. Their operator-specific quadratic term vanishes, and the scoped Ward test reduces to replacing one leg by a pure-gauge polarization and checking the cubic form vanishes.

## Numerical certificate

The resulting local C5 matrix has shape

`12 x 12`

and

`rank(V_C5)=12/12`.

Raw singular values:

`[25.2073630193, 11.0655202335, 2.78800330137, 1.22622203362, 0.149132094653, 0.0780853642444, 0.0732102830245, 0.0288591359907, 0.0110612427541, 0.00345543721171, 0.00123134679482, 0.0000713811211049]`.

Thus

`s_min/s_max = 2.8317567788e-6`

for the raw matrix. The fixed conditioning audits remain full rank.

Adding the corrected dRGT targets `d/d log(m^2)` and `d/d alpha3` does not increase rank:

`rank([V_C5,T])=12`.

Their residuals are numerical zero at the finite-protocol level. Raw relative residuals are approximately

- `dlogm2`: `1.18e-15`;
- `dalpha3`: `8.68e-15`.

## Ward certificate

Maximum gauge-leg residuals:

- linearized Ricci: `2.22e-16`;
- linearized Riemann: `1.11e-16`;
- derivative descendants: `6.14e-17`;
- mixed Ricci-Ricci-Riemann: `1.63e-17`.

Classification: `PASS_SCOPED_MACHINE_PRECISION`.

## Scientific classification

Retain:

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

`C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE ADDITIONAL BLOCKED COMPARATORS CANNOT RESTORE A RESIDUAL IN THAT SAME SPACE`.

This is **finite-protocol saturation / regime-specific non-identifiability**. It is not an exact identity between dRGT and local EFT and not a consistency FAIL of dRGT.

The Iteration-164 `dalpha3` residual was valid against the smaller implemented basis, but it does not survive the authorized C5 basis completion and therefore loses all novelty status.

Because a physically authorized C5 subset alone spans all 12 frozen TT rows, currently BLOCKED C3/nonlocal/AS columns cannot restore an orthogonal residual inside this same row space. They remain necessary for other protocols and for theory-level claims.

## Gate discipline

- `ANSATZ-003`: not created;
- Fisher/resources: forbidden because the algebraic residual in this finite sector is zero;
- no blocked comparator is zero-filled;
- no frozen gate is weakened.

## Readiness

`MODEL_READINESS: 24%`, up from 23%.

- comparator foundation: `24/25`;
- robust unique residual: `0/20`;
- frozen parent dynamics/ANSATZ: `0/20`;
- candidate consistency/positivity/Ward/causality: `0/15`;
- identifiability/Fisher: `0/10`;
- resource/experiment closure: `0/10`.

The +1 is awarded only for closing a substantial local-C5 comparator-basis gap. No residual-readiness points are awarded.

## Exact next gate

Iteration 166 must leave the saturated 12-dimensional observable space without target-driven tuning. Freeze additional observable rows before inspecting target residuals, preferably by a deterministic extension of the same source-completed metric protocol to more than 12 independent rows and/or an independently defined helicity/non-TT block. Recompute the fixed 12-column C5 rank first, then the corrected dRGT targets. Do not create `ANSATZ-003` unless a residual survives the expanded fixed comparator quotient.