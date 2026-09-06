# Recovery Delta — Iteration 510

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact assembly authority
Classification: `PASS_BASE_HALF_ASSEMBLY_LINEAR_INDEPENDENCE_EXACT__NON_PROMOTING`.

For the frozen central4 assembly on the 28 distinct BASE/HALF support coordinates, exact rational row reduction gives `rank([W_BASE,W_HALF])=2`. With the retained discrepancy row `W_DELTA=W_BASE-W_HALF`, `rank([W_BASE,W_HALF,W_DELTA])=2`; the two-row assembly map therefore has nullity 26 on the 28-coordinate sample space.

Exact Gram matrix:

`[[4225/5184, 4/81], [4/81, 4225/324]]`

with positive determinant `5948843/559872`. There are 12 BASE-only and 12 HALF-only nonzero coordinates, providing an exact independence witness.

Operational guardrail: BASE and HALF must remain independently assembled, but BASE-minus-HALF is a derived diagnostic and must not later be counted as a third statistically independent observable/constraint or used to manufacture extra Fisher rank. The frozen BASE↔HALF threshold remains mandatory and unchanged.

Reproducible audit: `candidate_gravity/code/iteration510_base_half_assembly_linear_independence_exact_audit.py`. Result: `candidate_gravity/results/iteration510_base_half_assembly_linear_independence_exact_audit.json`.

## Active heavy gate
Iteration 509 remains the latest completed numerical mass-support authority: rank22 raw-consumed PASS, certified support `27/32 = 84.375% = 2160/2560`. Canonical rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, run `34058694183`, job `101555199703`, remains the sole authorized heavy gate. Do not duplicate it.

## Nonclaims
This exact result is assembly/provenance authority only. It is not Candidate-Gravity consistency PASS/FAIL, physical promotion of unresolved index 2, comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate, or Fisher authority. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden before a nonzero algebraic residual.

Readiness change: **0 percentage points**. The assembly linear-algebra contract is strengthened, but no additional stable-rubric model component is complete.

## Exact next gate
Fail-closed raw-consume rank23 run `34058694183` after completion. Only raw-valid PASS permits rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10; BLOCKED freezes suffix progression and requires first-failing-sample localization under unchanged frozen conventions.
