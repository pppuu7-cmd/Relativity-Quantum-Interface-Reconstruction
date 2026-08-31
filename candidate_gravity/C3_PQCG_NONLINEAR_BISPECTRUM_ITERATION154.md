# Iteration 154 — nonlinear PQCG bispectrum tangent

**Date:** 2026-08-31  
**Comparator:** `C3-PQCG-NL-001`  
**Status:** `PASS_SCOPED_C3SYM / FULL_C3_BLOCKED`

## Result

The same covariant postquantum-classical gravity family used in Iteration 153 already contains a nonlinear pure-gravity Onsager–Machlup action

`S[g]=1/2 int sqrt(-g) [alpha R_mn R^mn - beta R^2]`.

No new noise kernel or phenomenological cubic coupling is introduced.

On the six frozen Iteration-149 TT probes:

- `R^2` has an analytic zero cubic TT coefficient because `R^(1)=0` on every TT leg;
- `R_mn R^mn` has a nonzero cubic coefficient;
- the resulting connected classical third cumulant is nonzero.

Matching the quadratic covariance to `D2,D0` gives

`D2=1/(2 alpha)`, `D0=1/[8(alpha-3 beta)]`.

The two supported observable coordinates are

`N2=A(5D2+D0)`,

`C3sym_TT=B D2^2`,

with

`A=258.83104475297773`,

`B=-617.4340282011477`.

Therefore

`V_C3 = [[5A,A],[2 B D2,0]]`

and

`det(V_C3)=-2 A B D2`.

For every physical `D2>0`, the supported tangent is exactly rank `2/2`.

A normalized `D2=1` conditioning diagnostic gives singular values

`[1798.6530445678386,177.70085794811004]`,

`smin/smax=0.0987966292247353`.

## Numerical regression

Six direct unreduced `alpha=1` cubic coefficients:

`[0.13859380655232462,0.10545702593041664,0.3612771529305377,0.1435006301577732,-0.0938503383460591,0.011015086130857252]`.

The largest Richardson-extrapolated numerical `R^2` cubic residual is

`7.19528079232966e-11`.

Step-halving convergence differs from the expected `1/4` factor by at most `1.86e-5` for the Ricci-squared coefficient and `1.63e-5` for the vanishing `R^2` regression.

## Retained scientific results

### `C3-NG-002`

`NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`.

The single `N2` coordinate of Iteration 153 identified only `5D2+D0`. The additional classical symmetric third cumulant distinguishes the spin-2 diffusion direction, lifting the supported tangent to rank 2/2.

### `NG-FUNNEL-012`

`CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`.

A nonzero gravitational third cumulant and increased post-Gaussian rank are not sufficient evidence for quantum spacetime: a concrete covariant classical stochastic gravity comparator generates both from its own nonlinear action.

## Scope guard

This does **not** complete C3.

Still blocked:

- ordered `chi2R_even/odd` from the same stochastic dynamics;
- non-TT tensor/geometric completion;
- `soft2` map;
- threshold coordinate;
- full C3 quotient.

No unsupported row is zero-filled. No Fisher/resource work is permitted. `ANSATZ-003` remains not created.

## Literature anchors

- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`.
- Oppenheim & Sajjad, arXiv:`2605.05375`.
- Grudka et al., arXiv:`2402.17844`.

## Reproducibility

- `analysis/c3_pqcg_nonlinear_bispectrum_iteration154.py`
- `results/c3_pqcg_nonlinear_bispectrum_iteration154.json`
- `candidate_gravity/comparators/C3-PQCG-NL-001.md`
