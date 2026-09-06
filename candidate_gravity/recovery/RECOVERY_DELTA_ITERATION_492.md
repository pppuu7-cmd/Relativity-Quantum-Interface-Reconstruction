# RECOVERY DELTA — ITERATION 492

Date: 2026-09-06
MODEL_READINESS: 24%

## New exact estimator/provenance result
Frozen central4 mixed weights `w_ij=c_i c_j` with `c=[1/12,-2/3,2/3,-1/12]` satisfy exactly

- `sum_i |c_i| = 3/2`,
- `sum_ij |w_ij| = 9/4`,
- `sum_ij w_ij^2 = 4225/5184`,
- `max_ij |w_ij| = 4/9`.

Hence, under a uniform per-sample absolute perturbation cap `|delta F_ij|<=eps`,

`|delta D_BASE| <= (9/4) eps / h^2`,

while HALF at step `h/2` obeys

`|delta D_HALF| <= 9 eps / h^2`.

The HALF/BASE worst-case absolute amplification-bound ratio is therefore exactly `4` solely from the `1/h^2` scaling.

Classification: `PASS_CENTRAL4_SAMPLE_ERROR_AMPLIFICATION_BOUND_EXACT__NON_PROMOTING`.

This is estimator/provenance authority only. It does not imply saturation, change frozen thresholds, promote index 2, establish comparator novelty, or constitute Candidate-Gravity consistency PASS/FAIL.

Reproducible code/result:
- `candidate_gravity/code/iteration492_central4_sample_error_amplification.py`
- `candidate_gravity/results/iteration492_central4_sample_error_amplification.json`

## Active heavy gate retained
Canonical frozen Iteration-455 rank16 `(u,v)=(-5e-6,-2.5e-6)`, multiplicity 1, run `34018646528`, remained `in_progress` on the last live check. No duplicate run was launched. Certified occurrence coverage remains `20/32 = 62.5%` until raw artifact consumption.

## Retained blockers and guardrails
Physical/operator authority remains Iteration 411. Iteration 421 remains `BLOCKED_CONVERGENCE` for unresolved set `[2]`. No zero-fill, no threshold weakening, no unsupported u↔v inference, no ANSATZ-003 before a robust comparator-subtracted residual, and no Fisher/resources before a nonzero algebraic residual.

## Readiness
MODEL_READINESS: 24%

Readiness change: 0 percentage points because this closes an estimator/provenance subgate but no new component of the stable 25/20/20/15/10/10 readiness rubric.

## Exact next gate
Fail-closed raw-consume rank16 run `34018646528`. If raw PASS, coverage may advance to `21/32 = 65.625%` and only frozen rank17 `(u,v)=(-5e-6,+2.5e-6)`, multiplicity 1, becomes authorized. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen conventions.
