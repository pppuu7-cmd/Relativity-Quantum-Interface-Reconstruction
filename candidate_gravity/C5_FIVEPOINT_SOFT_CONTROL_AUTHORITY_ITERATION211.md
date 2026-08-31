# RQIR Candidate Gravity — Iteration 211

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Attempt the first import of a physical standard-QG nonanalytic object into the Iteration-210 finite-soft regular+log extractor.

## Four-point kinematic obstruction

The Iteration-208 pure-Einstein one-loop four-graviton amplitude is an excellent **hard** nonanalytic positive control. It is not a generic independent soft-probe amplitude.

For real massless on-shell four-point kinematics, imposing momentum conservation while taking one external momentum independently soft collapses the remaining three hard massless momenta into a degenerate three-point configuration. Therefore a generic finite-soft family with one soft graviton and a nondegenerate hard scattering process requires at least five external legs (or a source-completed off-shell equivalent).

Hence the four-point anchor must not be forced into the Iteration-210 soft extractor.

## Multi-leg literature audit

Bern, Dixon, Perelstein and Rozowsky (`hep-th/9811140`) give two important multi-leg one-loop sequences:

- all-plus amplitudes in nonsupersymmetric gravity with arbitrary minimally coupled massless matter content;
- MHV amplitudes in `N=8` supergravity.

The pure-Einstein/all-plus amplitudes are rational functions (see also `hep-th/9809160`). They have valuable soft/collinear information but do not provide the branch-cut/log positive control required by the current `T_cut` program.

The cut-containing MHV sequence in that classic multi-leg construction is `N=8` supergravity, not pure Einstein gravity. It cannot be substituted for the frozen C5 comparator.

A directly reusable integrated pure-Einstein one-loop five-graviton cut-containing MHV hard function was not found in the audited authority. This is an operational availability statement, not a proof of nonexistence in the literature.

## Direct unitarity route

A closed integrated one-loop amplitude is not required to obtain the discontinuity itself.

For a physical two-particle channel of the one-loop five-graviton amplitude,

\[
\operatorname{Disc}\mathcal M_5^{(1)}
\sim
\sum_{h_1,h_2}
\int d\Phi_2\,
\mathcal M^{\rm tree}_{L}(\ldots,\ell_1^{h_1},\ell_2^{h_2})
\mathcal M^{\rm tree}_{R}(\ldots,-\ell_1^{-h_1},-\ell_2^{-h_2}),
\]

with the exact normalization, crossing convention and infrared prescription to be frozen before executable use.

The required pure-Einstein tree amplitudes are physical and can be constructed through KLT/BCFW/BGK methods. This route keeps the discontinuity gauge invariant on shell and avoids waiting for a compact integrated five-point loop formula.

## Classification

- four-point anchor as finite-soft control: `BLOCKED_BY_ONSHELL_SOFT_KINEMATICS`;
- integrated pure-Einstein five-point hard function: `OPERATIONAL_BLOCKED_NOT_REQUIRED_FOR_CUT`;
- direct five-point unitarity construction: `AUTHORIZED_NEXT_ROUTE`.

Retain:

- `KIN-NG-001 — MASSLESS_ONSHELL_FOUR_POINT_ANCHOR_HAS_NO_GENERIC_INDEPENDENT_SINGLE_SOFT_HARD_CONFIGURATION`;
- `C5-CUT-008 — FIRST_PHYSICAL_REGULAR_LOG_SOFT_CUT_CONTROL_REQUIRES_AT_LEAST_FIVE_EXTERNAL_LEGS_OR_A_SOURCE_COMPLETED_EQUIVALENT`;
- `C5-CUT-009 — PURE_EINSTEIN_FIVE_POINT_DISCONTINUITY_CAN_BE_BUILT_DIRECTLY_FROM_TREE_UNITARITY_WITHOUT_A_CLOSED_INTEGRATED_ONE_LOOP_AMPLITUDE`;
- `NG-FUNNEL-068 — DO_NOT_FORCE_A_HARD_FOUR_POINT_POSITIVE_CONTROL_INTO_A_DEGENERATE_SOFT_KINEMATIC_ROLE`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

The route is corrected but no physical five-point cut has yet been evaluated.

## Next gate

Implement a deterministic pure-Einstein five-graviton tree engine. Use a five-point KLT representation built from color-ordered Yang–Mills MHV amplitudes. Construct an exactly momentum-conserving one-soft family and require:

1. machine-precision momentum conservation;
2. gravity permutation symmetry under multiple relabelings;
3. leading energy-soft scaling `|M5| ~ epsilon^-1`;
4. agreement with the leading positive-helicity Weinberg soft factor times the four-graviton tree amplitude up to the fixed overall KLT/sign convention.

Only after those pass should the tree engine enter a one-loop cut integral.
