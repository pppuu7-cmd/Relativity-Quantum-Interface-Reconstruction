# Recovery Delta — RQIR Iteration 154

**Date:** 2026-08-31  
**Authoritative change:** first concrete nonlinear C3 symmetric-cumulant tangent derived from the same published postquantum-classical gravity action; the Iteration-153 linear diffusion degeneracy is lifted in the supported `(N2,C3sym_TT)` subspace.

## Previous front

Iteration 153 instantiated `C3-PQCG-LIN-001` with parameter vector `(D2,D0)` and supported rows `(N2,chi1R)`. One scalar `N2` coordinate measured only `5D2+D0`, giving rank `1/2`. All post-Gaussian rows remained BLOCKED.

## New comparator extension

`C3-PQCG-NL-001` uses the same covariant classical-quantum gravity family, with published pure-gravity Onsager–Machlup action

`S[g]=1/2 int sqrt(-g) [alpha R_mn R^mn - beta R^2]`.

Quadratic covariance matching gives

`D2=1/(2 alpha)`,

`D0=1/[8(alpha-3 beta)]`.

No new phenomenological cubic or noise kernel was added.

## New supported post-Gaussian row

On the six frozen TT probes:

- `R^(1)=0` on every leg;
- therefore the `R^2` cubic TT coefficient is analytically zero;
- `R_mn R^mn` has nonzero cubic coefficients;
- the classical stochastic metric therefore has a nonzero connected fully symmetric third cumulant.

Aggregate finite observable:

`C3sym_TT=B D2^2`,

with

`B=-617.4340282011477`.

Retained Iteration-153 noise coordinate:

`N2=A(5D2+D0)`,

`A=258.83104475297773`.

Therefore

`V_C3=[[5A,A],[2 B D2,0]]`,

`det(V_C3)=-2 A B D2`.

For every physical `D2>0`, the supported tangent has rank **2/2**.

Normalized `D2=1` SVD diagnostic:

`[1798.6530445678386,177.70085794811004]`,

`smin/smax=0.0987966292247353`.

## Numerical certificate

Six Ricci-squared cubic coefficients at `alpha=1`:

`[0.13859380655232462,0.10545702593041664,0.3612771529305377,0.1435006301577732,-0.0938503383460591,0.011015086130857252]`.

Maximum Richardson-extrapolated numerical residual for the analytically vanishing `R^2` cubic TT direction:

`7.19528079232966e-11`.

## New retained results

### `C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`

Adding a third symmetric cumulant derived from the same stochastic dynamics lifts the supported `(D2,D0)` tangent from rank 1 to rank 2.

This is an identifiability improvement for the comparator, not a consistency or novelty claim.

### `NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`

A nonzero gravitational symmetric bispectrum, even one that increases finite-rank identifiability, is not evidence by itself for quantum spacetime. The fixed covariant classical stochastic PQCG comparator generates it from its own nonlinear Onsager–Machlup action.

## Scope guard

Supported:

- `N2`;
- `C3sym_TT`.

Still BLOCKED:

- `chi2R_even/odd` ordered nonlinear response;
- non-TT tensor/geometric completion;
- `soft2`;
- threshold coordinate;
- full C3 quotient.

Blocked rows are not zeros.

`ANSATZ-003`: **NOT_CREATED**.  
Fisher/resources: **FORBIDDEN**.

## New files

- `analysis/c3_pqcg_nonlinear_bispectrum_iteration154.py`
- `results/c3_pqcg_nonlinear_bispectrum_iteration154.json`
- `candidate_gravity/comparators/C3-PQCG-NL-001.md`
- `candidate_gravity/C3_PQCG_NONLINEAR_BISPECTRUM_ITERATION154.md`
- `research_log/2026-08-31_iteration_154_c3_pqcg_nonlinear_bispectrum.md`
- `recovery/RECOVERY_DELTA_ITERATION_154.md`

## Literature anchors

- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`.
- Oppenheim & Sajjad, arXiv:`2605.05375`.
- Grudka et al., arXiv:`2402.17844`.

## Exact restart instruction — Iteration 155

Attempt the ordered nonlinear C3 response from the same published CQ gravity dynamics.

1. derive the causal second functional response from the stochastic Einstein / Onsager–Machlup formulation;
2. freeze any required stochastic-calculus and source-response convention explicitly;
3. map to the existing `chi2R_even/odd` finite protocol;
4. do not set the odd component to zero by classical intuition alone;
5. if the published realization does not uniquely fix the required ordered map, record `BLOCKED_ORDERED_C3_SPECIFICATION` and move to the first fixed nonlinear C4 comparator;
6. retain higher C5 local and loop/nonanalytic rows as BLOCKED;
7. no Fisher/resources and no `ANSATZ-003` until a nonzero residual survives fixed comparator quotienting.
