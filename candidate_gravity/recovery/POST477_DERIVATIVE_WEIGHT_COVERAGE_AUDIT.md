# Post-477 derivative-weight coverage audit

Status: **diagnostic only / non-promoting**. Canonical authority remains Iteration 477. Latest completed numerical mass-support authority at audit time is Iteration 475. Active heavy gate remains Iteration-455 distinct rank 11, run `33989317870`, coordinate `(u,v)=(+5e-6,+1e-5)`.

## Why this audit exists

Occurrence-weighted support coverage (`15/32 = 46.875%`) is a provenance metric, not a measure of how much of the frozen central4 mixed-derivative sensitivity is already locally MP-certified. This audit computes exact central4 derivative-weight coverage without changing source order, thresholds, or promotion rules.

For frozen central4 coefficient vector

`c=(1/12,-2/3,+2/3,-1/12)`,

sample weights are `W = c c^T`. Exact totals:

- `sum |W_ij| = 9/4`;
- `sum W_ij^2 = ||W||_F^2 = 4225/5184`.

## Current certified front

Iteration-455 BASE distinct ranks `0..10` are already certified (rank 10 was pre-certified and must not be rerun). Therefore current BASE sensitivity coverage is:

- L1 absolute derivative-weight coverage: `149/162 = 91.9753086419753%`;
- squared Frobenius / derivative-sensitive energy coverage: `8353/8450 = 98.85207100591716%`.

The current exact BASE/HALF shared certificates correspond only to the four HALF corner coordinates `(±5e-6,±5e-6)`. Their HALF sensitivity coverage is still tiny:

- HALF L1: `1/81 = 1.2345679012345678%`;
- HALF squared Frobenius: `1/4225 = 0.023668639053254437%`.

Thus the current bottleneck is asymmetric: BASE is already strongly covered in derivative-sensitive weight, while HALF convergence support remains mostly open.

## If active rank 11 passes

Rank 11 is BASE coordinate `(+5e-6,+1e-5)`, multiplicity 1. A raw-valid PASS would move occurrence coverage from `15/32` to `16/32 = 50%`, but BASE sensitivity coverage would move more strongly:

- BASE L1 -> `17/18 = 94.44444444444444%`;
- BASE squared Frobenius -> `129/130 = 99.23076923076923%`.

HALF sensitivity coverage would remain unchanged at that point.

## Scientific interpretation

1. Do **not** interpret `15/32` as only 46.875% of physical derivative sensitivity checked.
2. Do **not** interpret the high BASE sensitivity coverage as physical closure: the frozen contract still requires all support coordinates, independent BASE and HALF MP assembly, the assembled MP80↔MP120 gate, and BASE↔HALF convergence.
3. This audit cannot reorder Iteration-455 source order, skip low-weight coordinates, deduplicate `u<->v`, weaken thresholds, or promote `D_s`.
4. The result supports a more informative progress dashboard: report occurrence coverage and BASE/HALF derivative-sensitivity coverage separately rather than fabricating one scalar bottleneck percentage.

## Guardrails retained

- no support reordering;
- no `u<->v` deduplication;
- no skipping untested coordinates;
- no threshold change;
- no local-PASS-for-assembly substitution;
- no physical index-2 promotion;
- no `ANSATZ-003`;
- no Fisher/resource claims.

**MODEL_READINESS: 24%**. Readiness change: **0 pp**.
