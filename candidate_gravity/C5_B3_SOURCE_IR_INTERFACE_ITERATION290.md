# C5 B3 / Source IR Interface — Iteration 290

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Question

Can the robust common-cut pole measured in the current scoped same-parent Vilkovisky `B3` block,

`A_B3 = -0.061289813814603585`,

be cancelled or classified directly using the already frozen MSSC-001 source-cut relation

`R_in = R_out = -8 M_Born`?

## Answer

No direct subtraction is authorized.

The two residues currently belong to different objects and conventions:

1. the Iteration-289 pole is extracted from a scoped off-shell/1PI same-parent Vilkovisky orbit-trace contribution before source/Ward/contact completion;
2. the Iteration-222 relation is an on-shell connected scalar+graviton source-cut factorization in the stripped Iteration-219/221 normalization.

Iteration 218 fixes the off-shell source Ward identity

`k_mu V^{mu nu} = (p'^2-m^2) p^nu - (p^2-m^2) p'^nu`.

Therefore the longitudinal/off-shell completion is tied to inverse scalar propagators and contact terms from the same covariant source action. On shell these EOM terms vanish, so the on-shell Born-factorizing residue cannot determine their coefficient in the off-shell/1PI `B3` convention. This is the precise interface obstruction already compatible with the Iteration-217 non-identifiability result.

## Three-way IR classification

The current pole must be separated into three logically distinct classes before any finite C5 coordinate is promoted:

- **A — Ward/EOM/source-convention pole.** Must cancel or be removed by the linked/source completion in the same convention.
- **B — physical universal gravitational IR factor.** Need not cancel; it must be removed only through the already frozen Born/inclusive hard-remainder prescription in the corresponding physical connected observable.
- **C — finite transverse hard remainder.** Only this level is eligible for comparator-coordinate promotion.

The present data do not identify whether the measured `B3` pole is A, B, or a mixture. Calling it a physical IR divergence, a Ward failure, or a cancellable contact pole would overclaim.

## Frozen result

`PASS_SOURCE_IR_INTERFACE_AUTHORITY_MAP__B3_POLE_ORIGIN_STILL_BLOCKED`

Guardrails:

- `DO_NOT_SUBTRACT_MINUS_8_M_BORN_FROM_THE_CURRENT_B3_RESIDUE_WITHOUT_AN_EXPLICIT_OBSERVABLE_MAP`;
- `DO_NOT_REQUIRE_THE_FULL_SOURCE_COMPLETED_GRAVITATIONAL_IR_POLE_TO_VANISH_IF_IT_IS_A_PHYSICAL_BORN_FACTORIZING_IR_FACTOR`;
- `DO_NOT_PROMOTE_ANY_FINITE_REMAINDER_BEFORE_WARD_EOM_AND_PHYSICAL_IR_FACTORS_ARE_SEPARATED_IN_ONE_SOURCE_CONVENTION`.

## Scientific classification

This is an **operational/interface BLOCKED result**, not a consistency FAIL, not an exact comparator identity, not near-degeneracy, and not a novelty certificate. It also preserves the earlier regime-specific non-identifiability: on-shell source-cut data alone do not invert uniquely to the current off-shell/1PI pole coefficient.

## Exact next gate

Construct the pole-level linked observable in one convention,

`T_cut = D Gamma3_ret,soft - W[D K2]`,

and derive the `1/epsilon` coefficient of the linked `W[D K2]` plus required source/contact terms before computing any additional finite master pieces. The first executable test is whether the sum removes the Ward/EOM part of `A_B3`; only after that may any surviving Born-factorizing physical IR factor be subtracted by the frozen source prescription.

`ANSATZ-003` remains forbidden. Fisher/resources remain forbidden.