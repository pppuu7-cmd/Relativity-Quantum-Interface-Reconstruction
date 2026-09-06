# RQIR Candidate Gravity — Recovery Delta Iteration 508

**Date:** 2026-09-06

## Authority retained
- Latest validated physical/operator authority: Iteration 411.
- Latest raw-valid physical blocker: Iteration 421 `BLOCKED_CONVERGENCE`, exact unresolved set `[2]`.
- Latest completed numerical mass-support authority: Iteration 505 rank21 raw PASS.
- Certified occurrence-weighted mass-support coverage: `26/32 = 81.25% = 2080/2560` rows.
- Canonical rank22 run `34053331578`, job `101540723619`, remains the sole authorized heavy run and must not be duplicated.
- Stable readiness remains `MODEL_READINESS: 24%`.

## Iteration 508 new authority
Exact frozen central4 BASE/HALF coordinate geometry and overlap weights were audited independently.

Classification:

`PASS_BASE_HALF_32_OCCURRENCES_28_DISTINCT_OVERLAP_WEIGHTS_EXACT__NON_PROMOTING`

BASE uses the 4x4 tensor product of 1D offsets `{-2,-1,+1,+2}` in units of `h`; HALF uses the same offsets at step `h/2`, i.e. coordinates `{-1,-1/2,+1/2,+1}` in BASE-h units. Each stencil therefore contributes 16 source occurrences, but their exact intersection is only the four points `(±1,±1)`. Hence:

- total source occurrences: `16+16=32`;
- exact overlap count: `4`;
- distinct union coordinates: `16+16-4=28`.

Thus the frozen `32 occurrences / 28 distinct coordinates` bookkeeping is an exact consequence of the two central4 grids, not an arbitrary support deduplication.

At the four shared points, in units of `1/h^2`, BASE mixed weights are `±4/9`, HALF mixed weights are `±1/36`, and the exact `D_BASE-D_HALF` weights are `±5/12` with checkerboard signs. Local sampled precision certificates may be shared at identical coordinates, but BASE and HALF derivative weights remain mathematically distinct and both must be applied.

Exact L1 weight norms in units of `1/h^2`:
- BASE `9/4`;
- HALF `9`;
- separate BASE+HALF bookkeeping `45/4`;
- union-aggregated `D_BASE-D_HALF` `397/36`;
- exact overlap cancellation reduction `2/9`.

No frozen threshold, `ds=-d_base` convention, support order, or Richardson guardrail is changed.

## Reproducibility
- `candidate_gravity/code/iteration508_base_half_union_overlap_exact_audit.py`
- `candidate_gravity/results/iteration508_base_half_union_overlap_exact_audit.json`
- `candidate_gravity/research_log/2026-09-06_iteration_508.md`

No literature refresh was required because this iteration advances only exact internal assembly/provenance geometry, not an external comparator, novelty, consistency, or phenomenology claim.

## Scientific semantics
This is assembly/provenance PASS only. It is not Candidate-Gravity consistency PASS or FAIL, not physical index-2 promotion, not assembled numerical derivative closure, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

`ANSATZ-003` remains forbidden. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Readiness
**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. A real exact assembly subgate is closed, but no additional stable-rubric Candidate-Gravity component is completed.

## Exact next action
Raw-audit and raw-consume canonical rank22 run `34053331578` after completion. Only raw-valid PASS authorizes rank23 `(u,v)=(+2.5e-6,-2.5e-6)`. If rank22 is raw BLOCKED, freeze progression and localize the first failing `z/phi/radial` sample under unchanged dynamics, thresholds, support order, and precision convention.
