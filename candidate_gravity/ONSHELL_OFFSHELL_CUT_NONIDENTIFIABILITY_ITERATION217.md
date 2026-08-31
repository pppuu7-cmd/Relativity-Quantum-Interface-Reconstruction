# Candidate Gravity — Iteration 217: on-shell cut does not determine off-shell `T_cut`

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Question

Can the now-robust physical on-shell pure-Einstein five-graviton cut from Iterations 215–216 be promoted, by itself, into the missing off-shell/source-completed C5 linked-cut comparator?

## Algebraic obstruction

Let `K2(p)` denote the inverse external-leg kernel and let `H(q^2,r^2)` contain a physical branch cut. Consider two cubic kernels

`Gamma_B = Gamma_A + K2(p) H(q^2,r^2)`.

On the `p`-leg mass shell, `K2(p)=0`, so their on-shell amplitudes and on-shell unitarity cuts agree exactly.

Off shell,

`D Gamma_B - D Gamma_A = K2(p) D H`,

which is generically nonzero.

Therefore the restriction from an off-shell cubic kernel to the on-shell S-matrix has a nontrivial kernel even in the nonanalytic sector. Exact knowledge of the physical on-shell cut cannot invert this restriction.

The repository numerical certificate uses `D H=1` and verifies exact zero difference at `K2=0` while the off-shell cut difference grows linearly with nonzero `K2`.

## Physical interpretation

This does **not** imply that the two off-shell kernels are physically distinct theories. EOM/inverse-kernel-proportional terms can be correlated with field redefinitions and source/contact terms. That is precisely why RQIR requires a fixed source-completed physical convention.

The result is instead a non-identifiability theorem for the attempted bridge:

> an on-shell graviton S-matrix positive control cannot, without additional physical source information, be used as a unique off-shell/source-response comparator column.

## Retained results

- `C5-CUT-017 — EXACT_ONSHELL_UNITARITY_CUT_DOES_NOT_UNIQUELY_DETERMINE_OFFSHELL_SOURCE_COMPLETED_T_CUT`;
- `REL-NG-019 — EOM_OR_INVERSE_KERNEL_PROPORTIONAL_NONANALYTIC_CUBIC_TERMS_LIE_IN_THE_ONSHELL_RESTRICTION_KERNEL_BUT_CAN_CHANGE_OFFSHELL_CUTS`;
- `NG-FUNNEL-074 — ONSHELL_POSITIVE_CONTROLS_MUST_NOT_BE_PROMOTED_TO_OFFSHELL_COMPARATOR_COLUMNS_WITHOUT_A_PHYSICAL_SOURCE_COMPLETION_MAP`.

## Consequence

The physical C5 five-graviton vector remains valuable and authoritative as an on-shell nonanalytic positive control, but it cannot close `BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION` by itself.

The next route should construct the discontinuity **directly at the level of a connected physical source/in-in observable**, where conserved-source Ward identities and source contacts are part of the definition, rather than infer it from a gauge-dependent off-shell 1PI kernel.

## Readiness

`MODEL_READINESS: 23%` — unchanged. No robust Candidate Gravity residual, no `ANSATZ-003`, no Fisher/resources.
