# RQIR Research Log — Iteration 148

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / fixed C5 off-shell comparator  
**Promotion decision:** no `ANSATZ-003` frozen

## Starting authority

Iteration 147 fixed the tree-level retarded C5 factorization but left the first numerical `V_C5^(chi2R)` blocked by an under-specified off-shell projector/smearing protocol.

## New audit question

Before computing that rank, test whether the Iteration-146 on-shell/EOM-reduced EFT Wilson basis can be used unchanged as an off-shell response basis.

## Literature check

Recent work on generic field redefinitions and a 2026 gravity-specific off-shell equivalence analysis both emphasize that off-shell objects transform nontrivially. Physical equivalence requires transformed observables/probes, not numerical equality of coordinate Green functions. This is materially relevant because gravity EFT operator bases are routinely reduced by equations of motion and local metric redefinitions.

## Reproducible result

The scalar nonlinear-response regression in `analysis/c5_offshell_field_redefinition_iteration148.py` provides an exact finite illustration.

For

`K phi + g/2 phi^2 + J = 0`,

`chi_phi=-g Gp Gq Gr`.

Under `phi=psi+a psi^2`, the coordinate response shifts by `-2 a Gq Gr`, but reconstruction of the same physical observable adds `+2 a Gq Gr` and restores the original response.

Twelve deterministic off-shell points yield maximum reconstruction error `1.1102230246251565e-16` while every coordinate response changes, with minimum absolute shift `0.11688546786387487`.

## New retained blocker

**NG-FUNNEL-008 — ONSHELL_REDUCED_BASIS_NOT_OFFSHELL_RESPONSE_BASIS.**

The Iteration-146 local amplitude basis remains a valid on-shell comparator, but cannot define a basis-independent off-shell retarded `chi2R` tangent without the induced matter/source/contact completion associated with its field-redefinition/EOM reduction.

Classification: **operational/comparator-instantiation BLOCKED**, not consistency FAIL and not C5 falsification.

## Consequences

- Iteration-146 rank 10/10 remains PASS_SCOPED in amplitude space.
- Iteration-147 retarded factorization remains PASS_SCOPED.
- numerical local C5 `V_C5^(chi2R)` becomes `BLOCKED_SOURCE_COMPLETION`.
- `N2`, `C3sym`, loop/nonanalytic C5 rows remain BLOCKED.
- Fisher/resources remain forbidden.
- `ANSATZ-003` remains withheld.

## Next gate

Iteration 149: freeze a source-completed operational metric convention, including the matter/source map and all contact terms induced by any EOM/field-redefinition reduction, then freeze finite off-shell conserved probes/smearing and only then compute the first basis-stable Ward/rank certificate.
