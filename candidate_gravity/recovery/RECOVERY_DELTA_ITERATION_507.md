# RQIR Candidate Gravity — Recovery Delta Iteration 507

**Date:** 2026-09-06

## Authority retained
- Latest validated physical/operator authority: Iteration 411.
- Latest raw-valid physical blocker: Iteration 421 `BLOCKED_CONVERGENCE`, exact unresolved set `[2]`.
- Latest completed numerical mass-support authority: Iteration 505 rank21 raw PASS.
- Iteration 506 rank22 prerequisite dynamics/parameter-chain audit: PASS, non-promoting.
- Stable `MODEL_READINESS`: `24%`.
- Certified occurrence-weighted mass-support coverage: `26/32 = 81.25% = 2080/2560` rows.

## Iteration 507 new authority
Frozen Iteration-455 manifest suffix after rank21 was re-audited and preregistered exactly. Classification:

`PASS_RANK23_SUCCESSOR_AND_RANK22_27_SUFFIX_PREREGISTERED_EXACT__NON_PROMOTING`

The active rank22 coordinate remains `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1. If and only if rank22 later obtains raw-valid PASS, the sole authorized next coordinate is rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, multiplicity 1.

Remaining frozen suffix is ranks 22–27, all multiplicity 1:
- 22: `(+2.5e-6,-5e-6)`, HALF 8
- 23: `(+2.5e-6,-2.5e-6)`, HALF 9
- 24: `(+2.5e-6,+2.5e-6)`, HALF 10
- 25: `(+2.5e-6,+5e-6)`, HALF 11
- 26: `(+5e-6,-2.5e-6)`, HALF 13
- 27: `(+5e-6,+2.5e-6)`, HALF 14

No post-hoc support reordering, u/v deduplication, threshold change, surrogate fallback, ANSATZ-003 creation, or Fisher/resources activation is authorized.

## Conditional coverage ledger
Starting from raw-valid rank21 `26/32`:
- rank22 PASS -> `27/32 = 84.375% = 2160/2560`
- rank23 PASS -> `28/32 = 87.500% = 2240/2560`
- rank24 PASS -> `29/32 = 90.625% = 2320/2560`
- rank25 PASS -> `30/32 = 93.750% = 2400/2560`
- rank26 PASS -> `31/32 = 96.875% = 2480/2560`
- rank27 PASS -> `32/32 = 100% = 2560/2560`

These are conditional arithmetic consequences only, not claims that any unfinished rank has passed.

## Physical-blocker separation
Iteration 421 was re-read to ensure local support progress is not misreported as physical-model progress. Index 2 / class 3 / `q^2=-1` remains `BLOCKED_CONVERGENCE`: stability `2.2720400683804223e-05` and required fit residual `2.585665489102237e-05` narrowly exceed their prospective frozen `2e-05` limits. Structural, conditioning, direct-integrand and analytic checks otherwise pass. Diagnostic `D_s` remains non-authoritative. No threshold weakening is permitted.

The frozen Iteration-424 MP80/MP120 fallback contract therefore remains relevant only in the correct downstream position after complete support closure and independent BASE/HALF assembly. It is not authorization to bypass ranks 22–27.

## Reproducible records
- `candidate_gravity/code/iteration507_rank23_successor_suffix_preregistration_audit.py`
- `candidate_gravity/results/iteration507_rank23_successor_suffix_preregistration_audit.json`
- `candidate_gravity/research_log/2026-09-06_iteration_507.md`

## Active heavy gate
Canonical rank22 run `34053331578`, job `101540723619`, remains the only authorized heavy run on the live Iteration-507 check and must not be duplicated. Workflow colour alone is not authority; raw artifact audit/consumption is mandatory.

## Readiness
**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. This iteration removes successor-order discretion and strengthens recovery/provenance, but does not complete a stable-rubric Candidate-Gravity component.

## Exact next action
Raw-audit and raw-consume canonical rank22 after completion. Raw-valid PASS authorizes only rank23. Raw BLOCKED freezes progression and requires localization of the first failing `z/phi/radial` sample under unchanged dynamics, support order, precision convention, and thresholds.
