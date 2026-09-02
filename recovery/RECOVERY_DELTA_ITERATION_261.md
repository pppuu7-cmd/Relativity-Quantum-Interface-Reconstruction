# RECOVERY DELTA — Candidate Gravity Iteration 261

**Date:** 2026-09-02  
**Authoritative iteration:** 261  
**MODEL_READINESS: 24%**

## Delta from Iteration 260

Iteration 260 proved exact coefficientwise weighted symmetry for complete same-parent `B=U1 W=Q A Q`. Iteration 261 audits the physical three-leg interpretation of the cubic coefficient before component tensor work.

The one-parameter formula

`B3 = Q0 A3 Q0 + Q1 A2 Q0 + Q0 A2 Q1 + Q2 A1 Q0 + Q0 A1 Q2 + Q1 A1 Q1`

is retained as **degree-family bookkeeping**, but it is not yet the distinguishable-leg physical numerator.

For external legs `(s,a,b)`, with multilinear coefficients `Q1[x]`, symmetric `Q2[x,y]`, `A1[x]`, symmetric `A2[x,y]`, and complete symmetric `A3[x,y,z]`, polarization expands the six families into **19 explicit leg-resolved terms**.

Iteration 246 gives `E1[s]=0` on the frozen physical null-TT soft branch. Since `A=K E` and `E0=0`, `A1[s]=0`. Exactly four polarized terms vanish:

- `Q2[a,b] A1[s] Q0`;
- `Q0 A1[s] Q2[a,b]`;
- `Q1[a] A1[s] Q1[b]`;
- `Q1[b] A1[s] Q1[a]`.

Therefore **15 terms survive**.

Do not drop soft-background dressing terms `Q1[s] A2[a,b]`, `A2[s,a]`, `A2[s,b]`, `A3[s,a,b]`, or `Q1[s] A1[a] Q1[b]`; the null-soft theorem does not zero-fill the `e=1/e=2` connection sectors.

Freeze:

`PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION`

and

`NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR`.

Retain exact weighted Ward identity from Iteration 260. A mixed-derivative transpose mismatch is an implementation/index/convention regression, not a new physical consistency FAIL.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This result is not a consistency FAIL, exact Candidate-vs-GR comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 260: **0 percentage points**. Correct physical polarization closes a bookkeeping ambiguity but does not produce the physical C5 comparator coordinate or a robust nonzero algebraic residual. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct polarized same-parent `A1[x]`, `A2[x,y]`, complete `A3[s,a,b]`, and polarized `Q1[x]`, `Q2[x,y]` from the frozen orbit metric. Assemble the 15 surviving null-soft terms of `B3[s,a,b]`. Tensor reduction is allowed only after a nonzero physical numerator exists. Fisher/resources, blind heavy full-C5 integration and `ANSATZ-003` remain forbidden.
