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

## Canonical raw Actions provenance
- run: `34333673862`
- job: `102407910144`
- head: `66789fbef67c5676c67e8eb789fb24c480aabdf4`
- artifact: `10096791809` (`rqir-iteration657-null-ward-completion-rank-audit`)
- artifact digest / downloaded ZIP SHA-256: `3f14419ea7a77d2915c2358183cc2ad3ae49492b7556887f86a05e4b339e049d`
- raw JSON SHA-256: `247f43ab9273c98cd6cc4e8b2c9f9b106f8ec014c8c78f03ca2331cb3dec27d9`
- raw result: `failures=[]`; ranks `(4,4,1)`; overlap dimension `3`; `zero_fill_allowed=false`.

Scientific authority is assigned from the independently consumed raw artifact, not from workflow colour.

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
