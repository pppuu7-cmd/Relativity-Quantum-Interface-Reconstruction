# RQIR Research Log — Iteration 291

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Question

Does the scalar trace `tr(B3)` used after the weighted-kernel construction equal the actual cubic coefficient of `Tr U1` in the one-loop Vilkovisky effective action?

## Answer

No.

The exact weighted identity is `B=U1 W=Q A Q`, hence `U1=B Y_down`. Because `Y_down` depends on the background, the cubic trace contains routed `B2Y1` and `B1Y2` terms in addition to `B3Y0`.

At the frozen translation-closed checkpoint:

- `tr(B3)=0.9605914180`;
- `tr(B3Y0)=0.1071384537`;
- weight dressing `=0.6977901599`;
- complete `[Tr U1]_{sab}=0.8049286136`.

The correction is order one.

## Provenance correction

The current `B3` is background degree 3 but EOM degree 1 (`e=1,c=2`). It must not be identified with the separate EOM-degree-3 `Tr(U1U2)` / `Tr(U1^3)` sector.

## Consequence

The previous B-kernel numerator, routing and reconstruction work remains valuable, but the `tr(B3)` scalar master coefficients are proxy coefficients. The physical linear-EOM effective-action trace must be reconstructed and reduced again after the exact `Y_down` completion.

## Classification

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

No Candidate Gravity residual is declared.
