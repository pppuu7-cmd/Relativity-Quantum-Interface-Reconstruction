# Recovery Delta — RQIR Iteration 147

**Date:** 2026-08-31  
**Authoritative change:** first C5 tree-level retarded nonlinear-response formula fixed in one CTP convention; numerical finite `chi2R` embedding found to be underdetermined by the Iteration-146 on-shell protocol.

## Previous front

Iteration 146 froze the local tree-level four-graviton EFT comparator and produced a 12x10 rank-10/10 on-shell Wilson tangent. Full RQIR C5 embedding remained blocked because the amplitude is not the ordered retarded response.

## New authorities

- `analysis/c5_retarded_embedding_iteration147.py`;
- `results/c5_retarded_embedding_iteration147.json`;
- `candidate_gravity/C5_RETARDED_EMBEDDING_ITERATION147.md`;
- `research_log/2026-08-31_iteration_147_c5_retarded_embedding.md`;
- `recovery/RECOVERY_DELTA_ITERATION_147.md`.

## Frozen CTP convention

D=4 Minkowski, interacting in-vacuum, de Donder perturbative gauge, conserved physical source projections, linear `J_A h^A` coupling, and the same EH + parity-even local-EFT dynamics/order as Iteration 146.

## Derived response object

For `K h + 1/2 V[h,h] + J=0`,

`h^(1)=-G_R J`,

and

`chi2R_A;BC(p;q,r)=-(2pi)^4 delta4(p-q-r) G_R,AA'(p) Gamma3^A'_{B'C'}(p,-q,-r) G_R^B'_B(q) G_R^C'_C(r)`.

This is the required tree-level C5 nonlinear retarded response before finite RQIR projection.

## New retained blocker

### NG-FUNNEL-007 — ON_SHELL_4PT_KINEMATICS_DO_NOT_FIX_OFF_SHELL_RETARDED_3PT

The Iteration-146 `(s,t,u,phi)` four-point on-shell samples do not uniquely define the off-shell three-point retarded protocol. Missing data include:

- `p^2,q^2,r^2` and energy routing;
- one output and two input conserved tensor projectors;
- finite time/spatial smearing and normalization;
- explicit scalar `chi2R_even/odd` coordinate definitions;
- numerical Ward/gauge-artifact null test.

Therefore:

- `chi2R_even/odd`: `BLOCKED_PROTOCOL_UNDERSPECIFIED`;
- local-EFT retarded rank: `NOT_COMPUTABLE` yet;
- Iteration-146 rank-10/10 is retained only in on-shell amplitude space;
- no Fisher/resource calculation is allowed;
- no `ANSATZ-003` is frozen.

This is an operational comparator-instantiation blocker, not a consistency FAIL of C5.

## Other rows

`N2`, `C3sym`, and loop/nonanalytic columns remain BLOCKED pending same-convention CTP derivations.

## Exact restart instruction

Resume at **Iteration 148 — finite off-shell C5 response protocol**:

1. freeze sub-cutoff off-shell `(p,q,r)` points with `p=q+r` away from poles;
2. freeze explicit conserved tensor/source projectors plus finite smearing/window normalization;
3. define concrete `chi2R_even/odd` contractions;
4. evaluate EH and all contributing local-EFT cubic vertices;
5. perform Ward/gauge-null regression;
6. compute the first real `V_C5^(chi2R)` rank/SVD certificate;
7. leave loop/nonanalytic rows BLOCKED unless actually derived.
