# RECOVERY DELTA — ITERATION 657

Date: 2026-09-09

## Authority entering
Iter656 established that the Iter653 `q^-2/q^-4` reconstruction is outside its domain on the exact Iter655 null leg and forbade zero-fill/post-hoc regulators.

## Result
For the action-level gauge map `L_q(xi)=q_(mu xi_nu)` and divergence `D_q`, exact arithmetic at the frozen null direction gives `rank(L_q)=4`, `rank(D_q)=4`, `rank(D_q L_q)=1`, hence

`dim(Im L_q ∩ Ker D_q)=3`.

Therefore the null longitudinal/transverse split is intrinsically nonunique: three independent nonzero pure-gauge tensors are also transverse. The frozen plus-TT tensor is transverse but not pure gauge; nevertheless its decomposition can be shifted by any element of this three-dimensional overlap.

Classification:

`BLOCKED_ITER657_NULL_WARD_COMPLETION_NONUNIQUE__IMAGE_LQ_INTERSECTS_TRANSVERSE_SUBSPACE_DIM3__AUXILIARY_COMPLEMENT_REQUIRED__NON_RESIDUAL`

This is operational/mathematical BLOCKED, not model consistency FAIL/PASS, comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Frozen consequences
- `zero_fill=false`.
- No auxiliary null vector, off-null path or complement may be chosen after cut inspection.
- The Iter653 non-null projector remains valid only in its original domain.
- Native soft `T_cut`, Source/Born subtraction and fixed comparator quotient remain `NOT_PERFORMED`.
- No ANSATZ-003; no Fisher/resources.

## Readiness
MODEL_READINESS: 24%

Delta: 0 percentage points; robust unique residual remains 0/20 and no full rubric sector closes.

## Exact next gate
Iteration658: determine whether the frozen plus-TT soft `T_cut` measurement is a well-defined functional on `Ker(D_q)/(Im(L_q)∩Ker(D_q))`, invariant under all three null-gauge-overlap directions. If yes, construct it without a complement; if no, retain BLOCKED or prospectively define a complement before inspecting new cut values.
