# RQIR Candidate Gravity — Research Log Iteration 436

## Prospective gate freeze

Iteration 436 is allocated uniquely under `recovery/ITERATION_ID_REGISTRY.md` before its numerical workflow result is inspected.

The gate closes only the Iteration-270 `N1` parent layer used downstream by `Q1`. It carries the exact frozen chain

`geometry -> nhat -> y_down -> norb -> N1`

at the same Iteration-270 representative inputs:

- `M = POS`;
- legs `s, a, b`;
- loop momentum `P0 = [0.7,-0.4,0.5,0.9]`;
- symmetric amplitude derivative step `h = 3e-5`;
- the exact existing Iteration-270 momenta/polarizations, interpreted as the frozen numerical constants already defining the parent dynamics.

No derivative step, polarization, momentum, formula, routing, sign or normalization may change.

## Frozen precision implementation

The arbitrary-precision implementation must reproduce the complete Iteration-270 formulas for:

1. `geometry`: metric, inverse metric, first/second metric derivatives, Christoffels, derivative Christoffels, Ricci tensor;
2. `nhat`: complete covariant vector Laplacian plus Ricci term;
3. `y_down = sqrt(abs(det(g))) * g`;
4. `norb = y_down @ nhat`;
5. `N1 = [norb(+h)-norb(-h)]/(2h)`.

The implementation may not replace this chain by a simplified or denominator-only surrogate.

## Prospectively frozen acceptance

The following thresholds are frozen before raw workflow authority:

- required precisions: `80` and `120` decimal digits;
- maximum componentwise scaled `N1(80)-N1(120)` discrepancy: `1e-40`;
- maximum componentwise scaled endpoint `norb(binary64)-norb(120)` discrepancy at every `+h/-h` endpoint: `1e-12`;
- binary64-vs-120-digit `N1` discrepancy is classified against the unchanged physical reference tolerance `2e-5`:
  - `<=2e-5`: legacy N1 reproduced within the physical tolerance;
  - `>2e-5`: materially different legacy N1, while the multiprecision closure may still be scientifically valid if the precision and endpoint-equivalence gates pass;
- all 80/120-digit endpoint and N1 values must be finite.

The scientific gate passes only if the 80/120-digit cross-precision criterion, endpoint binary64-reproduction criterion, and finiteness checks pass. The `2e-5` legacy-N1 comparison is a pre-frozen diagnostic classification, not permission to weaken any downstream physical gate.

## Authority scope

`N1` precision only. A PASS does **not** certify `Q1`, `A_finite`, `Acoef`, `Asub`, 368/370, the fixed-mass `F`, Iteration 424, or the physical index-2 `D_s` coordinate.

## Readiness discipline

`MODEL_READINESS = 24%` at gate launch. No readiness increase is allowed from this gate alone unless it closes a separately defined stable rubric component; physical index 2 remains governed by Iteration 421/424 authority.
