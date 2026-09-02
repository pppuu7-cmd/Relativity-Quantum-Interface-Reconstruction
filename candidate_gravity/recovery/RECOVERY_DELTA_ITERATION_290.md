# Recovery Delta — Iteration 290

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## New authoritative result

The current Iteration-289 triangle common-cut pole is

`A_B3 = -0.061289813814603585`.

A direct subtraction using the older MSSC-001 source-cut relation

`R_in = R_out = -8 M_Born`

is **forbidden** because the two residues belong to different observables/conventions. The current `B3` object is a scoped off-shell/1PI same-parent Vilkovisky contribution before source/Ward/contact completion, while the `-8 M_Born` relation is an on-shell connected scalar+graviton source-cut result in the stripped Iteration-219/221 normalization.

Iteration 218 fixes

`k_mu V^{mu nu} = (p'^2-m^2)p^nu - (p^2-m^2)p'^nu`,

so off-shell longitudinal completion is EOM/contact dependent and cannot be reconstructed from the on-shell Born residue alone. This preserves the Iteration-217 non-identifiability boundary.

Freeze:

`PASS_SOURCE_IR_INTERFACE_AUTHORITY_MAP__B3_POLE_ORIGIN_STILL_BLOCKED`.

## Three-way classification

- A: Ward/EOM/source-convention pole — must cancel/remove in linked/source completion.
- B: physical universal gravitational IR factor — need not vanish; remove only in the matched physical observable by the frozen Born/inclusive prescription.
- C: finite transverse hard remainder — only this may become a comparator coordinate.

The present data do not yet determine whether `A_B3` is A, B, or a mixture.

## Current blocker

`BLOCKED_POLE_LEVEL_LINKED_K2_SOURCE_WARD_CONTACT_COMPLETION_IN_SAME_CONVENTION`.

## Next gate

Construct the pole-level linked observable

`T_cut = D Gamma3_ret,soft - W[D K2]`

in one parameter/normalization convention. Derive the `1/epsilon` coefficient of `W[D K2]` and all source/contact pieces fixed by MSSC-001, then test cancellation/separation against `A_B3`. Only after the Ward/EOM component is removed may a surviving physical Born-factorizing IR term be handled by the already frozen hard-remainder prescription.

No Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Change from Iteration 289: **0 percentage points**. The observable-interface ambiguity is now frozen precisely, but no new readiness-rubric block is closed.