# Recovery Delta — Iteration 512

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact assembly conditioning authority
Classification: `AUDIT_BASE_HALF_ASSEMBLY_SINGULAR_SPECTRUM_EXACT__NON_PROMOTING`.

For the exact Iteration-510 BASE/HALF Gram matrix `G=[[4225/5184,4/81],[4/81,4225/324]]`, the exact eigenvalues are `(71825±sqrt(4016652769))/10368`. Numerically they are approximately `0.81480824040386763744` and `13.0403229324356385354`. The Gram condition number is approximately `16.00416182091147668`, and the corresponding singular-value condition number of the two-row assembly map is approximately `4.0005201937887373552`.

Operational meaning: BASE and HALF remain exactly linearly independent and their two-dimensional assembly row space is not near singular under the Euclidean coordinate-error geometry encoded by this Gram matrix. This is a numerical/provenance diagnostic only and creates no new frozen threshold.

Reproducible audit: `candidate_gravity/code/iteration512_base_half_assembly_singular_spectrum_exact_audit.py`. Result: `candidate_gravity/results/iteration512_base_half_assembly_singular_spectrum_exact_audit.json`.

## Active heavy gate
Iteration 509 remains the latest completed numerical mass-support authority: rank22 raw-consumed PASS, certified support `27/32 = 84.375% = 2160/2560`. Canonical rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, run `34058694183`, job `101555199703`, remains the sole authorized heavy gate and must not be duplicated. At this iteration it was still `in_progress` on `Run manifest-rank23 full-z MP stage`; queued count was zero, raw authority audit and upload remained pending.

## Nonclaims
No physical promotion, comparator novelty, residual, Fisher authority, or readiness point is claimed. Physical/operator authority remains Iteration 411; blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved set `[2]`. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden before a nonzero algebraic residual.

Readiness change: **0 percentage points**.

## Exact next gate
Fail-closed raw-consume rank23 run `34058694183` after completion. Only raw-valid PASS permits rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10; BLOCKED freezes suffix progression and requires first-failing-sample localization under unchanged frozen conventions.
