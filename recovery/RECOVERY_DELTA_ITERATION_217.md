# Recovery Delta — RQIR Iteration 217

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iterations 215–216 established a numerically robust physical on-shell pure-Einstein five-graviton nonanalytic control. The physical 12-point vector plus its pointwise error envelope is authoritative; fitted regular+log coefficients are compression only.

## New theorem-level blocker

The on-shell cut cannot uniquely determine the missing off-shell/source-completed linked cut.

Construct

`Gamma_B = Gamma_A + K2(p) H(q^2,r^2)`

with a nonanalytic `H` and normalized channel discontinuity `D H != 0`.

On shell, `K2(p)=0`, so

`D Gamma_B = D Gamma_A`

for the on-shell S-matrix restriction.

Off shell,

`D Gamma_B - D Gamma_A = K2(p) D H`,

which is generically nonzero.

Thus the on-shell restriction map has a nontrivial kernel even in the nonanalytic sector. The Iteration-215/216 physical C5 cut is a valid positive control but is not an invertible bridge to the source-completed `T_cut`.

This is non-identifiability, not a consistency failure. EOM/inverse-kernel-proportional terms may be correlated with field redefinitions/source contacts; that reinforces the need for a fixed physical source convention.

## Retained results

- `C5-CUT-017 — EXACT_ONSHELL_UNITARITY_CUT_DOES_NOT_UNIQUELY_DETERMINE_OFFSHELL_SOURCE_COMPLETED_T_CUT`;
- `REL-NG-019 — EOM_OR_INVERSE_KERNEL_PROPORTIONAL_NONANALYTIC_CUBIC_TERMS_LIE_IN_THE_ONSHELL_RESTRICTION_KERNEL_BUT_CAN_CHANGE_OFFSHELL_CUTS`;
- `NG-FUNNEL-074 — ONSHELL_POSITIVE_CONTROLS_MUST_NOT_BE_PROMOTED_TO_OFFSHELL_COMPARATOR_COLUMNS_WITHOUT_A_PHYSICAL_SOURCE_COMPLETION_MAP`.

## External comparator state

Fresh literature audit still leaves:

- AS: timelike scalar-graviton/scalar-scattering information exists, but not the required same-parent Lorentzian source-completed three-graviton cut;
- C3 PQCG: 2026 gravitational MSR/JD analysis is explicitly linearized around Minkowski and does not determine the nonlinear ordered cut.

Both remain BLOCKED, never zero-filled.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Exact restart instruction

Resume at **Iteration 218**.

Do not infer off-shell `T_cut` from the on-shell five-graviton cut. Instead freeze a gauge-safe **connected conserved-source/in-in cut observable** in the weak-field Minkowski source-completed convention. Required checks:

1. source conservation/gauge invariance at the external coupling level;
2. explicit statement of nonlinear source/contact completion;
3. two-point conditioning/amputation rule consistent with Iteration 171;
4. unitarity/cut representation using physical intermediate states if available;
5. identify the minimal concrete source model required to make the nonlinear observable executable.

No ANSATZ-003. No Fisher/resources.
