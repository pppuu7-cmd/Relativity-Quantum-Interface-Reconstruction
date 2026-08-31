# Recovery Delta — Candidate Gravity Iteration 186

**Date:** 2026-08-31  
**Authoritative iteration:** **186**  
**MODEL_READINESS: 24%**

## What changed

Iteration 186 closes the previously BLOCKED full `QG-NL-EXP-001` lambda soft2 tangent on the six frozen null-soft TT rows and performs the exact hard-conditioned local-C5 quotient.

Fixed parent action:

`S ~ int sqrt(-g)[R + G_mn F(Box)R^mn]`,
`F(Box)=(exp(-lambda Box)-1)/Box`, `lambda=1`.

Thus `d_lambda F=-exp(-Box)`. Because every frozen external metric perturbation is TT, `R^(1)=0`; the cubic `-(1/2)R dF R` sector vanishes exactly in this protocol, including form-factor/Frechet insertions. The remaining Ricci-tensor sector was computed with the exact Iteration-185 multilinear covariant Box recursion through `n=14`.

## Frozen new vectors

Raw lambda soft2:

`S_NL=[4.015161989831051,0.18851421768711765,6.8958645469473,-2.160604075389611,-0.6546536226759653,-0.7636291997013364]`.

Frozen local exact-K2 compensation soft2 from Iteration 185:

`S_local=[0.6749106618554018,0.09041841732117784,1.6058813167372494,-0.8456710923733669,-0.0817908524675452,0.04041297883593838]`.

Conditioned nonlocal direction:

`S_cond=[4.690072651686453,0.27893263500829546,8.50174586368455,-3.006275167762978,-0.7364444751435104,-0.7232162208653979]`.

Projection on the frozen Iteration-178 exact zero-K2 local rank-4 span leaves

`r_NL=[0.026883997879370014,-0.16390037148459458,0.5945393887797525,-1.9589856765124543,1.8687871851331619,1.0763391630052563]`.

`||r_NL||_2=2.9781805828127865`.

Frozen envelope `5.2625580e-6`; margin `5.659188141608675e5`. The exponential series is converged: `max|N14-N13|=1.5099e-14`.

## Classification

- `NL-NG-005 — FULL_QG_NL_EXP_001_LAMBDA_SOFT2_TANGENT_IS_RESOLVABLE_AFTER_EXACT_K2_COMPENSATION`.
- `REL-NG-004 — K2_PRESERVING_NONLOCAL_DIRECTION_SURVIVES_THE_FROZEN_ZERO_K2_LOCAL_C5_RANK4_QUOTIENT`.
- `NG-FUNNEL-040 — A_RESOLVED_NONLOCAL_COMPARATOR_DIRECTION_IS_NUISANCE_AUTHORITY_NOT_CANDIDATE_NOVELTY`.

This is a **resolved independent comparator direction**. It is not Candidate Gravity novelty, not a consistency FAIL, not an exact identity, and not a near-degeneracy.

The fixed conditioned comparator authority for the present rows is now at least `span(V4,S_cond)`, of rank 5 unless later exact comparator relations enlarge/restructure the joint protocol.

## Still BLOCKED/open

- asymptotic-safety source-completed Lorentzian `(K2,S_soft2)` relation;
- C3 ordered metric-CTP/full soft2 completion;
- any Candidate Gravity target residual against the full fixed C3/C4/C5/nonlocal/AS quotient.

Do not zero-fill the unsupported AS or C3 directions.

## Promotion state

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Readiness accounting

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS: 24%`

Unchanged from Iteration 185: a major comparator blocker is closed, but full comparator foundation is not complete while AS real-time relation data and C3 ordered completion remain unresolved; no candidate residual exists.

## Authority files

- `analysis/nonlocal_lambda_soft2_quotient_iteration186.py`
- `results/nonlocal_lambda_soft2_quotient_iteration186.json`
- `candidate_gravity/NONLOCAL_LAMBDA_SOFT2_QUOTIENT_ITERATION186.md`
- `research_log/2026-08-31_iteration_186_nonlocal_lambda_soft2_quotient.md`
- `recovery/RECOVERY_DELTA_ITERATION_186.md`

## Exact next gate — Iteration 187

Freeze `span(V4,S_cond)` and perform the asymptotic-safety comparator audit in the same joint source-completed `(K2,S_soft2)` protocol. Promote a numerical AS column only if published/reconstructed dynamics uniquely determine the required Lorentzian off-shell/source-completed relation. Otherwise record `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, without zero-filling, and move to the C3 ordered-completion gate.
