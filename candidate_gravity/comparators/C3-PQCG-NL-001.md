# C3-PQCG-NL-001 — nonlinear postquantum-classical gravity comparator

**Iteration:** 154  
**Status:** SCOPED / PARTIAL COMPARATOR  
**Parent family:** covariant classical-quantum path-integral gravity of Oppenheim–Weller-Davies and the stochastic-mode analysis of Oppenheim–Sajjad.

## Purpose

Extend `C3-PQCG-LIN-001` beyond the Gaussian two-point layer without inventing a new stochastic kernel. The extension must come from the same published covariant classical-quantum gravity dynamics.

## Frozen parent dynamics

The gravitational classical-quantum path integral contains an Onsager–Machlup factor built from the Einstein equation,

`(G_mn + Lambda g_mn - 8 pi G_N Tbar_mn) D2^{-1 mn,rho sigma} (G_rho sigma + Lambda g_rho sigma - 8 pi G_N Tbar_rho sigma)`.

For the local generalized-DeWitt diffusion choice, the pure-gravity probability action is

`S[g] = 1/2 int d4x sqrt(-g) [alpha R_mn R^mn - beta R^2]`.

This is not introduced by RQIR; it is the published C3 comparator dynamics.

Literature anchors:

- J. Oppenheim and Z. Weller-Davies, **Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time**, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`.
- J. Oppenheim and M. Sajjad, **Stochastic modes in postquantum classical gravity**, arXiv:`2605.05375` (2026).
- A. Grudka, T. R. Morris, J. Oppenheim, A. Russo, M. Sajjad, **Renormalisation of postquantum-classical gravity**, arXiv:`2402.17844`.

## Parameter convention

Matching the quadratic pure-gravity covariance to the Iteration-153 stochastic mode convention gives

`2 D2 / (k^2)^2 = 1/[alpha (k^2)^2]`,

`2 D0 / (k^2)^2 = 1/[4(alpha-3 beta)(k^2)^2]`.

Therefore

`D2 = 1/(2 alpha)`,

`D0 = 1/[8(alpha-3 beta)]`.

The physical stochastic interior has `D2>0`, `D0>0` in this scoped parameterization.

## Frozen finite protocol

Use exactly the six Iteration-149 spacelike momentum triplets, Gaussian windows `(tau,L)=(0.8,0.6)`, and deterministic TT projectors/polarizations already used for the C5 off-shell comparison.

The supported C3 rows in Iteration 154 are

- `N2`;
- one fully symmetrized connected TT third-cumulant coordinate `C3sym_TT`, obtained by summing the six windowed connected three-point values.

Unsupported rows are not set to zero.

## Tree classical bispectrum

For a classical probability action

`S = S2 + S3 + ...`,

with covariance `C=K^{-1}`, the leading connected three-point function is

`<h1 h2 h3>_c = - C1 C2 C3 Gamma3`.

Because the metric is classical, this connected three-point function is already fully symmetrized.

On the frozen TT probes, the linearized Ricci scalar vanishes on every leg. Therefore the `R^2` part has no cubic TT coefficient:

`Gamma3_R2(TT,TT,TT)=0`.

The `R_mn R^mn` direction is nonzero.

Direct unreduced curvature evaluation gives the six `alpha=1` cubic coefficients

`[0.13859380655232462, 0.10545702593041664, 0.3612771529305377, 0.1435006301577732, -0.0938503383460591, 0.011015086130857252]`.

The numerical `R^2` Richardson-extrapolated residual is at most

`7.19528079232966e-11`,

while the raw value falls by the expected factor `~1/4` under step halving, supporting the analytic cubic zero.

## Finite observable map

Iteration 153 gave

`N2 = A (5 D2 + D0)`

with

`A = 258.83104475297773`.

For the nonlinear TT cumulant, using `alpha=1/(2D2)` and three stochastic propagators gives

`C3sym_TT = B D2^2`,

with

`B = -617.4340282011477`.

Thus the supported tangent is

`V_C3 = d(N2,C3sym_TT)/d(D2,D0)`

`      = [[5A, A], [2 B D2, 0]]`.

Its determinant is

`det(V_C3) = -2 A B D2`.

Since `A>0`, `B!=0`, and the physical stochastic interior has `D2>0`,

**the supported nonlinear tangent has rank 2/2 for every physical `D2>0`.**

At the normalized conditioning point `D2=1`, the numerical matrix is

`[[1294.1552237648887, 258.83104475297773], [-1234.8680564022955, 0]]`,

with singular values

`[1798.6530445678386, 177.70085794811004]`

and `smin/smax=0.0987966292247353`.

The normalized point is only a conditioning diagnostic; the rank statement above is analytic and generic for `D2>0`.

## Scientific interpretation

### C3-NG-001 retained

With `N2` alone, two diffusion parameters collapse to the combination `5D2+D0`.

### C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY

Adding a third symmetric cumulant derived from the same covariant stochastic action separates the spin-2 diffusion direction from the scalar diffusion contribution and raises the supported `(N2,C3sym_TT)` tangent from rank `1` to rank `2`.

This is a **positive comparator result**, not a new-gravity result.

### NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK

A nonzero symmetric gravitational bispectrum, even one that increases finite-rank identifiability, is not by itself evidence that spacetime is quantum. A concrete classical stochastic spacetime model generates such a bispectrum from its own covariant nonlinear Onsager–Machlup action.

## Remaining blockers

`chi2R_even/odd`: **BLOCKED_ORDERED_RESPONSE_COMPLETION**.  
`soft2`: **BLOCKED**.  
`tensor_geo`: **BLOCKED_NON_TT_COMPLETION**.  
`threshold`: **BLOCKED**.  
Full nonlinear C3 quotient: **BLOCKED**.

Do not infer zero values for these rows.

## Authority

- `analysis/c3_pqcg_nonlinear_bispectrum_iteration154.py`
- `results/c3_pqcg_nonlinear_bispectrum_iteration154.json`

## Next gate

Attempt to derive the ordered second-order response from the same full CQ/Onsager–Machlup dynamics without introducing an independent phenomenological kernel. If that map requires an unstated stochastic-calculus/source convention not fixed by the published realization, record the row as blocked and proceed to a fixed nonlinear C4 comparator rather than fabricating it.
