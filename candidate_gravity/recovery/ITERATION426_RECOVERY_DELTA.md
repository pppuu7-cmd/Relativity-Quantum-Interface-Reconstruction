# Iteration 426 Recovery Delta

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** diagnostic only; non-promoting  
**Raw-valid run:** 33886485823  
**Job:** 101067408773  
**Artifact:** 9943246167  
**Artifact digest:** `sha256:efd42550e9e5be80436585f1d4090d7ad29cb8adeed573f40dbadc3fc6fe6a66`

## Result

The 16-vs-32 phi-node diagnostic completed successfully for double-double index 2 / class 3 / `q^2=-1`.

The prospectively frozen materiality rule was unchanged: phi resolution would be considered material only if the symmetric-cross change exceeded `2e-5` scaled.

Observed:

- at `R=1e-5`: scaled cross-quotient change `2.7863995832877464e-7`;
- at `R/2=5e-6`: scaled cross-quotient change `1.231653667943533e-5`;
- maximum: `1.231653667943533e-5 < 2e-5`;
- maximum direct fixed-mass `F` 16-vs-32 change: `6.006480035569695e-16` scaled;
- parent-reproduction oracle: `8.673617379884035e-19` scaled.

Thus phi-node resolution is **not a dominant explanation** of Iteration-421 `BLOCKED_CONVERGENCE` at the unchanged physical tolerance.

## Consequence

Do not spend the next physical iteration on angular-grid escalation. The priority moves to the deeper traced-numerator/full-precision chain identified by Iterations 428 and 429. In particular, the numerator primitives and nested derivative machinery must be ported or certified before claiming an 80/120-digit Iteration-424 result.

## Current front

1. Iteration 421: raw-valid `BLOCKED_CONVERGENCE`.
2. Iteration 426: phi resolution stable and deprioritized.
3. Iteration 427: exact full-H mass-to-kinematic derivative reduction available as independent oracle.
4. Iteration 428: binary64 conditioning at the smallest symmetric-cross nodes quantified.
5. Iteration 429: full-F precision-closure manifest passed.
6. Next: Stage 1 implementation of the Iteration-424 fallback, starting in the deepest 368/370 numerator layer.

No physical coordinate is promoted by this result. `MODEL_READINESS = 24%`.
