# RQIR Candidate Gravity Research Log — Iteration 150

Date: 2026-08-31

Started from authoritative Iteration 149 after checking `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_149.md`, and recent commits.

## Work performed

Implemented a first explicit unreduced local C5 cubic-response block in the frozen Iteration-149 metric/source/probe convention.

- EH cubic coefficient evaluated directly from the `sqrt(-g) g Gamma Gamma` action density for three off-shell plane-wave modes.
- No on-shell/EOM-reduced amplitude basis used.
- Added two explicit covariant curvature-cubic directions: `Tr(Ricci^3)` and a cyclic `Riemann^3` contraction.
- Contracted with the six frozen spacelike probes, TT projectors, propagator factors, and Gaussian windows.
- Checked EH permutation symmetry and finite-difference convergence.
- Computed the first scoped local `V_C5^(chi2R)` tangent: shape `6x2`, rank `2/2`, singular values `[4.83562189, 1.10930485]`, `s_min/s_max=0.2294027268`.

## Important negative/methodological result

A standalone longitudinal replacement of one leg of the off-shell EH three-vertex is nonzero. This is not a GR consistency FAIL: the correct off-shell gauge statement is a Ward-Takahashi/Slavnov-Taylor identity involving inverse-propagator and source/contact terms.

Registered `NG-FUNNEL-010`: `OFFSHELL_VERTEX_LONGITUDINAL_NULL_IS_NOT_THE_WARD_IDENTITY`.

The old planned test `k.Gamma3 = 0` is therefore rejected as an invalid off-shell gate rather than used to manufacture a false failure.

## Status

PASS_SCOPED:
- EH TT cubic sub-block;
- two local curvature-cubic columns;
- finite rank/SVD certificate for this two-column local block.

BLOCKED:
- source-completed gravitational Ward-Takahashi identity;
- higher-dimension local C5 columns;
- loop/nonanalytic C5 columns;
- N2/C3sym.

No Fisher/resources. No `ANSATZ-003`.

## Next

Iteration 151: derive and implement the correct source-completed off-shell gravitational Ward-Takahashi relation for the exact EH sub-block, validate it on the same six probes, then decide whether to extend C5 local directions or instantiate fixed C3.
