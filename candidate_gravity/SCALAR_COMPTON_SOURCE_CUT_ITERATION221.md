# Candidate Gravity — Iteration 221: gauge-safe dynamical-source cut kernel

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Using the pure-Einstein `MSSC-001` tree block from Iteration 220, construct the total-s scalar+graviton two-particle cut of gravitational Compton scattering.

The external process is scalar + plus-polarized graviton -> scalar + plus-polarized graviton. The intermediate on-shell states are one scalar and the two physical spin-2 linear polarizations. Overall Cutkosky and phase-space normalization is stripped; this iteration tests physical-state completeness and singularity geometry.

## Physical polarization sum

The intermediate plus/cross basis is rotated by several arbitrary transverse-basis angles at three generic cut directions. The summed cut kernel changes by at most

`3.96e-16` relative.

Thus the physical intermediate-state sum is basis independent to machine precision.

## Collinear structure

For angular separations `delta=[0.1,0.05,0.02,0.01,0.005,0.002]`:

- approaching the incoming graviton direction gives log-log slope `-1.98791`;
- approaching the outgoing graviton direction gives `-1.98356`;
- the two antipodal directions have slopes near zero and finite limits.

Moreover `delta^2 |I_cut|` tends to about `10` at both singular directions.

Therefore the phase-space integral has the expected logarithmic gravitational collinear/IR divergence.

## Scientific meaning

The dynamical source completion solves the **off-shell gauge ambiguity** by working directly with connected gauge-invariant amplitudes, but it does not remove real gravitational IR physics. A source-completed cut still requires an inclusive definition or an explicitly frozen hard remainder before it can enter the comparator quotient.

## Retained results

- `SRC-CUT-001 — PHYSICAL_SCALAR_GRAVITON_TWO_PARTICLE_CUT_CAN_BE_BUILT_ENTIRELY_FROM_GAUGE_INVARIANT_DYNAMICAL_SOURCE_TREE_BLOCKS`;
- `SRC-CUT-002 — INTERMEDIATE_SPIN2_POLARIZATION_SUM_IS_INVARIANT_UNDER_TRANSVERSE_BASIS_ROTATION`;
- `IR-NG-005 — SOURCE_COMPLETION_REMOVES_OFFSHELL_GAUGE_AMBIGUITY_BUT_NOT_PHYSICAL_GRAVITATIONAL_COLLINEAR_IR_DIVERGENCES`;
- `NG-FUNNEL-077 — GAUGE_SAFE_CONNECTED_SOURCE_CUTS_STILL_REQUIRE_A_DECLARED_IR_SAFE_OR_HARD_REMAINDER_COMPLETION_BEFORE_COMPARATOR_PROMOTION`.

`MODEL_READINESS: 23%` — unchanged. No Candidate Gravity residual, no `ANSATZ-003`, no Fisher/resources.
