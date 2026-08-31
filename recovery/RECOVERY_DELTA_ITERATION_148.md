# Recovery Delta — RQIR Iteration 148

**Date:** 2026-08-31  
**Authoritative change:** added a source/observable-completion gate for off-shell C5 response before any numerical retarded rank is accepted.

## Previous front

Iteration 147 derived the correct tree-level retarded factorization but found the numerical finite `chi2R` projection under-specified.

## New result

A local field redefinition changes off-shell coordinate response functions while leaving the same physical observable invariant only when the induced observable/source contact terms are retained.

Deterministic regression:

- 12 finite off-shell points;
- `phi=psi+a psi^2`, `a=0.23`;
- maximum physical-response reconstruction error `1.1102230246251565e-16`;
- minimum coordinate-response shift `0.11688546786387487`.

Authorities:

- `analysis/c5_offshell_field_redefinition_iteration148.py`;
- `results/c5_offshell_field_redefinition_iteration148.json`;
- `candidate_gravity/C5_OFFSHELL_SOURCE_COMPLETION_ITERATION148.md`;
- `research_log/2026-08-31_iteration_148_c5_offshell_source_completion.md`.

## New retained blocker

### NG-FUNNEL-008 — ONSHELL_REDUCED_BASIS_NOT_OFFSHELL_RESPONSE_BASIS

The on-shell/EOM-reduced local C5 Wilson basis from Iteration 146 does not by itself define a basis-independent off-shell `chi^(2)R` tangent.

A valid comparator must freeze the operational metric/field variable, complete matter/source coupling, field-redefinition convention, induced source/contact operators, CTP state, renormalization/order, and finite projector/smearing protocol.

Therefore:

- Iteration-146 on-shell rank 10/10 remains valid;
- Iteration-147 retarded factorization remains valid;
- numerical `V_C5^(chi2R)` is `BLOCKED_SOURCE_COMPLETION`;
- this is not a C5 consistency FAIL;
- no Fisher/resources;
- no `ANSATZ-003`.

## Exact restart instruction

Resume at **Iteration 149 — source-completed C5 operational protocol**:

1. freeze the physical metric variable and conserved matter/source sector;
2. specify whether the Iteration-146 EOM-reduced basis is undone off shell or supplemented by all induced source/contact operators;
3. freeze finite sub-cutoff off-shell `(p,q,r)` with `p=q+r` away from poles;
4. freeze conserved projectors and finite smearing/window normalization;
5. define scalar `chi2R_even/odd` contractions;
6. evaluate EH + source-completed local-EFT cubic response;
7. perform field-redefinition covariance and Ward/gauge-null regressions;
8. only then compute `V_C5^(chi2R)` rank/SVD.
