# Candidate Gravity — Iteration 146: finite C5 tree-EFT tangent

**Date:** 2026-08-31  
**Status:** scoped C5 comparator progress; full post-Gaussian RQIR `V_C5` remains **BLOCKED** at the retarded/CTP map.

## Objective

Iteration 145 proved that broad class-capability masks are unusable as novelty quotients. The next requirement was a fixed finite C5 realization. This iteration freezes the first such realization and computes a reproducible physical Wilson tangent without pretending that an on-shell S-matrix is already the RQIR ordered response.

## Frozen C5 realization

Regime:

- four spacetime dimensions;
- perturbative low-energy quantum GR EFT;
- Einstein-Hilbert massless-graviton boundary;
- parity-even local gravitational operators;
- tree-level local EFT sector through mass dimension 12 for the 2-to-2 graviton amplitude;
- Wilson coefficients expanded about the Einstein-Hilbert point;
- dimensionless convention `Lambda=1`, amplitudes reported as `M_Pl^2 A`.

The finite local operator basis is taken from de Rham, Jaitly & Tolley, arXiv:2212.04975, eqs. (4.1)–(4.4). In four dimensions their basis contains the parity-even local operators contributing to tree-level four-graviton scattering through dimension 12. The calculation below uses the ten first-order Wilson directions visible around the EH point:

`theta_C5=(c3,c_plus,c_minus,e_plus,e_minus,f_plus,f_minus,g_plus,g_minus,j1)`.

`c_GB` does not contribute linearly to the quoted D=4 amplitude around the EH point in this convention.

## Frozen kinematics

For massless external gravitons `s+t+u=0`. Define

`x=st+tu+us`, `y=stu`.

The comparator is sampled at twelve finite points with `|s|,|t|,|u|<1` in cutoff units and several crossing-symmetric polarization phases `phi`. The exact list is stored in

`results/c5_tree_eft_tangent_iteration146.json`.

The analytic derivatives are those of the manifestly crossing-symmetric amplitude in arXiv:2212.04975 eq. (4.4), evaluated at vanishing Wilson coefficients. No numerical differentiation is used.

## Finite physical Wilson tangent

The resulting amplitude fingerprint matrix has shape

`12 x 10`.

SVD result:

- rank: **10/10**;
- singular values:
  `3.77624716e-1, 7.94667137e-2, 9.08015595e-3, 9.16415267e-4, 4.72836512e-4, 2.33370720e-5, 1.72727839e-5, 2.13079285e-6, 1.03238331e-6, 9.27010447e-7`;
- `s_min/s_max = 2.4548457953351053e-6`;
- standard floating SVD tolerance is far below the smallest singular value.

Thus the frozen finite kinematics resolves all ten declared local Wilson directions. This is the first **physical finite C5 tangent certificate** in the project, but only in the on-shell amplitude fingerprint space.

Reproducible authority:

- `analysis/c5_tree_eft_tangent_iteration146.py`;
- `results/c5_tree_eft_tangent_iteration146.json`.

## Why this is not yet the full Iteration-145 `V_C5`

The Iteration-145 reduced RQIR coordinates are

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

The matrix just computed is a derivative of an **on-shell scattering amplitude**. The RQIR object `chi^(2)R` is an ordered causal response built from nested commutators or an equivalent CTP/retarded vertex. These are related by the same underlying QFT, but they are not identical objects and cannot be equated without an explicit analytic-continuation/CTP prescription and state convention.

Therefore the following rows are not assigned zero:

- `N2`: **BLOCKED** — requires the declared CTP state and loop/influence-functional calculation;
- `C3sym`: **BLOCKED** — same reason;
- `chi2R_even/odd`: **BLOCKED** as a direct RQIR embedding until the retarded continuation of the selected vertex is derived;
- loop/nonanalytic columns: **BLOCKED** in the Iteration-145 coordinates.

Donoghue's gravitational EFT work emphasizes that the low-energy massless quantum effects are carried by nonlocal/nonanalytic terms. Those terms are therefore physically mandatory when the chosen perturbative order requires them; they cannot be silently absorbed into local Wilson coefficients or set to zero.

## NG-FUNNEL-006 — ON_SHELL_TANGENT_NOT_RQIR_TANGENT

A finite on-shell C5 amplitude tangent is not, by itself, a finite RQIR ordered-response tangent.

Consequences:

1. the local-EFT comparator is now concretely finite and rank-certified;
2. this does **not** yet certify the full C5 quotient in `z`;
3. unsupported CTP/loop rows remain `BLOCKED`, not zero;
4. no candidate residual, Fisher information or resource optimization is admissible yet.

This is an operational blocking result, not a consistency failure of perturbative quantum GR EFT.

## Literature anchors

- de Rham, Jaitly & Tolley, arXiv:2212.04975: explicit finite parity-even gravitational EFT operator basis and tree four-graviton amplitudes through dimension 12.
- Elvang, Jones & Naculich, arXiv:1611.07534: local EFT operators can alter the subsubleading graviton soft theorem while the subleading soft graviton theorem is unmodified in the analysed local EFT setting.
- Donoghue, arXiv:gr-qc/9405057: low-energy quantum gravity EFT and the physical importance of nonanalytic/nonlocal massless-loop terms.

## Next scientific gate

**Iteration 147 — retarded C5 embedding.**

Freeze one CTP state/prescription and derive a minimal retarded three-point/nonlinear-response sub-block from the same EH + local-EFT dynamics at the frozen finite kinematics. The first goal is not the whole eight-dimensional quotient: it is one explicitly normalized `chi2R` block plus its Ward/soft relation. Loop/nonanalytic columns may remain separately `BLOCKED` until derived, but may not be set to zero.

Only after this retarded C5 block exists should the project instantiate fixed C3 and nonlinear C4 tangents.
