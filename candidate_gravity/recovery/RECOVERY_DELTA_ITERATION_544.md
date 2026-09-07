# Recovery Delta — Iteration 544

Date: 2026-09-07

## Exact ratio-free h4/h6 cone contract
Authoritative start: Iteration 543. Canonical QUARTER rank4 run `34126397439`, job `101755969291`, remained `in_progress`; no duplicate heavy Action was launched.

For the frozen three-level diagnostic define `d1=BASE-HALF`, `d2=HALF-QUARTER`, `A=a h^4`, `B=b h^6`. Then

- `d1=(15/16)A+(63/64)B`
- `d2=(15/256)A+(63/4096)B`
- `Q:=d1-16d2=(189/256)B`
- `P:=64d2-d1=(45/16)A`
- therefore `A=(16/45)P`, `B=(256/189)Q` exactly.

This yields a ratio-free sign/cancellation diagnostic. Exact same-sign nonzero `A,B` gives `P*Q>0`; exact opposite-sign gives `P*Q<0`; `Q=0 <=> B=0`; `P=0 <=> A=0`.

For `|e1|<=eps1`, `|e2|<=eps2`:
- `rho_P=eps1+64eps2`
- `rho_Q=eps1+16eps2`.

Fail-closed classification:
- same-sign PASS only if both `P` and `Q` uncertainty intervals exclude zero and have the same sign;
- opposite-sign cancellation result only if both intervals exclude zero and have opposite signs;
- otherwise `BLOCKED/AMBIGUOUS_DIAGNOSTIC`, with no sign inference.

Classification: `PASS_ITER424_RATIO_FREE_H4_H6_CONE_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is truncation/numerical diagnostic authority only; it does not promote physical index 2 and is not Candidate-Gravity consistency PASS/FAIL, comparator identity, regime-specific non-identifiability, model-level near-degeneracy, or novelty certificate.

No frozen Iteration-424 threshold, parent dynamics, parameter convention, mass node, precision setting, or Iteration-532 successor order changed.

Machine authority: `candidate_gravity/results/iteration544_iter424_ratio_free_h4_h6_cone_contract.json`.
Reproducible audit: `candidate_gravity/code/iteration544_iter424_ratio_free_h4_h6_cone_contract.py`.

Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Robust comparator-subtracted residual remains absent; `ANSATZ-003`, Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; a robust diagnostic subgate closed, but no stable rubric sector closed.

Exact next gate: after rank4 terminal completion, fail-closed raw-consume run `34126397439`. Only raw-valid PASS authorizes frozen rank5 `(-1.25e-6,+1.25e-6)`; scientific FAIL/BLOCKED stops advancement and operational failure permits only minimal rank4 repair.
