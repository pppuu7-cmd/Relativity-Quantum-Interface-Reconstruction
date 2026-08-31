# Recovery Delta — RQIR Iteration 212

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 211 corrected the physical import route: the four-graviton one-loop anchor is a hard cut control, not a generic independent one-soft amplitude. A genuine soft cut requires at least five external legs, and direct tree unitarity was authorized.

## New authoritative result

A deterministic pure-Einstein five-graviton MHV tree engine has been implemented using Parke–Taylor Yang–Mills amplitudes and the field-theory five-point KLT relation.

A complex momentum-conserving family uniformly scales positive-helicity leg 5 as `k5 -> epsilon k5` while solving two hard tilde spinors exactly for momentum conservation.

Numerical certificate:

- max momentum-conservation residual `1.5290569968e-15`;
- max relative discrepancy across four nontrivial gravity relabelings `5.7311239179e-12`;
- asymptotic soft power from the six smallest epsilon values `-0.9997978278`;
- expected energy-soft power `-1`;
- at `epsilon=1e-4`, `M5/(S0 M4)` is within `1.98778e-5` of `-1`, where the minus sign is the frozen overall KLT/sign convention.

## Classification

- tree engine: `PASS_SCOPED`;
- loop cut: not yet implemented;
- candidate residual: none.

## Retained results

- `C5-CUT-010 — DETERMINISTIC_FIVE_GRAVITON_KLT_TREE_ENGINE_PASSES_MOMENTUM_PERMUTATION_AND_LEADING_SOFT_CHECKS`;
- `SOFT-NG-008 — MOMENTUM_CONSERVING_UNIFORM_SOFT_FAMILY_RECOVERS_WEINBERG_EPSILON_MINUS_ONE_SCALING`;
- `NUM-NG-017 — TREE_ENGINE_IS_VALIDATED_BEFORE_ANY_TWO_PARTICLE_CUT_INTEGRATION`;
- `NG-FUNNEL-069 — PHYSICAL_LOOP_CUT_CONSTRUCTION_MUST_BE_BUILT_FROM_A_VALIDATED_TREE_ENGINE_AND_FIXED_CROSSING_HELICITY_CONVENTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Exact restart instruction

Resume at **Iteration 213 — physical five-point s-channel cut preregistration and IR endpoint diagnostic**.

Freeze a real massless 2->3 family with total `s=1`, one outgoing positive-helicity soft graviton, and two hard outgoing gravitons obtained as a two-body decay of the recoiling hard subsystem. Use the all-outgoing MHV external helicity convention `--+++`. For the total-s two-particle cut, use left `M4(--++)` and right `M5(++ + --)` after crossing the cut states. Verify that the complete physical helicity sum reduces as expected from tree helicity selection rules. Parameterize the cut pair by the two-body CM sphere. Before any physical extraction, diagnose the angular endpoint behavior and demonstrate whether the raw cut integral depends logarithmically on a collinear cap. If so, classify it as universal IR contamination and require an analytic subtraction/inclusive completion before the Iteration-210 log-soft extractor.

No `ANSATZ-003`, Fisher or resources.
