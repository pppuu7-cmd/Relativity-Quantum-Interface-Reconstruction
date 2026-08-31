# RQIR Candidate Gravity — Iteration 212

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Validate the pure-Einstein five-graviton tree building block required by the direct two-particle unitarity-cut route authorized in Iteration 211.

No loop integral is attempted until the tree engine passes momentum, permutation and soft-limit checks.

## Frozen representation

Use coupling-stripped Parke–Taylor MHV Yang–Mills amplitudes with negative-helicity legs 1 and 2 and the five-point field-theory KLT representation

\[
M_5 = i s_{12}s_{34} A(12345)A(21435)
      + i s_{13}s_{24} A(13245)A(31425),
\]

with frozen convention `s_ij=<ij>[ji]`.

For the four-point reference use

\[
M_4=-i s_{12} A(1234)A(1243).
\]

The overall KLT phase/sign is a convention. It is held fixed throughout the numerical tests.

## Momentum-conserving soft family

Generate deterministic complex spinors with RNG seed `12345`. Leg 5 has positive helicity and is scaled uniformly as

\[
\lambda_5\to\sqrt\epsilon\,\lambda_5,
\qquad
\tilde\lambda_5\to\sqrt\epsilon\,\tilde\lambda_5,
\]

so `k5 -> epsilon k5`.

Keep the lambda spinors of two chosen hard legs fixed and solve their two tilde spinors exactly from

\[
\sum_{i=1}^5 \lambda_i\tilde\lambda_i=0.
\]

All legs remain null while momentum conservation is preserved at every finite epsilon.

## Numerical certificate

For

`epsilon = [1e-1,5e-2,2e-2,1e-2,5e-3,2e-3,1e-3,5e-4,2e-4,1e-4]`

we obtain:

- maximum momentum-conservation residual: `1.5291e-15`;
- maximum relative discrepancy over four nontrivial gravity relabelings: `5.7311e-12`;
- asymptotic log-log fit on the six smallest epsilon values:

\[
|M_5|\propto \epsilon^{-0.9997978278},
\]

with absolute exponent error `2.0217e-4` relative to Weinberg's `epsilon^-1` energy-soft scaling.

For the leading positive-helicity soft factor `S0`, the frozen KLT convention gives

\[
\frac{M_5}{S^{(0)}M_4}\to -1.
\]

At `epsilon=1e-4` the distance to `-1` is `1.9878e-5`, with approximately linear convergence in epsilon across the tested range.

## Scientific classification

- momentum conservation: `PASS_MACHINE_PRECISION`;
- gravity permutation/relabeling: `PASS_NUMERICAL`;
- leading Weinberg soft power: `PASS_SCOPED`;
- leading soft-factor normalization: `PASS_UP_TO_FROZEN_OVERALL_KLT_SIGN`;
- one-loop cut: not yet evaluated.

Retain:

- `C5-CUT-010 — DETERMINISTIC_FIVE_GRAVITON_KLT_TREE_ENGINE_PASSES_MOMENTUM_PERMUTATION_AND_LEADING_SOFT_CHECKS`;
- `SOFT-NG-008 — MOMENTUM_CONSERVING_UNIFORM_SOFT_FAMILY_RECOVERS_WEINBERG_EPSILON_MINUS_ONE_SCALING`;
- `NUM-NG-017 — TREE_ENGINE_IS_VALIDATED_BEFORE_ANY_TWO_PARTICLE_CUT_INTEGRATION`;
- `NG-FUNNEL-069 — PHYSICAL_LOOP_CUT_CONSTRUCTION_MUST_BE_BUILT_FROM_A_VALIDATED_TREE_ENGINE_AND_FIXED_CROSSING_HELICITY_CONVENTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

A reusable computational building block is now closed, but the physical five-point one-loop discontinuity is still absent.

## Next gate

Freeze one physical two-particle cut channel for the five-graviton amplitude, including:

1. external 2->3 massless kinematics with a finite positive-helicity soft leg;
2. cut partition and crossing conventions;
3. complete physical intermediate-helicity sum;
4. two-body phase-space parameterization;
5. explicit treatment of angular/soft IR endpoints;
6. normalization of `Disc/(2 pi i)`.

Only after preregistration should the cut be numerically integrated across the frozen epsilon grid and passed to the Iteration-210 regular+log extractor.
