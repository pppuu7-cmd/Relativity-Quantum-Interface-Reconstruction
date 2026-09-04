# Candidate Gravity Research Log — Iteration 444

**Date:** 2026-09-05  
**Scope:** post-parent contraction precision boundary after Iteration 443  
**Classification:** `PASS_ITER444_LAYER368_POSTPARENT_CONTRACTION_BOUNDARY_CONTRACT__NON_PROMOTING`

## Starting authority

Repository source of truth was read before this iteration: `CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_443.md`, `RESEARCH_LOG_ITERATION_443.md`, recent commits, recent Actions, and `ITERATION_ID_REGISTRY.md`.

Physical/operator authority remains Iteration 411. Iteration 421 remains the latest raw-valid physical blocker for double-double index 2 / class 3 / `q^2=-1`. Exact unresolved physical set remains `[2]`.

A recent workflow-local `431` completed successfully, but authoritative ID 431 is already reserved by the registry for a different scientific object. It is therefore treated only as a workflow-local duplicate identifier until separately raw-consumed under a future unique authoritative number; no authority was overwritten.

## New result

Iteration 443 already established that the outward 368/370 layer has two unclosed precision boundaries: the separately formed Y-site derivative `y1` at fixed `h=4e-5`, followed by retained-binary64 matrix products and trace contractions.

This iteration audits the exact post-parent contraction graph in the frozen Iteration-368 implementation and freezes its precision contract prospectively.

Every first-order or second-order U1 block is assembled by three matrix multiplications. A traced two-block amplitude then applies one additional block product before `np.trace`. Therefore each traced amplitude contains exactly

- 7 matrix multiplications;
- 1 trace operation;

outside the already separately certified parent objects.

Source guards verify one occurrence each of the frozen chains for `first_u1`, `V2`, `N_L`, `N_R`, `Y`, and the three orientation/cyclic trace forms. No routing, numerator, sign, normalization, step size, or downstream threshold changed.

## Prospectively frozen contraction subgate

This subgate is authorized only after the Iteration-443 Y-site `y1` gate passes.

For every representative 368/370 contraction used by the frozen routing/transport probe set:

1. reuse identical parent matrix values and identical routed momenta/orientations;
2. perform the entire 7-matmul + trace contraction continuously at 80 and 120 decimal digits;
3. require finite outputs;
4. require full representative contraction coverage;
5. require max scaled 80-vs-120 discrepancy `<=1e-30`.

`binary64` versus 120-digit discrepancy is diagnostic only and is not an acceptance gate.

Forbidden: threshold weakening, routing/numerator changes, cyclic/orientation quotient before the already frozen routed-translation equality, or wrapping only the outer scalar/trace in arbitrary precision while any matrix multiplication remains binary64.

## Scientific classification

This is a numerical-method/provenance contract, not a new physical `D_s`, not a consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

Iteration 412 exact15 remains blocked. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No literature update is materially required because no comparator, novelty, or consistency claim changed.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Readiness change from Iteration 443: **0 percentage points**. The post-parent precision graph and acceptance contract are now frozen, but no new physical coordinate or stable model-readiness rubric component has closed.

## Exact next gate

Execute the already frozen Iteration-443 Y-site `y1` 80/120-digit plus same-h fourth-order oracle test at unchanged `h=4e-5`. If and only if it passes, execute the Iteration-444 continuous 80/120-digit post-parent 7-matmul + trace contraction certificate before advancing to `379/374 -> 407 -> 424`.
