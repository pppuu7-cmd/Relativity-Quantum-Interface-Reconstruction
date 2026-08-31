# Recovery Delta — RQIR Iteration 146

**Date:** 2026-08-31  
**Authoritative change:** first fixed finite C5 local-EFT tangent computed; full RQIR C5 embedding remains blocked at the retarded/CTP map.

## Previous front

Iteration 145 froze the 8D post-Gaussian reduced protocol and proved that broad class-capability masks are too unconstrained for a meaningful novelty quotient.

## New files

- `analysis/c5_tree_eft_tangent_iteration146.py`
- `results/c5_tree_eft_tangent_iteration146.json`
- `candidate_gravity/C5_FINITE_TANGENT_ITERATION146.md`
- `research_log/2026-08-31_iteration_146_c5_finite_tangent.md`
- `recovery/RECOVERY_DELTA_ITERATION_146.md`

## Frozen C5 realization

D=4, parity-even, low-energy GR EFT around Einstein-Hilbert. Local tree-level four-graviton operator basis through dimension 12, using the explicit amplitude basis of de Rham, Jaitly & Tolley (arXiv:2212.04975).

Linear Wilson coordinates:

`theta_C5=(c3,c_plus,c_minus,e_plus,e_minus,f_plus,f_minus,g_plus,g_minus,j1)`.

Twelve finite sub-cutoff kinematic/polarization points are frozen in the result JSON.

## Numerical result

The analytic on-shell amplitude tangent

`V_amp = d(M_Pl^2 A)/d theta_C5`

has shape `12 x 10` and rank **10/10**.

SVD singular values:

`3.77624716e-1, 7.94667137e-2, 9.08015595e-3, 9.16415267e-4, 4.72836512e-4, 2.33370720e-5, 1.72727839e-5, 2.13079285e-6, 1.03238331e-6, 9.27010447e-7`.

`s_min/s_max = 2.4548457953351053e-6`.

This is a real finite C5 local-Wilson tangent certificate at frozen kinematics.

## New retained blocker

### NG-FUNNEL-006 — ON_SHELL_TANGENT_NOT_RQIR_TANGENT

The Iteration-145 novelty quotient requires `N2`, `C3sym`, and ordered causal `chi^(2)R` in one declared CTP/state convention. An on-shell S-matrix derivative is not identical to that retarded object.

Therefore:

- `N2`: BLOCKED;
- `C3sym`: BLOCKED;
- direct `chi2R_even/odd` embedding: BLOCKED pending explicit retarded/CTP continuation;
- loop/nonanalytic C5 columns: BLOCKED pending derivation in the same convention.

Do not set these entries to zero.

This is an operational comparator-instantiation blocker, not a C5 consistency FAIL.

## Literature anchors

- arXiv:2212.04975 — finite gravitational EFT operator/amplitude basis;
- arXiv:1611.07534 — subsubleading soft-graviton EFT modifications;
- arXiv:gr-qc/9405057 — nonanalytic/nonlocal low-energy quantum gravity terms.

## `ANSATZ-003`

Still intentionally not frozen. No algebraic residual exists yet after a fully embedded fixed C5 comparator, so Fisher/resources remain inadmissible.

## Exact restart instruction

Resume at **Iteration 147 — retarded C5 embedding**.

1. freeze one CTP state/prescription;
2. derive one minimal finite retarded three-point/nonlinear-response C5 sub-block from EH + the same local EFT dynamics;
3. normalize it directly into the Iteration-145 `chi2R` coordinate convention;
4. check Ward/soft consistency at the same kinematics;
5. retain loop/nonanalytic terms as explicit columns or BLOCKED;
6. only then proceed to fixed C3 and nonlinear C4 tangents.
