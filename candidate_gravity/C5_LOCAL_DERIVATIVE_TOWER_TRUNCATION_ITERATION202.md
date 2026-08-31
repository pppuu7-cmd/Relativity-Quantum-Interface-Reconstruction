# Candidate Gravity — Iteration 202: local C5 derivative-tower truncation audit

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**  
**Change:** 24% → 23% because one previously credited comparator-foundation point is reopened.

## Why this audit was necessary

Iterations 178–201 treated the zero-`K2` local C5 soft2 nuisance through the frozen dimension-12 cutoff,

`V4 = Riemann3_soft2 * {1,-x,x^2,-x^3}`,

with rank `4/12` on each frozen v3 polarization protocol.

That rank-four result is correct **within the declared truncation**. The present question is stronger:

> Is the remaining finite-dimensional complement a model-independent C5 residual space if higher local gravitational EFT operators are not bounded?

## Arbitrary derivative descendant

Iteration 178 explicitly established for `n=1,2,3`

`B_T[RiemannChain Box^n] = (2/3)(-q^2)^n B_T[Riemann^3]`.

The same cubic flat-background argument is independent of `n`.

Take the local covariant family schematically

`O_n = R_mn^{  rs} R_rs^{  ab} Box^n R_ab^{  mn}`.

At `O(h^3)` each curvature is linearized and the flat `Box^n` acts on one external curvature. Functional differentiation symmetrizes over the three legs.

For the physical null soft leg:

`k_soft^2 = 0`.

Thus terms with `Box^n` on the soft leg vanish for every `n>=1`. On either hard momentum eigenmode `q` or `-q` the flat box supplies `(-q^2)^n`. Four of the six leg permutations survive, giving

`v_0(i)=r_i`,

`v_n(i)=(2/3) r_i (-x_i)^n`, `n>=1`,

where `r_i` is the frozen `Riemann^3` soft2 carrier and `x_i=q_i^2` in the project convention.

This extends the exact Iteration-178 identity to arbitrary integer `n>=1` for this declared operator family.

## Finite-row rank theorem

For `N` frozen rows, define the first `N` columns `n=0,...,N-1`.

Apart from nonzero column factors, the matrix is

`diag(r_i) * Vandermonde(-x_i)`.

Therefore

`det V_N = (prod_i r_i) (2/3)^(N-1) prod_{i<j}[(-x_j)-(-x_i)]`.

If the hard nodes are distinct and all carriers are nonzero,

`rank(V_N)=N` exactly.

Both v3-A and v3-B satisfy these hypotheses on all twelve rows.

100-digit determinant certificates for the twelve-column tower are

- v3-A: `3.6219999948776965700299598809683147035e-56`;
- v3-B: `-3.2101534944510024202218188366614935333e-54`.

They are nonzero. Double precision eventually reports rank 11 because the Vandermonde problem becomes extremely ill-conditioned; this is numerical near-degeneracy, not an exact loss of rank.

Already the first omitted descendant changes the finite span:

- dimension 12 (`n<=3`): rank 4;
- dimension 14 (`n<=4`): rank 5;
- dimension 16 (`n<=5`): rank 6;
- ...;
- through `n=11` (dimension 28): exact rank 12.

## Why the current v3 range does not justify dropping the tower by power counting alone

The hard nodes span

`x in [0.184448, 0.994896]`.

At the largest node,

- `x^4 = 0.97974`;
- `x^8 = 0.95989`;
- `x^11 = 0.94527`.

Thus, absent an explicit Wilson-coefficient/remainder bound, higher derivative powers are not parametrically suppressed on the full current v3 range.

This matches the standard gravitational EFT logic: the local action admits an all-orders tower of higher-dimension operators, while predictive truncation requires a low-energy expansion and a declared accuracy/power-counting regime. Donoghue's EFT treatment separates controlled low-energy/nonanalytic effects from unknown short-distance local contributions. Ruhdorfer–Serra–Weiler construct non-redundant gravitational EFT operator bases of arbitrary dimension and emphasize that the construction extends systematically to all orders.

Literature anchors:

- J. F. Donoghue, Phys. Rev. D 50, 3874 (1994), arXiv:gr-qc/9405057;
- M. Ruhdorfer, J. Serra, A. Weiler, JHEP 05 (2020) 083, arXiv:1908.08050.

## Scope / redundancy caveat

This iteration does **not** claim that every written `O_n` representative is an independent element of every possible nonredundant four-dimensional EFT basis after all integrations by parts, Bianchi identities and EOM/field redefinitions.

The retained statement is narrower and sufficient for the RQIR gate:

1. the already-used Riemann-chain local analytic family has an arbitrary-derivative continuation at the cubic flat-background level;
2. its projected finite-row images generate successive hard-momentum powers;
3. general gravitational EFT contains independent higher-dimension local operators to arbitrary order;
4. therefore a finite residual may not be called model-independent merely because operators above dimension 12 were omitted, unless the truncation and its remainder are physically bounded.

Off-shell/source-completed RQIR observables also require the project’s existing field-redefinition/source-contact discipline; no on-shell EOM elimination is silently used here.

## Retained results

### `C5-NG-019 — LOCAL_RIEMANN_CUBIC_DERIVATIVE_TOWER_CAN_SATURATE_ANY_FINITE_NULLSOFT_ROW_SET_WITH_DISTINCT_HARD_NODES`

For the declared analytic Riemann-chain derivative family, the first `N` powers span an `N`-row null-soft protocol when the hard nodes are distinct and the base carrier is nonzero.

### `REL-NG-015 — DIMENSION12_RANK4_COMPLEMENT_IS_NOT_A_MODEL_INDEPENDENT_C5_RESIDUAL_SPACE_WITHOUT_EFT_REMAINDER_CONTROL`

The previous rank-four C5 result remains valid only as a dimension-12 scoped comparator result.

### `NG-FUNNEL-057 — FINITE_ANALYTIC_SOFT2_NOVELTY_REQUIRES_CONTROLLED_EFT_TRUNCATION_OR_A_NONINTERPOLABLE_LINKED_OBSERVABLE`

A candidate cannot earn novelty points from a finite analytic soft2 complement until omitted local EFT contributions are bounded or the witness is moved to a structure not reproducible by arbitrary local analytic interpolation.

### `READINESS-CORR-001 — C5_TRUNCATION_BLOCKER_REOPENS_ONE_COMPARATOR_FOUNDATION_POINT`

Comparator foundation is revised from `24/25` to `23/25`; total model readiness becomes **23%**.

## Important cross-polarization nuance

The saturation theorem above applies to each 12-row polarization protocol separately if its C5 coefficients are allowed to fit that protocol.

Physical Wilson coefficients must, however, be common across v3-A and v3-B. The same one-family derivative tower therefore has only twelve coefficient directions on the vertically stacked 24-row A+B observable, not twenty-four.

This does not restore a novelty certificate — the full all-orders C5 tensor basis contains further structures — but it makes the shared-coefficient cross-polarization quotient the correct next finite test.

## Readiness

`MODEL_READINESS: 23%`.

Breakdown:

- comparator foundation `23/25`;
- robust unique residual `0/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

No `ANSATZ-003`. No Fisher. No resource optimization.

## Next gate

Iteration 203: construct the **shared-Wilson cross-polarization derivative-tower quotient** on frozen v3-A + v3-B. Quantify what the single Riemann-chain tower can and cannot absorb when identical C5 coefficients must explain both polarization protocols. Keep the broader all-orders tensor EFT remainder explicitly open; do not promote any leftover direction until that remainder is controlled.
