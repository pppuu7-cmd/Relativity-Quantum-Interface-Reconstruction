# Recovery Delta — Iteration 396

Date: 2026-09-04

## Scope

Materialize and classify the completed Iteration-395 raw artifact without recomputation, then freeze the next scientific gate prospectively.

## Source-of-truth reads

- `candidate_gravity/recovery/CURRENT_QG_FRONT.md` (Iteration 393 authority at start of run)
- latest recovery/research material and recent commits
- Iteration-395 run `33821555831`, job `100865120160`, artifact `9918963191`
- artifact digest `sha256:ecf6b54dea9a2eb8d0231782015b02335c799baa32d5948b385e11cf3c40d30c`
- raw result SHA-256 `605d121616c36eb144b657d45de7be8a4dfd0d167402ec06eb48308daa8e5634`

## Scientific classification of Iteration 395

Iteration 395 is **BLOCKED_CONVERGENCE**, not a physics zero and not a consistency FAIL.

For the sole unresolved physical `Tr U1^2` double-double channel (global index 4, class 5, `q^2=-1`):

- old 6x12 high mixed derivative: `-3.0932102687618925e-4`
- new 8x16 base: `-2.8139677551950804e-4`
- new 8x16 phi-shifted: `-2.900091468025436e-4`
- new 8x16 h/2: `-2.8071606451092837e-4`
- base vs h/2 scaled error: `6.807110085796765e-7`
- base vs phi-shift scaled error: `8.612371283035585e-6`
- base vs old 6x12 scaled error: `2.792425135668121e-5`
- unchanged frozen threshold: `2e-5`
- max shell error: `2.42471651481016e-16`
- max radial Richardson scaled error: `8.725618426581871e-15`
- min uncut denominator: `0.12097107482337414`
- serial/parallel oracle error: `0.0`

Therefore execution and all non-angular checks pass, but the adjacent historical angular level has not yet met the frozen convergence threshold. The diagnostic candidate `D_s TrU1^2 = +2.8139677551950804e-4` is **not authority** while status remains BLOCKED_CONVERGENCE.

## Iteration 396 result

The raw Iteration-395 JSON is now materialized in-repository at:

`candidate_gravity/results/iteration395_tru1sq_double_double_channel4_stronger_angular_raw.json`

with provenance bridge:

`candidate_gravity/results/iteration396_materialize_iteration395_raw.json`.

Classification:

`PASS_MATERIALIZE_ITERATION395_RAW_WITHOUT_RECOMPUTATION`

No integration was repeated and no threshold was changed.

## Prospectively frozen next gate

Iteration 397 is a new version, not a post-hoc edit of Iteration 395. It advances only angular quadrature from 8x16 to 10x20 while keeping the same derivative arithmetic, radial rule, normalization, shell/uncut/Richardson/oracle checks and the same `2e-5` convergence threshold.

Prospective convergence tests are:

1. 10x20 base vs preserved 8x16 base;
2. 10x20 base vs 10x20 half-phi shift;
3. 10x20 base vs 10x20 h/2.

If Iteration 397 still returns BLOCKED_CONVERGENCE, no further blind grid escalation is authorized; channel 4 moves to analytic/spectral angular reduction.

## Readiness

MODEL_READINESS: 24%

Change from prior authority: `0 pp`. The sole double-double angular blocker is better localized and provenance-complete, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 observable and a comparator-subtracted residual remain open.
