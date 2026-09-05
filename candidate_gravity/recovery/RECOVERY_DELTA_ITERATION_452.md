# Recovery Delta — Candidate Gravity Iteration 452

**Date:** 2026-09-05  
**Authority type:** frozen mass-support source-occurrence multiplicity audit; non-promoting  
**Classification:** `PASS_MASS_SUPPORT_SOURCE_OCCURRENCE_MULTIPLICITY_AUDIT__NON_PROMOTING`

## Authority
Physical/operator authority remains Iteration 411. Physical blocker remains raw-valid Iteration 421 for double-double index 2 / class 3 / `q^2=-1`. Exact unresolved physical set remains `[2]`. Iteration 450 remains the latest completed one-coordinate full-training-z precision authority. Run `33935454815` remains the only active next-mass-node gate and is not duplicated.

## New retained fact
Iteration-407 mixed-mass evaluation consists of 16 BASE occurrences at `h=5e-6` plus 16 HALF occurrences at `h=2.5e-6`, using nodes `[-2h,-h,+h,+2h]`. These are 32 source occurrences but only 28 distinct `(u,v)` coordinates because BASE and HALF overlap at exactly:
`(-5e-6,-5e-6)`, `(-5e-6,+5e-6)`, `(+5e-6,-5e-6)`, `(+5e-6,+5e-6)`.

The frozen 32-occurrence denominator remains unchanged. The 28-coordinate view is auxiliary deduplication provenance only and does not weaken any acceptance criterion.

## Coverage correction
The raw-valid full-training-z precision certificate at `u=v=+5e-6` is a certificate of the same mass-only `F(u,v)` sample path for both BASE and HALF occurrences at that exact coordinate. Therefore occurrence-weighted precision coverage is 2/32 source occurrences = 160/2560 row occurrences = 6.25%. Distinct-coordinate coverage is 1/28 = 3.571428...%. The earlier 80/2560 = 3.125% statement is a conservative bookkeeping undercount, not a scientific error and not a promotion.

## Active source-order guard
The active coordinate `(-1e-5,-1e-5)` has source multiplicity one. If run `33935454815` raw-consumes as PASS, the prospectively fixed next untested BASE source-order coordinate is `(-1e-5,-5e-6)`. Do not launch it before raw consumption of the active gate.

`ANSATZ-003` remains uncreated. Iteration 412 exact15 remains BLOCKED. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Change: **0 percentage points** — corrected numerical-provenance accounting closes no stable readiness-rubric component.

## Next gate
Raw-consume run `33935454815` fail-closed. PASS permits only `u=-1e-5, v=-5e-6` next under unchanged conventions; BLOCKED requires first-failure localization at `u=v=-1e-5`.
