# Recovery Delta — Iteration 518

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact authority
Generalized BASE/HALF numerical-error propagation from diagonal independent coordinate errors to an arbitrary PSD covariance `Sigma` on the frozen 28-coordinate support union.

Classification: `PASS_BASE_HALF_FULL_PSD_COVARIANCE_SPECTRAL_CONTRACT_EXACT__NON_PROMOTING`.

Exact formulas: `C_A=h^-4 A Sigma A^T`, `A=[w_BASE^T;w_HALF^T]`; `Var(BASE-HALF)=h^-4(w_BASE-w_HALF)^T Sigma (w_BASE-w_HALF)`. Since `Sigma>=0`, assembled covariance is PSD.

With `lambda=lambda_max(Sigma)`, exact norm-level bounds are `Var(BASE)<=(4225/5184)lambda/h^4`, `Var(HALF)<=(4225/324)lambda/h^4`, `Var(BASE-HALF)<=(23771/1728)lambda/h^4`, and `|Cov(BASE,HALF)|<=(4225/1296)lambda/h^4`.

Guardrail: for arbitrary correlated PSD coordinate noise, `Cov(BASE,HALF)` may have either sign. Iteration 516 nonnegative covariance remains valid only for diagonal/independent errors. This is numerical assembly/error-provenance authority only and gives no physical covariance, consistency verdict, comparator identity, non-identifiability, near-degeneracy, novelty certificate, or Fisher authorization.

Reproducible audit: `candidate_gravity/code/iteration518_full_psd_covariance_contract.py`; result: `candidate_gravity/results/iteration518_full_psd_covariance_contract.json`.

## Active heavy gate
Canonical rank26 `(+5e-6,-2.5e-6)`, HALF local index 13, run `34071968236`, job `101590847259`, remained in progress during this iteration. No duplicate was launched. Certified local precision support remains `30/32 = 93.750%` until raw consumption.

## Retained blockers/nonclaims
Physical/operator authority remains Iteration 411. Physical blocker remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved set `[2]`. Robust comparator-subtracted residual is absent; `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

Readiness change: **0 percentage points** because no additional stable readiness-rubric sector closed.

## Exact next gate
Fail-closed raw-consume rank26 after completion. Only raw-valid PASS permits frozen rank27 `(+5e-6,+2.5e-6)`, HALF local index 14. BLOCKED freezes suffix progression and requires first-failing `z/phi/radial` localization without changing frozen conventions.
