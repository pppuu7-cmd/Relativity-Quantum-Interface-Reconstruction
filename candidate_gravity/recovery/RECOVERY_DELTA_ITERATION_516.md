# Recovery Delta — Iteration 516

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact authority
Iteration 516 establishes `PASS_BASE_HALF_HETEROSCEDASTIC_DIAGONAL_COVARIANCE_EXACT__NON_PROMOTING` for the frozen 28-coordinate BASE/HALF central4 union.

For independent mean-zero coordinate errors with arbitrary per-coordinate variances `v_p>=0`, exact diagonal propagation gives

- `Var(BASE)=h^-4 sum_p w_B(p)^2 v_p`;
- `Var(HALF)=h^-4 sum_p w_H(p)^2 v_p`;
- `Var(BASE-HALF)=h^-4 sum_p (w_B(p)-w_H(p))^2 v_p`.

Only the four shared nodes `(-1,-1),(-1,+1),(+1,-1),(+1,+1)` contribute to BASE/HALF cross-covariance, and each has exact coefficient `w_B w_H=1/81`. Hence

`Cov(BASE,HALF)=h^-4 (1/81) sum_shared v_p >= 0`,

with equality iff all four shared-node variances vanish. Each shared-node discrepancy coefficient is `(w_B-w_H)^2=25/144`. Iteration 511 is recovered exactly when all `v_p=sigma^2`.

Reproducible audit: `candidate_gravity/code/iteration516_base_half_heteroscedastic_covariance_audit.py`. Result: `candidate_gravity/results/iteration516_base_half_heteroscedastic_covariance_exact.json`.

## Retained numerical state
Latest completed numerical mass-support authority remains Iteration 515 rank24, certified support `29/32 = 90.625% = 2320/2560`. Canonical rank25 `(u,v)=(+2.5e-6,+5e-6)`, run `34066294587`, job `101575523337`, remains in progress and was not duplicated.

## Retained blockers/nonclaims
Physical/operator authority remains Iteration 411. Physical blocker remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved set `[2]`. Fixed comparator quotient remains operationally BLOCKED until the concrete upstream `Source/Ward/contact+K2` target is assembled. No consistency FAIL, comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate is inferred. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

Readiness change: **0 percentage points**. The iteration strengthens numerical assembly/provenance but closes no additional readiness-rubric sector.

## Exact next gate
Fail-closed raw-consume rank25 after completion. Only raw-valid PASS permits rank26 `(+5e-6,-2.5e-6)`, HALF local index 13, multiplicity 1. BLOCKED freezes suffix progression and requires first-failing `z/phi/radial` localization under unchanged frozen conventions.
