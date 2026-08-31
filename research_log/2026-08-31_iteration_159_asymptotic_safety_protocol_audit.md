# RQIR Research Log — Iteration 159

**Date:** 2026-08-31  
**Branch:** Candidate Gravity comparator funnel  
**MODEL_READINESS: 23%**

## Starting front

Iteration 158 added the first fixed partial nonlocal comparator and set model readiness to 22% under the frozen model-only rubric. The remaining missing strong quantum comparator family was asymptotic safety.

## Fixed realization

`AS-PT-001` is frozen to Pawlowski & Tränkle, Phys. Rev. D 110, 086011 (2024), arXiv:2309.17043.

This work reconstructs a diffeomorphism-invariant effective action from fully dressed multi-graviton correlation functions in a systematic vertex expansion. The background effective action is truncated through `R^2` and `R_mn R^mn` form factors with full covariant momentum dependence.

The TT reconstruction uses

`Gamma_tt^(n)(p_vec)=gamma_g^(n)(p) T_R,tt^(n)(p_vec)`

at the momentum-symmetric point.

For the TT three-point operator selection:

- `R^2` has zero TT 3-point overlap;
- `R_mn R^mn` has nonzero overlap;
- hence the `p^4` TT three-point contribution is attributed to the Ricci-squared sector within the declared truncation.

Literature anchors:

- Pawlowski & Tränkle, arXiv:2309.17043 / PRD 110, 086011;
- Denz, Pawlowski & Reichert, arXiv:1612.07315;
- contextual Lorentzian progress: Assant, Litim & Reichert, arXiv:2606.19321; Chiesa, Pawlowski & Reichert, arXiv:2603.10168.

## Finite protocol audit

The six RQIR probes use general off-shell triplets `(p,-q,-r)`.

Squared leg virtualities and relative spreads:

1. `(0.7473,0.5076,0.3313)`, spread `0.7867860`;
2. `(0.6157,0.3854,0.2935)`, spread `0.7466399`;
3. `(0.4418,0.4260,0.2746)`, spread `0.4390756`;
4. `(0.6120,0.3153,0.2773)`, spread `0.8335547`;
5. `(0.6682,0.4004,0.2278)`, spread `1.0191299`;
6. `(0.4239,0.2882,0.2321)`, spread `0.6094048`.

Symmetric-compatible probes: `0/6`.

Therefore the published symmetric-point scalar TT dressing cannot be directly evaluated on the frozen RQIR six-probe protocol.

Reproducible authority:

- `analysis/asymptotic_safety_protocol_audit_iteration159.py`;
- `results/asymptotic_safety_protocol_audit_iteration159.json`.

## Lorentzian/retarded boundary

The 2024 reconstruction starts from the Euclidean effective action and Wick-rotates the reconstructed action. This is not yet the same as a source-completed in-in/CTP retarded pure-graviton three-point kernel on the six RQIR triplets.

Recent Lorentzian spectral-function and scalar-scattering work demonstrates technical progress toward Lorentzian observables, but those separate computations are not treated as if they were the missing pure-graviton kernel of `AS-PT-001`.

## Decision

`BLOCKED_OFF_SYMMETRIC_RETARDED_VERTEX_MAP`.

This is not a consistency FAIL.

## New retained results

### `AS-NG-001 — SYMMETRIC_POINT_VERTEX_NOT_GENERAL_OFFSHELL_TANGENT`

A symmetric-point momentum-dependent 3-graviton dressing cannot be inserted as a general off-shell `chi2R` tangent.

### `NG-FUNNEL-016 — FIXED_TRUNCATION_STILL_REQUIRES_KINEMATIC_AND_CAUSAL_MAP`

A fixed theory/truncation only enters the RQIR quotient after its published kinematic domain and causal/retarded prescription cover the actual measurement protocol.

## Readiness accounting

Previous: `22%`.

**MODEL_READINESS: 23%**.

Reason for +1 point: comparator foundation increases `19/25 -> 20/25` because a specific AS truncation is now frozen and its exact RQIR embedding boundary is known. It does not receive full comparator credit because no six-probe AS tangent has been computed.

Unique residual discovery stays `3/20`; parent dynamics, candidate consistency, Fisher and resource blocks remain zero.

## Next gate — Iteration 160

The comparator landscape is now broad enough to switch from adding class labels to a **supported-row combined quotient audit**:

1. assemble only rows/columns that are genuinely shared and derived across the fixed C3/C4/C5/nonlocal blocks;
2. quantify which finite observable directions remain outside the currently implemented comparator span under common-boundary/gain conditioning;
3. keep AS and all other missing rows as explicit BLOCKED masks, not zeros;
4. identify whether any robust residual target is sufficiently well-defined to motivate a candidate parent dynamics, or whether one specific blocked comparator sector must be closed first;
5. no `ANSATZ-003` unless the target survives this supported-row quotient and cannot be trivially assigned to a blocked known-comparator direction.
