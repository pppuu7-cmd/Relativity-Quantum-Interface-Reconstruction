# Recovery Delta — Iteration 543

Date: 2026-09-07

## Exact h4/h6 ratio conditioning contract
Authoritative start: Iteration 542. Canonical QUARTER rank4 run `34126397439`, job `101755969291`, remained `in_progress`; no duplicate heavy Action was launched.

For the frozen three-level diagnostic with `d1=BASE-HALF`, `d2=HALF-QUARTER`, `A=a h^4`, `B=b h^6`:

- `A=16(64d2-d1)/45`
- `B=256(d1-16d2)/189`
- `q=B/A=(80/21)(d1-16d2)/(64d2-d1)`
- for `r=d1/d2`, `q=(80/21)(r-16)/(64-r)`
- `dq/dr=1280/[7(64-r)^2]`
- `kappa_rel(r->q)=|48r/((r-16)(64-r))|`

Direct Jacobian:
- `dq/dd1=(1280/7)d2/(64d2-d1)^2`
- `dq/dd2=-(1280/7)d1/(64d2-d1)^2`

Exact zero surfaces:
- `d1=64d2 <=> A=0` (ratio pole)
- `d1=16d2 <=> B=0`.

Finite-error fail-closed guard: for `|e1|<=eps1`, `|e2|<=eps2`, set `D=64d2-d1`, `N=d1-16d2`, `m=|D|-(eps1+64eps2)`. If `m>0`, the denominator cannot cross the reconstructed `A=0` pole, and

`|q'-q| <= (80/21)*[((eps1+16eps2)|D| + |N|(eps1+64eps2))/(|D|m)]`.

Classification: `PASS_ITER424_H4_H6_RATIO_CONDITIONING_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is truncation/numerical diagnostic authority only; it does not promote physical index 2 and is not Candidate-Gravity consistency PASS/FAIL, comparator identity, regime-specific non-identifiability, model-level near-degeneracy, or novelty certificate.

No frozen Iteration-424 thresholds, parent dynamics, parameter convention, mass nodes, precision settings or Iteration-532 successor order changed.

Machine authority: `candidate_gravity/results/iteration543_iter424_h4_h6_ratio_conditioning_contract.json`.
Reproducible audit: `candidate_gravity/code/iteration543_iter424_h4_h6_ratio_conditioning_contract.py`.

Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Robust comparator-subtracted residual remains absent; `ANSATZ-003`, Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: 0 percentage points; a diagnostic conditioning subgate closed, but no stable rubric sector closed.

Exact next gate: after rank4 terminal completion, fail-closed raw-consume run `34126397439`. Only raw-valid PASS authorizes frozen rank5 `(-1.25e-6,+1.25e-6)`; scientific FAIL/BLOCKED stops advancement and operational failure permits only minimal rank4 repair.
