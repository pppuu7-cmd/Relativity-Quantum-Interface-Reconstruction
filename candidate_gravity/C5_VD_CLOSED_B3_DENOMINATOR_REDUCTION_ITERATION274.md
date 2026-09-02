# RQIR Candidate Gravity — Iteration 274

## Exact closed B3 denominator-family reduction

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Iteration 273 certified an explicitly nonzero null-soft `B3=[Q A Q]_3` on the momentum-conservation surface `k_s+k_a+k_b=0`. This iteration repeats the Iteration-271 inverse-recursion census after imposing that exact closure relation.

The 15 surviving null-soft terms expand into the same 23 primitive inverse-recursion branches. In the open K-nonzero census these contained 2, 3 or 4 distinct routed `Q0` shifts. Under exact closure, the total-shift subset `{s,a,b}` becomes identical to the empty shift, so every primitive branch acquires one repeated scalar propagator segment.

Exact closed census:

- **1** branch: one distinct denominator with power pattern `(2)`;
- **10** branches: two distinct denominators with powers `(2,1)` — raised bubbles;
- **12** branches: three distinct denominators with powers `(2,1,1)` — raised triangles;
- **0** branches with four or more distinct scalar denominators.

Origin decomposition:

- `A3 Q0 Q0`: 1 squared-single-denominator branch;
- `Q1 A2 Q0`: 6 raised bubbles;
- `Q2_contact A1`: 4 raised bubbles;
- `Q2_sequential A1`: 8 raised triangles;
- `Q1 A1 Q1`: 4 raised triangles.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_RAISED_BUBBLE_TRIANGLE_DENOMINATOR_REDUCTION`.

## Consequence

The apparent four-distinct-resolvent structures of Iteration 271 were a property of the **open** fixed-`p` kernel, not of the translation-closed cubic trace. After enforcing `K=0`, no scalar box or higher polygon survives. This independently restores the Iteration-245/250 closed-topology theorem at the explicit routed B3 level.

The single `Q0^2` branch is scaleless at the scalar-denominator level in massless dimensional regularization, but it must not yet be dropped: numerator powers, contact bookkeeping and regulator conventions must be checked in the reconstructed `B3(p)` before declaring that branch zero.

## Current blocker

The remaining C5 task is no longer topology discovery. It is numerator reconstruction and reduction:

`BLOCKED_4D_EINSTEIN_VD_CLOSED_P_DEPENDENT_NUMERATOR_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

A full blind C5 run is still unnecessary. The authorized next computation is to sample/reconstruct the exact closed `B3(p)` over the already-certified raised-bubble/triangle denominator families, determine its polynomial tensor degree, and then perform scoped tensor/master reduction.

## Readiness

`MODEL_READINESS: 24%`.

No rubric category closes yet because the physical C5 comparator coordinate has not been integrated/projected. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.
