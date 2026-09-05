# Recovery Delta — Candidate Gravity Iteration 457

**Date:** 2026-09-05  
**Authority type:** exact central4 overlap-weight algebra/provenance audit; non-promoting  
**Classification:** `PASS_OVERLAP_PRECISION_SHARE_BUT_STENCIL_WEIGHT_COLLAPSE_FORBIDDEN__NON_PROMOTING`

## Result
The frozen Iteration-379/407 mixed auxiliary-mass derivative uses the fourth-order first-derivative stencil

`[1/12, -2/3, +2/3, -1/12] / h`

on both axes. BASE has `h=5e-6`; HALF has `h=2.5e-6 = h_BASE/2`.

At each of the four exact BASE/HALF coordinate overlaps `(±5e-6,±5e-6)`, the identical `F(u,v)` sample may share one direct MP precision certificate, but its tensor-product mixed-derivative coefficient is level-dependent. In units of `1/h_BASE^2`, BASE coefficients are `±4/9`, HALF coefficients are `±1/36`, with matching signs and exact magnitude ratio

`w_BASE / w_HALF = 16`.

Therefore the 28 distinct-coordinate precision queue is valid for avoiding duplicate `F(u,v)` evaluations, while the 32 source occurrences must remain distinct in downstream BASE/HALF derivative assembly. Any collapse of the derivative occurrence bookkeeping from 32 to 28 would be algebraically invalid.

No `F(u,v)` was evaluated and the active run `33946347229` was not duplicated.

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker remains Iteration 421 for double-double index 2 / class 3 / `q^2=-1`. Certified occurrence-weighted precision coverage remains `4/32 = 12.5%`; Iteration 457 changes bookkeeping semantics only, not coverage.

`ANSATZ-003`, Fisher/resources, exact15 promotion and comparator residual remain blocked.

MODEL_READINESS: 24%

Change: **0 percentage points**. A real algebra/provenance ambiguity is closed, but no stable readiness-rubric component is completed.

## Next gate
Raw-consume run `33946347229` fail-closed at `u=-1e-5, v=+5e-6`. PASS permits only the next Iteration-455 manifest coordinate with unchanged five-z/NPHI16/radial/direct-MP80/120 conventions. BLOCKED requires localization of the first failing sample at exactly the active coordinate.
