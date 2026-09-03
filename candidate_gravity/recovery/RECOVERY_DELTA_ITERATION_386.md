# RQIR Candidate Gravity — Recovery Delta Iteration 386

**Date:** 2026-09-04  
**Status:** DEPENDENCY / AUTHORITY AUDIT — NO NEW PHYSICS PROMOTION  
**MODEL_READINESS: 24%**

## Purpose

Iteration 386 freezes the exact dependency map that must be used after the active physical `e=2` operator calculations close. It prevents the research loop from reopening source/comparator branches that were already solved or from treating formal comparator blockers as zeros.

Frozen linked target:

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`, with `D_s F = Disc_s F/(2*pi*i)`.

## What is already closed

### Joint relation protocol — Iteration 183

The observable is the split-invariant joint object

`Y=(K2_rows,S_soft2_full_rows)`.

Comparator/nuisance directions must be conditioned on exact `delta K2_rows=0` before the cubic quotient. The previous internal `W/B` repartition is not an observable and must not be resurrected as one.

### Local quadratic C5 source-completed soft2 — Iteration 185

The dimension-12 local quadratic ladder is complete on the six frozen null-soft TT rows. The source-completed cubic plus nonlinear Lie contact construction passes scoped Ward residuals at machine precision. The K2-preserving local compensation soft2 vector is already frozen.

### Nonlocal C5 calibrated direction — Iteration 186

The `QG-NL-EXP-001` lambda tangent is resolved after exact K2-preserving local compensation and survives the frozen zero-K2 local rank-4 quotient. It is comparator authority, not Candidate Gravity novelty.

## What remains blocked

### C3 — Iteration 230

C3 is frozen as

`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`.

The same parent does not supply a unique nonlinear conserved representative modulo the explicit doubly-transverse `O(h)` homogeneous family. Choosing `H=0` or a convenient projector would be a new comparator model choice. Therefore C3 is `BLOCKED_NOT_ZERO`.

### Asymptotic safety — Iteration 234 plus 2026 refresh

The available Lorentzian scalar-scattering / scalar-scalar-graviton authority is not observable-identical to the frozen pure-gravity linked relation and does not supply a same-parent retarded three-graviton discontinuity plus shared K2/source-contact normalization. AS remains `BLOCKED_NOT_ZERO`.

### Native causal pure-gravity linked h3 object — Iteration 239

Generic retarded/dispersive QFT exists and causal GR source/worldline calculations exist, but the frozen `T_cut` still lacks an executable gauge-safe/source-completed pure-metric `Gamma3_ret[h,h,h]` linked to the same-parent `K2` with a controlled hard-channel discontinuity. This is the present authority boundary, not a statement that the coordinate is zero.

## Active prerequisite

Candidate `e=2` origin accounting is itself not yet complete. Active branches at the time of this audit are:

- Iteration 381 — 36 simple-double `Tr U1^2` channels;
- Iteration 384 — 48 repeated-cut `Tr U2` channels in two-channel chunks;
- Iteration 385 — resource-repaired one-channel double-double `Tr U1^2` pilot.

No downstream residual is permitted before those operator coordinates close.

## Exact post-e2 order

1. Freeze the complete q2-resolved Candidate `e=2` coordinate only after full `Tr U2` and full `Tr U1^2` closure.
2. Map that coordinate into the already-frozen joint relation convention `Y=(K2_rows,S_soft2_full_rows)`.
3. Reuse Iteration-185 local C5 and Iteration-186 nonlocal conditioned comparator columns; do not recompute them merely because the Candidate value changed.
4. Preserve C3 and AS as `BLOCKED_NOT_ZERO` until genuinely new same-parent authority removes the frozen blockers.
5. Do not claim a robust unique residual, create `ANSATZ-003`, or compute Fisher/resources while any required comparator coordinate remains BLOCKED.

## Retained finite-DR boundary

Iteration 297 remains binding for the determinant evanescent/regulator remainder. Iteration 383 closes only the ordinary two-simple-particle normalized determinant vector, not the full finite-dimensional determinant.

## Readiness

`MODEL_READINESS: 24%`.

Change: `0 pp`. This iteration reduces future workflow ambiguity but does not close the remaining comparator-foundation point or create a residual.
