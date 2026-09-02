# Candidate Gravity C5 — Iteration 291 U1 trace weight completion

**Date:** 2026-09-03  
**MODEL_READINESS:** **24%**

## Purpose

Audit whether the scalar `orbit_trace = tr(B3)` used in Iterations 278–289 is the actual cubic coefficient of the one-loop Vilkovisky insertion `Tr U1`.

The frozen exact orientation from Iterations 252/256 is

`B := U1 W = Q A Q`,

with `Q=N_orb^{-1}` and `W^{-1}=Y_down=sqrt(|g|) g`.

Therefore

`U1 = B Y_down`.

Consequently the cubic background coefficient of `Tr U1` is not `tr(B3)` whenever `Y_down` carries background dependence.

## Exact mixed cubic trace

For distinguishable translation-closed legs `(s,a,b)`, with the rightmost local `Y` insertion acting first, the complete coefficient is

`[Tr U1]_{sab} =`

`tr(B3[sab](p) Y0)`

`+ tr(B2[sa](p+k_b) Y1[b])`

`+ tr(B2[sb](p+k_a) Y1[a])`

`+ tr(B2[ab](p+k_s) Y1[s])`

`+ tr(B1[s](p+k_a+k_b) Y2[ab])`

`+ tr(B1[a](p+k_s+k_b) Y2[sb])`

`+ tr(B1[b](p+k_s+k_a) Y2[sa])`.

No new propagator is introduced by `Y_down`; it is a local weight insertion, but its momentum and matrix contraction change the numerator and the routing of the lower-background-order `B` blocks.

## Frozen translation-closed checkpoint

Using exactly the Iteration-273 kinematics:

- old proxy `tr(B3) = 0.9605914180462887`;
- correct flat-weight term `tr(B3 Y0) = 0.1071384536577547`;
- sum of the background-weight dressing terms `B2Y1+B1Y2 = 0.6977901599155829`;
- complete cubic coefficient
  `[Tr U1]_{sab}(p0) = 0.8049286135733377`.

The weight completion is therefore order-one and cannot be treated as a negligible convention correction.

Individual dressing terms:

- `B2[sa] Y1[b] = +0.12881941529711502`;
- `B2[sb] Y1[a] = +0.0928494721362878`;
- `B2[ab] Y1[s] = +0.2229526110219082`;
- `B1[s] Y2[ab] = -2.39e-16`;
- `B1[a] Y2[sb] = +0.2437591436830562`;
- `B1[b] Y2[sa] = +0.009409517777215947`.

The null-soft control remains intact: `||B1[s]||_F = 4.15e-9`. The first-order metric-density coefficient satisfies `Y1[x]=epsilon_x` to maximum component error `7.23e-11`.

## Scope correction to Iterations 278–289

Those iterations remain valid calculations of the weighted symmetric kernel `B=U1W` and its denominator/tensor structure. In particular their nonzero B3 certificates, routing checks, numerator-basis audits and DR reduction diagnostics remain useful.

However, the scalar quantity obtained there from `tr(B)` is **not** the effective-action trace `Tr U1`.

Therefore the Iteration-287 bubble coefficients and Iteration-289 triangle pole residue are not authoritative coefficients of the `-(i/2)Tr U1` sector. They must not be discarded as computational diagnostics, but they must be recomputed after the exact `Y_down` trace completion.

Freeze guardrail:

`ITERATIONS278_289_TRACE_B3_RESULTS_ARE_WEIGHTED_KERNEL_PROXY_RESULTS_NOT_TR_U1_AUTHORITY`.

## EOM-degree provenance

A second ambiguity is closed simultaneously.

`B3=[U1W]_{h^3}` means cubic **background perturbation degree**. Since `A=R(DR)E` contains one explicit equation-of-motion insertion, this sector remains

`e=1, c=2`

in the Iteration-243 finite-`R^3` bookkeeping.

It is not the EOM-degree-three sector

`+(i/2)Tr(U1 U2) - (i/6)Tr(U1^3)`.

Thus a complete finite `R^3` Vilkovisky connection result still requires separately:

- `e=1,c=2`: the present `Tr U1` sector after weight completion;
- `e=2,c=1`: dressed `Tr U2` and `Tr U1^2`;
- `e=3,c=0`: `Tr(U1U2)` and `Tr(U1^3)`.

The determinant sector `e=0,c=3` is also separate.

## Classification

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

This is an upstream authority correction, not a Candidate Gravity residual and not a consistency failure.

## Current blocker

`BLOCKED_P_DEPENDENT_COMPLETE_TR_U1_E1C2_NUMERATOR_AND_REDUCTION_AFTER_WEIGHT_COMPLETION`.

The Iteration-290 source/IR classification remains downstream. The measured `-0.0612898138/epsilon` weighted-kernel proxy pole cannot be classified as the pole of `Tr U1` before this corrected trace is reduced.

## Next gate — Iteration 292

1. Construct a p-dependent oracle for the complete `[Tr U1]_{sab}` expression above.
2. Canonicalize the denominator families after including `B3Y0`, `B2Y1` and `B1Y2` terms with exact routing.
3. Determine complete numerator degree ceilings and held-out polynomial reconstruction bases.
4. Tensor-reduce the corrected non-scaleless families and repeat the Laurent pole audit.
5. Only then return to the linked/source/Ward/Born-IR A/B classification.

`ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
