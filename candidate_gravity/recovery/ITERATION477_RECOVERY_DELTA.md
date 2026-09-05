# Iteration 477 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 (`BLOCKED_CONVERGENCE`), exact unresolved physical set `[2]`. Iteration 475 remains latest completed numerical mass-support authority. Canonical rank-11 run `33989317870`, job `101368577097`, remains the sole active heavy gate and was not duplicated.

## New exact quartet-space precision/provenance authority
For positive central4 magnitudes `a,b in {1,2}`, define

`DeltaQ_ab = DeltaF(+a,+b)-DeltaF(-a,+b)-DeltaF(+a,-b)+DeltaF(-a,-b)`.

With positive-node derivative vector

`g=(2/3,-1/12)=(1/12)(8,-1)`, exact central4xcentral4 assembly gives

`DeltaD=<Wq,DeltaQ>_F`,

where

`Wq=g g^T=(1/144)[[64,-8],[-8,1]]`.

Hence

`DeltaD=(64 DeltaQ11-8 DeltaQ12-8 DeltaQ21+DeltaQ22)/144`.

No `u<->v` identity is assumed: `DeltaQ12` and `DeltaQ21` remain independent.

Exact norms:
- `rank(Wq)=1`;
- `||Wq||_F=65/144`;
- `||Wq||_F^2=4225/20736`;
- quartet-space dimension 4;
- derivative-sensitive dimension 1;
- exact quartet nullspace dimension 3.

An explicit integer nullspace basis in order `(Q11,Q12,Q21,Q22)` is

- `(1,0,0,-64)`;
- `(0,1,0,8)`;
- `(0,0,1,8)`.

The unique sensitive quartet projection is

`DeltaQ_sens=(144/4225)DeltaD [[64,-8],[-8,1]]`,

with

`||DeltaQ_sens||_F=(144/65)|DeltaD|`.

For the Iteration-467 odd-odd projector `X=Qo DeltaF Qo`, exact sign replication gives

`||X||_F=(1/2)||DeltaQ||_F`,

and therefore

`|DeltaD| <= (65/144)||DeltaQ||_F = (65/72)||Qo DeltaF Qo||_F`.

This is exactly consistent with the Iteration-476 full-matrix rank-1 sensitive norm `(72/65)|DeltaD|`.

Classification: `PASS_QUARTET_RANK1_COMPRESSED_PRECISION_CERTIFICATE__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This is implementation/provenance compression only. It changes no frozen estimator, threshold, dynamics, support ordering, source occurrence accounting, coordinate state, or physical promotion rule. It does not authorize support deduplication or `u<->v` identification. Failure of quartet-versus-canonical assembly equivalence is implementation/provenance BLOCKED, not physics FAIL.

Reproducible code: `candidate_gravity/code/iteration477_quartet_rank1_compressed_certificate.py`.
Result: `candidate_gravity/results/iteration477_quartet_rank1_compressed_certificate.json`.
Research log: `candidate_gravity/research_log/2026-09-05_iteration_477.md`.

`ANSATZ-003` remains uncreated. Comparator-subtracted residual and Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: **0 percentage points**. The final assembly provenance path is compressed to an exact four-quartet rank-1 certificate, but no additional stable readiness-rubric component is fully closed.

## Exact next gate
Raw-consume canonical rank-11 run `33989317870` fail-closed. PASS permits only the next UNTESTED frozen Iteration-455 manifest coordinate; BLOCKED requires localization at rank 11 without threshold/dynamics/routing/precision changes.
