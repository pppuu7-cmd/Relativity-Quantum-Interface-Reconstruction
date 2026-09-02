# Recovery delta — RQIR Iteration 272

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

## New frozen result

Iteration 270's explicit nonzero `B3` was evaluated as an open Fourier kernel `<p+K|B3|p>` at `K=(1.1,0.8,0.85,0.8)`, so `K != 0`. Iteration 271 exposed the corresponding open resolvent census (23 primitive branches, up to four distinct routed Q0 factors).

Translation invariance of the closed three-point trace requires

`k_s+k_a+k_b=0`

through the global Fourier delta distribution. Freeze

`PASS_EXACT_TRANSLATION_TRACE_CLOSURE_GATE`.

Correct status of Iteration 270:

`VALID_OFF_CONSERVATION_SURFACE_PARENT_KERNEL_NONIDENTICAL_ZERO_CERTIFICATE; NOT_YET_PHYSICAL_THREE_POINT_NONZERO`.

Operational blocker:

`BLOCKED_PHYSICAL_B3_NONZERO_UNTIL_K_SUM_ZERO_RERUN`.

## Closed rerun

Keep `k_s=(1,0,0,1)` and `k_a=(0.25,0.6,0.3,0.15)`, set

`k_b=(-1.25,-0.6,-0.3,-1.15)`

and rebuild an independent TT polarization for b.

Executable certificate added:

`candidate_gravity/code/iteration273_closed_kinematics_physical_b3.py`.

It reuses the exact Iteration-270 routed implementation and classifies the K=0 result without assuming nonzero.

## Guardrails

- Do not call a K-nonzero fixed-p kernel a physical closed three-point comparator.
- Do not perform master reduction before translation closure and p-dependent integrand reconstruction.
- Do not discard Iteration 270: it remains evidence that the parent cubic kernel is not identically zero away from the conservation surface.
- Do not create `ANSATZ-003`; Fisher/resources remain forbidden.

## Next gate

Execute Iteration 273. If the translation-closed B3 is stably nonzero, reconstruct/sample the full p-dependent closed numerator, derive the actual denominator families, then proceed to tensor/master reduction and linked hard-channel/source projection.
