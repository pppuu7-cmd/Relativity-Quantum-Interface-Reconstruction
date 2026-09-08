# Recovery Delta — Iteration 570

## New exact diagnostic authority
Frozen QUARTER central4 mixed-stencil correlated-error propagation has been closed exactly for separable coordinate-error covariance.

With `w=(1,-8,8,-1)`, `C=w⊗w`, normalization `1/(144 h^2)`, and

`Cov(vec E)=Sigma_v ⊗ Sigma_u`, 

we have

`Var(D_uv)=(w^T Sigma_u w)(w^T Sigma_v w)/(144^2 h^4)`.

For symmetric `Sigma`,

`w^T Sigma w = S00 -16 S01 +16 S02 -2 S03 +64 S11 -128 S12 +16 S13 +64 S22 -16 S23 + S33`.

Since `sum(w)=0`, a perfectly common covariance mode `J` is nulled exactly: `w^T J w=0`.

Classification: `PASS_ITER424_QUARTER_SEPARABLE_CORRELATED_COVARIANCE_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Reproducible audit: `candidate_gravity/code/post569_iter424_quarter_correlated_covariance_contract.py`.  
Machine-readable result: `candidate_gravity/results/iteration570_iter424_quarter_separable_correlated_covariance_contract.json`.

## Heavy state
Rank12 `(+2.5e-6,+1.25e-6)` canonical run `34175330006`, job `101903475600`, remained in progress during this iteration. No duplicate was launched. Workflow status alone is not scientific authority.

## Physical state and guardrails
Physical/operator authority remains Iteration411. Physical blocker remains Iteration421 `BLOCKED_CONVERGENCE`, unresolved set `[2]`, class3, `q^2=-1`. Concrete `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent, so the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains operational BLOCKED. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

`MODEL_READINESS: 24%`

Change from Iteration569: **0 percentage points**. The correlated-error assembly contract closes a real diagnostic subgate but no new stable model-level rubric sector.

## Exact next gate
Inspect terminal state and raw artifact of rank12 run `34175330006`, job `101903475600`. Only fail-closed raw-valid PASS authorizes complete QUARTER assembly and the unchanged Iteration-424 five-clause physical reevaluation.
