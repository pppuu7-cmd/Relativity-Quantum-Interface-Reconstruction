# RQIR Candidate Gravity Recovery Delta — Iteration 367

Date: 2026-09-04

MODEL_READINESS: 24%

## Start-of-run source-of-truth audit

Validated scientific authority remains Iteration 366. `CURRENT_QG_FRONT.md` still listed Iteration 364 as active, but fresh Actions state supersedes that operational line.

Iteration 364 run `33801351823`, job `100801347762`, is `completed/cancelled`. The scientific step was cancelled after about 40 minutes; sentinel/schema audit and artifact upload were skipped. Artifact count is `0`. Therefore Iteration 364 has no scientific PASS/FAIL authority and must not be used to close or zero-fill the 48 cut-through-double-pole channels. A blind full-run duplicate is not authorized.

## Anti-idle action

Fresh commit `582f7f6619f3a04e8af27c1eb2b0203673514ab7` added `candidate_gravity/code/iteration367_tru1sq_timelike_singleton_pruning_reaudit.py`, an independent allowed gate for the open physical `Tr U1^2` sector.

The code re-audits only the historical Iteration-310 singleton-soft pruning premise on the current timelike common-background fixture. It uses the same-parent finite-geometry V2 construction, two independent derivative stencils and a step scan, with the old null-soft fixture retained as a negative control. It does not perform the full 42-placement contraction and does not perform a cut integral.

Workflow `rqir-iteration367-tru1sq-timelike-singleton-pruning-reaudit` was added in commit `19e7080aff61beac11a7bf6c9fa5366024724600` and automatically launched.

- run: `33806321673`
- status at launch audit: `queued`
- head: `19e7080aff61beac11a7bf6c9fa5366024724600`
- expected artifact: `iteration367-result`

No scientific conclusion is assigned until the raw JSON, sentinel/schema audit and artifact provenance are checked.

## Guardrails retained

- unsupported = BLOCKED, never zero-fill;
- historical Iteration-310 8-class pruning is not promoted on the timelike fixture unless re-proven;
- no `ANSATZ-003` before a robust comparator-subtracted residual;
- Fisher/resources remain forbidden;
- no Source/Born subtraction before matched-observable origin accounting;
- no blind heavy full-C5;
- operational cancellation of Iteration 364 is not a Candidate Gravity scientific FAIL.

## Exact next gate

1. Consume Iteration 367 raw artifact when available. If it validates that the timelike singleton U1 is nonzero, require full pre-pruning physical routing/contraction of all historical placements before any `Tr U1^2` cut integration. If the gate fails scientifically, preserve the negative result and diagnose the same-parent derivative/routing prerequisite without weakening thresholds.
2. Independently, replace Iteration 364 only with a scientifically targeted reduced/analytic or isolated-channel strategy; do not blindly duplicate the cancelled full 48-channel heavy run.

Authoritative iteration: 366.
MODEL_READINESS: 24%
