# RQIR Candidate Gravity — Iteration 201

## Frozen cross-polarization robustness gate

This gate is frozen before any `ANSATZ-003` or other promotable Candidate Gravity target is instantiated.

### Validation protocols

Preserve independently:

- `v3-A`: the prospectively frozen automation polarization protocol;
- `v3-B`: the prospectively frozen concurrent manual polarization protocol.

They share the same hard q-nodes but define different TT row functionals. Neither may be replaced after candidate evaluation.

## Candidate contract

A future candidate must declare one parent dynamics and one parameter convention. For the same candidate parameter `beta`, that dynamics must derive both protocol-specific tangent vectors

`b_A = dY_A/dbeta | beta=0`,

`b_B = dY_B/dbeta | beta=0`,

where each `Y_P` is the full supported joint relation for that frozen protocol, including hard K2 and the protocol-specific nonlinear/soft rows.

It is forbidden to fit independent `beta_A` and `beta_B` merely to make both protocols pass.

## Comparator subtraction

For each protocol separately construct only the physically authorized comparator/nuisance map `M_P` in that protocol's row coordinates. Unsupported AS/C3 components remain BLOCKED and are not zero-filled.

Apply exact hard constraints before any profiling/Fisher step. Define the supported algebraic residual

`r_P = (I - M_P M_P^+) b_P`

or the equivalent hard-constrained quotient representation appropriate to the final joint map.

## Frozen decision rule

Before candidate promotion, require:

1. `r_A != 0` above the declared numerical/model error envelope;
2. `r_B != 0` above the declared numerical/model error envelope;
3. both tangents derive from the same parent dynamics and the same `beta` convention;
4. neither protocol was selected, reweighted, reseeded, or dropped after seeing candidate residuals;
5. the residual interpretation survives the fixed C3/C4/C5/nonlocal/AS authority boundary for each protocol.

Classification:

- pass only A or only B: `POLARIZATION_SPECIFIC_IDENTIFICATION_INSUFFICIENT_FOR_PROMOTION`;
- pass A and B but AS/C3 still unresolved: `CROSS_POLARIZATION_SUPPORTED_BUT_COMPARATOR_INCOMPLETE`;
- pass A and B after full fixed comparator closure: eligible for the next candidate-consistency gates, not automatically new physics.

## 24-row dual-setting rule

A future protocol that measures both A and B settings as separate rows may be frozen as an additional validation layer. It uses the **same theory parameters** across both settings. The alternate-subspace union rank of Iteration 200 must never be interpreted as extra theory parameters.

A combined 24-row pass cannot substitute for a failure of the separately frozen A/B robustness requirement unless a new protocol version is preregistered before candidate construction with an explicit reason for replacing the separate-pass rule.

## Retained results

- `PROTO-NG-008 — CANDIDATE_PROMOTION_REQUIRES_SEPARATE_PASS_ON_TWO_PROSPECTIVELY_FROZEN_TT_POLARIZATION_PROTOCOLS`.
- `REL-NG-014 — SAME_PARENT_DYNAMICS_AND_SINGLE_PARAMETER_CONVENTION_MUST_GENERATE_BOTH_PROTOCOL_SPECIFIC_TANGENTS`.
- `NG-FUNNEL-055 — POLARIZATION_SPECIFIC_RESIDUAL_IS_NOT_A_ROBUST_CANDIDATE_GRAVITY_DISCRIMINATOR`.
- `NG-FUNNEL-056 — COMBINED_MULTI_SETTING_LIKELIHOOD_MAY_NOT_HIDE_FAILURE_OF_A_PREREGISTERED_CROSS_PROTOCOL_GATE`.

`MODEL_READINESS: 24%` — unchanged. This freezes an anti-overfitting rule; it does not discover a candidate residual or close AS/C3.
