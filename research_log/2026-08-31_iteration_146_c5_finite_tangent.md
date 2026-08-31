# RQIR Research Log — Iteration 146

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / fixed comparator tangents  
**Promotion decision:** no `ANSATZ-003` frozen

## Starting authority

Iteration 145 fixed the post-Gaussian protocol and showed that broad C3/C4/C5 capability masks saturate the reduced 8D space. The mandated next step was a fixed finite C5 realization.

## Literature checked

Fresh verification retained three anchors:

- de Rham, Jaitly & Tolley, arXiv:2212.04975 — explicit D=4 gravitational EFT operator basis and four-graviton amplitudes through dimension 12;
- Elvang, Jones & Naculich, arXiv:1611.07534 — local EFT modifications enter the graviton soft theorem at subsubleading order, not the subleading order in the analysed setting;
- Donoghue, arXiv:gr-qc/9405057 — low-energy massless quantum effects appear as nonanalytic/nonlocal contributions and cannot be represented merely by arbitrary local Wilson coefficients.

## Frozen comparator

C5 is frozen as D=4 parity-even low-energy GR EFT around Einstein-Hilbert, with local tree-level four-graviton operators through dimension 12. The linear Wilson coordinates are

`(c3,c_plus,c_minus,e_plus,e_minus,f_plus,f_minus,g_plus,g_minus,j1)`.

Twelve finite sub-cutoff kinematic/polarization points were frozen. The tangent is evaluated analytically from the published crossing-symmetric amplitude, not by finite differencing.

## Numerical certificate

`V_amp = d(M_Pl^2 A_a)/d theta_i`

has shape `12 x 10` and rank **10/10**.

Singular values:

`[3.77624716e-1, 7.94667137e-2, 9.08015595e-3, 9.16415267e-4, 4.72836512e-4, 2.33370720e-5, 1.72727839e-5, 2.13079285e-6, 1.03238331e-6, 9.27010447e-7]`.

The smallest-to-largest ratio is `2.4548457953351053e-6`; the matrix is full column rank at standard SVD tolerance.

Authorities:

- `analysis/c5_tree_eft_tangent_iteration146.py`;
- `results/c5_tree_eft_tangent_iteration146.json`;
- `candidate_gravity/C5_FINITE_TANGENT_ITERATION146.md`.

## Negative / blocking result

The computed object is an on-shell S-matrix tangent, whereas the Iteration-145 novelty quotient requires ordered causal `chi^(2)R` plus CTP fluctuation objects in one declared state.

Retained:

**NG-FUNNEL-006 — ON_SHELL_TANGENT_NOT_RQIR_TANGENT.**

Do not identify an amplitude derivative with a retarded nested-commutator response without an explicit continuation/prescription. `N2`, `C3sym`, the direct `chi2R` embedding and the required loop/nonanalytic rows remain **BLOCKED**, not zero.

This is not a consistency failure of C5. It is an operational comparator-instantiation blocker.

## Consequence for candidate design

No algebraic candidate residual is certified yet, so Fisher/resources remain forbidden. `ANSATZ-003` remains intentionally withheld.

## Next gate

Iteration 147: derive the first explicitly normalized retarded C5 nonlinear-response sub-block from the same EH + local-EFT dynamics and one frozen CTP state/prescription. Preserve loop/nonanalytic contributions as separate physical columns or explicit BLOCKED entries.
