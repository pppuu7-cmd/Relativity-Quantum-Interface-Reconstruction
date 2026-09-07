# Recovery Delta — Iteration 547

Date: 2026-09-07

## Exact P/Q innovation decorrelation contract
Authoritative start: Iteration 546. Canonical QUARTER rank5 run `34136802871`, job `101789577462`, remained `in_progress` in the scientific MP step. Raw authority audit and artifact upload had not started; no duplicate heavy Action was launched.

Retain the frozen three-level diagnostic `d1=BASE-HALF`, `d2=HALF-QUARTER`, `P=64d2-d1`, `Q=d1-16d2`. Iteration 546 gave

`Cov(P,Q)/sigma^2 = [[8322,-2130],[-2130,546]]`

for independent equal-variance BASE/HALF/QUARTER level errors.

Iteration 547 exact factorization:

- `det C = 6912 > 0`;
- innovation `R = Q + (355/1387) P`;
- `Cov(P,R)=0` exactly;
- `Var(R)/sigma^2 = 1152/1387 = 0.8305695746214852...`;
- `C^{-1} sigma^2 = [[91/1152,355/1152],[355/1152,1387/1152]]`;
- joint quadratic diagnostic `chi_PQ = (91 P^2 + 710 P Q + 1387 Q^2)/(1152 sigma^2)`.

Under `P=(45/16)A`, `Q=(189/256)B`,

`R = (15975/22192) A + (189/256) B`.

Thus R is a decorrelated numerical innovation but not a pure A/B component or a new physical observable. The exact joint form prevents future double-counting of the strongly anti-correlated P and Q directions.

Classification: `PASS_ITER424_PQ_INNOVATION_DECORRELATION_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Scope: equal-variance independent level-error model only; numerical/truncation diagnostic, not Candidate-Gravity near-degeneracy, identifiability, comparator identity, novelty, or consistency evidence. No frozen Iteration-424 threshold, dynamics, parameter convention, mass node, precision setting, or Iteration-532 successor order changed.

Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Robust comparator-subtracted residual is absent. `ANSATZ-003`, Fisher and resources remain blocked.

Machine authority: `candidate_gravity/results/iteration547_iter424_pq_innovation_decorrelation_contract.json`.
Reproducible audit: `candidate_gravity/code/iteration547_iter424_pq_innovation_decorrelation_contract.py`.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; a joint numerical-error subgate closed, but no stable readiness rubric sector closed.

Exact next gate: after rank5 terminal completion, fail-closed raw-consume run `34136802871`. Only raw-valid PASS authorizes frozen rank6 `(-1.25e-6,+2.5e-6)`; scientific FAIL/BLOCKED stops advancement and operational failure permits only minimal rank5 repair.
