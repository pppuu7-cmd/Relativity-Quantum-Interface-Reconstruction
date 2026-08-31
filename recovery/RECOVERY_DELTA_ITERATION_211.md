# Recovery Delta — RQIR Iteration 211

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 210 validated the 12-point one-loop regular+log soft extractor but had not imported a physical loop comparator.

## New authoritative result

The Iteration-208 pure-Einstein one-loop four-graviton amplitude cannot serve as the generic finite-single-soft input to that extractor. For real massless four-point on-shell kinematics, taking one external leg independently soft degenerates the remaining three-point hard configuration. The four-point result remains a hard nonanalytic C5 positive control only.

A generic independent one-soft on-shell control requires at least five external legs (or a source-completed off-shell equivalent).

Classic multi-leg one-loop authority separates two relevant sequences: nonsupersymmetric/all-plus gravity amplitudes, which are rational, and cut-containing MHV amplitudes in N=8 supergravity. The former are not branch-cut/log positive controls and the latter are not the pure-Einstein C5 comparator.

A directly reusable integrated cut-containing pure-Einstein one-loop five-graviton MHV hard function was not found in the audited authority. However the five-point discontinuity does not require the full integrated amplitude: it can be constructed directly through a physical two-particle unitarity cut from pure-Einstein tree amplitudes.

## Classification

- 4-point hard anchor -> finite-soft extractor: `BLOCKED_BY_ONSHELL_SOFT_KINEMATICS`;
- compact integrated pure-Einstein 5-point cut-containing hard function: `OPERATIONAL_BLOCKED_NOT_REQUIRED_FOR_CUT`;
- direct 5-point tree-unitarity discontinuity: `AUTHORIZED_NEXT_ROUTE`.

## Retained results

- `KIN-NG-001 — MASSLESS_ONSHELL_FOUR_POINT_ANCHOR_HAS_NO_GENERIC_INDEPENDENT_SINGLE_SOFT_HARD_CONFIGURATION`;
- `C5-CUT-008 — FIRST_PHYSICAL_REGULAR_LOG_SOFT_CUT_CONTROL_REQUIRES_AT_LEAST_FIVE_EXTERNAL_LEGS_OR_A_SOURCE_COMPLETED_EQUIVALENT`;
- `C5-CUT-009 — PURE_EINSTEIN_FIVE_POINT_DISCONTINUITY_CAN_BE_BUILT_DIRECTLY_FROM_TREE_UNITARITY_WITHOUT_A_CLOSED_INTEGRATED_ONE_LOOP_AMPLITUDE`;
- `NG-FUNNEL-068 — DO_NOT_FORCE_A_HARD_FOUR_POINT_POSITIVE_CONTROL_INTO_A_DEGENERATE_SOFT_KINEMATIC_ROLE`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Exact restart instruction

Resume at **Iteration 212 — pure-Einstein five-point tree/KLT engine**.

Implement the field-theory five-point KLT relation using Parke–Taylor MHV Yang–Mills amplitudes. Build a deterministic complex momentum-conserving family with one uniformly soft positive-helicity graviton. Verify momentum conservation, multiple permutation relabelings, `|M5| ~ epsilon^-1`, and convergence to the Weinberg leading soft factor times `M4` up to one frozen overall KLT/sign convention.

Store code/results before using the engine in any loop phase-space integral. No `ANSATZ-003`, Fisher or resources.
