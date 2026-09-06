# Recovery Delta — Iteration 511

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact assembly error-propagation authority
Classification: `PASS_BASE_HALF_SHARED_NODE_COVARIANCE_EXACT__NON_PROMOTING`.

Using the exact Iteration-510 Gram matrix for the frozen 28-coordinate BASE/HALF union, and only under the explicitly scoped diagnostic model of iid equal-variance coordinate-level sampling error `sigma^2`, the assembled error covariance is exactly `sigma^2 G/h^4` with

`G = [[4225/5184, 4/81], [4/81, 4225/324]]`.

Hence `Cov(BASE,HALF)=(4/81)sigma^2/h^4`, the exact correlation is `64/4225`, and for `DELTA=BASE-HALF`, `Var(DELTA)=(23771/1728)sigma^2/h^4`.

Operational guardrail: the four shared BASE/HALF sample coordinates induce exactly nonzero numerical-error covariance. Future error propagation must not treat BASE and HALF sample errors as strictly independent or count `BASE-HALF` as independent information. This does not alter any frozen threshold or physical-observable covariance claim.

Reproducible audit: `candidate_gravity/code/iteration511_base_half_shared_node_covariance_exact_audit.py`. Result: `candidate_gravity/results/iteration511_base_half_shared_node_covariance_exact_audit.json`.

## Active heavy gate
Iteration 509 remains the latest completed numerical mass-support authority: rank22 raw-consumed PASS, certified support `27/32 = 84.375% = 2160/2560`. Canonical rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, run `34058694183`, job `101555199703`, remains the sole authorized heavy gate and must not be duplicated.

## Nonclaims
This exact result is assembly numerical-error/provenance authority only. It is not Candidate-Gravity consistency PASS/FAIL, physical promotion, comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate, or Fisher authority. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden before a nonzero algebraic residual.

Readiness change: **0 percentage points**. The error-propagation contract is strengthened, but no additional stable-rubric model component is complete.

## Exact next gate
Fail-closed raw-consume rank23 run `34058694183` after completion. Only raw-valid PASS permits rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10; BLOCKED freezes suffix progression and requires first-failing-sample localization under unchanged frozen conventions.
