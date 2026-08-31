# RQIR Research Log — Iteration 154

**Date:** 2026-08-31  
**Branch:** Candidate Gravity comparator funnel  
**Comparator:** `C3-PQCG-NL-001`

## Starting point

Iteration 153 instantiated the first fixed C3 comparator but only in the linear stochastic sector. Its supported `(N2,chi1R)` tangent for `(D2,D0)` had rank `1/2`, because the one scalar noise coordinate measured only `5D2+D0`. All post-Gaussian rows were correctly left BLOCKED.

Iteration 154 asked whether a nonlinear C3 row could be derived from the **same published covariant classical-quantum dynamics**, rather than inserted phenomenologically.

## Literature audit

The 2026 covariant CQ gravity framework gives a path integral whose Onsager–Machlup part is the Einstein equation squared with a local diffusion matrix. The 2026 stochastic-mode paper writes the pure-gravity probability action as

`S[g]=1/2 int sqrt(-g) [alpha R_mn R^mn - beta R^2]`.

It also gives the flat-background two-point decomposition, from which the Iteration-153 convention implies

`D2=1/(2 alpha)`,

`D0=1/[8(alpha-3 beta)]`.

Anchors:

- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`;
- Oppenheim & Sajjad, arXiv:`2605.05375`;
- Grudka et al., arXiv:`2402.17844`.

## Derivation

For a classical stochastic probability functional

`S=S2+S3+...`,

with Gaussian covariance `C=K^{-1}`, the leading connected three-point function is

`<h1 h2 h3>_c = -C1 C2 C3 Gamma3`.

Since the metric is classical, this is already the fully symmetrized third cumulant required by the RQIR `C3sym` row.

The same six TT triplets, projectors, deterministic polarizations and Gaussian windows from Iteration 149 were retained.

For every TT leg, `R^(1)=0`. Consequently `R^2` has no cubic TT coefficient. The Ricci-squared operator does have a nonzero cubic coefficient.

The unreduced curvature action was evaluated directly from the metric, its first derivatives and second derivatives. No on-shell EOM reduction was imported.

## Numerical result

Six `alpha=1` Ricci-squared cubic coefficients:

`0.13859380655232462`,
`0.10545702593041664`,
`0.3612771529305377`,
`0.1435006301577732`,
`-0.0938503383460591`,
`0.011015086130857252`.

The analytically vanishing `R^2` cubic direction has maximum Richardson-extrapolated numerical residual

`7.19528079232966e-11`.

The mixed-derivative step-halving convergence follows the expected `O(d^2)` quarter scaling to about `2e-5` relative accuracy in the ratio diagnostic.

After the three propagators and window factors are included, the frozen aggregate TT cumulant is

`C3sym_TT = B D2^2`,

`B=-617.4340282011477`.

Iteration 153 already gave

`N2=A(5D2+D0)`,

`A=258.83104475297773`.

Thus

`V_C3 = [[5A,A],[2 B D2,0]]`.

Its determinant is

`det(V_C3)=-2 A B D2`.

For every physical `D2>0`, this is nonzero, so the supported nonlinear tangent is **rank 2/2**.

At a normalized `D2=1` conditioning point only, the SVD is

`[1798.6530445678386,177.70085794811004]`,

with `smin/smax=0.0987966292247353`.

The generic rank result does not depend on this arbitrary normalization.

## New retained scientific results

### `C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`

The linear one-coordinate noise protocol collapsed `(D2,D0)` to `5D2+D0`. A third cumulant derived from the same stochastic dynamics isolates the spin-2 diffusion direction and lifts the supported comparator rank from 1 to 2.

Classification: scoped identifiability improvement of the comparator, not new physics.

### `NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`

A nonzero symmetric gravitational bispectrum and increased post-Gaussian rank are not sufficient evidence for a quantum metric. A concrete covariant classical stochastic spacetime generates both from its own nonlinear Onsager–Machlup action.

This strengthens the earlier abstract `NG-FUNNEL-002` with a concrete fixed comparator calculation.

## Scope / blockers

The C3 comparator is still incomplete.

- `N2`: supported;
- `C3sym_TT`: supported, rank contribution established;
- `chi2R_even/odd`: BLOCKED_ORDERED_RESPONSE_COMPLETION;
- `soft2`: BLOCKED;
- `tensor_geo`: BLOCKED_NON_TT_COMPLETION;
- `threshold`: BLOCKED;
- full C3 quotient: BLOCKED.

No blocked row is assigned zero.

No Fisher/resource calculation is allowed and `ANSATZ-003` remains intentionally uncreated.

## Next scientific gate — Iteration 155

Try to derive the ordered second-order response from the same full CQ gravity realization:

1. start from the published stochastic Einstein/Onsager–Machlup dynamics rather than a new phenomenological kernel;
2. freeze the stochastic calculus/source-response convention required to define a causal second functional derivative;
3. determine whether the classical nonlinear drift gives a finite `chi2R_even/odd` prediction in the existing six-probe protocol and whether any diffusion-dependent correction is actually fixed by the published action;
4. do not assume `chi2R_odd=0` without derivation;
5. if the ordered map is under-specified by the published realization, record `BLOCKED_ORDERED_C3_SPECIFICATION` and move to the first fixed nonlinear C4 comparator;
6. keep C5 higher-local/loop sectors BLOCKED;
7. still no `ANSATZ-003` until a residual survives fixed comparator subtraction.
